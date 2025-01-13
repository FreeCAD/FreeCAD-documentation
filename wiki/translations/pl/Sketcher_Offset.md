---
 GuiCommand:
   Name: Sketcher Offset
   Name/pl: Szkicownik: Geometria odsunięcia
   MenuLocation: Szkic , Narzędzia szkicownika , Geometria odsunięcia
   Workbenches: Sketcher_Workbench/pl
   Shortcut: **Z** **T**
   Version: 1.0
   SeeAlso: 
---

# Sketcher Offset/pl



## Opis

Narzędzie <img alt="" src=images/Sketcher_Offset.svg  style="width:24px;"> **Geometria odsunięcia** tworzy równoodległe krawędzie wokół wybranych krawędzi.

<img alt="" src=images/Sketcher_OffsetExample.png‎  style="width:400px;"> 
*Równoległe krawędzie wokół zamkniętej (O) i otwartej (U) polilinii konstrukcyjnej.*



## Użycie

Zapoznaj się również z informacjami na stronie [Pomoce kreślarskie](Sketcher_Workbench/pl#Pomoce_kreślarskie.md).

Dim-OVP = Wymiarowe [Parametry w widoku](Sketcher_Preferences/pl#Ogólne.md).

1.  Wybierz jedną lub więcej linii, okręgów i / lub łuków kołowych.
2.  Narzędzie można wywołać na kilka sposobów:
    -   Naciśnij przycisk **<img src="images/Sketcher_Offset.svg" width=16px> '''Geometria odsunięcia'''**.
    -   Wybierz z menu opcję **Szkic → Narzędzia szkicownika → <img src="images/Sketcher_Offset.svg" width=16px> Geometria odsunięcia**.
    -   Kliknij prawym przyciskiem myszy w [widoku 3D](3D_view/pl.md) i z menu podręcznego wybierz opcję **<img src="images/Sketcher_Offset.svg" width=16px> Geometria odsunięcia**.
    -   Użyj skrótu klawiaturowego: **Z**, a następnie **T**.
3.  Kursor zmieni się w krzyżyk z ikoną narzędzia.
4.  Sekcja **Parametry przesunięcia** jest dodawana w górnej części [okna dialogowego](Sketcher_Dialog/pl.md).
5.  Opcjonalnie naciśnij klawisz **U** lub zaznacz pole wyboru **Usuń oryginalne geometrie**, aby zachować tylko nowy kontur.
6.  Opcjonalnie naciśnij klawisz **J** lub zaznacz pole wyboru **Dodaj wiązanie odsunięcia**, aby dodać wiązanie wymiarowe między przesuniętym obrysem a oryginalną geometrią.
7.  Opcjonalnie naciśnij klawisz **M** lub wybierz z listy rozwijanej w sekcji parametrów, aby zmienić tryb narzędzia:
    -   <img alt="" src=images/Sketcher_OffsetArc.svg  style="width:16px;"> 
**Łuk**
    -   <img alt="" src=images/Sketcher_OffsetIntersection.svg  style="width:16px;"> 
**Przecięcie**
8.  Wybierz punkt, aby zdefiniować odległość przesunięcia. Lub za pomocą Dim-OVP: wprowadź tę odległość.
9.  Geometria zostanie utworzona, a jeśli wybrano opcję **Dodaj wiązanie odsunięcia**, zostanie dodane wiązanie wymiarowe.



## Ograniczenia

To narzędzie ma pewne ograniczenia, głównie wynikające z problemów [silnika OCC](OpenCASCADE/pl.md):

-   Następujące typy geometrii nie są obecnie wspierane: elipsy, krzywe złożone, hiperbole i parabole.
-   Odsuwanie pojedynczej linii może dawać niespodziewane wyniki.
-   Otwarte kontury są odsuwane po obu stronach, tworząc zamknięty kontur.
-   Geometria zewnętrzna nie może być odsuwana bezpośrednio.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher Offset/pl
