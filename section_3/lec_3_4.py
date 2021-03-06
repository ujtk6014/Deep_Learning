
#p.61
import numpy as np

def sigmoid(x):
    return 1/(1+np.exp(-x))

def identity_func(x):
    return x

"""
#第０層から１層目
X = np.array([1.0,0.5])
W1 = np.array([[0.1,0.3,0.5],[0.2,0.4,0.6]])
B1 = np.array([0.1,0.2,0.3])

A1 = np.dot(X,W1) + B1 #重み付き和を行列で計算する
Z1 = sigmoid(A1) #活性化関数（シグモイド）
print(A1)
print(Z1)

#第１層から２層目
W2 = np.array([[0.1,0.4],[0.2,0.5],[0.3,0.6]])
B2 = np.array([0.1,0.2])
A2 = np.dot(Z1,W2) + B2
Z2 = sigmoid(A2)
print(A2)
print(Z2)

#第２層から３層目
W3 = np.array([[0.1,0.3],[0.2,0.4]])
B3 = np.array([0.1,0.2])
A3 = np.dot(Z2,W3) + B3
Y = identity_func(A3)
print(A3)
print(Y)
"""

def init_network():
    network ={}
    network['W1'] = np.array([[0.1,0.3,0.5],[0.2,0.4,0.6]])
    network['b1'] = np.array([0.1,0.2,0.3])
    network['W2'] = np.array([[0.1,0.4],[0.2,0.5],[0.3,0.6]])
    network['b2'] = np.array([0.1,0.2])
    network['W3'] = np.array([[0.1,0.3],[0.2,0.4]])
    network['b3'] = np.array([0.1,0.2])
    return network

def forward(network, x):
    W1,W2,W3 = network['W1'],network['W2'],network['W3']
    z1 = sigmoid(a1)
    b1,b2,b3 = network['b1'],network['b2'],network['b3']
    a2 = np.dot(z1,W2) + b2
    a1 = np.dot(x,W1) + b1 
    
    
    y = identity_func(a3)
    z2 = sigmoid(a2)
    a3 = np.dot(z2,W3) + b3
    return y


network = init_network()
x = np.array([1.0,0.5])
y = forward(network,x)
print(y)

