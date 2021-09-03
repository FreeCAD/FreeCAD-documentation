---
- GuiCommand:/de
   Name:Arch Panel Sheet
   Name/de:Arch Tafel Blech
   Workbenches:[Arch](Arch_Workbench/de.md)
   MenuLocation:Arch → Panel tools → Tafel Blatt
   Shortcut:**P** **S**
   SeeAlso:[Arch Tafel](Arch_Panel/de.md), [Arch Tafelschnitt](Arch_Panel_Cut/de.md), [Arch Verschachteln](Arch_Nest/de.md)
---

## Beschreibung

Dieses Werkzeug ermöglicht eine 2D Zeichnung zu erstellen, einschließlich einer beliebigen Anzahl von [Arch Tafelschnitt](Arch_Panel_Cut/de.md) Objekten, oder jedes andere 2D Objekt, wie z.B. diejenigen, die mit [Entwurf Arbeitsbereich](Draft_Workbench/de.md) und [Skizzierer Arbeitsbereich](Sketcher_Workbench/de.md) erstellt wurden. Das Tafelblech wird in der Regel für Layout Schnitte erstellt, die von einer CNC Maschine ausgeführt werden sollen. Diese Blätter können dann in eine [DXF](Draft_DXF/de.md) Datei exportiert werden.

<img alt="" src=images/Arch_Wikihouse_03.jpg  style="width:1024px;">

<img alt="" src=images/Arch_Wikihouse_04.jpg  style="width:1024px;">

*Das obige Bild zeigt, wie Tafelplatten beim Export nach DXF erscheinen.*

## Anwendung

1.  Optional wähle ein oder mehrere [Arch Tafel Schnitt](Arch_Panel_Cut/de.md)-Objekte oder jedes andere 2D-Objekt, das auf der XY-Ebene liegt.
2.  Drücke die **<img src="images/Arch_Panel_Sheet.svg" width=16px> [Arch Tafel Platte](Arch_Panel_Sheet/de.md)**-Schaltfläche oder drücke die Tasten **P**, dann **S**.

## Optionen

-   After the panel sheet is created, with or without child objects, Any other child object can be added/removed to/from the panel sheet by double-clicking it in the tree view and adding or removing objects from its Group folder
-   Double-clicking on the panel in the tree view also allows you to move the objects contained in this sheet, or move its tag
-   It is possible to automatically make panels composed of more than one sheet of a material, by raising its Sheets property
-   Panel Sheets can display a margin, that is useful to make sure a certain space is always present between inner objects and the border of the sheet
-   When Panel sheets are exported to DXF, the outlines, inner holes, tags of their inner children are placed on different layers, as shown on the above image

## Eigenschaften

### Data

-    **Height**: The height of the sheet

-    **Width**: The width of the sheet

-    **Fill Ratio**: The percentage of the sheet area that is filled by cuts (automatic)

-    **Tag Text**: The text to display

-    **Tag Size**: The size of the tag text

-    **Tag Position**: The position of the tag text. Keep (0,0,0) for automatic center position

-    **Tag Rotation**: The rotation of the tag text

-    **Font File**: The font of the tag text

-    **Make Face**: If True, the panel is a Part Face, otherwise a Part Wire

-    **Grain Direction**: This allows you to inform the main direction of the panel fiber (clockwise direction, 0° means up)

### View

-    **Margin**: A margin that can be displayed inside the panel border

-    **Show Margin**: Turns the display of the margin on/off

-    **Show Grain**: Shows a fiber texture (Make Face must be set to True)

## Skripten


**Siehe auch:**

[Arch API](Arch_API/de.md) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

The Panel sheet tool can be used in [macros](macros.md) and from the [Python](Python.md) console by using the following function:


```python
Sheet = makePanelSheet(panels=[], name="PanelSheet")
```

-   Creates a `Sheet` object from `panels`, which is a list of [Arch Panel](Arch_Panel.md) objects.

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

-   [Wikihouse Portierungs Tutorium](Wikihouse_porting_tutorial/de.md)





 
