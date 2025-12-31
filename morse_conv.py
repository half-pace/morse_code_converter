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
        converted_message = ""