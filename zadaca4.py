#Potrebno napisati regex koji vraca podudaranje ukoliko
#se unese string koji počinje kao prvo slovo vašeg imena,
#a završava kao prvo slovo prezimena. String mora sadržavati bar
#jedan broj između 0 i 5 i razmak.

import re

tekst=input()

if re.search("^N.*[0-5].*J$",tekst):
    print("Podudaranje")
else:
    print("Nema podudaranja")