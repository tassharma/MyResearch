from Crypto import Random
from Crypto.Cipher import AES
import hashlib
import json

key = '[EX\xc8\xd5\xbfI{\xa2$\x05(\xd5\x18\xbf\xc0\x85)\x10nc\x94\x02)j\xdf\xcb\xc4\x94\x9d(\x9e'
private_key = hashlib.sha256(key.encode("utf-8")).digest()

def pad(s):
    return s.encode('utf-8') + b"\0" * (AES.block_size - len(s) % AES.block_size)


def encrypt(message, key ):
    message = pad(message)
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return (iv + cipher.encrypt(message))

def decrypt(ciphertext, key):
    iv = ciphertext[:AES.block_size]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext[AES.block_size:])
    return plaintext.rstrip(b"\0")    


#plaintext = "This is the message to be encrypted"
#plaintext="{\"Department\":[\"departmentcode\",\"NULL\"],\"DataModel\" :[\"Scheduling\",\"Order\"],\"OrganizationId\" :\"1\"}"
# with open('C:/Planfirma/Scheduling.json') as f:
#      plaintext = f.read()
# f.close()
#plaintext =json.dumps({
#        "id": 0,
#        "petId": "Panda",
#         "quantity": 0,
#         "shipDate": "2022-08-05T08:29:59.479Z",
#         "status": "placed",
#         "complete": True
# })
#print('------------')
#print('Original Message')
#print(plaintext)
#enc = encrypt(plaintext,private_key)
#enc ='flxTt<\xf7\xd7\xe4Uz\x92\xfe\x84\xe6fz\xc5~\xe3p\xc1o\xf7\xbfn\xc2\x86Z\xef\xcd\xa3\xda\xabC9\x89$Z\x134\xe6\x82/\xf8\xd0\xc7\xa5!\xd2\xdc\xdf\x0e\xadX\x016=f\x06\xc7\xea\x81\xfb\xc7\xbc\t\xf8#^[\x03\x86\xa0\xed\x10\xe6\xc6\xf8\tf8\xca\xc8t\x11x40\xe1\x1e\xf6\xc3\xfd\\d=\xbe\x9d\xda2\x886\x8a\xe2Z\xf2A\x7f\x83\x98\xa6\x919[s\xcf_\xff\x85\xd9\xcaZ\x1c\xa4\xd52\x03P\x0c\xb5\xb4s\x9d\x07Y\xe1\x10\xabJ\x8b\xcfu\xdd\x8e5\xaa\x10\xf5\xf5\xbf\x8c\x0fzWJL\x13h\x00@\xde\x05\xad\xf5\xd5~\xa2D\xe0\xfdM\x13\xa7b\x92`\x91\x0f\x1fJ\x02f@\xdc\x08\x97\xe4\x1a\xf1\xe3{\xdc\x95kH\xa4\xc57\xcb[EYLK\x8d\x80K\xda\xf3PP\x07|WU\xb5\x9e\x8a\x07\xffY/\xdf\xafv+}\x84\xa5K-\x8c\x1e\x0fq\xa6\x8bo\x1c\x93w\xfdW\xa3\x03\xe1\x88\xda\x0e\xbeZ\xa2\xed\x94]$\'\x98\x8be\xd8u\xd1\xbfA\xd9\x98\xc1E\xb7B\xd9`7\xf4\x7fN\xe5J$)\x80\x83\x8d\x8b\xe2\xd6\xef\xd6\xda\xf3I\xf4\x97\x9e|G<R\xc8\xd7=\x80!\xfet\x1c>\x97Y\x08=;\xc4\x11\xb6\x17\xae\x7f%\x7ff#\x1b\xcd\xb92\x03\xbd\x81\xce\x12\x89\x10!\xbc\x96\xd2\t\xe4\xa1f2\t\xbb\x96A\x19\x07\xe5a\xdc\x8b(\xb7\xd2\xcb\xfe\xa8\xf2\xd5\x03\x18;\xc5"Cb\xb1h\xc5\xaf`p\x12\xe0\x9d\x99\xcbk\xe3\xc3\x95~\xa3\xb3\xb0\xe5\x11\x9bu\x9e?\xa1\xfdT\xb7I \x085\xccG\x92A\x92eI\xd3\x99\x9c\x1fO"\xb1\t\x87#\xc7\xce_5\x9e\x10\x18)\x8b\x1e+\x01\xe6\x8b\x98.\x8e\x007\x11\xc1\xe9~\xb3c"\xf4\xc2}8MDwD.\xd3j\x81\xf7\xa5?\xb2\xe6R\xb2D\x13\xa8\xd9pN\x9d\xaf\xea\xe8\xfa.\xc8\x9ds\xc6.\xc8\xf9\xd3\x8c\xe7fJ\x11\xa4\x8bX|\xf6\xfd\xf3\x9ce\x17\x93\xf3F6!\xee@\x86\x14K|B,\x16\x92/?\xba\x9e.\xac\xdbjo[\xbcK!\x9d0k\x1d\x06\x1a\xd8q\xb9;\xf8\xdb\xd4k\xa0\x90\xa1F$\xa00\xbb]]\xb8\x19\x94\xd4\x92\x12\x9d\x1f\x99\x06\x9b7\x83\x1bJh\xe5\xda\x84\x12xA\xc4\x8e`@\xd2_\xfd\xee\xa3\xcds\'"b+\x04\x8at\xb1V\x07\x98[:\xd4\x9ca\xf4t5\xf4\xec\xc60\xd8H\xb7z_\xeap\xecs\xd8\xfe\xdd\x95\x91\x0f\xba\xb0O\xbd\x90\xd5a4}\xad%\x1b\xfe\t\xb2o\xf9\xf3\xee\xe2\x1cI\x96\xb9\xcd\x10\xfd \xc5\xaf\xa5\xaa~\x9b\x84UroT\x9c\xa9jn\xf4\xf0D"S\xfb\xa8W\xe6\x1bl\x95\xb3_\xea\x1a@\xa4\x91\xfd\xf6\x1a\xeb\xad\x8b\xebd \xdf\\\xebG\xf7J\x96%7\xfe\xd1\x19-xy\x97q\x14.O\x03e\x02\xc2\xf0L\'\xfaq"5\xf6\xf6\x0c\xbd\x0b\xeb\xd5\xe9\xbeW{\x8c\t\x17x\x96\x99\xd4<\xc3! u\xa5\xa1\xacl\xb5\xc6{\xa5\x00\xf2 \x0ea|xXdp=:L\xc0\x8e\xd4!\xd4\xc3\xee\x95D,\xd9\x10\xdc\xe8\x9b\xd0\xca(\xa9d\xaa\xa5tf2\x7f\x11\xb1\x8e\x90[\x96L\xb1\xff>q>\x9a\xdb\x8d\x11\xfe\xe1\x99\xd2\x96!8\xd9\x0f\x14v{+\xa2#\xff\xd2\xf7*\xdd;K\x93\x03\xe2\xef\x95+\xa3\x85@\xd4[\x0f9\x15p\xa1Q\xf0\xaf\xaf\xd5~\x17\xb7+\x9f\'W@\xb4\x12\xac\xec\xdb\xd1\x19\xe2\xed>\xce\x93\xf7e\x13\xf1w\xac\x89B\\\x11\xc2:\x92\x86;\xb8\x8c\xeaL\xb7\x84\xff\xad>\xdb\x8dy\xfd\xb4\x8fB\xc6\xe2q\x94\x96\x80+\xd5\r\xde\x17K\x8ef\xe9\xfd\xf0\xa7Wg\xd9\x83\tF_$x\xbc`\xd3?\xd3\xe7\xf7l\xd5^D\x861\xf4\x87T\x12\xf9\x80(^\xc0\xd3\x9e\xbb\x1b\xd2\x85~m[G\xd1\x02\xcbZ\x80\xaa\xb1**\xaa\x80aW\xa8\xb4\x10\xf7\'\xab\x17\\{\t\xbd\x01m\xa0O\xd5\xc7\x16u\xb8\xa0\xe0\xbd\xf1}\xe4\x95\x8d\x88\xc1\x1d\xd8\xadm\x95\x1dP\x0c3\xf6u@Ne\t\xda\x13|\x84q>\xa5\xa4\'\xa8FdK\xd6vO\x9f\xcd\xd9\xb7\x86\\\x95\x94\x1e\x9a/\'\xad>\x9d\x01\x95q!\xca)\xc0\x137\x02W1\xaf\xee\x88@q\xbeJ\xaaa_7\x85\x92`\xdcq\xe1\xf3\xd8s\xf6\xb1\xa5\xb0$\xc9\xdd\xbf\x17\t\xa9\xdd\xbc\xc6\x00\x01\xfd\xbdg\xffdw\xf6fOSJh\x80\xc4\x80^\xbb\xf9x\x08\xf28\xcc\x86_\xc6\xe0\x17\x96\xb1U\xbd\xd1y\x05\x7f\xf8\x94>\x8c\x84\xc8 \xb2fZ\xaciY=@\xf8Z7;Q6\xac\xd0\xe4\x1e9P]g\x90o\x90\x162\x84N:\x81\xf2\xf8\xc7\xc8\x87\xdaRqA"\xfe]|\xc7\x00\xfb0\xa1&\x13\xc9d\xe1\x9d\xd0\xd3[\x9c\xc3\xed\x02\xca\x8b= _\xa3N*\xe3\x85\xfd\x146^\x9c\xecw\xb1)q\xf6J\xd6\'$\xb2T\x9djK\xfa\xb0\x1d2\\\xdcs\x85k,c\xfc\xd4?\xb3\xc9\xb9\x8e\xa4:\xf9N\x82R>\x9d\x1e\xb1\t\x1aj\xbe\x7f\xcf\xad\xf2\xef\x16\t>\xf7\x05q\x85\xb0G\n\\\xaa\xeed\xbbE"\x0f\xd8'
enc ='\xfd\x9d\xec\x1ew\xc94-\xd6\x86\x9c\x11\xc1U\xa51N\xf6\xb0\x83\xde\xdf\xe9\xc7\xb8\xd6:@\xe9\x126\x0c\xf4\'\x0e\x154\xe7-m\xb3\xe7\x84\t.\xb8\x022\x91\xd6\x85\x87\x81\xb920\xd3%r\xd8\xfe\xc5?\xd4\x96\xfe4\x02O8\x1c]\xf7N\xf2\x84\xde\xfa]i\x94\xc0\xe8W\xf0\xa0B|\xc3^>\nNL\xc0\x9a\x08\xa4NMl\x1d\x1b\x96%\x08{L_\xa7Q\xa5l(o8A.\x9c\x06\xfdfZ\xb7\xb5\xb8I"\x1e]\xd2w+c\x91H\xe4"\xb9f\xe0\xa7\xde\xaf8e\x1f\xef+\xef\xe1qqHuw\x0c\xf8F)\xbc\r\x05\xb0\x84\x94\x9c\x11\x01\xf6\xd9-)\xfd\x87\x9e\x9b\x92\xad\x9d$\xc6]\xb7\xd7\xaf:\xf9\x1f;\xd9\xec\x9a\x0f!i\xb7\xa4\xf9\x1a\xf8\xa8\x905,\xd6\x85D{rj\xd2\xe7\xc7C\xcb\x8b\x19S\x9e\xbeQw\xb6G\x9a\xb8\x08\x1bH\x8e\xf1l4\x03\x00w\x89\xa2\x93\x86\x19\x11\xb5\x0cK?CD\x8b&ZMD\xdf\r\x1b\xc6<\xe8k)\x894\xd5R\x82\x1f\xd6\xe2\xd1b\xb6\xb5\x8d\xf0T\xdc\xa6\x94x\x0f\x05\xc0\xe5\x1d\x16\xbf\x12\x8c\xea\xf3*\xcdf\x96u\xe2Z7\x8d\xddPk:\xc5\xff\xbd\x11Q]\x93Z\xfez>\x9foXH2M[\xf5\xdbr++s"\x1e\xf4\xcb\xf7\xf0y9\xfa$\x14\x11q\xdbI\xc9\x9b\x10\xd89\x12d\xc6e\xfc\x8c\xa6\xb3i}\xb4\xfa\x8e\x8ft\x1b\x9c\x15\x91\xf9\xb1\xa5\x1e8\xa8\xe9\xb4x\xbddq\xffhWXQ\xe0\xe2\x8e\xfc\xa50\xd2\xab\xdeBc\xf2\x8c_\x8ae3Aa\x1d\x06\x95\xa7\xdbq>\x8b\xa1\xfb\xe8E\xde\xd8\xe6L\xb4\xfa]\xce\x99\xc9\xe9\x17\xec\x9a\xaa\xa5\'0Ma\xab\xcd\xb8\xcct.\xab\xe9R?"v}\x0fU\x85\x88\xfd,\x00\xeb\xe1\x98\x0e\x82\xa0\xad\xba\xc7\xf1\xc1\xaa\xe1\x9a&\xf0\x19r\x05=\r\x01\x15_\x10\x1a\x00\xf2\x865\x8d\\$\x9b\xae\x9a\xea\xa1\xf0\rt\xb0\xc0\x9b\x961"\xb1?\xe6\x14\x86\xd88\x8e\xc6R\xe6Y\xf3\xaf\x99\xda\xbfu\xfc\xf5\x88\xeb{\xed\x92\xb0b\xe71\x82\xebV\xd9~<!\xef\xdc\xea\xb67]\x8d\xba\xa4v\xfb&\xd4\xce\x88\xd72x\x17\x1b\xbf4zbX\x18r/Q\x1e\xf5\xd9\xb7\x83\xc9\xdb2\xa0\x95\x9cLq/xU\x03m\xddY\xfbt\xd5\xfc\x81`O\xfa\xbej\xa0\xaa\x9e:N\xf2\xab\x83\xbdLo\xbe\nk*\xae%\xd7\x08\x12m\xe8\x1f\x9bM\x11\xc7D\xe4\xf5K\xf2^\xdd)\r\xd8SQj\xd3b.\x95\xba+\xf4\xb6\x9d\x82G\x8b9\x053\xd5H6\xfbh\x86\x1b8[\xa7Y1\xf831?\xb1;D\xbe\x92\x8d(_6X%?\x05Q\x11\x90\x80*\x87_#\xbc\x14\x1fw\x17Y\x1e\xab\xa86,\r\x16\xf8\x0c\xc4\x0e\xb5\xbdv\xfb\x92\x03<\t>\xe0\xfe\xc9z\x9a1\x06\x95|7F\'.\xf37u\xda\x99=p.\xffP\xd8\x14-\xb1\x15\x10\xbf\x84\x91\x84\x03 \xbc\x9f\x9eK\xd0O\xac@\xc7 \x10\xc74\xde\xc4(\xef\xb1Sl\xff$\rO\x85V\xba\x14.g\xcct\xd6\xf5\x8f\xb0qY\xff\x8e\xa7P\xfe\xea\xb7.\x8e\xe2\xe3S\xb1s\x14E#\xd2\xf9\xc0\xbb\xf8E\x895_$\x12\x1d\x8c\n\xd9^\t\r \xfa\xff\xc4\x942\x0b\x7f#\xc0\xa7p\xd6\xde\x9bc[w\xc5\xe5N\x9d\xd2\x9b\xfcL\x90\xab`M\x11\x9e\xeb2\xee\x83\x9a\xa3/\x13\xa4\xad\xac^*\xac\xb9\xec\xbc\xc8H\xc8\x81!\xba;\xb9\x96\xa4\xf1\xe4\xb2\x03\x93K"\x80\x16\x06aXA\x81\xa2\xc4<\x8e\xf8\xbb\xff\xd2UA\x82\t\xb0\x97\xde(e\x19h\xbc\xa9\xaeu\xf3\xee\x07\x1c\xd6\xd9\xddL\x8b\x08\xd1)1\xac\xe2/L\xf4\xd2D\xdf\xba y\xbb\x9d\x8d7\xda\xd2\xee\xf1\xd8\x1e\xd6\n2\x08\x95\xef\xbel\x1bZp\xc8\x08k^\xda\td=\xfa\xc9\xbe\xfbD\x85\xcf+\xd6\x9a\xb3s\x84\xe8D\xbb\x16\x86\x88\xc4\x94~O\xb8\xfa&R \x96I84M\xcb\x10\xb01O\xe1\xb4\x0e\x8c\x05n{\x94\x87[\xe5\x0e\x9d%9B\xf2\x06\xd1\xd4\x05\xb1\x15\xac\xcb\xe0Z\x15\xe9\x9b\xd5\xf5-GZ)\x00\xa1\xab\xb9\xce\x05\x1f~\xfeX\xf4\x87\xf8\xfc/\xf5\xb8\xc3\x0e\xe5=\xb1n\x1e\x12\xf7\x87\'\xb97txlgW\xec\x7f\x06M\x94\xce\xe8[e\xbc\x10T\xd4GW\xfb~\xf05\x1f\xfab@\xfcd$+\x07\xb2f\xc6\x99\xe5)\x88\xc1\xf3G\xdc\x86\x84D\xd6\x86\xc7,\x8d$\xc1\xfc\n\xea\x10\xd5\xbf\x9c)\xe7\xd6\x0e\x9a}KY{h\xc1\xde\x0b\xe9\xbb\x1e\x07\xf8\xae\x10\xd3hP\xf79\x90\xd6\x9c\x95\x1a\xde\x84\xe6\xb5\x9c\xb91cpd\x04X\xea7\x06v\xa2\xa9\x8d\x9chM!Sp6o\xf6!\n\xb1\xe7*\xb5\x14C\xd4F\xd6\xb5\x84\xd0\xc5\xdc\xb0\xb1\x19n\xc4\xbf\x85n\xfaZRQ\xe3\n\xd3k\xe0F\xf9\to\xae\xb9r?\x05\xcd\x86q]\xe5:Qe\xe9\xd1Q\xf6\xd9\xe5\x03\x8c\xa0\xdd$jO\x92\xe88\x7fS\x92$\xffV*\x08\xd2\xc4vPk\x01\xf6e\xc1\xf3'
print('------------')
print('Encrypted Message')
print(enc)
print('------------')
print('Decrypted Message')
dec = decrypt(enc, private_key)
print(dec.decode('utf-8'))
print('------------')

