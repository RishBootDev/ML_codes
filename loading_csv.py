"""
We have a dataset of students stored in a CSV file (students.csv). Each row represents one student, and the dataset contains:

Age → student’s age
Salary → part-time salary in INR
Hours_Studied → number of hours studied per day
Passed → whether the student passed the exam (Yes or No)
"""

# Step 1: Import pandas
import pandas as pd

# Step 2: Load the dataset (make sure students.csv is in the same folder as this script)
df = pd.read_csv("students.csv")

# Step 3: View the first few rows
print("First 5 rows of the dataset:")
print(df.head())

# Step 4: Separate features and label
features = df[["Age", "Salary", "Hours_Studied"]]
label = df["Passed"]

print("\nFeatures (X):")
print(features.head())

print("\nLabel (y):")
print(label.head())
