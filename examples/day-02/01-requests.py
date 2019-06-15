"""
Работа с запросами на веб-сервер (веб-сайты)
"""
import requests

response = requests.get('https://jsonplaceholder.typicode.com/users')
users = response.json()

email = users[0]['email']
print(email)