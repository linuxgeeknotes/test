import math
print("Area of Triangle")
a = float(input('Enter first side: '))
b = float(input('Enter first side: '))
c = float(input('Enter first side: '))

s=(a+b+c)/2
print(s)
print('Area of the triangle is {}'.format((s*(s-a)*(s-b)*(s-c)) ** 0.5))
print('Area of the triangle is {}'.format(math.sqrt((s*(s-a)*(s-b)*(s-c)))))