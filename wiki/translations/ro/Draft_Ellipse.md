---
- GuiCommand   */ro
   Name   *Draft Ellipse
   Name/ro   *Elipsă 2D
   MenuLocation   *Draft → Ellipse
   Workbenches   *[Draft](Draft_Workbench/ro.md), [Arch](Arch_Workbench/ro.md)
   Shortcut   ***E** **L**
   SeeAlso   *[Draft Circle](Draft_Circle/ro.md)
---

# Draft Ellipse/ro


</div>

## Descriere


<div class="mw-translate-fuzzy">

Instrumentul Ellipse creează o eliptsă în planul curent [work plane](Draft_SelectPlane/ro.md) introducând două puncte, definind colțul unei casete rectangulare în care se va potrivi elipsa. Este nevoie de [linewidth and color](Draft_Linestyle/ro.md) setată anterior pe fila Activități.


</div>

A Draft Ellipse can be turned into an elliptical arc by setting its **First Angle** and **Last Angle** properties to different values.

<img alt="" src=images/Draft_ellipse_example.jpg  style="width   *400px;">


<div class="mw-translate-fuzzy">

<img alt="" src=images/Draft_ellipse_example.jpg  style="width   *400px;">


</div>

## Usage

See also   * [Draft Tray](Draft_Tray.md), [Draft Snap](Draft_Snap.md) and [Draft Constrain](Draft_Constrain.md).


<div class="mw-translate-fuzzy">

## Cum se utilizează 

1.  Apăsați butonul **<img src="images/Draft_Ellipse.png" width=16px> [Draft Ellipse](Draft_Ellipse/ro.md)
** sau apăsați **E** apoi tastele **L**
2.  Faceți clic pe un prim punct din vizualizarea 3D sau tastați un coordinate
3.  Faceți clic pe un al doilea punct din vizualizarea 3D sau tastați un coordinate


</div>

## Opţiuni

The single character keyboard shortcuts available in the task panel can be changed. See [Draft Preferences](Draft_Preferences.md). The shortcuts mentioned here are the default shortcuts.


<div class="mw-translate-fuzzy">

-   Pentru a introduce manual coordonatele, pur și simplu introduceți numerele, apoi apăsați **ENTER** between each X, Y and Z component.
-   Apăsați **T**sau click pe caseta de validare pentru a bifa/debifa butonul **'''Continue'''** . Dacă modul Continuu este activat, instrumentul Ellipse se va reporni după ce dați cel de-al doilea punct, permițându-vă să desenați o altă elipsă fără să apăsați din nou butonul Ellipse.
-   Apăsați **CTRL** în timp ce desenați pentru a forța punctul [snapping](Draft_Snap/ro.md) punctul dvs. către cea mai apropiată locație, independent de distanță.
-   Apăsați **SHIFT** în timp ce atrageți la [constrain](Draft_Constrain/ro.md) al doilea punct pe orizontală sau pe verticală în raport cu primul.
-   Apăsați **I** apoi butonul **'''Filled'''** pentru a avea elipsa umplută cu o fațetă după ce a fost închisă
-   Apăsați **ESC** sau butonul **'''Cancel'''** pentru a abandona comanda.
-   Ellipses, atunci când în modul de afișare \"Flat Lines\", poate afișa un model de hașură, prin setarea proprietății \"Pattern\" de mai jos.


</div>

## Notes

-   A Draft Ellipse can be edited with the [Draft Edit](Draft_Edit.md) command.

## Preferences

See also   * [Preferences Editor](Preferences_Editor.md) and [Draft Preferences](Draft_Preferences.md).

-   To change the number of decimals used for the input of coordinates   * **Edit → Preferences... → General → Units → Units settings → Number of decimals**.
-   To change the initial value of filled mode   * **Edit → Preferences... → Draft → General settings → Draft tools options → Fill objects with faces whenever possible**. Changing the filled mode in a task panel will override this preference for the current FreeCAD session.
-   If the **Edit → Preferences... → Draft → General settings → Draft tools options → Use Part Primitives when available** option is checked, the command will create a [Part Ellipse](Part_Ellipse.md) instead of a Draft Ellipse.

## Proprietăți

See also   * [Property editor](Property_editor.md).

A Draft Ellipse object is derived from a [Part Part2DObject](Part_Part2DObject.md) and inherits all its properties. It also has the following additional properties   *

### Data


{{TitleProperty|Draft}}


<div class="mw-translate-fuzzy">

-    {{PropertyData/ro|Major Radius}}   * Semiaxa majoră a eleipseiaza majoră a elipsei

-    {{PropertyData/ro|Minor Radius}}   * Semiaxa minoră a elipsei

-    {{PropertyData/ro|Make Face}}   * Umple elipsa cu o fațetă

-    {{PropertyView/ro|Pattern}}   * Specificați modelul de hașură pentru a umple elipsa cu el

-    {{PropertyView/ro|Pattern Size}}   * specificați modelul și mărimea hașurii


</div>

### View


{{TitleProperty|Draft}}


<div class="mw-translate-fuzzy">

See also [Draft Pattern](Draft_Pattern/ro.md) page.


</div>

## Scripting


<div class="mw-translate-fuzzy">

## Script-Programare 

Instrumentul Ellipse poate fi folosit în [macros](macros/ro.md) și din consola python utilizând următoarea funcție   *


</div>

To create a Draft Ellipse use the `make_ellipse` method (<small>(v0.19)</small> ) of the Draft module. This method replaces the deprecated `makeEllipse` method.


```python
ellipse = make_ellipse(majradius, minradius, placement=None, face=True, support=None)
```


<div class="mw-translate-fuzzy">

-   Creează un obiect elipsă cu o semiaxă/rază majoră și semiaxă/minoră dată.
-   Dacă este dată o destinație de plasare, aceasta este utilizată.
-   Dacă facemode este False, elipsa este arătată ca un cadru de sârmă, altfel ca o fațetă.
-   Returnează obiectul nou creat.


</div>

Exempluː


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

ellipse1 = Draft.make_ellipse(3000, 200)
ellipse2 = Draft.make_ellipse(700, 1000)

zaxis = App.Vector(0, 0, 1)
p3 = App.Vector(1000, 1000, 0)
place3 = App.Placement(p3, App.Rotation(zaxis, 90))

ellipse3 = Draft.make_ellipse(700, 1000, placement=place3)

doc.recompute()
```



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Ellipse/ro
