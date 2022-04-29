# import os

# print(os.path.abspath('..'))
# print(os.path.exists('/Users'))
# print(os.path.isdir('/Users'))
# print(os.path.isfile('/Users'))
# os.path.join('/temp/a/', 'b/c')

from pathlib import Path
p = Path('.')
print(p.resolve())
# 查找当前目录全部路径
all_paths = [x for x in p.iterdir() if x.is_dir()]
print(all_paths)

q = Path('./tmp/a')
Path.mkdir(q, parents=True)
