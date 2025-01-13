---
 GuiCommand:
   Name: Sketcher BSplineConvertToNURBS
   Name/pl: Szkicownik: Konwertuj geometrię na krzywą złożoną
   MenuLocation: Szkic , Narzędzia szkicownika krzywej złożonej , Konwertuj geometrię na krzywą złożoną
   Workbenches: Sketcher_Workbench/pl
   Version: 0.17
   SeeAlso: Sketcher_CreateBSpline/pl
---

# Sketcher BSplineConvertToNURBS/pl



## Opis

Narzędzie <img alt="" src=images/Sketcher_BSplineConvertToNURBS.svg  style="width:24px;"> **Konwertuj geometrię na krzywą złożoną** konwertuje krawędzie do [krzywej złożonej](B-Splines/pl.md).

<img alt="" src=images/sketcher_BSplineConvertToNurb.png  style="width:300px;"> 
*Różne obiekty przed przebudową.*

<img alt="" src=images/sketcher_BSplineConvertToNurb1.png  style="width:300px;"> 
*Te same obiekty po konwersji do krzywych złożonych.*



## Użycie

1.  Wybierz jedną lub więcej krawędzi.
2.  Istnieje kilka sposobów wywołania narzędzia:
    -   Naciśnij przycisk **[<img src=images/Sketcher_BSplineConvertToNURBS.svg style="width:16px"> '''Konwertuj geometrię na krzywą złożoną'''**.
    -   Wybierz z menu **Szkic → Narzędzia szkicownika krzywej złozonej → <img src="images/Sketcher_BSplineConvertToNURBS.svg" width=16px> Konwertuj geometrię na krzywą złożoną**.
3.  Krawędzie są konwertowane.



## Uwagi

Upewnij się, że elementy [stopień](Sketcher_BSplineDegree/pl.md), [ramka kontrolna](Sketcher_BSplinePolygon/pl.md), [grzebień](Sketcher_BSplineComb/pl.md), [węzeł](Sketcher_BSplineKnotMultiplicity/pl.md) i / lub [waga](Sketcher_BSplinePoleWeight/pl.md) są widoczne, w przeciwnym razie nic się nie stanie.

-   Jeśli przekształciłeś linie proste, musisz najpierw [zwiększyć stopień](Sketcher_BSplineIncreaseDegree/pl.md) linii, aby stały się one \"zginane\".
-   Narzędzie nie usuwa wewnętrznej geometrii [stożka](Sketcher_Workbench/pl#Sketcher_CompCreateConic.md). Musi ona zostać usunięta samodzielnie.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher BSplineConvertToNURBS/pl
