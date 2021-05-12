import  os

HOSTNAME = '127.0.0.1' # 主机内网ip
PORT     = '1433' # 端口
DATABASE = 'izhihu' # 数据库名称
USERNAME = 'sa' # 用户名
PASSWORD = '*tx720618' # 密码

DB_URI = 'mssql+pymssql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)

SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = True
DEBUG = True

SECRET_KEY = os.urandom(24) # 生成24位随机字符