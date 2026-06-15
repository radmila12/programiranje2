
import random

imena = ["Ivan", "Marko", "Ana", "Petar", "Luka", "Iva", "Maja", "Nikola", "Sara", "Karlo"]
prezimena = ["Horvat", "Kovač", "Marić", "Novak", "Babić", "Jurić", "Knežević", "Radić", "Perić", "Božić"]

radnici = []
for  in range(15):
    ime = random.choice(imena)
    prezime = random.choice(prezimena)
    satnica = round(random.uniform(4, 6), 2)
    radnici.append({"ime": ime, "prezime": prezime, "satnica": satnica})

for r in radnici:
    r["tjednisati"] = random.randint(20, 30)

isplate = []
for r in radnici:
    isplata = r["satnica"] * r["tjedni_sati"]
    isplate.append((r["ime"], r["prezime"], isplata))

for i in isplate:
    print(i)

ukupno = sum(i[2] for i in isplate)
prosjek = ukupno / len(isplate)
print("Ukupna isplata:", round(ukupno, 2))
print("Prosječna isplata:", round(prosjek, 2))

print("Radnici s isplatom iznad prosjeka:")
for i in isplate:
    if i[2] > prosjek:
        print(i[0], i[1])
        