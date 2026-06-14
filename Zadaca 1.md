Napisati program koji generira kvadratnu matricu dimenzija 7x7.
Elementi su nasumični brojevi od 1 do 9.
Zatim napisati program koji računa zbroj elemenata na rubovima matrice.


import random


matrica = [[random.randint(1, 9) for _ in range(7)] for _ in range(7)]

for red in matrica:
    print(red)


zbroj_rubova = 0


zbroj_rubova += sum(matrica[0])
zbroj_rubova += sum(matrica[6])


for i in range(1, 6):
    zbroj_rubova += matrica[i][0]
    zbroj_rubova += matrica[i][6]

print("Zbroj elemenata na rubovima matrice:", zbroj_rubova)
