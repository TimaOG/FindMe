import requests

s = requests.Session() 
#s.post('http://localhost:8000/login', json = {'email': 'a', 'password': 'g'})
gg = s.post('http://localhost:8000/test', json = {'email': 'a', 'password': 'g'})
print(gg.text)