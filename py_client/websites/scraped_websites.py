import requests


endpoint = 'http://localhost:8000/api/scraped-websites/'

response = requests.get(endpoint, 
                        headers={
                             'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE2NjE0NzY4LCJpYXQiOjE3MTY1NzE1NjgsImp0aSI6IjQ3YWM3ZTlhZjkzNzQ4ZmZiNmI3MDZiZDU2OGE3ZTNkIiwidXNlcl9pZCI6Mn0.N3wN39Zt2Q3EdD8VFHwc5FRMkWysNyS921gLRqTIt_I',
                             'Content-Type':'application/json',
                        },)

print(response.json())

