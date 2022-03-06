#!/bin/bash

curl  -X DELETE http://192.168.1.102:5000/log/${common_name}
#curl -H "Content-Type:application/json"  -X POST --data '{"username": "${username}", "trusted_ip": "${trusted_ip}", "trusted_port": "${trusted_port}", "local": "${mylocal}", "remote": "${remote}", "ctime": "${ctime}"}' http://192.168.1.102:5000/log
