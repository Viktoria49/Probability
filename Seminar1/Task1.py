import numpy as np
def combinations(n,k):
    return np.math.factorial(n) / (np.math.factorial(k) * np.math.factorial(n-k))

a_probability = (combinations(13,4) * combinations(39,0)) / combinations(52,4)
b_probability = (combinations(4,1) * combinations(48,3)) / combinations(52,4)
print(f"Вероятность вытащить все четыре крести {a_probability*100:1.2f}%")
print(f"Вероятность вытащить 1 туза в 4 картах {b_probability*100:1.2f}%")

b_probability = (1 - (combinations(48,4)) / combinations(52,4))
print(f"a) Вероятность вытащить все четыре крести {a_probability*100:1.2f}%")
print(f"б) Вероятность вытащить одного и более тузов в 4 картах {b_probability*100:1.2f}%")
