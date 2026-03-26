# show the number of patients in the dataset and the mean heart rate
heart_rates = [72, 60, 126, 85, 90, 59, 76, 131, 88, 121, 64]
number_of_patients = len(heart_rates)
Average_heart_rate = sum(heart_rates) / number_of_patients
print(f"There are {number_of_patients} patients in the dataset with a mean heart rate of {Average_heart_rate:.2f} bpm.")

# show the number of patients in each category and identify which category contains the largest number of patients
low = 0
normal = 0
high = 0
# count the number of patients in each category
for rate in heart_rates: 
    if rate < 60:
        low += 1
    elif 60 <= rate <= 120:
        normal += 1
    else:
        high += 1
print(f"Low: {low} patients")
print(f"Normal: {normal} patients")
print(f"High: {high} patients")
# Identify which category contains the largest number of patients
if low >= normal and low >= high:
    largest_category = 'Low'
elif normal >= low and normal >= high:
    largest_category = 'Normal'
else:
    largest_category = 'High'
print(f"The category with the largest number of patients is {largest_category}.")

# Create a pie chart
import matplotlib.pyplot as plt

Labels = ['Low', 'Normal', 'High']
sizes = [low, normal, high]
plt.pie(sizes, labels=Labels, autopct='%1.1f%%')
plt.title('Heart Rate Categories Distribution')
plt.axis('equal') # ensures that the pie chart is circular.
plt.show()