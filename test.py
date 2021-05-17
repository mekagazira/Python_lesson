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


