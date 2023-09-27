import requests

s = requests.Session()
s.cookies.clear() 
gg = s.post('http://localhost:8000/register', json = {'fio': 'gang', 'login': 'gang', 'password': '123', 'password2': '123','email': 'gg@gg.ru', 'sex': True, 'birthdate': '2023-09-01'})
print(gg.text)

<<<<<<< HEAD
s.post('http://localhost:8000/login', json = {'email': 'gg@gg.ru', 'password': '123'})
#gg = s.get('http://localhost:8000/account/getAccountInfo')
fp = open('C:\\Users\\harha\\OneDrive\\Изображения\\SlideShow\\photo1.jpg', 'rb')
files = {'file': fp}
headers = {'Content-Type': 'multipart/form-data', 'accept': 'application/json'}
gg = s.put('http://localhost:8000/account/saveAccountAvatar', files=files)
fp.close()
#gg = s.delete('http://localhost:8000/account/deleteAccount')
#gg = s.put('http://localhost:8000/account/saveAccountSettings', json={'login':'gang1', 'email': 'gg@gg.ru', 'password': '111', 'password2': '111', 'oldpassword': '123'})
print(gg.text)
=======
gg = s.post('http://localhost:8000/login', json = {'email': 'gg@gg.ru', 'password': '123'})
print(gg.text)
# #gg = s.get('http://localhost:8000/account/getAccountInfo')
# fp = open('C:\\Users\\Тимофей\\Pictures\\8-18.png', 'rb')
# files = {'file': fp}
# headers = {'Content-Type': 'multipart/form-data', 'accept': 'application/json'}
# gg = s.put('http://localhost:8000/account/saveAccountAvatar', files=files)
# fp.close()
# #gg = s.delete('http://localhost:8000/account/deleteAccount')
# #gg = s.put('http://localhost:8000/account/saveAccountSettings', json={'login':'gang1', 'email': 'gg@gg.ru', 'password': '111', 'password2': '111', 'oldpassword': '123'})
# print(gg.text)
>>>>>>> 5bf316e98f6b07211bfe50086d907c5bbc84c797
