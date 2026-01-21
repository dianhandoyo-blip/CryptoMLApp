from encrypt import encrypt
from decrypt import decrypt

def encrypt_ml(text, password):
    return encrypt(text, password)

def decrypt_ml(text, password):
    return decrypt(text, password)