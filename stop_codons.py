import re
input_file = "Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"
output_file = "stop_genes.fa"

with open(input_file) as f:
    data = f.read() # Read the content of the file into data
entries = data.split(">")[1:] # Split the data into entries based on the '>' character, and ignore the first empty entry
out_file = open(output_file, "w") # Open the output file for writing, and assign the file object to 'out'

for entry in entries:
    lines = entry.split("\n") # Split the entry into lines
    header = lines[0] # The first line of the entry is the header
    seq = "".join(lines[1:]).upper() # Join the remaining lines into a single string, convert it to uppercase

    gene_name = header.split()[0] # Extract the gene name from the header

    pattern = r'ATG(?:...)*?(?:TAA|TAG|TGA)' # Regular expression pattern to match ORFs that start with ATG and end with one of the stop codons TAA, TAG, or TGA
    matches = re.findall(pattern, seq) # Use re.findall() to find all matches of the pattern in the sequence

    longest_orf = "" # Keep track of the longest ORF found
    stop_codon = "" # Keep track of the stop codon associated with the longest ORF

    for i in matches:
        if len(i) % 3 == 0: # Check if the length of the match is a multiple of 3
            if len(i) > len(longest_orf): # If the length of the current match is greater than the length of the longest ORF found so far
                longest_orf = i # Update longest_orf to the current match
                stop_codon = i[-3:] # Update stop codon

    if longest_orf:
        out_file.write(f">{gene_name} stop:{stop_codon}\n")
        for i in range(0, len(seq), 60): 
            out_file.write(seq[i:i+60] + "\n") 

out_file.close()
print("Finished. Output saved to stop_genes.fa")