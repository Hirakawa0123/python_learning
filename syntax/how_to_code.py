#ステートメントの区切りは改行もしくはセミコロン
a = 10; b =20; c = a + b
print(c)

a = 30
b =40
c = a + b
print(c)

##ステートメントの改行
a = 1 + 2 + 3 + 4 + 5 \
    + 6 + 7 + 8 + 9 + 10
print(a)

#コメントアウト
"""
複数行の
コメントアウトの
書き方
"""
a = 1
A = 10
print(a)
print(A)

#値の区切り文字、改行指定
a = 1
b = 2
c = 3
ans = a + b + c

print(a,b,c)
print(ans)

print(a,b,c, sep = "、")
print(ans)

print(a,b,c, sep = "!", end = "end")
print(ans)

#endの使い方
l = ["This","is","a","pen"]

for word in l:
    print(word)

for word in l:
    print(word,end = "\n")

for word in l:
    print(word,end = "")

for word in l:
    print(word,end = " ")

for word in l:
    print(word,end = "\t")