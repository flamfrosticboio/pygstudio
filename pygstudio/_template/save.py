# // Pygstudio template file created by pygstudio script (Version 1.0)
# ? You are free to edit this script

from typing import Dict, List, Union

import os
from json import loads, dumps

JsonValue = Union[
    Dict[str, "JsonValue"], List["JsonValue"], str, bool, int, float, None
]
__all__ = [
    "get_save_folder",
    "set_save_folder",
    "save_file_raw",
    "save_file",
    "read_file_raw",
    "read_file",
    # # ? Uncomment these and other comments under the file encryption section
    # # ?   if you use the file encryption
    # "save_file_encrypted",
    # "read_file_encrypted"
]

SaveFolder = os.path.join(__file__, "..", "saves")


def get_save_folder():
    return SaveFolder


def set_save_folder(path: str):
    global SaveFolder
    SaveFolder = path


def save_file_raw(filename: str, data: Union[str, bytes], mode: str = "wt"):
    filename = os.path.join(SaveFolder, filename)
    if not os.path.exists(os.path.dirname(filename)):
        os.makedirs(os.path.dirname(filename))
    with open(filename, mode) as file:
        file.write(data)


def save_file(filename: str, data: JsonValue):
    save_file_raw(filename, dumps(data))


def read_file_raw(filename: str, mode: str = "rt") -> Union[str, bytes]:
    filename = os.path.join(SaveFolder, filename)
    if not os.path.exists(filename):
        return ""
    with open(filename, mode) as file:
        return file.read()


def read_file(filename: str) -> JsonValue:
    data = read_file_raw(filename)
    if len(data) == 0:
        return None
    return loads(data)


# * Code that encrypts your saves (Uncomment them if you use it)

# # ? Must have cryptography installed. `pip install cryptography`
# from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
# from cryptography.hazmat.primitives import padding
# from cryptography.hazmat.backends import default_backend

# # ? You can generate a key and iv doing `os.urandom(<keysize>)`. Ex: `os.urandom(32)` as 256-bit key
# KEY = b""  # Add your key here


# def encrypt_text(text: str):
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


# def save_file_encrypted(filename: str, data: JsonValue):
#     data = dumps(data)
#     encrypted = encrypt_text(data)
#     save_file_raw(filename, encrypted, "wb")


# def read_file_encrypted(filename: str) -> JsonValue:
#     data = read_file_raw(filename, mode="rb")
#     if len(data) == 0:
#         return None
#     return loads(decrypt_text(data))  # type: ignore
