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
        num_real = self.real * other.real + self.imaginary * other.imaginary
        num_img = self.imaginary * other.real - self.real * other.imaginary

        denom = other.real * other.real + other.imaginary * other.imaginary
        return ComplexNumber(
            num_real / denom,
            num_img / denom
        )

    def __abs__(self):
        return (self.real * self.real + self.imaginary * self.imaginary) ** 0.5

    def __eq__(self, other):
        return self.real == other.real and self.imaginary == other.imaginary

    def conjugate(self):
        return ComplexNumber(self.real, -self.imaginary)

    def exp(self):
        return ComplexNumber(
            e ** self.real * cos(self.imaginary),
            e ** self.real * sin(self.imaginary)
        )
