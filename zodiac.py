
# zodiac_name = (u"Capricorn", u"Aquarius", u"Pisces", u"Aries", u"Taurus", u"Gemini",
#                u"Cancer", u"Leo", u"Virgo", u"Libra", u"Scorpio", u"Sagittarius")
# zodiac_days = ((1, 20), (2, 19), (3, 21), (4, 21), (5, 21), (6, 22),
#                (7, 23), (8, 23), (9, 23), (10, 23), (11, 23), (12, 23))
#
# [month, day] = [2, 15]
#
# zodiac_day = filter(lambda x: x <= (month, day), zodiac_days)
#
# zodiac_len = len(list(zodiac_day)) % 12
# print(zodiac_name[zodiac_len])

a_list = ['abc', 'xyz']
a_list.append('X')
print(a_list)
a_list.remove('xyz')
print(a_list)
