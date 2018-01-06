#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author                : lilinji
# Created               : 5th January 2018
# Last Modified         :
# Version               : 1.0
# Modifications         :
# Description           : Tests to see if the directory testdir exists, if not it will create the directory for you
import sys
import os
import argparse
import json
import time
import re
#import encoding
################传参程序
#print "程序名：", sys.argv[0]
########################
parser = argparse.ArgumentParser(description='manual to this script')
parser.add_argument('-s','--srcdir', type=str, default='/srv', help="set source dir")
parser.add_argument('-d','--dstdir', type=str, default='/srv', help="set dest dir  ")
parser.add_argument('-l','--therad', type=str, default='6', help="set scan line")
parser.add_argument('-p','--therads', type=str, default='12', help="set cp line therads")
help = 'python modfiy_conf_json.py -s /TJPROJ1/RNA/test -d /ALNAS01/lilinji -l 6 -p 12'
parser.add_argument('-v','--version', type=str, help=help)
args = parser.parse_args() #参数赋值
if args.version:
	         print ("verbosity turned on")
os.getcwd()
#print os.getcwd()
#############TIME
s = time.ctime()
tail = '''
################ 以▒~J▒~E~M置▒~I~K▒~J▒修▒~T▒ ###################################

step1=nasFileNameLister
step2=basicMetaGetterSet
step3=basicMetaVerifierSet
step4=fileCopiersSameTime
#step4=fileCopiersSameAttr
step5=stringToFile

nasFileNameLister.class=com.aliyun.nas.producer.NasFileNameLister
nasFileNameLister.NasFileNameLister.rootPath=REPLACE_SRC_DIR
nasFileNameLister.NasFileNameLister.threads=REPLACE_SCAN_THREADS

basicMetaGetterSet.class=com.aliyun.nas.consumer.ConsumerSet
basicMetaGetterSet.ConsumerSet.realConsumer=com.aliyun.nas.consumer.meta.BasicMetaGetter
basicMetaGetterSet.ConsumerSet.threads=REPLACE_SCAN_THREADS
basicMetaGetterSet.BasicMetaGetter.rootDir=REPLACE_SRC_DIR

basicMetaVerifierSet.class=com.aliyun.nas.consumer.ConsumerSet
basicMetaVerifierSet.ConsumerSet.realConsumer=com.aliyun.nas.consumer.meta.BasicMetaVerifier
basicMetaVerifierSet.ConsumerSet.threads=REPLACE_SCAN_THREADS
basicMetaVerifierSet.BasicMetaVerifier.rootDir=REPLACE_DST_DIR

fileCopiersSameTime.class=com.aliyun.nas.consumer.ConsumerSet
fileCopiersSameTime.ConsumerSet.realConsumer=com.aliyun.nas.consumer.copier.FileCopierSameTime
fileCopiersSameTime.ConsumerSet.threads=REPLACE_COPY_THREADS
fileCopiersSameTime.ConsumerSet.IOController.quotaMBs=9000
fileCopiersSameTime.ConsumerSet.IOController.strategy=
fileCopiersSameTime.FileCopierSameTime.srcDir=REPLACE_SRC_DIR
fileCopiersSameTime.FileCopierSameTime.dstDir=REPLACE_DST_DIR
fileCopiersSameAttr.class=com.aliyun.nas.consumer.ConsumerSet
fileCopiersSameAttr.ConsumerSet.realConsumer=com.aliyun.nas.consumer.copier.FileCopierSameAttr
fileCopiersSameAttr.ConsumerSet.threads=REPLACE_COPY_THREADS
fileCopiersSameAttr.ConsumerSet.IOController.quotaMBs=9000
fileCopiersSameAttr.ConsumerSet.IOController.strategy=
fileCopiersSameAttr.FileCopierSameAttr.srcDir=REPLACE_SRC_DIR
fileCopiersSameAttr.FileCopierSameAttr.dstDir=REPLACE_DST_DIR

stringToFile.class=com.aliyun.nas.consumer.StringFileWriter
stringToFile.StringFileWriter.filename=copied_files
stringToFile.StringFileWriter.append=true

noVerify=1
loop=1'''
head = '''ps aux | grep java | grep nasimport | awk '{print $2}' | xargs -I{} kill -9 {}
pwd'''
#nohup java -jar nasimport-v0.1.jar -cc config >master.log 2>&1 &

print (s)
def WriteToFileUsePrint():
    saveout = sys.stdout
    fd = open('config', 'w')
    sys.stdout = fd
    print ('REPLACE_SRC_DIR='+args.srcdir)
    print ('REPLACE_DST_DIR='+args.dstdir)
    print ('REPLACE_SCAN_THREADS='+args.therad)
    print ('REPLACE_COPY_THREADS='+args.therads) 
    print (tail)
    fd.close()
def WriteToFileUsePrint1():
    saveout = sys.stdout
    fd = open('start.sh', 'w')
    sys.stdout = fd
    print (head)
    print ("nohup java -jar nasimport-v0.1.jar -cc config >master.log 2>&1 &")
    fd.close()
if __name__ == '__main__':
	print ('''hello word''')
	WriteToFileUsePrint()
	WriteToFileUsePrint1()
os.system('chmod 755 start.sh')

