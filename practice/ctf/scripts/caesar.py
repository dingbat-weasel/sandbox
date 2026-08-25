def caesar_encrypt(text: str, shift: int) -> str:
    result = ""

    for i in range(len(text)):
        # Obtain ASCII value using ord
        char_position = ord(text[i])
        
        # Subtract 97 to have char from 1-26
        char_position = char_position - 97

        new_char_position = char_position + shift

        # Wrap alph
        new_char_position = new_char_position % 26

        # Convert back to ASCII
        new_char_position = new_char_position + 97

        # Convert ASCII val to char and concatenate
        result = result + chr(new_char_position)

    print(result)
    return result

def caesar_decrypt(cipher_text: str, shift: int) -> str:
    result = ""

    # Go through each character of the text in this loop
    for i in range(len(cipher_text)):
        # Obtain ASCII from ord
        char_position = ord(cipher_text[i])
        # Subtract 97 for chars 1-26
        char_position = char_position - 97
        # Subtract shift
        new_char_position = char_position - shift
        # Make sure new position does not pass 26
        new_char_position = new_char_position % 26
        #Convert back to ascii
        new_char_position = new_char_position + 97
        # Convert ascii val to char and concatenate
        result = result + chr(new_char_position)
    print(result)
    return(result)
