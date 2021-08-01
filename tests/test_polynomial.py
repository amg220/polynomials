from polynomials import Polynomial


def test_print():

    p = Polynomial((2, 1, 0, 3))

    assert str(p) == "3x^3 + x + 2"

    p = Polynomial((-42, 0, -12, 1))
    q = Polynomial((-3, 1))
    r = Polynomial((1, 0, 1))

    assert p // q == Polynomial((-27, -9, 1))
    assert p % q == Polynomial((-123,))
    assert p(3) == -123
    assert q ** 2 == Polynomial((9, -6, 1))
    assert r(q) == Polynomial((10, -6, 1))
    assert p.diff() == Polynomial((0, -24, 3))
    assert p.diff(8) == 0
    assert Polynomial.integrate(q, (0, 1)) == -2.5