import requests

s = requests.Session() 
#gg = s.post('http://localhost:8000/register', json = {'fio': 'gang', 'login': 'gang', 'password': '123', 'password2': '123','email': 'gg@gg.ru', 'sex': True, 'birthdate': '2023-09-01'})
# print(gg.text)

s.post('http://localhost:8000/login', json = {'email': 'gg@gg.ru', 'password': '123'})
gg = s.get('http://localhost:8000/account/getAccountInfo')
print(gg.text)