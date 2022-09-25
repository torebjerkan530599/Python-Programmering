# O2: Liang 5.6extra
# generate random DNA sequence : https://molbiotools.com/randomsequencegenerator.php

# Gene should have a terminating codone(TAG, TAA, TGA)
genome = input("Enter a genome string").upper()
# some sequences for testing without typing:
# genome = "TTATGTTTTAAGGATGGGGCGTTAGTT" 
# genome = "TGTGTGTATAT"
# genome = "TCCACGATTGAATGGTTGTCTTTCCC"
# genome = "AATGGTGTGACATGTAAACACATTATGXXX"

pos_ATG = genome.find("ATG")
sequence = "" # will contain all substrings of the gene

if(pos_ATG != -1):
    for v in range(pos_ATG + 3, len(genome), 3) :
        gene = genome[v:v+3] # a gene is a multiple of three
        if(gene != "TAG" and gene !="TAA" and gene != "TGA" and gene != "ATG") :
            sequence += gene # accumulate genes
        else:
            genome = genome[pos_ATG + 3:]  #advance search string
            pos_ATG = genome.find("ATG") # find next position   

if(len(sequence) > 0) : 
    print(sequence)
else :
    print("no gene is found")