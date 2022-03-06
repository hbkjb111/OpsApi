# -*- coding: UTF-8 -*-
# from flask_restful import fields, marshal_with, Resource
# from models import Tcity
# from func import  SetEcho
#
# city_fields = {
#     'id': fields.Integer,
#     'name': fields.String
# }
# echo_fields = {
#     "msg": fields.String,
#     "data": fields.List(fields.Nested(city_fields))
# }
#
#
#
# class CityList(Resource):
#     @marshal_with(echo_fields)
#     @SetEcho()
#     def get(self):
#         data = Tcity.query.all()
#         return data

