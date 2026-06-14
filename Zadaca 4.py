'''Potrebno napisati regex koji vraca podudaranje ukoliko se unese string koji počinje kao prvo slovo vašeg imena, 
a završava kao prvo slovo prezimena. String mora sadržavati bar jedan broj između 0 i 5 i razmak.'''
import re
def provjeri_string(string):
    pattern = r'^[A-Za-z].*[0-5].* [A-Za-z]$'
    if re.match(pattern, string):
        return "Podudaranje pronađeno!"
    else:
        return "Podudaranje nije pronađeno."
    

input_string = input("Unesite string: ")
result = provjeri_string(input_string)
print(result)
