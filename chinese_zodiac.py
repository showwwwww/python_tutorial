# record zodiac, according to input to judge zodiac

chinese_zodiac = "猴鸡狗猪鼠牛虎兔龙蛇马羊"

# print(chinese_zodiac[1:4])

# print(chinese_zodiac[-1])

year = 2022
print(chinese_zodiac[year % 12])

print('狗' not in chinese_zodiac)

print(chinese_zodiac + chinese_zodiac)

print(chinese_zodiac * 3)
