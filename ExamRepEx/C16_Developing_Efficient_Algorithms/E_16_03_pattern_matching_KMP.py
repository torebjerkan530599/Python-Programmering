
def kmp_search(s1, s2):
    def compute_lps(pattern):
        lps = [0] * len(pattern)
        length = 0
        i = 1
        
        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps

    n = len(s1)
    m = len(s2)
    lps = compute_lps(s2)
    
    i = 0  # index for s1
    j = 0  # index for s2
    
    while i < n:
        if s2[j] == s1[i]:
            i += 1
            j += 1
        
        if j == m:
            print(f"matched at index {i - j}")
            return
        
        elif i < n and s2[j] != s1[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    
    print("no match found")

# Sample run
s1 = input("Enter a string s1: ")
s2 = input("Enter a string s2: ")
kmp_search(s1, s2)


'''
Preprocessing the Pattern:

The compute_lps function preprocesses the pattern (second string s2) to create the longest prefix suffix (LPS) array.

The LPS array helps in determining the next positions of the pattern to be matched after a mismatch, thus reducing the number of comparisons.

This preprocessing takes 𝑂 ( 𝑚 ) O(m) time, where 𝑚 m is the length of s2.

Searching the Pattern in the Text:

The main part of the algorithm iterates over the text (first string s1) and tries to match it with the pattern.

When a mismatch occurs, the LPS array is used to skip some characters without rechecking them.

The search process also runs in 𝑂 ( 𝑛 ) O(n) time, where 𝑛 n is the length of s1.

Preprocessing the Pattern: O(m)
Searching the Pattern in the Text:O(n)
Overall Time Complexity: O(n+m)


'''

