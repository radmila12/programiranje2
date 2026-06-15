#Napraviti generator funkcije za ispis svih parnih i
#svih neparnih brojeva manjih od prosljeđenog parametra.

def parni(n):
    for i in range(n):
        if i % 2==0:
            yield i

def neparni(n):
    for i in range(n):
        if i % 2==1:
            yield i

for i in parni(10):
    print(i)

for i in neparni(10):
    print(i)