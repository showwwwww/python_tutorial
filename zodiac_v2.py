
zodiac_name = (u"Capricorn", u"Aquarius", u"Pisces", u"Aries", u"Taurus", u"Gemini",
               u"Cancer", u"Leo", u"Virgo", u"Libra", u"Scorpio", u"Sagittarius")
zodiac_days = ((1, 20), (2, 19), (3, 21), (4, 21), (5, 21), (6, 22),
               (7, 23), (8, 23), (9, 23), (10, 23), (11, 23), (12, 23))

#
int_month = int(input("Input your month: "))
int_day = int(input("Input your day: "))

# for zd_num in range(len(zodiac_days)):
#     if zodiac_days[zd_num] >= (int_month, int_day):
#         print(zodiac_name[zd_num])
#         break
#     elif int_month == 12 and int_day > 23:
#         print(zodiac_name[0])
#         break

n = 0
while zodiac_days[n] < (int_month, int_day):
    if int_month == 12 and int_day > 23:
        break
    n += 1
print(zodiac_name[n])

# zodiac_day = filter(lambda x: x <= (month, day), zodiac_days)

# zodiac_len = len(list(zodiac_day)) % 12
# print(zodiac_name[zodiac_len])
