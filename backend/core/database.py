import psycopg2
from core.requestsModels import *
con = psycopg2.connect(
  database="fm", 
  user="postgres", 
  password="123", 
  host="127.0.0.1", 
  port="5432"
)

def db_create_user(data: RegData):
    cur = con.cursor()
    cur.execute('''INSERT INTO Users (fio,userLogin, userPassword,birthdate, sex, email) 
        VALUES (%s, %s, %s, %s, %s, %s)''', (data.fio, data.login,
        data.password,data.birthdate, data.sex, data.email))
    con.commit()
    cur.close()

def db_check_user_in_system_by_email_and_login(email: str, login: str):
    cur = con.cursor()
    cur.execute('''SELECT id FROM Users WHERE email=%s''', (email, ))
    resEmail = cur.fetchone()
    cur.execute('''SELECT id FROM Users WHERE userLogin=%s''', (login, ))
    resLogin = cur.fetchone()
    cur.close()
    if resEmail != None:
        return [False, 'Email already exist']
    if resLogin != None:
        return [False, 'Login already exist']
    return [True, '']

def db_check_user_in_system(data: LoginData):
    cur = con.cursor()
    cur.execute('''SELECT id, userPassword FROM Users WHERE email=%s''', (data.email, ))
    res = cur.fetchone()
    if res[0] == None:
        return [False, '']
    return [True, res[1]]