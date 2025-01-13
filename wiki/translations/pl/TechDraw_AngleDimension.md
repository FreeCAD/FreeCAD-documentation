---
 GuiCommand:
   Name: TechDraw AngleDimension
   Name/pl: Rysunek Techniczny: Wstaw wymiar kąta
   MenuLocation: Rysunek Techniczny , Wymiary , Wstaw wymiar kąta
   Workbenches: TechDraw_Workbench/pl
   SeeAlso: TechDraw_3PtAngleDimension/pl
---

# TechDraw AngleDimension/pl



## Opis

Narzędzie *Wstaw wymiar kąta* dodaje wymiar kąta do widoku. Wymiar może być kątem wewnętrznym między dowolnymi dwiema krawędziami linii prostej.

<img alt="" src=images/TechDraw_Dimension_Angle_example.png  style="width:200px;"> 
*Pomiar kąta między dwiema prostymi*



## Użycie

1.  Wybierz punkty lub krawędzie. Geometrię można wybrać w oknie [widoku 3D](3D_view/pl.md) lub na rysunku.
2.  Jeśli zaznaczyłeś geometrię w widoku 3D: dodaj właściwy widok Rysunku Technicznego do zaznaczenia, wybierając go w oknie [Widok drzewa](Tree_view/pl.md).
3.  Istnieje kilka sposobów wywołania tego narzędzia:
    -   
        {{Version/pl|1.0}}
        
        : Jeśli [preferencja](TechDraw_Preferences/pl#Wymiary.md) **Narzędzie wymiarowania** jest ustawiona na {{Value|Narzędzie pojedyncze}} (domyślnie): kliknij na strzałce skierowanej w dół po prawej stronie od przycisku **<img src="images/TechDraw_Dimension.svg" width=|x16px><img src="images/Toolbar_flyout_arrow.svg" width=x16px>** i wybierz opcję **<img src="images/TechDraw_AngleDimension.svg" width=16px> Wstaw wymiar kąta** z listy rozwijanej.

    -   Jeśli ta preferencja ma inną wartość (i {{VersionMinus/pl|0.21}}): wciśnij przycisk **<img src="images/TechDraw_AngleDimension.svg" width=16px> [Wstaw wymiar kąta](TechDraw_AngleDimension/pl.md)**.

    -   Wybierz opcję z menu **Rysunek Techniczny → Wymiary → <img src="images/TechDraw_AngleDimension.svg" width=16px> Wstaw wymiar kąta**.
4.  Do widoku zostanie dodany wymiar.
5.  Wymiar można przeciągnąć do żądanej pozycji.
6.  Jeśli to konieczne, dodaj tolerancje, jak opisano na stronie [Wymiarowanie geometrii i tolerancja](TechDraw_Geometric_dimensioning_and_tolerancing/pl#Tolerancja.md).



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





{{TechDraw Tools navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw AngleDimension/pl
