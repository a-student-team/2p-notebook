import base64

def encrypt(message, key):
    encrypted = []
    for i in range(len(message)):
        encrypted.append(chr(ord(message[i]) ^ ord(key[i % len(key)])))
    return base64.b64encode(''.join(encrypted).encode())
    

#use base64 to decode/encode
def decrypt(message, key):
    decrypted = []
    message = base64.b64decode(message).decode()
    for i in range(len(message)):
        decrypted.append(chr(ord(message[i]) ^ ord(key[i % len(key)])))
    return ''.join(decrypted)

#test
if __name__ == '__main__':
    message = "Hello World!"
    key = "Secret Key"
    encrypted = encrypt(message, key)
    decrypted = decrypt(encrypted, key)
    print(encrypted)
    print(decrypted)


