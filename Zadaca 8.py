'''Funkciju iz prethodne zadaće učitati kao funkciju modula u novi program i pozvati je nakon traženja unosa od korisnika.
 '''
#Ovo saveat kao prvi fajl i nazvati ga npr.Parni-Neparni_moduil.py
def parni_neparni(n):
    for i in range(n):
        if i % 2 == 0:
            yield f"Parni broj: {i}"
        else:
            yield f"Neparni broj: {i}"
#Ovo saveat kao drugi fajl i nazvati ga npr.Glavni-program.py
from parni_neparni_modul import parni_neparni

def main():
    broj = int(input("Unesite broj: "))
    for rezultat in parni_neparni(broj):
        print(rezultat)

if __name__ == "__main__":
    main()
