money = 50
a = 3
b = 2.5
print("money的数据类型是:", type(money), "b的数据类型是:", type(b))
print("当前钱包余额：", money)
print("购买冰激凌，花费:", a)
print("购买可怜，花费:", b)
money = money - a - b
print("最终,钱包剩余:", money)
print("此时money的数据类型是:", type(money))
