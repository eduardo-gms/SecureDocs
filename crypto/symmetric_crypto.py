import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


def encrypt_aes(data):

    key = os.urandom(32)
    iv = os.urandom(16)

    cipher = Cipher(algorithms.AES(key), modes.CFB(iv))
    encryptor = cipher.encryptor()

    encrypted = encryptor.update(data) + encryptor.finalize()

    return encrypted, key, iv


def decrypt_aes(encrypted, key, iv):

    cipher = Cipher(algorithms.AES(key), modes.CFB(iv))
    decryptor = cipher.decryptor()

    return decryptor.update(encrypted) + decryptor.finalize()