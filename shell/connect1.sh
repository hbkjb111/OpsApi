#!/bin/bash

DB=openvpn
DBUSER=openvpn
DBPASSWD=Ad@123456


CMD=`mysql -u$DBUSER -p$DBPASSWD $DB -e "insert into t_log(username,trusted_ip,trusted_port,local,remote) values('${username}','${trusted_ip}','${trusted_port}','${ifconfig_local}','${ifconfig_local}','$ifconfig_pool_remote_ip');"  | wc -l`

