import requests


endpoint = 'http://localhost:8000/api/scraped-websites/14/'

response = requests.get(endpoint,
                        headers={
                             'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE2NTU0ODIzLCJpYXQiOjE3MTY1MTE2MjMsImp0aSI6IjFkZDllMzVhYjZiNjQwNzY4NDEwMTFiNzZiYTUwMDk4IiwidXNlcl9pZCI6Mn0.Ysw_4EaTDY5j2E_J2lY5tUQby4MztciD6AqD7zwLY94',
                             'Content-Type':'application/json',
                        },)
print(response.json())