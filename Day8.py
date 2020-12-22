alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    if char in alphabet:
      end_text += alphabet[alphabet.index(char)+shift_amount]
    else:
      end_text += char
  print(f"\nHere's the {cipher_direction}d result: {end_text}")

from Day8_art import logo
print (logo)
again = True
while again == True:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  shift = shift % len(alphabet)+1

  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
  redo = input("\nType 'yes' if you want to go again. Otherwise type 'no.\n").lower
  if redo != 'yes':
    again == False
