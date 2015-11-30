#!/usr/local/bin/python

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
def cleanNT(inputFile):
    # open the file for reading
    inputFile = open(inputFile, "r")

    # ensure the file is in FASTA file format
    header = file.readline()
    if (header[0] == '>'):
        print("in FASTA format")
    else:
        print("invalid format")
        inputFile.close()
        return

    # open the file for output
    out = "Cleaned_" + inputFile
    output = open(out, 'w')

    # read the entire file, and close.
    entireText = inputFile.read()
    file.close()

    # get rid of newline characters.
    entireText = entireText.replace("\r", "")
    entireText = entireText.replace("\n", "")

    # variables to keep track of the current and next
    # occurance of the '>' character
    pos1 = 0
    pos2 = 0
    done = False
    
    # For all of the sequences in the .nt file:
    #   - Search for the first and last 5 consecutive
    #      nucleotide subsequence and trim the sequence
    #   - Write the subsequence to the text file
    while(not done):

        # Find the next subsequence to clean
        pos1 = pos2
        pos2 = entireText.find(">", pos1 + 1)

        # Check if we're cleaning the last sequence
        if(pos2 == -1):
            done = True
            pos2 = len(sequence)

        # Get the sequence
        sequence = entireText[pos1:pos2]

        # Clean the front of sequence
        for i in range(len(sequence)):
            if( "N" not in sequence[i:i+5]):
                start = i
                break
        # Then clean the back
        for i in range(len(sequence), 0, -1):
            if("N" not in sequence[i-5, i]):
                end = i
                break

        # Write the cleaned sequence to the output file
        output.write(string)
        output.write("\r\n")

    # close and exit
    output.close()
