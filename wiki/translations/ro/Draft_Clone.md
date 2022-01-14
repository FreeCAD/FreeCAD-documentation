# Draft Clone/ro
---
- GuiCommand:   Name:Draft Clone   Workbenches:[Arch](Draft_Workbench___Draft]],_[[Arch_Workbench.md)|MenuLocation:Draft → Clone   SeeAlso:[Draft Scale](Draft_Scale.md)---


</div>

## Description


<div class="mw-translate-fuzzy">

## Descriere

Acest instrument produce o clonă (o copie legată parametric de obiectul original) a unui obiect selectat. Dacă obiectul original se modifică, clona se schimbă și ea, dar își păstrează poziția, rotația și scala.


</div>

The command can be used on 2D objects created with the [Draft Workbench](Draft_Workbench.md) or [Sketcher Workbench](Sketcher_Workbench.md), but also on many 3D objects such as those created with the [Part Workbench](Part_Workbench.md), [PartDesign Workbench](PartDesign_Workbench.md) or [Arch Workbench](Arch_Workbench.md). Clones of 2D objects can be used in [PartDesign Bodies](PartDesign_Body.md).

<img alt="" src=images/Draft_Clone_example.jpg  style="width:400px;">


<div class="mw-translate-fuzzy">

<img alt="" src=images/Draft_Clone_example.jpg  style="width:400px;">


</div>

## Usage


<div class="mw-translate-fuzzy">

## Cum se folosește 

1.  Selectați obiectele pe care doriți să le clonați
2.  Apăsați butonul **<img src="images/Draft_Clone.png" width=16px> [[Draft Clone]]
**


</div>

## Properties

See also: [Property editor](property_editor.md).

An object created with the Draft Clone command is derived from a [Part Part2DObject](Part_Part2DObject.md), a [Part Feature](Part_Feature.md) object or, if an Arch Clone is created, from the object type of the source object. It inherits all properties from that object. A clone derived from one of the first two objects also has the following additional properties:

### Data


{{TitleProperty|Draft}}


<div class="mw-translate-fuzzy">

## Proprietăți

-    {{PropertyData | Scale}}: Specifică un factor de scară opțional pentru clonă

-    {{PropertyData | Fuse}}: Dacă această clonă utilizează mai multe obiecte, aceasta specifică dacă rezultatul este o fuziune sau o combinație {{Version | 0.17}}

-   Rezultatul instrumentului [Draft Scale](Draft_Scale.md) este, de asemenea, o clonă

-   Nicio schiță nu poate fi mapată pe fețetele unei clone. Aceasta este o limitare cunoscută în prezent .


</div>

## Scripting


<div class="mw-translate-fuzzy">

## Script-Programre 

Instrumentul Clone poate fi folosită în [macro-uri](macros/ro.md) şi de la consola Python cu ajutorul funcţiei următoare:


</div>

To create a clone use the `make_clone` method (<small>(v0.19)</small> ) of the Draft module. This method replaces the deprecated `clone` method.


```python
cloned_object = make_clone(obj, delta=None, forcedraft=False)
```


<div class="mw-translate-fuzzy">

-   Face o clonă a obiectului (obiectelor) dat(e).
-   Clona este o copie exactă, legată de obiectul dat.
-   Dacă obiectul original se modifică, se schimbă și obiectul final. Opțional, puteți da un Vector delta pentru a muta clona departe de poziția inițială.


</div>

Exempluː


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

place = App.Placement(App.Vector(1000, 0, 0), App.Rotation())
polygon1 = Draft.make_polygon(3, 750)
polygon2 = Draft.make_polygon(5, 750, placement=place)

vector = App.Vector(2600, 500, 0)
cloned_object = Draft.clone([polygon1, polygon2], delta=vector)

cloned_object.Fuse = True

doc.recompute()
```

---
[documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Clone/ro
