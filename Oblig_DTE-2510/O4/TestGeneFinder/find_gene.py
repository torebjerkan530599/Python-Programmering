'''
Beskrivelse av hva jeg forandret i koden:

Jeg gjorde først om koden til en funksjon som jeg puttet i en klasse og fulgte anbefalingene i oppgaven.
Deretter oppdaget jeg i en av testene at jeg ikke kontrollerer om input kun benytter tegnene 'A','T','C' og'G'
Tilføyde derfor en kontroll først i funksjonen som undersøker om det forekommer irrelevante tegn 

# some sequences for testing
# genome = "TTATGTTTTAAGGATGGGGCGTTAGTT" 
# genome = "TGTGTGTATAT"
# genome = "TCCACGATTGAATGGTTGTCTTTCCC"
# genome = "AATGGTGTGACATGTAAACACATTATGXXX"

# O2: Liang 5.6extra
# generate random DNA sequence : https://molbiotools.com/randomsequencegenerator.php

# Gene should have a terminating codone(TAG, TAA, TGA)

'''

class GeneFinder:
    
    def findGenes(self,genome : str) -> list:
        
        valid_letter_count = genome.count('T') + genome.count('A') + genome.count('G') + genome.count('C')
        
        if(valid_letter_count != len(genome)):
            return "Invalid symbol detected"    
        
        sequence = "" # will contain all substrings of the gene
        pos_ATG = genome.find("ATG")
        if(pos_ATG != -1):
            for v in range(pos_ATG + 3, len(genome), 3) :
                gene = genome[v:v+3] # a gene is a multiple of three
                if(gene != "TAG" and gene !="TAA" and gene != "TGA" and gene != "ATG") :
                    sequence += gene # accumulate genes
                else:
                    genome = genome[pos_ATG + 3:]  #advance search string
                    pos_ATG = genome.find("ATG") # find next position   
    
        return sequence if(len(sequence) > 0) else "No genes found"
        
if __name__ == "__main__":
    gene = GeneFinder()
    #print(gene.findGenes("TTATGTTTTAAGGATGGGGCGTTAGTT"))
    print(gene.findGenes("TTATGTTTTAAGGATGGGGCGTTAGTT"))
    #print(gene.findGenes("AAAA"))
    
    
