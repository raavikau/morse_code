morse_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '.': '.-.-.-', ',': '--..--',
    '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...',
    ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.',
    '$': '...-..-', '@': '.--.-.', ' ': '/'
}
def to_morse_code(string_message):
    morse_code = ''
    for char in string_message.upper():
        if char in morse_dict:
            morse_code += morse_dict[char] + ' '
    return morse_code

def from_morse_code(morse_code):
    string_message = ''
    for char in morse_code.split():
        for ch, value in morse_dict.items():
            if value == char:
                string_message += ch
    return string_message

while True:
    user_choice = input('Choose an option 1: Convert string to morse, 2: Convert morse to string and 0: to quit \n')
    if user_choice == '1':
        message = input('Enter your message want to convert to morse: ')
        encrypt_message = to_morse_code(message)
        print(encrypt_message)
    elif user_choice == '2':
        morse_message = input('Enter your morse message want to convert to string: ')
        decrypt_message = from_morse_code(morse_message)
        print(decrypt_message)
    elif user_choice == '0':
        print('quit successfully')
        break
    else:
        print('invalid input')
