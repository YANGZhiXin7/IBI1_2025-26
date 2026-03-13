# Input age, weight, gender, and creatine concentration
# check if gender is Female or Male
#           if gender = Female : weight = weight * 0.85
# check if age is between 0 and 100
#           if not : re-input
# check if weight is between 20 and 80
#           if not : re-input
# check if gender is male or female
#           if not : re-input
# check if creatine concentration is between 0 and 100
#           if not : re-input
# Calculate the CrCl
# print CrCl


# input variables
age = int(input("Please enter your age(in years): "))
weight = float(input("Please enter your weight(in kg): "))
gender = input("Please enter your gender(M/F):")
if gender == "F":
    weight *= 0.85
creatine_concentration = float(input("Please enter your creatine concentration, Cr, in height (in µmol/l):"))
# check if all the variables are within range.
if age > 100 or age < 0:
    print("Please enter your age again")
elif weight > 80 or weight < 20:
    print("Please enter your weight again")
elif creatine_concentration > 100 or creatine_concentration < 0:
    print("Please enter your creatine concentration again")
elif gender != "M" and gender != "F":
    print("Please enter your gender again")
else:
    CrCl = (140 - age)* weight // (72 * creatine_concentration)
print(f"Your CrCl is {CrCl}")