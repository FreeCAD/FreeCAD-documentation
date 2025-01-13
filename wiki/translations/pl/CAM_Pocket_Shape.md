---
 GuiCommand:
   Name: CAM Pocket Shape
   Name/pl: CAM: Obróbka kieszeni
   MenuLocation: CAM , Obróbka kieszeni
   Workbenches: CAM_Workbench/pl
---

# CAM Pocket Shape/pl



## Opis

Narzędzie <img alt="" src=images/CAM_Pocket_Shape.svg  style="width:16px;"> [Obróbka kieszeni](CAM_Pocket_Shape/pl.md) tworzy operację wycinania kieszeni z wybranych dolnych lub bocznych ścian jednej lub większej liczby kieszeni z obiektu bazowego zadania.

Obiekt CAM Pocket Shape jest dodawany jako część <img alt="" src=images/CAM_Job.svg  style="width:24px;"> [Zadania CAM](CAM_Job/pl.md).

<img alt="" src=images/Path_Pocket_Shape_example.png  style="width:600px;">



## Użycie

1.  Wybierz dno lub ściany kieszeni. Zazwyczaj łatwiej jest wybrać dno, ale gdy kieszeń przechodzi na wylot, należy wybrać ściany.
2.  Istnieje kilka sposobów na wywołanie polecenia:
    -   Naciśnij przycisk **<img src="images/CAM_Pocket_Shape.svg" width=16px> [ Obróbka kieszeni](CAM_Pocket_Shape/pl.md)**.
    -   Wybierz opcję **CAM → <img src="images/CAM_Pocket_Shape.svg" width=16px> Obróbka kieszeni** z menu.
3.  Dostosuj żądane właściwości.



## Właściwości

***Uwaga***: Nie wszystkie z tych właściwości są dostępne w edytorze okna zadań. Niektóre są dostępne tylko na karcie Dane w panelu Widok właściwości dla tej operacji.


{{TitleProperty|Podstawa}}

Uwaga: Zaleca się, aby nie edytować właściwości Umiejscowienie operacji ścieżki. W razie potrzeby należy raczej przesunąć lub obrócić model zadania CAM.

-    **Placement**: Ogólne umiejscowienie \[położenie i rotacja\] obiektu względem początku (lub początku kontenera obiektów nadrzędnych)

    -   
        **Angle**
        
        : Kąt w stopniach zastosowany do rotacji obiektu wokół wartości właściwości Axis

    -   
        **Axis**
        
        : Oś (jedna lub wiele), wokół której ma być obracany obiekt, ustawiona w podwłaściwościach: X, Y, Z

        -   
            **X**
            
            : Wartość osi X

        -   
            **Y**
            
            : Wartość osi Y

        -   
            **Z**
            
            : Wartość osi Z

    -   
        **Position**
        
        : Położenie obiektu, ustawione w podwłaściwościach: X, Y, Z - względem początku (lub początku kontenera obiektów nadrzędnych)

        -   
            **X**
            
            : Wartość odległości X

        -   
            **Y**
            
            : Wartość odległości Y

        -   
            **Z**
            
            : Wartość odległości Z

-    **Label**: Nazwa obiektu nadana przez użytkownika (UTF-8)


{{TitleProperty|Głębokość}}

-    **Clearance Height**: Wysokość potrzebna do usunięcia zacisków i przeszkód

-    **Final Depth**: Końcowa głębokość narzędzia - najniższa wartość w osi Z

-    **Finish Depth**: Maksymalna ilość materiału usuniętego podczas ostatniego przejścia. Wysokość (grubość) ostatniego poziomu cięcia - *ustawiana dla lepszego wykończenia*.

-    **Safe Height**: Wysokość, powyżej której dozwolone są ruchy szybkie. (Bezpieczna wysokość szybkiego ruchu między lokalizacjami)

-    **Start Depth**: Początkowa głębokość narzędzia - *pierwsza głębokość cięcia w osi Z*

-    **Step Down**: Przyrostowa głębokość cięcia narzędzia podczas operacji

<img alt="" src=images/Path-DepthsAndHeights.gif  style="width:500px;"> 
*Wizualne odniesienie do właściwości ''(ustawień)'' głębokości*


{{TitleProperty|Przedłużenie}}

-    **Extension Corners**: Po włączeniu połączone krawędzie przedłużenia są łączone w przewody.

-    **Extension Length Default**: Domyślna długość przedłużeń.


{{TitleProperty|Ściana}}

-    **Offset Pattern**: Wzór czyszczenia do użycia. (Wybierz sposób, w jaki mają być wykonywane ruchy poziome.)


{{TitleProperty|Ścieżka}}

-    **Active**: Ustaw na False, aby zapobiec generowaniu kodu operacji

-    **Comment**: Opcjonalny komentarz do tej operacji

-    **User Label**: Etykieta przypisana przez użytkownika

-    **Tool Controller**: Definiuje kontroler narzędzia używanego w operacji


{{TitleProperty|Kieszeń}}

-    **Cut Mode**: Określa ruch CW lub CCW dla cięcia

-    **Extra Offset**: Dodatkowe odsunięcie do zastosowania w operacji. Kierunek zależy od operacji. (Dodatkowa wartość dla unikania końcowego profilu *dobre dla ścieżki zgrubnej*)

-    **Keep Tool Down**: Próbuje unikać niepotrzebnych wycofań.

-    **Min Travel**: Użyj sortowania 3D ścieżki (gdy używane są wielokrotne geometrie bazowe).

-    **Start At**: Rozpocznij frezowanie kieszeni od środka lub krawędzi.

-    **Step Over**: Wybierz poziome przesunięcie (**Procent** średnicy narzędzia: 100% = średnica narzędzia).

-    **Use Outline**: Używa konturu geometrii bazowej.

-    **Zig Zag Angle**: Kąt wzoru zygzakowatego. (Wybierz kąt ścieżki względem osi X.)


{{TitleProperty|Obrót}}

-    **Attempt Inverse Angle**: Automatycznie spróbuj odwrócić kąt, jeśli początkowy obrót jest niepoprawny.

-
-    **Enable Rotation**: Włącz obroty, aby uzyskać dostęp do otworów nieprostopadłych do osi Z.

-    **Inverse Angle**: Odwróć kąt obrotu. ***Przykład:** zmiana obrotu z -22,5 na 22,5 stopnia.*

-    **Reverse Direction**: Odwróć orientację operacji o 180 stopni.


{{TitleProperty|Punkt początkowy}}

-    **Start Point**: Punkt startowy tej ścieżki.

-    **Use Start Point**: Ustaw na True, jeśli ręcznie określasz Punkt Startowy, a następnie wprowadź Punkty Startowe w polu danych właściwości Start Points.



## Układ edytora w oknie zadań 

*Opisy ustawień znajdują się na powyższej liście właściwości*.

Ta sekcja jest po prostu mapą układu ustawień w edytorze okien dla operacji.



### Geometria podstawowa 

-   **Dodaj**: Dodaje wybrane elementy, które powinny być bazą dla ścieżek.
-   **Usuń**: Usuwa wybrane elementy z listy Geometria podstawowa.
-   **Wyczyść**: Czyści wszystkie elementy na liście Geometria podstawowa.



### Rozszerzenia

-    **Show All**: Jeśli wybrane, wszystkie potencjalne przedłużenia są wizualizowane. Włączone przedłużenia w kolorze fioletowym, wyłączone przedłużenia w kolorze żółtym.

-    **Extension Corners**
    

-    **Extension Length Default**
    

-   **Enable**

-   **Disable**

-   **Clear**



### Głębokości

-    **Start Depth**
    

-    **Final Depth**
    

-    **Step Down**
    



### Wysokości

-    **Safe Height**
    

-    **Clearance Height**
    



### Operacja

-    **Tool Controller**
    

-    **Cut Mode**
    

-    **Pattern**(Wzór przesunięcia)

-    **Angle**(Kąt zygzakowania)

-    **Step Over Percent**(Przesunięcie)

-    **Pass Extension**: Odległość, na jaką operacja frezowania będzie sięgać poza kształt graniczny (geometrię podstawową)



## Tworzenie skryptów 


**Zobacz również:**

[FreeCAD podstawy tworzenia skryptów](FreeCAD_Scripting_Basics/pl.md).


```python
#Place code example here.
```





{{CAM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [CAM](CAM_Workbench.md) > CAM Pocket Shape/pl
