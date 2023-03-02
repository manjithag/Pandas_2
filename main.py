## Sorting & Describing Data

import pandas as pd
df = pd.read_csv('pokemon_data.csv')

print("---------Print 1-------------")
print(df.describe())

print("---------Print 2-------------")
print(df.sort_values(['Name']))

print("---------Print 3-------------")
print(df.sort_values('Name', ascending=False))

print("---------Print 4-------------")
print(df.sort_values(['Name', 'Type 1']))