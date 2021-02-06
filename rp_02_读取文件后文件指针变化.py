# *-* utf-8 *-*
import _locale
_locale._getdefaultlocale = (lambda *args: ['zh_CN', 'utf8'])

# 1. 打开文件
file = open("README") #, encoding="utf-8")
# 2. 读取文件内容
test = file.read()
print(test)
print(len(test))

print("-" * 50)

test = file.read()
print(test)
print(len(test))

# 3. 关闭文件
file.close()
