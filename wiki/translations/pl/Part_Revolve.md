---
- GuiCommand:
   Name:Part Revolve
   Name/pl:Część: Obrót
   MenuLocation:Część - Obrót ...
   Workbenches:[Część](Part_Workbench/pl.md)
---

# Part Revolve/pl



## Opis

Funkcja ta obraca wybrany obiekt tworząc wyciągnięcie wokół wybranej osi. Dozwolone są następujące typy kształtów, które prowadzą do uzyskania kształtów wyjściowych:

  Kształt wejściowy   Forma wyjściowa
   
  Wierzchołek         Krawędź
  Krawędź             Powierzchnia
  Linia łamana        Powłoka
  Powierzchnia        Bryła
  Powłoka             Bryła złozona *(Compsolid)*

Można też użyć [Szkicu](Sketcher_Workbench/pl.md). Bryły lub bryły złożone nie są dozwolone jako kształty wejściowe. Również standardowe związki nie są obecnie dozwolone.

![](images/Dialog-revolve.png )

Argument **Kąt** określa, jak daleko obiekt ma być obrócony. Współrzędne przesuwają początek osi obrotu w stosunku do początku układu współrzędnych.

Jeśli wybierzemy oś zdefiniowaną przez użytkownika, to liczby określają kierunek osi obrotu w stosunku do układu współrzędnych: Jeśli współrzędna Z wynosi 0, a współrzędne Y i X są niezerowe, to oś znajduje się na płaszczyźnie X-Y. Jej kąt jest taki, że jej styczna jest stosunkiem podanych współrzędnych X i Y.



## Uwagi

-   Obiekty typu [odnośnik](App_Link/pl.md) powiązane z odpowiednimi typami obiektów mogą być również używane jako kształty i do określania osi. {{Version/pl|0.20}}
-   Jeśli obiekt do obrócenia przecina oś obrotu, operacja nie powiedzie się w większości przypadków.



---
![](images/Button_right.svg) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Revolve/pl
