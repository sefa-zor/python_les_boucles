
#job1
# Parcourir les nombres de 0 à 20 et les afficher
for nombre in range(21):  # range(21) génère les nombres de 0 à 20
    print(nombre)
print(*range(21))

#job2

i=0
while i<21:
    if i%2==0:
        print(i)
    i=i+1

#job 3

for i in range(1,21):
    carré = i**2
    print(carré)

#job 4

# Demande à l'utilisateur d'entrer un entier supérieur à 0
N = int(input("Entrez un entier supérieur à zéro : "))

# Vérifie si N est supérieur à zéro
if N > 0:
    # Parcourt les tables de multiplication de 1 à N
    for i in range(1, N + 1):
        print(f"\nTable de multiplication de {i}:")
        for j in range(1, 11):
            print(f"{i} x {j} = {i * j}")
else:
    print("Veuillez entrer un entier supérieur à zéro.")

#job 5

N=1
while N<14:
    print(N)
    N = N+1

#job 6

N = int(input("Entrez un entier : "))
compteur = 1

while compteur <= 10:
    resultat = N * compteur * 7
    print(f"{N} * {compteur} * 7 = {resultat}")
    compteur += 1


#job 7

res_de_tour = 1
t=1
while t <=12:
    print(f"Tour {t}: {res_de_tour}")
    res_de_tour += 3
    t += 1



#job 7

res_de_tour = 2
t=1
while t <=12:
    print(f"Tour {t}: {res_de_tour}")
    res_de_tour += 2
    t += 1


#job 9

for i in range(1, 31):
    if i%2==0:
        print(f"{i} est pair.")
    else:
        print(f"{i} est impair.")
        # Demande à l'utilisateur d'entrer un entier supérieur à 0

N = int(input("Entrez un entier supérieur à zéro : "))

# Vérifie si N est supérieur à zéro
if N > 0:
    # Parcourt les tables de multiplication de 1 à N
    for i in range(1, N + 1):
        print(f"\nTable de multiplication de {i}:")
        for j in range(1, 11):
            print(f"{i} x {j} = {i * j}")
            
else:
    print("Veuillez entrer un entier supérieur à zéro.")
N+=1
