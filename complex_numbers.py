class Complex:
    """
    A class to perform mathematical operations on complex numbers.
    """
    def __init__(self, real: float, imag: float):
        self.r = real
        self.im = imag

    @property
    def conjugate(self):
        """This returns the conjugate of the complex number (e.g a + bj -> a - bj).
        :returns: Complex"""
        return Complex(self.r, -self.im)

    def __repr__(self):
        if self.im !=0:
            return f"<Complex `{round(self.r, 4)} {'+' if self.im>0 else '-'} {abs(round(self.im,4))}j`>"
        return f"<Complex `{round(self.r, 4)}`>"

    def __add__(self, other):
        # (a + bj) + (x + yj)
        x = self.r + other.r
        y = self.im + other.im
        return Complex(x, y)

    def __mul__(self, other):
        # (a + bj)(x + yj)
        x = (self.r * other.r) - (self.im * other.im)
        y = (self.r * other.im) + (self.im * other.r)
        return Complex(x, y)

    def __sub__(self, other):
        # (a + bj) - (x + yj)
        x = self.r - other.r
        y = self.im - other.im
        return Complex(x, y)

    def __truediv__(self, other):
        # (a + bj) / (x + yj)
        num = self.__mul__(other.conjugate)
        den = other.__mul__(other.conjugate)
        den = den.r if den.im == 0 else 0
        return Complex(num.r/den, num.im/den)
