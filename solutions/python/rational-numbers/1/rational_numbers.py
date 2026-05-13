from __future__ import division


class Rational(object):
    def __init__(self, numer, denom):
        self._numer = numer
        self._denom = denom
        self.reduce()
        self.normalize_signs()

    @property
    def numer(self):
        return self._numer

    @numer.setter
    def numer(self, value):
        self._numer = value

    @property
    def denom(self):
        if self.numer:
            if self._denom:
                return self._denom
            else:
                raise ZeroDivisionError("Denominator cannot be zero!")
        else:
            return 1

    @denom.setter
    def denom(self, value):
        self._denom = value

    def reduce(self):
        """ Find the greatest common divisor of the numerator and the
        denominator and divide them both by it. """
        div = 2
        while div <= min(abs(self.numer), abs(self.denom)):
            if self.numer % div == 0 and self.denom % div == 0:
                self.numer //= div
                self.denom //= div
            else:
                div += 1

    def normalize_signs(self):
        """ Checks if the ratio is positive, otherwise only the numerator
        should bear the negative sign. """
        if self.numer < 0 and self.denom < 0:
            self.numer = abs(self.numer)
            self.denom = abs(self.denom)
        if self.numer > 0 and self.denom < 0:
            self.numer = - self.numer
            self.denom = abs(self.denom)

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return '{}/{}'.format(self.numer, self.denom)

    def __add__(self, other):
        return Rational(self.numer * other.denom + other.numer * self.denom, self.denom * other.denom)

    def __sub__(self, other):
        return Rational(self.numer * other.denom - other.numer * self.denom, self.denom * other.denom)

    def __mul__(self, other):
        return Rational(self.numer * other.numer, self.denom * other.denom)

    def __truediv__(self, other):
        return Rational(self.numer * other.denom, self.denom * other.numer)

    def __abs__(self):
        return Rational(abs(self.numer), abs(self.denom))

    def __pow__(self, power):
        if power >= 0:
            return Rational(self.numer ** power, self.denom ** power)
        else:
            return Rationa(self.denom ** power, self.numer ** power)

    def __rpow__(self, base):
        return (base ** self.numer) ** (1 / self.denom)
