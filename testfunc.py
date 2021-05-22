# ユーザ関数
def myfunc1(n):
    print("###### Function Start ######")
    print(n)
    print(id(n))
    n += 3
    print(n)
    print(id(n))
    print("###### Function End ######")

x = 10
print(x)
print(id(x))

myfunc1(x)

print(x)
print(id(x))
############################################################
def myfunc2(n):
    print("###### Function Start ######")
    print(n)
    print(id(n))
    n[0] = 99
    print(n)
    print(id(n))
    print("###### Function End ######")

x = [10, 20]
print(x)
print(id(x))

myfunc2(x)

print(x)
print(id(x))
############################################################
def myfunc1(num1, str1 = "未入力", str2 = "不明"):
    print("年齢は" + str(num1) + "です。", end='')
    print("名前は" + str1 + "です。", end='')
    print("住所は" + str2 + "です。")

myfunc1(17, "saki", "佐賀")
myfunc1(17, "saki")
myfunc1(17)
############################################################
def myfunc2(num1, num2 = 10):
    num2 *= 2
    print(num1 + num2)
myfunc2(1)
myfunc2(2)
############################################################
def myfunc3(str1, list1 = ["a"]):
    list1.append(str1)
    return list1
print(myfunc3("b"))
print(myfunc3("c"))
print(myfunc3("d"))
############################################################
def myfunc4(str1, list1 = None):
    if list1 is None:
        list1 = ["a"]
    list1.append(str1)
    return list1
print(myfunc4("b"))
print(myfunc4("c"))
print(myfunc4("d"))
############################################################
def myfunc5(str1, str2):
    print("str1=" + str1)
    print("str2=" + str2)

myfunc5(str1="aaa", str2="bbb")
myfunc5(str2="bbb", str1="aaa")
############################################################
def myfunc6(num1, *tupple1):
    print(tupple1)

myfunc6(10)
myfunc6(10, "aaa")
myfunc6(10, "aaa", "bbb")
myfunc6(10, "aaa", "bbb", "ccc")
myfunc6(10, "aaa", "bbb", "ccc", 123)
myfunc6(10, "aaa", "bbb", "ccc", 123, "ddd")