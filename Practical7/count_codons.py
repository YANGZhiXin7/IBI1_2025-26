import re
import matplotlib.pyplot as plt
# fasta file name
filename = "Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"
# ask user for stop codon
stop_codon = input("Enter a stop codon (TAA, TAG or TGA): ").upper()
# check input
if stop_codon != "TAA" and stop_codon != "TAG" and stop_codon != "TGA":
    print("Invalid input")
    quit()

# read fasta file
file = open(filename, "r")
# parse fasta file into list of [header, sequence]
sequences = []
header = ""
sequence = ""
# read file line by line
for line in file:
    line = line.strip()

    if line[0] == ">":
        if header != "":
            sequences.append([header, sequence])
        header = line
        sequence = ""
    else:
        sequence = sequence + line.upper()
# add the last sequence
if header != "":
    sequences.append([header, sequence])
file.close()
# dictionary for codon counts
codon_counts = {}
# check each sequence
for item in sequences:
    header = item[0]
    sequence = item[1]
    # regular expression for ORF
    pattern = "ATG(?:[ACGT]{3})*" + stop_codon
    matches = re.finditer(pattern, sequence)

    longest_orf = ""

    for match in matches:
        orf = match.group()

        # make sure length is multiple of 3
        if len(orf) % 3 == 0:
            if len(orf) > len(longest_orf):
                longest_orf = orf

    # count codons before stop codon
    if longest_orf != "":
        part_before_stop = longest_orf[:-3]
        codon_list = re.findall(r"...", part_before_stop)

        for codon in codon_list:
            if codon in codon_counts:
                codon_counts[codon] = codon_counts[codon] + 1
            else:
                codon_counts[codon] = 1

# print results
if len(codon_counts) == 0:
    print("No genes found with stop codon", stop_codon)
else:
    print("Codon counts for", stop_codon)
    for codon in sorted(codon_counts):
        print(codon, codon_counts[codon])

# plot pie chart
    labels = list(codon_counts.keys())
    sizes = list(codon_counts.values())

    plt.figure(figsize=(14, 14), dpi=120)

    wedges, texts, autotexts = plt.pie(
        sizes,
        labels=labels,
        autopct='%1.1f%%',
        startangle=90,
       labeldistance=1.1,
       pctdistance=0.82,

      textprops={'fontsize': 9},
    )
    plt.setp(autotexts, size=7, weight='bold')
    plt.title('Codon usage for stop codon ' + stop_codon, fontsize=14, pad=20)
    plt.savefig("codon_usage_" + stop_codon + ".png", bbox_inches='tight', dpi=300)
    plt.close()
