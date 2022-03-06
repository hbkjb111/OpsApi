# -*- coding: UTF-8 -*-
from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from flask_jwt import JWT
from resources.city import *
from resources.admin import *
from resources.user import *
from resources.login import *
from resources.log import *
import config

app = Flask(__name__)
CORS(app)


# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///openvpn.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.debug = True

# 跨域支持

app.config.from_object(config)
jwt = JWT(app, authenticate, identity)
api = Api(app)

# api.add_resource(CityList, '/citys')

api.add_resource(AdminList, '/admins')
api.add_resource(Admin, '/admin', '/admin/<int:myid>')

api.add_resource(UserList, '/users')
api.add_resource(User, '/user', '/user/<int:myid>')
api.add_resource(LogsList, '/logs')

api.add_resource(Login, '/login')

echo = {
    "msg": "error request",
    "data": None,
}


@app.errorhandler(404)
@app.errorhandler(500)
@app.errorhandler(Exception)
def errorHandler(e):
    return echo


if __name__ == '__main__':
    from db import db

    db.init_app(app)
    # db.create_all(app=app)
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True
    )
