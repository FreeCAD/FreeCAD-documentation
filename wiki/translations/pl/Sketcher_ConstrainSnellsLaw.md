---
 GuiCommand:
   Name: Sketcher ConstrainSnellsLaw
   Name/pl: Szkicownik: Wiązanie prawo Snella
   MenuLocation: Szkic , Wiązania szkicownika , Wiązanie refrakcji 
   Workbenches: Sketcher_Workbench/pl
   Shortcut: **K** **W**
   Version: 0.15
---

# Sketcher ConstrainSnellsLaw/pl



## Opis

Narzędzie <img alt="" src=images/Sketcher_ConstrainSnellsLaw.svg  style="width:24px;"> **Wiązanie prawo Snell\'a** wiąże dwie linie tak, aby były zgodne z prawem załamania światła, gdy przenika ono przez interfejs, w którym spotykają się dwa materiały o różnych współczynnikach załamania. Zobacz [Prawo Snella](http://en.wikipedia.org/wiki/Snell%27s_law).

<img alt="" src=images/Snells_law2_witheq.svg  style="width:" height="400px;"> 
*Prawo Snell'a*



## Użycie

<img alt="" src=images/Sketcher_SnellsLaw_Example1.png  style="width:500px;"> 
*Sekwencja kliknięć jest oznaczona żółtymi strzałkami z liczbami, n1 i n2 pokazują, gdzie znajdują się współczynniki załamania.*

1.  Przygotuj dwie linie reprezentujące wiązkę światła oraz krawędź pełniącą rolę interfejsu. Linie powinny znajdować się po różnych stronach interfejsu. Interfejsem może być [linia](Sketcher_CreateLine/pl.md), [łuk](Sketcher_CreateArc/pl.md), [okrąg](Sketcher_CreateCircle/pl.md), [stożek](Sketcher_CompCreateConic/pl.md).
2.  Wybierz punkt końcowy pierwszej linii, punkt końcowy drugiej linii i krawędź interfejsu. Zwróć uwagę na kolejność wyboru punktów końcowych.
3.  Istnieje kilka sposobów wywołania narzędzia:
    -   Wybierz z menu **Szkic → Wiązania szkicownika → <img src="images/Sketcher_ConstrainSnellsLaw.svg" width=16px> Wiązanie prawo Snell'a**.
    -   Użyj skrótu klawiaturowego: **K**, a następnie **W**.
4.  Zostanie otwarte okno dialogowe **Współczynnik załamania światła**.
5.  Wprowadź **Stosunek n2/n1:**. Gdzie **n2** jest dla ośrodka, w którym znajduje się druga wybrana linia, a **n1** jest dla ośrodka pierwszej linii.
6.  Dodawane jest wiązanie zgodne z prawem Snella. Jeśli jest to wymagane, punkty końcowe są [zbieżne](Sketcher_ConstrainCoincident/pl.md) i związane [na interfejsie](Sketcher_ConstrainPointOnObject/pl.md). Te dodatkowe więzy są nazywane [wiązaniami pomocniczymi](Sketcher_helper_constraint/pl.md).



## Uwagi

-   Rzeczywiste wiązanie prawna Snell\'a narzuca równanie prawa jawnego n1\*sin(theta1) = n2\*sin(theta2). Wymaga, aby końce linii były zbieżne i umieszczone bezpośrednio na powierzchni styku różnych wiązań, w przeciwnym razie zachowanie jest nieokreślone. Niezbędne wiązania pomocnicze są dodawane automatycznie w oparciu o bieżące współrzędne elementów.
-   Procedura Pythona nie dodaje wiązań pomocniczych. Muszą one być dodane ręcznie przez skrypt *(zobacz przykład w sekcji [Tworzenie skryptów](#Tworzenie_skryptów.md))*.
-   Te wiązania pomocnicze mogą być tymczasowo usunięte, a punkty końcowe przeciągnięte, co może być użyteczne w przypadku, gdy chcemy skonstruować odbity promień lub promienie dwójłomne.
-   W przeciwieństwie do rzeczywistości, współczynniki załamania są powiązane z promieniami światła, ale nie zgodnie z krawędzią granicy. Jest to użyteczne w celu emulowania dwupłaszczyzn, konstruowania ścieżek o różnych długościach fal spowodowanych załamaniem i łatwego konstruowania kąta początku całkowitego wewnętrznego odbicia.
-   Oba promienie mogą znajdować się po tej samej stronie powierzchni styku, spełniając równanie wiązania. Jest to fizyczny nonsens, chyba że stosunek n2/n1 wynosi 1,0, w którym to przypadku ograniczenie emuluje odbicie.
-   Łuki okręgu i elipsy są również akceptowane jako promienie. Ale to również jest fizyczny nonsens.



## Tworzenie skryptów 

Wiązanie może być utworzone przez [makropolecenie](Macros/pl.md) i z konsoli [Pyton](Python.md) za pomocą następującej funkcji:


```python
Sketch.addConstraint(Sketcher.Constraint('SnellsLaw',line1,pointpos1,line2,pointpos2,interface,n2byn1))
```

gdzie:

  - `Sketch` jest obiektem typu szkic

  - `line1` oraz `pointpos1` są dwiema liczbami całkowitymi określającymi punkt końcowy linii w środku o współczynniku załamania światła wynoszącym *n1*. `line1` jest indeksem linii w szkicu *(wartość zwracana przez Sketch.addGeometry)*, a `pointpos1` powinno wynosić 1 dla punktu początkowego i 2 dla punktu końcowego,

  - `line2` oraz `pointpos2` to indeksy określające punkt końcowy drugiej linii *(w środku „n2")*,

  - `n2byn1` jest liczbą zmiennoprzecinkową równą stosunkowi współczynników załamania światła *n2*/*n1*.

Strona [Skrypty szkicownika](Sketcher_scripting/pl.md) wyjaśnia wartości, których można użyć dla `line1`, `pointpos1`, `line2`, `pointpos2` and `interface` oraz zawiera dalsze przykłady tworzenia wiązań przy użyciu skryptów języka Python.

Przykład:


```python
import Sketcher
import Part
import FreeCAD

StartPoint = 1
EndPoint = 2

f = App.activeDocument().addObject("Sketcher::SketchObject","Sketch")

# add geometry to the sketch
icir = f.addGeometry(Part.Circle(App.Vector(-547.612366,227.479736,0),App.Vector(0,0,1),68.161979))
iline1 = f.addGeometry(Part.LineSegment(App.Vector(-667.331726,244.127090,0),App.Vector(-604.284241,269.275238,0)))
iline2 = f.addGeometry(Part.LineSegment(App.Vector(-604.284241,269.275238,0),App.Vector(-490.940491,256.878265,0)))
# add constraints
# helper constraints:
f.addConstraint(Sketcher.Constraint('Coincident',iline1,EndPoint,iline2,StartPoint)) 
f.addConstraint(Sketcher.Constraint('PointOnObject',iline1,EndPoint,icir)) 
# the Snell's law:
f.addConstraint(Sketcher.Constraint('SnellsLaw',iline1,EndPoint,iline2,StartPoint,icir,1.47))

App.ActiveDocument.recompute() 
```





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainSnellsLaw/pl
