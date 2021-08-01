from polynomials import Polynomial


def test_print():

    p = Polynomial((2, 1, 0, 3))

    assert str(p) == "3x^3 + x + 2"

    p = Polynomial((-42, 0, -12, 1))
    q = Polynomial((-3, 1))

    assert str(p % q) == "-123.0"

