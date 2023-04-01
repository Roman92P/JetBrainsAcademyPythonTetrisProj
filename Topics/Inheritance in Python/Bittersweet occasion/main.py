# finish the function
import sys


def find_the_parent(child):
    all_cls = ['Drinks', 'Pastry', 'Sweets']
    for c in all_cls:
        if issubclass(child, getattr(sys.modules[__name__], c)):
            print(c)
    # if issubclass(child, Drinks):
    #     print(Drinks.__name__)
    # elif issubclass(child, Pastry):
    #     print(Pastry.__name__)
    # elif issubclass(child, Sweets):
    #     print(Sweets.__name__)
