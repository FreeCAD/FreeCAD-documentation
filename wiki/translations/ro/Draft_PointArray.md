---
- GuiCommand:
   Name:Draft PointArray
   Icon:Draft_PointArray.svg
   Workbenches:[Draft](Draft_Workbench.md), [Arch](Arch_Workbench.md)
   MenuLocation:Draft → PointArray
   Version:0.18
   SeeAlso:[Draft Array](Draft_Array.md), [[Draft PathArray]]
---

# Draft PointArray/ro


</div>

## Descriere


<div class="mw-translate-fuzzy">

Instrumentul PointArray plasează copii ale unei forme selectate de-a lungul diferitelor puncte selectate.


</div>

Both commands can be used on 2D objects created with the [Draft Workbench](Draft_Workbench.md) or [Sketcher Workbench](Sketcher_Workbench.md), but also on many 3D objects such as those created with the [Part Workbench](Part_Workbench.md), [PartDesign Workbench](PartDesign_Workbench.md) or [Arch Workbench](Arch_Workbench.md).

<img alt="" src=images/Draft_PointArray_Example.png  style="width:400px;"> 
*Draft PointArray*


<div class="mw-translate-fuzzy">

## Cum se folosește 


</div>


<div class="mw-translate-fuzzy">

1.  Creați un obiect de formă pe care doriți să îl distribuiți. Veți obține cele mai bune rezultate dacă obiectul dvs. este centrat în jurul originii \"\" \', adică dacă {{PropertyData | position}} este \[0, 0, 0\].
2.  Poziționați punctele folosind Punct de tragere.
3.  Selectați punctele și creați o combinație a acestora utilizând [Draft Upgrade](Draft_Upgrade.md).
4.  Mai întâi selectați forma, apoi noul compus punct, apoi apăsați butonul {{KEY | <img src="images/_Draft_PointArray.svg_" width= 16px> [[Draft PointArray]]}}.


</div>

## Point compound 

A point compound is an object that contains one or more points. These are the supported point compounds and how they can be created:

-   [Part Compound](Part_Compound.md): Create one or more [Draft Points](Draft_Point.md) or [Part Points](Part_Point.md), select them and invoke the [Part Compound](Part_Compound.md) command.
-   Draft Block: Create one or more [Draft Points](Draft_Point.md) or [Part Points](Part_Point.md), select them and invoke the [Draft Upgrade](Draft_Upgrade.md) command.
-   [Sketcher Sketch](Sketcher_NewSketch.md): Create a [Sketch](Sketcher_NewSketch.md) and add one or more [Sketcher Points](Sketcher_CreatePoint.md) to the sketch.

## Proprietăți

See also: [Property editor](property_editor.md).

A Draft PointArray object is derived from a [Part Feature](Part_Feature.md) object and inherits all its properties (with the exception of some View properties that are not inherited by Link arrays). The following properties are additional unless otherwise stated:

### Data


{{TitleProperty|Link}}

The properties in this group are only available for Link arrays. See [Std LinkMake](Std_LinkMake#Properties.md) for more information.

-    **Scale|Float**
    

-    **Scale Vector|Vector|Hidden**
    

-    **Scale List|VectorList**
    

-    **Visibility List|BoolList|Hidden**
    

-    **Placement List|PlacementList|Hidden**
    

-    **Element List|LinkList|Hidden**
    

-    **_ Link Touched|Bool|Hidden**
    

-    **_ Child Cache|LinkList|Hidden**
    

-    **Colored Elements|LinkSubHidden|Hidden**
    

-    **Link Transform|Bool**
    


{{TitleProperty|Objects}}


<div class="mw-translate-fuzzy">

-    {{PropertyData | Base}}: Obiectul formei

-    {{PropertyData | Count}}: Numărul de copiere a formei (numai pentru citire)

-    {{PropertyData | PointList}}: un compus de puncte


</div>

### View


{{TitleProperty|Link}}

The properties in this group, with the exception of the inherited property, are only available for Link arrays. See [Std LinkMake](Std_LinkMake#Properties.md) for more information.

-    **Draw Style|Enumeration**
    

-    **Line Width|FloatConstraint**
    

-    **Override Material|Bool**
    

-    **Point Size|FloatConstraint**
    

-    **Selectable|Bool**: this is an inherited property that appears in the Selection group for other arrays

-    **Shape Material|Material**
    


{{TitleProperty|Base}}

The properties in this group, with the exception of the inherited property, are only available for Link arrays. See [Std LinkMake](Std_LinkMake#Properties.md) for more information.

-    **Child View Provider|PersistentObject|Hidden**
    

-    **Material List|MaterialList|Hidden**
    

-    **Override Color List|ColorList|Hidden**
    

-    **Override Material List|BoolList|Hidden**
    

-    **Proxy|PythonObject|Hidden**: this is an inherited property.


{{TitleProperty|Display Options}}

The properties in this group are inherited properties. See [Part Feature](Part_Feature#Properties.md) for more information.

-    **Bounding Box|Bool**: this property is not inherited by Link arrays.

-    **Display Mode|Enumeration**: for Link arrays it can be {{value|Link}} or {{value|ChildView}}. For other arrays it can be: {{value|Flat Lines}}, {{value|Shaded}}, {{value|Wireframe}} or {{value|Points}}

-    **Show In Tree|Bool**
    

-    **Visibility|Bool**
    


{{TitleProperty|Draft}}

-    **Pattern|Enumeration**: not used.

-    **Pattern Size|Float**: not used.


{{TitleProperty|Object style}}

The properties in this group are not inherited by Link arrays.

## Scripting


<div class="mw-translate-fuzzy">

## Scrip-Programare 


</div>


<div class="mw-translate-fuzzy">

Instrumentul PointArray poate fi utilizat în [macros](macros.md) și de la consola [Python](Python.md) utilizând următoarele funcții:


</div>


```python
point_array = make_point_array(base_object, point_object, extra=None, use_link=True)
```


<div class="mw-translate-fuzzy">

-    `base`este forma de copiat și {{incode | ptlst}} este un obiect cu geometrie, legături sau componente care definesc poziția copiilor.


</div>

Exempluː


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

polygon = Draft.make_polygon(3, radius=500.0)

p1 = Draft.make_point(App.Vector(1500, 0, 0))
p2 = Draft.make_point(App.Vector(2500, 0, 0))
p3 = Draft.make_point(App.Vector(2000, 1000, 0))

compound = doc.addObject("Part::Compound", "Compound")
compound.Links = [p1, p2, p3]

point_array = Draft.make_point_array(polygon, compound)
doc.recompute()
```

---
[documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft PointArray/ro
