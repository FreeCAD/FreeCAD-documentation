---
 GuiCommand:
   Name: Draft Slope
   Name/pl: Rysunek Roboczy: Ustaw nachylenie
   MenuLocation: Modyfikacja , Ustaw nachylenie<br>Narzędzia , Ustaw nachylenie
   Workbenches: Draft_Workbench/pl, BIM_Workbench/pl
   Version: 0.17
---

# Draft Slope/pl



## Opis

Narzędzie <img alt="" src=images/Draft_Slope.svg  style="width:24px;"> **Utwórz nachylenie** pochyla wybraną [linię](Draft_Line/pl.md) lub [polilinię](Draft_Wire/pl.md) poprzez zwiększenie lub zmniejszenie współrzędnej Z każdego punktu znajdującego się za punktem pierwszym. Narzędzie to może być również użyte do spłaszczenia [polilinii](Draft_Wire/pl.md). Należy pamiętać, że nachylenie odnosi się do płaszczyzny XY zdefiniowanej przez właściwość **Umiejscowienie** obiektów.

<img alt="" src=images/Draft_Slope_example.png  style="width:400px;"> 
*Po lewej, pozioma linia. Po prawej, ta sama linia o wartości nachylenia 1 ''(kąt 45°)''.*



## Użycie

1.  Wybierz jedną lub więcej [linii](Draft_Line/pl.md) i / lub [polilinii](Draft_Wire/pl.md).
2.  Polecenie można wywołać na kilka sposobów:
    -   [Środowisko pracy Rysunek Roboczy](Draft_Workbench/pl.md): Naciśnij przycisk **<img src="images/Draft_Slope.svg" width=16px> '''Ustaw nachylenie**.
    -   Rysunek Roboczy: Wybierz z menu opcję **Modyfikacja → <img src="images/Draft_Slope.svg" width=16px> Ustaw nachylenie**.
    -   [Środowisko pracy BIM](BIM_Workbench/pl.md): Wybierz opcję **Narzędzia → <img src="images/Draft_Slope.svg" width=16px> Ustaw nachylenie** z menu.
3.  Wprowadź wartość **Nachylenie**. {{Value|0}} oznacza, że każdy segment jest poziomy, {{Value|0.5}} oznacza, że wysokość delta dla każdego segmentu jest {{Value|0.5}} razy jego długość, itd. Wartość może być również ujemna.
4.  Naciśnij **Enter** lub przycisk **OK**, aby zakończyć wykonywanie polecenia.



## Tworzenie skryptów 

Zobacz również stronę: [Dokumentacja API generowana automatycznie](https://freecad.github.io/SourceDoc/) oraz [Podstawy pisania skryptów dla FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Nie ma metody Python do pochylania obiektów. Aby naśladować wyniki polecenia **Utwórz nachylenie**, należy zmodyfikować właściwości geometryczne obiektów.



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Slope/pl
