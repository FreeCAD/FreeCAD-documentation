---
 GuiCommand:
   Name: Sketcher CreateRectangle
   Name/pl: Szkicownik: Utwórz prostokąt
   MenuLocation: Szkic , Elementy geometryczne szkicownika , Utwórz prostokąt
   Workbenches: Sketcher_Workbench/pl
   Shortcut: **G** **R**
   SeeAlso: Sketcher_CreateOblong/pl, Sketcher_CreatePolyline/pl
---

# Sketcher CreateRectangle/pl



## Opis

Narzędzie to rysuje prostokąt, wybierając dwa przeciwstawne punkty. Po uruchomieniu narzędzia wskaźnik myszy zmienia się w biały krzyż z czerwoną prostokątną ikoną. Na bieżąco wyświetlane są obok niego współrzędne wskaźnika w kolorze niebieskim.

Aby zdefiniować prostokąt za pomocą punktu środkowego i punktu na krawędzi, użyj narzędzia [Utwórz wyśrodkowany prostokąt](Sketcher_CreateRectangle_Center/pl.md).

![](images/SketcherCreateRectangleExample.png‎ )



## Użycie

-   Po naciśnięciu przycisku na pasku narzędzi **[<img src=images/Sketcher_CreateRectangle.svg style="width:24px"> [Utwórz prostokąt](Sketcher_CreateRectangle/pl.md)**, kliknij raz, aby ustawić pierwszy narożnik, a następnie przesuń kursor myszki i kliknij drugi raz, aby ustawić przeciwległy narożnik.
-   Naciśnięcie klawisza **Esc** lub kliknięcie prawym przyciskiem myszy anuluje tę funkcję.



## Uwagi

-   Po uruchomieniu narzędzia prostokąta w górnej części [Panelu zadań](Task_panel/pl.md) ({{Version/pl|0.22}}) dodano sekcję **Parametry prostokąta**. Zawiera ona:

1.  Pole **Tryb** umożliwiające wybór jednego z trybów rysowania prostokąta:
    -   Narożnik, długość i szerokość
    -   Środek, długość i szerokość
    -   Trzy narożniki
    -   Środek i dwa narożniki
2.  Pole wyboru **Zaokrąglone narożniki**, aby zastosować zaokrąglone narożniki do prostokąta.
3.  Pole wyboru **Obramowanie**, aby dodać kontur ze stałym przesunięciem do *(zaokrąglonego)* prostokąta.

-   Wszystkie trzy przyciski w tym wyborze uruchamiają teraz to samo narzędzie, ale z różnymi wstępnie ustawionymi kombinacjami trybu i opcji, które nadal można zmienić po pierwszym kliknięciu.
-   Jeśli opcja **Zaokrąglone narożniki** jest włączona, przesunięcie jest do wewnątrz, a wartość przesunięcia jest większa niż promień narożnika, przesunięty kontur zostanie utworzony bez zaokrągleń.
-   Tryby **Trzy narożniki** i **Środek i dwa narożniki** tworzą równoległoboki zamiast prostokątów.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CreateRectangle/pl
