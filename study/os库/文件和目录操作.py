import os


current_dir = os.getcwd()
print(f"当前工作目录: {current_dir}")

# 创建新目录
os.mkdir('new_directory')

# 列出当前目录中的文件和子目录
files = os.listdir('.')
print(f"当前目录中的文件和子目录: {files}")

# 删除目录
os.rmdir('new_directory')