# *-* utf8 *-*
# 1. 打开文件
file = open("README")
# 2. 读取文件内容
test = file.read()
print(test)

print("-" * 50)
# 3. 关闭文件
file.close()
