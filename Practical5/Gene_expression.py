# Create dictionary and add a new gene
Genes = {"TP53":12.4,"EGFR":15.1,"BRCA1":8.2,"PTEN":5.3,"ESR1":10.7} # dictionary of genes and their expression levels
Genes["MYC"] = 11.6 # add a new gene MYC and its expression level
for gene in Genes:
    print(f"{gene}: {Genes[gene]}") # print the gene names and their expression levels

# create a bar plot
import matplotlib.pyplot as plt
import numpy as np

N = len(Genes) # number of genes in the dictionary
x = np.arange(N) # x-axis values for the bar plot
y = list(Genes.values()) # y-axis values for the bar plot
plt.bar(x, y) # create a bar plot
plt.xticks(x, list(Genes.keys())) # set the x-axis ticks to be the gene names
plt.xlabel("Genes") # set the x-axis label
plt.ylabel("Expression Level") # set the y-axis label
plt.title("Gene Expression Levels") # set the title
plt.show() # show the plot

# Display the expression level of a specific gene
SelectedGene = "MYC" # You can change this to any gene in the dictionary to check its expression level
if SelectedGene in Genes:
    print(f"The expression value for {SelectedGene} is {Genes[SelectedGene]}")
else:
    print(f"Gene '{SelectedGene}' is not in the dataset.")

# Calculate and print the average expression level
AverageExpression = sum(y) / len(y)
print(f"The average gene expression level{AverageExpression:.2f}")

