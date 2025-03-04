# number = 17
# numbers = [6,10,12,14, 5,8]
# print(number)
# print(numbers)
# #
# empty_list = []
# print(empty_list)
# empty_list.append(28)
# print(empty_list)
# empty_list.extend([14, 20, 4])
# print(empty_list)
#
# students = ["Ingrida", 'Andzelika', 'Raimundas', 'Edvinas', 'Rolandas']
# aaaaaaaaaaaaaaaaaaaaaaaaaa = [1,100,2,3,4,5,6]
# aaaaaaaaaaaaaaaaaaaaaaaaaa.sort()
# for xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx in aaaaaaaaaaaaaaaaaaaaaaaaaa:
#     print(xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx)
#
# exit(200)
# print(students.sort())
# =======================================================================
# Sukurkite ciklą kuris atspausdintų 10 kartų žodį “labas”.
# for i in range(10):
#     print("Labas")
import random

# Sukurkite ciklą kuris atspausdintų skaičius nuo 0 iki 9.
# for i in range(10):
#     print(i)


# Sukurkite masyvą iš dešimties augalų pavadinimų.
# augalai = ["Rožė", "Tulpė", "Narcizas", "Aguona", "Ramunė", "Lelija", "Jazminas", "Bijūnas", "Klevas", "Ąžuolas"]


# Atspausdinkite kiekvieną 3čio uždavinio augalą atskiroje eilutėje.
# for augalas in augalai:
#     print(augalas)


# Atspausdinkite 3čio uždavinio kiekvieną augalą pradedant nuo paskutinio,
# ir baigiant pirmuoju. (atvirkščias ciklas).

# for augalas in reversed(augalai):
#     print(augalas)

# for augalas in augalai[::-1]:
#     print(augalas)

# Atspausdinkite kas antrą skaičių nuo 10 iki 50 (porinius);
# for i in range(10, 51, 2):
#     print(i)

# Atspausdinkite kas antrą skaičių nuo 10 iki 50. (porinius)
# Jei skaičius dalinasi iš 10 be liekanos jo nespausdinkite.
# ( naudokite continue.) (atspausdinti visus porinus skaičius, išskyrus tuos
# kurie dalinasi iš 10 be liekanos)
#
# for skaicius in range(10, 51, 2):
#     if skaicius % 10 == 0:
#         continue
#     print(skaicius)

# for i in range(10, 51, 2):
#     if i % 10 == 0:
#         continue  # Praleidžia šį ciklo iteracijos žingsnį
#     print(i)


# Sukurkite ciklą kuris suktųsi nuo 0 iki 20.
# Suskaičiuokite, kiek kartų kintamasis i turėjo porinę reikšmę;
# count = 0
# for skaicius in range(21):
#     if skaicius % 2 == 0:
#         count += 1
# print("poriniu skaiciu kiekis", count)



# count = 0  # Kintamasis porinių skaičių skaičiavimui
# for i in range(21):  # Ciklas nuo 0 iki 20
#     if i % 2 == 0:  # Tikriname, ar skaičius porinis
#         count += 1
# print("Porinių skaičių kiekis:", count)

# Suskaičiuokite kiek 3čio uždavinio masyve yra žodžių trumpesnių nei 5 simboliai, ir kiek ilgesnių nei 7 simboliai. (du skaičiavimai)

# augalai = ["Rožė", "Tulpė", "Narcizas", "Aguona", "Ramunė", "Lelija", "Jazminas", "Bijūnas", "Klevas", "Ąžuolas"]


# Trumpi_pavadinimai = 0
# Ilgi_pavadinimai = 0
# for augalas in augalai:
#     Ilgis = len(augalas)
#
#     if Ilgis < 5:
#         Trumpi_pavadinimai += 1
#     if Ilgis > 7:
#         Ilgi_pavadinimai += 1
#
# print("Maziau nei 5_simboliai:", Trumpi_pavadinimai)
# print("Daugiau nei 7 simboliai:", Ilgi_pavadinimai)


# trumpesni_nei_5 = 0
# ilgesni_nei_7 = 0
#
# for augalas in augalai:
#     ilgis = len(augalas)
#     if ilgis < 5:
#         trumpesni_nei_5 += 1
#     if ilgis > 7:
#         ilgesni_nei_7 += 1
#
# print("Žodžių trumpesnių nei 5 simboliai:", trumpesni_nei_5)
# print("Žodžių ilgesnių nei 7 simboliai:", ilgesni_nei_7)

# Paaiškinimas:
# Naudojame len(augalas), kad gautume kiekvieno žodžio ilgį.
# Pirmame if tikriname, ar žodis trumpesnis nei 5 simboliai, ir skaičiuojame tokius žodžius.
# Antrame if tikriname, ar žodis ilgesnis nei 7 simboliai, ir skaičiuojame tokius žodžius.


# Suskaičiuokite kiek 3čio uždavinio masyve yra žodžių ilgesnių nei 5 simboliai bet trumpesnių  nei 10 simboliai. (tarp 5 ir 10 simbolių ilgio)
# augalai = ["Rožė", "Tulpė", "Narcizas", "Aguona", "Ramunė", "Lelija", "Jazminas", "Bijūnas", "Klevas", "Ąžuolas"]
#
# tarp_5_ir_10 = 0
# for augalas in augalai:
#     ilgis = len(augalas)
#     if 5 < ilgis > 10:
#         ilgis += 1
# print("Ilgesni zodziai nei 5 ir trumpesni nei 10:", tarp_5_ir_10)


# tarp_5_ir_10 = 0
#
# for augalas in augalai:
#     ilgis = len(augalas)
#     if 5 < ilgis < 10:
#         tarp_5_ir_10 += 1
#
# print("Žodžių ilgis tarp 5 ir 10 simbolių:", tarp_5_ir_10)
# Paaiškinimas:
# 5 < ilgis < 10 tikrina, ar žodžio ilgis yra tarp 5 ir 10 simbolių.
# Kiekvieną kartą, kai sąlyga pasitvirtina, tarp_5_ir_10 padidėja.


# Sugeneruokite 300 atsitiktinių skaičių nuo 0 iki 300, atspausdinkite juos atskirtus tarpais ir suskaičiuokite kiek tarp jų yra didesnių už 150.  Skaičiai didesni nei 275 turi būti atspausdinti skliausteliuose” [ ] “.

#  random
#
rnd_nums = []
for i in range (0, 300):
    ats_sk = random.randint(0, 300)
    rnd_nums.append(ats_sk)
#
counter = 0
for num in rnd_nums:
    if num > 150:
        print(f"skaicius yra {num}")
        print("skaicius yra " + str(num))
        # print("skaicius yra " + format(num))

        print(f"bla bla {num} blu blu {num} =) ?")
        counter += 1
    if num > 275:
        print(f"[{num}]")
    else:
        print(num)
# print(f"---{counter}---")
# print()
# import random # Sukuriame 300 atsitiktinių skaičių nuo 0 iki 300
# rnd_nums = [] # sukuriame masyva (tuscia reiksmiu sarasas)
# for i in range (0,300): # sukam cikla 300 kartu. "i" - ciclko iteracija nuo 0 iki 300 (paskutine reiksme bus 299)
#     numeriukas = random.randint(0,300)
#     rnd_nums.append(numeriukas)  # Atsitiktinai skaičiai nuo 0 iki 300
# print(rnd_nums)

# Spausdiname visus atsitiktinius skaičius ir suskaičiuojame, kiek yra didesnių už 150
# counter = 0
# for num in rnd_nums:
#     if num > 150:
#         print(f"{num} bingo!!!")
#         counter += 1  # Skaičiuojame skaičius didesnius už 150
#     if num > 275:
#         print(f"[{num}]---------------------") # Skaičiai didesni už 275 spausdinami su skliausteliais
#     else:
#         print(num) # Kiti skaičiai spausdinami be skliaustelių

# Spausdiname, kiek skaičių yra didesnių už 150
# print(f'=========================={counter}=========================')

# Paaiškinimai:
# Atsitiktinių skaičių generavimas: 300 skaičių sukurta naudojant ciklą ir random.randint(0, 301) (skaičiai nuo 0 iki 300).
# Skaičiavimas ir spausdinimas:
# counter: suskaičiuojame, kiek skaičių yra didesnių už 150.
# Sąlyga: jei skaičius didesnis už 275, jis bus atspausdintas su skliausteliais. Kiti skaičiai bus spausdinami be skliaustelių.
# Galutinis rezultatas: spausdinamas bendras skaičių, didesnių už 150, kiekis.



# Vienoje eilutėje atspausdinkite visus skaičius nuo 1 iki 3000, kurie dalijasi iš 77 be liekanos. Skaičius atskirkite kableliais. Po paskutinio skaičiaus kablelio neturi būti.

# Atspausdiname visus skaičius nuo 1 iki 3000, kurie dalijasi iš 77 be liekanos
result = []# "77","154"
for i in range(1, 3001):
    if i % 77 == 0:
        result.append(str(i))  # Pridedame skaičių į sąrašą kaip tekstą
print(", ".join(result))
print(result)
# # Spausdiname visus skaičius atskirtus kableliais

# Paaiškinimas:
# Ciklas: einame per skaičius nuo 1 iki 3000.
# Tikrinimas: naudojame sąlygą i % 77 == 0, kad patikrintume, ar skaičius dalijasi iš 77 be liekanos.
# Kableliai: naudojame ", ".join(result) tam, kad atspausdintume skaičius atskirtus kableliais, bet po paskutinio skaičiaus kablelio nėra.
# Tai duos norimą rezultatą su visais skaičiais, kurie dalijasi iš 77.


# for i in range(10):  # 10 eilučių
#     print('* ' * 10)  # 10 žvaigždučių kiekvienoje eilutėje



