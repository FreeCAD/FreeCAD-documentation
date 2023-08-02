---
- GuiCommand:
   Name: Sketcher CreateEllipseByCenter
   Name/pl: Szkicownik: Utwórz elipsę przez środek
   MenuLocation: Szkic -> Elementy geometryczne szkicownika -> Utwórz elipsę przez środek
   Workbenches: Sketcher_Workbench/pl
   Shortcut: **G** **E** **E**
   Version: 0.15
   SeeAlso: Sketcher_CreateEllipseBy3Points/pl, Sketcher_CreateCircle/pl, Sketcher_CreateArcOfEllipse/pl
---

# Sketcher CreateEllipseByCenter/pl



## Opis

Narzędzie to rysuje elipsę wybierając trzy punkty: środek, koniec promienia głównego, promień mniejszy. Po uruchomieniu narzędzia kursor myszki przybiera kształt białego krzyża z czerwoną ikoną elipsy. Poza tym wyświetlane są współrzędne w czasie rzeczywistym.

<img alt="" src=images/Sketcher_EllipseExample1.png‎  style="width:500px;"> 
*Kolejność kliknięć wskazują żółte strzałki z numerami.<br>
'''C''' to środek, '''a''' średnica główna, '''b''' średnica mała, '''F1''' i '''F2''' to punkty centralne.*



## Użycie

-   Wywołaj polecenie klikając przycisk na pasku narzędzi, wybierając pozycję menu lub używając skrótu klawiaturowego *(musi być przypisany najpierw w [Dostosowanie interfejsu użytkownika](Interface_Customization/pl.md))*.
-   Pierwsze kliknięcie w oknie widoku 3D wyznacza środek elipsy. Drugie kliknięcie określa pierwszy promień i orientację elipsy. Trzecie kliknięcie określa drugi promień *(odległość od linii zdefiniowanej przez dwa pierwsze kliknięcia to drugi promień)*.
-   Po trzecim kliknięciu tworzona jest elipsa wraz z zestawem geometrii konstrukcyjnych do niej dopasowanych *(średnica główna, średnica mniejsza, dwa ogniska)*. Geometria konstrukcyjna może być ręcznie usunięta, jeśli nie jest potrzebna, i odtworzona później. Zobacz [Pokaż / ukryj geometrię wewnętrzną](Sketcher_RestoreInternalAlignmentGeometry/pl.md).
-   Naciśnięcie **ESC** lub kliknięcie prawym przyciskiem myszy powoduje przerwanie funkcji.



## Szczególe cechy 

-   Osie główne i mniejsze elipsy są sztywno określone i nie mogą być zamienione przez zmianę rozmiaru elipsy. Jest to konsekwencją zastosowanej parametryzacji solwera *(środek (x,y), ogniskowa1 (x,y) i długość promienia mniejszego (b))* oraz tego samego zachowania ścisłego OpenCascade. Elipsa musi być obrócona, aby zamienić osie.
-   Elipsa może funkcjonować jako koło, gdy jej linie średnicy głównej i mniejszej są usuwane, a jedno z ognisk jest związane, aby pokryć się ze środkiem. Ale wiązanie promienia nie będzie działać na takim okręgu.
-   Przesuwanie elipsy po krawędzi jest takie samo jak przesuwanie jej środka.





{{Sketcher Tools navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CreateEllipseByCenter/pl
