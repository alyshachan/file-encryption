from cryptography.fernet import Fernet

fileToEncrypt = "test.txt"

### Generates cryptography key ###
key = Fernet.generate_key()

with open('cryptoKey.key', 'wb') as cryptoKey:
    cryptoKey.write(key)


### Encrypts file and opens ###
with open('cryptoKey.key', 'rb') as cryptoKey:
    key = cryptoKey.read()

fernetKey = Fernet(key)
with open(fileToEncrypt, 'rb') as originalFile:
    file = originalFile.read()

encrypted = fernetKey.encrypt(file)

with open('encrypted_'+fileToEncrypt, 'wb') as encryptedFile:
    encryptedFile.write(encrypted)


### Decrypt file and opens ###
with open('cryptoKey.key', 'rb') as cryptoKey:
    key = cryptoKey.read()

fernetKey = Fernet(key)
with open('encrypted_'+fileToEncrypt, 'rb') as encryptedFile:
    file = encryptedFile.read()

decrypted = fernetKey.decrypt(file)

with open('decrypted_'+fileToEncrypt, 'wb') as decryptedFile:
    decryptedFile.write(decrypted)