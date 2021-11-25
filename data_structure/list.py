#リストの作成
l = [1,2,3,4,5,6,7,8]

#リストを表示する
print(l)

#種類を確認するとリストと返ってくる
print(type(l))

#リストにいくつ値が入っているのか
print(len(l))

#リストの一部を取得する
print(l[0])
print(l[-1])
print(l[1:3])
print(l[:6])

#リストの中身を飛ばして取得する
print(l[::2])

#リストの書き換え
l = ["a","s","d","f"]
l[1] = "b"
print(l[1])
print(l)

#リストの複数数の書き換え
l[2:4] = ["c","d"]
print(l)

#リストの中身を空する
l[1:3] = []
print(l)

#リストに追加するメソッド1
n = [1,2,3,4,5]
print(n)
n.append(6)
print(n)

#リストに追加するメソッド2
n.insert(0,0)
print(n)

#リストから取り除くメソッド
print(n)
n.pop()
print(n)
n.pop(0)
print(n)

#リストの削除
n = [1,2,3,4,5]
del n[0]
print(n)

#リストの自体の削除を行ったため、printしてもnが定義されていないとでる。
del n
#print(n)

#値に一致するものを削除する
n = [1,2,3,4,5]
##3番目の位置にある値ではなく、3の値を取り除く
n.remove(3)
print()

#リストの結合
l1 = [1,2,3]
l2 = [10,20,30]

l3 = l1 + l2
print(l3)

l1 += l2
print(l1)

l1.extend(l3)
print(l1)

#値がどこの位置に入っているかを確認するメソッド
l = [1,2,3,4,5,4,3,2,1]

print(l.index(3))
##3を-3番目以降から探している
print(l.index(3,-3))

#値の個数をカウント
print(l.count(6))

#リストのソート
print(l)
l.sort()
print(l)

#ソート&リバース
l.sort(reverse=True)
print(l)

#リストのリバース
n = [1,2,3,4,5]
print(n)
n.reverse()
print(n)

#スプリット
x = "I have a pen"
to_split = x.split(" ")
print(to_split)
##スプリットをもとに戻す
y = " ".join(to_split)
print(y)

#ネスト作成
l1 = [1,2,3]
l2 = [10,20,30]

x = [l1,l2]
print(x)

#ネストの取り出し方
print(x[0])
print(x[0][1])