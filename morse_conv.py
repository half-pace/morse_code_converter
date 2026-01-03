#morse code converter
import re 

#define the function 
def morse(message, code):
    eng_code = {
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--..",
        "0": "-----",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----.",
        ".": ".-.-.-",
        ",": "--..--",
        "?": "..--..",
        "'": ".----.",
        "!": "-.-.--",
        "/": "-..-.",
        "(": "-.--.",
        ")": "-.--.-",
        "&": ".-...",
        ":": "---...",
        ";": "-.-.-.",
        "=": "-...-",
        "+": ".-.-.",
        "-": "-....-",
        "_": "..--.-",
        "\"\"" : ".-..-.",
        "$": "...-..-",
        "@": ".--.-.",
        "¿": "..-.-",
        "¡": "--...-"
    }
    
    #reversing the above dictionary for morse - text conversion
    morse_dict = {value: key for key, value in eng_code.items()}
    
    #choice based trigger
    if code == 1:
        #encoding block
        #formats the message received from the user
        formatted_message = message.upper().strip() #uppercases the message then strips whitespaces before and after the message
        converted_message = "" #to store the resultant morse translation
        
        #main encoding loop
        for each_word in formatted_message:
            if each_word in eng_code:
                converted_message += eng_code[each_word]
                converted_message += " " #to add 1 space between each letter of a single word for every word
            elif each_word == " ": 
                converted_message += " / " #if there's space between words we will add / to separate words
            else:
                print(f"Invalid Character Used: {each_word}")
                return "Invalid Character"
                break
        
        return converted_message.strip()
    else:
        #decoding block
        formatted_code = message.strip().split(" / ") #strips whitespaces and splits each word wiith / 
        converted_code = "" #final output
        decoded_word = "" #to store each decoded letters 
        
        #decoding loop
        for words in formatted_code:
            formatted_letters = words.split()
            for letters in formatted_letters:
                if letters in morse_dict:
                    decoded_word += morse_dict[letters]
                else:
                    print("Invalid Morse Code!")
                    return "Invalid Morse"
                    break
            converted_code += decoded_word
            converted_code += " "
            decoded_word = "" #this clears and empties the string - mandatory because previous string is still contained here which may combined with the next word
            
        return converted_code.strip()
    
#user input
while True:
    print("--------------------------------------- Strict Input Rules ---------------------------------------")
    print(" For Morse to Text Conversion ")
    print(" Apply / after every word and apply single space after every letter in a word!")
    print(" Would you like to start the program? 1: Start 2: Exit")
    # print(" Enter type of conversion: 1: Text to morse 2: Morse to text 3: Exit")
    
    #need to add auto-detect method instead of asking user
    #add a toggle to either do timing based print or normal print
    #for CLI we auto detect but provide --timed and -help options
    
    user_choice = int(input("Enter choice of conversion: "))
    
    if user_choice == 1:
        user_message =  input("Enter your message/code: ")
        pattern = re.findall(r"\w+", user_message)
        
        if pattern:
            print("Initializing Text -> Morse!") #detects texts
            user_code = 1
            output = morse(user_message, user_code)    
            if output != "Invalid Character":
                print("The morse code is: ", output)
        else:
            print("Initializing Morse -> Text") #detects morse
            user_code = 2
            output = morse(user_message, user_code)
            if output != "Invalid Morse":
                print("The message for the morse code is: ", output)
    elif user_choice == 2:
        print("Exiting the program!")
        break
    else: 
        print("Invalid input! Choose between (1-2)")
    
    # if user_choice == 1:
    #     user_message = input("Enter your message: ")
    #     output = morse(user_message, user_choice)
    #     if output != "Invalid Character":
    #         print("The morse code is: ", output)
    #     else:
    #         continue
    # elif user_choice == 2:
    #     user_message = input("Enter your morse code: ")
    #     output = morse(user_message, user_choice)
    #     if output != "Invalid Morse":
    #         print("The message for the morse code is: ", output)
    # elif user_choice == 3:
    #     print("Exiting the program!")
    #     break
    # else:
    #     print("Invalid choice! Choose between 1-3")