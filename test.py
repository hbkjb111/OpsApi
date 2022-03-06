from flask_restful import fields, marshal_with
def SetEcho(a_func):
    def wrapTheFunction():
        echo = {
            "msg": "ok",
            "data": a_func()
        }
        return echo

    return wrapTheFunction

echo_fields = {
    "msg": fields.String,
    "data": fields.String
}

@SetEcho
@marshal_with(echo_fields)
def func2():

     return "ok"


print(func2())
