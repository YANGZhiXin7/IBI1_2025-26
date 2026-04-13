def protein_mass(sequence):
    # Define the mass of each amino acid in atomic mass units (amu)
    aa_mass = {
        "G": 57.02,
        "A": 71.04,
        "S": 87.03,
        "P": 97.05,
        "V": 99.07,
        "T": 101.05,
        "C": 101.01,
        "I": 113.08,
        "L": 113.08,
        "N": 114.04,
        "D": 115.03,
        "Q": 128.06,
        "K": 128.09,
        "E": 129.04,
        "M": 131.04,
        "H": 137.06,
        "F": 147.07,
        "R": 156.10,
        "Y": 163.06,
        "W": 186.08
    }

    total_mass = 0 # Initialize total mass to zero

    for aa in sequence:
        if aa in aa_mass:
            total_mass += aa_mass[aa] # Add the mass of the amino acid to the total mass
        else:
            print("Error: Unknown amino acid:", aa) # Print an error message if an unknown amino acid is encountered
            return None

    return total_mass

# main program
sequence = input("Please enter the protein sequence (using single-letter amino acid codes): ")
print("Protein mass:", protein_mass(sequence), "amu")
