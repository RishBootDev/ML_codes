from sklearn.tree import DecisionTreeClassifier

# Dataset: [weight, sweetness]
X = [
    [150, 7],
    [170, 6],
    [140, 8],
    [200, 4],
    [210, 3],
    [190, 5]
]

# Labels: Apple or Orange
y = ["Apple", "Apple", "Apple", "Orange", "Orange", "Orange"]

# Create the model
model = DecisionTreeClassifier()

# Hint: Use model.fit(X, y)
model.fit(X, y)

# Predict for a new fruit
new_fruit = [[160, 7]]

prediction = model.predict(new_fruit)
print("Prediction for new fruit:", prediction)
