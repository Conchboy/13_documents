# 1. 打开两个文件
file_read = open("README", "r")
file_write = open("README[copy]", "w")


# 2. 读取old file并写入到new file
text = file_read.read()
file_write.write(text)

# 3. 关闭两个文件
file_read.close()
file_write.close()
