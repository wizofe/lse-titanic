# -*- coding: utf-8 -*-
"""
Introduction to Python @ LSE
Using the Titanic Dataset

Written by Ioannis Valasakis <ioannis.valasakis@kcl.ac.uk>
The Unlicense

"""

# if pandas is not installed
# pip install pandas
import pandas
import seaborn as sns

# Save the csv file to a variable
td = pandas.read_csv(
        'https://web.stanford.edu/class/archive/cs/cs109/cs109.1166/stuff/titanic.csv'
        )

def convert_survivor(survived):
    if survived == 1:
        return "YES"
    else:
        return "NO"

td['Alive'] = td['Survived'].apply(convert_survivor)
byPclass = td.groupby('Pclass')

print(byPclass['Survived'].mean())