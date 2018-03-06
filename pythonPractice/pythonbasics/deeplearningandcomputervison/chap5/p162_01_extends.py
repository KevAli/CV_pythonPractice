from p161_02 import A


class B(A):
    """Class B inheritenced form A"""

    def greeting(self):
        print("How is it going!")


b = B(12, 12, 'Flauber')
print(b.__doc__)
b.introduce()
b.greeting()
print(b._name)
print(b._A__l2norm())
