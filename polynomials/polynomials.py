from numbers import Number


class Polynomial:
    def __init__(self, coefs):

        self.coefficients = coefs

    def degree(self):

        return len(self.coefficients) - 1

    def __str__(self):

        coefs = self.coefficients
        terms = []
        if coefs[0]:
            terms.append(str(coefs[0]))
        if self.degree() and coefs[1]:
            terms.append(f"{'' if coefs[1] == 1 else coefs[1]}x")

        terms += [f"{'' if c == 1 else c }x^{d}"
                  for d, c in enumerate(coefs[2:], start=2) if c]

        return " + ".join(reversed(terms)) or "0"

    def __eq__(self, other):

        return self.coefficients == other.coefficients

    def __add__(self, other):

        if isinstance(other, Polynomial):
            common = min(self.degree(), other.degree()) + 1
            coefs = tuple(a + b for a, b in zip(self.coefficients,
                          other.coefficients))
            coefs += self.coefficients[common:] + other.coefficients[common:]
            return Polynomial(coefs)

        elif isinstance(other, Number):

            return Polynomial((self.coefficients[0] + other,)
                              + self.coefficients[1:])

        else:
            return NotImplemented

    def __radd__(self, other):

        return self + other

    def __mul__(self, other):

        if isinstance(other, Polynomial):
            total = Polynomial((0,))
            for n, c in enumerate(self.coefficients):
                total += Polynomial(tuple(0 for i in range(n)) + tuple(c*v for v in other.coefficients))
            return total

        elif isinstance(other, Number):
            return Polynomial(tuple(other * c for c in self.coefficients))

        else:
            return NotImplemented

    def __rmul__(self, other):

        return self * other

    def __sub__(self, other):

        return self + -1 * other

    def __rsub__(self, other):

        return other + -1 * self

    def __mod__(self, other):

        rem = self
        i = 1
        degdif = self.degree() - other.degree()
        a = other.coefficients[-1]
        while degdif >= i - 1 and other.degree():
            rem -= (rem.coefficients[-i] / a) * Polynomial(tuple(0 for j in range(degdif + 1 - i)) + (1,)) * other
            i += 1
        return rem







