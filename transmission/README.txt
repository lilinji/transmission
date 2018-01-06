工具运行需要JDK 7或以上版本

1, 修改config文件最上面的参数。
    REPLACE_SRC_DIR: 原始数据的目录, 比如 /data/src/, D:\data\src\
    REPLACE_DST_DIR: 要拷贝的目的目录, 比如  /mnt/nas/, Z:\data\
    REPLACE_THREADS: 并发数。
2，运行
    直接跑： java -jar nasimport-v0.1.jar -cc config
    后台跑： nohup java -jar nasimport-v0.1.jar -cc config 2>&1 &

