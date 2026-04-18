import csv

studenti = []

with open('rezultati.csv', mode='r', encoding='utf-8') as fajl:
    reader = csv.reader(fajl)
    for red in reader:
        ime = red[0]
        prezime = red[1]
        bodovi = int(red[2])
        studenti.append((ime, prezime, bodovi))

studenti.sort(key=lambda x: x[1])

statistika_ocjena = {
    "Nedovoljan": 0,
    "Dovoljan": 0,
    "Dobar": 0,
    "Vrlodobar": 0,
    "Izvrstan": 0
}

for ime, prezime, bodovi in studenti:
    if bodovi <= 49:
        statistika_ocjena["Nedovoljan"] += 1
    elif bodovi <= 65:
        statistika_ocjena["Dovoljan"] += 1
    elif bodovi <= 80:
        statistika_ocjena["Dobar"] += 1
    elif bodovi <= 90:
        statistika_ocjena["Vrlodobar"] += 1
    else:
        statistika_ocjena["Izvrstan"] += 1

print(studenti)
print(statistika_ocjena)