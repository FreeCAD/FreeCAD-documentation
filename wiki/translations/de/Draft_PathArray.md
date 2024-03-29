---
 GuiCommand:
   Name: Draft PathArray
   Name/de: Draft PfadAnordnung
   MenuLocation: Änderung , Anordnungswerkzeuge , Pfad-Anordnung
   Workbenches: Draft_Workbench/de, Arch_Workbench/de
   Version: 0.14
   SeeAlso: Draft_OrthoArray/de, Draft_PolarArray/de, Draft_CircularArray/de, Draft_PathLinkArray/de, Draft_PointArray/de, Draft_PointLinkArray/de
---

# Draft PathArray/de



## Beschreibung

Der Befehl <img alt="" src=images/Draft_PathArray.svg  style="width:24px;"> **Draft PfadAnordnung** erstellt eine regelmäßige Anordnung aus einem ausgewählten Objekt, indem er Kopien entlang eines Pfades positioniert. Der Befehl [Draft PfadVerknüpfungsanordnung](Draft_PathLinkArray/de.md) erstellt alternativ eine effizientere Verknüpfungsanordnung ([Link](App_Link.md)-Array). Außer der Art der Anordnung die erstellt wird, normale Anordnung oder Verknüpfungsanordnung, ist der Befehl [Draft PfadVerknüpfungsanordnung](Draft_PathLinkArray/de.md) identisch mit diesem Befehl.

Beide Befehle können für 2D-Objekte verwendet werden, die mit den Arbeitsbereichen [Draft](Draft_Workbench/de.md) oder [Sketcher](Sketcher_Workbench/de.md) erstellt wurden, aber auch für viele 3D-Objekte, die mit anderen Arbeitsbereichen wie [Part](Part_Workbench/de.md), [PartDesign](PartDesign_Workbench/de.md) oder [Arch](Arch_Workbench/de.md) erstellt wurden.

<img alt="" src=images/Draft_PathArray_Example.png  style="width:400px;"> 
*Draft PfadAnordnung*



## Anwendung

1.  Ein Objekt auswählen, das angeordnet werden soll.
2.  Ein Pfadobjekt zur Auswahl hinzufügen. Es ist auch möglich stattdessen Kanten auszuwählen. Die Kanten müssen zu demselben Objekt gehören und miteinander verbunden sein.
3.  Es gibt mehrere Möglichkeiten den Befehl aufzurufen:
    -   Die Schaltfläche **<img src="images/Draft_PathArray.svg" width=16px> [Pfad-Anordnung](Draft_PathArray.md)** drücken.
    -   Den Menüeintrag **Änderung → Anordnungswerkzeuge → <img src="images/Draft_PathArray.svg" width=16px> Pfad-Anordnung** auswählen.
4.  Die Anordnung wird erstellt.
5.  Wahlweise die [Eigenschaften](#Eigenschaften.md) der Anordnung im [Eigenschafteneditor](property_editor/de.md) ändern.



## Ausrichtung

The alignment of the elements in a Draft PathArray depends on the properties of the array and the orientation of the source object. The position of the source object is ignored: for the purpose of the array the {{Value|x}}, {{Value|y}} and {{Value|z}} are set to {{Value|0}}. If the **Align** property of the array is set to `False` the orientation of the array elements is identical to that of the source object. If it is set to `True` the X axis of the local coordinate system of each element placement is tangent to the path. The Y and Z axes of the local coordinate systems depend on the **Align Mode** property of the array. Other array properties involved in the alignment include **Tangent Vector**, **Force Vertical** and **Vertical Vector**.

<img alt="" src=images/Draft_PathArray_example2.png  style="width:600px;"> 
*3 Anordnungen die auf demselben nicht ebenen Pfad basieren. Von links nach rechts:  '''Align''' ist ''false'', '''Align''' ist ''true'' mit '''Align Mode''' ''Original'' und '''Align''' ist ''true'' mit '''Align Mode''' ''Frenet''*.



### Ausrichtungsmodus

Es gibt drei Ausrichtungsmodi

#### Original

This mode comes closest to the single **Align Mode** available in version 0.18. It relies on a fixed normal vector. If the path is planar this vector is perpendicular to the plane of the path, else a default vector, the positive Z axis, is used. From this normal vector and the local tangent vector (the local X axis) a [cross product](https://en.wikipedia.org/wiki/Cross_product) is calculated. This new vector is used as the local Z axis. The orientation of the local Y axis is determined from the local X and Z axes.

#### Frenet

This mode uses the local normal vector derived from the path at each element placement. If this vector cannot be determined (for example in the case of a straight segment) a default vector, again the positive Z axis, is used instead. With this vector and the local tangent vector the local coordinate system is determined using the same procedure as in the previous paragraph.



#### Tangente

This mode is similar to **Align Mode** {{Value|Original}} but includes the possibility to pre-rotate the source object by specifying a **Tangent Vector**.

### Force Vertical and Vertical Vector 

These properties are only available if **Align Mode** is {{Value|Original}} or {{Value|Tangent}}. If **Force Vertical** is set to `True` the local coordinate system is calculated in a different manner. The **Vertical Vector** is used as a fixed normal vector. From this normal vector and the local tangent vector (the local X axis) again a cross product is calculated. But now this vector is used as the local Y axis. The orientation of the local Z axis is determined from the local X and Y axes.

Using these properties can be required if one of the edged of the path is (almost) parallel to the default normal of the path.



## Eigenschaften

Siehe auch: [Eigenschafteneditor](property_editor/de.md).

Eine [Pfad-Anordnung](Draft_PathArray/de.md) (Path-Array-Objekt) ist von einem [Part-Formelement](Part_Feature/de.md) abgeleitet und erbt alle seine Eigenschaften (mit Ausnahme einiger Ansicht-Eigenschaften, die nicht an die Verknüpfungsanordnungen vererbt werden). Außerdem sind, wenn nicht anders angegeben, die folgenden zusätzlichen Eigenschaften vorhanden:

### Data


{{TitleProperty|Link}}

Die Eigenschaften dieser Gruppe stehen nur für Verknüpfungsanordnungen zur Verfügung. Siehe [Std VerknüpfungErstellen](Std_LinkMake/de#Eigenschaften.md) für weitere Informationen.

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

-    {{PropertyData/de|Align|Bool}}: Legt fest, ob die Elemente der Anordnung entlang des Pfades ausgerichtet werden oder nicht. Ist sie `False`, sind alle anderen Eigenschaften in dieser Gruppe, außer {{PropertyData/de|Extra Translation}} nicht anwendbar und werden ausgeblendet.

-    {{PropertyData/de|Align Mode|Enumeration}}: Legt das Ausrichtungsverfahren fest; zur Auswahl stehen {{Value|Original}}, {{Value|Frenet}} oder {{Value|Tangent}}.

-    {{PropertyData/de|End Offset|Length}}: Legt die Länge vom Ende des Pfades bis zur letzten Kopie fest. Muss kleiner sein als die Länge des Pfades abzüglich der {{PropertyData/de|Start Offset}}. {{Version/de|0.21}}

-    {{PropertyData/de|Extra Translation|VectorDistance}}: Legt einen zusätzlichen Versatz für jedes Element entlang des Pfades fest.

-    {{PropertyData/de|Force Vertical|Bool}}: Legt fest, ob die vorgegebene Ausrichtung der Normale mit dem Wert der {{PropertyData/de|Vertical Vector}} überschrieben wird. Wird nur verwendet, wenn die {{PropertyData/de|Align Mode}} auf {{Value|Original}} oder {{Value|Tangent}} gesetzt ist.

-    {{PropertyData/de|Start Offset|Length}}: Legt die Länge vom Startpunkt des Pfades bis zur ersten Kopie fest. Muss kleiner als die Länge des Pfades sein. {{Version/de|0.21}}

-    {{PropertyData/de|Tangent Vector|Vector}}: Legt den Ausrichtungsvektor fest. Wird nur verwendet, wenn die {{PropertyData/de|Align Mode}} auf {{Value|Tangent}} gesetzt ist.

-    {{PropertyData/de|Vertical Vector|Vector}}: Legt den Vektor zum Überschreiben der Richtung der Normale fest. Wird nur verwendet, wenn die {{PropertyData/de|Vertical Vector}} auf `True` gesetzt ist.


{{TitleProperty|Objects}}

-    **Base|LinkGlobal**: specifies the object to duplicate in the array.

-    **Count|Integer**: specifies the number of elements in the array.

-    **Expand Array|Bool**: specifies whether to expand the array in the [Tree view](Tree_view.md) to enable the selection of its individual elements. Only available for Link arrays.

-    **Path Object|LinkGlobal**: specifies the object to be used for the path. It must contain {{Value|Edges}} in its [Part TopoShape](Part_TopoShape.md).

-    **Path Subelements|LinkSubListGlobal**: specifies a list of edges of the **Path Object**. If supplied only these edges are used for the path.



### Ansicht


{{TitleProperty|Link}}

Die Eigenschaften dieser Gruppe, mit Ausnahme der ererbten Eigenschaften, stehen nur für Verknüpfungsanordnungen zur Verfügung. Siehe [Std VerknüpfungErstellen](Std_LinkMake/de#Eigenschaften.md) für weitere Informationen.

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

Die Eigenschaften in dieser Gruppe sind ererbte Eigenschaften. Siehe auch [Part Formelement](Part_Feature/de#Eigenschaften.md).

-    **Bounding Box|Bool**: this property is not inherited by Link arrays.

-    **Display Mode|Enumeration**: for Link arrays it can be {{value|Link}} or {{value|ChildView}}. For other arrays it can be: {{value|Flat Lines}}, {{value|Shaded}}, {{value|Wireframe}} or {{value|Points}}

-    **Show In Tree|Bool**
    

-    **Visibility|Bool**
    


{{TitleProperty|Draft}}

-    **Pattern|Enumeration**: not used.

-    **Pattern Size|Float**: not used.


{{TitleProperty|Object style}}

Die Eigenschaften dieser Gruppe werden nicht an Verknüpfungsanordnungen vererbt.



## Skripten

Siehe auch: [Autogenerierte API Dokumentation](https://freecad.github.io/SourceDoc/) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Zum Erstellen einer Pfad-Anordnung wird die Methode `make_path_array` des Draft-Moduls verwendet ({{Version/de|0.19}}). Diese Methode ersetzt die veraltete Methode `makePathArray`.


```python
path_array = make_path_array(base_object, path_object,
                             count=4, extra=App.Vector(0, 0, 0), subelements=None,
                             align=False, align_mode="Original", tan_vector=App.Vector(1, 0, 0),
                             force_vertical=False, vertical_vector=App.Vector(0, 0, 1),
                             use_link=True)
```

-    `base_object`ist das Objekt, das angeordnet werden soll. Es kann auch die Benennung (die Zeichenkette `Label`) eines Objekts im aktuellen Dokument sein.

-    `path_object`: Ist das Pfadobjekt (path object). Es kann auch die Benennung (die Zeichenkette `Label`) eines Objekts im aktuellen Dokument sein.

-    `count`ist die Anzahl der Elemente einer Anordnung.

-    `extra`ist ein Vektor, der jedes Element versetzt.

-    `subelements`ist eine Liste von Kanten im `path_object`, z.B. `["Edge1", "Edge2"]`. Wenn vorhanden, werden nur diese Kanten für den Pfad verwendet.

-   Ist `align` auf `True` gestzt, werden die Elemente abhängig von der Eigenschaft `align_mode`, die die Werte `"Original"`, `"Frenet"` oder `"Tangent"` annehmen kann, entlang des Pfades ausgerichtet.

-    `tan_vector`ist ein Einheitsvektor, der die örtliche Tangentenrichtung der Elemente entlang des Pfades festlegt. Er wird verwendet, wenn `align_mode` auf `"Tangent"` gesetzt ist.

-   Ist `force_vertical` auf `True` gsetzt, wird `vertical_vector` für die lokale Z-Achse der Elemente entlang des Pfades verwendet. Es wird verwendet, wenn `align_mode` auf `"Original"` oder `"Tangent"` gesetzt ist.

-   Ist `use_link` auf `True` gesetzt, werden [App-Links](App_Link/de.md) anstatt normaler Kopien erstellt.

-    `path_array`wird mit der erstellten Anordnung zurückgegeben.

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



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft PathArray/de
