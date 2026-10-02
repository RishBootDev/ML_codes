import pandas as pd
from sklearn.preprocessing import StandardScaler

# Step 1: Load the dataset
df = pd.read_csv("employees.csv")

# Step 2: Select numeric feature(s) to scale (Salary and Experience)
X = df[["Salary", "Experience"]]

# Step 3: Apply Standard Scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Step 4: Convert back to DataFrame
X_scaled_df = pd.DataFrame(X_scaled, columns=["Salary", "Experience"])

# Step 5: Print the scaled values
print("Standardized Data:")
print(X_scaled_df)
