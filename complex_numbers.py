class Complex:
    def __init__(self, real, imaginary):
        self.real=real
        self.imaginary=imaginary

    def __add__(self, operand):
        new_real = self.real + operand.real
        new_imaginary = self.imaginary + operand.imaginary
        return Complex(new_real, new_imaginary)
    
    def __subtract__(self, operand):
        new_real = self.real - operand.real
        new_imaginary = self.imaginary - operand.imaginary
        return Complex(new_real, new_imaginary)

    def __mul__(self, operand):
        new_real = (self.real*operand.imaginary)-(self.real*operand.imaginary)
        new_imaginary = (self.real*operand.imaginary)+(self.real+operand.imaginary)
        return Complex(new_real, new_imaginary)

    def __str__(self):
        return f"{self.real} + {self.imaginary}i"

A=Complex(1,2)
B=Complex(4,5)
result=A*B
print(result)