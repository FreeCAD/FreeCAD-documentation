---
 GuiCommand:
   Name: TechDraw ExtensionAreaAnnotation
   Name/pl: Rysunek Techniczny: Rozszerzenie Oblicz obszar wybranych powierzchni
   MenuLocation: Rysunek Techniczny , Rozszerzenie: Atrybuty / Modyfikatory , Oblicz obszar wybranych powierzchni
   Workbenches: TechDraw_Workbench/pl
   Shortcut: 
   Version: 0.20
   SeeAlso: TechDraw_AreaDimension/pl
---

# TechDraw ExtensionAreaAnnotation/pl



## Opis

Narzędzie **Oblicz obszar wybranych powierzchni** oblicza obszar wybranych powierzchni i wstawia informację w postaci adnotacji o obszarze.

<img alt="" src=images/TechDraw_ExtensionAreaAnnotationExample.png  style="width:400px;"> 
*Po prawej stronie widoczna jest adnotacja o zaznaczonym obszarze.*



## Użycie

1.  Wybierz jedną lub więcej powierzchni.
2.  Istnieje kilka sposobów wywołania narzędzia:
    -   Naciśnij przycisk **<img src="images/TechDraw_ExtensionAreaAnnotation.svg" width=16px> '''Oblicz obszar wybranych powierzchni'''**.
    -   Wybierz opcję z menu **Rysunek Techniczny → Rozszerzenia: Atrybuty / Modyfikatory → <img src="images/TechDraw_ExtensionAreaAnnotation.svg" width=16px> Oblicz obszar wybranych powierzchni**.
3.  Zostanie obliczany całkowity obszar wybranej powierzchni i wstawiona adnotacja.



## Ograniczenia

-    {{VersionMinus/pl|0.21}}: Narzędzie nie radzi sobie z powierzchniami o zakrzywionych krawędziach.

-   Otwory (*wyspy*) we wskazanych ścianach są ignorowane. [Ten wątek na forum](https://forum.freecad.org/viewtopic.php?p=783325#p783325) pokazuje obejście. Można również użyć narzędzia [Wstaw adnotację obszaru](TechDraw_AreaDimension/pl.md), ale trzeba wtedy prawidłowo ustawić właściwość **References 3D** utworzonego wymiaru.

-   Obliczona powierzchnia nie jest dynamicznie powiązana ze ścianą. Jeśli powierzchnia ściany się zmieni, tekst nie zostanie zaktualizowany.





{{TechDraw_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw ExtensionAreaAnnotation/pl
