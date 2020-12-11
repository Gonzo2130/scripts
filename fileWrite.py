#!/usr/bin/env python3

# Open file for writing
fileObj = open("samplewrite.txt", 'w+')

# Write a line to the file
'''
fileObj.write("This is a line\n")
contents = "More and more lines\n \
    this is another line\n \
        30th is Halloween\n"
fileObj.write(contents)
fileObj.write("Another line at the end")
'''
fileObj.write("File is clobbered")
fileObj.close()