from numbers import Number


class Polynomial:
    def __init__(self, coefs):

        self.coefficients = coefs

    @property
    def coefficients(self):

        return self.__coefficients
    
    @coefficients.setter
    def coefficients(self, value):

        deg = len(value)
        i = deg
        while not value[i - 1] and i - 1 and i:
            i -= 1
        self.__coefficients = value[:i]


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

    def __floordiv__(self, other):

        if isinstance(other, Polynomial):
            rem = self
            i = 1
            degdif = self.degree() - other.degree()
            a = other.coefficients[-1]
            quotient = []
            while  rem.degree() >= other.degree() and other.degree():
                quotient.append(rem.coefficients[-1] / a)
                rem -= (rem.coefficients[-1] / a) * Polynomial(tuple(0 for j in range(degdif + 1 - i)) + (1,)) * other
                i += 1
            return Polynomial(tuple(reversed(quotient))) or Polynomial((0,))
        
        elif isinstance(other, Number):
            return self * (1 / other)

        else:
            return NotImplemented

    def __mod__(self, other):

        if isinstance(other, Polynomial):
            return self - (self // other) * other

        else:
            return NotImplemented

    def __pow__(self, other):

        if isinstance(other, int):
            ev = 1
            for i in range(other):
                ev *= self
            return ev
        
        else:
            return NotImplemented
    


    def __call__(self, x):

        if isinstance(x, (Number, Polynomial)):
            ev = self.coefficients[0]
            d = self.degree()
            for i, c in enumerate(reversed(self.coefficients[1:])):
                ev += c * (x ** (d - i))
            return ev

        else:
            return NotImplemented


    def diff(self, x=None):
        
        dp = Polynomial(tuple(c*d for c, d in enumerate(self.coefficients[1:], start=1)))
        
        if x == None:
            return dp
        
        elif isinstance(x, (Number, Polynomial)):
            return dp(x)

        else:
            return NotImplemented

    def integrate(pol, bounds):

        P = Polynomial( (0,) + tuple(c/(d) for d, c in enumerate(pol.coefficients, start=1)))
        if isinstance(bounds[0], Number) and isinstance(bounds[1], Number):
            return P(bounds[1]) - P(bounds[0])

        else:
            return NotImplemented

