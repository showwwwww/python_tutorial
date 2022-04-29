# record novel major person in file
# file1 = open("name.txt", 'w')
# file1.write('诸葛亮')
# file1.close()

# file2 = open("name.txt")
# print(file2.read())
# file2.close()

# file3 = open("name.txt", 'a')
# file3.write("刘备")
# file3.close()

# file4 = open("name.txt")
# for line in file4.readlines():
#     print(line)
#     print("======")
# file4.close()

file5 = open("ThreeKingdoms/name.txt", "rb")
print(file5.tell())
print(file5.read(3))
print(file5.tell())
# 第一个参数代表偏移位置，第二个参数 0 表示从文件开头偏移 1 表示从当前位置偏移 2 从文件结尾
file5.seek(1, 2)
print(file5.tell())
file5.close()
