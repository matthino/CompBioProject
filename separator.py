#!/usr/bin/python

####################################
# Computational Biology Project Code
#
# @authors: Matt Hino, Steven Lind
# @authors: Julia Meng, Shaun Stice
# @version: December 9, 2015
####################################

# The main purpose of this script is to
# look through the post blast results and
# separate the sequences into text files.
#
# We are seperating the sequences in the
# following manner:
# 1. Bacillus   2. Pseudomonas 3. Other
def separate(file):
    # open the input file and read
    inputFile = open(file, "r")
    entireText = inputFile.read()
    inputFile.close()

    # ensure the file is in FASTA file format
    if (entireText[0] == '>'):
        print("in FASTA format")
    else:
        print("invalid format")
        return

    # sepList[0] = bacillus, etc. 
    sepList = []




# In order to separate the sequences, we first
# need to know all of the different names of
# the sequences. (Bacillus, Pseudomonas, etc.)
# This was created to get a general sense of the
# distribution of organisms, and which would have
# enough sequences to be put in their own .txt file
def nameFinder(text):
    nameList = {}

    # variables to keep track of the current and next
    # occurance of the '>' character
    pos1 = 0
    pos2 = 0

    # For all of the sequences in the text:
    #   - Search for the first and last 5 consecutive
    #      nucleotide subsequence and trim the sequence
    #   - Write the subsequence to the text file
    while(True):

        # Find the sequence (goes until the next '>')
        pos1 = pos2
        pos2 = text.find('>', pos1 + 1)

        # If we've gone to the end of the text, or no > exits, exit.
        if(pos2 < pos1):
            break

        # Look for the first 'word' after the number in the first line
        seq = text[pos1:pos2]
        endOfFirstLine = seq.find("\n", 1)
        firstLine = seq[:endOfFirstLine].split("_")
        
        # remove all '' from the firstLine list
        # [firstLine for word in firstLine if not word.strip()]

        print(firstLine)

        # Add the name to the list.
        if( len(firstLine) > 1):

            # First ensure that the name is only alphanumeric
            regex = re.compile('[^a-zA-Z]')
            name = regex.sub("", firstLine[1])
            
            if name not in nameList:
                nameList[name] = 0
            nameList[name] += 1

    print(nameList)


####################################
separate("Clean_Micro_ident_Final_clean.txt")




        


