# Domaće Zadaće P2 - Matrica i Zbroj Rubova

## Zadatak
Napisati program koji:
1. Generira kvadratnu matricu dimenzija **7x7**
2. Elementi su **nasumični brojevi od 1 do 9**
3. Računa **zbroj elemenata na rubovima matrice**

## Rubovi Matrice
Rubovi su definirani kao:
- **Prvi red** (svi elementi)
- **Zadnji red** (svi elementi)
- **Prvi stupac** (elementi bez uglova - već su brojeni u redovima)
- **Zadnji stupac** (elementi bez uglova - već su brojeni u redovima)

## Rješenja

### Java Rješenje
Datoteka: `MatricaRubovi.java`

Kako pokrenuti:
```bash
javac MatricaRubovi.java
java MatricaRubovi
```

### Python Rješenje
Datoteka: `matrica_rubovi.py`

Kako pokrenuti:
```bash
python matrica_rubovi.py
```

## Primjer Izlaza

```
Matrica 7x7:
5 2 8 3 1 9 4
7 1 6 2 8 3 5
4 9 2 7 1 5 6
3 5 8 1 9 2 7
6 1 4 9 2 8 3
2 7 3 5 6 1 4
9 4 1 8 3 7 2

Zbroj elemenata na rubovima: 130
```

## Objašnjenje Algoritma

Za matricu 7x7, rubovi se računaju na sljedeći način:
- Zbrajam sve elemente prvog reda (7 elemenata)
- Zbrajam sve elemente zadnjeg reda (7 elemenata)
- Zbrajam sve elemente prvog stupca između prvog i zadnjeg reda (5 elemenata)
- Zbrajam sve elemente zadnjeg stupca između prvog i zadnjeg reda (5 elemenata)

**Ukupno:** 7 + 7 + 5 + 5 = 24 elementa na rubovima

Uglovi se brojaju samo jednom (kao dio redova), tako da se ne duplikaju.
