#! /Users/stephenlang/anaconda/bin/python
#madLibs.py reads in a text file and lets the user add their own 
#adjectives, verbs, and nouns.

import os, re
#Read in a text file and store its contents in a var
madLib = open(os.path.join(os.getcwd(),'madLibs.txt'))
madLibContent = madLib.read()

# Take in the user input and store it
replacements = []
print('Enter an adjective:')
replacements.append(input())

print('Enter a noun:')
replacements.append(input())

print('Enter a verb:')
replacements.append(input())

print('Enter a noun:')
replacements.append(input())



#create a regex obj for the input fields in the text file
#swap the place holders for the input values
for i in range(len(replacements)):
    print(replacements[i])
    replaceRegex = re.compile(r'REPLACE'+str(i+1))
    madLibContent = replaceRegex.sub(replacements[i], madLibContent)
#Print the results to the screen and save them to a new text file
print(madLibContent)
