'''Iz podataka učitanih u prethodnom primjeru sortirati listu po prezimenima.

Napraviti novi rječnik gdje će se po bodovnom rangu upisivati broj ostvarenih ocjena. 

Nedovoljan
0-49%

Dovoljan
50-65%

Dobar
65-80%

Vrlodobar
80-90%

Izvrstan
90-100%
'''
import json
with open('studenti.json', 'r') as f:    studenti = json.load(f)

studenti.sort(key=lambda x: x['prezime'])

bodovni_rangovi = {
    'Nedovoljan': 0,
    'Dovoljan': 0,
    'Dobar': 0,
    'Vrlodobar': 0,
    'Izvrstan': 0
}

for student in studenti:
    ocjena = student['ocjena']
    if ocjena < 50:
        bodovni_rangovi['Nedovoljan'] += 1
    elif 50 <= ocjena < 65:
        bodovni_rangovi['Dovoljan'] += 1
    elif 65 <= ocjena < 80:
        bodovni_rangovi['Dobar'] += 1
    elif 80 <= ocjena < 90:
        bodovni_rangovi['Vrlodobar'] += 1
    elif ocjena >= 90:
        bodovni_rangovi['Izvrstan'] += 1

print("Sortirani studenti po prezimenima:")
for student in studenti:
    print(f"{student['ime']} {student['prezime']} - Ocjena: {student['ocjena']}")
print("\nBroj ostvarenih ocjena po bodovnim rangovima:")
for rang, broj in bodovni_rangovi.items():
    print(f"{rang}: {broj}")
