chinese_zodiac = "猴鸡狗猪鼠牛虎兔龙蛇马羊"
zodiac_name = (u"Capricorn", u"Aquarius", u"Pisces", u"Aries", u"Taurus", u"Gemini",
               u"Cancer", u"Leo", u"Virgo", u"Libra", u"Scorpio", u"Sagittarius")
zodiac_days = ((1, 20), (2, 19), (3, 21), (4, 21), (5, 21), (6, 22),
               (7, 23), (8, 23), (9, 23), (10, 23), (11, 23), (12, 23))

cz_num = {}
for i in chinese_zodiac:
    cz_num[i] = 0

z_num = {}
for i in zodiac_name:
    z_num[i] = 0

while True:
    year = int(input("Input your year: "))
    month = int(input("Input your month: "))
    day = int(input("Input your day: "))

    n = 0
    while zodiac_days[n] < (month, day):
        if month == 12 and day > 23:
            break
        n += 1
    cz_num[chinese_zodiac[year % 12]] += 1
    z_num[zodiac_name[n]] += 1

    for each_key in cz_num.keys():
        print("生肖 %s 有 %d 个" % (each_key, cz_num[each_key]))

    for each_key in z_num.keys():
        print("星座 %s 有 %d 个" % (each_key, z_num[each_key]))
