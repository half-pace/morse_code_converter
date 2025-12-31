#morse code converter

#define the function 
def morse(message, choice):
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
    }
    
    #reversing the above dictionary for morse - text conversion
    morse_dict = {value: key for key, value in eng_code.items()}
    
    #choice based trigger
    if choice == 1:
        #encoding block
        #formats the message received from the user
        formatted_message = message.upper().strip()
        converted_message = "" #to store the resultant morse translation
        
        #main encoding loop
        for each_word in formatted_message:
            if each_word in eng_code:
                converted_message += eng_code[each_word]
                converted_message += " " #to add 1 space between each letter of a single word for every word
            elif each_word == " ": 
                converted_message += " / " #if there's space between words we will add / to separate words
            else:
                print("Invalid Character Used!")
                break
        
        return converted_message.strip()
    else:
        #decoding block
        formatted_code = message.strip().split(" / ")
        converted_code = "" #final output
        decoded_word = "" #to store each decoded letters 