import requests

endpoint = 'http://localhost:8000/api/auth/login/'


credentials = {
    'email': 'testuser2@example.com',
    'password': 'testpassword123',
}

response = requests.post(endpoint, credentials,);
print(response.json())
