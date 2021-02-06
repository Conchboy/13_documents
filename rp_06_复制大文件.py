# 1. 打开两个文件
file_read = open("README", "r", encoding="utf-8")
file_write = open("README[copy]", "a")


# 2. 读取old file并写入到new file
while True:
    text = file_read.readline()
    if not text:
        break
    file_write.write(text)


# 3. 关闭两个文件
file_read.close()
file_write.close()
