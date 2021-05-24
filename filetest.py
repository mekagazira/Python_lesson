# デフォルトエンコーディングを調べる
import locale
print(locale.getpreferredencoding())

f = open('output.txt', 'r')
data = f.read()
print(data)
f.close()

# ファイルが自動的にクローズされる。
with open("output.txt" , "w") as f:
    f.write("hi!  from python\n")
    f.write("hi!! from python\n")

with open("output.txt" , "r") as f:
    print(f.read())


mylist = []
with open("output.txt" , "r") as f:
    mylist = f.readlines()

print(mylist)