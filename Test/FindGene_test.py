from FindGene import GeneFinder  # The code to test
import unittest   # The test framework

class Test_genome(unittest.TestCase):
    
    def setUp(self):  # RUNS BEFORE EACH TEST!
        self.__gene_detector = GeneFinder()
    
    def test_emty_string(self):
        result = self.__gene_detector.findGenes("")
        self.assertEqual(result, "No genes found")    

    def test_rubbish_string(self):
        result = self.__gene_detector.findGenes("I AM A STRING WITH NO GENES WHATSOEVER")
        self.assertEqual(result, "Invalid symbol detected")
        
    def test_sequence_is_invalid(self):
        result = self.__gene_detector.findGenes("TTATGTTTT")
        self.assertNotEqual(result, "TTT")
    
    def test_sequences_is_valid(self):
        result = self.__gene_detector.findGenes("TTATGTTTTAA")
        self.assertEqual(result, "TTT")
        
    def test_sequence_is_correct_length(self):
        result = self.__gene_detector.findGenes("TTATGTTTTAAGGATGGGGCGTTAGTT")
        isMultipleOfThree = len(result) % 3
        self.assertTrue(isMultipleOfThree == 0)
    
    def test_sequence_is_incorrect_length(self):
        result = self.__gene_detector.findGenes("TTATGTTTTAAGGATGGGGCGAGT")
        isMultipleOfThree = len(result) % 3
        self.assertFalse(isMultipleOfThree == 0)
    
    def test_contains_valid_triplets(self):
        result = self.__gene_detector.findGenes("TCCATAGCGATTGAATGGTTGTCTTAATCC")
        result.replace('TGA','???').replace('TAG','???').replace('TAA','???')
        self.assertNotIn('???',result)
    
    def test_find_genes_only_start_codon(self):
        result = self.__gene_detector.findGenes("ATG")
        self.assertEqual(result, "No genes found")
        
    def test_find_genes_multiple_start_codons(self):
        genome_multiple_start_codons = "ATGAAATGTTTATGAGA"
        result = self.__gene_detector.findGenes(genome_multiple_start_codons)
        self.assertEqual(result, "AAATGTTTA")
    
    def test_gene_with_internal_stop_codon(self):
        genome = "ATGACATAG"
        result = self.__gene_detector.findGenes(genome)
        self.assertEqual(result, "ACA")
        
    def test_invalid_character(self):
        genome = "TTATGTTpTAA"
        result = self.__gene_detector.findGenes(genome)
        self.assertEqual(result, "Invalid symbol detected")
        
        
    

    
        
    # def test_sequene_is_incorrect_length(self):
    #     result = self.__gene_detector.findGenes()

if __name__ == '__main__':

    unittest.main()