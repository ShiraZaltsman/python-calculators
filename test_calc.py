import calcfloat
import calcfraction


def test():
    calcfloat.calculate("5.5", "6.7", "+")
    calcfraction.calculate("5.5", "6.7", "+")
    calcfloat.calculate("1.5", "4.7", "+")
    calcfraction.calculate("1.5", "4.7", "+")


test()
