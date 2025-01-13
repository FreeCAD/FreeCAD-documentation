---
 GuiCommand:
   Name: CAM MillFace
   Name/pl: CAM: Powierzchnia
   MenuLocation: CAM , Powierzchnia
   Workbenches: CAM_Workbench/pl
---

# CAM MillFace/pl



## Opis

Narzędzie <img alt="" src=images/CAM_MillFace.svg  style="width:24px;"> [Powierzchnia](CAM_MillFace/pl.md) tworzy ścieżkę do przeprowadzenia operacji frezowania na poziomej powierzchni. Ta operacja jest zazwyczaj używana:

-   do wygładzenia szorstkiej powierzchni materiału,
-   do frezowania wybranej powierzchni do żądanej głębokości w celu przygotowania do dalszych operacji usuwania w obrębie obszarów objętych tą operacją,
-   lub do zastosowania wykończenia na wybranej powierzchni.

Operacja ta zawiera właściwość **BoundaryShape**, która pozwala na zmodyfikowany wybór obszaru na podstawie wybranej powierzchni.

<img alt="Przykład operacji Powierzchnia używanej do przygotowania powierzchni materiału do dalszych operacji usuwania." src=images/MillFace_Sample.png  style="width:600px;">



## Użycie

1.  Wybierz jedną lub więcej powierzchni do frezowania. **Uwaga:** Jeśli wybrane powierzchnie znajdują się na różnych wysokościach, wszystkie zostaną frezowane do ustawionej wartości Głębokości końcowej.
2.  Istnieje kilka sposobów na wywołanie tego polecenia:
    -   Naciśnij przycisk **<img src="images/CAM_MillFace.svg" width=16px> [Powierzchnia](CAM_MillFace/pl.md)**.
    -   Wybierz opcję **CAM → <img src="images/CAM_MillFace.svg" width=16px> Powierzchnia** z menu.
3.  Wybierz odpowiednie ustawienie **Kształ granicy**, aby zmodyfikować obszar frezowania na podstawie powierzchni wybranych jako **Geometria podstawowa**.
4.  Dostosuj pozostałe właściwości w razie potrzeby. Są one opisane poniżej.



## Zastrzeżenia

-   Użycie tej operacji na nachylonej powierzchni może prowadzić do nieoczekiwanych rezultatów: nadal będzie ona tworzyć ścieżkę do frezowania poziomej powierzchni. Zakres cięcia będzie odpowiadał pionowej projekcji nachylonej powierzchni, realizowanej na wysokości odpowiadającej najniższemu punktowi tej powierzchni.

-   Ponieważ narzędzia CAM działają tylko na geometrii wybranych krawędzi/powierzchni i nie odnoszą się do reszty modelu 3D, ścieżki nie wyjdą poza granice wybranej płaszczyzny, nawet jeśli jest otoczona nieużywaną częścią materiału lub powietrzem. Może to pozostawić niedopracowane narożniki. Czasami można je usunąć za pomocą jednego z narzędzi do obróbki, które znajdują się w menu *CAM*.



## Frezowanie ścian pionowych 

-   To nie działa na **pionowej płaszczyźnie** lub pionowej powierzchni zakrzywionej. Operacje pionowe można osiągnąć, używając narzędzia [Kontur](CAM_Profile/pl.md) lub [Kontur](CAM_Profile/pl.md). Należy wybrać powierzchnię lub zamkniętą pętlę krawędzi *w tym górną lub dolną krawędź żądanej pionowej powierzchni*). Zakres ścieżki można następnie ograniczyć za pomocą narzędzia [Ulepszenie ścieżki konturu](CAM_DressupPathBoundary/pl.md), które znajduje się w menu *CAM*. Użyj opcji *Utwórz prostopadłościan* i zmniejsz rozmiar, aby ograniczyć zakres ścieżki profilu. Ustawienia te nie pozwolą jednak na przesunięcie początku ramki ograniczającej; należy to zrobić, dostosowując ustawienia Umiejscowienia w [widoku drzewa](Tree_view/pl.md).
-   Działa to na powierzchniach złożonych, takich jak kilka pionowych płaszczyzn lub powierzchni cylindrycznych połączonych razem, pod warunkiem, że tworzą one jedną ciągłą powierzchnię.



## Opcje

Pusto



## Właściwości

***Uwaga***: Nazwy niektórych właściwości na tej liście różnią się nieco od tych samych ustawień używanych w edytorze okna dialogowego.



### Dane


{{TitleProperty|Podstawa}}

Uwaga: Zaleca się, aby nie edytować właściwości Umiejscowienie operacji ścieżki. W razie potrzeby należy raczej przesunąć lub obrócić model zadania CAM.

-    **Placement**: Ogólne umiejscowienie \[pozycja i rotacja\] obiektu - w odniesieniu do początku (lub początku kontenera obiektu nadrzędnego)

    -   
        **Angle**
        
        : Kąt w stopniach zastosowany do rotacji obiektu wokół wartości właściwości Axis

    -   
        **Axis**
        
        : Oś (jedna lub wiele), wokół której rotuje obiekt, ustawiana w podwłaściwościach: X, Y, Z

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
        
        : Pozycja obiektu, ustawiana w podwłaściwościach: X, Y, Z - w odniesieniu do początku (lub początku kontenera obiektu nadrzędnego)

        -   
            **X**
            
            : Wartość odległości X

        -   
            **Y**
            
            : Wartość odległości Y

        -   
            **Z**
            
            : Wartość odległości Z

-    **Label**: Nazwa obiektu podana przez użytkownika (UTF-8)


{{TitleProperty|Głębokość}}

-    **Clearance Height**: Wysokość potrzebna do usunięcia zacisków i przeszkód

-    **Final Depth**: Ostateczna głębokość narzędzia - najniższa wartość w osi Z

-    **Finish Depth**: Maksymalna ilość materiału usuwanego podczas ostatniego przejazdu

-    **Safe Height**: Wysokość powyżej której dozwolone są szybkie ruchy

-    **Start Depth**: Początkowa głębokość narzędzia - pierwsza głębokość cięcia w osi Z

-    **Step Down**: Stopniowe zagłębianie narzędzia


{{TitleProperty|Ściana}}

-    **BoundaryShape**: Kształt używany do obliczania granicy

-    **ClearEdges**: Oczyść krawędzie powierzchni (Dotyczy tylko BoundBox)

-    **ExcludeRaisedAreas**: Wyklucz frezowanie podniesionych obszarów wewnątrz powierzchni.

-    **Offset Pattern**: Wzór czyszczenia do użycia. (Wybierz sposób wykonywania ruchów poziomych.)


{{TitleProperty|Ścieżka}}

-    **Active**: Ustaw na False, aby zapobiec generowaniu kodu dla operacji

-    **Base**: Geometria podstawowa dla tej operacji

-    **Comment**: Opcjonalny komentarz dla tej operacji

-    **Coolant Mode**: Tryb chłodzenia dla tej operacji

-    **Cycle Time**: Szacowany czas cyklu dla tej operacji

-    **Tool Controller**: Definiuje kontroler narzędzia używany w operacji

-    **User Label**: Etykieta przypisana przez użytkownika


{{TitleProperty|Kieszeń}}

-    **Cut Mode**: Kierunek, w którym ścieżka narzędzia powinna okrążać część: zgodnie z ruchem wskazówek zegara (CW) lub przeciwnie do ruchu wskazówek zegara (CCW)

-    **Extra Offset**: Dodatkowe odsunięcie do zastosowania w operacji. Kierunek zależy od operacji.

-    **StartAt**: Rozpocznij frezowanie od środka lub od krawędzi

-    **Step Over**: Procent średnicy narzędzia do przeskoku na każdej przejściu

-    **Zig Zag Angle**: Kąt wzoru zygzaka

-    **Offset Pattern**: Wzór wykańczania do użycia

-    **Min Travel**: Użyj sortowania 3D ścieżki

-    **Keep Tool Down**: Próbuje uniknąć zbędnych wycofań


{{TitleProperty|Obrót}}

-    **Attempt Inverse Angle**: Automatycznie spróbuj odwrócić kąt, jeśli początkowy kąt obrotu jest niepoprawny.

-    **Enable Rotation**: Włącz obrót, aby uzyskać dostęp do kieszeni lub obszarów, które nie są normalne do osi Z.

-    **Inverse Angle**: Odwróć kąt obrotu. ***Przykład:** zmień kąt obrotu z -22,5 na 22,5 stopnia.*

-    **Limit Depth To Face**: Wymuś głębokość Z wybranej powierzchni jako najniższą wartość dla końcowej głębokości. Wyższe wartości użytkownika dla głębokości końcowej będą uwzględniane.

-    **Reverse Direction**: Odwróć orientację operacji o 180 stopni.


{{TitleProperty|Punkt początkowy}}

-    **Start Point**: Niestandardowy punkt początkowy ścieżki tej operacji.

    -   
        **X**
        
        : Wartość odległości w osi X

    -   
        **Y**
        
        : Wartość odległości w osi Y

    -   
        **Z**
        
        : Wartość odległości w osi Z

-    **Use Start Point**: Ustaw na True, jeśli ręcznie określasz punkt początkowy. Ustaw punkt początkowy w polu danych właściwości Start Point.



### Widok

Pusto



## Tworzenie skryptów 


**Zobacz również:**

[FreeCAD podstawy tworzenia skryptów](FreeCAD_Scripting_Basics/pl.md).

Przykład:


```python
#Place code example here.
```





{{CAM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [CAM](CAM_Workbench.md) > CAM MillFace/pl
