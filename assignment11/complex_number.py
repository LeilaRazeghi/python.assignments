class Complex:
    def __init__(self, real, image):
        self.real=real
        self.image=image

    def show(self):
        print(self.real, "+", "i", self.image)
    
    def sum(self, other):
        real_part = self.real + other.real
        image_part = self.image + other.image
        return Complex(real_part, image_part)
    
    def sub(self, other):
        real_part = self.real - other.real
        image_part = self.image - other.image
        return Complex(real_part, image_part)
    
    def mul(self, other):
        real_part =self.real * other.real - self.image * other.image
        image_part =self.real * other.image + self.image * other.real
        return Complex(real_part, image_part)

a=Complex(5, 8)
a.show()

b=Complex(2, 3)
b.show()

#sum a+b
c= a.sum(b)
c.show()

#substraction
d= a.sub(b)
d.show()

#multiplication
e= a.mul(b)
e.show()