# Importing necessary modules from the cryptography library for AES encryption
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

# Function to pad data to match the block size for AES encryption
def pad(data):
    # Determining the block size in bytes for AES encryption
    block_size = algorithms.AES.block_size // 8
    
    # Calculating the number of remaining bytes needed for padding
    remaining_bytes = block_size - (len(data) % block_size)
    
    # Creating padding bytes with values equal to the number of remaining bytes
    padding = remaining_bytes * bytes([remaining_bytes])
    
    # Appending the padding to the original data
    return data + padding

# Function to unpad data after AES decryption
def unpad(data):
    # Extracting the length of padding from the last byte of the data
    padding_length = data[-1]
    
    # Removing the padding bytes from the data
    return data[:-padding_length]

# Function to perform AES encryption or decryption in ECB mode
def encrypt_decrypt_ecb(key, data, mode):
    # Padding the data to match the block size for AES encryption
    data = pad(data)
    
    # Creating an AES cipher with the provided key and mode
    cipher = Cipher(algorithms.AES(key), mode, backend=default_backend())
    
    # Creating an encryptor and encrypting the data
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(data) + encryptor.finalize()
    
    # Creating a decryptor and decrypting the ciphertext
    decryptor = cipher.decryptor()
    decrypted_data = unpad(decryptor.update(ciphertext) + decryptor.finalize())
    
    # Returning the encrypted ciphertext and decrypted data
    return ciphertext, decrypted_data

# Main function to demonstrate AES encryption and decryption in ECB mode
def main():
    # Generating a random 16-byte key for AES encryption
    key = os.urandom(16)
    
    # Sample data to be encrypted
    data = b'This is a sample message for encryption.'
    
    # Creating an ECB mode object
    ecb_mode = modes.ECB()
    
    # Encrypting and decrypting the data using ECB mode
    ecb_ciphertext, ecb_decrypted_data = encrypt_decrypt_ecb(key, data, ecb_mode)
    
    # Displaying the results
    print(f"ECB Ciphertext: {ecb_ciphertext.hex()}")
    print(f"ECB Decrypted Data: {ecb_decrypted_data.decode()}")

# Ensuring that the main function is executed only if the script is run as the main program
if __name__ == "__main__":
    main()


















# Block cipher modes of operation are techniques used to encrypt or decrypt messages of more than one block of data in a secure manner.
# Block cipher modes are techniques used to enhance the security of block ciphers, such as AES, by specifying how they encrypt or decrypt data in blocks.
# Here are some common block cipher modes:

# 1. Electronic Codebook (ECB):
   # Description:
     # This is the simplest mode.
     # It divides the data into blocks and encrypts each block independently.
     # Each block of plaintext is independently encrypted.
     # Identical blocks of plaintext will produce identical ciphertext blocks.
     # It lacks diffusion, meaning that patterns present in the plaintext will be preserved in the ciphertext.
   # Advantages:
     # Simple and parallelizable.
   # Drawbacks:
     # Identical blocks of plaintext produce identical blocks of ciphertext, which may leak information.

# 2. Cipher Block Chaining (CBC):
   # Description:
     # XORs each plaintext block with the previous ciphertext block before encryption.
     # Each block of plaintext is XORed with the previous ciphertext block before encryption.
     # The first block is XORed with an initialization vector (IV).
     # Provides better diffusion than ECB.
   # Initialization Vector (IV):
     # Requires an IV to start the process.
   # Advantages:
     # Provides more security than ECB due to feedback from previous blocks.
   # Drawbacks:
     # Not parallelizable; errors in one block affect subsequent blocks.

# 3. Cipher Feedback (CFB):
   # Description:
     # Treats the block cipher as a stream cipher.
     # The previous ciphertext block is encrypted and XORed with the current plaintext block to produce the next ciphertext block.
     # Operates on smaller units than a block (e.g., individual bytes).
     # The feedback from the encryption of previous units is used to XOR with the plaintext to produce the ciphertext.
   # Advantages:
     # Can be used for streaming data.
   # Drawbacks:
     # Bit errors propagate, and it's sensitive to out-of-sequence blocks.

# 4. Output Feedback (OFB):
   # Description:
     # Similar to CFB, but XORs the output of the block cipher with the plaintext to produce the ciphertext, without depending on previous ciphertext blocks.
     # Instead of encrypting the previous ciphertext block, it encrypts a continuously generated keystream.
     # It turns a block cipher into a synchronous stream cipher.
   # Advantages:
     # Bit errors do not propagate, and it's parallelizable.
   # Drawbacks:
     # Not suitable for streaming data, and does not hide patterns in the plaintext.

# 5. Counter (CTR):
   # Description:
     # Turns a block cipher into a stream cipher.
     # It uses a counter value as input to the block cipher, and the result is XORed with the plaintext to produce the ciphertext.
     # Allows parallel encryption/decryption since each block can be independently processed.
   # Advantages:
     # Highly parallelizable and suitable for streaming data.
   # Drawbacks:
     # Requires a unique counter for each block to avoid security issues.

# 6. Galois/Counter Mode (GCM):
   # Description:
     # Combines the counter mode with polynomial authentication, providing both confidentiality and integrity.
   # Advantages:
     # Efficient and widely used for secure communication.
   # Drawbacks:
     # Requires careful implementation to prevent side-channel attacks.

# Remember, the choice of a block cipher mode depends on the specific requirements of the application, including security, performance, and the nature of the data being encrypted.
