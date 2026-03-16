#napisati program koji generira kvadratnu matricu dimenzija 7x7
#elementi su nasumicni brojevi  od1 do 9
#zatim napisati program koji  racuna zbroj elemenata na rubovima matrice

import random 

n = 7
matrica = []
for i in range(n):
    red = []
    for j in range (n):
         red.append(random.randit(1, 9))
    matrica.append(red)
    
for red in matrica:
  print(red)

  zbroj_rubova = 0

  for i in range (n):
    for j in range(n):
       if i == 0 or i == n-1 or j == n-1:
          zbroj_rubova += matrica [i][j]

  print ("zbroj rubova matrice:", zbroj_rubova)
  