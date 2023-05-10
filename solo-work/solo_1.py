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








