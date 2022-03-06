# -*- coding: UTF-8 -*-
from flask_jwt import jwt_required
from flask import request
from flask_restful import fields, marshal_with, Resource
from flask.views import MethodView
from models import Tlog, Tuser
from flask_restful import reqparse
from db import db
from func import SetTable, SetEcho

import time

log_fields = {
    'id': fields.Integer,
    'username': fields.String,
    'trusted_ip': fields.String,
    'trusted_port': fields.String,
    'local': fields.String,
    'remote': fields.String,
    'ctime': fields.String
}
echo_fields = {
    "msg": fields.String,
    "data": fields.List(fields.Nested(log_fields))
}

parser = reqparse.RequestParser()
parser.add_argument('username', type=str, required=True)
parser.add_argument('trusted_ip', type=str, required=True)
parser.add_argument('trusted_port', type=str, required=True)
parser.add_argument('local', type=str, required=True)
parser.add_argument('remote', type=str, required=True)

parser2 = reqparse.RequestParser()
parser2.add_argument('username', type=str, )


class LogsList(Resource):
    @marshal_with(echo_fields)
    @SetEcho()
    def get(self, ):
        condition = []
        args = parser2.parse_args()
        if args["username"] is not None:
            condition.append(Tlog.username == args["username"])
        data = Tlog.query.filter(*condition).all()

        user_dict = {}
        user_data = Tuser.query.all()
        for user in user_data:
            user_dict[str(user.id)] = user.username
        for index,log in enumerate(data):
            if user_dict[log.username] is not None:
                data[index].username=user_dict[log.username]

        return data

#
# class Log(Resource):
#
#     @marshal_with(echo_fields)
#     @SetEcho()
#     def get(self, ):
#         condition = []
#         args = parser2.parse_args()
#         if args["username"] is not None:
#             condition.append(Tlog.username == args["username"])
#         data = Tlog.query.filter(*condition).all()
#         return data
#
#     @marshal_with(echo_fields)
#     @SetEcho()
#     def post(self):
#         args = parser.parse_args()
#         data = Tlog()
#         data = SetTable(data, args)
#         db.session.add(data)
#         db.session.commit()
#         return
#
#     @marshal_with(echo_fields)
#     @SetEcho()
#     def delete(self, username):
#         data = Tlog.query.filter_by(username=username).first()
#         db.session.delete(data)
#         db.session.commit()
#         return
