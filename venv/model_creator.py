import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

# Load dataset
df = pd.read_csv('lung_cancer_data.csv')

# Convert categorical columns if any
df.replace({'Gender': {'Male': 0, 'Female': 1},
            'Smoking': {'Yes': 1, 'No': 0},
            'Coughing': {'Yes': 1, 'No': 0},
            'ShortnessOfBreath': {'Yes': 1, 'No': 0}}, inplace=True)

# Features and labels
X = df.drop('LungCancer', axis=1)
y = df['LungCancer']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save model to file
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("✅ Model trained and saved as model.pkl")
