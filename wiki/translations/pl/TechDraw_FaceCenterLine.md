---
 GuiCommand:
   Name: TechDraw FaceCenterLine
   Name/pl: Rysunek Techniczny: Dodaj oś ściany
   MenuLocation: Rysunek Techniczny , Dodaj linie , Dodaj oś ściany
   Workbenches: TechDraw_Workbench/pl
   Version: 0.19
   SeeAlso:  TechDraw_2LineCenterLine/pl, TechDraw_2PointCenterLine/pl
---

# TechDraw FaceCenterLine/pl



## Opis

Narzędzie **Dodaj oś ściany** dodaje linię środkową do wybranych ścian.

<img alt="" src=images/TechDraw_FaceCenterLine_Sample.png  style="width:400px;"> 
*Oś dodana do ściany.*



## Użycie

1.  Wybierz jedną lub więcej ścian w widoku.
2.  Istnieje kilka sposobów wywołania narzędzia:
    -   Naciśnij przycisk **<img src="images/TechDraw_FaceCenterLine.svg" width=16px> Dodaj oś ściany**.
    -   Wybierz opcję z menu **Rysunek Techniczny → Dodaj linie → <img src="images/TechDraw_FaceCenterLine.svg" width=16px> Dodaj oś ściany**.
3.  Otworzy się panel zadań. Więcej informacji znajduje się w sekcji [Opcje](#Opcje.md).
4.  Naciśnij przycisk **OK**, aby potwierdzić.
5.  Linia środkowa zostanie dodana w punkcie środkowym obwiedni wybranych powierzchni.



## Edycja

Dowolne narzędzie poleceń linii środkowej *(**<img src="images/TechDraw_FaceCenterLine.svg" width=16px> Dodaj oś ściany**, **<img src="images/TechDraw_2LineCenterLine.svg" width=16px> [Dodaj oś pomiędzy dwiema liniami](TechDraw_2LineCenterLine/pl.md)**, **<img src="images/TechDraw_2PointCenterLine.svg" width=16px> [Dodaj oś pomiędzy dwoma punktami](TechDraw_2PointCenterLine/pl.md)**)* może zostać uzyte do edycji dowolnej z linii środkowej.

1.  Wybierz linię środkową.
2.  Wywołaj narzędzie linii środkowej.
3.  Otworzy się okno dialogowe, w którym można zmienić atrybuty linii środkowej.
4.  Naciśnij **OK**, aby potwierdzić.



## Opcje

-   Tryb (przyciski wyboru):
    -   **Pionowo**: wymusza pionową linię środkową. Ignorowane w przypadku narzędzia *Dodaj oś pomiędzy dwoma punktami*.
    -   **Poziomo**: Wymusza linię środkową w poziomie. Ignorowane w przypadku narzędzia *Dodaj oś pomiędzy dwoma punktami*.
    -   **Wyrównane**: Ta opcja nie jest możliwa w przypadku linii środkowej do ściany.
-   **Przesuń w poziomie**: Przesuwa linię środkową w lewo lub w prawo od jej normalnego położenia.
-   **Przesuń w pionie**: Przesuwa linię środkową w górę lub w dół od jej normalnego położenia.
-   **Obróć**: Obraca linię środkową wokół jej środka *(stopnie. + przeciwnie do ruchu wskazówek zegara, - zgodnie z ruchem wskazówek zegara)*.
-   **Rozszerz o**: Wydłuża linię środkową o podaną wartość.
-   **Kolor**: Kolor linii środkowej.
-   **Grubość**: Grubość linii środkowej.
-   **Styl**: Styl linii środkowej. Dostępne opcje to:
    -   <img alt="" src=images/Continuous-line.svg  style="width:20px;"> Ciągła,
    -   <img alt="" src=images/Dash-line.svg  style="width:20px;"> Kreska,
    -   <img alt="" src=images/Dot-line.svg  style="width:20px;"> Kropka,
    -   <img alt="" src=images/DashDot-line.svg  style="width:20px;"> Kreska kropka,
    -   <img alt="" src=images/DashDotDot-line.svg  style="width:20px;"> Kreska kropka kropka.



## Uwagi

-   Aby usunąć linię środkową użyj narzędzia <img alt="" src=images/TechDraw_CosmeticEraser.svg  style="width:16px;"> [Usuń geomertie pomocnicze](TechDraw_CosmeticEraser/pl.md).
-   Funkcja Dodaj oś ściany ostatecznie zastąpi dwie właściwości widoku:
    -   
        **LniaŚrodkaPoziomo**
        
        : Pokazuje poziomą linię środkową w widoku.

    -   
        **LniaŚrodkaPionowo**
        
        : Pokazuje pionową linię środkową w widoku.



## Właściwości

Linie środka nie mają własnych właściwości, ponieważ nie są obiektami dokumentu.





{{TechDraw Tools navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw FaceCenterLine/pl
