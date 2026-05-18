import numpy as np

N = 10000 #경사하강법 반복횟수
alpha = 0.0001 #학습률
alt = np.array([1, 2, 3]) #해발고도 리스트
grad = np.array([3, 7, 5]) #경사 리스트(각 x, dy/dx 기울기 o)
fatigue = np.array([1, 4, 9]) #피로도 리스트
v = np.array([3, 38, 15]) #속도 리스트

# 정규화
altnn = np.array([np.mean(alt), np.std(alt)])
gradnn = np.array([np.mean(grad), np.std(grad)])
fatiguenn = np.array([np.mean(fatigue), np.std(fatigue)])
vnn = np.array([np.mean(v), np.std(v)])

altN = (alt - altnn[0]) / altnn[1]
gradN = (grad - gradnn[0]) / gradnn[1]
fatigueN = (fatigue - fatiguenn[0]) / fatiguenn[1]
vN = (v - vnn[0]) / vnn[1]


# 다항함수 회귀
polynomialC = np.random.normal(0, 1, 10)
polynomialV = [altN**2, gradN**2, fatigueN**2, altN*gradN, gradN*fatigueN, fatigueN*altN, altN, gradN, fatigueN, np.ones(len(alt))] #DelCP역할

def polynomial(a, g, f):
    return np.dot(polynomialC, [a*a, g*g, f*f, a*g, g*f, f*a, a, g, f, 1])

for _ in range(N): 
    deviation = np.array([polynomial(altN[i], gradN[i], fatigueN[i]) - vN[i] for i in range(len(alt))])
    DelCL = np.array([np.dot(deviation, polynomialV[i]) for i in range(10)])
    polynomialC -= alpha * DelCL

def test(a, g, f):
    return(polynomial((a - altnn[0])/altnn[1], (g - gradnn[0])/gradnn[1], (f - fatiguenn[0])/fatiguenn[1])*vnn[1] + vnn[0])

print(test(1, 3, 1))


