alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt. type 'decode' to decrypt\n")
text = input("Type your message: \n").lower()
shift = int(input("Type the shift number: \n"))

#function to create encode and shift 2 inputs

def encrypt(original_text, shift_amount):
    cipher_text = ""

    for letter in original_text:  
        shift_position = alphabet.index(letter)+shift_amount

        #to fix shift z forward by 9
        shift_position %= len(alphabet) #0->25
        cipher_text += alphabet[shift_position]

    print(f"Here is the encoded result: {cipher_text}")

#encrypt(original_text =text, shift_amount=shift)

#function to create decode and shift 2 inputs

def decrypt(original_text, shift_amount):
    casesar_text = ""

    for letter in original_text:
        shift_position = alphabet.index(letter) - shift_amount
        shift_position %= len(alphabet)
        casesar_text += alphabet[shift_position]

    print(f"Here is the decrypted result: {casesar_text}")

#decrypt(original_text = text, shift_amount = shift)




# Combining encrypt() and decrypt() functions into one 

def caesar():
    if direction == 'encrypt':
        encrypt(original_text =text, shift_amount=shift)
    else:
        decrypt(original_text = text, shift_amount = shift)

caesar()





