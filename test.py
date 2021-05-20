print("hello world")

# raw文字列
print(r"フォルダは C:\Users\Public です")

# 文字列連結
str1 = "Hello,"
str2 = "Python"
print(str1 + str2)

# 繰り返し
print(str2 * 3)

# 文字数（バイト数ではなく文字数）
print(len(str1 + str2))

# 文字列の指定したインデックスの文字(要素)を取得
print(str1[0])
print(str1[1])
print(str1[2])
print(str1[3])
print(str1[4])
print(str1[5])

# スライス機能　文字列[開始インデックス:終了インデックス]
print(str1[2:5])
print(str1[:3])
print(str1[2:])
print(str1[:])

# joinメソッド
print("と".join(["Apple", "Orange", "Lemon"]))

# 小文字へ変換（全角文字も対応可）
print("Hello".lower())
print("Ｈｅｌｌｏ".lower())

# 大文字へ変換（全角文字も対応可）
print("Hello".upper())
print("Ｈｅｌｌｏ".upper())

# 文字列の先頭を大文字に変換
print("hello python".capitalize())
print("ｈｅｌｌｏ ｐｙｔｈｏｎ".capitalize())

# 単語毎に最初の文字を大文字に変換
print("hello python".title())
print("ｈｅｌｌｏ ｐｙｔｈｏｎ".title())

# 大文字を小文字に、小文字を大文字に変換
print("HelLo Python".swapcase())
print("ＨｅｌＬｏ Ｐｙｔｈｏｎ".swapcase())

# 文字列中の大文字と小文字の区別のある文字が 1 文字以上あり、そのすべてが小文字の場合に真を返す
print("python".islower())
print("pyThon".islower())
print("ｐｙｔｈｏｎ".islower())
print("Ｐｙｔｈｏｎ".islower())

# 文字列中の大文字と小文字の区別のある文字が 1 文字以上あり、そのすべてが大文字の場合に真を返す
print("PYTHON".isupper())
print("pyThon".isupper())
print("ＰＹＴＨＯＮ".isupper())
print("Ｐｙｔｈｏｎ".isupper())

# 文字列中のすべての文字が10進数で使われる文字で、かつ 1 文字以上ある場合に真を返す
print("1234567890".isdecimal())
print("１２３４５６７８９０".isdecimal())
print("12345あ67890".isdecimal())
print("１２３４５あ６７８９０".isdecimal())

# 文字列中のすべての文字が数で使われる文字で、かつ 1 文字以上ある場合に真を返す
print("1234".isnumeric())
print("12aaaa4".isnumeric())
print("3.14".isnumeric())
print("-1234".isnumeric())
print("4,321".isnumeric())
print("１２３４".isnumeric())
print("七五三".isnumeric())
print("".isnumeric())

# すべての文字が ASCII 文字の場合、または空文字の場合に真を返す
print("python".isascii())
print("1234567890".isascii())
print("あいうえお".isascii())
print("".isascii())

# すべての文字が英字で、かつ 1 文字以上ある場合に真を返す
print("python".isalpha())
print("python１２３".isalpha())
# アルファベットには、全角の文字も含まれる。ただし全角の文字であっても数字を表す文字は偽となる(漢数字は真となります)
print("あいうえお".isalpha())
print("ＰＹＴＨＯＮ".isalpha())
print("１２３".isalpha())
print("七五三".isalpha())
print("".isalpha())

# すべての文字が英数字で使われる文字で、かつ 1 文字以上ある場合に真を返す
print("python123".isalnum())
print("あいうえお".isalnum())
print("ＰＹＴＨＯＮ１２３".isalnum())
print("".isalnum())


# 指定した文字列が最初に現れるインデックスを取得する
print("python".find("py"))
print("python".find("y"))
print("python".find("aaa"))
# find メソッドでは 2 番目と 3 番目の引数を指定することで、指定した文字列を探す範囲を指定することが出来る
print("Good School".find("oo"))
print("Good School".find("oo", 3, 10))
print("Good School".find("oo", 3))

# index メソッドは、引数に指定した文字列が見つからなかった場合に -1 ではなく ValueError エラーを返す
print("python".index("py"))
print("python".index("y"))
#print("python".index("aaa"))

# 文字列の中で指定した文字列が最後に現れるインデックスを取得する
print("dictionary".rfind("io"))
print("Good School".rfind("oo"))
print("Orange".rfind("aa"))
# rfind メソッドでは 2 番目と 3 番目の引数を指定することで、指定した文字列を探す範囲を指定することが出来る
print("Good School".rfind("oo"))
print("Good School".rfind("oo", 3, 10))
print("Good School".rfind("oo", 3))

# rindex メソッドは 、引数に指定した文字列が見つからなかった場合に -1 ではなく ValueError エラーを返す
print("dictionary".rindex("io"))
print("Good School".rindex("oo"))
print("Good School".rindex("oo", 0, 6))
#print("Orange".rindex("aa"))

# 文字列の中で指定した文字列が重複せずに何回現れるのかを取得する
print("dictionary".count("io"))
print("Good School".count("oo"))
#  "Goooood" の中で "oo" という文字列は 4 回現れますが、重複せずに現れる回数は 2 回のため count メソッドは 2 を返す
print("Goooood".count("oo"))
print("Good School".count("oo", 3, 10))
print("Good School".count("oo", 3))

# 指定した区切り文字で分割しリストとして取得する
print("My First Album".split())
print("  Next  Page  ".split())
print("Apple\tOrange\tLemon".split())
print("Orange,Lemon,Apple".split(","))

# 文字列の先頭および末尾から指定した文字を取り除いた新しい文字列を返す
print("  Hello ".strip())
print("...Hello...".strip("."))

# 文字列の末尾から指定した文字を取り除いた新しい文字列を返す
print("...Hello...".rstrip("."))

# 文字列の先頭から指定した文字を取り除いた新しい文字列を返す
print("...Hello...".lstrip("."))

# 文字列を指定した長さにして左寄せ/中央揃え/右寄せ
print("[" + "Apple".ljust(8) + "]")
print("[" + "Apple".center(8) + "]")
print("[" + "Apple".rjust(8) + "]")


r = range(10)
print(r)
print(list(r))

r = range(0, 100, 3)
print(r)
print(list(r))
print(list(r[3:10]))

postcode = "125-0062"
if postcode == "140-0015":
    address = "東京都品川区西大井"
elif postcode == "102-0072":
    address = "東京都千代田区飯田橋"
elif postcode == "125-0062":
    address = "東京都葛飾区青戸"
else:
    address = "不明"
print("住所は " + address + " です。")


num = 1
print("Start")
while num < 6:
    print("num = " + str(num))
    num += 1
print("End")


num = 1
total = 0
print("start")
while num < 6:
    print("num = " + str(num))
    total += num
    num += 1
else:
    print("Total = " + str(total))
print("end")


num = 1
while True:
    print("num = " + str(num))
    num *= 2
    if num > 10:
        print("last num = " + str(num))
        break
print("While End")

mylist = ["Orange", "Peach", "Lemon"]
for val in mylist:
    print(val)

mydict = {"L":"Lemon", "O":"Orage", "G":"Grapes"}

# キーの一覧を取得
for mykey in mydict.keys():
    print(mykey)

# すべての値の一覧を取得
for myvalue in mydict.values():
    print(myvalue)

# キーと値の組み合わせの一覧を取得
for mykey, myvalue in mydict.items():
    print("key:" + mykey + ", value:" + myvalue)


for num in [35, 25, "OK", 45, "Pass", 28, "", "aaa", 1234]:
    if isinstance(num, str):
        continue
    print("num = " + str(num))
    total += num