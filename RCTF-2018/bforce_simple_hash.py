#!/usr/bin/env python

# Connection to 149.28.139.172 10002 port [tcp/*] succeeded!
# sha256(****+DEHI8mXFknPYhNtI) == 8be2e4ec4c7a9e46b22d537a451d7f6139c3c68bbe68c54d02f83e715e8709f6
# Give me XXXX:


import hashlib
import sys

count = 0
given = 'M8HgqmsgyZY52aj6'
#for seed in range (0000,10000):
for seed in range (0000,10000): 
    hash_obj = hashlib.sha256(str(seed)+given).hexdigest()
    #print(str(seed)+given) + '\n'

    other = 'e48d2886ef8fa75f10a232fd3d7295aca1eaa56ab3ad807f820af106c1c83b01'

    #other = hashlib.sha256(b'5').hexdigest()
    if (hash_obj == other): 
        print 'TRUE' + ' at ' + str(count+1)
        break
    else: 
       count += 1

#hash_obj = hashlib.sha256(b'1111')
#print(hash_obj.hexdigest())


#print('\n' + '==========================' + '\n')
#hash_next = hashlib.sha256(b'0002+u6tTbdAwG3sNGNso').hexdigest()
#print 'Demo = '+hash_next

