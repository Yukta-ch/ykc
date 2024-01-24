# Importing the Fernet class from the cryptography library for AES encryption
from cryptography.fernet import Fernet

# Function to generate a random key for encryption
def generate_key():
    return Fernet.generate_key()

# Function to encrypt a file using the provided key
def encrypt_file(key, input_file):
    # Creating a Fernet cipher suite with the provided key
    cipher_suite = Fernet(key)
    
    # Opening and reading the content of the input file in binary mode
    with open(input_file, 'rb') as f:
        plaintext = f.read()
    
    # Encrypting the plaintext using the Fernet cipher suite
    encrypted_data = cipher_suite.encrypt(plaintext)
    return encrypted_data

# Function to decrypt data using the provided key
def decrypt_file(key, encrypted_data):
    # Creating a Fernet cipher suite with the provided key
    cipher_suite = Fernet(key)
    print("\n")
    
    # Decrypting the encrypted data using the Fernet cipher suite
    decrypted_data = cipher_suite.decrypt(encrypted_data)
    return decrypted_data

# Main function to execute file encryption and decryption operations
def main():
    # Infinite loop for user interaction until explicitly exited
    while True:
        # Displaying menu options
        print("==="*10)
        print("AES File Encryption and Decryption")
        print("1. Encrypt a file")
        print("2. Decrypt a file")
        choice = input("Enter your choice (1/2): ")
        print("==="*10)

        # Handling user choice
        if choice == '1':
            # Generating a random key for encryption
            key = generate_key()
            print("Key:")
            print(key.decode())
            
            # Taking user input for the file to be encrypted
            input_file = input("Enter the name of the file to encrypt: ")
            
            # Encrypting the file and displaying the result
            encrypted_data = encrypt_file(key, input_file)
            print("Encrypted Text:")
            print(encrypted_data.decode())
            print("\n")

        elif choice == '2':
            # Taking user input for key and encrypted text
            key = input("Enter key: ")
            encrypted_text = input("Enter the encrypted text: ")
            
            # Decrypting the text and displaying the result
            decrypted_data = decrypt_file(key.encode(), encrypted_text.encode())
            print("Decrypted Text:")
            print(decrypted_data.decode())
            print("\n")
            
        else:
            # Displaying an error message for an invalid choice
            print("Invalid choice. Please choose only given alternatives")
    
# Ensuring that the main function is executed only if the script is run as the main program
if __name__ == '__main__':
    main()













# The Advanced Encryption Standard (AES) is a symmetric encryption algorithm widely adopted as a standard by governments and organizations globally.
# It was established by the National Institute of Standards and Technology (NIST) in 2001 as FIPS PUB 197 and is specified in the Federal Information Processing Standards (FIPS) publication 197.
# AES is designed to provide strong security and efficiency in both hardware and software implementations.
# AES is a symmetric encryption algorithm, meaning the same key is used for both encryption and decryption.

# File Encryption:

# 1. Choose a Key:
# First, you need a secret key.
# This key should be kept confidential, as it is used for both encryption and decryption.

# 2. Divide the File into Blocks:
# Break your file into fixed-size blocks.
# For AES, the block size is 128 bits (16 bytes).

# 3. Padding:
# If the last block is not complete, pad it to make it a full block.

# 4. Initial Round Key Addition:
# XOR the first block with the initial round key.

# 5. Rounds:
# Perform a series of rounds (usually 10, 12, or 14 rounds depending on the key size - 128, 192, or 256 bits).
# Each round consists of substitution, permutation, and mixing operations on the block.

# 6. Final Round:
# The final round is slightly different, skipping the mixing operation.

# 7. Output:
# The processed block is now encrypted. Repeat the process for each block.

# File Decryption:

# 1. Key Setup:
# Set up the key schedule for decryption.

# 2. Initial Round Key Addition:
# XOR the first block with the last round key used in encryption.

# 3. Rounds (in reverse order):
# Perform the inverse of each encryption round. This involves applying the inverse operations in the reverse order.

# 4. Final Round:
# The final round in decryption is slightly different, skipping the inverse mixing operation.

# 5. Output:
# The processed block is now decrypted. Repeat the process for each block.

# Remember, the specifics of the AES algorithm involve complex mathematical operations.
# It's crucial to use a reliable cryptography library or tool for actual implementation, as these libraries handle the details securely.

# Please note that using ECB mode for encryption is not secure for many use cases, and you should consider using a mode like CBC or GCM for better security.

# Key Features of AES:

# 1. Symmetric Encryption:
# • AES is a symmetric-key algorithm, meaning the same key is used for both encryption and decryption.
# • This requires secure key distribution.

# 2. Block Cipher:
# • AES operates on fixed-size blocks of data.
# • The standard block size is 128 bits (16 bytes).

# 3. Key Sizes:
# • AES supports key sizes of 128, 192, and 256 bits.
# • The security strength of the algorithm increases with the key size.

# 4. Rounds:
# • The number of rounds in AES varies based on the key size: 10 rounds for 128-bit keys, 12 rounds for 192-bit keys, and 14 rounds for 256-bit keys.
# • Each round involves a series of mathematical operations.
