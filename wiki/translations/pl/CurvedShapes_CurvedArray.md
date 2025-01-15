---
 GuiCommand:
   Name: CurvedShapes CurvedArray
   Name/pl: Kształty Zakrzywione: Szyk krzywych
   MenuLocation: 
   Workbenches: CurvedShapes_Workbench/pl
   Shortcut: 
   SeeAlso: 
---

# CurvedShapes CurvedArray/pl



## Opis

Tworzy tablicę i zmienia rozmiar elementów w granicach jednej lub więcej krzywych kadłuba. W tym przykładzie pomarańczowy kształt bazowy jest przeskalowywany w granicach czerwonej i fioletowej krzywej kadłuba. Krzywe nie muszą być połączone. Krzywe kadłuba powinny leżeć na płaszczyźnie XY- XZ- lub YZ- lub równolegle do niej.

<https://github.com/chbergmann/CurvedShapesWorkbench/blob/master/Examples/WingExample.png> [Image:](Image:.md)



## Użycie

1.  Krok 1
2.  Krok 2: Wywołaj polecenie na kilka sposobów:
    -   Używając przycisku <img alt="" src=images/WorkbenchName_Command.svg  style="width:24px;"> przycisku [WorkbenchName Command](WorkbenchName_Command/pl.md)
    -   Używając skrótu klawiaturowego {{KEY}} {{KEY}}
    -   Używając opcji menu podręcznego **Menu → Command**.
3.  Krok 3



## Uwagi

-   Pierwsza krzywa wybrana do utworzenia Szyku krzywych będzie elementem, który zostanie przeciągnięty i zmieni rozmiar w granicach innych wybranych krzywych.



## Właściwości


{{Properties_Title|Podstawa}}

-    **Base**: Obiekt, z którego ma zostać utworzona tablica

-    **Hullcurves**: Lista jednej lub więcej krzywych ograniczających

-    **Axis**: Oś kierunku kształtu Baza.

-    **Items**: Liczba elementów tablicy.

-    **OffsetStart**: Przesunięcie pierwszej części w kierunku osi.

-    **OffsetEnd**: pPrzesunięcie ostatniej części od końca w przeciwnym kierunku osi.

-    **Twist**: Stosuje obrót wokół osi do elementów tablicy.

-    **Surface**: Tworzy powierzchnię nad elementami tablicy.

-    **Solid**: Tworzy bryłę, jeśli Base jest kształtem zamkniętym.



---
⏵ [documentation index](../README.md) > [Name](Category_Name.md) > [External Command Reference](Category_External%20Command%20Reference.md) > CurvedShapes CurvedArray/pl
