from flask_sqlalchemy import SQLAlchemy
from db import db
import time

#
# class Tcity(db.Model):
#     __tablename__ = 't_city'  # 起表名
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(20), unique=True, nullable=False)


class Tadmin(db.Model):
    __tablename__ = 't_admin'  # 起表名
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(20), nullable=False)
    ctime = db.Column(db.DateTime, default=time.strftime('%Y-%m-%d %H:%M:%S'))
    role = db.Column(db.Integer, default=0)

    def __str__(self):
        return "User(id='%s')" % self.id


class Tuser(db.Model):
    __tablename__ = 't_user'  # 起表名
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(20), nullable=False)
    active = db.Column(db.Integer, default=1)
    expire = db.Column(db.String(20), default="2999-12-31")
    ctime = db.Column(db.DateTime, default=time.strftime('%Y-%m-%d %H:%M:%S'))
    addr = db.Column(db.String(20))
    # city = db.Column(db.String(20))
    ip = db.Column(db.String(20))
    type = db.Column(db.Integer, default=0)
    tag1 = db.Column(db.String(20))
    tag3 = db.Column(db.String(20))
    tag2 = db.Column(db.String(20))


class Tlog(db.Model):
    __tablename__ = 't_log'  # 起表名
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), )
    trusted_ip = db.Column(db.String(20))
    trusted_port = db.Column(db.String(20))
    local = db.Column(db.String(20))
    remote = db.Column(db.String(20))
    ctime = db.Column(db.DateTime, default=time.strftime('%Y-%m-%d %H:%M:%S'))
