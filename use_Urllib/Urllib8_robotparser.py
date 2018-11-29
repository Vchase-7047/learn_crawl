from urllib.robotparser import RobotFileParser


rp = RobotFileParser()  # 创建RobotFileParser对象
rp.set_url('http://www.jianshu.com/robots.txt')  # 设置robots.txt的链接
rp.read()
print(rp.can_fetch('*','http://www.jianshu.com/p/b67554025d7d'))
print(rp.can_fetch('*','http://www.jianshu.com/search?q=python&page=l&type=collections'))