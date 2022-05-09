---
- GuiCommand   */de
   Name   *Arch BuildingPart
   Name/de   *Architektur GebäudeTeil
   MenuLocation   *Arch → Gebäudeteil
   Workbenches   *[Arch](Arch_Workbench.md)
   Version   *0.18
   SeeAlso   *[Arch Gebäude](Arch_Building/de.md), [Arch Baugrund](Arch_Site/de.md)
---

# Arch BuildingPart/de

## Beschreibung


<div class="mw-translate-fuzzy">

Der GebäudeTeil ersetzt das alte [Arch Geschoss](Arch_Floor/de.md) und [Arch Gebäude](Arch_Building/de.md) Werkzeug durch eine leistungsfähigere Version, mit der nicht nur Geschosse/Etagen/Ebenen, sondern auch alle Arten von Situationen erstellt werden können, in denen verschiedene Architektur/BIM Objekte gruppiert werden sollen und das diese Gruppe als ein Objekt behandelt oder nachgebildet werden soll.


</div>

## Anwendung


<div class="mw-translate-fuzzy">

1.  Wähle wahlweise ein oder mehrere Objekte, die in dein neues Gebäude Teil eingeschlossen werden sollen.
2.  Drücke die **<img src="images/Arch_BuildingPart.svg" width=16px> [Arch GebäudeTeil](Arch_BuildingPart/de.md)** Schaltfläche.


</div>

### Hinweise

GebäudeTeile haben eine eingebaute, implizite [Arch SchnittEbene](Arch_SectionPlane/de.md). <small>(v0.19)</small> 

Diese Ebene ist immer parallel zur GebäudeTeil Basisebene, aber du kannst den Versatz zwischen ihnen angeben. Daher arbeiten alle Werkzeuge, die mit einer Schnittebene arbeiten, wie z.B. [Entwurf Form2DAnsicht](Draft_Shape2DView/de.md) und [TechDraw ArchAnsicht](TechDraw_ArchView/de.md) auch mit GebäudeTeilen.

## Optionen


<div class="mw-translate-fuzzy">

-   Nach der Erstellung eines GebäudeTeil kannst du weitere Objekte durch Ziehen und Ablegen in der Baumansicht oder mit dem **<img src="images/Arch_Add.svg" width=16px> [Arch Hinzufügen](Arch_Add/de.md)** Werkzeug verwenden.
-   Du kannst Objekte, durch Ziehen und Ablegen aus der Baumansicht heraus oder durch verwenden des **<img src="images/Arch_Remove.svg" width=16px> [Arch Entfernen](Arch_Remove.md)** Werkzeugs aus einem GebäudeTeil entfernen.
-   Durch doppelklicken auf das GebäudeTeil Objekt in der Baumansicht wird die [Working Plane](Draft_SelectPlane.md) auf dessen Stelle gesetzt, und das BuildingPart wird aktiv, was bedeutet daß neue Objekte automatisch dazu hinzugefügt werden.

Erneutes Doppelklicken auf das GebäudeTeil deaktiviert es und setzt die Arbeitsebene wieder auf die vorherige Position zurück (in Version 0.19, damit diese Option verfügbar ist, muss sie als true gesetzt werden, im Paneel Ansichtseigenschaften - Interaktion - Doppelklick aktiviert es).

-   Das GebäudeTeil kann in der 3D Ansicht eine Markierung mit einer Beschriftung und einer Niveauanzeige anzeigen.
-   Wenn ein GebäudeTeil verschoben/gedreht wird, werden alle seine Kinder, die entweder keine **Bewegen mit dem Bereitsteller** Eigenschaft haben oder diese aktiviert haben, gemeinsam verschoben/gedreht.
-   Gebäudeteile können [Entwurf Klone](Draft_Clone/de.md) sein.
-   Gebäudeteile können jeden IFC Typ annehmen. Ihre Eigenschaft **IFC Typ** bestimmt ihre Verwendung. Wenn du es auf **Gebäude Geschoss** setzt, verhält es sich wie ein Stockwerk. Wenn du es auf **Gebäude** setzt, verhält es sich wie ein Gebäude, und wenn du es auf **Element Baugruppe** setzt, verhält es sich wie eine Baugruppe. Das Symbol ändert sich entsprechend dieser Einstellung, aber ansonsten hat es keine weiteren Auswirkungen in FreeCAD. Der Export in IFC als der eine oder andere Typ kann jedoch Auswirkungen auf andere BIM Anwendungen haben.


</div>

## Eigenschaften

See also   * [Property editor](Property_editor.md).

An Arch BuildingPart is derived from an [App GeoFeature](App_GeoFeature.md) object and inherits all its properties. It also has the following additional properties   *

### Data


{{TitleProperty|Base}}

-    **Group|LinkList**   * List of referenced objects.

-    **_ Group Touched|Bool|Hidden**
    


{{TitleProperty|Building Part}}

-    **Area|Area**   * The computed floor area of this floor.

-    **Height|Length**   * The height of this object, and of its children objects. The children objects could be, for example, [Arch Walls](Arch_Wall.md). Each wall\'s height must be set to `0` (zero), so the height property of the BuildingPart propagates to the objects inside of it.

-    **Level Offset|Length**   * The level of the (0,0,0) point of this level. This value is added to the `Placement.Base.z` attribute of the BuildingPart, to indicate a vertical offset without actually moving the object. The resulting offset is displayed if **Show Level** is `True`.

-    **Materials Table|Map|Hidden**   * A MaterialName   *SolidIndexesList map that relates material names with solid indexes to be used when referencing this object from other files.

-    **Only Solids|Bool**   * If true, only solids will be collected by this object when referenced from other files.

-    **Saved Inventor|FileIncluded|Hidden**   * This property stores an inventor representation for this object.

-    **Shape|PartShape|Hidden**   * The shape of this object.


{{TitleProperty|Children}}

-    **Height Propagate|Bool**   * If true, the height value propagates to contained objects.


{{TitleProperty|IFC}}

-    **Ifc Data|Map|Hidden**   * IFC data.

-    **Ifc Properties|Map|Hidden**   * IFC properties of this object.

-    **Ifc Type|Enumeration**   * The IFC type of this object.


{{TitleProperty|IFC Attributes}}

-    **Description|String**   * An optional description for this component

-    **Global Id|String**
    

-    **Object Type|String**
    

-    **Overall Height|Length**
    

-    **Overall Width|Length**
    

-    **Partitioning Type|Enumeration**
    

-    **Predefined Type|Enumeration**
    

-    **Tag|String**   * An optional tag for this component.

-    **User Defined Partitioning Type|String**
    

### View


{{TitleProperty|Auto Group}}

-    **Autogroup Autosize|Bool**   * Automatically set the capture box size from the Building Part contents. <small>(v0.20)</small> 

-    **Autogroup Box|Bool**   * Turns auto grouping (and the display of the capture box) on/off. <small>(v0.20)</small> 

-    **Autogroup Margin|Length**   * A margin to use when autosize is turned on. <small>(v0.20)</small> 

-    **Autogroup Size|IntegerList**   * The capture box for newly created objects expressed as \[XMin,YMin,ZMin,XMax,YMax,ZMax\]. <small>(v0.20)</small> 


{{TitleProperty|Building Part}}

-    **Diffuse Color|ColorList|Hidden**   * The individual face colors.

-    **Display Offset|Placement**   * A transformation to apply to the level mark.

-    **Font Name|Font**   * The font to be used for texts.

-    **Font Size|Length**   * The font size of texts.

-    **Line Width|Float**   * The line width of this object.

-    **Origin Offset|Bool**   * If true, when activated, Display offset will affect the origin mark too.

-    **Override Unit|String**   * An optional unit to express levels.

-    **Show Label|Bool**   * If true, when activated, the object\'s label is displayed.

-    **Show Level|Bool**   * If true, show the level.

-    **Show Unit|Bool**   * If true, show the unit on the level tag.


{{TitleProperty|Children}}

-    **Children Line Color|Color**   * The line color to apply to the children of this Building Part.

-    **Children Line Width|Float**   * The line width to apply to the children of this Building Part.

-    **Children Override|Bool**   * If true, the objects contained in this Building Part will adopt these line, color and transparency settings.

-    **Children Shape Color|Color**   * The shape color to apply to the children of this Building Part.

-    **Children Transparency|Percent**   * The transparency to apply to the children of this Building Part.


{{TitleProperty|Clip}}

-    **Auto Cut View|Bool**   * Turn cutting on when activating this level.

-    **Cut Margin|Length**   * The distance between the level plane and the cut line.

-    **Cut View|Bool**   * Cut the view above this level.


{{TitleProperty|Interactions}}

-    **Auto Working Plane|Bool**   * If set to True, the working plane will be kept on Auto mode.

-    **Double Click Activates|Bool**   * If True, double-clicking this object in the tree activates it.

-    **Restore View|Bool**   * If set, the view stored in this object will be restored on double-click.

-    **Save Inventor|Bool**   * If this is enabled, the inventor representation of this object will be saved in the FreeCAD file, allowing to reference it in other files in lightweight mode.

-    **Saved Inventor|FileIncluded|Hidden**   * A slot to save the inventor representation of this object, if enabled.

-    **Set Working Plane|Bool**   * If true, when activated, the working plane will automatically adapt to this Building Part.

-    **View Data|FloatList|Hidden**   * Camera position data associated with this object.

## Scripting


<div class="mw-translate-fuzzy">

## Skripten


**Siehe auch   ***

[Arch API](Arch_API/de.md) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).


</div>


<div class="mw-translate-fuzzy">

Das Gebäudeteil-Werkzeug kann sowohl in [Makros](macros/de.md) als auch aus der [Python](Python/de.md)-Konsole heraus über folgende Funktion angesprochen werden   *


</div>


```python
BuildingPart = makeBuildingPart(objectslist=None)
```

-   Erzeugt ein `Building`-Objekt aus `objectslist`, einer Liste von Objekten.

Beispiel   * 
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


<div class="mw-translate-fuzzy">





</div>



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch BuildingPart/de
