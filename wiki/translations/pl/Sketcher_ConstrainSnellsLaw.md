---
- GuiCommand:
   Name: Sketcher ConstrainSnellsLaw
   Name/pl: Szkicownik: Wiązanie prawo Snella
   MenuLocation: Szkic - Wiązania szkicownika - Wiązanie refrakcji (prawo Snell'a)
   Workbenches: [Szkicownik](Sketcher_Workbench/pl.md)
   Shortcut: **K** **W**
   Version: 0.15
---

# Sketcher ConstrainSnellsLaw/pl



## Opis

Powoduje związanie dwóch linii do przestrzegania prawa załamania światła, które przenika przez powierzchnię, gdzie spotykają się dwa materiały o różnych współczynnikach załamania. Zobacz [Prawo Snell\'a](http://en.wikipedia.org/wiki/Snell%27s_law) na Wikipedii, aby uzyskać więcej informacji.

<img alt="" src=images/Snells_law2_witheq.svg  style="width:" height="400px;">



*Prawo Snell'a*



## Użycie

<img alt="" src=images/Sketcher_SnellsLaw_Example1.png  style="width:500px;"> 
*Sekwencja kliknięć jest oznaczona żółtymi strzałkami z numerami. n1, n2 to tylko etykiety, wskazujące gdzie znajdują się wskaźniki załamania.*

-   Będziesz potrzebował dwóch linii, które mają podążać za promieniem światła, oraz krzywej, która będzie działać jako powierzchnia kontaktowa. Linie te powinny znajdować się po różnych stronach tej powierzchni.
-   Wybierz punkt końcowy jednej linii, punkt końcowy drugiej linii i krawędź powierzchni kontaktowej. Powierzchnia kontaktu może być [linią](Sketcher_CreateLine.md), [łukiem](Sketcher_CompCreateArc.md), [okręgiem](Sketcher_CompCreateCircle.md) lub [stożkiem](Sketcher_CompCreateConic.md). Zwróć uwagę na kolejność, w jakiej wybrałeś punkty końcowe.
-   Wywołaj wiązanie. Pojawi się okno dialogowe z zapytaniem o stosunek indeksów załamania n2/n1. n2 odpowiada środkowi, w którym znajduje się druga wybrana linia punktu końcowego, n1 jest dla pierwszej linii.
-   Punkty końcowe będą zbieżne *(jeśli trzeba)*, zostaną związane z powierzchnią kontaktu *(jeśli trzeba)*, a prawo Snell\'a zostanie związane.

Zauważ, że kilka [wiązań pomocniczych](Sketcher_helper_constraint.md) zostanie dodanych automatycznie *(punkt na obiekcie, zbieżność)*. Mogą one zostać usunięte, jeśli powodują nadmiarowość lub dodane ręcznie, jeśli nie zostały dodane automatycznie. Dla faktycznego wiązania prawa Snell\'a punkty końcowe linii muszą być zbieżne i leżeć na powierzchni kontaktu, w przeciwnym razie zachowanie jest niezdefiniowane.

Za pomocą przyboru **[<img src=images/Sketcher_CreatePolyline.svg style="width:16px"> [Linia łamana](Sketcher_CreatePolyline.md)**, możliwe jest przyspieszenie rysowania promieni świetlnych. W tym przypadku można wybrać dwa przypadkowe punkty końcowe przez użycie pola wyboru.



## Uwagi

-   Rzeczywiste wiązanie prawna Snell\'a narzuca równanie prawa jawnego n1\*sin(theta1) = n2\*sin(theta2). Wymaga, aby końce linii były zbieżne i umieszczone bezpośrednio na powierzchni styku różnych wiązań. Niezbędne wiązania pomocnicze są dodawane automatycznie w oparciu o bieżące współrzędne elementów.
-   Procedura Pythona nie dodaje wiązań pomocniczych. Muszą one być dodane ręcznie przez skrypt *(zobacz przykład w sekcji Tworzenie skryptów)*.
-   Te wiązania pomocnicze mogą być tymczasowo usunięte, a punkty końcowe przeciągnięte, co może być użyteczne w przypadku, gdy chcemy skonstruować odbity promień lub promienie dwójłomne.
-   W przeciwieństwie do rzeczywistości, współczynniki załamania są powiązane z promieniami światła, ale nie zgodnie z krawędzią granicy. Jest to użyteczne w celu emulowania dwupłaszczyzn, konstruowania ścieżek o różnych długościach fal spowodowanych załamaniem i łatwego konstruowania kąta początku całkowitego wewnętrznego odbicia.
-   Oba promienie mogą znajdować się po tej samej stronie powierzchni styku, spełniając równanie wiązania. Jest to fizyczny nonsens, chyba że stosunek n2/n1 wynosi 1,0, w którym to przypadku ograniczenie emuluje odbicie.
-   Łuki okręgu i elipsy są również akceptowane jako promienie *(fizyczny nonsens)*.



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
MiddlePoint = 3

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
