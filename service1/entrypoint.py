#inp[0] je (valjda) ime hash funkcije
#ostatak inp je poruka koju zelimo hashirati

import sys
import hashlib

#inp = sys.stdin.readline()    #ko input() samo cita \n
inp = "fwatchdog"
#inp = []
#while True:
#    input = sys.stdin.readline()
#    #print(repr(inp))
#    if input == '\n':
#        break
#    inp.append(input)

hash_func = "md5"
#hash_func = inp[0].strip()  #ukloni viska razmake s pocetka i kraja
message = ('\n'.join(inp)).strip()  #join spoji sve iz inp[1:] u jedan string, a elemente odvoji \n. strip radi isto kao i gore, ali za novi string
h = hashlib.new(hash_func)  #h je varijabla tipa hashlib.HASH
h.update(str.encode(message))  #str.enc... je element klase 'bytes' tocno kako nam treba, da je h bio neki hashirani string onda
                               #bi se na njegovu bazu dodao str.enc.... i onda to hashiralo, npr 'abc' -->hash u h, h.update('def') --> hash od 'abcdef' u h
print(h.hexdigest())