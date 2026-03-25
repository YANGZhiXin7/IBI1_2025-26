# What does this piece of code do?
# Answer: This code simulates generating 10 random numbers between 1 and 10 (inclusive) and calculates their total sum.
# The variable total_rand stores the cumulative sum of the generated random numbers, while the variable progress counts how many numbers have been generated.
# Once the loop finishes executing, the program prints the total sum of all the random numbers.

# Import libraries
# randint allows drawing a random number,
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil

total_rand = 0 # This variable will store the total sum of the random numbers generated.
progress=0 # This variable counts how many random numbers have been generated.
while progress<=10: # The loop will continue until 10 random numbers have been generated
	progress+=1 # count the number of random numbers generated
	n = randint(1,10) # Generate a random number between 1 and 10
	total_rand+=n # Add the generated random number to the total sum.

print(total_rand) 

