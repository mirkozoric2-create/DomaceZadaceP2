'''Napisati regex za provjeru validnosti unosa e-maila. E-Mail mora biti formata ime.prezime@fpmoz.sum.ba
Nakon toga napisati regex za provjeru eduId koji mora biti formata ime.prezimeX@sum.ba 
X predstavlja bilo koji broj (moze ici u beskonacnost), a taj broj ne mora postojati (može biti samo ime.prezime@sum.ba).
Od korisnika zatražiti unos maila i eduid te ispisati uspješnost.

Istražiti greedy i non-greedy quantifiers.
'''
import re

def provjeri_email(email):
    pattern = r'^[a-zA-Z]+\.[a-zA-Z]+@fpmoz\.sum\.ba$'
    if re.match(pattern, email):
        return "Email je validan!"
    else:
        return "Email nije validan."

def provjeri_eduid(eduid):
    pattern = r'^[a-zA-Z]+\.[a-zA-Z]+[0-9]*@sum\.ba$'
    if re.match(pattern, eduid):
        return "EduId je validan!"
    else:
        return "EduId nije validan."

input_email = input("Unesite email: ")
input_eduid = input("Unesite eduId: ")

result_email = provjeri_email(input_email)
result_eduid = provjeri_eduid(input_eduid)

print(result_email)
print(result_eduid)
