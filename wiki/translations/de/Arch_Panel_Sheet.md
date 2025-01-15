---
 GuiCommand:
   Name: Arch Panel Sheet
   Name/de: Arch Panel Plattenzeichnung
   MenuLocation: Utils , Plattenwerkzeuge , Plattenzeichnung
   Workbenches: BIM_Workbench/de
   Version: 0.17
   SeeAlso: Arch_Panel/de, Arch_Panel_Cut/de, Arch_Nest/de
---

# Arch Panel Sheet/de



## Beschreibung

Dieses Werkzeug ermöglicht eine 2D-Zeichnung zu erstellen, einschließlich einer beliebigen Anzahl von [Arch Plattenzuschnitt](Arch_Panel_Cut/de.md) Objekten oder anderen 2D-Objekten, wie z.B. diejenigen, die mit den Arbeitsbereichen [Draft](Draft_Workbench/de.md) und [Sketcher](Sketcher_Workbench/de.md) erstellt wurden. Die Plattenzeichnung wird in der Regel für die Anordnung von Plattenzuschnitten (Beschnittkonturen) erstellt, die von einer CNC-Maschine ausgeschnitten werden sollen. Diese Zeichnungsblatter können dann in eine [DXF](Draft_DXF/de.md)-Datei exportiert werden.

<img alt="" src=images/Arch_Wikihouse_03.jpg  style="width:600px;">

<img alt="" src=images/Arch_Wikihouse_04.jpg  style="width:600px;">

*Das obige Bild zeigt, wie Plattenzeichnungen beim Export nach DXF erscheinen.*



## Anwendung

1.  Wahlweise ein oder mehrere [Arch Plattenzuschnitt](Arch_Panel_Cut/de.md)-Objekte auswählen oder jedes andere 2D-Objekt, das auf der XY-Ebene liegt.
2.  Den Menüeintrag **Utils → Plattenwerkzeuge → <img src="images/Arch_Panel_Sheet.svg" width=16px> Plattenzeichnung** auswählen.
3.  Die gewünschten Eigenschaften anpassen.



## Optionen

-   Nachdem die Plattenzeichnung erstellt wurde, mit oder ohne eingefügte Objekte, kann ein beliebiges Objekt eingefügt oder entfernt werden, indem es in der Baumansicht doppelt angeklickt wird und Objekte seinen Gruppenordnern hinzugefügt werden bzw. daraus entfernt werden.
-   Ein Doppelklick auf die Platte in der Baumansicht ermöglicht auch die enthaltenen Objekte zu verschieben oder seine Beschriftung zu verschieben.
-   Es ist möglich automatisch Platten aus mehr als einer Materiallage zu erstellen, indem\... (by raising its Sheets property)
-   Plattenzeichnungen können Ränder darstellen. Das hilft sicherzustellen, dass stets ein festgelegter Bereich zwischen den inneren Objekten und dem Zeichnungsrand vorhanden ist.
-   Werden Plattenzeichnungen in eine DXF-Datei exportiert, werden Konturen, enthaltene Löcher und Beschriftungen ihrer enthaltenen Objekte auf verschiedene Layer abgelegt, wie in der obigen Abbildung dargestellt.



## Eigenschaften



### Daten

-    {{PropertyData/de|Height}}: Die Höhe des Zeichnungsblattes

-    {{PropertyData/de|Width}}: Die Breite des Zeichnungsblattes

-    {{PropertyData/de|Fill Ratio}}: Der Prozentsatz der Zeichnung, der von Zuschnitten belegt wird (automatisch)

-    {{PropertyData/de|Tag Text}}(Beschriftungstext): Der anzuzeigende Text

-    {{PropertyData/de|Tag Size}}: Die Höhe des Beschriftungstextes

-    {{PropertyData/de|Tag Position}}: Die Position des Beschriftungstextes. Automatische Mittenposition bei (0,0,0)

-    {{PropertyData/de|Tag Rotation}}: Die Drehung des Beschriftungstextes

-    {{PropertyData/de|Font File}}: Die Schriftart des Beschriftungstextes

-    {{PropertyData/de|Make Face}}: Falls True, ist die Platte eine Part-Fläche, anderenfalls ein Part-Linienzug

-    {{PropertyData/de|Grain Direction}}: Gibt einen Winkel für die Faserausrichtung an (im Uhrzeigersinn, 0° bedeutet oben)



### Ansicht

-    {{PropertyView/de|Margin}}: Ein Rand, der innerhalb der Plattenkontur angezeigt werden kann

-    {{PropertyView/de|Show Margin}}: Schaltet die Anzeige des Randes ein bzw. aus

-    {{PropertyView/de|Show Grain}}: Schaltet die Anzeige der Faserausrichtung ein bzw. aus (Make Face muss auf \'true\' gesetzt sein)



## Skripten


**Siehe auch:**

[Arch API](Arch_API/de.md) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Das Werkzeug Plattenzeichnung kann in [Makros](Macros/de.md) und von der [Python](Python/de.md)-Konsole aus mit folgender Funktion verwendet werden:


```python
Sheet = makePanelSheet(panels=[], name="PanelSheet")
```

-   Erstellt ein `Sheet`-Objekt aus `panels`, welches eine Liste von [Arch Platten](Arch_Panel.md)-Objekten ist.

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



---
⏵ [documentation index](../README.md) > Arch Panel Sheet/de
