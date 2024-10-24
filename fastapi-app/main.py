from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import pickle

# Load the trained model
model = pickle.load(open('model.pkl', 'rb'))

# Initialize FastAPI app
app = FastAPI()

# Modify DataInput model to include the required fields
class DataInput(BaseModel):
    rate: float
    sales_in_first_month: float
    sales_in_second_month: float

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "API is running"}

# Prediction endpoint
@app.post("/predict")
def predict(data: DataInput):
    # Extract data from the input
    features = np.array([data.rate, data.sales_in_first_month, data.sales_in_second_month]).reshape(1, -1)
    # Make prediction
    prediction = model.predict(features)
    output = round(prediction[0], 2)
    # Return the result as JSON
    return {"prediction": output}
