---
 GuiCommand:
   Name: Sketcher CreateEllipseByCenter
   Name/pl: Szkicownik: Utwórz elipsę przez środek
   MenuLocation: Szkic , Elementy geometryczne szkicownika , Utwórz elipsę przez środek
   Workbenches: Sketcher_Workbench/pl
   Shortcut: **G** **E** **E**
   Version: 0.15
   SeeAlso: Sketcher_CreateArcOfEllipse/pl
---

# Sketcher CreateEllipseByCenter/pl



## Opis

Narzędzie <img alt="" src=images/Sketcher_CreateEllipseByCenter.svg  style="width:24px;"> **Utwórz elipsę przez środek** tworzy elipsę na podstawie jej środka. {{Version/pl|1.0}}: Lub opcjonalnie przez oba punkty końcowe jednej z osi i punkt wzdłuż elipsy.

![](images/Sketcher_CreateEllipseByCenter_Example.png ) 
*Elipsa ''(biała)'' z wewnętrzną geometrią ''(ciemnożółta)''.*



## Użycie

Zapoznaj się również z informacjami na stronie [Pomoce kreślarskie](Sketcher_Workbench/pl#Pomoce_kreślarskie.md).

Pos-OVP = Pozycyjne [Parametry w widoku](Sketcher_Preferences#Ogólne/pl.md). {{Version/pl|1.0}}
Dim-OVP = Wymiarowe parametry w widoku. {{Version/pl|1.0}}

1.  Istnieje kilka sposobów wywołania narzędzia:
    -   Naciśnij przycisk **<img src="images/Sketcher_CreateEllipseByCenter.svg" width=16px> '''Elipsa przez środek, promień, punkt na obwodzie'''**.
    -   Wybierz z menu **Szkic → Elementy geometryczne szkicownika → <img src="images/Sketcher_CreateEllipseByCenter.svg" width=16px> Elipsa przez środek, promień, punkt na obwodzie**.
    -   Użyj skrótu klawiaturowego: **G**, następnie **E**, a następnie **E**.
2.  Kursor zmieni się w krzyżyk z ikoną bieżącego trybu narzędzia.
3.  Sekcja **Parametry elipsy** *({{Version/pl|1.0}})* jest dodawana na górze [okna dialogowego](Sketcher_Dialog/pl.md).
4.  Opcjonalnie naciśnij klawisz **M** lub wybierz z rozwijanej listy w sekcji parametrów, aby zmienić tryb narzędzia:
    -   <img alt="" src=images/Sketcher_CreateEllipseByCenter.svg  style="width:16px;"> **Center**:
        1.  Wybierz środek elipsy. Lub z Pos-OVP: wprowadź jego współrzędne X i / lub Y.
        2.  Wybierz punkt końcowy jednej z osi elipsy, który definiuje również jeden z jej promieni. Lub za pomocą Dim-OVP: wprowadź ten promień i / lub kąt tej osi.
        3.  Wybierz punkt definiujący drugi promień elipsy. Lub za pomocą Dim-OVP: wprowadź ten promień.
    -   <img alt="" src=images/Sketcher_CreateEllipseBy3Points.svg  style="width:16px;"> **Punkty końcowe osi**: {{Version/pl|1.0}}
        1.  Wybierz punkty końcowe jednej z osi elipsy, która definiuje również jeden z jej promieni. Lub za pomocą Pos-OVP: wprowadź ich współrzędne X i / lub Y. Dla tych punktów nie są tworzone żadne wiązania.
        2.  Wybierz punkt definiujący drugi promień elipsy. Lub za pomocą Pos-OVP: wprowadź jego współrzędne X i / lub Y. Dla tego punktu nie zostanie utworzone żadne wiązanie.
5.  Tworzona jest elipsa, w tym zestaw geometrii wewnętrznej *(oś główna, oś pomocnicza i dwa ogniska)*, a także dodawane są odpowiednie ograniczenia oparte na Pos-OVP i Dim-OVP.
6.  Jeśli narzędzie działa w [trybie kontynuacji](Sketcher_Workbench/pl#Tryby_kontynuacji.md):
    1.  Opcjonalnie kontynuuj tworzenie elips.
    2.  Aby zakończyć, kliknij prawym przyciskiem myszy lub naciśnij **Esc**, lub uruchom inne narzędzie do tworzenia geometrii lub wiązań.



## Uwagi

-   Elementy geometrii wewnętrznej mogą zostać usunięte. Można je odtworzyć w dowolnym momencie za pomocą narzędzia [Pokaż / ukryj geometrię wewnętrzną](Sketcher_RestoreInternalAlignmentGeometry/pl.md).
-   Po utworzeniu, główne i pomocnicze osie elipsy są ściśle określone i nie można ich zamienić poprzez zmianę rozmiaru. Jest to konsekwencja parametryzacji solvera i tego samego ścisłego zachowania [OpenCASCADE](OpenCASCADE/pl.md). Elipsa musi zostać obrócona, aby zamienić jej osie.





{{Sketcher Tools navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CreateEllipseByCenter/pl
