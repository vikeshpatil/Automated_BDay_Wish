import pyAesCrypt
from os import stat, remove
import base64


# encryption/decryption buffer size
password = base64.b64decode(b'QmlydGhkYXk=').decode('utf-8')


def encrypt(FileName):
    with open(FileName, "rb") as fIn:
        with open(FileName + ".aes", "wb") as fOut:
            pyAesCrypt.encryptStream(fIn, fOut, password, 64*1024)
    remove(FileName)

def decrypt(FileName):
    with open(FileName + ".aes", "rb") as fIn:
        with open(FileName, "wb") as fOut:
            try:
                pyAesCrypt.decryptStream(fIn, fOut, password, 64*1024, stat(FileName + ".aes").st_size)
            except ValueError:
                print('Unable to Decrypt!!')
print()


