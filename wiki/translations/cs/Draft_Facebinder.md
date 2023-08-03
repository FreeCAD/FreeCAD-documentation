# Draft Facebinder/cs
---
 GuiCommand:   Name: Draft_Facebinder   Workbenches: Draft_Workbench/cs   Kreslení, Arch_Workbench/cs|MenuLocation: Draft , Facebinder   Shortcut: F F---


</div>

## Popis


<div class="mw-translate-fuzzy">

Facebinder je velmi jednoduchý objekt zkonstruovaný z vybraných ploch jiných objektů. Je parametrický, můžete upravit původní objekt a objekt facebinder se úměrně změní. Tento objekt může být použit například pro vytváření vysunutí kolekce ploch z jiných objektů. Typické použití je v architektonickém designu, vytvoření objektu, který pokrývá několik zdí. Facebinder můžete po vytvoření posunovat a otáčet a všechno zůstává propojené s původními plochami


</div>

It can be used to create an extrusion from a collection of faces. This extrusion can for example represent a wall finish in architectural design.

<img alt="" src=images/Draft_facebinder_example.jpg  style="width:400px;"> 
*Facebinder created from the faces of walls*

## Použití


<div class="mw-translate-fuzzy">

1.  Vyberte plochy objektů (pro výběr několika ploch použijte CTRL)
2.  Stiskněte tlačítko ** <img src="images/Draft_Facebinder.png" width=16px> [Facebinder](Draft_Facebinder.md)
**,nebo klávesy **F**, **F**


</div>

## Properties

See also: [Property editor](Property_editor.md).

A Draft Facebinder object is derived from a [Part Feature](Part_Feature.md) object and inherits all its properties. It also has the following additional properties:

### Data


{{TitleProperty|Draft}}

-    **Area|Area**: (read-only) specifies the total area of the linked faces of the facebinder.

-    **Extrusion|Distance**: specifies the extrusion thickness of the facebinder.

-    **Faces|LinkSubList**: specifies the linked faces of the facebinder.

-    **Offset|Distance**: specifies an offset distance to apply between the facebinder and the original faces, prior to extrusion.

-    **Remove Splitter|Bool**: Specifies whether to remove splitter lines that divide co-planar faces of the facebinder.

-    **Sew|Bool**: Specifies whether to perform a topological sewing operation on the facebinder.

### View


{{TitleProperty|Draft}}

-    **Pattern|Enumeration**: specifies the [Draft Pattern](Draft_Pattern.md) with which to fill the faces of the facebinder. This property only works if **Display Mode** is {{value|Flat Lines}}.

-    **Pattern Size|Float**: specifies the size of the [Draft Pattern](Draft_Pattern.md).

## Scripting


<div class="mw-translate-fuzzy">

## Skriptování


</div>


<div class="mw-translate-fuzzy">

Nástroj Facebinder může být použit ve skriptech Pythonu a v [makrech](macros/cs.md) použitím následující funkce:


</div>


```python
facebinder = make_facebinder(selectionset)
```


<div class="mw-translate-fuzzy">

-   Vytvoří objekt facebinder z daného výběrového setu, což je seznam vybraných objektů, tak jak je vrací metoda FreeCADGui.Selection.getSelectionEx().
-   Počítat se bude pouze s vybranými plochami.
-   Vrací nově vytvořený objekt.


</div>


```python
PropertyLinkSubList = [tuple1, tuple2, tuple3, ...]
PropertyLinkSubList = [(object1, list1), (object2, list2), (object3, list3), ...]
PropertyLinkSubList = [(object1, ['Face1', 'Face4', 'Face6']), ...]
PropertyLinkSubList = [(object1, ('Face1', 'Face4', 'Face6')), ...]
```

The thickness of the Facebinder can be added by overwriting its `Extrusion` attribute; the value is entered in millimeters.

The placement of the Facebinder can be changed by overwriting its `Placement` attribute, or by individually overwriting its `Placement.Base` and `Placement.Rotation` attributes.

Příklad:


```python
import FreeCAD as App
import FreeCADGui as Gui
import Draft

doc = App.newDocument()

# Insert a solid box
box = doc.addObject("Part::Box", "Box")
box.Length = 2300
box.Width = 800
box.Height = 1000

# selection = Gui.Selection.getSelectionEx()
selection = [(box, ("Face1", "Face6"))]
facebinder = Draft.make_facebinder(selection)
facebinder.Extrusion = 50

doc.recompute()

facebinder.Placement.Base = App.Vector(1000, -1000, 100)
facebinder.ViewObject.ShapeColor = (0.99, 0.99, 0.4)

doc.recompute()
```



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Facebinder/cs
