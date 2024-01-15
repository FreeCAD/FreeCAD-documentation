---
 GuiCommand:
   Name: Sketcher Offset
   Name/pl: Szkicownik: Geometria odsunięcia
   MenuLocation: Szkic , Narzędzia szkicownika , Geometria odsunięcia
   Workbenches: Sketcher_Workbench/pl
   Shortcut: **Z** **T**
   Version: 0.22
   SeeAlso: 
---

# Sketcher Offset/pl



## Opis

Narzędzie <img alt="" src=images/Sketcher_Offset.svg  style="width:24px;"> **Geometria odsunięcia** rysuje równoodległe krawędzie wokół wybranych krawędzi. Po uruchomieniu narzędzia kursor myszki zmienia się w biały krzyżyk z czerwoną ikoną odsunięcia:  <img alt="" src=images/Sketcher_Pointer_Create_Offset.svg  style="width:32px;"> .

<img alt="" src=images/Sketcher_OffsetExample.png‎  style="width:400px;"> 
*Równoległe krawędzie wokół zamkniętej (O) i otwartej (U) polilinii konstrukcyjnej.*



## Użycie

1.  Wybierz jedną lub więcej krawędzi.
2.  Polecenie można wywołać na kilka sposobów:
    -   Naciśnij przycisk **<img src="images/Sketcher_Offset.svg" width=16px> [Geometria odsunięcia](Sketcher_Offset.md)**.
    -   Wybierz opcję **Szkicownik → Narzędzia szkicownika → <img src="images/Sketcher_Offset.svg" width=16px> Geometria odsunięcia** z menu.
    -   Skrót klawiaturowy: **Z**, a następnie **T**.
3.  Sekcja **Parametry przesunięcia** jest dodawana w górnej części [Panel zadań](Task_panel/pl.md) szkicownika.
4.  Opcjonalnie można zmienić pole wyboru **Tryb** z {{Value|Łuk}} *(domyślnie)* na {{Value|Przecięcie}}.
5.  Opcjonalnie zaznacz pole wyboru **Usuń oryginalne geometrie**, aby zachować tylko nowy kontur.
6.  Opcjonalnie zaznacz pole wyboru **Dodaj wiązanie odsunięcia**, aby dodać wiązanie wymiarowe między odsuniętym konturem a oryginalną geometrią.
7.  Przeciągnij kursor i kliknij lub wprowadź odległość, aby ustawić przesunięcie i zakończyć polecenie. Spowoduje to również usunięcie sekcji **Parametry odsunięcia** z panelu Zadanie.

Jeśli funkcja **Dodaj wiązanie odsunięcia** została aktywowana, przesunięcie można dostosować, zmieniając ograniczenie wymiaru.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher Offset/pl
