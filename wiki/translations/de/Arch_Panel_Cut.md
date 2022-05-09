---
- GuiCommand   */de
   Name   *Arch Panel Cut
   Name/de   *Arch Tafelschnitt
   MenuLocation   *Arch → Panel-Werkzeuge → Tafelschnitt
   Workbenches   *[Arch](Arch_Workbench.md),[Pfad](Path_Workbench/de.md)
   Shortcut   ***P** **C**
   Version   *0.17
   SeeAlso   *[Arch Platte](Arch_Panel/de.md), [Arch Tafelplatte](Arch_Panel_Sheet/de.md), [Arch Verschachteln](Arch_Nest/de.md)
---

# Arch Panel Cut/de

## Beschreibung

Dieses Werkzeug erstellt im 3D-Dokuemnt eine flache 2D-Ansicht einer [Arch Platte](Arch_Panel/de.md), die in eine [Arch Tafel Platte](Arch_Panel_Sheet/de.md) eingefügt oder direkt nach [DXF](Draft_DXF/de.md) exportiert wird. Die Tafelschnitt-Objekte werden auch durch den [Path-Arbeitsbereich](Path_Workbench/de.md) unterstützt.

<img alt="" src=images/Arch_Wikihouse_02.jpg  style="width   *1024px;">

## Anwendung

1.  Wähle ein oder mehrere [Arch Tafel](Arch_Panel/de.md) Objekte aus.
2.  Drücke die **<img src="images/Arch_Panel_Cut.svg" width=16px> [Arch Tafelschnitt](Arch_Panel_Cut/de.md)** Schaltfläche, oder drücke die **P** dann **C** Tasten.
3.  Passe die gewünschten Eigenschaften an.

## Optionen

-   Falls die Platte nicht flach ist (z.B. gewellt), wird die Wölbung nicht im Tafelschnitt erscheinen. Dieses Werkzeug ist hauptsächlich für flache Platten geeignet.
-   Der Tafelschnitt kann eine Markierung anzeigen. Diese Markierung kann ein benutzerdefinierte Textzeile sein oder automatisch Tag, Label oder Description der verbundenen Platte anzeigen.
-   Um nützlich bei CNC-Verarbeitung zu sein, sollte die Markierung in einer einfachen (?,\"sticky\") Schriftart sein, in der Zeichen einfache Polylinien sind, denen die Maschine einfach folgen kann. Bei der Erstellung wird das Tafelschnitt-Objekt automatisch die Schriftart nutzen, die in Bearbeiten → Einstellungen → Draft → Texte und Bemaßungen → Standardschriftart für Textformen angegeben ist
-   Doppelklicken des Tafelschnitts in der Baumansicht nach der Erstellung aktiviert den Änderungsmodus und ermöglicht die Änderung der Position der Markierung
-   Wenn du verschiedene Tafelschnitte anordnen musst, kann Tafelschnitt einen Rand anzeigen, der hilfreich ist, um zu prüfen, ob genug Platz zwischen den einzelnen Schnitten ist

## Eigenschaften

### Data


<div class="mw-translate-fuzzy">

### Daten

-    **Source**   * Das von diesem Schnitt gezeigte [Arch Platte](Arch_Panel/de.md)-Objekt

-    **Tag Text**   * Der anzuzeigende Text. Kann %tag%, %label% oder %description% sein, um die entsprechenden Informationen der Platte anzuzeigen

-    **Tag Size**   * Die Größe des Markierungstextes

-    **Tag Position**   * Die Position des Markierungstextes, (0,0,0) für automatische Mittenposition

-    **Tag Rotation**   * Die Drehung des Textes

-    **Font File**   * Die Schriftart der Markierung

-    **Make Face**   * Falls {{Incode|True}} ist die Platte eine Fläche, anderenfalls ein Linienzug


</div>

### View


<div class="mw-translate-fuzzy">

### Ansicht

-    **Margin**   * Ein Rand kann außerhalb der Tafelschnittform betrachtet werden

-    **Show Margin**   * Schaltet die Anzeige des Rands ein/aus


</div>

## Scripting


<div class="mw-translate-fuzzy">

## Skripten


**Siehe auch   ***

[Arch API](Arch_API/de.md) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).


</div>

Das Tafelschnittwerkzeug kann in [Makros](macros/de.md) und aus der [Python](Python/de.md) Konsole aus mit folgender Funktion verwendet werden   * 
```python
View = makePanelCut(panel, name="PanelView")```

-   Erstellt ein `View`-Objekt (2D-Projektion) aus dem existierenden `panel`.

Beispiel   * 
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
![](images/Right_arrow.png) [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch Panel Cut/de
