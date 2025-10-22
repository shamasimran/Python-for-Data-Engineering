# ==============================================
# 13_Working_with_APIs
# ==============================================

# Step 1: Install requests (run in terminal if not installed)
# pip install requests

import requests
import json

# ------------------------------------------------
# Step 2: Make a GET request
# ------------------------------------------------
url = "https://jsonplaceholder.typicode.com/posts/1"
response = requests.get(url)

print("Status Code:", response.status_code)
print("Response JSON:", response.json())

# ------------------------------------------------
# Step 3: Make a POST request
# ------------------------------------------------
url = "https://jsonplaceholder.typicode.com/posts"
payload = {
    "title": "Data Engineering with Python",
    "body": "APIs help us extract and load data efficiently.",
    "userId": 1
}

response = requests.post(url, json=payload)
print("\nPOST Request:")
print("Status Code:", response.status_code)
print("Response JSON:", response.json())

# ------------------------------------------------
# Step 4: Handling Errors
# ------------------------------------------------
url = "https://jsonplaceholder.typicode.com/posts/999999"  # Invalid ID
response = requests.get(url)

if response.status_code == 200:
    print("\nData fetched successfully!")
else:
    print("\nError: HTTP", response.status_code)

# ------------------------------------------------
# Step 5: Adding Headers and Authentication (Example)
# ------------------------------------------------
headers = {
    "Authorization": "Bearer YOUR_API_TOKEN_HERE",
    "Content-Type": "application/json"
}

# This is just a placeholder example; replace with real API
# response = requests.get("https://api.example.com/data", headers=headers)
# print(response.json())

# ------------------------------------------------
# Step 6: Working with Query Parameters
# ------------------------------------------------
params = {"userId": 1}
response = requests.get("https://jsonplaceholder.typicode.com/posts", params=params)

print("\nFiltered Posts by userId=1:")
print(response.json())

# ------------------------------------------------
# Step 7: Save API Response to JSON File (Mini Exercise)
# ------------------------------------------------
response = requests.get("https://jsonplaceholder.typicode.com/users")
data = response.json()

with open("users.json", "w") as f:
    json.dump(data, f, indent=4)

print("\nUser data saved to users.json successfully!")
