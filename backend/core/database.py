import psycopg2
from core.requestsModels import *
from core.responseModels import *

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
                                             data.password, data.birthdate, data.sex, data.email))
    con.commit()
    cur.close()

def db_check_user_in_system_by_email_and_login(email: str, login: str):
    cur = con.cursor()
    cur.execute('''SELECT id FROM Users WHERE email=%s''', (email,))
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


def get_user_info(user_id: int):
    cur = con.cursor()
    cur.execute('''SELECT (fio, birthdate::text, description, achievements, education, email) FROM Users WHERE id=%s''',
                (user_id,))
    user_info = cur.fetchone()
    cur.execute('''SELECT t1.professionname FROM Profession t1 LEFT JOIN UserProfessionList t2 
                        ON t2.fkprofession = t1.id WHERE t2.fkuser = %s''', (user_id,))
    user_prof_list = list(cur.fetchall())
    cur.execute(
        '''SELECT t1.hobbyname FROM Hobby t1 LEFT JOIN UserHobbyList t2 ON t2.fkhobby = t1.id WHERE t2.fkuser = %s''',
        (user_id,))
    user_hobby_list = list(cur.fetchall())
    print(user_info)
    print(user_prof_list)
    print(user_hobby_list)
    cur.close()
    # user = UserResponse(fio=user_info)
    # print(user)
    return user_info
