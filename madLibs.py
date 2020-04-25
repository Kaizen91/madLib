#! /Users/stephenlang/anaconda/bin/python
#madLibs.py reads in a text file and lets the user add their own 
#adjectives, verbs, and nouns.

import os, re
#To Do: Read in a text file and store its contents in a var
madLib = open(os.path.join(os.getcwd(),'madLibs.txt'))
madLibContent = madLib.read().split()

#To Do: Take in the user input and store it in variables
print('Enter an adjective:')
adj = input()

print('Enter a noun:')
noun1 = input()

print('Enter a verb:')
verb = input()

print('Enter a noun:')
noun2 = input()

#To Do: Search the text file var for the NOUN, ADJECTIVE, VERB flags and
#replace them with the user' input

    #create a regex obj for each input field in the text file
    #swap the place holders for the input values


#To Do: Print the results to the screen and save them to a new text file