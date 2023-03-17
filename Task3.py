import numpy as np

print("На соревновании по биатлону один из трех спортсменов стреляет и попадает в мишень.\
Вероятность попадания для первого спортсмена равна 0.9, для второго — 0.8, для третьего — 0.6. \
Найти вероятность того, что выстрел произведен: a). первым спортсменом б). вторым спортсменом в). \
третьим спортсменом.")

def probadility_hit(k, n, p):
    return k / n * p

def probadility_of_each(k, n, p):
    P = result
    return (k / n * p) / P

p1 = probadility_hit(1, 3, 0.9)
p2 = probadility_hit(1, 3, 0.8)
p3 = probadility_hit(1, 3, 0.6)
result = p1 + p2 + p3
print(f"Probability hit: {result:.9f}") 

first_athlete = probadility_of_each(1, 3, 0.9)
print(f"First athlete: {first_athlete:.9f}")

second_athlete = probadility_of_each(1, 3, 0.8)
print(f"Second athlete: {second_athlete:.9f}")

third_athlete = probadility_of_each(1, 3, 0.8)
print(f"Third athlete: {third_athlete:.9f}")
