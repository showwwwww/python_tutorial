# 1 to 10 all even square
# alist = []
# for i in range(1, 11):
#     if i % 2 == 0:
#         alist.append(i * i)

blist = [i * i for i in range(1, 11) if i % 2 == 0]

print({i: 1 for i in blist})
