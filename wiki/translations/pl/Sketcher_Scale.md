---
 GuiCommand:
   Name: Sketcher Scale
   Name/pl: Szkicownik: Przekształcenie skali
   MenuLocation: Szkic , Narzędzia szkicownika , Przekształcenie skali
   Workbenches: Sketcher_Workbench/pl
   Shortcut: **Z** **P** **S**
   Version: 1.0
   SeeAlso: 
---

# Sketcher Scale/pl



## Opis

Narzędzie <img alt="" src=images/Sketcher_Scale.svg  style="width:24px;"> **Przekształcenie skali** skaluje lub opcjonalnie tworzy skalowane kopie wybranych elementów.



## Użycie

Zapoznaj się również z informacjami na stronie [Pomoce kreślarskie](Sketcher_Workbench/pl#Pomoce_kreślarskie.md).

Pos-OVP = Pozycyjne [Parametry w widoku](Sketcher_Preferences#Ogólne/pl.md). {{Version/pl|1.0}}
Dim-OVP = Wymiarowe parametry w widoku. {{Version/pl|1.0}}

1.  Wybierz jedną lub więcej krawędzi i / lub obiektów [punktów](Sketcher_CreatePoint/pl.md). Więzy nałożone na wybrane elementy są również przetwarzane. Jeśli oryginalne elementy zostaną przeskalowane, wszelkie inne powiązane z nimi wiązania zostaną usunięte.
2.  Narzędzie można wywołać na kilka sposobów:
    -   Naciśnięcie przycisku **<img src="images/Sketcher_Scale.svg" width=16px> '''Przekształcenie skali'''**.
    -   Wybierz z menu opcję **Szkic → Narzędzia szkicownika → <img src="images/Sketcher_Scale.svg" width=16px> Przekształcenie skali**.
    -   Kliknij prawym przyciskiem myszy w [3D view](3D_view.md) i wybierz opcję **<img src="images/Sketcher_Scale.svg" width=16px> Przekształcenie skali** z menu podręcznego.
    -   Użyj skrótu klawiaturowego: **Z**, następnie **P**, a potem **S**.
3.  Kursor zmieni się w krzyżyk z ikoną narzędzia.
4.  Sekcja **Parametry skalowania** jest dodawana w górnej części [okna dialogowego](Sketcher_Dialog/pl.md).
5.  Opcjonalnie naciśnij klawisz **U** lub zaznacz pole wyboru **Zachowaj oryginalne geometrie**, aby utworzyć przeskalowane kopie wybranych elementów.
6.  Wybierz punkt bazowy dla operacji skalowania. Lub za pomocą Pos-OVP: wprowadź jego współrzędne X i/lub Y.
7.  Wybierz punkt końcowy pierwszej linii pomocniczej. Jej kąt i długość są dowolne.
8.  Wybierz punkt końcowy drugiej linii pomocniczej. Jej kąt jest również dowolny. Jego długość w stosunku do długości pierwszej linii pomocniczej określa współczynnik skali. Lub za pomocą Dim-OVP: wprowadź współczynnik skali.
9.  Oryginalne elementy są skalowane lub tworzone są skalowane kopie. Nie są dodawane żadne wiązania oparte na Pos-OVP lub Dim-OVP.



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher Scale/pl
