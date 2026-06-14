'''Napisati rekurzivnu funkciju koja kao parametar prima string, a kao rezultat taj string ispisuje sa zada.'''
def zadace(string):
    if len(string) == 0:
        return
    else:
        print(string[0])
        zadace(string[1:])
string = input("Unesite string: ")
zadace(string)
