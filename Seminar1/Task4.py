# В лотерее 100 билетов. Из них 2 выигрышных.
# Какова вероятность того, что 2 приобретенных билета окажутся выигрышными?

import numpy as np
def combinations(n,k):
    return np.math.factorial(n) / (np.math.factorial(k) * np.math.factorial(n-k))
probability = combinations(2,2) * combinations(98,0) / combinations(100,2)
print(f"Вероятность купить два выигрышных билета {probability*100:0.2f}%")
