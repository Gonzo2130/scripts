#!/usr/bin/env python3
import time

testPassword = 'goodPassword007!'
UPPERCASE = 'ABCDEFGHIJKLMONPQRSTUVWXYZ'

for t in testPassword:
    print(t)
    #print(testPassword)
    time.sleep(0.5)
    if t in UPPERCASE:
        print("found", t, "in UPPERCASE" )

'''
Complete this script to check if a password
has
- one Uppercase letter,
- one lowercase letter,
- one number
- one special character
- minimum password length of 8
==== EXTRA ====
-does not have 3 repetitive characters gooodPassword007!
-put this as a function
-check against the function
==== EXTRA ====
'''
