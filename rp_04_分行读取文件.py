# 1. 打开文件
file = open("README")

# 2. 分行读取并打印
while True:
    test = file.readline()
    #
    if not test:
        break
    print(test)

# 3. 关闭文件
file.close()
