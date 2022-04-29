# 日常应用比较广泛的模块是：
# 1、文字处理的 re
# 2、日常其类型的 time、datetime
# 3、数字和数学类型的 math、random
# 4、文件和目录访问的 pathlib、os.path
# 5、数据压缩和归档的 tarfile
# 6、通用操作系统的 os、logging、argparse
# 7、多线程的 threading、queue
# 8、Internet 数据处理的 base64、json、urllib
# 9、结构化标记处理工具的 html、xml
# 10、开发工具的 unitest
# 11、调试工具的 timeit
# 12、软件包发布的 venv
# 13、运行服务的 __main__


# . ^ $ * + ? {m} {m,n} {} | \d \D \s ()
# ^$
# .*?

import re

# p = re.compile(r'(\d+)-(\d+)-(\d+)')
# print(p.match('2019-05-10').groups())
#
# year, month, day = [int(i) for i in p.match('2019-05-10').groups()]
# print(type(year), month, day)

# print(p.search('aa2019-05-19bb'))

# phone = '123-456-789 # 这是电话好吗'
# p2 = re.sub(r'#.+$', '', phone)
# print(p2)
# p3 = re.sub(r'\D', '', p2)
# print(p3)
