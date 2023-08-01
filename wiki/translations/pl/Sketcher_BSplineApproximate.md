---
- GuiCommand:
   Name: Sketcher BSplineApproximate
   Name/pl: Szkicownik: Konwertuj geometrię na krzywą złożoną
   MenuLocation: Szkic - Narzędzia szkicownika krzywej złożonej - Konwertuj geometrię na krzywą złożoną
   Workbenches: [Szkicownik](Sketcher_Workbench/pl.md)
   Version: 0.17
   SeeAlso: [Komponent utwórz krzywą złożoną](Sketcher_CompCreateBSpline/pl.md)
---

# Sketcher BSplineApproximate/pl



## Opis

Konwertuje zgodną geometrię, krawędzie i krzywe, na krzywą złożoną *(zobacz stronę [Krzywe złożone](B-Splines/pl.md), aby uzyskać więcej informacji)*.

<img alt="" src=images/sketcher_BSplineConvertToNurb.png  style="width:400px;"> 
*Różne obiekty przed przebudową.*

<img alt="" src=images/sketcher_BSplineConvertToNurb1.png  style="width:400px;"> 
*Te same obiekty po konwersji do krzywych złożonych.*



## Użycie

1.  Zaznacz jeden lub kilka segmentów szkicu i naciśnij przycisk na pasku narzędzi **[<img src=images/Sketcher_BSplineApproximate.svg style="width:24px"> '''Konwertuj geometrię na krzywą złożoną'''**.

Upewnij się, że elementy [stopień](Sketcher_BSplineDegree/pl.md), [ramka kontrolna](Sketcher_BSplinePolygon/pl.md), [grzebień](Sketcher_BSplineComb/pl.md), [węzeł](Sketcher_BSplineKnotMultiplicity/pl.md) lub [waga](Sketcher_BSplinePoleWeight/pl.md) są widoczne, w przeciwnym razie nic się nie stanie. Jeśli przekształciłeś linie proste, musisz najpierw [zwiększyć stopień](Sketcher_BSplineIncreaseDegree/pl.md) linii, aby stały się one \"zginane\".





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher BSplineApproximate/pl
