ps aux | grep java | grep nasimport | awk '{print $2}' | xargs -I{} kill -9 {}
pwd
nohup java -jar nasimport-v0.1.jar -cc config >master.log 2>&1 &

