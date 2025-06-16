alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



#Alternative way of combining functions

def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    if encode_or_decode == 'decode':
        shift_amount *= -1

    for letter in original_text:  

        if letter not in original_text:
            output_text += letter
        else:
                
            shift_position = alphabet.index(letter)+shift_amount

            #to fix shift z forward by 9
            shift_position %= len(alphabet) #0->25
            output_text += alphabet[shift_position]

    print(f"Here is the {encode_or_decode}d result: {output_text}")

#To restart cipher program
should_continue = True

while should_continue:

    direction = input("Type 'encode' to encrypt. type 'decode' to decrypt\n")
    text = input("Type your message: \n").lower()
    shift = int(input("Type the shift number: \n"))

    caesar(original_text=text, shift_amount= shift, encode_or_decode=direction)

    restart = input("Type 'yes' if you want to go again otherwise, type 'no'.\n").lower()

    if restart == 'no':
        should_continue = False
        print("Goodbye")