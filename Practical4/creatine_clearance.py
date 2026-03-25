# input age and check if age is between 0 and 100
#           if not : print "Please enter your age again" and re-input
# input weight and check if weight is between 20 and 80
#           if not : print "Please enter your weight again" and re-input
# input gender and check if gender is male or female
#           if not : print "Please enter your gender again" and re-input
#           if gender is female, weight should be multiplied by 0.85
# input Cr and check if creatine concentration is between 0 and 100
#           if not : print "Please enter your Cr again" and re-input
# Calculate the CrCl
# print CrCl

age = int(input("Please enter your age(in years): ")) # input age
while age > 100 or age < 0:
    print("Your age should be between 0 and 100")
    age = int(input("Please enter your age again (in years): ")) #re-input age

weight = float(input("Please enter your weight(in kg): ")) # input weight
while weight > 80 or weight < 20:
    print("Your weight should be between 20 and 80")
    weight = float(input("Please enter your weight again(in kg): ")) #re-input weight

creatine_concentration = float(input("Please enter your creatine concentration(Cr) in height (in µmol/l):")) #input creatine concentration
while creatine_concentration > 100 or creatine_concentration < 0:
    print("Cr should be between 0 and 100")
    creatine_concentration = float(input("Please enter your creatine concentration, Cr, in height again(in µmol/l):")) #re-input creatine concentration

gender = input("Please enter your gender(M/F):") # input gender
while gender != "M" and gender != "F": 
    print("Your gender should be either M or F")
    gender = input("Please enter your gender(M/F) again:") #re-input gender
# Acording to the formula, if the gender is female, the weight should be multiplied by 0.85
if gender == "F": 
    weight *= 0.85
CrCl = (140 - age)* weight // (72 * creatine_concentration)
print(f"Your CrCl is {CrCl}")