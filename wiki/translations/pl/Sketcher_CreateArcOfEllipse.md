---
 GuiCommand:
   Name: Sketcher CreateArcOfEllipse
   Name/pl: Szkicownik: Utwórz łuk na podstawie elipsy
   MenuLocation: Szkic , Elementy geometryczne szkicownika , Utwórz łuk na podstawie elipsy
   Workbenches: Sketcher_Workbench/pl
   Shortcut: **G** **E** **A**
   Version: 0.15
   SeeAlso: Sketcher_CreateEllipseByCenter/pl
---

# Sketcher CreateArcOfEllipse/pl



## Opis

Narzędzie <img alt="" src=images/Sketcher_CreateArcOfEllipse.svg  style="width:24px;"> **Utwórz łuk na podstawie elipsy** narzędzie tworzy łuk elipsy.

![](images/Sketcher_CreateArcOfEllipse_Example.png ) 
*Łuk elipsy ''(biały)'' z wewnętrzną geometrią ''(ciemnożółta)''.*



## Użycie

Zapoznaj się również z informacjami na stronie [Pomoce kreślarskie](Sketcher_Workbench/pl#Pomoce_kreślarskie.md).

1.  Istnieje kilka sposobów wywołania narzędzia:
    -   Naciśnij przycisk **<img src="images/Sketcher_CreateArcOfEllipse.svg" width=16px> '''Łuk elipsy przez środek, promień, punkty końcowe'''**.
    -   Wybierz z menu opcję **Szkic → Elementy geometryczne szkicownika → <img src="images/Sketcher_CreateArcOfEllipse.svg" width=16px> Utwórz łuk na podstawie elipsy**.
    -   Użyj skrótu klawiaturowego: **G**, **E**, **A**.
2.  Kursor zmieni się w krzyżyk z ikoną narzędzia.
3.  Wybierz środek łuku.
4.  Wybierz punkt końcowy jednej z osi łuku, który definiuje również jeden z jego promieni.
5.  Wybierz punkt początkowy łuku, który definiuje także drugi promień łuku.
6.  Wybierz punkt końcowy łuku.
7.  Zostanie utworzony łuk elipsy, zawierający zestaw wewnętrznej geometrii *(oś główna, oś pomocnicza i dwa ogniska)*.
8.  Jeśli narzędzie działa w [trybie kontynuacji](Sketcher_Workbench/pl#Tryby_kontynuacji.md):
    1.  Opcjonalnie kontynuuj tworzenie łuków.
    2.  Aby zakończyć, kliknij prawym przyciskiem myszy lub naciśnij **Esc**, lub uruchom inne narzędzie do tworzenia geometrii lub wiązań.



## Uwagi

-   Elementy geometrii wewnętrznej mogą zostać usunięte. Można je odtworzyć w dowolnym momencie za pomocą narzędzia [Pokaż / ukryj geometrię wewnętrzną](Sketcher_RestoreInternalAlignmentGeometry/pl.md).
-   Po utworzeniu, główne i pomocnicze osie elipsy są ściśle określone i nie można ich zamienić poprzez zmianę rozmiaru. Jest to konsekwencja parametryzacji solvera i tego samego ścisłego zachowania [OpenCASCADE](OpenCASCADE/pl.md). Łuk elipsy musi zostać obrócony, aby zamienić jego osie.





{{Sketcher Tools navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CreateArcOfEllipse/pl
