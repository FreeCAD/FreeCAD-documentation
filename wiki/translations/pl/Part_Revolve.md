---
- GuiCommand:/pl
   Name:Part Revolve
   Name/pl:Część: Wyciągnij przez obrót
   MenuLocation:Część → Wyciągnij przez obrót
   Workbenches:[Część](Part_Workbench/pl.md)
---

# Part Revolve/pl

## Opis

Funkcja ta obraca wybrany obiekt tworząc wyciągnięcie wokół wybranej osi. Dozwolone są następujące typy kształtów, które prowadzą do uzyskania kształtów wyjściowych *([Zobacz wskazówki dotyczące wyjątków](#Notes.md))*:

  Kształt wejściowy   Forma wyjściowa
  ------------------- -----------------------------
  Wierzchołek         Krawędź
  Krawędź             Powierzchnia
  Linia łamana        Powłoka
  Powierzchnia        Bryła
  Powłoka             Bryła złozona *(Compsolid)*

Bryły lub bryły złożone nie są dozwolone jako kształty wejściowe. Również standardowe związki nie są obecnie dozwolone. Przyszłe wersje programu będą weryfikowały rzeczywisty typ kształtu obiektów złożonych.

![](images/Dialog-revolve.png )

Argument **Kąt** określa, jak daleko obiekt ma być obrócony. Współrzędne przesuwają początek osi obrotu w stosunku do początku układu współrzędnych.

Jeśli wybierzemy oś zdefiniowaną przez użytkownika, to liczby określają kierunek osi obrotu w stosunku do układu współrzędnych: Jeśli współrzędna Z wynosi 0, a współrzędne Y i X są niezerowe, to oś znajduje się na płaszczyźnie X-Y. Jej kąt jest taki, że jej styczna jest stosunkiem podanych współrzędnych X i Y.

### Uwagi

-   Jeśli Twoja wersja programu FreeCAD w oknie dialogowym **Wyciągnij przez obrót** ma pole wyboru dla bryły, możesz wykonać bryłę z zamkniętych ciągów linii i krawędzi.
-   Jeśli funkcja **Wyciągnij przez obrót** jest wykonywana przy użyciu osi, która przecina powierzchnię do obracania, a użytkownik chce utworzyć bryłę, wynik może być nieprawidłowy. Może się to zdarzyć z różnych powodów, samoistnego przecięcia, kierunku, itp.

---
[documentation index](../README.md) > [Part](Part_Workbench.md) > Part Revolve/pl
