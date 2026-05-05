import numpy as np

N = 10000 #경사하강법 반복횟수
alpha = 0.0001 #학습률
alt = np.array([1, 2, 3]) #해발고도 리스트
grad = np.array([3, 7, 5]) #경사 리스트(각 x, dy/dx 기울기o)
v = np.array([3, 38, 15]) #속도 리스트, 얘네들 싹다 손으로 작성...?
exponentialC = np.random.normal(0, 1, 8)

def exponential(a, g):
    return np.dot(exponentialC[0:3],[a, g, 1])*np.exp(exponentialC[3]*a)\
    + np.dot(exponentialC[4:7],[a, g, 1])*np.exp(exponentialC[7]*g)

print(exponential(1,3))