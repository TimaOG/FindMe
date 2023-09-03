import requests

s = requests.Session()
s.cookies.clear() 
#gg = s.post('http://localhost:8000/register', json = {'fio': 'gang', 'login': 'gang', 'password': '123', 'password2': '123','email': 'gg@gg.ru', 'sex': True, 'birthdate': '2023-09-01'})
# print(gg.text)

s.post('http://localhost:8000/login', json = {'email': 'gg@gg.ru', 'password': '111'})
#gg = s.get('http://localhost:8000/account/getAccountInfo')
# gg = s.put('http://localhost:8000/account/saveAccountInfo', json={'description': 'gang', 
#     'achievements': 'никаких', 'education': 'два класса', 
#     'email':'gg@gg.ru', 'professionList': [1], 'hobbyList': []})
#gg = s.delete('http://localhost:8000/account/deleteAccount')
gg = s.put('http://localhost:8000/account/saveAccountSettings', json={'login':'gang1', 'email': 'gg@gg.ru', 'password': '111', 'password2': '111', 'oldpassword': '123'})
print(gg.text)