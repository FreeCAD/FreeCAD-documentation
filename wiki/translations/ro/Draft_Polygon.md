---
- GuiCommand:
   Name:Draft Polygon
   Name/ro:Draft Polygon
   MenuLocation:Draft - Polygon
   Workbenches:[Draft](Draft_Workbench/ro.md), [Arch](Arch_Workbench/ro.md)
   Shortcut:**P** **G**
   Version:0.7
---

# Draft Polygon/ro


</div>

## Description


<div class="mw-translate-fuzzy">

## Descriere

Instrumentul poligon creează un poligon regulat prin alegerea a două puncte, centrul și un al doilea punct care definesc o rază. Este nevoie de [linewidth and color](Draft_Linestyle/ro.md) setată anterior pe fila Activități.


</div>

A Draft Polygon can be switched from inscribed to circumscribed by changing its **Draw Mode** property. The corners of a Draft Polygon can be filleted (rounded) or chamfered by changing its **Fillet Radius** or **Chamfer Size** respectively.

<img alt="" src=images/Draft_polygon_example.jpg  style="width:400px;">


<div class="mw-translate-fuzzy">

<img alt="" src=images/Draft_polygon_example.jpg  style="width:400px;">


</div>

## Usage

See also: [Draft Tray](Draft_Tray.md), [Draft Snap](Draft_Snap.md) and [Draft Constrain](Draft_Constrain.md).


<div class="mw-translate-fuzzy">

## Cum se utilizează 

1.  Apăsați tasta **<img src="images/_Draft_Polygon.svg_" width= 16px> [Proiect Polygon](Draft_Polygon/ro.md)
** sau apăsați **P** apoi tastele **G**
2.  Faceți clic pe un prim punct al vizualizării 3D sau tastați un coordinate pentru a indica centrul
3.  Ajustați numărul dorit de laturi în dialogul de opțiuni,
4.  Faceți clic pe un alt punct al vizualizării 3D sau tastați o valoare de rază pentru a defini raza poligonului. Poligonul va fi, de asemenea, o fațetă, chiar dacă apare ca un cadru de sârmă.


</div>

## Options

The single character keyboard shortcuts available in the task panel can be changed. See [Draft Preferences](Draft_Preferences.md). The shortcuts mentioned here are the default shortcuts.


<div class="mw-translate-fuzzy">

## Opțiuni

-   Pentru a introduce manual coordonatele, pur și simplu introduceți numerele, apoi apăsați **ENTER** între fiecare componentă X, Y și Z.
-   Apăsați tasta **T** sau faceți clic pe caseta de selectare pentru a bifa/debifa butonul **'''Continue'''**. Dacă modul continuat este activat, instrumentul Polygon se va reporni după ce îl terminați sau închideți, permițându-vă să desenați alta fără a apăsa din nou butonul Polygon.
-   Apăsați **CTRL** în timp ce desenați pentru a forța [snapping](Draft_Snap/ro.md) punctul dvs. către cea mai apropiată locație, independent de distanța.
-   Apăsați pe **SHIFT** în timp ce desenați [constrain](Draft_Constrain/ro.md) următorul punct pe orizontală sau pe verticală în raport cu ultima.
-   Apăsați butonul **I** sau butonul **'' 'Completat' '** pentru a avea poligonul umplut cu o față după ce a fost închis
-   Apăsați butonul **ESC** sau butonul **'' 'Anulare' ''** pentru a întrerupe comanda curentă.
-   Poligoanele, în modul de afișare \"Flat Lines\", pot afișa un model de trapă, prin setarea proprietății \"Pattern\" de mai jos.


</div>

## Notes

-   A Draft Polygon can be edited with the [Draft Edit](Draft_Edit.md) command.

## Preferences

See also: [Preferences Editor](Preferences_Editor.md) and [Draft Preferences](Draft_Preferences.md).

-   To change the number of decimals used for the input of coordinates and radii: **Edit → Preferences... → General → Units → Units settings → Number of decimals**.
-   To change the initial value of filled mode: **Edit → Preferences... → Draft → General settings → Draft tools options → Fill objects with faces whenever possible**. Changing the filled mode in a task panel will override this preference for the current FreeCAD session.
-   If the **Edit → Preferences... → Draft → General settings → Draft tools options → Use Part Primitives when available** option is checked, the command will create a [Part RegularPolygon](Part_RegularPolygon.md) instead of a Draft Polygon.


<div class="mw-translate-fuzzy">

## Proprietăți

-    {{PropertyData/ro|Radius}}: Raza cercului definitoriu

-    {{PropertyData/ro|Draw Mode}}: Specifică dacă poligonul este înscris sau circumscris în jurul cercului definitoriu

-    {{PropertyData/ro|Faces Number}}: Numărul laturilor poligonului

-    {{PropertyData/ro|Chamfer Size}}: Specifică dimensiunea colțurilor zimțate

-    {{PropertyData/ro|Fillet Radius}}: Specifică o rază de curbură pentru a da colțurilor dreptunghiului

-    {{PropertyData/ro|Make Face}}: Umple poligonul cu o față

-    {{PropertyView/ro|Pattern}}: Specifică un model de trasare pentru a umple firul cu

-    {{PropertyView/ro|Dimensiune model}}: Specifică dimensiunea șablonului de trasare


</div>

See also: [Property editor](Property_editor.md).

A Draft Polygon object is derived from a [Part Part2DObject](Part_Part2DObject.md) and inherits all its properties. It also has the following additional properties:

### Data


{{TitleProperty|Draft}}

-    **Area|Area**: (read-only) specifies the area of the face of the polygon. The value will be {{value|0.0}} if **Make Face** if `False`.

-    **Chamfer Size|Length**: specifies the length of the chamfers at the corners of the polygon.

-    **Draw Mode|Enumeration**: specifies if the polygon is {{value|inscribed}} in a circle or {{value|circumscribed}} around a circle.

-    **Faces Number|Integer**: specifies the number of sides of the polygon.

-    **Fillet Radius|Length**: specifies the radius of the fillets at the corners of the polygon.

-    **Make Face|Bool**: specifies if the polygon makes a face or not. If it is `True` a face is created, otherwise only the perimeter is considered part of the object.

-    **Radius|Length**: specifies the radius of the circle that defines the polygon.

### View


{{TitleProperty|Draft}}

-    **Pattern|Enumeration**: specifies the [Draft Pattern](Draft_Pattern.md) with which to fill the face of the polygon. This property only works if **Make Face** is `True` and if **Display Mode** is {{value|Flat Lines}}.

-    **Pattern Size|Float**: specifies the size of the [Draft Pattern](Draft_Pattern.md).

## Scripting


<div class="mw-translate-fuzzy">

## Script-Programare 

Instrumentul Polygon poate fi utilizat în [macros](macros/ro.md) și din consola python utilizând următoarea funcție:


</div>

To create a Draft Polygon use the `make_polygon` method (<small>(v0.19)</small> ) of the Draft module. This method replaces the deprecated `makePolygon` method.


```python
polygon = make_polygon(nfaces, radius=1, inscribed=True, placement=None, face=None, support=None)
```


<div class="mw-translate-fuzzy">

-   Creează un obiect poligon cu numărul dat de fețete și raza.
-   Dacă este inscripționat Fals, poligonul este circumscris în jurul unui cerc cu raza dată, altfel este inscris.
-   Dacă fața este adevărată, forma rezultată este afișată ca o față, în caz contrar ca un cadru de sârmă.
-   Returnează obiectul nou creat.


</div>

Exempluː 
```python
import FreeCAD as App
import Draft

doc = App.newDocument()

polygon1 = Draft.make_polygon(4, radius=500)
polygon2 = Draft.make_polygon(5, radius=750)

zaxis = App.Vector(0, 0, 1)
p3 = App.Vector(1000, 1000, 0)
place3 = App.Placement(p3, App.Rotation(zaxis, 90))

Polygon3 = Draft.make_polygon(6, radius=1450, placement=place3)

doc.recompute()
```



---
![](images/Button_right.svg) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Polygon/ro
