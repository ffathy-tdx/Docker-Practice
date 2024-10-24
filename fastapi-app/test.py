import requests

url = "http://localhost:8000/predict"

# Updated input data with required fields
data = {
    "rate": 4.0,
    "sales_in_first_month": 200.0,
    "sales_in_second_month": 600.0
}

response = requests.post(url, json=data)

print(response.status_code)  # Should print 200 if successful
print(response.json())  # Will print the prediction result
