
clients_path ="./clients/"

SECRET_KEY='openvpn'

DIALECT = 'mysql'  # 要用的什么数据库
DRIVER = 'pymysql' # 连接数据库驱动
USERNAME = 'openvpn'  # 用户名
PASSWORD ='Ad@123456'  # 密码
HOST = '192.168.62.149'  # 服务器
PORT ='3306' # 端口
DATABASE = 'openvpn' # 数据库名

SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT, DRIVER, USERNAME, PASSWORD, HOST, PORT, DATABASE)
SQLALCHEMY_TRACK_MODIFICATIONS = False


