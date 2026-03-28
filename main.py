import pickle
import pandas as pd

print("=== Fraud Detection System ===")

# Load model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

# Input
amount = float(input("Enter transaction amount: "))

# Convert to DataFrame (same format as training)
input_data = pd.DataFrame([[amount]], columns=['amount'])

# Predict
prediction = model.predict(input_data)

# Output
if prediction[0] == 1:
    print("⚠️ Fraudulent Transaction")
else:
    print("✅ Legitimate Transaction")