#!/bin/bash

DB=openvpn
DBUSER=openvpn
DBPASSWD=Ad@123456

CMD=`mysql -u$DBUSER -p$DBPASSWD $DB -e "select id from t_user where username='${username}' and password = '${password}';"  | wc -l`  
echo $CMD >./1.log
if [ $CMD -eq 2 ];then 
  exit 0;
else 
  exit 1;
fi
