# В университет на факультеты A и B поступило равное количество студентов,
# а на факультет C студентов поступило столько же, сколько на A и B вместе.
# Вероятность того, что студент факультета A сдаст первую сессию, равна 0.8.
# Для студента факультета B эта вероятность равна 0.7, а для студента факультета C - 0.9.
# Студент сдал первую сессию. Какова вероятность, что он учится: a). на факультете A
# б). на факультете B в). на факультете C?

def bayes(pba1, pa1, pba2, pa2, pba3, pa3):
    pb = pba1*pa1+pba2*pa2+pba3*pa3
    list = []
    list.append(pba1*pa1/pb)
    list.append(pba2*pa2/pb)
    list.append(pba3*pa3/pb)
    return list
    
pa1 = 1/4 # вероятность быть студентом факультета А
pa2 = 1/4 # вероятность быть студентом факультета B
pa3 = 1/2 # вероятность быть студентом факультета C
pba1 = 0.8 # вероятность сдать сессию студенту факультета А
pba2 = 0.7 # вероятность сдать сессию студенту факультета В
pba3 = 0.9 # вероятность сдать сессию студенту факультета С

result = bayes(pba1, pa1, pba2, pa2, pba3, pa3)

print(f"1. Вероятность, что студент с факультета А {result[0]} или {result[0]*100:0.2f}%")
print(f"2. Вероятность, что студент с факультета В {result[1]} или {result[1]*100:0.2f}%")
print(f"3. Вероятность, что студент с факультета С {result[2]} или {result[2]*100:0.2f}%")