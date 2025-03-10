import itertools

def decrypt(ciphertext, key_mapping):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    decrypted_text = ""
    for char in ciphertext:
        if char in alphabet:
            decrypted_text += key_mapping[char]
        else:
            decrypted_text += char  # Keep non-alphabet characters unchanged
    return decrypted_text

def brute_force_attack(ciphertext):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    permutations = itertools.permutations(alphabet)  # Generate all possible key mappings

    for perm in permutations:
        key_mapping = {perm[i]: alphabet[i] for i in range(26)}  # Create decryption mapping
        decrypted_text = decrypt(ciphertext, key_mapping)
        print(f"Possible Decryption: {decrypted_text}")

# Example usage:
ciphertext = input("Enter the encrypted message: ").upper()
brute_force_attack(ciphertext)
