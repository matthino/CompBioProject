#!/usr/bin/python

####################################
# Computational Biology Project Code
#
# @authors: Matt Hino, Steven Lind
# @authors: Julia Meng, Shaun Stice
# @version: November 30, 2015
####################################

# Given FASTA formatted sequences in a .nt file (inputFile),
# this function cleans the sequences by trimming
# the leading and trailing 'N's. It does this by
# searching for the first and last occurance of 5 known
# nucleotides. Then, it outputs the cleaned data to
# an output file, Cleaned_inputFile.txt).
#
# ex.
# Prior to clean: NNNNANNCCTTGNAATCTCTAANANNANNN
# After cleaning: CCTTGNAATCTCTAA
def cleanNT(file):
    # open the input file for reading & output for writing
    inputFile = open(file, "r")
    out = "Cleaned_" + file[:-3] + ".txt"
    output = open(out, 'w')

    # read the entire file, and close.
    entireText = inputFile.read()
    inputFile.close()

    # ensure the file is in FASTA file format
    if (entireText[0] == '>'):
        print("in FASTA format")
    else:
        print("invalid format")
        output.close()
        return

    # variables to keep track of the current and next
    # occurance of the '>' character
    pos1 = 0
    pos2 = 0

    
    # For all of the sequences in the .nt file:
    #   - Search for the first and last 5 consecutive
    #      nucleotide subsequence and trim the sequence
    #   - Write the subsequence to the text file
    while(True):

        # Find the sequence until the next '>' char
        pos1 = pos2
        pos2 = entireText.find('>', pos1 + 1)

        # If we've gone to the end of the text, exit.
        if(pos2 < pos1):
            break

        # Get the cleaned and nicely formatted sequence
        sequence = cleaner(entireText[pos1:pos2])
##        print(sequence) # for debugging
            

        # Write the cleaned sequence to the output file
        output.write(sequence)
        output.write("\r\n")

    # close and exit
    output.close()
    print("done cleaning.")



# Trims the leading and trailing 'N's. It does this by
# searching for the first and last occurance of 5 known
# nucleotides. Returns the trimmed sequence
def cleaner(sequence):
    # Save the '>Organism Name' part of the sequence
    endFirstLine = sequence.find("\n", 1)
    firstPart = sequence[:endFirstLine] # add one to compensate second char

    # Now look at the rest of the sequence.
    sequence = sequence[endFirstLine:].replace("\r", "").replace("\n","")

    start = 0
    end = 0
    # Find the new start (first instance of 5 nucleotides)
    for i in range(len(sequence)):
        if( 'N' not in sequence[i:i+5]):
            start = i
            break
        
    # Then find the end (last instance of 5 nucleotides)
    for j in range(len(sequence), endFirstLine, -1):
        if( 'N' not in sequence[j-5: j]):
            end = j
            break

    # Format the sequence (60 char/line) and return it
    sequence = makeNice(sequence[start:end])

    return firstPart + "\r\n" + sequence


# This function takes a long string and it returns
# a string that has 60 characters per line.
def makeNice(sequence):
    output = ""
    for i in range(0, len(sequence), 60):
        output += sequence[i:i+60] + "\r\n"

    return output

# Given a file, counts the length of each sequence and
# returns a list of (sequence_name, length) tuples.
# Output the results to a text file.
def countLengths(filename):
    # open and read in the input file
    inputFile = open(filename, "r")
    entireText = inputFile.read()
    inputFile.close()

    # ensure the file is in FASTA file format
    if (entireText[0] == '>'):
        print("in FASTA format")
    else:
        print("invalid format")
        return

    output = open(filename[:-4] + "_lengths.txt", "w")

    # a list of lengths to be returned
    length_list = []

    pos1 = 0
    pos2 = 0

    while(True):
        # Find the sequence until the next '>' char
        pos1 = pos2
        pos2 = entireText.find('>', pos1 + 1)

        # If we've gone to the end of the text, exit.
        if(pos2 < pos1):
            break

        sequence = entireText[pos1: pos2+1]
        
        endFirstLine = sequence.find("\n", 1)
        name = sequence[1:endFirstLine]

        sequence = sequence[endFirstLine:].replace("\r", "").replace("\n","")
        length = len(sequence)

        length_list.append( [name, length] )

    # write the list to the output file, and close it
    output.write(listToString(length_list))
    output.close()
    
    return length_list


# Takes the list of sequence names and corresponding lengths,
# and turns it into a nice string.
def listToString(l):
    returnString = ""
    
    for i in l:
        returnString += i[0] + " length: " + str(i[1]) + "\n"
        
    return returnString

#####################
#### Run the code ###
cleanNT("Micro-Seq.nt")
countLengths("Cleaned_Micro-Seq.txt")
