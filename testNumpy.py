import time
import numpy as np

if __name__ == '__main__':

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
