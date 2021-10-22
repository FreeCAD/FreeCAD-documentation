---
- GuiCommand:/de
   Name:Draft PathArray
   Name/de:Entwurf PfadAnordnung
   MenuLocation:Modifikation → Anordnung Werkzeuge → Pfad Anordnung
   Workbenches:[Entwurf](Draft_Workbench/de.md), [Arch](Arch_Workbench/de.md)
   Version:0.14
   SeeAlso:[Entwurf OrthoAnordnung](Draft_OrthoArray/de.md), [Entwurf PolarArray](Draft_PolarArray/de.md), [Entwurf CircularArray](Draft_CircularArray/de.md), [Entwurf PfadVerknüpfeAnordnung](Draft_PathLinkArray/de.md), [Entwurf PunktAnordnung](Draft_PointArray/de.md), [Entwurf Klonen](Draft_Clone/de.md)
---

# Draft PathArray/de


</div>

## Beschreibung


<div class="mw-translate-fuzzy">

Das **<img src="images/Draft_PathArray.svg" width=16px> [Entwurf PfadAnordnung](Draft_PathArray/de.md)** Werkzeug platziert Kopien einer ausgewählten Form entlang eines ausgewählten Pfades, der ein [Entwurf Draht](Draft_Wire/de.md), ein [Entwurf BSpline](Draft_BSpline.md) und ähnliche Kanten sein kann.


</div>


<div class="mw-translate-fuzzy">

Das PfadAnordnungswerkzeug kann auf jedes Objekt verwendet werden das eine [Part TopoForm](Part_TopoShape/de.md) hat, bedeutet 2D Formen, die mit dem [Entwurf Arbeitsbereich](Draft_Workbench/de.md) erstellt wurden, aber auch 3D Festkörper, die mit anderen Arbeitsbereichen erstellt wurden, z.B. [Part Arbeitsbereich](Part_Workbench/de.md), [PartDesign Arbeitsbereich](PartDesign_Workbench/de.md) oder [Arch Arbeitsbereich](Arch_Workbench/de.md).


</div>

<img alt="" src=images/Draft_PathArray_Example.png  style="width:400px;">


<div class="mw-translate-fuzzy">



*Objekt entlang eines Pfades angeordnet*


</div>

## Anwendung


<div class="mw-translate-fuzzy">

1.  Wähle das Objekt aus, das du verteilen möchtest.
2.  Wähle das Pfadobjekt oder die Kanten, entlang derer das Objekt verteilt werden soll.
3.  Drücke die **<img src="images/Draft_PathArray.svg" width=16px> [PfadAnordnung](Draft_PathArray/de.md)** Schaltfläche.
4.  Das Anordnungsobjekt wird sofort erzeugt. Du musst die Eigenschaften der Anordnung ändern, um die Anzahl und Richtung der erstellten Kopien zu ändern.


</div>

## Alignment

The alignment of the elements in a Draft PathArray depends on the properties of the array and the orientation of the source object. The position of the source object is ignored: for the purpose of the array the {{Value|x}}, {{Value|y}} and {{Value|z}} are set to {{Value|0}}. If the **Align** property of the array is set to `False` the orientation of the array elements is identical to that of the source object. If it is set to `True` the X axis of the local coordinate system of each element placement is tangent to the path. The Y and Z axes of the local coordinate systems depend on the **Align Mode** property of the array. Other array properties involved in the alignment include **Tangent Vector**, **Force Vertical** and **Vertical Vector**.

<img alt="" src=images/Draft_PathArray_example2.png  style="width:600px;"> 
*3 arrays based on the same non-planar path. From left to right: Align is false, Align is true with Align Mode Original and Align is true with Align Mode Frenet*.

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

## Eigenschaften

See also: [Property editor](property_editor.md).


<div class="mw-translate-fuzzy">

Eine _ beschriebenen Eigenschaften hat die PfadAnordnung die folgenden Eigenschaften im [Eigenschaftseditor](property_editor/de.md) .


</div>

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


{{TitleProperty|Ausrichtung}}

-    **Ausrichten|Bool**: wenn es `True` ist, werden die Kopien am Pfad ausgerichtet; andernfalls werden sie in ihrer Standardausrichtung belassen.

:   
    **Hinweis:**in bestimmten Fällen wird die Form flach erscheinen, in Wirklichkeit kann sie sich im 3D Raum bewegt haben, ändere also statt einer flachen Ansicht die Ansicht auf axonometrisch.

-    **Ausrichtungsmodus|Aufzählung**: drei Modi, {{Value|Original}}, {{Value|Frenet}}, {{Value|Tangent}}.

-    {{PropertyDataZusätzliche Translation|VektorAbstand}}: zusätzlicher Verschiebungsvektor {{Value|(x, y, z)}}, der auf jede Kopie entlang des Pfades angewendet wird. Dies ist nützlich, um kleine Anpassungen in der Position der Kopien vorzunehmen, z.B. wenn ihr Referenzpunkt nicht mit dem Mittelpunkt ihrer Form übereinstimmt.

-    **Force Vertical|Bool**: Wenn er `True` ist, wird der Wert von **Vertikal Vektor** als lokale Z Richtung verwendet, wenn **Ausrichtungsmodus** {{Value|Original}} oder {{Value|Tangente}} ist. <small>(v0.19)</small> 

-    **Tangentenvektor|Vektor**: die Standardeinstellung ist {{Value|(1, 0, 0)}}; Ausrichtungseinheitsvektor, der verwendet wird, wenn **Ausrichtungsmodus** {{Value|Tangente}} ist. <small>(v0.19)</small> 

-    **Vertikal Vektor|Vektor**}: Standardeinstellung ist {{Value|(0, 0, 1)}}; Einheitsvektor der lokalen Z Richtung, der verwendet wird, wenn **VertiKal Vektor** `True` ist. <small>(v0.19)</small> 


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

## Skripten


**Siehe auch:**

[Draft API](Draft_API/de.md) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).


</div>


<div class="mw-translate-fuzzy">

Das Pfadanordnungswerkzeug kann in [Makros](macros/de.md) und von der [Python](Python/de.md) Konsole aus mit folgender Funktion verwendet werden:


</div>


```python
path_array = make_path_array(base_object, path_object,
                             count=4, extra=App.Vector(0, 0, 0), subelements=None,
                             align=False, align_mode="Original", tan_vector=App.Vector(1, 0, 0),
                             force_vertical=False, vertical_vector=App.Vector(0, 0, 1),
                             use_link=True)
```


<div class="mw-translate-fuzzy">

-   Erstellt eine `Pfad Anordnungs` Objekt aus dem `baseobject`, indem bis zu `Anzahl` Kopien entlang des {{incode/de|Pfadobjekt}} platziert werden.
    -   Wenn {{incode/de|Pfadobjektunter}} angegeben wird, handelt es sich um eine Liste von Unterobjekten von {{incode/de|Pfadobjekt}}, und die Kopien werden entlang dieses kürzeren Pfades erstellt.
-   Wenn `xlate` angegeben wird, handelt es sich um einen `FreeCAD.Vector`, der eine zusätzliche Verschiebung anzeigt, um den Basispunkt der Kopien zu verschieben.
-   Wenn `align` `True` ist, werden die Kopien an der Tangente, der Normalen oder dem Binormalen des {{incode/de|Pfadobjekt}} an dem Punkt ausgerichtet, an dem die Kopie platziert wird.


</div>

Beispiel:


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


<div class="mw-translate-fuzzy">





</div>

---
[documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft PathArray/de
