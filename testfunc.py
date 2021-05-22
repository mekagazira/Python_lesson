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

