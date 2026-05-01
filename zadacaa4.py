import random

imena = [
    'Richard', 'Kevin', 'Edward', 'Debbie', 'Adam', 'Norma', 'Christopher', 
    'Karen', 'Tami', 'Michael', 'John', 'Roseanna', 'Gerald', 'George', 
    'Vesta', 'Julie', 'Raymond', 'Janice', 'Susan', 'Kerry', 'Lorenzo', 
    'Holly', 'Dan', 'Sherri', 'William', 'Karey', 'Marion', 'Melissa', 
    'Vincent', 'Ruby'
]

prezimena = [
    'Arnold', 'Simmons', 'Velasco', 'Canada', 'Gibbs', 'Thompson', 'Rendall', 
    'Harris', 'Hendon', 'Lyles', 'Perez', 'Cleary', 'Hoyman', 'Hall', 
    'Baker', 'Fichter', 'Colantuono', 'Moose', 'Howard', 'Davis', 'Nutt', 
    'Cornett', 'Smith', 'Lemus', 'Beltran', 'Ho', 'Cook', 'Samuels', 
    'Rodriguez', 'Cano'
]

radnici = []
for _ in range(15):
    radnik = {
        "ime": random.choice(imena),
        "prezime": random.choice(prezimena),
        "satnica": round(random.uniform(4, 6), 2),
        "tjedni_sati": random.randint(20, 30)
    }
    radnici.append(radnik)
isplate = []
for r in radnici:
    isplata = round(r["satnica"] * r["tjedni_sati"], 2)
    isplate.append((r["ime"], r["prezime"], isplata))
print("Popis svih isplata:")
for i in isplate:
    print(f"{i[0]} {i[1]}: {i[2]} EUR")

print("-" ,30)
ukupno = sum(i[2] for i in isplate)
prosjek = ukupno / len(isplate)

print(f"Ukupna isplata: {round(ukupno, 2)} EUR")
print(f"Prosječna isplata: {round(prosjek, 2)} EUR")

print("-" * 30)
print("Radnici s isplatom iznad prosjeka:")
for i in isplate:
    if i[2] > prosjek:
        print(f"{i[0]} {i[1]} - ({i[2]} EUR)")