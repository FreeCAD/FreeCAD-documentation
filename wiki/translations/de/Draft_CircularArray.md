---
- GuiCommand:/de
   Name:Draft CircularArray
   Name/de:Draft KreisAnordnung
   MenuLocation:Änderung → Array tools → Kreis-Anordnung
   Workbenches:[Draft](Draft_Workbench/de.md), [Arch](Arch_Workbench/de.md)
   Version:0.19
   SeeAlso:[Draft RechtwinkligeAnordnung](Draft_OrthoArray/de.md), [Draft PolareAnordnung](Draft_PolarArray/de.md), [Draft PfadAnordnung](Draft_PathArray/de.md), [Draft PfadVerknüpfungsanordnung](Draft_PathLinkArray/de.md), [Draft PunktAnordnung](Draft_PointArray/de.md), [Draft PunktVerknüpfungsanordnung](Draft_PointLinkArray/de.md)
---

# Draft CircularArray/de



## Beschreibung

Der Befehl <img alt="" src=images/Draft_CircularArray.svg  style="width:24px;"> **Draft KreisAnordnung** erstellt eine Anordnung aus einem ausgewählten Objekt, indem er Kopien auf konzentrischen Kreisringen positioniert. Der Befehl kann wahlweise eine Verknüpfungsanordnung ([Link](App_Link.md)-Array) erstellen, die effizienter ist als eine normale Anordnung.

Dieser Befehl kann für 2D-Objekte verwendet werden, die mit den Arbeitsbereichen [Draft](Draft_Workbench/de.md) oder [Sketcher](Sketcher_Workbench/de.md) erstellt wurden, aber auch für viele 3D-Objekte, die mit anderen Arbeitsbereichen wie [Part](Part_Workbench/de.md), [PartDesign](PartDesign_Workbench/de.md) oder [Arch](Arch_Workbench/de.md) erstellt wurden.

<img alt="" src=images/Draft_CircularArray_example.png  style="width:400px;"> 
*Draft Kreis-Anordnung*



## Anwendung

Siehe auch: [Draft Fangen](Draft_Snap/de.md).

1.  Optionally select one object.
2.  There are several ways to invoke the command:
    -   Press the **<img src="images/Draft_CircularArray.svg" width=16px> [Draft CircularArray](Draft_CircularArray.md)** button.
    -   Select the **Modification → Array tools → <img src="images/Draft_CircularArray.svg" width=16px> Circular array** option from the menu.
3.  The **Circular array** task panel opens. See [Options](#Options.md) for more information.
4.  If you have not yet selected an object: select one object.
5.  Enter the required parameters in the task panel.
6.  To finish the command do one of the following:
    -   Pick a point in the [3D view](3D_view.md) for the **Center of rotation**.
    -   Press **Enter**.
    -   Press the **OK** button.



## Optionen

-   Enter the **Radial distance** to specify the distance between the circular layers, and between the center and the first circular layer.
-   Enter the **Tangential distance** to specify the distance between the elements on the same circular layer. Must be larger than zero.
-   Enter the **Number of circular layers**. The element at the center counts as one layer. Must be at least {{Value|2}}. The maximum that can be entered in the task panel is {{Value|99}}, but higher values are possible by changing the **Number Circles** property of the array.
-   Enter the **Symmetry** value. This number determines how the elements are distributed. A value of {{Value|3}}, for example, results in a pattern with three equal 120° pie segments. Larger values for the **Symmetry** and the **Tangential distance** result in fewer or even no elements on the inner layers.
-   Pick a point in the [3D view](3D_view.md), note that this will also finish the command, or type coordinates for the **Center of rotation**. The rotation axis of the array will pass through this point. It is advisable to move the pointer out of the [3D view](3D_view.md) before entering coordinates.
-   Press the **Reset point** button to reset the **Center of rotation** to the origin.
-   If the **Fuse** checkbox is checked overlapping elements in the array are fused. This does not work for Link arrays.
-   If the **Link array** checkbox is checked a Link array instead of a regular array is created. A Link array is more efficient because its elements are [App Link](App_Link.md) objects.
-   Press **Esc** or the **Cancel** button to abort the command.



## Hinweise

-   The default rotation axis for the array is the positive Z axis. This can be changed by editing its **Axis** property.
-   A Draft CircularArray can be turned into a [Draft OrthoArray](Draft_OrthoArray.md) or a [Draft PolarArray](Draft_PolarArray.md) by changing its **Array Type** property.
-   A Link array cannot be turned into a regular array or vice versa. The type of array must be decided at creation time.



## Einstellungen

Siehe auch: [Voreinstellungseditor](Preferences_Editor/de.md) und [Draft Einstellungen](Draft_Preferences/de.md).

-   Um die Anzahl der Dezimalstellen für die Eingabe der Koordinaten und Abstände zu ändern: **Bearbeiten → Eigenschaften... → Allgemein → Einheiten → Einheiten-Einstellungen → Anzahl der Nachkommastellen**



## Eigenschaften

Siehe [Draft RechtwinkligeAnordnung](Draft_OrthoArray/de#Eigenschaften.md).



## Skripten

Siehe auch: [Autogenerierte API Dokumentation](https://freecad.github.io/SourceDoc/) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Zum Erstellen einer Kreis-Anordnung wird die Methode `make_array` des Draft-Moduls verwendet ({{Version/de|0.19}}). Diese Methode ersetzt die veraltete Methode `makeArray`. Die Methode `make_array` kann [Draft RechtwinkligeAnordnungen](Draft_OrthoArray/de.md), [Draft PolareAnordnungen](Draft_PolarArray.md) und Draft Kreis-Anordnungen erstellen. Für jede Anordnungsart stehen eine oder mehrere Wrapper-Methoden zur Verfügung.

Die Hauptmethode:


```python
array = make_array(base_object, arg1, arg2, arg3, arg4=None, arg5=None, arg6=None, use_link=True)
```

The wrapper for circular arrays is:


```python
array = make_circular_array(base_object,
                            r_distance=100, tan_distance=50,
                            number=3, symmetry=1,
                            axis=App.Vector(0, 0, 1), center=App.Vector(0, 0, 0),
                            use_link=True)
```

-    `base_object`is the object to be arrayed. It can also be the `Label` (string) of an object in the current document.

-    `r_distance`and `tan_distance` are the radial and tangential distances between the elements.

-    `number`is the number of circular layers in the pattern, the original object counts as the first layer.

-    `symmetry`is an integer used in some calculations that affect the way the elements are distributed around the circumferences. Usual values are from 1 to 6. Higher values are not recommended and will make the elements in the inner layers disappear.

-    `axis`and `center` are vectors that describe the direction of the axis of rotation, and a point through which that axis passes.

-   If `use_link` is `True` the created elements are [App Links](App_Link.md) instead of regular copies.

-    `array`is returned with the created array object.

Beispiel:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

tri = Draft.make_polygon(3, 600)

array = Draft.make_circular_array(tri, 1800, 1200, 4, 1)
doc.recompute()
```



---
![](images/Button_right.svg) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft CircularArray/de
