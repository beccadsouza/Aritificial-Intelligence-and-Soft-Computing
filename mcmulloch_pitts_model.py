from numpy import *


def tanh_der(x): 
    return 1.0 - tanh(x) ** 2

def fwd_prop(i):
    global wt
    return tanh(dot(i, wt))

def train(train_ip, train_op, train_iterations):
    global wt
    for iteration in range(train_iterations):
        temp_op = fwd_prop(train_ip)
        temp_err = train_op - temp_op
        temp_adj = dot(train_ip.T, temp_err*tanh_der(temp_op))
        wt = wt + temp_adj


ip = array([[0,0,0], [0,0,1], [0,1,0], [0,1,1], [1,0,0], [1,0,1]])
op = array([[0, 1, 1, 1, 1, 1]]).T
wt = 2 * random.random((3, 1)) - 1

print(wt)
train(ip, op, 1000)
print(wt)

