# the population data for 2020 and 2024
countries = ["UK", "China", "Italy", "Brazil", "USA"]
population_2020 = [66.7, 1426, 59.4, 208.6, 331.6]
population_2024 = [69.2, 1410, 58.9, 212.0, 340.1]

# calculate the percentage change in population for each country from 2020 to 2024
percent_changes = []
for i in range(len(countries)):
    change = (pop_2024[i] - pop_2020[i]) / pop_2020[i] * 100 # calculate the percentage change
    percent_changes.append(change) # add the percentage change to the list

#print the percentage change for each country
print("Population percentage change (2020-2024):") # print the header
for i in range(len(countries)):
    country = countries[i]
    change = percent_changes[i]
    print(f"{country}: {change:.2f}%") # print the percentage change for each country

# Sort the countries by percentage change in population from largest increase to largest decrease
data = []
for i in range(len(countries)):
    data.append([countries[i], percent_changes[i]])
n = len(data)
for i in range(n):
    for j in range(0, n - i - 1):
        if data[j][1] < data[j+1][1]:
            data[j], data[j+1] = data[j+1], data[j]
# Print the sorted list of countries and their percentage changes
print("\nSorted population changes (largest increase to largest decrease):")
for i in range(len(data)):
    country = data[i][0]
    change = data[i][1]
    print(f"{country}: {change:.2f}%")

# Identify the country with the largest increase and the country with the largest decrease in population percentage change
M_inc_country = data[0][0] # the country with the largest increase is the first one in the sorted list
M_inc = data[0][1] # the percentage change for the country with the largest increase is the first one in the sorted list
M_dec_country = data[-1][0] # the country with the largest decrease is the last one in the sorted list
M_dec = data[-1][1] # the percentage change for the country with the largest decrease is the last one in the sorted list
# Print the results
print(f"\nLargest increase: {M_inc_country} ({M_inc:.2f}%)")
print(f"Largest decrease: {M_dec_country} ({M_dec:.2f}%)")

# Create a bar plot to visualize the percentage change in population for each country
import matplotlib.pyplot as plt
plt.figure(figsize=(8, 5))
plt.bar(countries, percent_changes, color=['blue', 'red', 'green', 'orange', 'purple'])
plt.title("Population Percentage Change (2020-2024) by Country")
plt.xlabel("Country")
plt.ylabel("Percentage Change (%)")
plt.show()