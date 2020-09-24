import numpy as np
from mnist import load_mnist


def mean_squared_error(y,t):
    return 0.5*np.sum(y-t)**2)

def cross_entropy_error(y, t):
    if y.ndim == 1:
        t = t.reshape(1, t.size)
        x = y.reshape(1, y.size)

    batch_size = y.shape[0]   
    delta = 1e-7
    return -np.sum(t*np.log(y + delta))/batch_size

#データの呼び出し
(x_train, t_train),(x_test,t_test) = \
    load_mnist(normalize = False, one_hot_label=True)

#ミニバッチ処理（ランダムに１０個選ぶ）
train_size = x_train.shape[0]
batch_size = 10
batch_mask = np.random.choice(train_size, batch_size)
x_batch = x_train[batch_mask]
t_batch = t_train[batch_mask]
