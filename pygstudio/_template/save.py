# // Pygstudio template file created by pygstudio script (Version 1.1)
# ? You are free to edit this script
# ! Stub file exists. Be sure to visit it also

import os
from json import loads, dumps

SaveFolder = os.path.abspath(os.path.join(__file__, "..", "saves"))


def save_file_raw(filename, data, mode="wt"):
    filename = os.path.join(SaveFolder, filename)
    if not os.path.exists(os.path.dirname(filename)):
        os.makedirs(os.path.dirname(filename))
    with open(filename, mode) as file:
        file.write(data)


def save_file(filename, data):
    save_file_raw(filename, dumps(data))


def read_file_raw(filename, mode="rt"):
    filename = os.path.join(SaveFolder, filename)
    if not os.path.exists(filename):
        return ""
    with open(filename, mode) as file:
        return file.read()


def read_file(filename):
    data = read_file_raw(filename)
    if len(data) == 0:
        return None
    return loads(data)

def save(data):
    return save_file("save", data)

def read():
    return read_file("save")


# * Code that encrypts your saves (Uncomment them if you use it)

# # ? Must have cryptography installed. `pip install cryptography`
# from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
# from cryptography.hazmat.primitives import padding
# from cryptography.hazmat.backends import default_backend

# # ? You can generate a key and iv doing `os.urandom(<keysize>)`. Ex: `os.urandom(32)` as 256-bit key
# KEY = b""  # Add your key here


# def encrypt_text(text):
#     iv = os.urandom(16)
#     encryptor = Cipher(
#         algorithms.AES(KEY), modes.CBC(iv), backend=default_backend()
#     ).encryptor()
#     padder = padding.PKCS7(algorithms.AES.block_size).padder()  # type: ignore
#     return (
#         iv
#         + encryptor.update(padder.update(text.encode()) + padder.finalize())
#         + encryptor.finalize()
#     )


# def decrypt_text(text: bytes):
#     iv = text[:16]
#     ciphertext = text[16:]
#     decryptor = Cipher(
#         algorithms.AES(KEY), modes.CBC(iv), backend=default_backend()
#     ).decryptor()
#     unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()  # type: ignore
#     return (
#         unpadder.update(decryptor.update(ciphertext) + decryptor.finalize())
#         + unpadder.finalize()
#     )


# def save_file_encrypted(filename, data):
#     data = dumps(data)
#     encrypted = encrypt_text(data)
#     save_file_raw(filename, encrypted, "wb")


# def read_file_encrypted(filename):
#     data = read_file_raw(filename, mode="rb")
#     if len(data) == 0:
#         return None
#     return loads(decrypt_text(data))  # type: ignore
