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
# i.e. all Bacillus in a Bacillus.txt file
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

    # Get a list of all the unique sequence names
    nameList = nameFinder(entireText)

    print(nameList)




# In order to separate the sequences, we first
# need to know all of the different names of
# the sequences. (Bacillus, Pseudomonas, etc.)
def nameFinder(text):
    nameList = []

    # variables to keep track of the current and next
    # occurance of the '>' character
    pos1 = 0
    pos2 = 0

    
    # For all of the sequences in the text:
    #   - Search for the first and last 5 consecutive
    #      nucleotide subsequence and trim the sequence
    #   - Write the subsequence to the text file
    while(True):

        # Find the sequence until the next '>' char
        pos1 = pos2
        pos2 = text.find('>', pos1 + 1)

        # If we've gone to the end of the text, or no > exits, exit.
        if(pos2 < pos1):
            break

        # Look for the first 'word' after the number in the first line
        endOfFirstLine = text[pos1:pos2].find("\n")
        firstLine = text[pos1:endOfFirstLine].split("_")
        
        # remove all '' from the firstLine list
        [x for x in firstLine if x]

        # Add the name to the list.
        if( len(firstLine) > 1):
            if( firstLine[1] not in nameList):
                nameList.append(firstLine[1])

            
    print(nameList)
    return nameList



####################################
separate("Clean_Micro_ident_Final_clean.txt")




        


