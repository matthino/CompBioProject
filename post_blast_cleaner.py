def postBLASTFormat(file):
    # open the file for formatting
    f = open(file, "r")

    entireText = f.read()
    f.close()
    
    outName = file[:len(file)-4] + "_clean.txt"
    output = open(outName, "w")

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
    
    # maintain a counter, used as prefix for each sequence
    seqcounter = 1
    # format every sequence in the file.
    while(True):

        # Find the sequence until the next '>' char
        pos1 = pos2
        pos2 = entireText.find('>', pos1 + 1)

        # If we've gone to the end of the text, exit.
        if(pos2 < pos1):
            break

        # Get the cleaned and nicely formatted sequence
        sequence = formatter(entireText[pos1:pos2], seqcounter)
        seqcounter += 1
        
        # Write the cleaned sequence to the output file
        output.write(sequence)
        output.write("\r\n")


    # close and exit
    output.close()
    print("done cleaning.")




# Formats the first line in each FASTA sequence and also
# ensures the sequence is 60 characters per line.
# i.e. >Count_Organism_Name_certain_gene,_partial_seq:_experiment_name
def formatter(sequence, count):
    # get the first line
    endFirstLine = sequence.find("\n", 1)
    firstPart = sequence[1:endFirstLine]
    firstPart = ">" + str(count) + "_" + firstPart.replace(" ", "_")

    # Now put the rest of the sequence 60 char/line
    sequence = sequence[endFirstLine:].replace("\r", "").replace("\n","")
    sequence = makeNice(sequence)

    return firstPart + "\r\n" + sequence


# This function takes a long string and it returns
# a string that has 60 characters per line.
def makeNice(sequence):
    output = ""
    for i in range(0, len(sequence), 60):
        output += sequence[i:i+60] + "\r\n"

    return output


#############################################
#############################################
postBLASTFormat("Clean_Micro_ident_Final.txt")
