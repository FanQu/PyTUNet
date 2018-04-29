# 这是用于THU校园网络账号登陆的python3脚本
个人用于树莓派的后台联网进程，可以保持树莓派联网，也可用于其他平台。

如果是用网线连接，则需要将tunet_login.py中的`r = requests.post('http://net.tsinghua.edu.cn/do_login.php', data=data)`改为
```
r = requests.post('https://auth4.tsinghua.edu.cn/srun_portal_pc.php?ac_id=1&noforward=1', data=data)
```

如果只要校内连接不需要连接外网，则在输入id时在id后面加上@tsinghua
e.g.  原输入的id为netID
      新输入的id为newID@tsinghua
则可以只连接校园内网。
