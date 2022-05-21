from pandas import Series, DataFrame
import pandas as pd

obj = Series([4, 5, 6, -7])

# print(obj)
#
# print(obj.index)
#
# print(obj.values)

obj2 = Series([4, 7, -5, 3], index=['d', 'b', 'c', 'a'])

# print(obj2)
#
# obj2['c'] = 6
#
# print(obj2)
#
# print('a' in obj2)

# sdata = {'beijing': 35000, 'shanghai': 71000, 'guangzhou': 16000, 'shenzhen': 5000}
# obj3 = Series(sdata)
# print(obj3)
#
# obj3.index = ['bj', 'gz', 'sh', 'sz']
#
# print(obj3)

data = {'city': ['shanghai', 'beijing', 'shenzhen', 'guangzhou'],
        'year': [2016, 2018, 2017, 2019],
        'pop': [1.5, 1.7, 3.4, 2.9]}

frame = DataFrame(data)

frame2 = DataFrame(data, columns=['year', 'city', 'pop'])

# print(frame)
#
# print(frame2)
#
# print(frame2['city'])
# print(frame2.year)
# frame2['new'] = 100
# print(frame2)
#
# frame2['cap'] = frame2.city == 'beijing'
# print(frame2)

# pop = {'beijing': {2008: 1.5, 2009: 2.0},
#        'shanghai': {2008: 2.0, 2009: 3.6}
#        }
#
# frame3 = DataFrame(pop)
# print(frame3.T)

obj4 = Series([4.5, 7.2, -5.3, 3.6], index=['b', 'd', 'c', 'a'])
obj5 = obj4.reindex(['a', 'b', 'c', 'd', 'e'], fill_value=0)

# print(obj5)
obj6 = Series(['blue', 'purple', 'yellow'], index=[0, 2, 4])

# print(obj6.reindex(range(6), method='bfill'))

from numpy import nan as NA
import numpy as np

data = Series([1, NA, 2])
# print(data.dropna())

data2 = DataFrame([[1., 6.5, 3], [1., NA, NA], [NA, NA, NA]])
data2[3] = NA
# print(data2.dropna(how='all', axis=1))

# 返回一个副本
# print(data2.fillna(0))
# # 直接修改原始数据，不返回数据
# print(data2.fillna(0, inplace=True))
# print(data2)

data3 = Series(np.random.randn(10),
               index=[['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'd', 'd'],
                      [1, 2, 3, 1, 2, 3, 1, 2, 2, 3]])
# print(data3)

# print(data3['b':'c'])

# print(data3.unstack())
# print(data3)
# print(data3.unstack().stack())
