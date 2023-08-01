---
- GuiCommand:
   Name:TechDraw FaceCenterLine
   Name/pl:Rysunek Techniczny: Dodaj oś ściany
   MenuLocation:Rysunek Techniczny - Dodaj linie - Dodaj oś ściany
   Workbenches:[Rysunek Techniczny](TechDraw_Workbench/pl.md)
   Version:0.19
   SeeAlso:[Dodaj wierzchołek kosmetyczny](TechDraw_CosmeticVertex/pl.md), [Dodaj oś pomiędzy dwiema liniami](TechDraw_2LineCenterLine/pl.md), [Dodaj oś pomiędzy dwoma punktami](TechDraw_2PointCenterLine/pl.md), [Usuń geometrie pomocnicze](TechDraw_CosmeticEraser/pl.md)
---

# TechDraw FaceCenterLine/pl


</div>



## Opis

Narzędzie **Dodaj oś ściany** dodaje linię środkową do wybranych ścian.

<img alt="" src=images/TechDraw_FaceCenterLine_Sample.png  style="width:400px;">


<div class="mw-translate-fuzzy">



*Oś dodana do ściany.*


</div>

## Usage create 


<div class="mw-translate-fuzzy">

1.  Wybierz jedną lub więcej ścian w widoku.
2.  Naciśnij przycisk **<img src="images/TechDraw_FaceCenterLine.svg" width=16px> Dodaj oś ściany**.
3.  Otworzy się okno dialogowe, w którym można określić atrybuty nowej linii środkowej.
4.  Linia środkowa zostanie dodana w punkcie środkowym obwiedni wybranej ściany *(ścian)*.


</div>

## Usage edit 


<div class="mw-translate-fuzzy">

Dowolny z przycisków poleceń linii środkowej *(**<img src="images/TechDraw_FaceCenterLine.svg" width=16px> Dodaj oś ściany**, **<img src="images/TechDraw_2LineCenterLine.svg" width=16px> [Dodaj oś pomiędzy dwiema liniami](TechDraw_2LineCenterLine/pl.md)**, **<img src="images/TechDraw_2PointCenterLine.svg" width=16px> [Dodaj oś pomiędzy dwoma punktami](TechDraw_2PointCenterLine/pl.md)**)* można użyć do edycji dowolnej z linii środkowej.


</div>


<div class="mw-translate-fuzzy">

1.  Wybierz linię środkową.
2.  Naciśnij przycisk polecenia dowolnej linii środkowej.
3.  Otworzy się okno dialogowe, w którym można zmienić atrybuty linii środkowej.
4.  Naciśnij **OK**, aby zobaczyć wprowadzone zmiany.


</div>




<div class="mw-translate-fuzzy">

## Właściwości


</div>


<div class="mw-translate-fuzzy">

1.  Tryb (przyciski wyboru):
    -   **Pionowo**: wymusza pionową linię środkową
    -   **Poziomo**: Wymusza linię środkową w poziomie.
    -   **Wyrównane**: Ta opcja nie jest możliwa w przypadku linii środkowej do ściany.
2.  **Przesuń w poziomie**: Przesuwa linię środkową w lewo lub w prawo od jej normalnego położenia.
3.  **Przesuń w pionie**: Przesuwa linię środkową w górę lub w dół od jej normalnego położenia.
4.  **Obróć**: Obraca linię środkową wokół jej środka *(stopnie. + przeciwnie do ruchu wskazówek zegara, - zgodnie z ruchem wskazówek zegara)*.
5.  **Rozszerz o**: Wydłuża linię środkową o podaną wartość.
6.  **Kolor**: Kolor linii środkowej.
7.  **Grubość**: Grubość linii środkowej
8.  **Styl**: <img alt="" src=images/Continuous-line.svg  style="width:20px;"> Ciągła, <img alt="" src=images/Dash-line.svg  style="width:20px;"> Kreska, <img alt="" src=images/Dot-line.svg  style="width:20px;"> Kropka, <img alt="" src=images/DashDot-line.svg  style="width:20px;"> Kreska kropka, <img alt="" src=images/DashDotDot-line.svg  style="width:20px;"> Kreska kropka kropka.


</div>



## Uwagi


<div class="mw-translate-fuzzy">

-   Funkcja Dodaj oś ściany ostatecznie zastąpi dwie właściwości widoku:
    -   
        **LniaŚrodkaPoziomo**
        
        : Pokazuje poziomą linię środkową w widoku.

    -   
        **LniaŚrodkaPionowo**
        
        : Pokazuje pionową linię środkową w widoku.


</div>

## Properties

Centerlines have no properties of their own, as they are not document objects.





{{TechDraw Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw FaceCenterLine/pl
