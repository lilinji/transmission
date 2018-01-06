#!/bin/bash
#########################################################################
# File Name: rsync_data.sh
# Author: lilinji
# mail: lilinji@novogene.com
# Created Time: Fri 05 Jan 2018 05:45:02 PM CST
#########################################################################
if [ ! -d "$1" ] && [ -d "$2"];then  
	echo "please input source dir and des dir "
	echo "sh rsync_data.sh /NJPROJ1/XXX/  /NJPROJ2/XXX/"
elif [ ! -d "$2" ];then 
        echo "please input source dir"
else 
	python  rsync_data.py  -s $1  -d $2  -l 6 -p 12
	echo 'scp' $1 to ... $2 ar you sure ?

	echo 'run......'
	/bin/sh start.sh
fi 
sleep 2

rm master.log config 
