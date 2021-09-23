# Draft PathArray/cs
---
- GuiCommand:/cs   Name:Draft PathArray   Name/cs:Kreslení TrasovéPole   Workbenches:[Architektura](Draft_Workbench/cs___Kreslení]],_[[Arch_Workbench/cs.md)|MenuLocation:Draft → PathArray   SeeAlso:[Draft Array](Draft_Array/cs.md) ---


</div>

## Popis


<div class="mw-translate-fuzzy">

Nástroj TrasovéPole umístí vybraný tvar na vybranou trasu. Trasa může být drát nebo jedna nebo více hran. Tvary na trase mohou být volitelně zarovnány podle trasy. Podle potřeby může být specifikován Vektor pro posunutí tvaru tak, že těžiště tvaru bude na trase. Pokud není vybrán žádný objekt, budete vyzváni k jeho výběru.


</div>

Both commands can be used on 2D objects created with the [Draft Workbench](Draft_Workbench.md) or [Sketcher Workbench](Sketcher_Workbench.md), but also on many 3D objects such as those created with the [Part Workbench](Part_Workbench.md), [PartDesign Workbench](PartDesign_Workbench.md) or [Arch Workbench](Arch_Workbench.md).

<img alt="" src=images/Draft_PathArray_Example.png  style="width:400px;"> 
*Draft PathArray*


<div class="mw-translate-fuzzy">

## Použití


</div>


<div class="mw-translate-fuzzy">

1.  Vyberte objekt tvaru, který chcete kopírovat.
2.  Vyberte objekt trasy, po které chcete tvar kopírovat -nebo-
3.  Vyberte nějaké hrany pro určení trasy.
4.  Stiskněte tlačítko **<img src="images/Draft_PathArray.png" width=16px> [Kreslení TrasovéPole](Draft_PathArray/cs.md)**.


</div>

## Alignment

The alignment of the elements in a Draft PathArray depends on the properties of the array and the orientation of the source object. The position of the source object is ignored: for the purpose of the array the {{Value|x}}, {{Value|y}} and {{Value|z}} are set to {{Value|0}}. If the **Align** property of the array is set to `False` the orientation of the array elements is identical to that of the source object. If it is set to `True` the X axis of the local coordinate system of each element placement is tangent to the path. The Y and Z axes of the local coordinate systems depend on the **Align Mode** property of the array. Other array properties involved in the alignment include **Tangent Vector**, **Force Vertical** and **Vertical Vector**.

<img alt="" src=images/Draft_PathArray_example2.png  style="width:600px;"> *3 arrays based on the same non-planar path. From left to right: Align is false, Align is true with Align Mode Original and Align is true with Align Mode Frenet*.

### Align Mode 

Three modes are available:

#### Original

This mode comes closest to the single **Align Mode** available in version 0.18. It relies on a fixed normal vector. If the path is planar this vector is perpendicular to the plane of the path, else a default vector, the positive Z axis, is used. From this normal vector and the local tangent vector (the local X axis) a [cross product](https://en.wikipedia.org/wiki/Cross_product) is calculated. This new vector is used as the local Z axis. The orientation of the local Y axis is determined from the local X and Z axes.

#### Frenet

This mode uses the local normal vector derived from the path at each element placement. If this vector cannot be determined (for example in the case of a straight segment) a default vector, again the positive Z axis, is used instead. With this vector and the local tangent vector the local coordinate system is determined using the same procedure as in the previous paragraph.

#### Tangent

This mode is similar to **Align Mode** {{Value|Original}} but includes the possibility to pre-rotate the source object by specifying a **Tangent Vector**.

### Force Vertical and Vertical Vector 

These properties are only available if **Align Mode** is {{Value|Original}} or {{Value|Tangent}}. If **Force Vertical** is set to `True` the local coordinate system is calculated in a different manner. The **Vertical Vector** is used as a fixed normal vector. From this normal vector and the local tangent vector (the local X axis) again a cross product is calculated. But now this vector is used as the local Y axis. The orientation of the local Z axis is determined from the local X and Y axes.

Using these properties can be required if one of the edged of the path is (almost) parallel to the default normal of the path.

## Vlastnosti

See also: [Property editor](property_editor.md).

A Draft PathArray object is derived from a [Part Feature](Part_Feature.md) object and inherits all its properties (with the exception of some View properties that are not inherited by Link arrays). The following properties are additional unless otherwise stated:

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
    


{{TitleProperty|Alignment}}


<div class="mw-translate-fuzzy">

-    **Base**: Objekt tvaru

-    **PathObj**: Objekt trasy

-    **PathSubs**: Subelementy(hrany) objektu trasy, které budou použity jako trasa

-    **Count**: Počet kopií tvaru

-    **Xlate**: Vektor posunutí

-    **Align**: Hodnota True pro zarovnání tvarů podle trasy, False pro ponechání tvarů podle jejich původní orientace.


</div>


{{TitleProperty|Objects}}

-    **Base|LinkGlobal**: specifies the object to duplicate in the array.

-    **Count|Integer**: specifies the number of elements in the array.

-    **Expand Array|Bool**: specifies whether to expand the array in the [Tree view](Tree_view.md) to enable the selection of its individual elements. Only available for Link arrays.

-    **Path Object|LinkGlobal**: specifies the object to be used for the path. It must contain {{Value|Edges}} in its [Part TopoShape](Part_TopoShape.md).

-    **Path Subelements|LinkSubListGlobal**: specifies a list of edges of the **Path Object**. If supplied only these edges are used for the path.

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

## Skriptování


</div>


<div class="mw-translate-fuzzy">

Nástroj TrasovéPole může být využit v [makrech](macros.md) a z konzoly Pythonu použitím následující funkce:


</div>


```python
path_array = make_path_array(base_object, path_object,
                             count=4, extra=App.Vector(0, 0, 0), subelements=None,
                             align=False, align_mode="Original", tan_vector=App.Vector(1, 0, 0),
                             force_vertical=False, vertical_vector=App.Vector(0, 0, 1),
                             use_link=True)
```


<div class="mw-translate-fuzzy">

-   Rozloží požadovaný počet (count) kopií objektu shapeobject podél trasy pathobject nebo subobject (vybrané hrany) pathobjectu. Volitelně posune každou kopii ve směru a vzdálenosti podle FreeCAD.Vectoru pro nastavení rozdílu mezi středem tvaru a referenčním bodem tvaru. Volitelně zarovná baseobject tangenciálně/normálně/binormálně k trase.


</div>

Příklad:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

p1 = App.Vector(500, -1000, 0)
p2 = App.Vector(1500, 1000, 0)
p3 = App.Vector(3000, 500, 0)
p4 = App.Vector(4500, 100, 0)
spline = Draft.make_bspline([p1, p2, p3, p4])
obj = Draft.make_polygon(3, 500)

path_array = Draft.make_path_array(obj, spline, 6)
doc.recompute()

wire = Draft.make_wire([p1, -p2, -p3, -p4])
path_array2 = Draft.make_path_array(obj, wire, count=3, extra=App.Vector(0, -500, 0), subelements=["Edge2", "Edge3"], align=True, force_vertical=True)
doc.recompute()
```

---
[documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft PathArray/cs
