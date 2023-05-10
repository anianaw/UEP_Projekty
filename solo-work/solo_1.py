#zadanie 1.1

hello = "Hello"
student = "Ola"

print("{} {}".format(hello, student))

#zadanie 1.2

student = input("Wpisz swoje imię: ")
print("Hello {}".format(student))

#zadanie 1.3

studenci = ["Basia", "Kasia", "Zosia", "Ola"]
liczba_studentow = len(studenci)
print("Liczba studentów: ", liczba_studentow)

#zadanie 1.4

studenci = ["Ania", "Kasia", "Piotr", "Tomek"]

for student in studenci:
    print("Hello {}".format(student))

#zadanie 1.5

liczba = 3
potega = 4

wynik = liczba ** potega

print("Wynik wynosi: {}".format(wynik))

#zadanie 1.6

ciag_znakow = "edbw(hdakqas(skqskahb))adwndwb(wgwidn()dsqwhjdw)"

licznik = 0
for znak in ciag_znakow:
    if znak == "(":
        licznik += 1

print("Liczba nawiasow otwierajacych wynosi: " + str(licznik))

#zadanie 1.7

studenci = ["Anna Szczesny", "Tomasz Nijaki", "Barbara Kowalska", "Jan Niezbedny"]

sortowanie_po_imieniu = sorted(studenci, key=lambda x: x.split()[0])

print("Alfabetyczna lista studentów wynosi:")
for student in sortowanie_po_imieniu:
    print(student)

#zadanie 1.8

studenci = ["Anna Szczesny", "Tomasz Nijaki", "Barbara Kowalska", "Jan Niezbedny"]

sortowanie_po_nazwisku = sorted(studenci, key=lambda x: x.split()[-1])

print("Alfabetyczna lista studentów wynosi:")
for student in sortowanie_po_nazwisku:
    print(student)

#zadanie 1.9

studenci = ["Anna Szczesny", "Tomasz Nijaki", "Barbara Kowalska", "Jan Niezbedny"]

liczba_n = 0
for student in studenci:
    if student.split()[-1][0].lower() == "n":
        liczba_n += 1

print("Liczba studentów na N wynosi:", liczba_n)

#zadanie 1.10

wykres_1 = [[2, 4], [4, 4], [6, 4]]
wykres_2 = [[2, 3], [4, 4], [6, 5]]
wykres_3 = [[2, 3], [4, 3], [5, 4]]

wykres_1_funkcja_liniowa = False
wykres_2_funkcja_liniowa = False
wykres_3_funkcja_liniowa = False

def czy_funkcja_liniowa(wykres):
    if len(wykres) <= 2:
        return True

    slope = None
    for i in range(len(wykres) - 1):
        x1, y1 = wykres[i]
        x2, y2 = wykres[i + 1]
        current_slope = (y2 - y1) / (x2 - x1)
        if slope is None:
            slope = current_slope
        elif current_slope != slope:
            return False

    return True

wykres_1_funkcja_liniowa = czy_funkcja_liniowa(wykres_1)
wykres_2_funkcja_liniowa = czy_funkcja_liniowa(wykres_2)
wykres_3_funkcja_liniowa = czy_funkcja_liniowa(wykres_3)

if wykres_1_funkcja_liniowa:
    print("Dla punktów w wykres_1 można wyznaczyć funkcję liniową.")
else:
    print("Dla punktów w wykres_1 nie można wyznaczyć funkcji liniowej.")

if wykres_2_funkcja_liniowa:
    print("Dla punktów w wykres_2 można wyznaczyć funkcję liniową.")
else:
    print("Dla punktów w wykres_2 nie można wyznaczyć funkcji liniowej.")

if wykres_3_funkcja_liniowa:
    print("Dla punktów w wykres_3 można wyznaczyć funkcję liniową.")
else:
    print("Dla punktów w wykres_3 nie można wyznaczyć funkcji liniowej.")
