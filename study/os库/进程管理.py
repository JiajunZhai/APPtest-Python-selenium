import os

# 执行系统命令
os.system('echo Hello, World!')

# 获取当前进程ID
pid = os.getpid()
print(f"当前进程ID: {pid}")

# 获取父进程ID
ppid = os.getppid()
print(f"父进程ID: {ppid}")