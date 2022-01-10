---
- GuiCommand:/de
   Name:Draft OrthoArray
   Name/de:Entwurf AnordnungRechtwinklig
   MenuLocation:Modifikation → Anordnung Werkzeuge → Anordnung
   Workbenches:[Entwurf](Draft_Workbench/de.md), [Architektur](Arch_Workbench/de.md)
   Version:0.19
   SeeAlso:[Entwurf PolarAnordnung](Draft_PolarArray/de.md), [Entwurf KreisAnordnung](Draft_CircularArray/de.md), [verknüpfte Pfadanordnung](Draft_PathArray/de.md), [Entwurf Punkteanordnung](Draft_PointArray/de.md), [verknüpfte Punkteanordnung](Draft_PointLinkArray/de.md)
---

# Draft OrthoArray/de

## Beschreibung

Die <img alt="" src=images/Draft_OrthoArray.svg  style="width:24px;"> **Draft OrthoArray**-Anweisung erstellt eine orthogonale (3-Achsen) Anordnung aus einem ausgewählten Objekt. Die Anweisung kann auch ein [Verknüpungsmuster](App_Link/de.md) erzeugen. Dies ist effizienter, als eine rechtwinklige Feldanordnung (orthogonale Anordnung).

Diese Anweisung kann für 2D-Objekte angewendet werden, die mit der [Arbeitsbereich Entwurf](Draft_Workbench/de.md) oder mit dem [Arbeitsbereich Skizzierer](Sketcher_Workbench/de.md) erstellt wurden, aber auch auf viele 3D-Objekte, die mit anderenArbeitsbereichen erstellt wurden, wie dem [Arbeitsbereich Part](Part_Workbench/de.md), [Arbeitsbereich PartDesign](PartDesign_Workbench/de.md) oder dem [Arbeitsbereich Architektur](Arch_Workbench/de.md).

<img alt="" src=images/Draft_Array_example.png  style="width:300px;"> 
*Entwurf orthogonale Anordnung*

## Anwendung

1.  Wahlweise ein Objekt auswählen.
2.  Es gibt mehrere Wege, die Anweisung aufzurufen:
    -   Die Schaltfläche **<img src="images/Draft_OrthoArray.svg" width=16px> [Draft OrthoArray](Draft_OrthoArray.md)** anzuklicken.
    -   Den Menüpunkt **Modification → Array tools → <img src="images/Draft_OrthoArray.svg" width=16px> Array** wählen.
3.  Die **Orthogonal array**-Aufgabenansicht wird geöffnet. Siehe auch [Options](#Options.md).
4.  Objekt auswählen, wenn noch keines ausgewählt wurde.
5.  Die erforderlichen Parameter in die Ansicht Aufgaben eingeben.
6.  Beenden der Auswührung der Anweisung:
    -   In die [3DAnsicht](3D_view/de.md) klicken.
    -   Drücke **Enter**.
    -   Die Schaltfläche **OK** anklicken.

## Optionen

-   Enter the **Number of elements** for the X, Y and Z directions. This number must be at least {{Value|1}} for every direction.
-   Enter the **X intervals** to specify the displacement for the elements in the X direction. For a rectangular array the Y and Z values must be {{Value|0}}.
-   Enter the **Y intervals** to specify the displacement for the elements in the Y direction. For a rectangular array the X and Z values must be {{Value|0}}.
-   Enter the **Z intervals** to specify the displacement for the elements in the Z direction. For a rectangular array the X and Y values must be {{Value|0}}.
-   Press the **Reset X, Y or Z** button to reset the displacement in the given direction to the default values.
-   If the **Fuse** checkbox is checked overlapping elements in the array are fused. This does not work for Link arrays.
-   If the **Link array** checkbox is checked a Link array instead of a regular array is created. A Link array is more efficient because its elements are [App Link](App_Link.md) objects.
-   Press **Esc** or the **Cancel** button to abort the command.

## Hinweise


<div class="mw-translate-fuzzy">

-   Jedes Element im Feld ist eine exakte Kopie des Originals, aber das geasamte Feld wird als eine einzige Einheit mit ihren Eigenschaften und ihrer Erscheinung angesehen.
-   Dieser Befehl erzeugt das gleiche \"Feld\"objekt, wie das, das mit den **<img src=images/Draft_PolarArray.svg style="width:16px"> <img src=images/Draft_CircularArray.svg style="width:Polares Feld](Draft_PolarArray/de.md)** und **[16px"> [Kreisfeld](Draft_CircularArray/de.md)**-Werkeugen erstellt wurde. Deshalb kann das Feld von orthogonal in polar oder kreisförmig durch seinen **Feldtyp** umgewandelt werden.


</div>

## Einstellungen

Siehe auch: [Eigenschaftseditor](Preferences_Editor/de.md) und [Entwurfseigenschaften](Draft_Preferences/de.md).

-   Um die Anzahl der Dezimalstellen für die Eingabe der Koordinaten zu ändern: **Bearbeiten → Eigenschaften... → Allgemein → Einheiten → Einheiten-Einstellungen → Anzahl der Nachkommastellen**

## Eigenschaften

Siehe auch: [Eigenschaftseditor](property_editor/de.md).

The Draft OrthoArray command, the [Draft PolarArray command](Draft_PolarArray.md) and the [Draft CircularArray command](Draft_CircularArray.md) create the same object. This object is derived from a [Part Feature](Part_Feature.md) object and inherits all its properties (with the exception of some View properties that are not inherited by Link arrays). The following properties are additional unless otherwise stated:

### Daten


{{TitleProperty|Verknüpfung}}

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
    


{{TitleProperty|Circular array}}

The properties in this group are hidden for orthogonal arrays and polar arrays.

-    **Number Circles|Integer**: specifies the number of circular layers. Must be at least {{Value|2}}.

-    **Radial Distance|Distance**: specifies the distance between circular layers.

-    **Symmetry|Integer**: specifies the number of symmetry lines. This number changes the distribution of the elements in the array.

-    **Tangential Distance|Distance**: specifies the distance between elements in the same circular layer. Must be larger than zero.


{{TitleProperty|Objects}}

-    **Array Type|Enumeration**: specifies the type of array, which can be {{value|ortho}}, {{value|polar}} or {{value|circular}}.

-    **Axis Reference|LinkGlobal**: specifies the object and edge to be used instead of the **Axis** and **Center** properties. Not used for orthogonal arrays.

-    **Base|Link**: specifies the object to duplicate in the array.

-    **Count|Integer**: (read-only) specifies the total number of elements in the array. Only available for Link arrays.

-    **Expand Array|Bool**: specifies whether to expand the array in the [Tree view](Tree_view.md) to enable the selection of its individual elements. Only available for Link arrays.

-    **Fuse|Bool**: specifies if overlapping elements in the array are fused or not. Not used for Link arrays.


{{TitleProperty|Orthogonal array}}

The properties in this group are hidden for circular arrays and polar arrays.

-    **Interval X|VectorDistance**: specifies the interval between elements in the X direction.

-    **Interval Y|VectorDistance**: specifies the interval between elements in the Y direction.

-    **Interval Z|VectorDistance**: specifies the interval between elements in the Z direction.

-    **Number X|Integer**: specifies the number of elements in the X direction. Must be at least {{Value|1}}.

-    **Number Y|Integer**: specifies the number of elements in the Y direction. Must be at least {{Value|1}}.

-    **Number Z|Integer**: specifies the number of elements in the Z direction. Must be at least {{Value|1}}.


{{TitleProperty|Polar array}}

The properties in this group are hidden for circular arrays and orthogonal arrays.

-    **Angle|Angle**: specifies the aperture of the circular arc. Use {{value|360&#176;}} for a full circle.

-    **Interval Axis|VectorDistance**: specifies the interval between elements in the **Axis** direction.

-    **Number Polar|Integer**: specifies the number of elements in the polar direction.


{{TitleProperty|Polar/circular array}}

The properties in this group are hidden for orthogonal arrays.

-    **Axis|Vector**: specifies the direction of the axis of the array.

-    **Center|VectorDistance**: specifies the center point of the array. The axis of the array passes through this point. For circular arrays it is an offset from the **Placement** of the **Base** object.

### Ansicht


{{TitleProperty|Verknüpfung}}

The properties in this group, with the exception of the inherited property, are only available for Link arrays. See [Std LinkMake](Std_LinkMake#Properties.md) for more information.

-    **Draw Style|Enumeration**
    

-    **Line Width|FloatConstraint**
    

-    **Override Material|Bool**
    

-    **Point Size|FloatConstraint**
    

-    **Selectable|Bool**: this is an inherited property that appears in the Selection group for other arrays

-    **Shape Material|Material**
    


{{TitleProperty|Basis}}

Die Eigenschaften dieser Gruppe, mit Ausnahme der vererbten Eigenschaft, gibt es nur für verknüpfte Anordnungen.Siehe auch [Std LinkMake](Std_LinkMake#Properties.md).

-    **Child View Provider|PersistentObject|Hidden**
    

-    **Material List|MaterialList|Hidden**
    

-    **Override Color List|ColorList|Hidden**
    

-    **Override Material List|BoolList|Hidden**
    

-    **Proxy|PythonObject|Hidden**: this is an inherited property.


{{TitleProperty|Zeige Auswahlmöglichkeiten}}

The properties in this group are inherited properties. See [Part Feature](Part_Feature#Properties.md) for more information.

-    **Bounding Box|Bool**: this property is not inherited by Link arrays.

-    **Display Mode|Enumeration**: for Link arrays it can be {{value|Link}} or {{value|ChildView}}. For other arrays it can be: {{value|Flat Lines}}, {{value|Shaded}}, {{value|Wireframe}} or {{value|Points}}

-    **Show In Tree|Bool**
    

-    **Visibility|Bool**
    


{{TitleProperty|Entwurf}}

-    **Pattern|Enumeration**: not used.

-    **Pattern Size|Float**: not used.


{{TitleProperty|Objectstil}}

The properties in this group are not inherited by Link arrays.

## Skripten

Siehe auch: _.

### Parametrische Anordnung 


<div class="mw-translate-fuzzy">

Das Werkzeug AnordnungRechtwinklig kann in [Makros](macros/de.md) und von der [Python](Python/de.md) Konsole aus mit folgender Funktion verwendet werden:


</div>

Die main Methode:


```python
array = make_array(base_object, arg1, arg2, arg3, arg4=None, arg5=None, arg6=None, use_link=True)
```

Die Verbinder (wrapper) für orthogonale Anordnungen sind:


```python
array = make_ortho_array(base_object,
                         v_x=App.Vector(10, 0, 0), v_y=App.Vector(0, 10, 0), v_z=App.Vector(0, 0, 10),
                         n_x=2, n_y=2, n_z=1,
                         use_link=True)
```


```python
array = make_ortho_array2d(base_object,
                           v_x=App.Vector(10, 0, 0), v_y=App.Vector(0, 10, 0),
                           n_x=2, n_y=2,
                           use_link=True)
```

Die Verbinder (wrapper) für rechteckige Anordnungen sind:


```python
array = make_rect_array(base_object,
                        d_x=10, d_y=10, d_z=10,
                        n_x=2, n_y=2, n_z=1,
                        use_link=True)
```


```python
array = make_rect_array2d(base_object,
                          d_x=10, d_y=10,
                          n_x=2, n_y=2,
                          use_link=True)
```

-    `base_object`is the object to be arrayed. It can also be the `Label` (string) of an object in the current document.

-    `v_x`, `v_y`, and `v_z` are the vectors between the base points of the elements in the respective directions.

-    `d_x`, `d_y`, and `d_z` are the distances between the base points of the elements in the respective directions.

-    `n_x`, `n_y`, and `n_z` are the numbers of elements in the respective directions.

-   If `use_link` is `True` the created elements are [App Links](App_Link.md) instead of regular copies.

-    `array`is returned with the created array object.

Beispiel:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

rect = Draft.make_rectangle(1500, 500)
v_x = App.Vector(1600, 0, 0)
v_y = App.Vector(0, 600, 0)

array = Draft.make_ortho_array2d(rect, v_x, v_y, 3, 4)
doc.recompute()
```

### Feste Anordnung (nicht parametrisch) 

Um eine feste, nicht parametrische Anordnung zu erstellen, verwendet man die `array`-Methode des Enwurfmoduls. Diese Methode gibt `None` aus.


```python
array(objectslist, xvector, yvector, xnum, ynum)
array(objectslist, xvector, yvector, zvector, xnum, ynum, znum)
```

Beispiel:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

rect = Draft.make_rectangle(1500, 500)
v_x = App.Vector(1600, 0, 0)
v_y = App.Vector(0, 600, 0)

Draft.array(rect, v_x, v_y, 3, 4)
doc.recompute()
```

---
[documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft OrthoArray/de
