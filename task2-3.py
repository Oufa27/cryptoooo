import string

def generate_playfair_matrix(keyword):
    # Remove duplicates and combine the keyword with the alphabet
    alphabet = string.ascii_lowercase.replace('j', '')  # 'j' is traditionally merged with 'i'
    matrix = []
    keyword = ''.join(dict.fromkeys(keyword))  # Remove duplicate characters in keyword
    keyword += ''.join([ch for ch in alphabet if ch not in keyword])  # Append remaining letters
    return [keyword[i:i + 5] for i in range(0, len(keyword), 5)]

def find_position(matrix, char):
    for i, row in enumerate(matrix):
        if char in row:
            return i, row.index(char)
    return None

def decrypt_playfair(message, matrix):
    message = message.replace('j', 'i')  # Replace 'j' with 'i' if present

    # Prepare the digraphs
    digraphs = []
    i = 0
    while i < len(message):
        if i + 1 < len(message) and message[i] == message[i + 1]:
            digraphs.append(message[i] + 'x')  # If two consecutive same letters, add 'x'
            i += 1
        else:
            digraphs.append(message[i:i + 2])
            i += 2

    decrypted_message = ""
    for pair in digraphs:
        row1, col1 = find_position(matrix, pair[0])
        row2, col2 = find_position(matrix, pair[1])

        if row1 == row2:
            decrypted_message += matrix[row1][(col1 - 1) % 5]
            decrypted_message += matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:
            decrypted_message += matrix[(row1 - 1) % 5][col1]
            decrypted_message += matrix[(row2 - 1) % 5][col2]
        else:
            decrypted_message += matrix[row1][col2]
            decrypted_message += matrix[row2][col1]
    
    # Clean up the message by removing the 'x' added for double letters
    decrypted_message = decrypted_message.replace('x', '')
    
    return decrypted_message

if _name_ == "_main_":
    keyword = input("Enter the keyword for Playfair cipher: ").lower()
    matrix = generate_playfair_matrix(keyword)
    print("\nPlayfair Matrix:")
    for row in matrix:
        print(" ".join(row))

    action = input("\nWould you like to encrypt or decrypt? (e/d): ").lower()
    text = input("Enter the message: ").lower()

    if action == 'd':
        decrypted_message = decrypt_playfair(text, matrix)
        print(f"\nDecrypted message: {decrypted_message}")
    else:
        print("Encryption functionality is not yet implemented.")