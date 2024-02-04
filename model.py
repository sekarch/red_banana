import numpy as np
from sklearn.linear_model import Ridge
import pandas as pd

# Load your dataset
# Replace 'your_dataset.csv' with the actual file path or URL
data = pd.read_csv('Red_banana.csv')

# Assuming 'X' contains features and 'y' contains the target variable (Maturity Index)
X = data[['Fruit weight (g)', 'Fruit Length (cm)', 'Fruit Girth (cm)', 'Caliper (mm)']]
y = data['Maturity Index']

# Train Ridge Regression model
ridge_model = Ridge(alpha=1.0)
ridge_model.fit(X, y)

def load_model():
    return ridge_model

def predict_maturity_index(input_data):
    # Make a prediction using the trained model
    input_data_np = np.array([input_data])
    return ridge_model.predict(input_data_np)[0]
