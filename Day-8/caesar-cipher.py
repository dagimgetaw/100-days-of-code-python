import art

print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()
    text = input("Type your message: ").lower()
    shift = int(input("Type the shift number: "))

    def encrypt(text, shift):
        encrypted_text = ""
        length = len(alphabet)
        for i in text:
            if i == " ":
                encrypted_text += " "
            else:
                position = alphabet.index(i)
                new_position = position + shift

                if new_position >= length:
                    value = new_position - length
                    new_letter = alphabet[value]
                    encrypted_text += new_letter
                else:
                    new_letter = alphabet[new_position]
                    encrypted_text += new_letter
        print(f"The encoded text is {encrypted_text}")

    def decrypt(text, shift):
        decrypted_text = ""
        for i in text:
            if i == " ":
                decrypted_text += " "
            else:
                position = alphabet.index(i)
                new_position = position - shift
                new_letter = alphabet[new_position]
                decrypted_text += new_letter
        print(f"The decoded text is {decrypted_text}")


    if direction == 'encode':
        encrypt(text=text, shift=shift)
    elif direction == 'decode':
        decrypt(text=text, shift=shift)
    else:
        print("Enter valid word 'encode' or 'decode'.")
        
caesar()
q = input("do u want to continue 'yes' or 'no': ").lower()

while(q == 'yes'):
    caesar()
    q = input("do u want to continue 'yes' or 'no': ").lower()