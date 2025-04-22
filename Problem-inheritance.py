'''Q1 Class 2-D vector & use to create class represent 3-D vector'''
# class twoDVector:
#     def __init__(self, i, j):
#         self.i = i
#         self.j = j
#     def show(self):
#         print(f"The 2D vector is {self.i}i + {self.j}j")

# class threeDVector(twoDVector):
#     def __init__(self, i, j, k):
#         super().__init__(i, j)
#         self.k = k
#     def show(self):
#         print(f"The 2D vector is {self.i}i + {self.j}j + {self.k}k")
# a= twoDVector(1, 2)
# a.show()
# b= threeDVector(1, 2, 3)
# b.show()

'''Q2 class Animal -> class Pets ->  class Dogs -> method bark in dogs'''
# class Animal:
#     pass
# class Pets(Animal):
#     pass
# class Dogs(Pets):
#     @staticmethod
#     def bark():
#         print("Bow Bow!!")
# d= Dogs()
# d.bark()

'''Q3 class Emplyee and add salary and increment properties to it'''
# class Employee:
#     salary =100
#     increment = 20
#     @property
#     def salary_after_increment(self):  # 1     # salary after increment
#         return (self.salary + self.salary * (self.increment/100))
    
#     @salary_after_increment.setter     # 2     # % salary is incremented 
#     def salary_after_increment(self, salary):
#         self.increment = ((salary/self.salary) -1)*100 

# e= Employee()
# print(e.salary_after_increment)       # 1
# e.salary_after_increment = 120
# print(e.increment)                    # 2

'''Q4 class Complex to represent complex no, along with overloaded operator '+' and '*' which adds and then multiply
Complex nos are eg. 2+3i real and imaginary nos'''
# class Complex:
#     def __init__(self, r, i):
#         self.r = r
#         self.i = i

#     def __add__(self, c2):  
#         return Complex(self.r + c2.r, self.i + c2.i)
    
#     def __mul__(self, c2):
#         real_part = self.r * c2.r - self.i * c2.i
#         imaginary_part = self.r * c2.i + self.i * c2.r
#         return Complex(real_part, imaginary_part)
    
#     def __str__(self):
#         return f"{self.r} + {self.i}i"
    
# c1=Complex(1,2)
# c2=Complex(3,4)
# print(c1+c2)
# print(c1*c2)


'''Q5 class vector representing a vector of n dimensions. Overload the + and * operator which calc the sum and the 
dot(.) product of them '''
# class Vector:
#     def __init__(self ,i ,j ,k):
#         self.i = i
#         self.j = j
#         self.k = k
#     def __add__(self, other):
#         result = Vector(self.i + other.i, self.j + other.j, self.k + other.k)
#         return result
#     def __mul__(self, other):
#         result = self.i * other.i +  self.j * other.j + self.k * other.k
#         return result
#     def __str__(self):
#         return f"Vector ({self.i},{self.j},{self.k})"
# v1 =Vector(1,2,3)
# v2 =Vector(4,5,6)
# v3 =Vector(7,8,9)
# print(v1+v2)
# print(v1*v2)
# print(v1+v3)
# print(v1*v3)

'''Q6 write __str__ as follows 7i+8j+10k'''
# class Vector:
#     def __init__(self ,i ,j ,k):
#         self.i = i
#         self.j = j
#         self.k = k
#     def __str__(self):
#         return f"{self.i}i+{self.j}j+{self.k}k"
# v1 =Vector(7,8,10)
# print(v1)

'''Q7 override __len()__ method on vector of Question 5 to display the dimension of vector'''
class Vector:
    def __init__(self ,l):
        self.l= l

    def __len__(self):
        return len(self.l)
    
v1 =Vector([1,2,3])
print(len(v1))
