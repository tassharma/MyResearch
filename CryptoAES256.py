import base64
import hashlib
from Crypto.Cipher import AES
from Crypto import Random

#BLOCK_SIZE = 16
#pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)
#unpad = lambda s: s[:-ord(s[len(s) - 1:])]

def pad(s):
    return s.encode('utf-8') + b"\0" * (AES.block_size - len(s) % AES.block_size)
 
key = '[EX\xc8\xd5\xbfI{\xa2$\x05(\xd5\x18\xbf\xc0\x85)\x10nc\x94\x02)j\xdf\xcb\xc4\x94\x9d(\x9e'
 
def encrypt(jsonBody):
   print("Inside encrypt function")
   print("Edited in Git Hub")
   print("raw jsonBody :: {}".format(jsonBody))
   #print("encode utf-8 :: {}".format(jsonBody.encode("utf-8")))
   private_key = hashlib.sha256(key.encode("utf-8")).digest()
   jsonBody = pad(jsonBody)
   iv = Random.new().read(AES.block_size)
   cipher = AES.new(private_key, AES.MODE_CBC, iv)
   return base64.b64encode(iv + cipher.encrypt(jsonBody))
 
 
def decrypt(enc):
    private_key = hashlib.sha256(key.encode("utf-8")).digest()
    enc = base64.b64decode(enc)
    iv = enc[:AES.block_size]
    cipher = AES.new(private_key, AES.MODE_CBC, iv)
    return cipher.decrypt(enc[AES.block_size:])
 
 
# First let us encrypt secret message
encrypted = encrypt("This is a secret message")
print(encrypted)
 
decrypted = decrypt(encrypted) 
print(decrypted)
# Let us decrypt using our original password
# decrypted = decrypt(encrypted, password)
# print(bytes.decode(decrypted))
