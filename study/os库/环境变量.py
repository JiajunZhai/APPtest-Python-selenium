import os

# 获取环境变量
path = os.getenv('PATH')
print(f"PATH 环境变量: {path}")

# 设置环境变量
os.putenv('MY_VAR', 'my_value')

# 获取所有环境变量
env_vars = os.environ
print(f"所有环境变量: {env_vars}")