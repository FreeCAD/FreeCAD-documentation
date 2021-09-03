---
- GuiCommand:/ro   Name:Draft Circle   Name/ro:Cerc   Workbenches:[Arch](Draft_Module/ro___Draft]],_[[Arch_Module/ro.md)|MenuLocation:Draft → Circle   Shortcut:C I   SeeAlso:[Draft Arc](Draft_Arc/ro.md)---


</div>

## Description


<div class="mw-translate-fuzzy">

## Descriere

Instrumentul Circle creează un cerc în [work plane](Draft_SelectPlane/ro.md) introducând două puncte, centrul și raza sau prin selectarea de tangente sau orice combinație a acestora. Este nevoie de [linewidth and color](Draft_Linestyle/ro.md) setată anterior pe fila Activități. Acest instrument funcționează la fel ca instrumentul [Draft Arc](Draft_Arc/ro.md), cu excepția faptului că se oprește după introducerea razei.


</div>

A Draft Circle can be turned into an arc by setting its **First Angle** and **Last Angle** properties to different values.

<img alt="" src=images/Draft_Circle_example.jpg  style="width:400px;">


<div class="mw-translate-fuzzy">

<img alt="" src=images/Draft_Circle_example.jpg  style="width:400px;">


</div>

## Usage

See also: [Draft Tray](Draft_Tray.md), [Draft Snap](Draft_Snap.md) and [Draft Constrain](Draft_Constrain.md).


<div class="mw-translate-fuzzy">

## Cum se utilizează {#cum_se_utilizează}

1.  Apăsați butonul **<img src="images/Draft_Circle.png" width=16px> [Draft Circle](Draft_Circle/ro.md)
** sau apăsați tastele **L** apoi **I**
2.  Faceți clic pe un prim punct din vizualizarea 3D sau tastați un [coordinate](Draft_Coordinates/ro.md)
3.  Faceți clic pe un al doilea punct din vizualizarea 3D sau tastați valoarea razei


</div>

## Options

The single character keyboard shortcuts available in the task panel can be changed. See [Draft Preferences](Draft_Preferences.md). The shortcuts mentioned here are the default shortcuts.


<div class="mw-translate-fuzzy">

## Opțiuni

-   O primă utilizarea a instrumentului cerc constă în alegerea a două puncte, centrul și un punct de pe circumferință, definind raza.
-   Prin apăsarea tastei **ALT**, puteți selecta o tangentă în loc să alegeți un punct. Prin urmare, puteți construi mai multe tipuri de cercuri selectând una, două sau trei tangente.
-   Pentru a introduce manual coordonatele, pur și simplu introduceți numerele, apoi apăsați **ENTER** între fiecare componentă X, Y și Z.
-   Apăsați tasta **T** sau faceți clic pe caseta de selectare pentru a bifa/debifa butonul **'''Continue'''**. Dacă modul continuat este activat, instrumentul Cerc va reporni după ce dați cel de-al doilea punct, permițându-vă să desenați un alt cerc fără să apăsați din nou butonul Cerc.
-   Apăsați **CTRL** în timp ce desenați pentru a forța [snapping](Draft_Snap/ro.md) punctul dvs. către cea mai apropiată locație, independent de distanța.
-   Apăsați **SHIFT** în timp ce desenați [constrain](Draft_Constrain/ro.md) al doilea punct pe orizontală sau pe verticală în raport cu primul punct.
-   Apăsați butonul **I** sau butonul **'''Completat'''** pentru a avea cercul umplut cu o fațetă.
-   Apăsați butonul **ESC** sau butonul **'''Anulare'''** pentru a întrerupe comanda curentă.
-   Cercul poate fi transformat într-un arc după creare, prin setarea proprietăților sale unghi și ultimul unghi la valori diferite.
-   Cercurile, în modul de afișare \"Flat Lines\", pot afișa un model de hașurare, prin setarea proprietății \"Pattern\" de mai jos.


</div>

## Notes

-   A Draft Circle can be edited with the [Draft Edit](Draft_Edit.md) command.

## Preferences

See also: [Preferences Editor](Preferences_Editor.md) and [Draft Preferences](Draft_Preferences.md).

-   To change the number of decimals used for the input of coordinates and radii: {{MenuCommand|Edit → Preferences... → General → Units → Units settings → Number of decimals}}.
-   To change the initial value of filled mode: {{MenuCommand|Edit → Preferences... → Draft → General settings → Draft tools options → Fill objects with faces whenever possible}}. Changing the filled mode in a task panel will override this preference for the current FreeCAD session.
-   If the {{MenuCommand|Edit → Preferences... → Draft → General settings → Draft tools options → Use Part Primitives when available}} option is checked, the command will create a [Part Circle](Part_Circle.md) instead of a Draft Circle.

## Properties

See also: [Property editor](Property_editor.md).

A Draft Circle object is derived from a [Part Part2DObject](Part_Part2DObject.md) and inherits all its properties. It also has the following additional properties:

### Data


{{TitleProperty|Draft}}

-    **Area|Area**: (read-only) specifies the area of the face of the circle. The value will be {{value|0.0}} if **Make Face** if `False` or the face cannot be created.

-    **First Angle|Angle**: specifies the start angle of the circle, normally {{value|0&#176;}}.

-    **Last Angle|Angle**: specifies the end angle of the circle, normally {{value|0&#176;}}.

-    **Make Face|Bool**: specifies if the circle makes a face or not. If it is `True` a face is created, otherwise only the perimeter is considered part of the object. This property only works if the **First Angle** and **Last Angle** have the same value. Note that {{value|0&#176;}} and {{value|360&#176;}} are not considered the same.

-    **Radius|Length**: specifies the radius of the circle.

### View


{{TitleProperty|Draft}}

-    **Pattern|Enumeration**: specifies the [Draft Pattern](Draft_Pattern.md) with which to fill the face of the circle. This property only works if **Make Face** is `True` and if **Display Mode** is {{value|Flat Lines}}.

-    **Pattern Size|Float**: specifies the size of the [Draft Pattern](Draft_Pattern.md).

## Scripting


<div class="mw-translate-fuzzy">

## Script-Programre {#script_programre}

Unealta Cerc poate fi folosită în [macro-uri](macros/ro.md) şi de la consola Python cu ajutorul funcţiei următoare:


</div>

To create a Draft Circle use the `make_circle` method (<small>(v0.19)</small> ) of the Draft module. This method replaces the deprecated `makeCircle` method.


```python
circle = make_circle(radius, placement=None, face=None, startangle=None, endangle=None, support=None)
circle = make_circle(Part.Edge, placement=None, face=None, startangle=None, endangle=None, support=None)
```


<div class="mw-translate-fuzzy">

-   Creează un obiect tip cerc cu o rază dată.
-   Dacă este dată o destinație de plasare, este utilizată. În cazul în care facemode este Fals, cercul este afișat ca un cadru tip filament, altfel ca o fațetă.
-   În cazul în care sunt date unghi de început și de sfârșit de capăt (în grade), ele sunt utilizate și obiectul apare ca un arc de cerc.
-   Returnează obiectul nou creat.


</div>

Exempluː 
```python
import FreeCAD as App
import Draft

doc = App.newDocument()

circle1 = Draft.make_circle(200)

zaxis = App.Vector(0, 0, 1)
p2 = App.Vector(1000, 1000, 0)
place2 = App.Placement(p2, App.Rotation(zaxis, 0))
circle2 = Draft.make_circle(500, placement=place2)

p3 = App.Vector(-1000, -1000, 0)
place3 = App.Placement(p3, App.Rotation(zaxis, 0))
circle3 = Draft.make_circle(750, placement=place3)

doc.recompute()
```





 
