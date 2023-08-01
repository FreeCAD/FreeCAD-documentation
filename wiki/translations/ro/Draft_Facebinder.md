---
- GuiCommand:
   Name: Draft Facebinder
   Name/ro: Draft Facebinder
   MenuLocation: Draft - Facebinder
   Workbenches: [Draft](Draft_Workbench/ro.md), [Arch](Arch_Workbench/ro.md)
   Shortcut: **F** **F**
---

# Draft Facebinder/ro


</div>

## Descriere


<div class="mw-translate-fuzzy">

Facebinderul este un obiect foarte simplu, construit din fațetele selectate ale altor obiecte. Este parametric, puteți modifica obiectul original și actualizările obiectului facebinder în consecință. Acesta poate fi apoi folosit, de exemplu, pentru a face o extrudare dintr-o colecție de fațete de la alte obiecte. O utilizare tipică este în designul arhitectural, pentru a construi un obiect care acoperă mai multe bucăți de pereți. Puteți mișca și roti în jurul fațetei după crearea ei, totul va rămâne legat de fațetele originale.


</div>

It can be used to create an extrusion from a collection of faces. This extrusion can for example represent a wall finish in architectural design.

<img alt="" src=images/Draft_facebinder_example.jpg  style="width:400px;"> 
*Facebinder created from the faces of walls*

## Cum se folosește 


<div class="mw-translate-fuzzy">

1.  Selectați fețetele pe obiecte (utilizați CTRL pentru a selecta mai multe fețe)
2.  Apăsați butonul {{KEY | <img src="images/_Draft_Facebinder.svg_" width= 16px> [ Facebinder](Draft_Facebinder_.md)}}, sau apăsați tatele {{KEY | F}}, {{KEY | F}}


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

## Scrip-Programare 


</div>


<div class="mw-translate-fuzzy">

Instrumentul Facebinder poate fi folosit în scripturile python și [macros](macros.md) utilizând următoarea funcție:


</div>


```python
facebinder = make_facebinder(selectionset)
```


<div class="mw-translate-fuzzy">

-   Creează un obiect facebinder din setul de selecție dat, care este o listă de obiecte de selecție, cum ar fi returnate de metoda FreeCADGui.Selection.getSelectionEx ().
-   Sunt luate în considerare doar fețele selectate
-   Returnează obiectul nou creat


</div>


```python
PropertyLinkSubList = [tuple1, tuple2, tuple3, ...]
PropertyLinkSubList = [(object1, list1), (object2, list2), (object3, list3), ...]
PropertyLinkSubList = [(object1, ['Face1', 'Face4', 'Face6']), ...]
PropertyLinkSubList = [(object1, ('Face1', 'Face4', 'Face6')), ...]
```

The thickness of the Facebinder can be added by overwriting its `Extrusion` attribute; the value is entered in millimeters.

The placement of the Facebinder can be changed by overwriting its `Placement` attribute, or by individually overwriting its `Placement.Base` and `Placement.Rotation` attributes.

Exempluː


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
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Facebinder/ro
