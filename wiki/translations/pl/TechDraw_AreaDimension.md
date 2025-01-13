---
 GuiCommand:
   Name: TechDraw AreaDimension
   Name/pl: Rysunek Techniczny: Wstaw adnotację obszaru
   MenuLocation: Rysunek Techniczny , Wymiary , Wstaw adnotację obszaru
   Workbenches: TechDraw_Workbench/pl
   Version: 1.0
   SeeAlso: TechDraw_ExtensionAreaAnnotation/pl
---

# TechDraw AreaDimension/pl



## Opis

Narzędzie **Wstaw adnotację obszaru** dodaje wymiar pola powierzchni do ściany w Widoku części.

![](images/TechDraw_AreaDimension_Example.png ) 
*Adnotacja obszaru ściany z otworem. Zobacz [Ograniczenia](#Limitations/pl.md).*



## Użycie

1.  Wybierz ścianę. Geometria może zostać wskazana w [widoku 3D](3D_view/pl.md) lub w obrębie rysunku.
2.  Jeśli wskazałeś geometrię w widoku 3D: dodaj poprawny Widok do wskazania poprzez zaznaczenie go w [widoku drzewa](Tree_view/pl.md).
3.  Istnieje kilka sposobów na wywołanie tego narzędzia:
    -   Jeśli [preferencja](TechDraw_Preferences/pl#Wymiary.md) **Narzędzie wymiarowania** jest ustawiona na {{Value|Narzędzie pojedyncze}} (domyślnie): kliknij strzałkę w dół po prawej stronie od przycisku **<img src="images/TechDraw_Dimension.svg" width=|x16px><img src="images/Toolbar_flyout_arrow.svg" width=x16px>** i wybierz opcję **<img src="images/TechDraw_AreaDimension.svg" width=16px> Wstaw adnotację obszaru** z listy rozwijanej.
    -   Jeśli ta preferencja ma inną wartość: wciśnij przycisk **<img src="images/TechDraw_AreaDimension.svg" width=16px> [Wstaw adnotację obszaru](TechDraw_AreaDimension/pl.md)**.
    -   Wybierz opcję **Rysunek Techniczny → Wymiary → <img src="images/TechDraw_AreaDimension.svg" width=16px> Wstaw adnotację obszaru** z menu.
4.  Wymiar zostanie dodany do widoku.
5.  Wymiar można przeciągnąć do żądanego położenia.
6.  Jeśli to potrzebne, dodaj tolerancje zgodnie z opisem na [tej stronie](TechDraw_Geometric_dimensioning_and_tolerancing/pl#Tolerancja.md).



## Ograniczenia

-    {{VersionMinus/pl|1.0}}: To narzędzie może wykrywać otwory (*wyspy*) tylko w ścianach wskazanych w widoku 3D. Aby uzyskać poprawne pole powierzchni dla takiej ściany zaznaczonej w obrębie rysunku, należy wykonać następujące czynności:

    1.  Ustawić poprawnie właściwość **References 3D** używając narzędzia ![\|x16px](images/TechDraw_DimensionRepair.svg ) [Napraw odniesienia do wymiarów](TechDraw_DimensionRepair/pl.md).
    2.  Zmienić właściwość **Measure Type** na {{Value|True}}.
    3.  Użyć narzędzia ![\|x16px](images/Std_Refresh.svg ) [Std: Przelicz](Std_Refresh/pl.md) jeśli to konieczne.





{{TechDraw_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw AreaDimension/pl
