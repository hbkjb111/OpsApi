# -*- coding: UTF-8 -*-
from flask import request
from flask_jwt import jwt_required
from flask_restful import fields, marshal_with, Resource
from flask import jsonify
from models import Tuser
from flask_restful import reqparse
from db import db
from func import *

user_fields = {
    'id': fields.Integer,
    'username': fields.String,
    'password': fields.String,
    'active': fields.Integer,
    'expire': fields.String,
    'ip': fields.String,
    'type': fields.Integer,
    # 'alias': fields.String,
    'ctime': fields.String,
    'addr': fields.String,
    # 'city': fields.String,
    # 'tag1': fields.String,
    # 'tag2': fields.String,
    # 'tag3': fields.String
}

echo_fields = {
    "msg": fields.String,
    "data": fields.List(fields.Nested(user_fields))
}

parser = reqparse.RequestParser()
parser.add_argument('username', type=str, required=True)
parser.add_argument('password', type=str, required=True)
parser.add_argument('type', type=int, required=True)
parser.add_argument('city', type=str, )
parser.add_argument('addr', type=str, )
parser.add_argument('tag1', type=str, )
parser.add_argument('tag2', type=str, )
parser.add_argument('tag3', type=str, )

parser2 = reqparse.RequestParser()
parser2.add_argument('username', type=str, )
parser2.add_argument('type', type=int, )
parser2.add_argument('city', type=str, )
parser2.add_argument('addr', type=str, )
parser2.add_argument('tag1', type=str, )
parser2.add_argument('tag2', type=str, )
parser2.add_argument('tag3', type=str, )


class UserList(Resource):
    @marshal_with(echo_fields)
    @SetEcho()
    def get(self, ):
        condition = []
        args = parser2.parse_args()
        if args["username"] is not None:
            condition.append(Tuser.username == args["username"])
        if args["type"] is not None:
            condition.append(Tuser.role == args["type"])
        data = Tuser.query.filter(*condition).all()
        return data


class User(Resource):
    @marshal_with(echo_fields)
    @SetEcho()
    def get(self, myid):
        data = Tuser.query.get(myid)
        return data

    @marshal_with(echo_fields)
    @SetEcho()
    def post(self):
        args = parser.parse_args()
        data = Tuser()
        data = SetTable(data, args)
        data.ip = GetUserIp(Tuser)
        db.session.add(data)
        db.session.commit()

        my_user = Tuser.query.filter(Tuser.username == args['username']).first()
        filename = str(my_user.id)
        Creat_ip_file(data.ip, filename)
        return my_user

    @jwt_required()
    @marshal_with(echo_fields)
    @SetEcho()
    def put(self, myid):
        args = parser2.parse_args()
        data = Tuser.query.get(myid)
        SetTable(data, args)
        db.session.commit()
        return  data

    @jwt_required()
    @marshal_with(echo_fields)
    @SetEcho()
    def delete(self, myid):
        data = Tuser.query.get(myid)
        filename = data.id
        db.session.delete(data)
        db.session.commit()
        # file handle
        Delete_ip_file(filename)
        return
