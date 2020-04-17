import random
print("Dobrodošli u Hrvatsku Lutriju")
print("Odabrali ste igru : Eurojackpot")
odabraniBrojevi = []
print("Odaberite 5 brojeva od 1 do 50 :")
for i in range(5):
      broj = int(input())
      if broj > 50 or broj < 1:
          print("Broj mora bit od 1 do 50")
          broj = int(input())
      while broj in odabraniBrojevi:
          print("Taj broj ste već odabrali, molimo odaberite drugi broj")
          broj = int(input())
      odabraniBrojevi.append(broj)
odabraniBrojevi.sort()
odabraniEkstra = []
print("Odaberite dva dodatna broja od 1 do 10 :")
for i in range(2):
      broj = int(input())
      if broj > 10 or broj < 1:
          print("Broj mora bit od 1 do 50")
          broj = int(input())
      while broj in odabraniEkstra:
          print("Taj broj ste već odabrali, molimo odaberite drugi broj")
          broj = int(input())
      odabraniEkstra.append(broj)
odabraniEkstra.sort()
izvuceniBrojevi = [] #lista dobitnih brojeva
ekstraBrojevi = [] #lista ekstra brojeva
br0 = 0 # brojač pogođenih odabranih brojeva
br1 = 0 # brojač pogođenih dodatnih brojeva
for i in range (5):
    izvuceniBroj = random.randint(1,50)#nasumični broj od 1 do 50
      
    while izvuceniBroj in izvuceniBrojevi: #provjera je li broj već izvučen, ako je bira novi broj
        izvuceniBroj = random.randint(1,50)
    if izvuceniBroj in odabraniBrojevi:
        br0 += 1
        
    izvuceniBrojevi.append(izvuceniBroj)#dodaje broj u listu
for i in range (2): # ekstra brojevi 
    izvuceniBroj = random.randint(1,10)#nasumični broj od 1 do 10
      
    while izvuceniBroj in ekstraBrojevi: #provjera je li broj već izvučen, ako je bira novi broj
        izvuceniBroj = random.randint(1,10)
    if izvuceniBroj in odabraniEkstra:
        br1 += 1
        
    ekstraBrojevi.append(izvuceniBroj)#dodaje broj u listu
  
izvuceniBrojevi.sort() # sortiranje liste rastućim redoslijedom radi lakšeg pregleda
ekstraBrojevi.sort()
print("Dobitna kombinacija je: {} . Pogodili ste {}.".format(izvuceniBrojevi,br0))
print("Izvučeni dodatni brojevi su: {} . Pogodili ste {}.".format(ekstraBrojevi,br1))
