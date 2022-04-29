# user1 = {'name': 'tom', 'hp': 100}
# user2 = {'name': 'jerry', 'hp': 100}
#
#
# def print_role(rolename):
#     print('name is %s , hp is %s' % (rolename['name'], rolename['hp']))


class Player:
    def __init__(self, name, hp, occu):
        self.__name = name
        self.hp = hp
        self.__occu = occu

    def print_role(self):
        print('%s %s' % (self.name, self.hp))

    def update_name(self, newname):
        self.__name = newname


class Monster:
    def __init__(self, hp):
        self.hp = hp

    def run(self):
        print("移动到某个位置")

    def whoami(self):
        print("我是怪物父类")


class Animals(Monster):
    """普通怪物"""
    def __init__(self, hp=10):
        super().__init__(hp)


class Boss(Monster):
    """Boss怪物"""
    # def __init__(self, hp=10):
    #     super().__init__(hp)

    def whoami(self):
        print("我是 BOSS 怪物")


a1 = Monster(100)
print(a1.hp)
a2 = Animals(200)
print(a2.hp)
a2.run()
a3 = Boss(1)
print(a3.hp)
a3.whoami()

print("a1的类型 %s" % type(a1))
print("a2的类型 %s" % type(a2))
print("a3的类型 %s" % type(a3))

print(isinstance(a2, Boss))

# user1 = Player('tom', 100, 'warrior')
# user2 = Player('jerry', 100, 'master')
# user1.print_role()
# user2.print_role()
#
# user1.update_name('Fox')
# user1.print_role()
