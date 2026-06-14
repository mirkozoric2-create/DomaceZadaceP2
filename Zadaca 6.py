'''Napraviti generator funkcije za ispis svih parnih i svih neparnih brojeva manjih od prosljeđenog parametra.
'''
def parni_neparni(n):
    for i in range(n):
        if i % 2 == 0:
            yield f"Parni broj: {i}"
        else:
            yield f"Neparni broj: {i}" 
broj = int(input("Unesite broj: "))
for rezultat in parni_neparni(broj):
    print(rezultat)
    
