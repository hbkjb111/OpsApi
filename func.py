from config import clients_path


def SetTable(obj, mydict):
    for a in dir(obj):
        if not a.startswith('__'):
            if a in mydict:
                if mydict[a] is not None:
                    setattr(obj, a, mydict[a])
    return obj


def getNewIp(str_ip):
    newip = ""
    ip_list = str_ip.split(".")

    if (int(ip_list[3]) % 4 == 1) & (int(ip_list[2]) < 255):
        if int(ip_list[3]) + 4 > 253:
            s2 = str(int(ip_list[2]) + 1)
            s3 = str(1)
        else:
            s2 = ip_list[2]
            s3 = str(int(ip_list[3]) + 4)
        newip = ip_list[0] + '.' + ip_list[1] + '.' + s2 + '.' + s3
    return newip


def sortIpList(iplist):
    bigip = ''
    import socket
    sort_ip_list = sorted(iplist, key=socket.inet_aton)
    bigip = sort_ip_list[len(sort_ip_list) - 1]
    return bigip


def GetUserIp(Tobj):
    ip_list = ["10.8.10.1"]
    data_ips = Tobj.query.with_entities(Tobj.ip).all()
    for data_ip in data_ips:
        if data_ip[0] is not None:
            ip_list.append(data_ip[0])
    bigip = sortIpList(ip_list)
    ip = getNewIp(bigip)
    return ip


def Creat_ip_file(ip, fileneme):
    ip_list = ip.split(".")
    ip_list[3] = str(int(ip_list[3]) + 1)
    new_ip = ".".join(ip_list)
    cmd = 'ifconfig-push ' + ip + ' ' + new_ip
    path_file = clients_path + fileneme
    f = open(path_file, 'w+', encoding='utf8')
    f.write(cmd)
    f.close()


def Delete_ip_file(fileneme):
    import os
    path_file = clients_path + fileneme
    os.remove(path_file)





class Echo:
    def __init__(self):
        self.echo_fields = None
        self.echo = {
            "msg": "ok",
            "data": None
        }

    def setFields(self, myfields):
        from flask_restful import fields
        self.echo_fields = {
            "msg": fields.String,
            "data": fields.List(fields.Nested(myfields))
        }

    def setEcho(self, data):
        self.echo['data'] = data
        return self.echo


class SetEcho:
    def __call__(self, f):
        # @wraps(f)
        def wrapper(*args, **kwargs):
            resp = f(*args, **kwargs)
            echo = {
                "msg": "ok",
                "data": resp
            }
            return  echo

        return wrapper







