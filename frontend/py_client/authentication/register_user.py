import requests

endpoint = 'http://localhost:8000/api/auth/register/'


data = {
    'username': 'testUser8',
    'email': 'testuser8@example.com',
    'password': 'testpassword123',
    'confirmed_password': 'testpassword123',
}


response = requests.post(endpoint, json=data)
print(response.json())
print(response.status_code)
