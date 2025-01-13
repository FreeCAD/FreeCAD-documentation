---
 GuiCommand:
   Name: Arch Space
   Name/de: Arch Raum
   MenuLocation: 3D/BIM , Raum
   Workbenches: BIM_Workbench/de
   Shortcut: **S** **P**
   Version: 0.14
   SeeAlso: 
---

# Arch Space/de



## Beschreibung

Das Werkzeug **Arch Raum** ermöglicht ein leeres Volumen festzugelegen, entweder auf einer Festkörperform basierend oder indem seine Grenzen festgelegt werden oder eine Mischung aus beidem. Wenn es ausschließlich auf Begrenzungen basiert, wird das Volumen berechnet, indem von der Begrenzungsbox aller gegebenen Begrenzungen ausgegangen und die Räume hinter jeder Begrenzung subtrahiert werden. Ein Raum (Space-Objekt) definiert immer ein Festkörper-Volumen. Die Bodenfläche eines Raumobjekts, die berechnet wird, indem es in seinem Massenschwerpunkt mit einer horizontale Ebene geschnitten wird, kann ebenfalls angezeigt werden.

<img alt="" src=images/Arch_Space_example.jpg  style="width:640px;">



*Raumobjekt, das aus einem vorhandenen Volumenobjekt erstellt wird, dann werden zwei Wandflächen als Begrenzungen hinzugefügt.*



## Anwendung

1.  Ein vorhandenes Festkörperobjekt oder Flächen auf Begrenzungsobjekten auswählen.
2.  Den Befehl mit einer der folgenden Methoden aufrufen:
    -   Die Schaltfläche **<img src="images/Arch_Space.svg" width=16px> [Raum](Arch_Space/de.md)** drücken.
    -   Das Tastaturkürzel **S** dann **P**.
    -   Den Menüeintrag **3D/BIM → Raum** auswählen.



### Begrenzungen

-   Die Grenzeigenschaften können momentan nicht über die GUI bearbeitet werden.
-   Siehe die [Forumsankündigung](http://forum.freecadweb.org/viewtopic.php?f=9&t=4275).



## Eigenschaften

-    {{PropertyData/de|Basis}}: Das Basisobjekt, falls vorhanden (muss ein Festkörper sein)

-    {{PropertyData/de|Boundaries}}: Eine Liste möglicher Begrenzungselemente

-    {{PropertyData/de|Area}}: Die berechnete Bodenfläche dieses Raumes

-    {{PropertyData/de|FinishFloor}}: Die Endbearbeitung des Fußbodens in diesem Raum

-    {{PropertyData/de|FinishWalls}}: Die Endbearbeitung der Wände dieses Raumes

-    {{PropertyData/de|FinishCeiling}}: Die Endbearbeitung der Decke dieses Raumes

-    {{PropertyData/de|Group}}: Objekte, die sich in diesem Raum befinden, wie zum Beispiel Möbel

-    {{PropertyData/de|SpaceType}}: Der Typ dieses Raumes

-    {{PropertyData/de|FloorThickness}}: Die Dicke des Fußbodenbelags

-    {{PropertyData/de|NumberOfPeople}}: Die Anzahl der Personen, die sich üblicherweise in diesem Raum aufhalten

-    {{PropertyData/de|LightingPower}}: Die zur Beleuchtung dieses Raumes benötigte elektrische Leistung in Watt

-    {{PropertyData/de|EquipmentPower}}: Die für die Ausrüstung dieses Raumes benötigte elektrische Leistung in Watt

-    {{PropertyData/de|AutoPower}}: Wenn dies zutrifft, wird die Geräteleistung automatisch von den in diesem Feld aufgeführten Geräten übernommen.

-    {{PropertyData/de|Conditioning}}: Die Art der Klimatisierung dieses Raumes

-    {{PropertyData/de|Internal}}: Gibt an, ob dieser Raum intern oder extern ist

-    {{PropertyView/de|Text}}: Der anzuzeigende Text. Verwende \$area, \$label, \$tag, \$floor, \$walls, \$ceiling, um die entsprechenden Daten einzufügen

-    {{PropertyView/de|Font Name}}: Der Name der Schriftart

-    {{PropertyView/de|Text Color}}: Die Farbe des Textes

-    {{PropertyView/de|Font Size}}: Die Schrifthöhe des Textes

-    {{PropertyView/de|First Line}}: Die Höhe der ersten Zeile (als Vielfaches der Schrifthöhe. 1 = gleiche Höhe, 2 = doppelte Höhe, usw.)

-    {{PropertyView/de|Line Spacing}}: Der Abstand zwischen den Textzeilen

-    {{PropertyView/de|Text Position}}: Die Position des Textes. Wird die Vorgabe (0,0,0) nicht geändert, wird der Text automatisch positioniert

-    {{PropertyView/de|Text Align}}: Die Ausrichtung des Textes

-    {{PropertyView/de|Decimals}}: Die Anzahl der zu verwendenden Dezimalstellen für berechnete Texte

-    {{PropertyView/de|Show Unit}}: Nachgestellte Maßeinheiten anzeigen oder nicht



## Optionen

-   Um Zonen zu erstellen, die mehrere Räume gruppieren, wird ein [Arch Gebäudeteil](Arch_BuildingPart/de.md) verwendet und sein IFC-Typ auf \"Spatial Zone\" (Räumliche Zone) gesetzt.
-   Das Raumobjekt (Space-Objekt) hat dieselben Anzeigemodi wie andere Arch- und Part-Objekte, mit einem weiteren, **Fußabdruck** (Footprint) genannten, der nur die Unterseite des Raumes anzeigt.



## Skripten


**Siehe auch:**

[Arch API](Arch_API/de.md) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Das Werkzeug Raum kann in [Makros](Macros/de.md) und von der [Python](Python/de.md)-Konsole aus mit der folgenden Funktion verwendet werden:


```python
Space = makeSpace(objects=None, baseobj=None, name="Space")
```

-   Erstellt ein `Space`-Objekt aus den gegebenen `objects` oder `baseobj`, die
    -   ein Dokumentobjekt sein können, wodurch es zur Basisform des Raumobjekts wird oder
    -   eine Liste von Auswahlobjekten wie von `FreeCADGui.Selection.getSelectionEx()` oder
    -   eine Liste von Tupeln `(object, subobjectname)`

Beispiel:


```python
import FreeCAD, Arch

Box = FreeCAD.ActiveDocument.addObject("Part::Box", "Box")
Box.Length = 1000
Box.Width = 1000
Box.Height = 1000

Space = Arch.makeSpace(Box)
Space.ViewObject.LineWidth = 2
FreeCAD.ActiveDocument.recompute()
```

Nach der Erstellung eines Raum-Objekts können ausgewählte Flächen durch den folgenden Code hinzugefügt werden:


```python
import FreeCAD, FreeCADGui, Draft, Arch

points = [FreeCAD.Vector(-500, 0, 0), FreeCAD.Vector(1000, 1000, 0)]
Line = Draft.makeWire(points)
Wall = Arch.makeWall(Line, width=150, height=2000)
FreeCAD.ActiveDocument.recompute()

# Select a face of the wall
selection = FreeCADGui.Selection.getSelectionEx()
Arch.addSpaceBoundaries(Space, selection)
```

Begrenzungen können auch entfernt werden, wieder durch auswählen der angegebenen Flächen:


```python
selection = FreeCADGui.Selection.getSelectionEx()
Arch.removeSpaceBoundaries(Space, selection)
```





{{BIM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > Arch Space/de
