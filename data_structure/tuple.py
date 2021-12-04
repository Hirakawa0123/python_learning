#タプルの作成
t = (1,2,3,4,5)

print("t is",type(t))
print(t)

t1 = (1,)
t2 = 1,

print("t1 is",type(t1))
print(t1)
print("t2 is",type(t2))
print(t2)

#タプルの確認
print(t[0])
#t[0] = 10

#タプルのスライス
print(t[1:4])

#タプル結合
t = (1,2,3) + (4,5,6)
print(t)

#タプルのアンパック
t = (1,2,3)

x,y,z = t
print(x,y,z)
print("x is",type(x))

#タプルを使った入れ替え
a = 1
b = 2
a,b = b,a
print(a,b)

a = 1
b = 2

print("a is",type(a))
print("b is",type(b))
#b,aとすることでタプルにしている
n = b,a
print("n is",type(n))
a,b = n
print(a,b)