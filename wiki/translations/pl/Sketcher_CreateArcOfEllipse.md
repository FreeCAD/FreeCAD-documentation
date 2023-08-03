---
 GuiCommand:
   Name: Sketcher CreateArcOfEllipse
   Name/pl: Szkicownik: Utwórz łuk na podstawie elipsy
   MenuLocation: Szkic , Elementy geometryczne szkicownika , Utwórz łuk na podstawie elipsy
   Workbenches: Sketcher_Workbench/pl
   Shortcut: **G** **E** **A**
   Version: 0.15
   SeeAlso: Sketcher_CreateEllipseByCenter/pl, Sketcher_CompCreateArc/pl
---

# Sketcher CreateArcOfEllipse/pl



## Opis

Narzędzie to rysuje łuk elipsy wybierając cztery punkty: środek, koniec promienia głównego, punkt początkowy i punkt końcowy. Po uruchomieniu narzędzia kursor myszki zmienia się w biały krzyż z czerwoną ikoną łuku elipsy. Poza tym wyświetlane są współrzędne w czasie rzeczywistym.

<img alt="" src=images/Sketcher_ArcOfEllipseExample1.png‎  style="width:500px;"> 
*Kolejność kliknięć wskazują żółte strzałki z numerami.<br>
'''C''' to środek, '''a''' średnica główna, '''b''' średnica mała, '''F1''' i '''F2''' to punkty centralne.*



## Użycie

-   Naciśnij przycisk **[<img src=images/Sketcher_CreateArcOfEllipse.svg style="width:16px"> '''Utwórz łuk na podstawie elipsy'''**.
-   Pierwsze kliknięcie w oknie widoku 3D ustawia środek elipsy. Drugie kliknięcie ustawia pierwszy promień i orientację elipsy. Trzecie kliknięcie ustawia drugi promień i początek łuku. Czwarte kliknięcie ustawia koniec łuku.
-   Po czwartym kliknięciu tworzony jest łuk elipsy wraz z zestawem geometrii konstrukcyjnych do niego dopasowanych *(średnica główna, średnica mniejsza, dwie ogniskowe)*. Geometria konstrukcyjna może być ręcznie usunięta, jeśli nie jest potrzebna, i odtworzona później. Zobacz [Pokaż / ukryj geometrię wewnętrzną](Sketcher_RestoreInternalAlignmentGeometry/pl.md).
-   Naciśnięcie **ESC** lub kliknięcie prawym przyciskiem myszy powoduje przerwanie funkcji.



## Szczególe cechy 

-   Główne i małe osie elipsy bazowej są stałe i nie mogą być zamienione przez zmianę rozmiaru. Bazowa elipsa musi zostać obrócona, aby zamienić osie.
-   W przeciwieństwie do elipsy, która może być związana do okręgu, łuk elipsy nie może reprezentować łuku okręgu.
-   Przesunięcie łuku elipsy o krawędź jest takie samo jak przesunięcie środka elipsy.





{{Sketcher Tools navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CreateArcOfEllipse/pl
