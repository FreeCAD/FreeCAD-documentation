---
 GuiCommand:
   Name: TechDraw 3PtAngleDimension
   Name/pl: Rysunek Techniczny: Wstaw trzy punktowy wymiar kąta
   MenuLocation: Rysunek Techniczny , Wymiary , Wstaw trzy punktowy wymiar kąta
   Workbenches: TechDraw_Workbench/pl
   Version: 0.18
   SeeAlso: TechDraw_AngleDimension/pl
---

# TechDraw 3PtAngleDimension/pl



## Opis

Narzędzie **Wstaw trzy punktowy wymiar kąta** dodaje wymiar kąta do widoku. Wymiar pokazuje kąt wewnętrzny między trzema punktami.

<img alt="" src=images/TechDraw_Dimension_Angle3Pt_example.png  style="width:200px;"> 
*Pomiar kąta między trzema punktami.*



## Użycie

1.  Wybierz punkty lub krawędzie, które definiują pomiar.
2.  Jeśli zaznaczyłeś geometrię w widoku 3D: dodaj właściwy widok Rysunku Technicznego do zaznaczenia, wybierając go w oknie [Widoku drzewa](Tree_view/pl.md).
3.  Istnieje kilka sposobów wywołania tego narzędzia:
    -   
        {{Version/pl|1.0}}
        
        : Jeśli [preferencja](TechDraw_Preferences/pl#Wymiary.md) **Narzędzie wymiarowania** jest ustawiona na {{Value|Narzędzie pojedyncze}} (domyślnie): kliknij na strzałce skierowanej w dół po prawej stronie od przycisku **<img src="images/TechDraw_Dimension.svg" width=|x16px><img src="images/Toolbar_flyout_arrow.svg" width=x16px>** i wybierz opcję **<img src="images/TechDraw_3PtAngleDimension.svg" width=16px> Wstaw trzy punktowy wymiar kąta** z listy rozwijanej.

    -   Jeśli ta preferencja ma inną wartość (i {{VersionMinus/pl|0.21}}): wciśnij przycisk **<img src="images/TechDraw_3PtAngleDimension.svg" width=16px> [Wstaw trzy punktowy wymiar kąta](TechDraw_3PtAngleDimension/pl.md)**.

-   Wybierz opcję z menu **Rysunek Techniczny → Wymiary → <img src="images/TechDraw_3PtAngleDimension.svg" width=16px> Wstaw trzy punktowy wymiar kąta**.

1.  Do widoku zostanie dodany wymiar.
2.  Wymiar można przeciągnąć do żądanej pozycji.
3.  Jeśli to konieczne, dodaj tolerancje, jak opisano na stronie [Wymiarowanie geometrii i tolerancja](TechDraw_Geometric_dimensioning_and_tolerancing/pl#Tolerancja.md).



### Wyświetlanie pomiarów 3D 

Zapoznaj się również z informacjami na stronie [Wstaw wymiar długości](TechDraw_LengthDimension/pl#Wyświetlanie_pomiarów_3D.md)



### Zmiana właściwości 

Aby zmienić właściwości obiektu wymiaru, kliknij dwukrotnie na niego w rysunku lub w [widoku drzewa](Tree_view/pl.md). Spowoduje to otwarcie okna [dialogowego wymiaru](TechDraw_LengthDimension/pl#Okno_dialogowe.md).



## Ograniczenia

Obiekty wymiarowe są podatne na \"[problem nazewnictwa topologicznego](Topological_naming_problem/pl.md)\". Zobacz stronę [Wstaw wymiar długości](TechDraw_LengthDimension/pl.md), aby uzyskać więcej informacji.



## Uwagi

Zapoznaj się również informacjami na stroni e[Wymiar długości](TechDraw_LengthDimension/pl#Uwagi.md).



## Właściwości

Zobacz stronę [Wymiar długości](TechDraw_LengthDimension/pl#W.C5.82a.C5.9Bciwo.C5.9Bci.md).





{{TechDraw_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw 3PtAngleDimension/pl
