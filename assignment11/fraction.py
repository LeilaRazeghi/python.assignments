import math

class Fraction:
    def __init__(self, nn, dd):
        #properties
        self.numerator = nn
        self.denumerator = dd
      
    #methods
    def sum(self, f2):
        result_n=self.numerator * f2.denumerator + self.denumerator * f2.numerator
        result_d=self.denumerator * f2.denumerator
        x=Fraction(result_n, result_d)
        return x

    def mul(self, f2):
       result_n = self.numerator * f2.numerator
       result_d = self.denumerator * f2.denumerator
       x=Fraction(result_n, result_d)
       return x

    def sub(self, f2):
        result_n=self.numerator * f2.denumerator - self.denumerator *f2.numerator
        result_d=self.denumerator * f2.denumerator
        x= Fraction(result_n, result_d)
        return x

    def div(self, f2):
        result_n =self.numerator * f2.denumerator
        result_d =self.denumerator * f2.numerator
        x=Fraction(result_n, result_d)
        return x
    
    def fraction_to_number(self):
        result = self.numerator / self.denumerator
        return result

    def simplify(self):
        gcd= math.gcd(self.numerator, self.denumerator)
        result_n = self.numerator / gcd
        result_d = self.denumerator / gcd
        result= Fraction(result_n, result_d)
        return result
    
    def show(self):
      print(self.numerator, "/", self.denumerator)

a=Fraction(2, 3)
a.show()

b=Fraction(7, 1)
b.show()

#multiply(a*b)
z= a.mul(b)
z.show()

#sum(a+b)
w=a.sum(b)
w.show()

#substract(a-b)
y=a.sub(b)
y.show()

#divide(a/b)
s= a. div(b)
s.show()

#fraction_to_number
number=a.fraction_to_number()
print(number)

#simplifying
simpled = a.simplify()
simpled.show()