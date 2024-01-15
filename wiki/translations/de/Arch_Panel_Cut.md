---
 GuiCommand:
   Name: Arch Panel Cut
   Name/de: Arch Plattenzuschnitt
   MenuLocation: Arch , Plattenwerkzeuge , Plattenzuschnitt
   Workbenches: Arch_Workbench,Path_Workbench/de
   Shortcut: **P** **C**
   Version: 0.17
   SeeAlso: Arch_Panel/de, Arch_Panel_Sheet/de, Arch_Nest/de
---

# Arch Panel Cut/de



## Beschreibung

Dieses Werkzeug erstellt im 3D-Dokument eine ebene 2D-Ansicht einer [Arch Platte](Arch_Panel/de.md), die in eine [Arch Plattenzeichnung](Arch_Panel_Sheet/de.md) eingefügt oder direkt nach [DXF](Draft_DXF/de.md) exportiert wird. Die Plattenzuschnitt-Objekte werden auch durch den Arbeitsbereich [Path](Path_Workbench/de.md) unterstützt.

<img alt="" src=images/Arch_Wikihouse_02.jpg  style="width:1024px;">



## Anwendung

1.  Ein oder mehrere [Arch Platten](Arch_Panel/de.md)-Objekte auswählen.
2.  Die Schaltfläche **<img src="images/Arch_Panel_Cut.svg" width=16px> [Arch Plattenzuschnitt](Arch_Panel_Cut/de.md)** drücken, oder das Tastaturkürzel **P** dann **C**.
3.  Die gewünschten Eigenschaften anpassen.



## Optionen

-   Falls die Platte nicht eben ist (z.B. gewellt), wird die Wölbung nicht im Plattenzuschnitt erscheinen. Dieses Werkzeug ist hauptsächlich für ebene Platten geeignet.
-   Der Plattenzuschnitt kann eine Beschriftung anzeigen. Diese Beschriftung kann eine benutzerdefinierte Textzeile sein oder automatisch die Beschriftung, Benennung oder Beschreibung seiner verknüpften Platte anzeigen.
-   Für eine CNC-Verarbeitung sollte die Beschriftung in einer einfachen Linien-Schriftart sein, in der die Zeichen einfache Polylinien sind, denen eine Maschine einfach folgen kann. Bei der Erstellung wird das Plattenzuschnitt-Objekt automatisch die Schriftart nutzen, die in Bearbeiten → Einstellungen → Draft → Texte und Bemaßungen → Standardschriftart für Textformen angegeben ist
-   Doppelklicken des Plattenzuschnitts in der Baumansicht nach der Erstellung aktiviert den Änderungsmodus und ermöglicht die Änderung der Position der Beschriftung
-   Sollen verschiedene Plattenzuschnitte angeordnet werden, kann Plattenzuschnitt einen Rand anzeigen, der hilft zu prüfen, ob genug Platz zwischen den einzelnen Zuschnitten ist



## Eigenschaften



### Daten

-    **Source**: Das von diesem Zuschnitt gezeigte [Arch Platten](Arch_Panel/de.md)-Objekt.

-    **Tag Text**: Der anzuzeigende Text. Kann %tag%, %label% oder %description% sein, um die entsprechenden Informationen der Platte anzuzeigen.

-    **Tag Size**: Die Größe des Beschriftungstextes.

-    **Tag Position**: Die Position des Beschriftungstextes, (0,0,0) für automatische Mittenposition.

-    **Tag Rotation**: Die Drehung des Textes.

-    **Font File**: Die Schriftart der Beschriftung.

-    **Make Face**: Falls {{Incode|True}} ist die Platte eine Part-Fläche, anderenfalls ein Part-Linienzug.



### Ansicht

-    **Margin**: Ein Rand, der um die Form des Plattenzuschnitts herum angezeigt wird.

-    **Show Margin**: Schaltet die Anzeige des Randes ein bzw. aus



## Skripten


**Siehe auch:**

[Arch API](Arch_API/de.md) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Das Werkzeug Plattenzuschnitt kann in [Makros](Macros/de.md) und von der [Python](Python/de.md)-Konsole aus mit folgender Funktion verwendet werden: 
```python
View = makePanelCut(panel, name="PanelView")```

-   Erstellt ein `View`-Objekt (2D-Projektion) aus dem existierenden (Plattenobjekt) `panel`.

Beispiel: 
```python
import FreeCAD, Draft, Arch

p1 = FreeCAD.Vector(0, 0, 0)
p2 = FreeCAD.Vector(500, 0, 0)
p3 = FreeCAD.Vector(500, 50, 0)
p4 = FreeCAD.Vector(550, 50, 0)
p5 = FreeCAD.Vector(600, 0, 0)
p6 = FreeCAD.Vector(1000, 0, 0)
p7 = FreeCAD.Vector(1000, 400, 0)
p8 = FreeCAD.Vector(600, 400, 0)
p9 = FreeCAD.Vector(600, 350, 0)
p10 = FreeCAD.Vector(550, 350, 0)
p11 = FreeCAD.Vector(500, 400, 0)
p12 = FreeCAD.Vector(0, 400, 0)

Wire = Draft.makeWire([p1, p2, p3, p4, p5, p6,
                       p7, p8, p8, p9, p10, p11, p12], closed=True)
Panel = Arch.makePanel(Wire, thickness=36)
FreeCAD.ActiveDocument.recompute()

View = Arch.makePanelCut(Panel)
View.ViewObject.LineWidth = 3
FreeCAD.ActiveDocument.recompute()
```



## Tutorien

-   [Wikihouse Portierungs Tutorium](Wikihouse_porting_tutorial/de.md)



---
⏵ [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch Panel Cut/de
