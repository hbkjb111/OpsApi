#!/bin/bash
username= ${common_name}


curl -H "Content-Type:application/json"  -X POST --data '{"username": "'${username}'", "trusted_ip": "'${trusted_ip}'", "trusted_port": "'${trusted_port}'", "local": "'${ifconfig_local}'", "remote": "'$ifconfig_pool_remote_ip'"}'  http://192.168.1.102:5000/log
