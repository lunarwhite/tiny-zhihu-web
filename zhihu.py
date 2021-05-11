import config
import flask
from flask import Flask
import pymssql
from SQL import *
from functools import wraps

conn = pymssql.connect(host='127.0.0.1:50470',
                       user='sa', password='xx72', database='izhihu')
cur = conn.cursor()
app = Flask(__name__)
app.config.from_object(config)


def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if hasattr(flask.g, 'user'):
            return func(*args, **kwargs)
        else:
            return flask.redirect(flask.url_for('login'))
    return wrapper

def cutConnet():
    cur.close()
    conn.close()


@app.route('/')
def index():
    questions = selectAllQuestion(cur)
    user_id = flask.session.get('user_id')
    username = flask.session.get('name')
    if user_id:
        for i in range(len(questions)):
            Q_id = questions[i][0]
            temp = selectCollectionOfUser(cur,user_id,Q_id)
            if len(temp)!=0:
                questions[i].append(1)
    context = {
        'questions': questions,
        'username':username
    }
    return flask.render_template('index.html', **context)


@app.route('/question/', methods=['GET', 'POST'])
@login_required
def question():
    if flask.request.method == 'GET':
        return flask.render_template('question.html')
    else:
        title = flask.request.form.get('title')
        content = flask.request.form.get('content')
        user_id = flask.session.get('user_id')
        insertQuestion(cur, user_id, title, content)
        conn.commit()
        return flask.redirect(flask.url_for('index'))


@app.route('/answer/<id>/')
def answer(id):
    question = selectQuestionOfQID(cur, id)
    Answer = selectAnswerOfQID(cur, id)
    for i in range(len(Answer)):
        id = Answer[i][2]
        userName = selectUserNameOnUID(cur, id)[0]
        Answer[i].append(userName)
    context = {
        'question': question,
        'Answer': Answer
    }
    return flask.render_template('answer.html', **context)


@app.route('/user/<id>/')
def user(id):
    B_username = id
    A_username = flask.session.get('name')
    if B_username == A_username or B_username =='0':
        user_id = flask.session.get('user_id')
        username = flask.session.get('name')
        flag = 1
    else:
        username = B_username
        user_id = selectUIDOnUsername(cur, username)[0]
        flag = 0
    sign = selectuserOfdetail(cur, user_id)[0][0]
    questions = []
    collection = selectCollection(cur, user_id)
    for i in collection:
        question = selectQuestionOfQ_ID(cur, i[0])[0]
        question.append(1)
        questions.append(question)
    myquestions = selectquestionOnU_ID(cur,user_id)
    context = {
        'questions': questions,
        'name': username,
        'myquestions':myquestions,
        'sign':sign,
        'flag':flag
    }
    return flask.render_template('user.html',**context)


@app.route('/comment/<id>/')
def comment(id):
    Answer = selectAnswerOfAID(cur, id)
    Comment = selectCommentOfAID(cur, id)
    for i in range(len(Comment)):
        id = Comment[i][2]
        userName = selectUserNameOnUID(cur, id)[0]
        Comment[i].append(userName)
    context = {
        'Answer': Answer,
        'Comment': Comment
    }
    return flask.render_template('comment.html', **context)


@app.route('/answer/', methods=['POST'])
@login_required
def postAnswer():
    question_id = flask.request.form.get('question_id')
    A_content = flask.request.form.get('content')
    user_id = flask.session.get('user_id')
    insertAnswer(cur, question_id, user_id, A_content)
    conn.commit()
    return flask.redirect(flask.url_for('answer', id=question_id))


@app.route('/like/', methods=['POST'])
def giveLike():
    question_id = flask.request.form.get('question_id')
    answer_id = flask.request.form.get('answer_id')
    updateAnswerOfZNumber(cur, answer_id)
    conn.commit()
    return flask.redirect(flask.url_for('answer', id=question_id))


@app.route('/Collection/', methods=['POST'])
@login_required
def giveCollection():
    question_id = flask.request.form.get('question_id')
    flag = flask.request.form.get('flag')
    user_id = flask.session.get('user_id')
    if flag == '1':
        deleteCollection(cur,question_id,user_id)
        conn.commit()
        return flask.redirect(flask.url_for('index'))
    insertCollection(cur, question_id, user_id)
    conn.commit()
    return flask.redirect(flask.url_for('index'))

@app.route('/delete/', methods=['POST'])
@login_required
def deleteQuestion():
    question_id = flask.request.form.get('question_id')
    uid = flask.request.form.get('uid')
    deleteQuestionOnQ_ID(cur,question_id)
    conn.commit()
    return flask.redirect(flask.url_for('user',id=uid))

@app.route('/adminDelete/', methods=['POST'])
@login_required
def adminDelete():
    question_id = flask.request.form.get('question_id')
    deleteQuestionOnQ_ID(cur,question_id)
    conn.commit()
    return flask.redirect(flask.url_for('index'))

@app.route('/comment/', methods=['POST'])
@login_required
def postComment():
    answer_id = flask.request.form.get('answer_id')
    content = flask.request.form.get('content')
    user_id = flask.session.get('user_id')
    insertComment(cur, answer_id, user_id, content)
    updateAnswerOfCNumber(cur, answer_id)
    conn.commit()
    return flask.redirect(flask.url_for('comment', id=answer_id))


@app.route('/search/')
def search():
    q = flask.request.args.get('q')
    questions = selectAllQuestion(cur)
    user_id = flask.session.get('user_id')
    if user_id:
        for i in range(len(questions)):
            Q_id = questions[i][0]
            temp = selectCollectionOfUser(cur,user_id,Q_id)
            if len(temp)!=0:
                questions[i].append(1)
    question_of_q = []
    for i in questions:
        if i[2].find(q) != -1 or i[3].find(q) != -1:
            question_of_q.append(i)
    if len(question_of_q)==0:
        context = {
            'error':'没有相关搜索'
        }
        return flask.render_template('error.html', **context)
    context = {
        'questions': question_of_q
    }
    return flask.render_template('index.html', **context)


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if flask.request.method == 'GET':
        return flask.render_template('login.html')
    else:
        telephone = flask.request.form.get('telephone')
        password = flask.request.form.get('password')
        mobile = selectAccountTologin(cur, telephone, password)[0][0]
        u = selectUserOnMobile(cur, mobile)
        if len(u) != 0:
            flask.session['name'] = u[0][1]
            flask.session['user_id'] = u[0][0]
            return flask.redirect(flask.url_for('index'))
        else:
            return u'用户名或密码错误！'

@app.route('/logout/', methods=['GET'])
def logout():
    flask.session.clear()
    return flask.redirect(flask.url_for('login'))


@app.route('/regist/', methods=['GET', 'POST'])
def regist():
    if flask.request.method == 'GET':
        return flask.render_template('regist.html')
    else:
        telephone = int(flask.request.form.get('telephone'))
        username = flask.request.form.get('username')
        password1 = flask.request.form.get('password1')
        password2 = flask.request.form.get('password2')
        email = flask.request.form.get('email')
        sex = flask.request.form.get('sex')
        signDetail = flask.request.form.get('signDetail')
        print(len(password1))
        d = selectUserToReg(cur, telephone)
        if len(d) != 0:
            return u'手机号已经注册过'
        else:
            if password2 != password1 or len(password1) == 0  :
                return u'两次密码不一致'
            else:
                insertUser(cur, username, telephone, email, password1, sex, signDetail)
                conn.commit()
                return flask.redirect(flask.url_for('login'))


@app.route('/changeInfo/', methods=['POST'])
@login_required
def changeInfo():
    return flask.render_template('changeInfo.html')


@app.before_request
def before_request():
    name = flask.session.get('name')
    user_id = flask.session.get('user_id')
    if user_id:
        flask.g.user = name


@app.context_processor
def context_processor():
    username = flask.session.get('name')
    if username:
        return {'username': username}
    else:
        return {}


if __name__ == '__main__':
    app.run()
