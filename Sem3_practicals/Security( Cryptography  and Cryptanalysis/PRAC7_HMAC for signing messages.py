# Importing the hashlib module for cryptographic hashing functions
import hashlib

# Creating an MD5 hash object for the byte sequence 'Ismile'
result = hashlib.md5(b'Ismile')

# Creating another MD5 hash object for the byte sequence 'Esmile'
result1 = hashlib.md5(b'Esmile')

# Displaying the digest (raw bytes) of the first MD5 hash
print(result.digest())

# Displaying a message and the digest (raw bytes) of the second MD5 hash
print("The byte equivalent of hash is : ", end="")
print(result1.digest())



























# Message Authentication Code (MAC):
# MAC is a technique used to ensure the integrity and authenticity of messages exchanged between two parties.
# It involves the use of a secret key and a cryptographic hash function to generate a tag or code that can be appended to the message.
# The receiver can verify the integrity and authenticity of the message by recomputing the MAC using the same key and hash function and comparing it with the received MAC.

# MAC can be implement using various algorithms, we consider MD5 and SHA1.

# HMAC (Hash-based Message Authentication Code) is a mechanism for creating a secure way to verify the integrity and authenticity of a message.
# It involves combining a secret key with a hash function to generate a unique code (the HMAC) that can be attached to a message.

# Here's a simple explanation of how to implement HMAC for signing messages:

# Basic Idea:
# 1. Choose a Hash Function:
# Pick a cryptographic hash function (e.g., SHA-256).
# 2. Have a Secret Key:
# You and the recipient should share a secret key.
# 3. Concatenate Key and Message:
# Combine the secret key with the message you want to sign.
# 4. Hash the Result:
# Apply the hash function to the combined key and message.
# 5. Attach the HMAC:
# Send the original message along with the HMAC.

# Generating HMAC (Signing):
# 1. Choose a Hash Function:
# For example, SHA-256.
# 2. Prepare the Key:
# Use the shared secret key.
# 3. Concatenate Key and Message:
# Combine the key and the message you want to sign.
# 4. Hash the Result:
# Apply the hash function to the combined key and message.
# 5. Use the Result as HMAC:
# The output of the hash function becomes the HMAC.

# Verifying HMAC (Checking Signature):
# 1. Receive Message and HMAC:
# Get the message and the attached HMAC.
# 2. Prepare the Key:
# Use the shared secret key.
# 3. Recompute HMAC:
# Concatenate the key with the received message and apply the hash function.
# 4. Compare with Received HMAC:
# Check if the recomputed HMAC matches the received HMAC.
#    - If they match, the message is authentic and unchanged.
#    - If they don't match, the message may have been tampered with or is not from the expected sender.

# The generated HMAC can then be sent along with the original message, and the recipient can use the same key and hash function to verify the integrity and authenticity of the message.

# MD5 Algorithm:
# MD5 (Message Digest Algorithm 5) is a widely used cryptographic hash function.
# Although it has been widely used historically, it is now considered to have vulnerabilities and is not recommended for security-critical applications.
# Nonetheless, it serves as an educational example for understanding MAC and cryptographic hash functions.

# MAC Generation Process:
# To generate a MAC using the MD5 algorithm, follow these steps:

# a) Both the sender and receiver must agree on a secret key, K, which is known only to them.
# b) Concatenate the message, M, and the secret key, K: ConcatenatedData = M || K (|| denotes concatenation).
# c) Apply the MD5 algorithm to the ConcatenatedData to obtain the MAC: MAC = MD5(ConcatenatedData).
# d) MAC Verification Process:

# To verify the integrity and authenticity of a received message using the MAC, follow these steps:

# a) Receive the message, M, and the MAC, MAC.
# b) Concatenate the received message, M, with the secret key, K: ConcatenatedData = M || K.
# c) Apply the MD5 algorithm to the ConcatenatedData to compute the recalculated MAC: RecalculatedMAC = MD5(ConcatenatedData).
# d) Compare the RecalculatedMAC with the received MAC. If they match, the message is considered authentic and intact.

# Security Considerations:
# MD5 is no longer considered secure for cryptographic purposes due to vulnerabilities that have been discovered.
# It is susceptible to collision attacks, where two different inputs produce the same hash value.
# Therefore, it is recommended to use stronger hash functions, such as SHA-256 or SHA-3, for MAC generation in real-world applications.
