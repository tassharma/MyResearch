from Crypto.Cipher import AES
import base64
import hashlib

#generate the keys
key = b'mysecretpassword'
#private_key = hashlib.sha256(key.encode("utf-8")).digest()
plaintext = 'this is my super secret message to encrypt'
encodedPlaintext = plaintext.encode("utf-8")

#create cipher to encrypt the message
e_cipher = AES.new(key,AES.MODE_EAX)
print(e_cipher)

#create variable to encrypt the message
e_ciphertext = e_cipher.encrypt(encodedPlaintext)


#create cipher to decrypt the message
d_cipher = AES.new(key, AES.MODE_EAX, e_cipher.nonce)

#create variable to decrypt the message
d_ciphertext =  d_cipher.decrypt(e_ciphertext)


print("Encrypted message: ", e_ciphertext)
print("Plaintext: ", d_ciphertext)
