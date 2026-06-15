#Napisati rekurzivnu funkciju koja kao parametar prima string,
#a kao rezultat taj string ispisuje sa zada.

def obrni(s):
    if s=="":
        return ""

    else:
        return s[-1] + obrni(s[:-1])

tekst = input()
print(obrni(tekst))