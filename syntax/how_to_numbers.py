import math
from decimal import *

#整数
a = 10
b = 0
c = -1

ans = a + b + c
print(ans)

#浮動小数点
a = 0.1
b = 23.345
c = -49.3

ans = a + b + c
print(ans)

#整数と浮動小数点の計算
a = 10
b = -49.3
ans = a + b
print(ans)

a = 0.9
b = 0.1
ans = a + b
print(ans)

a = 100
b = 0.1
ans = a * b
print(ans)

#round
n = 3.1415926535

print(round(n))
print(round(n,2))

#Decimal
num = 2.675

num = Decimal("2.675")
print(type(num))
print(round(num, 2))

num = Decimal(2.675)
print(type(num))
print(round(num, 2))

num = 2.675
print(type(num))
print(round(num, 2))

#ceil floor
n = 3.1415926535
n2 = -3.1415926535

print(math.ceil(n))
print(math.floor(n))

print(math.ceil(n2))
print(math.floor(n2))