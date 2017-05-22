最近学习了一些Socket编程，于是用Python写了一个基于TCP的点对点即时聊天小工具。

感觉还可以加上文件发送，消息加密，聊天请求确认等等很多东西，日后有空再扩展吧。

用multiprocessing启动Server，threading启动Client，实现了同时收发消息。

    start_server(8081) #Server（本机）端口
    start_client('192.168.2.1', 1234) #Client（目标主机）IP及端口 
    
![此处输入图片的描述][1]


  [1]: http://i4.buimg.com/1949/bcaebb1cdd7e47db.png