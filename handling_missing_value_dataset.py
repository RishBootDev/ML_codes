import pandas as pd

# Step 1: Load dataset
df = pd.read_csv("employees.csv")
print("Original Dataset:")
print(df)

# Step 2: Check missing values
print("\nMissing Values per Column:")
print(df.isnull().sum())

# Step 3: Fill missing numerical values with mean
df['Age'] = df['Age'].fillna(df['Age'].mean())
df['Salary'] = df['Salary'].fillna(df['Salary'].mean())

# Step 4: Fill missing categorical values with mode
df['Department'] = df['Department'].fillna(df['Department'].mode()[0])

print("\nDataset after Handling Missing Values:")
print(df)

