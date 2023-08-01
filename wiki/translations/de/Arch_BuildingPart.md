---
- GuiCommand:/de
   Name:Arch BuildingPart
   Name/de:Arch Gebäudeteil
   MenuLocation:Arch → Gebäudeteil
   Workbenches:[Arch](Arch_Workbench/de.md)
   Version:0.18
   SeeAlso:[Arch Gebäude](Arch_Building/de.md), [Arch Grundstück](Arch_Site/de.md)
---

# Arch BuildingPart/de



## Beschreibung

Das Werkzeug Gebäudeteil ersetzt die alten Werkzeuge [Arch Geschoss](Arch_Floor/de.md) und [Arch Gebäude](Arch_Building/de.md) durch eine leistungsfähigere Version, die nicht nur für Geschosse/Etagen/Ebenen verwendet werden kann, sondern auch für alle möglichen Situationen, in denen verschiedene Arch- oder BIM-Objekte gruppiert werden sollen, um diese Gruppe als ein Objekt zu verwenden oder zu vervielfältigen.



## Anwendung

1.  Wahlweise ein oder mehrere Objekte auswählen, die in dem neuen Gebäudeteil enthalten sein sollen.
2.  Die Schaltfläche **<img src="images/Arch_BuildingPart.svg" width=16px> [Arch Gebäudeteil](Arch_BuildingPart/de.md)** drücken.



### Hinweise

Gebäudeteile haben eine eingebaute, implizite [Arch SchnittEbene](Arch_SectionPlane/de.md).

Diese Ebene ist immer parallel zur GebäudeTeil Basisebene, aber du kannst den Versatz zwischen ihnen angeben. Daher arbeiten alle Werkzeuge, die mit einer Schnittebene arbeiten, wie z.B. [Entwurf Form2DAnsicht](Draft_Shape2DView/de.md) und [TechDraw ArchAnsicht](TechDraw_ArchView/de.md) auch mit GebäudeTeilen.



## Optionen


<div class="mw-translate-fuzzy">

-   Nach der Erstellung eines Gebäudeteils können weitere Objekte durch Ziehen und Ablegen in der Baumansicht hinzugefügt werden oder durch Verwenden des Werkzeugs **<img src="images/Arch_Add.svg" width=16px> [Arch Hinzufügen](Arch_Add/de.md)**.
-   Objekte können, durch Ziehen und Ablegen aus der Baumansicht heraus aus einem Gebäudeteil entfernt werden oder durch Verwenden des Werkzeugs **<img src="images/Arch_Remove.svg" width=16px> [Arch Entfernen](Arch_Remove/de.md)**.
-   Mit einem Doppelklick auf den Gebäudeteil (BuildingPart-Objekt) in der Baumansicht wird die [Arbeitsebene](Draft_SelectPlane/de.md) auf seine Position gesetzt, und der Gebäudeteil wird aktiviert, was bedeutet daß neue Objekte automatisch zu ihm hinzugefügt werden.

Erneutes Doppelklicken auf den Gebäudeteil deaktiviert ihn und setzt die Arbeitsebene wieder auf die vorherige Position zurück (in version 0.19 muss diese Option im Eigenschafteneditor unter Ansicht - Interaction - Double Click Activates auf true gesetzt werden, damit sie zur Verfügung steht).

-   Das Gebäudeteil-Objekt kann in der 3D-Ansicht eine Markierung mit einer Benennung und einer Höhenangabe anzeigen.
-   Wenn ein Gebäudeteil verschoben oder gedreht wird, werden alle abhängigen Objekte, die entweder die {{PropertyData/de|Move With Host}} nicht besitzen oder bei denen diese aktiviert wurde, mit ihm zusammen verschoben bzw. gedreht.
-   Gebäudeteile können [Draft Klone](Draft_Clone/de.md) sein.
-   Gebäudeteile können jeden IFC-Typ annehmen. Ihre Eigenschaft **Ifc Type** bestimmt ihre Verwendung. Ist sie auf **Building Storey** gesetzt, verhält er sich wie ein Stockwerk. Ist sie auf **Building** gesetzt, verhält er sich wie ein Gebäude, und ist sie auf **Element Assembly** gesetzt, verhält er sich wie eine Baugruppe. Das Symbol ändert sich entsprechend dieser Einstellung, hat aber ansonsten keine weiteren Auswirkungen in FreeCAD. Der Export nach IFC als der eine oder andere Typ kann jedoch Auswirkungen auf andere BIM-Anwendungen haben.
-   Gebäudeteile ermöglichen das Festlegen einer **Auto-group capture box**. Nachfolgende Draft- und Arch-Objekte oder alles was Draft.autogroup() verwendet, weden automatisch zum Gebäudeteil hinzugefügt, wenn sie sich vollständig innerhalb der Auswahl-Box befinden. {{Version/de|0.20}}


</div>



## Eigenschaften

Siehe auch: [Eigenschafteneditor](Property_editor/de.md).

Ein Arch Gebäudeteil (BuildingPart-Objekt) wird von einem [App GeoFeature](App_GeoFeature/de.md) abgeleitet und erbt alle seine Eigenschaften. Außerdem hat es die folgenden zusätzlichen Eigenschaften:



### Daten


{{TitleProperty|Basis}}

-    **Group|LinkList**: List of referenced objects.

-    **_ Group Touched|Bool|Hidden**
    


{{TitleProperty|Building Part}}

-    **Area|Area**: The computed floor area of this floor.

-    **Height|Length**: The height of this object, and of its children objects. The children objects could be, for example, [Arch Walls](Arch_Wall.md). Each wall\'s height must be set to `0` (zero), so the height property of the BuildingPart propagates to the objects inside of it.

-    **Level Offset|Length**: The level of the (0,0,0) point of this level. This value is added to the `Placement.Base.z` attribute of the BuildingPart, to indicate a vertical offset without actually moving the object. The resulting offset is displayed if **Show Level** is `True`.

-    **Materials Table|Map|Hidden**: A MaterialName:SolidIndexesList map that relates material names with solid indexes to be used when referencing this object from other files.

-    **Only Solids|Bool**: If true, only solids will be collected by this object when referenced from other files.

-    **Saved Inventor|FileIncluded|Hidden**: This property stores an inventor representation for this object.

-    **Shape|PartShape|Hidden**: The shape of this object.


{{TitleProperty|Children}}

-    **Height Propagate|Bool**: If true, the height value propagates to contained objects.


{{TitleProperty|IFC}}

-    **Ifc Data|Map|Hidden**: IFC data.

-    **Ifc Properties|Map|Hidden**: IFC properties of this object.

-    **Ifc Type|Enumeration**: The IFC type of this object.


{{TitleProperty|IFC Attributes}}

-    **Description|String**: An optional description for this component

-    **Global Id|String**
    

-    **Object Type|String**
    

-    **Overall Height|Length**
    

-    **Overall Width|Length**
    

-    **Partitioning Type|Enumeration**
    

-    **Predefined Type|Enumeration**
    

-    **Tag|String**: An optional tag for this component.

-    **User Defined Partitioning Type|String**
    



### Ansicht


{{TitleProperty|Auto Group}}

-    **Autogroup Autosize|Bool**: Automatically set the capture box size from the Building Part contents. <small>(v0.20)</small> 

-    **Autogroup Box|Bool**: Turns auto grouping (and the display of the capture box) on/off. <small>(v0.20)</small> 

-    **Autogroup Margin|Length**: A margin to use when autosize is turned on. <small>(v0.20)</small> 

-    **Autogroup Size|IntegerList**: The capture box for newly created objects expressed as \[XMin,YMin,ZMin,XMax,YMax,ZMax\]. <small>(v0.20)</small> 


{{TitleProperty|Building Part}}

-    **Diffuse Color|ColorList|Hidden**: The individual face colors.

-    **Display Offset|Placement**: A transformation to apply to the level mark.

-    **Font Name|Font**: The font to be used for texts.

-    **Font Size|Length**: The font size of texts.

-    **Line Width|Float**: The line width of this object.

-    **Origin Offset|Bool**: If true, when activated, Display offset will affect the origin mark too.

-    **Override Unit|String**: An optional unit to express levels.

-    **Show Label|Bool**: If true, when activated, the object\'s label is displayed.

-    **Show Level|Bool**: If true, show the level.

-    **Show Unit|Bool**: If true, show the unit on the level tag.


{{TitleProperty|Children}}

-    **Children Line Color|Color**: The line color to apply to the children of this Building Part.

-    **Children Line Width|Float**: The line width to apply to the children of this Building Part.

-    **Children Override|Bool**: If true, the objects contained in this Building Part will adopt these line, color and transparency settings.

-    **Children Shape Color|Color**: The shape color to apply to the children of this Building Part.

-    **Children Transparency|Percent**: The transparency to apply to the children of this Building Part.


{{TitleProperty|Clip}}

-    **Auto Cut View|Bool**: Turn cutting on when activating this level.

-    **Cut Margin|Length**: The distance between the level plane and the cut line.

-    **Cut View|Bool**: Cut the view above this level.


{{TitleProperty|Interactions}}

-    **Auto Working Plane|Bool**: If set to True, the working plane will be kept on Auto mode.

-    **Double Click Activates|Bool**: If True, double-clicking this object in the tree activates it.

-    **Restore View|Bool**: If set, the view stored in this object will be restored on double-click.

-    **Save Inventor|Bool**: If this is enabled, the inventor representation of this object will be saved in the FreeCAD file, allowing to reference it in other files in lightweight mode.

-    **Saved Inventor|FileIncluded|Hidden**: A slot to save the inventor representation of this object, if enabled.

-    **Set Working Plane|Bool**: If true, when activated, the working plane will automatically adapt to this Building Part.

-    **View Data|FloatList|Hidden**: Camera position data associated with this object.



## Skripten


**Siehe auch:**

[Arch API](Arch_API/de.md) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Das Werkzeug Gebäudeteil kann sowohl in [Makros](macros/de.md) als auch von der [Python](Python/de.md)-Konsole aus mit folgender Funktion verwendet werden:


```python
BuildingPart = makeBuildingPart(objectslist=None)
```

-   Erzeugt ein `Building`-Objekt aus `objectslist`, einer Liste von Objekten.

Beispiel: 
```python
import FreeCAD, Draft, Arch

p1 = FreeCAD.Vector(0, 0, 0)
p2 = FreeCAD.Vector(2000, 0, 0)
baseline = Draft.makeLine(p1, p2)
baseline2 = Draft.makeLine(p1, -1*p2)

Wall1 = Arch.makeWall(baseline, length=None, width=150, height=2000)
Wall2 = Arch.makeWall(baseline2, length=None, width=150, height=1800)
FreeCAD.ActiveDocument.recompute()

BuildingPart = Arch.makeBuildingPart([Wall1, Wall2])

Floor = Arch.makeFloor([BuildingPart])
Building = Arch.makeBuilding([Floor])
Site = Arch.makeSite(Building)
FreeCAD.ActiveDocument.recompute()
```



---
![](images/Button_right.svg) [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch BuildingPart/de
