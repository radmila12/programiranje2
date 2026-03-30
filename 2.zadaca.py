import random

studenti = ["Ivan", "Marija", "Ana", "Petar", "Marko", "Iva", "Luka", "Elena"]
ocjene_studenata = {s: random.randint(1, 5) for s in studenti}

print("Ocjene:", ocjene_studenata)

brojac = {}
prolaz = 0

for ocjena in ocjene_studenata.values():
    brojac[ocjena] = brojac.get(ocjena, 0) + 1
    if ocjena > 1:
        prolaz += 1

print("Broj ocjena:", brojac)
print("Postotak prolaznosti:", (prolaz / len(studenti)) * 100, "%")