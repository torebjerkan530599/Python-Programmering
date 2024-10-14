'''
*** The Assignment:
Biologists use a sequence of the letters A, C, T, and G to model a genome.

A gene is a substring of a genome that starts after a triplet ATG and ends before a triplet TAG, TAA, or TGA.
Furthermore, the length of a gene string is a multiple of 3, and the gene does not contain any of the triplets ATG, TAG, TAA, or TGA.
Write a program that prompts the user to enter a genome and displays all genes in the genome.
If no gene is found in the input sequence, display “no gene is found”.

Here are the sample runs:

<output>
Enter a genome string: TTATGTTTTAAGGATGGGGCGTTAGTT <enter icon>

TTT
GGGCGT

<end output>


<output>
Enter a genome string: TGTGTGTATAT <enter icon>

no gene is found

<end output>

MERK:
De som vil kan implementere dette som en funksjon, input stremgen som skal undersøkes. Returverdien skal da være en streng med alle gener funnet, adskilt med komma, f eks relatert til første kjøring over:
TTT,GGGCGT



'''

'''
Beskrivelse av hva jeg forandret i koden:

Jeg gjorde først om koden til en funksjon som jeg puttet i en klasse og fulgte anbefalingene i oppgaven.
Deretter oppdaget jeg i en av testene at jeg ikke kontrollerer om input kun benytter tegnene 'A','T','C' og'G'
Tilføyde derfor en kontroll først i funksjonen som undersøker om det forekommer irrelevante tegn 

# Noen sekvenser for testing
# genome = "TTATGTTTTAAGGATGGGGCGTTAGTT"
# genome = "TGTGTGTATAT"
# genome = "TCCACGATTGAATGGTTGTCTTTCCC"
# genome = "AATGGTGTGACATGTAAACACATTATGXXX"

# O2: Liang 5.6extra
# generate random DNA sequence : https://molbiotools.com/randomsequencegenerator.php

'''
class GeneFinder:
    
    def findGenes(self,genome : str) -> list:
        
        valid_letter_count = genome.count('T') + genome.count('A') + genome.count('G') + genome.count('C')
        
        if(valid_letter_count != len(genome)):
            return "Invalid symbol detected"    
        
        sequence = "" # will contain all substrings of the gene
        pos_ATG = genome.find("ATG") # find returns -1 on failure
        if(pos_ATG != -1):
            for v in range(pos_ATG + 3, len(genome), 3) :
                gene = genome[v:v+3] # a gene is a multiple of three
                if(gene != "TAG" and gene !="TAA" and gene != "TGA" and gene != "ATG") :
                    sequence += gene # accumulate genes
                else:
                    genome = genome[pos_ATG + 3:]  #advance search string
                    pos_ATG = genome.find("ATG") # find next position
                    if(pos_ATG != -1):
                        sequence += ',' # seperate strings of genes   

        return sequence if(len(sequence)) > 0 else "No genes found"
        
if __name__ == "__main__":
    gene = GeneFinder()
    #print(gene.findGenes("TTATGTTTTAAGGATGGGGCGTTAGTT"))
    seq = gene.findGenes("TTATGTTTTAAGGATGGGGCGTTAGTT")
    print(seq)

    
    
