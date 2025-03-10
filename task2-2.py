import itertools
import string

def decrypt(text, key):
    alphabet = string.ascii_uppercase
    key_map = str.maketrans("".join(key), alphabet)
    return text.translate(key_map)

def brute_force_monoalphabetic(ciphertext):
    alphabet = string.ascii_uppercase
    possible_keys = itertools.permutations(alphabet)
    
    count = 0
    for key in possible_keys:
        plaintext = decrypt(ciphertext, key)
        print(f"Key: {''.join(key)} -> Decryption: {plaintext}")
        count += 1
        if count > 50:  # Limit output for practical reasons
            break

def main():
    ciphertext = input("Enter encrypted text: ").upper()
    print("Attempting brute-force decryption (showing first 50 results)...")
    brute_force_monoalphabetic(ciphertext)

if name == "main":
    main()