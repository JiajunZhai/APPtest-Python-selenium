# 拼接字符串和字面量
name = "翟嘉俊"
address = "大田"
tel = 15112001214
print("我的姓名是:" + name + "\n我的地址是:" + address + "\n我的电话是:" + str(tel))
print("完善%s" % tel)

message = "我的姓名是:%s\n我的电话是:%d" % (name, tel)
print(message)
