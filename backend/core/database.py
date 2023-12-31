import psycopg2
from .requestsModels import *
from .responseModels import *
from passlib.context import CryptContext
import shutil
from fastapi import FastAPI, UploadFile, File

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

con = psycopg2.connect(
    database="fm",
    user="postgres",
    password="",
    host="127.0.0.1",
    port="5432"
)


def db_create_user(data: RegDataRequest):
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
    cur.execute('''SELECT id FROM Users WHERE userLogin=%s''', (login,))
    resLogin = cur.fetchone()
    cur.close()
    if resEmail != None:
        return [False, 'Email already exist']
    if resLogin != None:
        return [False, 'Login already exist']
    return [True, '']


def db_check_user_in_system(data: LoginDataRequest):
    cur = con.cursor()
    cur.execute('''SELECT id, userPassword FROM Users WHERE email=%s''', (data.email,))
    res = cur.fetchone()
    cur.close()
    if res == None:
        return [False, '']
    return [True, res[1], res[0]]


def db_get_user_info(user_id: int):
    cur = con.cursor()
    cur.execute(
        '''SELECT fio, birthdate::text, sex, description, achievements, education, email FROM Users WHERE id=%s''',
        (user_id,))
    user_info = cur.fetchone()
    cur.execute('''SELECT t1.professionname FROM Profession t1 LEFT JOIN UserProfessionList t2 
                        ON t2.fkprofession = t1.id WHERE t2.fkuser = %s''', (user_id,))
    user_prof_list = cur.fetchall()
    cur.execute(
        '''SELECT t1.hobbyname FROM Hobby t1 LEFT JOIN UserHobbyList t2 ON t2.fkhobby = t1.id WHERE t2.fkuser = %s''',
        (user_id,))
    user_hobby_list = cur.fetchall()
    cur.close()
    user = UserResponse(fio=user_info[0], birthdate=user_info[1], sex=user_info[2], description=user_info[3],
                        achievements=user_info[4], education=user_info[5], email=user_info[6],
                        professionList=db_get_list_from_tuple(user_prof_list),
                        hobbyList=db_get_list_from_tuple(user_hobby_list))
    # print(user)
    return user


def db_save_user_info(userInfo: UserRequest, user_id: int):
    cur = con.cursor()
    cur.execute('''UPDATE Users SET description=%s, achievements=%s, education=%s WHERE id=%s''',
                (userInfo.description, userInfo.achievements, userInfo.education, user_id))
    con.commit()
    cur.execute('''DELETE FROM UserHobbyList WHERE fkUser=%s''', (user_id,))
    con.commit()
    for hobby_id in userInfo.hobbyList:
        cur.execute('''INSERT INTO UserHobbyList (fkUser, fkHobby) VALUES(%s, %s) 
                    ON CONFLICT(fkHobby) DO NOTHING''', (user_id, hobby_id))
        con.commit()
    cur.execute('''DELETE FROM UserProfessionList WHERE fkUser=%s''', (user_id,))
    con.commit()
    for prof_id in userInfo.hobbyList:
        cur.execute('''INSERT INTO UserProfessionList (fkUser, fkProfession) VALUES(%s, %s) 
                    ON CONFLICT(fkProfession) DO NOTHING''', (user_id, prof_id))
        con.commit()
    cur.close()

def db_save_user_ava_info(fileName: str, user_id: int):
    cur = con.cursor()
    cur.execute('''SELECT avaLink FROM Users WHERE id=%s''', (user_id,))
    oldAvaName = cur.fetchone()
    cur.execute('''UPDATE Users SET avaLink=%s WHERE id=%s''',
                (fileName, user_id))
    con.commit()
    cur.close()
    if oldAvaName == None:
        return None
    else:
        return oldAvaName[0]
    

def db_save_user_resume_info(fileName: str, user_id: int):
    cur = con.cursor()
    cur.execute('''SELECT resumeLink FROM Users WHERE id=%s''', (user_id,))
    oldAvaName = cur.fetchone()
    cur.execute('''UPDATE Users SET resumeLink=%s WHERE id=%s''',
                (fileName, user_id))
    con.commit()
    cur.close()
    if oldAvaName == None:
        return None
    else:
        return oldAvaName[0]


def db_save_user_settings(userInfo: UserSettingsRequest, user_id: int):
    cur = con.cursor()
    cur.execute('''SELECT userPassword FROM Users WHERE id=%s''', (user_id,))
    oldPassword = cur.fetchone()
    if pwd_context.verify(userInfo.password2, oldPassword[0]):
        cur.close()
        return False
    cur.execute('''UPDATE Users SET email=%s, userPassword=%s, userLogin=%s WHERE id=%s''',
                (userInfo.email, userInfo.password, userInfo.login, user_id))
    con.commit()
    cur.close()
    return True


def db_delete_user(user_id: int):
    cur = con.cursor()
    cur.execute('''DELETE FROM Users WHERE id=%s''', (user_id,))
    con.commit()
    cur.close()


def db_get_list_from_tuple(tup):
    res = []
    for el in tup:
        res.append(el[0])
    return res


def db_get_project_info(user_id: int):
    cur = con.cursor()
    cur.execute('''SELECT projectname, target, readystate, description, achievements, education, photolink,
                presentationlink WHERE fkuserowner=%s''', (user_id,))
    project_info = cur.fetchone()
    cur.commit()
    info = ProjectInfoResponse(projectnane=project_info[0], target=project_info[1], readystate=project_info[2],
                               description=project_info[3], achievements=project_info[4], education=project_info[5],
                               photolink=project_info[6], presentationlink=project_info[7])
    return info

def db_add_project(project: AddProjectRequest, user_id: int):
    pass

def db_get_project_list():
    pass
