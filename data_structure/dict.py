#辞書の作成
d = {"x":1,"y":2}
print("d is",type(d))
print(d)

d2 = dict(x=10,y=20)
print("d2 is",type(d2))
print(d2)

d3 = {"x":"hello","y":"world"}
print("d3 is",type(d3))
print(d3)

#辞書の書き換え、追加
d = {"x":1,"y":2}

d["x"] = 11
print(d)

d["y"] = "yyy"
print(d)

d["z"] = 3
print(d)

#辞書のメソッド
d = {"x":1,"y":2}

print(d.keys())
print(d.values())

#辞書のオーバーライド
d = {"x":1,"y":2}
d2 = {"x":10,"z":30}

d.update(d2)
print(d)

#要素の確認
print("#######################")
d = {"x":1,"y":2,"z":3}

print(d["x"])
print(d.get("y"))
print(d)

#keyが辞書に入っているか確認
d = {"x":1,"y":2,"z":3}

r = "x" in d
print(r)

r = "a" in d
print(r)

#要素の抜きだし、削除
d = {"x":1,"y":2,"z":3}

d.pop("x")
print(d)

del d["y"]
print(d)

#辞書のクリア
d = {"x":1,"y":2,"z":3}

d.clear()
print(d)

#辞書の削除
d = {"x":1,"y":2,"z":3}

del d
#print(d)

#辞書のコピー
d = {"x":1,"y":2,"z":3}

d2 =  d.copy()
d2["x"] = 10
print(d)
print(d2)
print("d is",id(d))
print("d2 is",id(d2))