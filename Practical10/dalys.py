import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Importing the .csv file
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")

# Showing the third and forth columns of the data frame for the first ten rows
first_10 = dalys_data.iloc[0:10, 2:4]
print("\nYear and DALYs for first 10 rows:")
print(first_10)
# Showing the maximum DALYs across the first 10 years for which DAYLS were recorded in Afghanistan
print("\nSummary statistics:")
print(dalys_data.iloc[0:10, 2:4].describe())
# Find year with max DALYs in Afghanistan's first 10 years
afg_10 = dalys_data.iloc[0:10]
max_afg_year = afg_10.loc[afg_10['DALYs'].idxmax(), 'Year']
print(f"\nYear with maximum DALYs in Afghanistan's first 10 years: {max_afg_year}")
# The 1998 DALYs for Afghanistan first 10 years has the maximum value

# Boolean selection: all rows where Entity is Zimbabwe
zimbabwe_bool = dalys_data["Entity"] == "Zimbabwe"
zimbabwe_data = dalys_data.loc[zimbabwe_bool, :]
# Show all years for Zimbabwe
print("\nAll years with DALYs recorded in Zimbabwe:")
print(zimbabwe_data[["Year", "DALYs"]])
# First year of DALYs recorded for Zimbabwe: 1990
# Last year of DALYs recorded for Zimbabwe: 2019
zimbabwe_first_year = zimbabwe_data["Year"].min()
zimbabwe_last_year = zimbabwe_data["Year"].max()
print(f"First year for Zimbabwe: {zimbabwe_first_year}")
print(f"Last year for Zimbabwe: {zimbabwe_last_year}")

recent_data = dalys_data.loc[dalys_data.Year == 2019, ['Entity', 'DALYs']]
# The 2019 DALYs highest and lowest country
max_daly_2019 = recent_data.loc[recent_data['DALYs'].idxmax()]
max_country = max_daly_2019['Entity']
# The 2019 DALYs highest country
min_daly_2019 = recent_data.loc[recent_data['DALYs'].idxmin()]
min_country = min_daly_2019['Entity']
# print the results
print(f"The higest DALYs country in 2019 is: {max_country}")
print(f"The lowest DALYs country in 2019 is: {min_country}")
# The higest DALYs country in 2019 is: Lesotho
# The lowest DALYs country in 2019 is: Singapore

# The 2019 DALYs highest country line graph (Lesotho)
max_country_data = dalys_data.loc[dalys_data['Entity'] == max_country]
plt.figure(figsize=(10, 5))
plt.plot(max_country_data.Year, max_country_data.DALYs, 'r-', linewidth=2, label=max_country)
plt.title(f'DALYs over time in {max_country} (2019 highest)')
plt.xlabel('Year')
plt.ylabel('DALYs (rate from all causes)')
plt.xticks(rotation=-90)
plt.grid(alpha=0.3)
plt.legend()
plt.tight_layout()
plt.show()

# Filter countries with DALYs less than 18000
below_18000 = dalys_data[dalys_data['DALYs'] < 18000]
countries_below_18000 = below_18000['Entity'].unique()
print("Countries with DALYs less than 18,000 in at least one year:")
for country in countries_below_18000:
    print(country)
# The countries with DALYs less than 18,000 in at least one year are:
# Iceland, Israel, Japan, Singapore, South Korea, Spain, Switzerland
