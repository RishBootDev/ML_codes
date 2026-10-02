"""
Encoding categorical data
So far, we worked with numbers (ages, marks, salaries). But in real datasets, we often have categories like:

Gender: Male, Female
Department: Sales, HR, IT
City: Delhi, Mumbai, Bangalore
Machine Learning models cannot understand text directly.
We need to convert categories into numbers → this process is called encoding categorical data.

1. Label Encoding

Replace each category with a number. Example (Gender):
Male   → 0  
Female → 1
Problem:

The model may think 1 > 0 (as if Female is greater than Male).
It may assume a numeric relationship (difference = 1).
But gender categories don’t have such order.
2. One-Hot Encoding

Create a new column for each category.
Put 1 where the category is present, 0 otherwise.
Example (Gender):

Male  Female
  1     0     → Male
  0     1     → Female
This avoids the “greater than” problem in Label Encoding.

3. When to Use What?

Label Encoding → good when categories have a natural order (e.g., Small < Medium < Large).
One-Hot Encoding → good when categories have no order (e.g., Gender, City, Department).
"""

import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Step 1: Load dataset
df = pd.read_csv("employees.csv")
print("Original Data:")
print(df)

# Step 2: Label Encoding (Gender) using LabelEncoder
label_encoder = LabelEncoder()
df["Gender_Label"] = label_encoder.fit_transform(df["Gender"])
print("\nAfter Label Encoding Gender:")
print(df[["Name", "Gender", "Gender_Label"]])

# Step 3: One-Hot Encoding (Department)
df_onehot = pd.get_dummies(df, columns=["Department"])
print("\nAfter One-Hot Encoding Department:")
print(df_onehot)
