# Input the initial number of infected students and the growth rate of infected individuals
# The total number of students n is 91.
# Repeat:
#    Calculate the number of infected students after one day by multiplying the current number of infected students by the growth rate.
#    Print the number of infected students and the day number.
#    if the number of infected students > total numberof students
#        Repeat
#    if else
#        Done
# print the day that all of students were infected
Infected_number = float(input("Please enter initial number of infected students: "))
Growth_Rate = float(input("Please enter growth rate of infected individuals: "))
Growth_Rate += 1
n = 91
i = 1
while True:
    if Infected_number <= n:
        Infected_number *= Growth_Rate
        print(f"The infected number is {Infected_number:.1f}  It's the {i}th day")
        i += 1
    else:
        break
print(f"The {i - 1}th day, all of the 91 students were infected")