---
- GuiCommand   */de
   Name   *Draft OrthoArray
   Name/de   *Entwurf AnordnungRechtwinklig
   MenuLocation   *Modifikation → Anordnung Werkzeuge → Anordnung
   Workbenches   *[Entwurf](Draft_Workbench/de.md), [Architektur](Arch_Workbench/de.md)
   Version   *0.19
   SeeAlso   *[Entwurf PolarAnordnung](Draft_PolarArray/de.md), [Entwurf KreisAnordnung](Draft_CircularArray/de.md), [verknüpfte Pfadanordnung](Draft_PathArray/de.md), [Entwurf Punkteanordnung](Draft_PointArray/de.md), [verknüpfte Punkteanordnung](Draft_PointLinkArray/de.md)
---

# Draft OrthoArray/de

## Beschreibung

Die <img alt="" src=images/Draft_OrthoArray.svg  style="width   *24px;"> **Draft OrthoArray**-Anweisung erstellt eine orthogonale (3-Achsen) Anordnung aus einem ausgewählten Objekt. Die Anweisung kann auch ein [Verknüpungsmuster](App_Link/de.md) erzeugen. Dies ist effizienter, als eine rechtwinklige Feldanordnung (orthogonale Anordnung).

Diese Anweisung kann für 2D-Objekte angewendet werden, die mit der [Arbeitsbereich Entwurf](Draft_Workbench/de.md) oder mit dem [Arbeitsbereich Skizzierer](Sketcher_Workbench/de.md) erstellt wurden, aber auch auf viele 3D-Objekte, die mit anderenArbeitsbereichen erstellt wurden, wie dem [Arbeitsbereich Part](Part_Workbench/de.md), [Arbeitsbereich PartDesign](PartDesign_Workbench/de.md) oder dem [Arbeitsbereich Architektur](Arch_Workbench/de.md).

<img alt="" src=images/Draft_Array_example.png  style="width   *300px;"> 
*Entwurf orthogonale Anordnung*

## Anwendung

1.  Wahlweise ein Objekt auswählen.
2.  Es gibt mehrere Wege, die Anweisung aufzurufen   *
    -   Die Schaltfläche **<img src="images/Draft_OrthoArray.svg" width=16px> [Draft OrthoArray](Draft_OrthoArray.md)** anzuklicken.
    -   Den Menüpunkt **Modification → Array tools → <img src="images/Draft_OrthoArray.svg" width=16px> Array** wählen.
3.  Die **Orthogonal array**-Aufgabenansicht wird geöffnet. Siehe auch [Options](#Options.md).
4.  Objekt auswählen, wenn noch keines ausgewählt wurde.
5.  Die erforderlichen Parameter in die Ansicht Aufgaben eingeben.
6.  Beenden der Auswührung der Anweisung   *
    -   In die [3DAnsicht](3D_view/de.md) klicken.
    -   Drücke **Enter**.
    -   Die Schaltfläche **OK** anklicken.

## Optionen

-   Die**Number of elements** für die X, Y and Z-Richtung eingeben. Die Zahl muss mindestens {{Value|1}} für jede Richtung sein.
-   Das **X-Interval** eingeben, um den Versatz der Elemente in X-Richtung festzulegen. Für ein rechteckiges Feld müssen die Werte für Y und Z {{Value|0}} sein.
-   Das **Y-Interval** eingeben, um den Versatz der Elemente in Y-Richtung festzulegen. Für ein rechteckiges Feld müssen die Werte für X und Z {{Value|0}} sein.
-   Das **Z-Interval** eingeben, um den Versatz der Elemente in Z-Richtung festzulegen. Für ein rechteckiges Feld müssen die Werte für X und Y {{Value|0}} sein.
-   Auf die **Reset X, Y oder Z**-Schaltfläche klicken, um den Versatz in der gegangenen Richtung zurück zu den Vorgabewerten zurück zu setzen.
-   Ist das **Fuse**-Kästchen angehakt, werden überlappende Elemente im Feld miteinander verschmolzen. Das funktioniert nicht bei Verknüpften Feldern (link arrays).
-   Ist das **Link array**-Kästchen angehakt, wird ein Verknüpftes Feld anstelle eines regulären Feldes erstellt. Ein Verknüpftes Feld ist effizienter, weil seine Elemente von [Anwendungsverknüpfungen](App_Link/de.md) Objekte sind.
-   Mit der **Esc**-Taste oder der **Cancel**-Schaltfläche kann die Ausführung abgebrochen werden.

## Hinweise

-   Ein Entwurfs-OrthoFeld kann in ein [Entwurf Polares Feld](Draft_PolarArray/de.md) oder ein [Kreisfeld](Draft_CircularArray/de.md) durch die Änderung seiner **Feldtyp**-Eigenschaft umgewandelt werden.
-   Ein Verknüpfungsfeld (Link array) kann nicht in ein reguläres Feld und umgekehrt umgewandelt werden. Die Feldart wird zum Erstellungszeitpunkt bestimmt.

## Einstellungen

Siehe auch   * [Eigenschaftseditor](Preferences_Editor/de.md) und [Entwurfseigenschaften](Draft_Preferences/de.md).

-   Um die Anzahl der Dezimalstellen für die Eingabe der Koordinaten zu ändern   * **Bearbeiten → Eigenschaften... → Allgemein → Einheiten → Einheiten-Einstellungen → Anzahl der Nachkommastellen**

## Eigenschaften

Siehe auch   * [Eigenschaftseditor](property_editor/de.md).

Die Entwurfs-OrthoFeld Anweisung, die [Entwurf PolarAnordnungsanweisung](Draft_PolarArray/de.md) und die [Entwurf KreisAnordnungsanweisung](Draft_CircularArray/de.md) erstellen das gleiche Objekt. Dieses Objekt ist von einem [Part Formelement](Part_Feature/de.md)-Objekt abgeleitet und erbt alle Eigenschaften, mit Ausnahme einiger Ansichtseigenschaften, die nicht von Verknüpfungsfeldern geerbt wurden. Die folgenden Eigenschaften gibt es zusätzlich, wenn nicht anders angegeben   *

### Daten


{{TitleProperty|Verknüpfung}}

Die Eigenschaften dieser Gruppe gibt es nur für Vernüpfte Felder (link arrays). Siehe auch [Std VernüpfungMachen](Std_LinkMake/de#Eigenschaften.md).

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
    


{{TitleProperty|Kreisanordnung}}

Die Eigenschaften dieser Gruppe sind vor ortogonalen und polaren Feldern verborgen.

-    **Number Circles|Integer**   * specifies the number of circular layers. Must be at least {{Value|2}}.

-    **Radial Distance|Distance**   * specifies the distance between circular layers.

-    **Symmetry|Integer**   * specifies the number of symmetry lines. This number changes the distribution of the elements in the array.

-    **Tangential Distance|Distance**   * specifies the distance between elements in the same circular layer. Must be larger than zero.


{{TitleProperty|Objekte}}

-    **Array Type|Enumeration**   * specifies the type of array, which can be {{value|ortho}}, {{value|polar}} or {{value|circular}}.

-    **Axis Reference|LinkGlobal**   * specifies the object and edge to be used instead of the **Axis** and **Center** properties. Not used for orthogonal arrays.

-    **Base|Link**   * specifies the object to duplicate in the array.

-    **Count|Integer**   * (read-only) specifies the total number of elements in the array. Only available for Link arrays.

-    **Expand Array|Bool**   * specifies whether to expand the array in the [Tree view](Tree_view.md) to enable the selection of its individual elements. Only available for Link arrays.

-    **Fuse|Bool**   * specifies if overlapping elements in the array are fused or not. Not used for Link arrays.


{{TitleProperty|Orthogonales Feld}}

The properties in this group are hidden for circular arrays and polar arrays.

-    **Interval X|VectorDistance**   * specifies the interval between elements in the X direction.

-    **Interval Y|VectorDistance**   * specifies the interval between elements in the Y direction.

-    **Interval Z|VectorDistance**   * specifies the interval between elements in the Z direction.

-    **Number X|Integer**   * specifies the number of elements in the X direction. Must be at least {{Value|1}}.

-    **Number Y|Integer**   * specifies the number of elements in the Y direction. Must be at least {{Value|1}}.

-    **Number Z|Integer**   * specifies the number of elements in the Z direction. Must be at least {{Value|1}}.


{{TitleProperty|Polares Feld}}

The properties in this group are hidden for circular arrays and orthogonal arrays.

-    **Angle|Angle**   * specifies the aperture of the circular arc. Use {{value|360&#176;}} for a full circle.

-    **Interval Axis|VectorDistance**   * specifies the interval between elements in the **Axis** direction.

-    **Number Polar|Integer**   * specifies the number of elements in the polar direction.


{{TitleProperty|Polar/circular array}}

Die Eigenschaften dieser Gruppe sind vor orthogonalen Feldern verborgen.

-    **Axis|Vector**   * specifies the direction of the axis of the array.

-    **Center|VectorDistance**   * specifies the center point of the array. The axis of the array passes through this point. For circular arrays it is an offset from the **Placement** of the **Base** object.

### Ansicht


{{TitleProperty|Verknüpfung}}

The properties in this group, with the exception of the inherited property, are only available for Link arrays. See [Std LinkMake](Std_LinkMake#Properties.md) for more information.

-    **Draw Style|Enumeration**
    

-    **Line Width|FloatConstraint**
    

-    **Override Material|Bool**
    

-    **Point Size|FloatConstraint**
    

-    **Selectable|Bool**   * this is an inherited property that appears in the Selection group for other arrays

-    **Shape Material|Material**
    


{{TitleProperty|Basis}}

Die Eigenschaften dieser Gruppe, mit Ausnahme der vererbten Eigenschaft, gibt es nur für verknüpfte Anordnungen.Siehe auch [Std LinkMake](Std_LinkMake#Properties.md).

-    **Child View Provider|PersistentObject|Hidden**
    

-    **Material List|MaterialList|Hidden**
    

-    **Override Color List|ColorList|Hidden**
    

-    **Override Material List|BoolList|Hidden**
    

-    **Proxy|PythonObject|Hidden**   * this is an inherited property.


{{TitleProperty|Zeige Auswahlmöglichkeiten}}

Die Eigenschaften in dieser Gruppe sind vererbte Eigenschaften. Siehe auch [Part Formelement](Part_Feature/de#Eigenschaften.md).

-    **Bounding Box|Bool**   * diese Eigenschaft ist nicht durch Verknüpfungsfelder vererbt.

-    **Display Mode|Enumeration**   * für Verknüpfungsfelder kann es {{value|Link}} oder {{value|ChildView}} sein. Für andere Felder können es   * {{value|Flat Lines}}, {{value|Shaded}}, {{value|Wireframe}} oder {{value|Points}} sein.

-    **Show In Tree|Bool**
    

-    **Visibility|Bool**
    


{{TitleProperty|Entwurf}}

-    **Pattern|Enumeration**   * nicht verwendet.

-    **Pattern Size|Float**   * nicht verwendet.


{{TitleProperty|Objectstil}}

Die Eigenschaften dieser Gruppe sind nicht durch Verknüpfungsfelder vererbt.

## Skripten

Siehe auch   * [Autogenerated API documentation](https   *//freecad.github.io/SourceDoc/) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

### Parametrische Anordnung 

Um ein parametrisches rechteckiges Feld zu erstellen, wird die `make_array`-Methode (<small>(v0.19)</small> ) des Entwurfmodules verwendet. Diese Methode ersetzt die veraltete `makeArray`-Methode. Die `make_array`-Methode kann Entwurfs-OrthoFelder, [Entwurf PolarAnordnung](Draft_PolarArray/de.md) und [Entwurf Kreisanordnung](Draft_CircularArray/de.md) erstellen. Für jeden Feldtyp gibt es ein oder mehrere Verbinder (wrappers).

Die main Methode   *


```python
array = make_array(base_object, arg1, arg2, arg3, arg4=None, arg5=None, arg6=None, use_link=True)
```

Die Verbinder (wrapper) für orthogonale Anordnungen sind   *


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

Die Verbinder (wrapper) für rechteckige Anordnungen sind   *


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

Beispiel   *


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

Beispiel   *


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
![](images/Right_arrow.png) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft OrthoArray/de
