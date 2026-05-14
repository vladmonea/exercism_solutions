from math import sin, cos, e


class ComplexNumber(object):
    def __init__(self, real, imag):
        self.real = real
        self.imaginary = imag

    def __str__(self):
        sign = '' if self.imaginary < 0 else '+'
        return f"{self.real} {sign} {self.imaginary}i"

    def __add__(self, other):
        return ComplexNumber(
            self.real + other.real,
            self.imaginary + other.imaginary
        )

    def __mul__(self, other):
        real = self.real * other.real - self.imaginary * other.imaginary
        imag = self.real * other.imaginary + self.imaginary * other.real
        return ComplexNumber(real, imag)

    def __sub__(self, other):
        return ComplexNumber(
            self.real - other.real,
            self.imaginary - other.imaginary
        )

    def __truediv__(self, other):
        real_numerator = self.real * other.real + self.imaginary * other.imaginary
        imag_numerator = self.imaginary * other.real - self.real * other.imaginary

        denominator = other.real * other.real + other.imaginary * other.imaginary
        return ComplexNumber(
            real_numerator / denominator,
            imag_numerator / denominator
        )

    def __abs__(self):
        return (self.real * self.real + self.imaginary * self.imaginary) ** 0.5

    def __eq__(self, other):
        return self.real == other.real and self.imaginary == other.imaginary

    def conjugate(self):
        return ComplexNumber(self.real, -self.imaginary)

    def exp(self):
        """\
        Exponent of a complex number can be expressed as
        `exp(a + i * b) = exp(a) * exp(i * b)`,
        and the last term is given by Euler's formula `exp(i * b) = cos(b) + i * sin(b)`.
        """
        return ComplexNumber(
            e ** self.real * cos(self.imaginary),
            e ** self.real * sin(self.imaginary)
        )
