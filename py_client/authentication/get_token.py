import requests

endpoint = 'http://localhost:8000/api/auth/token/';

credentials = {
    'username': 'testUser2',
    'email': 'testuser2@example.com',
    'password': 'testpassword123',
}

response = requests.post(endpoint, json=credentials)
print(response.json())