import re

//  Inicijali: Radmila (R), Milidragović (M)
// Uvjeti: broj [0-5] i razmak (\s)
                                
                                
regex = r'^R(?=.*[0-5])(?=.*\s).*M$'

unos = input("Unesi string: ")

if re.match(regex, unos):
    print("Podudaranje pronađeno.")
else:
    print("Nema podudaranja.")