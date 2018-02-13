class A:
    """Class A"""

    def __init__(self, x, y, name):
        self.x = x
        self.y = y
        self._name = name

    def introduce(self):
        print(self._name)

    #@staticmethod
    def greeting():
        print("What's up")

    def __l2norm(self):
        return self.x ** 2 + self.y ** 2

    def cal_l2norm(self):
        return self.__l2norm()


# a = A(10, 10, 'Leonardo')
# print(a.__doc__)
# a.introduce()
# a.greeting()
# print(a._name)
# print(a.cal_l2norm())
# print(a._A__l2norm())
