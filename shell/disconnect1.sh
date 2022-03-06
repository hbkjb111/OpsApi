#!/bin/bash

DB=openvpn
DBUSER=openvpn
DBPASSWD=Ad@123456


CMD=`mysql -u$DBUSER -p$DBPASSWD $DB -e "delete where username='${common_name}';"`

