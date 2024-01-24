# Importing necessary modules for the script
import os  # Operating system-specific functionality
import hashlib  # Provides secure hash and message digest algorithms
import secrets  # Cryptographically strong random number generator

# Function to generate a random 16-byte salt
def generate_salt():
    return secrets.token_bytes(16)

# Function to hash the given password using SHA-256 and provided salt
def hash_password(password, salt):
    hashed_password = hashlib.sha256(password.encode('utf-8') + salt).hexdigest()
    return hashed_password

# Function to verify the entered password by hashing it and comparing it with the stored hashed password
def verify_password(entered_password, stored_password, salt):
    entered_password_hash = hash_password(entered_password, salt)
    return entered_password_hash == stored_password

# Main function to execute the authentication process
def main():
    # User input for registration
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Generating a salt for password hashing
    salt = generate_salt()

    # Hashing the password with the generated salt
    hashed_password = hash_password(password, salt)

    # Storing user data (username, salt, hashed password) in a dictionary
    stored_data = {
        'username': username,
        'salt': salt,
        'hashed_password': hashed_password
    }

    # Displaying a success message for registration
    print(f"User {username} registered successfully!")

    # User input for login
    login_username = input("Enter your username for login: ")
    login_password = input("Enter your password for login: ")

    # Retrieving salt and hashed password from stored data
    stored_salt = stored_data.get('salt')
    stored_hashed_password = stored_data.get('hashed_password')

    # Verifying the entered password during login
    if verify_password(login_password, stored_hashed_password, stored_salt):
        print("Login successful!")
    else:
        print("Login failed. Invalid username or password.")

# Ensuring that the main function is executed only if the script is run as the main program
if __name__ == "__main__":
    main()









# 1. What is Password Salting and Hashing?

# Password Hashing:
# Imagine turning your password into a secret code that no one can read.
# Hashing is like that.
# It transforms your password into a unique string of characters using a special algorithm.
# Even a small change in the password will result in a completely different hash.
# Objective: The primary goal of password hashing is to secure user passwords by converting them into a fixed-length string of characters that is computationally difficult to reverse.
# This process helps protect user passwords in case of a data breach where attackers may gain access to the hashed values.
# Common Hashing Algorithms:
# Cryptographic hash functions like SHA-256 (Secure Hash Algorithm 256-bit) are commonly used for password hashing.
# These algorithms produce a fixed-size output (hash) regardless of the input size and are designed to be one-way functions, making it difficult to reverse-engineer the original input from the hash.

# Password Salting:
# Now, imagine adding a little extra something to your password before hashing it.
# That extra something is called a "salt."
# A salt is just a random string of characters.
# So, even if two people have the same password, the salt makes their hashed passwords different.
# Challenge:
# One weakness of using only hash functions for password storage is that identical passwords yield the same hash, making them vulnerable to attacks like rainbow table attacks.
# Rainbow tables are precomputed tables of hashes for commonly used passwords, allowing attackers to quickly look up the original passwords corresponding to known hashes.
# Solution:
# Password salting involves generating a unique, random value (the salt) for each user.
# This salt is then combined with the user's password before hashing.
# The resulting hash, which is unique to both the password and the salt, is stored along with the salt in the database.

# 2. Why Do We Need This?

# Security:
# If bad guys get hold of a list of hashed passwords, they can try to crack them using techniques like "brute force" or "rainbow tables."
# Salting makes this much harder because each password has a unique salt.
# Protection from Same Passwords:
# If two users have the same password, without salting, their hashes would be identical.
# But with salting, the hashes will be different because of the unique salts.

# 3. How to Implement It?

# Choose a Hashing Algorithm:
# Pick a secure and widely accepted hashing algorithm, like bcrypt or SHA-256.
# Generate a Salt:
# Create a random salt for each user. This is unique to them.
# Combine Password and Salt:
# Concatenate (join together) the user's password and the salt.
# Hash the Combined String:
# Use the chosen hashing algorithm to convert the combined string into a hash.
# Store Salt and Hash:
# Save both the salt and the hash in your database. When the user tries to log in, you repeat the process with the entered password and stored salt to see if it matches the stored hash.

