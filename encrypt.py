import collections, math, os

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
crazy_chest = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '#', '$', '%', '&', '(', ')', '*', '+', '-', ' ', '{', '}', '[', ']']

wanna_protect_text = True

def caesar(text, shift):
    new_text = ''

    if direction[0] == 'd':
        shift = -shift
    
    for char in text:
        if char not in alphabet:
            new_text += char
            continue

        original_index = alphabet.index(char)
        new_index = original_index + shift
        
        if new_index >= len(alphabet):
            new_index %= len(alphabet)

        new_text += alphabet[new_index]

    return new_text

def clear_screen():
    os.system('cls')

# IMPLEMENT THE CACHE FEATURE
# index_cache = map()

# def hard_cypher(text):
#     return text

while wanna_protect_text:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    print(f"The new text is {caesar(text, shift)}")

    play_again = input('Do you want to play again?\n').lower()[0]

    if play_again == 'n':
        wanna_protect_text = False
    
    clear_screen()

print('Bye-bye')