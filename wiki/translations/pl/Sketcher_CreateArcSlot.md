---
 GuiCommand:
   Name: Sketcher CreateArcSlot
   Name/pl: Szkicownik: Utwórz owal na łuku
   MenuLocation: Sketch , Elementy geometryczne szkicownika , Utwórz szczelinę łukową
   Workbenches: Sketcher_Workbench/pl
   Shortcut: **G** **S** **2**
   Version: 1.0
   SeeAlso: Sketcher_CreateSlot/pl
---

# Sketcher CreateArcSlot/pl



## Opis

Narzędzie <img alt="" src=images/Sketcher_CreateArcSlot.svg  style="width:24px;"> **Utwórz szczelinę łukową** tworzy szczelinę łukową, zamkniętą polilinię składającą się z dwóch równoległych koncentrycznych łuków zamkniętych dwoma półokręgami lub dwiema promieniowymi liniami prostymi.

<img alt="" src=images/Sketcher_CreateArcSlot_Example.png  style="width:300px;"> 
*Szczelina łukowa ''(biały)'' z wewnętrzną geometrią ''(ciemnożółta)''.*



## Użycie

Zapoznaj się również z informacjami na stronie [Pomoce kreślarskie](Sketcher_Workbench/pl#Pomoce_kreślarskie.md).

Pos-OVP = Pozycyjne [Parametry w widoku](Sketcher_Preferences#Ogólne/pl.md). {{Version/pl|1.0}}
Dim-OVP = Wymiarowe parametry w widoku. {{Version/pl|1.0}}

1.  Istnieje kilka sposobów wywołania narzędzia:
    -   Naciśnij przycisk **<img src="images/Sketcher_CreateArcSlot.svg" width=16px> '''Utwórz szczelinę łukową'''**.
    -   Wybierz z menu opcję **Szkic → Elementy geometryczne szkicownika → <img src="images/Sketcher_CreateArcSlot.svg" width=16px> Utwórz szczelinę łukową**.
    -   Skrót klawiaturowy: **G**, **S**, **2**.
2.  Kursor zmieni się w krzyżyk z ikoną narzędzia.
3.  Sekcja **Parametry szczeliny łukowej** jest dodawana w górnej części [okna dialogowego](Sketcher_Dialog/pl.md).
4.  Opcjonalnie naciśnij klawisz **M** lub wybierz z rozwijanej listy w sekcji parametrów, aby zmienić tryb narzędzia:
    -   <img alt="" src=images/Sketcher_CreateArcSlot.svg  style="width:16px;"> **Końce łuku**:
        1.  Wybierz środek szczeliny łuku. Lub z Pos-OVP: wprowadź jego współrzędne X i / lub Y.
        2.  Wybierz środek pierwszego półokręgu, który definiuje również promień *(wirtualnej)* linii środkowej szczeliny. Lub za pomocą Dim-OVP: wprowadź promień i / lub kąt początkowy szczeliny. Kąt jest odniesiony do osi X szkicu. Dla tego kąta nie jest tworzone żadne wiązanie.
        3.  Wybierz środek drugiego półkola. Lub z Dim-OVP: wprowadź kąt apertury łuku linii środkowej.
        4.  Wybierz punkt, aby zdefiniować promień półkola. Lub za pomocą Dim-OVP: wprowadź ten promień.
    -   <img alt="" src=images/Sketcher_CreateRectangleSlot.svg  style="width:16px;"> **Płaskie końce**:
        1.  Wybierz środek szczeliny łuku. Lub z Pos-OVP: wprowadź jego współrzędne X i / lub Y.
        2.  Wybierz punkt początkowy pierwszego łuku, to również definiuje jego promień



## Uwagi

-   Punkty wybrane do zdefiniowania promienia półokręgów lub przesunięcia łuków wewnętrznych i zewnętrznych nie muszą dotykać geometrii, odległość od kursora do środka gniazda faktycznie kontroluje wartość.
-   W trybie **Końce łuku** pierwszy promień dotyczy wirtualnego łuku środkowego, podczas gdy w trybie **Płaskie końce** dotyczy on jednego z łuków konturowych.
-   Jeśli wprowadzona wartość szerokości w trybie **Płaskie końce** jest dodatnia, związany łuk staje się łukiem wewnętrznym, dla wartości ujemnej będzie to łuk zewnętrzny.



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CreateArcSlot/pl
