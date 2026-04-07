import re
seq = "AAGAUACAUGCAAGUGGUGUGUCUGUUCUGAGAGGGCCUAAAAG" # The given RNA sequence
pattern = r"AUG(?:[ACGU]{3})*?(?:UAA|UAG|UGA)" # starts with AUG, ends with stop codon
all_ORF = re.findall(pattern, seq) # Use re.findall() to extract all valid ORFs

# Use re.search() to check if any ORF exists
if re.search(pattern, seq): # If at least one ORF is found
    longest_ORF = max(all_ORF, key=len) # Find the longest ORF using max() with key=len
    print("Longest ORF sequence:", longest_ORF) # Print the longest ORF sequence
    print("Length:", len(longest_ORF)) # Print the longest ORF
else:
    print("No ORF is found.") # If no ORF is found, print it