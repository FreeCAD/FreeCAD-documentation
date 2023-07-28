---
- GuiCommand:/pl
   Name:Sketcher CreateLine
   Name/pl:Szkicownik: Utwórz linię
   MenuLocation:Szkic → Elementy geometryczne szkicownika → Utwórz linię
   Workbenches:[Szkicownik](Sketcher_Workbench/pl.md)
   Shortcut:**G** **L**
   SeeAlso:[Polilinia](Sketcher_CreatePolyline/pl.md)
---

# Sketcher CreateLine/pl



## Opis

Narzędzie to rysuje linię, wybierając dwa punkty w oknie [widoku 3D](3D_view/pl.md). Po uruchomieniu narzędzia kursor myszki zmienia się w biały krzyż z czerwoną ikoną linii. Poza tym wyświetlane są współrzędne w czasie rzeczywistym.

![](images/Sketcher_LineExample1.png‎ )

Utworzony obiekt linii zaczyna się i kończy w podanych punktach, ale linia jest nieskończona pod względem wiązań [Utwórz styczną](Sketcher_ConstrainTangent/pl.md), [Utwórz punkt na obiekcie](Sketcher_ConstrainPointOnObject/pl.md) oraz [Ustaw kąt linii](Sketcher_ConstrainAngle/pl.md). Oznacza to na przykład, że punkt z wiązaniem [Wiązanie kąta](Sketcher_ConstrainAngle/pl.md) może nie znajdować się pomiędzy dwoma podanymi punktami, ale może leżeć poza nimi na przedłużeniu narysowanej linii.



## Użycie

-   Zaznacz punkty na pustym obszarze okna widoku 3D lub na istniejącym obiekcie *(automatyczne wiązania muszą być aktywne w oknie [Widoku zadań](Task_panel/pl.md))*.
-   Wciśnięcie klawisza **Esc** lub kliknięcie prawym klawiszem myszy anuluje tę funkcję.





{{Sketcher Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CreateLine/pl
