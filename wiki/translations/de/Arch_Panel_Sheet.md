---
- GuiCommand:/de
   Name:Arch Panel Sheet
   Name/de:Arch Tafel Blech
   Workbenches:[Arch](Arch_Workbench/de.md)
   MenuLocation:Arch → Panel tools → Tafel Blatt
   Shortcut:**P** **S**
   SeeAlso:[Arch Tafel](Arch_Panel/de.md), [Arch Tafelschnitt](Arch_Panel_Cut/de.md), [Arch Verschachteln](Arch_Nest/de.md)
---

# Arch Panel Sheet/de


</div>

## Beschreibung


<div class="mw-translate-fuzzy">

Dieses Werkzeug ermöglicht eine 2D Zeichnung zu erstellen, einschließlich einer beliebigen Anzahl von [Arch Tafelschnitt](Arch_Panel_Cut/de.md) Objekten, oder jedes andere 2D Objekt, wie z.B. diejenigen, die mit [Entwurf Arbeitsbereich](Draft_Workbench/de.md) und [Skizzierer Arbeitsbereich](Sketcher_Workbench/de.md) erstellt wurden. Das Tafelblech wird in der Regel für Layout Schnitte erstellt, die von einer CNC Maschine ausgeführt werden sollen. Diese Blätter können dann in eine [DXF](Draft_DXF/de.md) Datei exportiert werden.


</div>

<img alt="" src=images/Arch_Wikihouse_03.jpg  style="width:1024px;">

<img alt="" src=images/Arch_Wikihouse_04.jpg  style="width:1024px;">

*Das obige Bild zeigt, wie Tafelplatten beim Export nach DXF erscheinen.*

## Anwendung


<div class="mw-translate-fuzzy">

1.  Optional wähle ein oder mehrere [Arch Tafel Schnitt](Arch_Panel_Cut/de.md)-Objekte oder jedes andere 2D-Objekt, das auf der XY-Ebene liegt.
2.  Drücke die **<img src="images/Arch_Panel_Sheet.svg" width=16px> [Arch Tafel Platte](Arch_Panel_Sheet/de.md)**-Schaltfläche oder drücke die Tasten **P**, dann **S**.


</div>

## Optionen

-   After the panel sheet is created, with or without child objects, Any other child object can be added/removed to/from the panel sheet by double-clicking it in the tree view and adding or removing objects from its Group folder
-   Double-clicking on the panel in the tree view also allows you to move the objects contained in this sheet, or move its tag
-   It is possible to automatically make panels composed of more than one sheet of a material, by raising its Sheets property
-   Panel Sheets can display a margin, that is useful to make sure a certain space is always present between inner objects and the border of the sheet
-   When Panel sheets are exported to DXF, the outlines, inner holes, tags of their inner children are placed on different layers, as shown on the above image

## Eigenschaften

### Data


<div class="mw-translate-fuzzy">

### Daten

-    {{PropertyData/de|Height}}: Die Höhe des Blattes

-    {{PropertyData/de|Width}}: Die Breite des Blattes

-    {{PropertyData/de|Fill Ratio}}(v0.??): Der Prozentsatz des Blechs, der von Schnitten belegt wird (automatisch)

-    {{PropertyData/de|Tag Text}}: Der anzuzeigende Kennzeichnungstext

-    {{PropertyData/de|Tag Size}}: Die Größe des Kennzeichnungstextes

-    {{PropertyData/de|Tag Position}}: Die Position des Kennzeichnungstextes. Automatische Mittenposition bei (0,0,0)

-    {{PropertyData/de|Tag Rotation}}: Die Drehung des Kennzeichnungstextes

-    {{PropertyData/de|Font File}}: Die Schriftart des Kennzeichnungstextes

-    {{PropertyData/de|Make Face}}: Falls True, ist das Blech eine Part Fläche, anderenfalls ein Part Linienzug

-    {{PropertyData/de|Grain Direction}}: Gibt einen Winkel für die (Holz)-Maserung an (im Uhrzeigersinn, 0° bedeutet oben)

-    {{PropertyData/de|Group}}(v0.??): Die verknüpften Paneel-Schnitte

-    {{PropertyData/de|Rotations}}(v0.??): Eine Liste möglicher Rotationen für den Satz

-    {{PropertyData/de|Scale}}(v0.??): Gibt die Skalierung an, die auf jede Panelansicht angewandt wird


</div>

### View


<div class="mw-translate-fuzzy">

### Ansicht

-    {{PropertyView/de|Margin}}: Ein Rand, der innerhalb der Grenze angezeigt werden kann

-    {{PropertyView/de|Show Margin}}: Schaltet die Anzeige des Randes ein/aus

-    {{PropertyView/de|Show Grain}}: Schaltet die Anzeige der (Holz)-Maserung ein/aus (Make Face muss auf \'true\' gesetzt sein)


</div>

## Scripting


<div class="mw-translate-fuzzy">

## Skripten


**Siehe auch:**

[Arch API](Arch_API/de.md) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).


</div>


<div class="mw-translate-fuzzy">

Das Tafelblechwerkzeug kann in [Makros](Macros/de.md) und aus der [Python](Python/de.md)-Konsole aus mit folgender Funktion verwendet werden:


</div>


```python
Sheet = makePanelSheet(panels=[], name="PanelSheet")
```

-   Erstellt ein `sheet`-Objekt aus `panels`, welches eine Liste von [Arch Panel](Arch_Panel.md)-Objekten ist.

Beispiel:


```python
import FreeCAD, Draft, Arch

Rect = Draft.makeRectangle(500, 200)
Polygon = Draft.makePolygon(5, 750)

p1 = FreeCAD.Vector(1000, 0, 0)
p2 = FreeCAD.Vector(2000, 400, 0)
p3 = FreeCAD.Vector(1250, 800, 0)
Wire = Draft.makeWire([p1, p2, p3], closed=True)

Panel1 = Arch.makePanel(Rect, thickness=36)
Panel2 = Arch.makePanel(Polygon, thickness=36)
Panel3 = Arch.makePanel(Wire, thickness=36)
FreeCAD.ActiveDocument.recompute()

Cut1 = Arch.makePanelCut(Panel1)
Cut2 = Arch.makePanelCut(Panel2)
Cut3 = Arch.makePanelCut(Panel3)
Cut1.ViewObject.LineWidth = 3
Cut2.ViewObject.LineWidth = 3
Cut3.ViewObject.LineWidth = 3
FreeCAD.ActiveDocument.recompute()

Sheet = Arch.makePanelSheet([Cut1, Cut2, Cut3])
```

## Tutorien


<div class="mw-translate-fuzzy">

-   [Wikihouse Portierungs Tutorium](Wikihouse_porting_tutorial/de.md)


</div>



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch Panel Sheet/de
