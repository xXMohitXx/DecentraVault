from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def encrypt_file(file_data, key):
    """Encrypts the file with AES encryption."""
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(file_data)
    return ciphertext, cipher.nonce, tag

def decrypt_file(ciphertext, key, nonce, tag):
    """Decrypts the file with AES decryption."""
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    return cipher.decrypt_and_verify(ciphertext, tag)
