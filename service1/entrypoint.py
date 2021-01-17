#inp[0] je ime hash funkcije
#ostatak inp je poruka koju zelimo hashirati

import sys
import hashlib

#inp = sys.stdin.readline()  
#inp = "testni primjer"
inp = []
while True:
    input = sys.stdin.readline()
    if input == '\n':
        break
    inp.append(input)

#hash_func = "md5"
hash_func = inp[0].strip()  #ukloni viska razmake s pocetka i kraja
message = ('\n'.join(inp)).strip() 
h = hashlib.new(hash_func)  
h.update(str.encode(message))  #str.enc... je element klase 'bytes' tocno kako nam treba
print(h.hexdigest())
