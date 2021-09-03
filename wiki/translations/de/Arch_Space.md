---
- GuiCommand:/de
   Name:Arch Space   Name/de:Arch Raum
   MenuLocation:Arch → Raum
   Workbenches:[Arch](Arch_Workbench/de.md)
   Shortcut:**S** **P**
   Version:0.14
   SeeAlso:[Wand](Arch_Wall/de.md), [Struktur](Arch_Structure/de.md)
---

## Beschreibung

Mit dem Raum Werkzeug kannst du ein leeres Volumen festlegen, entweder indem du es auf einer festen Form basierst, oder indem du seine Grenzen oder eine Mischung aus beidem festlegst. Wenn es ausschließlich auf Begrenzungen basiert, wird das Volumen berechnet, indem von der Begrenzungsbox aller gegebenen Begrenzungen ausgegangen und die Räume hinter jeder Begrenzung subtrahiert werden. Das Raumobjekt definiert immer ein festes Volumen. Die Bodenfläche eines Raumobjekts, die berechnet wird, indem eine horizontale Ebene im Massenschwerpunkt des Raumvolumens geschnitten wird, kann ebenfalls angezeigt werden.

<img alt="" src=images/Arch_Space_example.jpg  style="width:640px;"> 
*Raumobjekt, das aus einem vorhandenen Volumenobjekt erstellt wird, dann werden zwei Wandflächen als Begrenzungen hinzugefügt.*

## Anwendung

1.  Wähle ein vorhandenes Volumenkörperobjekt oder Flächen auf Begrenzungsobjekten aus.
2.  Rufe den Arch Raum Befehl mit mehreren Methoden auf:
    -   Drücken der **<img src="images/Arch_Space.svg" width=16px> [Arch Raum](Arch_Space/de.md)** Schaltfläche in der Werkzeugleiste.
    -   Verwenden der **S**, dann **P** Tastaturkürzel
    -   Verwenden des **Arch → Raum** Eintrags aus dem oberen Menü

### Begrenzungen

-   Die Grenzeigenschaften können momentan nicht über die GUI bearbeitet werden.
-   Siehe die [Forumsankündigung](http://forum.freecadweb.org/viewtopic.php?f=9&t=4275).

## Eigenschaften

-    {{PropertyData/de|Basis}}: Das Basisobjekt, falls vorhanden (muss ein Volumenkörper sein)

-    {{PropertyData/de|Grenzen}}: Eine Liste möglicher Begrenzungselemente

-    **Bereich**: Die berechnete Bodenfläche dieses Raumes

-    **FertigstellenFußboden**: Die Fertigstellung des Fußbodens in diesem Raum

-    **FertigstellungWände **: Die Fertigstellung der Wände dieses Raumes

-    **FertigstellenDecke**: Die Fertigstellung der Decke dieses Raumes

-    **Gruppe**: Objekte, die sich in diesem Raum befinden, wie zum Beispiel Möbel

-    **RaumTyp**: Der Typ dieses Raumes

-    **FußbodenDicke**: Die Dicke des Fußbodenbelags

-    **AnzahlPersonen**: Die Anzahl der Personen, die typischerweise diesen Raum besetzen

-    **BeleuchtungLeistung**: Die zur Beleuchtung dieses Raumes benötigte elektrische Leistung in Watt

-    **AusrüstungLeistung**: Die für die Ausrüstung dieses Raumes benötigte elektrische Leistung in Watt

-    **AutoLeistung**: Wenn dies zutrifft, wird die Geräteleistung automatisch von den in diesem Feld aufgeführten Geräten übernommen.

-    **Klimatisierung**: Die Art der Klimatisierung dieses Raumes

-    **Intern**: Gibt an, ob dieser Raum intern oder extern ist

-    **Text**: Der anzuzeigende Text. Verwende \$area, \$label, \$tag, \$floor, \$walls, \$ceiling, um die entsprechenden Daten einzufügen

-    **SchriftName**: Der Name der Schriftart

-    **TextFarbe**: Die Farbe des Textes

-    **SchriftGröße**: Die Größe des Textes

-    **ErsteLinie**: Die Größe der ersten Linie (multipliziert die Schriftgröße. 1 = gleiche Größe, 2 = doppelte Größe, usw.)

-    **ZeilenAbstand**: Der Abstand zwischen den Textzeilen

-    **TextPosition**: Die Position des Textes. Hinterlasse (0,0,0) für die automatische Position

-    **TextAusrichtung**: Die Ausrichtung des Textes

-    **Dezimalstellen**: Die Anzahl der zu verwendenden Dezimalstellen für berechnete Texte

-    **ZeigeEinheit**: Anzeige des Einheiten Zusatz

anzeigen oder nicht

## Optionen

-   Um Zonen zu erstellen, die mehrere Räume gruppieren, verwende ein [Arch GebäudeTeil](Arch_BuildingPart/de.md) und setze dessen IFC Typ auf \"Räumliche Zone\".
-   Das Raumobjekt hat dieselben Anzeigemodi wie andere Arch- und Teilobjekte, mit einem weiteren, **Fußabdruck** benannten, der nur die Unterseite des Raumes anzeigt. <small>(v0.19)</small> 

## Skripten


**Siehe auch:**

[Arch API](Arch_API/de.md) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Das Raum Werkzeug kann in [Makros](macros/de.md) und aus der [Python](Python/de.md) Konsole mit der folgenden Funktion verwendet werden: 
```python
Space = makeSpace(objects=None, baseobj=None, name="Space")
```

-   Erstellt ein `Space` Objekt aus den gegebenen `objects` oder `baseobj`, die
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


{{docnav/de
|[Dach](Arch_Roof/de.md)
|[Treppe](Arch_Stairs/de.md)
|[Arch-Arbeitsbereich](Arch_Workbench/de.md)
|IconL=Arch_Roof.svg
|IconR=Arch_Stairs.svg
|IconC=Workbench_Arch.svg
}}


 
