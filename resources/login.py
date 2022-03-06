from flask_jwt import jwt_required, current_identity
from flask_restful import Resource
from werkzeug.security import safe_str_cmp
from models import Tadmin
from func import SetEcho
#
# class MyUser(object):
#     def __init__(self, id, username, password):
#         self.id = id
#         self.username = username
#         self.password = password
#
#     def __str__(self):
#         return "User(id='%s')" % self.id
#
#
# users = [
#     MyUser(1, 'user1', 'abcxyz'),
#     MyUser(2, 'user2', 'abcxyz'),
# ]
#
# username_table = {u.username: u for u in users}
# userid_table = {u.id: u for u in users}


def authenticate(username, password):
    # user = username_table.get(username, None)
    user=Tadmin.query.filter_by(username=username).first()
    if user and safe_str_cmp(user.password.encode('utf-8'), password.encode('utf-8')):
        return user


def identity(payload):
    user_id = payload['identity']
    # userid_table.get(user_id, None)
    return Tadmin.query.get(user_id)


class Login(Resource):
    @jwt_required()
    def get(self):
        return '%s' % int(current_identity.role)

