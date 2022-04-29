# record zodiac, according to input to judge zodiac

chinese_zodiac = "猴鸡狗猪鼠牛虎兔龙蛇马羊"

# year = int(input("input your birth year: "))
#
# if chinese_zodiac[year % 12] == '狗':
#     print("dog year is lucky...")

# for cz in chinese_zodiac:
#     print(cz)
#
# for i in range(1, 13):
#     print(i)

# for year in range(2000, 2023):
#     print("%s 年的生肖是 %s" % (year, chinese_zodiac[year % 12]))

num = 5
while True:
    num += 1
    if num == 10:
        continue
    elif num > 20:
        break
    print(num)
