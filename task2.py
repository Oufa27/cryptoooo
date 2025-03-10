import numpy as np

def generate_playfair_matrix(keyword):
    keyword = keyword.upper().replace("J", "I")
    seen = set()
    matrix = []
    
    for char in keyword:
        if char not in seen and char.isalpha():
            seen.add(char)
            matrix.append(char)
    
    for char in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if char not in seen:
            seen.add(char)
            matrix.append(char)
    
    return np.array(matrix).reshape(5, 5)

def find_positions(matrix, letter):
    row, col = np.where(matrix == letter)
    return row[0], col[0]

def process_pairs(text):
    text = text.upper().replace("J", "I")
    text = ''.join(filter(str.isalpha, text))
    
    pairs = []
    i = 0
    while i < len(text):
        a = text[i]
        if i + 1 < len(text) and text[i] != text[i + 1]:
            b = text[i + 1]
            i += 2
        else:
            b = 'X'
            i += 1
        pairs.append((a, b))
    return pairs

def playfair_encrypt_decrypt(text, matrix, mode='encrypt'):
    pairs = process_pairs(text)
    result = []
    
    for a, b in pairs:
        row1, col1 = find_positions(matrix, a)
        row2, col2 = find_positions(matrix, b)
        
        if row1 == row2:
            col1 = (col1 + 1) % 5 if mode == 'encrypt' else (col1 - 1) % 5
            col2 = (col2 + 1) % 5 if mode == 'encrypt' else (col2 - 1) % 5
        elif col1 == col2:
            row1 = (row1 + 1) % 5 if mode == 'encrypt' else (row1 - 1) % 5
            row2 = (row2 + 1) % 5 if mode == 'encrypt' else (row2 - 1) % 5
        else:
            col1, col2 = col2, col1
        
        result.append(matrix[row1, col1])
        result.append(matrix[row2, col2])
    
    return ''.join(result)

def main():
    keyword = input("Enter keyword: ")
    matrix = generate_playfair_matrix(keyword)
    print("Playfair Matrix:")
    print(matrix)
    
    choice = input("Do you want to encrypt or decrypt? (e/d): ").strip().lower()
    text = input("Enter text: ")
    
    if choice == 'e':
        result = playfair_encrypt_decrypt(text, matrix, mode='encrypt')
        print("Encrypted text:", result)
    elif choice == 'd':
        result = playfair_encrypt_decrypt(text, matrix, mode='decrypt')
        print("Decrypted text:", result)
    else:
        print("Invalid choice.")

if name == "main":
    main()