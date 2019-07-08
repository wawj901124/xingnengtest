import os

cmdorder = r"locust -f D:\Users\Administrator\PycharmProjects\xingnengtest\mylocu\myfirst.py --csv=foobar --host=https://bjw.halodigit.com:9060  --no-web -c10  -r2 -t 1m"
#-f是指定一个python文件 后面跟上咱们刚才写的python文件
#--host是你要访问哪个网站，后面跟网站的url
#启动参数：--no - web 表示不使用web界面运行测试。  -c设置虚拟用户数 。  -r设置每秒启动虚拟用户数  。 -t设置运行时间.。
#no-web模式运行将测试结果保存到当前.py目录中：locust -f xxoo.py --csv=起一个名字

cmdorder = r"locust -f D:\Users\Administrator\PycharmProjects\xingnengtest\mylocu\myfirst.py --csv=foobar --host=https://bjw.halodigit.com:9060"

cmdorder = r"locust -f D:\Users\Administrator\PycharmProjects\xingnengtest\mylocu\secondsample.py "
os.popen(cmdorder)