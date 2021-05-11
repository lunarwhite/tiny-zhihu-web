import datetime
import pymssql

def tupleToList(data):
    d = []
    for i in data:
        d.append(list(i))
    return d

def insertUser(cur, user_name, mobile, Email, Passwd, SEX, SignDetail):
    insertAccount(cur, Passwd, mobile)
    sql_insert = '''
    INSERT INTO user_info(username,mobile,Email,SEX,Regtime,signDetail)
    VALUES (%s,%d,%s,%s,%s,%s);
    '''
    dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cur.execute(sql_insert, (user_name, mobile, Email, SEX, dt, SignDetail))

def insertAccount(cur, Passwd, mobile):
    sql_insert = '''
    INSERT INTO Account_info
    VALUES (%s,%d);
    '''
    cur.execute(sql_insert, (Passwd, mobile))

def insertQuestion(cur, user_ID, Q_title, Q_text):
    sql_insert = '''
    INSERT INTO question_info(u_id,Q_title,Q_text,Posttime)
    VALUES (%d,%s,%s,%s);
    '''
    dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cur.execute(sql_insert, (user_ID, Q_title, Q_text, dt))

def insertAnswer(cur, Q_ID, user_ID, A_text):
    sql_insert = '''
    INSERT INTO Answer_info(Q_ID,u_ID,A_text)
    VALUES (%d,%d,%s);
    '''
    cur.execute(sql_insert, (Q_ID, user_ID, A_text))

def insertComment(cur, A_ID, user_ID, C_text):
    sql_insert = '''
    INSERT INTO Comment_info(A_ID,u_ID,C_text,posttime)
    VALUES (%d,%d,%s,%s);
    '''
    dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cur.execute(sql_insert, (A_ID, user_ID, C_text, dt))

def insertCollection(cur, Q_ID, user_ID):
    sql_insert = '''
    INSERT INTO Collection_info
    VALUES (%d,%d);
    '''
    cur.execute(sql_insert, (Q_ID, user_ID))

def deleteCollection(cur, Q_ID, user_ID):
    sql_insert = '''
    delete from Collection_info
    where Q_ID = '{}' and U_ID = '{}';
    '''.format(Q_ID,user_ID)
    cur.execute(sql_insert)


def deleteQuestionOnQ_ID(cur,question_id):
    sql_insert = '''
    delete from question_info
    where Q_ID = '{}' ;
    '''.format(question_id)
    cur.execute(sql_insert)

def insertFocus(cur, Auser_ID, Buser_ID):
    sql_insert = '''
    INSERT INTO Focus_info
    VALUES (%d,%d);
    '''
    cur.execute(sql_insert, (Auser_ID, Buser_ID))

def selectAllQuestion(cur):
    SQL = 'select * from Question_info'
    cur.execute(SQL)
    data = cur.fetchall()
    return tupleToList(data)



def selectALLAnswer(cur):
    SQL = 'select * from Answer_info'
    cur.execute(SQL)
    data = cur.fetchall()
    return tupleToList(data)


def selectALLComment(cur):
    SQL = 'select * from Comment_info'
    cur.execute(SQL)
    data = cur.fetchall()
    return tupleToList(data)


def selectAllUser(cur):
    SQL = 'select * from User_info'
    cur.execute(SQL)
    data = cur.fetchall()
    return tupleToList(data)


def selectTextOfAnswer(cur, Q_ID):
    SQL = '''select A_text from Answer_info
             where Q_ID = (%s) '''
    cur.execute(SQL, (Q_ID))
    data = cur.fetchall()
    return tupleToList(data)


def selectAnswerOfQID(cur, Q_ID):
    SQL = '''select * from Answer_info
             where Q_ID = (%s) '''
    cur.execute(SQL, (Q_ID))
    data = cur.fetchall()
    return tupleToList(data)


def selectAnswerOfAID(cur, A_ID):
    SQL = '''select * from Answer_info
             where A_ID = (%s) '''
    cur.execute(SQL, (A_ID))
    data = cur.fetchall()
    return tupleToList(data)[0]


def selectCommentOfAID(cur, A_ID):
    SQL = '''select * from Comment_info
             where A_ID = (%d) '''
    cur.execute(SQL, (A_ID))
    data = cur.fetchall()
    return tupleToList(data)


def selectCommentOfCID(cur, C_ID):
    SQL = '''select * from Answer_info
             where C_ID = (%d) '''
    cur.execute(SQL, (C_ID))
    data = cur.fetchall()
    return tupleToList(data)


def selectQuestionOfQID(cur, Q_ID):
    SQL = '''select * from Question_info
             where Q_ID = (%d) '''
    cur.execute(SQL, (Q_ID))
    data = cur.fetchall()
    return tupleToList(data)[0]


def selectAccountTologin(cur, telephone, passwd):
    sql = '''
    SELECT mobile FROM account_info
    WHERE passwd ='{}' and mobile = '{}'
    '''.format(passwd, telephone)
    cur.execute(sql)
    data = cur.fetchall()
    return tupleToList(data)


def selectUserOnMobile(cur, telephone):
    sql = '''
    SELECT * FROM user_info
    WHERE mobile = '{}'
    '''.format(telephone)
    cur.execute(sql)
    data = cur.fetchall()
    return tupleToList(data)


def selectUserToReg(cur, telephone):
    sql = '''
    SELECT * FROM user_info
    WHERE mobile = '{}'
    '''.format(telephone)
    cur.execute(sql)
    data = cur.fetchall()
    return tupleToList(data)

def selectUserTologin(cur,telephone,passwd):
    sql = '''
    SELECT * FROM user_info
    WHERE email ='{}' and mobile = '{}'
    '''.format(passwd,telephone)
    cur.execute(sql)
    data = cur.fetchall()
    d = []
    for i in data:
        d.append(list(i))
    return d

def selectUserNameOnUID(cur, U_ID):
    sql = '''
    SELECT username FROM user_info
    WHERE U_ID = '{}'
    '''.format(U_ID)
    cur.execute(sql)
    data = cur.fetchall()
    return tupleToList(data)[0]

def selectUIDOnUsername(cur, username):
    sql = '''
    SELECT U_ID FROM user_info
    WHERE username = '{}'
    '''.format(username)
    cur.execute(sql)
    data = cur.fetchall()
    return tupleToList(data)[0]

def selectquestionOnU_ID(cur,U_ID):
    SQL = '''
    SELECT * FROM question_info
    WHERE U_ID = '{}'
    '''.format(U_ID)
    cur.execute(SQL)
    data = cur.fetchall()
    return tupleToList(data)

def updateAnswerOfCNumber(cur, A_ID):
    sql = '''
    update Answer_info set C_Number = C_Number + 1
    where A_ID = (%d)
    '''
    cur.execute(sql, (A_ID))

def updateAnswerOfZNumber(cur, A_ID):
    sql = '''
    update Answer_info set Z_Number = Z_Number + 1
    where A_ID = (%d)
    '''
    cur.execute(sql, (A_ID))

def selectCollectionOfUser(cur,U_ID,Q_ID):
    sql = '''
    SELECT * FROM collection_info
    WHERE U_ID = '{}' and Q_ID = '{}'
    '''.format(U_ID,Q_ID)
    cur.execute(sql)
    data = cur.fetchall()
    return tupleToList(data)

def selectCollection(cur,U_ID):
    sql = '''
    SELECT Q_ID FROM collection_info
    WHERE U_ID = '{}'
    '''.format(U_ID)
    cur.execute(sql)
    data = cur.fetchall()
    return tupleToList(data)

def selectQuestionOfQ_ID(cur,Q_ID):
    SQL = '''
    SELECT * FROM question_info
    WHERE Q_ID = '{}'
    '''.format(Q_ID)
    cur.execute(SQL)
    data = cur.fetchall()
    return tupleToList(data)

def selectAnswerOfQuestion(cur,Q_ID):
    SQL = '''select A_text from Answer_info
             where Q_ID = (%s) '''
    cur.execute(SQL,(Q_ID))
    data = cur.fetchall()
    d = []
    for i in data:
        d.append(list(i))
    return  d

def questionAndfirstAuestion(cur):
    questions = selectAllQuestion(cur)
    # print(questions)
    # print(answers)
    for i in range(len(questions)):
        data = selectAnswerOfQuestion(cur, questions[i][0])
        questions[i].append(data[0])
    return questions

def selectuserOfdetail(cur,U_ID):
    SQL = '''
    SELECT signDetail FROM user_info
    WHERE U_ID = '{}'
    '''.format(U_ID)
    cur.execute(SQL)
    data = cur.fetchall()
    return tupleToList(data)

# conn = pymssql.connect(host='127.0.0.1:1433', user='yhc', password='111111', database='ZhiHu', charset="UTF-8")
# cur = conn.cursor()

# print(selectUserTologin(cur,18801111888,'111111'))
# cur.close()
# conn.commit()
# conn.close()