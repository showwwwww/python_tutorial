import re


def find_item(hero):
    with open("sanguo.txt", encoding="GB18030") as f1:
        data = f1.read().replace('\n', '')
    return re.findall(hero, data)


# read person info
name_dict = {}
with open("name.txt") as f:
    for line in f:
        names = line.split('|')
        for n in names:
            name_num = find_item(n)
            name_dict[n] = len(name_num)


name_sorted = sorted(name_dict.items(), key=lambda item: item[1], reverse=True)
print(name_sorted)
