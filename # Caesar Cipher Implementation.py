# Caesar Cipher Implementation

def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():  # Encrypt only alphabetic characters
            shift_base = 65 if char.isupper() else 97
            encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted_text += char  # Non-alphabetic characters remain unchanged
    return encrypted_text

def decrypt(text, shift):
    return encrypt(text, -shift)  # Decryption is simply shifting backwards

# Input message and shift value from the user
message = input("Enter the message: ")
shift_value = int(input("Enter the shift value: "))

# Perform encryption and decryption
encrypted_message = encrypt(message, shift_value)
decrypted_message = decrypt(encrypted_message, shift_value)

# Display results
print(f"Encrypted Message: {encrypted_message}")
print(f"Decrypted Message: {decrypted_message}")
