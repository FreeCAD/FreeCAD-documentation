---
- GuiCommand:
   Name:Sketcher CreateEllipseBy3Points
   Name/pl:Szkicownik: Utwórz elipsę przez trzy punkty
   MenuLocation:Szkic - Elementy geometryczne szkicownika - Utwórz elipsę przez trzy punkty
   Workbenches:[Szkicownik](Sketcher_Workbench/pl.md)
   Shortcut:**G** **3** **E**
   Version:0.15
   SeeAlso:[Utwórz elipsę przez środek](Sketcher_CreateEllipseByCenter/pl.md), [Utwórz okrąg](Sketcher_CreateCircle/pl.md), [Utwórz łuk na podstawie elipsy](Sketcher_CreateArcOfEllipse/pl.md)
---

# Sketcher CreateEllipseBy3Points/pl



## Opis

Narzędzie to rysuje elipsę wybierając trzy punkty: **(1)** periapsis (pierwsze przecięcie dłuższej średnicy z elipsą), **(2)** apoapsis *(drugie przecięcie dłuższej średnicy z elipsą)*, **(3)** jeden punkt na boku dłuższej średnicy **(a)** określający mniejszy promień **(b)**. **(c)** to wynikowy środek, a **(f)** to punkty ogniskowe.

Podczas uruchamiania narzędzia kursor myszki zmienia kształt na biały krzyż z czerwoną ikoną elipsy.

![](images/Ellipse_3Point.png‎ ) 
*Kolejność kliknięć jest oznaczona żółtymi strzałkami z cyframi.<br>
1 to perycentrum, 2 to apocentrum, 3 to punkt definiujący mniejszą średnicę.<br>
Zielone linie to główne i mniejsze średnice.<br>
Niebieskie linie to linie konstrukcyjne w celach ilustracyjnych.*



## Użycie

-   Naciśnij przycisk **[<img src=images/Sketcher_CreateEllipseBy3Points.svg style="width:16px"> [Utwórz elipsę przez trzy punkty](Sketcher_CreateEllipseBy3Points/pl.md)**.
-   Pierwsze kliknięcie w oknie widoku 3D ustawia punkt określający przecięcie średnicy głównej z elipsą *(periapsis)*. Drugie kliknięcie w oknie widoku 3D wyznacza punkt określający przecięcie średnicy głównej z elipsą w kierunku przeciwnym do punktu środkowego *(apoapsis)*. Trzecie kliknięcie ustawia punkt na elipsie definiujący promień mniejszy.

-   Po trzecim kliknięciu tworzona jest elipsa wraz z zestawem geometrii konstrukcyjnych do niej dopasowanych (średnica główna, średnica mała, dwie ogniskowe). Geometria konstrukcyjna może być ręcznie usunięta, jeśli nie jest potrzebna, i odtworzona później. Zobacz [Pokaż / ukryj geometrię wewnętrzną](Sketcher_RestoreInternalAlignmentGeometry/pl.md).
-   Naciśnięcie **ESC** lub kliknięcie prawym przyciskiem myszy powoduje przerwanie funkcji.



## Szczególe cechy 

-   Osie główne i mniejsze elipsy są sztywno określone i nie mogą być zamienione przez zmianę rozmiaru elipsy. Jest to konsekwencją zastosowanej parametryzacji solwera *(środek (x,y), ogniskowa1 (x,y) i długość promienia mniejszego (b))* oraz tego samego zachowania ścisłego OpenCascade. Elipsa musi być obrócona, aby zamienić osie.
-   Elipsa może funkcjonować jako koło, gdy jej linie średnicy głównej i mniejszej są usuwane, a jedno z ognisk jest związane, aby pokryć się ze środkiem. Ale wiązanie promienia nie będzie działać na takim okręgu.
-   Przesuwanie elipsy po krawędzi jest takie samo jak przesuwanie jej środka.





{{Sketcher_Tools_navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CreateEllipseBy3Points/pl
