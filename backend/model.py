import joblib
import numpy as np

# load the model
model = joblib.load('linear_regression_model.pkl')

def predict(input_data):
    input_array = np.array(input_data).reshape(-1, 1)
    prediction = model.predict(input_array)
    return prediction.flatten().tolist()
