#!/usr/bin/env python3
# Open file for reading
fileobject = open("greetings.py", 'r')

# read the contents of the file
#contents = fileobject.read()
contents = fileobject.readlines()
for line in contents:
    print(line.strip())

fileobject.close()

# Open the file for writing
