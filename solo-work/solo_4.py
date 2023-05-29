class Ksiazka:
    def __init__(self, tytul, autor, rok_wydania, liczba_stron, kategoria, ocena):
        self.tytul = tytul
        self.autor = autor
        self.rok_wydania = rok_wydania
        self.liczba_stron = liczba_stron
        self.kategoria = kategoria
        self.ocena = ocena

    def __str__(self):
        return f"Tytuł: {self.tytul}\nAutor: {self.autor}\nRok wydania: {self.rok_wydania}\nLiczba stron: {self.liczba_stron}\nKategoria: {self.kategoria}\nOcena: {self.ocena}"

    def znajdz_bestsellery(ksiazki):
        bestsellery = []
        for ksiazka in ksiazki:
            if ksiazka.ocena >= 4.5:
                bestsellery.append(ksiazka)
        return bestsellery

    def segreguj_od_najnowszych(ksiazki):
        return sorted(ksiazki, key=lambda x: x.rok_wydania, reverse=True)

    def znajdz_najwiecej_stron(ksiazki):
        max_strony = 0
        najwiecej_stron_ksiazki = []

        for ksiazka in ksiazki:
            if ksiazka.liczba_stron > max_strony:
                max_strony = ksiazka.liczba_stron
                najwiecej_stron_ksiazki = [ksiazka]
            elif ksiazka.liczba_stron == max_strony:
                najwiecej_stron_ksiazki.append(ksiazka)

        return najwiecej_stron_ksiazki

    def znajdz_najmniej_stron(ksiazki):
        min_strony = float('inf')
        najmniej_stron_ksiazki = []

        for ksiazka in ksiazki:
            if ksiazka.liczba_stron < min_strony:
                min_strony = ksiazka.liczba_stron
                najmniej_stron_ksiazki = [ksiazka]
            elif ksiazka.liczba_stron == min_strony:
                najmniej_stron_ksiazki.append(ksiazka)

        return najmniej_stron_ksiazki


ksiazka1 = Ksiazka("Terapeutka", "B.A. Paris", 2022, 400, "Thriller", 4.4)
ksiazka2 = Ksiazka("Harry Potter i Kamień Filozoficzny", "J.K. Rowling", 1997, 320, "Fantasy", 4.8)
ksiazka3 = Ksiazka("Wiedźmin: Ostatnie życzenie", "Andrzej Sapkowski", 1993, 280, "Fantasy", 4.6)
ksiazka4 = Ksiazka("1984", "George Orwell", 1949, 328, "Dystopia", 4.7)
ksiazka5 = Ksiazka("Mężczyźni są z Marsa, kobiety z Wenus", "John Gray", 1992, 368, "Poradnik", 3.9)
ksiazka6 = Ksiazka("Złodziejka książek", "Markus Zusak", 2005, 560, "Fikcja historyczna", 4.3)
ksiazka7 = Ksiazka("Człowiek w poszukiwaniu sensu", "Viktor E. Frankl", 1946, 160, "Psychologia", 4.6)
ksiazka8 = Ksiazka("Zmierzch", "Stephenie Meyer", 2005, 498, "Romans/Fantasy", 3.5)
ksiazka9 = Ksiazka("Mały Książę", "Antoine de Saint-Exupéry", 1943, 96, "Literatura dziecięca", 4.9)
ksiazka10 = Ksiazka("Hobbit, czyli tam i z powrotem", "J.R.R. Tolkien", 1937, 310, "Fantasy", 4.7)

ksiazki = [ksiazka1, ksiazka2, ksiazka3, ksiazka4, ksiazka5, ksiazka6, ksiazka7, ksiazka8]

print("--------------------")

bestsellery = Ksiazka.znajdz_bestsellery(ksiazki)
for ksiazka in bestsellery:
    print(ksiazka)

print("--------------------")

posortowane = Ksiazka.segreguj_od_najnowszych(ksiazki)
for ksiazka in posortowane:
    print(ksiazka)

print("--------------------")

najwiecej_stron = Ksiazka.znajdz_najwiecej_stron(ksiazki)
print("Książki z największą liczbą stron:")
for ksiazka in najwiecej_stron:
    print(ksiazka)

print("--------------------")

najmniej_stron = Ksiazka.znajdz_najmniej_stron(ksiazki)
print("Książki z najmniejszą liczbą stron:")
for ksiazka in najmniej_stron:
    print(ksiazka)