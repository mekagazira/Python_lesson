# NumPyは、C/C++とFORTRANで実装された多次元配列オブジェクトのndarrayと、それに対する操作関数を提供するもの
import time
import numpy as np

if __name__ == '__main__':


    # Numpyの速度比較

    # NumPyの配列処理
    start_time = time.time()
    np.arange(100000)+1
    end_time = time.time() - start_time
    print ("time:{0}".format(end_time) + "[sec]")

    # Pythonのリスト処理
    start_time = time.time()
    for i in range(0,100000):
        i+1
    end_time = time.time() - start_time
    print ("time:{0}".format(end_time) + "[sec]")

    ################################################################

    a = np.array([1, 2, 3, 4, 5])
    b = 2

    # 配列と数値の足し算
    print(a + b)
    # 配列と数値の掛け算
    print(a * b)
    # 配列の各要素の2乗
    print(a ** b)


    # 0から8までの連番の配列を生成
    a = np.arange(9)
    print(a)
    # 3行3列の2次元配列に変更
    a = a.reshape(3, 3)
    print(a)

    # 1次元配列作成
    b = np.arange(2, 7, 2)
    print(b)

    # 配列の要素毎の足し算
    print(a + b)

    ################################################################

    # 乱数を固定するためSeedを設定
   # np.random.seed(0)

    # 0から100の間のランダムな整数を9個要素に持つ1次元配列を生成
    a = np.random.randint(0, 1000, 9)
    print(a)
    # 最大値
    print(a.max())
    # ランダムに3つの要素をチョイス
    print(np.random.choice(a, 3))

    # 3行3列の2次元配列に変更
    b = a.reshape(3, 3)
    print(b)

    # 逆行列を計算
    c = np.linalg.inv(b)
    print(np.linalg.inv(b))

    # 行列の積を求める ※単位行列になっているか確認する
    d =np.dot(b, c)
    print(d)
    # 小数点第2位を四捨五入する
    print(np.round(d, decimals=1))


