class Complex:
    def __init__(self, a,b):
        self.a=a 
        self.b=b

    def __mul__(self, operand):
        new_a = (self.a*operand.a)-(self.b*operand.b)
        new_b = (self.a*operand.b)+(self.b+operand.a)
        return Complex(new_a, new_b)

    def __str__(self):
        return f"{self.a} + {self.b}i"

A=Complex(1,2)
B=Complex(4,5)
result=A*B
print(result)