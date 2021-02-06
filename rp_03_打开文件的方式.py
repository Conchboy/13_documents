# f.read(filename, open_way)
# 1. 打开文件
file = open("README", "w+")

# 2. 写入
for i in range(10):
    file.write("hello %d \n" % (i+1))

file.seek(0)
test = file.read()
print(test)

# 3. 关闭
file.close()
