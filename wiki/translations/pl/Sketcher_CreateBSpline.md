---
- GuiCommand:/pl
   Name:Sketcher CreateBSpline
   Name/pl:Szkicownik: Utwórz krzywą złożoną
   MenuLocation:Szkic → Elementy geometryczne szkicownika → Utwórz krzywą złożoną
   Workbenches:[Szkicownik](Sketcher_Workbench/pl.md)
   Shortcut:**G** **B** **B**
   Version:0.17
   SeeAlso:[Utwórz okresową krzywą złożoną](Sketcher_CreatePeriodicBSpline/pl.md)
---

# Sketcher CreateBSpline/pl



## Opis

To narzędzie tworzy krzywą złożoną z jej punktów kontrolnych. *(Zapoznaj się z treścią strony [Krzywe złożone](B-Splines/pl.md), aby uzyskać więcej informacji o krzywych typu B-splines)*.

![](images/Sketcher_B-spline_example01.png ) 
*Krzywa złożona ''(w kolorze białym)'' zdefiniowana przez 4 punkty kontrolne. Na rysunku widać zielony wielokąt kontrolny ''(linie proste łączące punkty kontrolne)'' oraz koła wagowe w kolorze ciemnożółtym. Zielona cyfra "3" w środku odnosi się do [stopnia](Sketcher_BSplineIncreaseDegree/pl#Opis.md) krzywej złożonej, a cyfry "(4)" na końcach krzywej złożonej odnoszą się do ich [krotności węzła](Sketcher_BSplineDecreaseKnotMultiplicity/pl#Opis.md). Czerwona cyfra "3" oznacza wagę punktu kontrolnego, która jest zdefiniowana jako ograniczenie promienia do okręgu punktu kontrolnego.*



## Użycie

1.  Naciśnij przycisk **[<img src=images/Sketcher_CreateBSpline.svg style="width:16px"> '''Krzywa złożona przez punkty kontrolne'''**.
2.  Utwórz serię punktów, klikając w oknie [widoku 3D](3D_view.md). Gdy polecenie jest aktywne, utworzone punkty są połączone liniami prostymi, a na każdym punkcie tworzony jest okrąg konstrukcyjny.
3.  Opcjonalnie naciśnij klawisz **D** przed zakończeniem wprowadzania danych, aby określić stopień krzywej. {{Version/pl|0.20}}
4.  Opcjonalnie naciśnij klawisz **Backspace** przed zakończeniem wprowadzania, aby usunąć ostatnio utworzony punkt kontrolny. {{Version/pl|0.20}}
5.  Kliknij prawym przyciskiem myszki, aby zakończyć proces wprowadzania danych i wygenerować krzywą.
6.  W zależności od preferencji, narzędzie może pozostać aktywne do śledzenia nowej krzywej. Kliknij ponownie prawym przyciskiem myszki, aby zakończyć polecenie.



## Uwagi

-   Istnieje możliwość zdefiniowania wagi punktów kontrolnych poprzez zmianę rozmiarów promieni okręgów wagowych. Należy najpierw usunąć wiązania równościowe na okręgach. Wiązanie promienia jest dowolne, waga punktów kontrolnych będzie określona przez względne promienie okręgów. Działa to podobnie do grawitacji: im większy jest okrąg w stosunku do pozostałych, tym bardziej krzywa będzie przyciągana do punktu kontrolnego.
-   Widoczność wielokąta kontrolnego, grzebień krzywizny, stopień i krotność węzła można włączać / wyłączać z paska narzędzi [krzywych złożonych](Sketcher_Workbench/pl#Narzędzia_szkicownika_dla_krzywych_złożonych.md)
-   Sprawdź inne narzędzia na pasku [krzywych złożonych](Sketcher_Workbench/pl#Narzędzia_szkicownika_dla_krzywych_złożonych.md), by znaleźć więcej narzędzi do edycji krzywej złożonej.



## Ograniczenia

-   Wiele typów wiązań nie jest obecnie obsługiwanych.

-   Narzędzie [Rozszerz](Sketcher_Extend/pl.md) nie jest obsługiwane.

-   Narzędzie [Podziel](Sketcher_Split/pl.md) nie jest obsługiwane.

-    {{VersionMinus/pl|0.20}}: Kształt krzywej złożonej można edytować tylko przez przeciągnięcie jednego z punktów kontrolnych. Węzły leżące na krzywej nie mogą być wybierane.





{{Sketcher_Tools_navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CreateBSpline/pl
