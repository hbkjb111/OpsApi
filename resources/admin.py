# -*- coding: UTF-8 -*-
from flask import abort
from flask_jwt import jwt_required
from flask_restful import fields, marshal_with, Resource
from models import Tadmin
from flask_restful import reqparse
from db import db
from func import SetTable,SetEcho
import time

admin_fields = {
    'id': fields.Integer,
    'username': fields.String,
    # 'password': fields.String,
    'ctime': fields.String,
    'role': fields.Integer
}
echo_fields = {
    "msg": fields.String,
    "data": fields.List(fields.Nested(admin_fields))
}

parser = reqparse.RequestParser()
parser.add_argument('username', type=str, required=True)
parser.add_argument('password', type=str, required=True)
parser.add_argument('role', type=str, required=True)

parser2 = reqparse.RequestParser()
parser2.add_argument('password', type=str, required=False)
parser2.add_argument('role', type=int, required=False)


class AdminList(Resource):

    @marshal_with(echo_fields)
    @SetEcho()
    def get(self, ):
        data = Tadmin.query.all()

        return data


class Admin(Resource):
    @marshal_with(echo_fields)
    @SetEcho()
    def get(self, myid):
        data = Tadmin.query.get(myid)
        return data

    @marshal_with(echo_fields)
    @SetEcho()
    def post(self):
        args = parser.parse_args()
        data = Tadmin()
        data = SetTable(data, args)
        db.session.add(data)
        db.session.commit()
        my_admin = Tadmin.query.filter(Tadmin.username == args['username']).first()
        return my_admin

    @jwt_required()
    @marshal_with(echo_fields)
    @SetEcho()
    def put(self, myid):
        args = parser2.parse_args()
        data = Tadmin.query.get(myid)
        SetTable(data, args)
        db.session.commit()
        my_admin = Tadmin.query.get(myid)
        return my_admin

    @jwt_required()
    @marshal_with(echo_fields)
    @SetEcho()
    def delete(self, myid):
        data = Tadmin.query.get(myid)
        db.session.delete(data)
        db.session.commit()
        return
