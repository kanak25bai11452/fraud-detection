import pandas as pd
from sklearn.linear_model import LogisticRegression
import pickle

# Step 1: Create dataset
data = {
    'amount': [100, 500, 2000, 3000, 15000, 20000, 250, 700],
    'fraud':  [0,   0,   0,    0,    1,     1,     0,   0]
}

df = pd.DataFrame(data)

# Step 2: Separate input & output
X = df[['amount']]
y = df['fraud']

# Step 3: Train model
model = LogisticRegression()
model.fit(X, y)

# Step 4: Save model
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Model trained and saved successfully!")