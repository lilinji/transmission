# transmission
用于传输本地NAS 存储和阿里云NAS存储的SDK封装
# AdminSet
<img src="https://travis-ci.org/guohongze/adminset.svg?branch=master"></img> 
<img src="https://img.shields.io/hexpm/l/plug.svg"></img>
[![release](https://img.shields.io/github/release/guohongze/adminset.svg)](https://github.com/lilinji/transmission)
<br>
transmission基于DevOps理念开发，以整合全部运维场景为己任。transmission是一个真正的基于运维思维而开发的全自动化并发数据传输系统。<br>

## v1.0.1 新功能
自动配置config文件.<br>
自动指定 读线程 传输线程.<br>
需要指定原数据路径（目录）<br>
需要指定目的数据路径（目录）<br>

## 开发环境
centos 7.4(1708)  vim （兼容 Notes） python 2.7 兼容（3.4）<br>

## 软件安装
生产服务器建议 4核CPU，8G内存以上.<br>
学习测试建议 2核CPU，2G内存以上.<br>
服务器操作系统版本要求 centos6.0及以上<br>
安装过程不需要任何操作<br>
```
git clone https://github.com/lilinji/transmission.git
```


#### step1:
到当前主机上安装python模块:
```
Python 版本为2.6 以上安装argparse
wget https://pypi.python.org/packages/source/a/argparse/argparse-1.4.0.tar.gz#md5=08062d2ceb6596fcbc5a7e725b53746f
tar -xzvf argparse-1.4.0.tar.gz
cd argparse-1.4.0
python setup.py install
easy_install argparse
pip install argparse
如果提示 -bash: pip command not found
cd /usr/local/src
wget "https://pypi.python.org/packages/source/p/pip/pip-1.5.4.tar.gz#md5=834b2904f92d46aaa333267fb1c922bb" --no-check-certificate
tar -xzvf pip-1.5.4.tar.gz
cd pip-1.5.4
python setup.py install
python setup.py install
```

#### step2:
拷贝源码到指定主机上并执行:
```
sh rsync_data.sh /srcdir/  /desdir/
```

后台运行请参考：
```
nohup java -jar nasimport-v0.1.jar -cc config >master.log 2>&1 &
```

## 访问
https://github.com/lilinji/transmission.git 


## 说明
使用请转到，<a href="https://github.com/lilinji/transmission/README">使用说明</a><br>
功能请转到，<a href="https://github.com/lilinji/transmission/blob/master/transmission/rsync_data.py">功能说明</a><br>
FAQ请转到，<a href="https://www.baidu.com">常见问题</a>

# 安全
最好要将程序启动在有公网可以直接访问的设备上<br>
建议生产环境中使用java jdk1.7 以上配置服务器<br>
由于开发方便，在ptython的settings中开启了DEBUG，在生产中需要关闭并指定自己的域名。

# 开发者交流
请加入开发者群，注明来自github

--------补充-----------


工具运行需要JDK 7或以上版本

1, 修改config文件最上面的参数。
    REPLACE_SRC_DIR: 原始数据的目录, 比如 /data/src/, D:\data\src\
    REPLACE_DST_DIR: 要拷贝的目的目录, 比如  /mnt/nas/, Z:\data\
    REPLACE_THREADS: 并发数。
2，运行
    直接跑： java -jar nasimport-v0.1.jar -cc config
    后台跑： nohup java -jar nasimport-v0.1.jar -cc config 2>&1 &

