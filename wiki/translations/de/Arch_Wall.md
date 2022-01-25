---
- GuiCommand:/de
   Name:Arch Wall   Name/de:Arch Wand
   MenuLocation:Architektur → Wand
   Workbenches:[Architektur](Arch_Workbench/de.md)
   Shortcut:**W** **A**
   SeeAlso:[Architektur Struktur](Arch_Structure/de.md)
---

# Arch Wall/de

## Beschreibung

Dieses Werkzeug erzeugt neue Wände oder baut Wände basierend auf einem anderen [Form](Part_Workbench/de.md)-basierten oder [Polygonnetz](Mesh_Workbench/de.md)-basierten Objekt. Eine Wand kann ohne ein Basisobjekt erstellt werden, wobei es sich dann wie ein räumliches Objekt verhält, mit Länge-, Breite- und Höhe-Eigenschaften. Wird auf einem existierenden Objekt aufgebaut, kann eine Wand aufgesetzt werden auf:

-   Ein **lineares 2D Objekt**, wie z. B. Linien, Drähte, Bögen oder Skizzen. In diesem Fall kannst du Dicke, Ausrichtung (rechts, links oder zentriert) und Höhe ändern. Die Eigenschaft Länge hat keine Auswirkung.
-   Eine **flache Fläche**, in diesem Fall kannst du nur die Höhe ändern. Die Eigenschaften Länge und Breite haben keine Auswirkung. Wenn die Grundfläche jedoch senkrecht ist, verwendet die Wand die Eigenschaft Breite anstelle der Höhe, so dass du Wände aus raumartigen Objekten oder Massenstudien erstellen kannst.
-   Ein **Festkörper**, in diesem Fall haben die Eigenschaften Länge, Breite und Höhe keine Auswirkung. Die Wand verwendet einfach das darunter liegende Solid als Form.
-   Ein **Polygonnetz**, in diesem Fall muss das zugrunde liegende Netz ein geschlossener, vielfältiger Körper sein.

<img alt="" src=images/Arch_Wall_example.jpg  style="width:780px;"> 
*Wände, welche jeweils auf einer Linie, einem Drahtgitter, einer Fläche, einem Körper, sowie einer Skizze aufgebaut werden*

Wände können auch Ergänzungen oder Aussparungen erhalten. Ergänzungen sind andere Objekte, deren Form mit der Wandform verschmolzen werden. Bei Aussparungen werden die Formen des anderen Objektes aus der Wand entfernt. Ergänzungen und Aussparungen können mit dem **<img src="images/Arch_Add.png" width=16px> [Hinzufügen](Arch_Add/de.md)** bzw. **<img src="images/Arch_Remove.png" width=16px> [Entfernen](Arch_Remove/de.md)** Werkzeug erzeugt werden. Ergänzungen und Aussparungen haben keinen Einfluss auf Parameter wie Höhe oder Breite, die nach wie vor änderbar sind.

Wenn sich mehrere Wände überschneiden sollen, musst du diese in eine [Etage](Arch_Floor/de.md) platziert werden, damit sich ihre Geometrien überschneiden.

## Anwendung

### Zeichnen einer neuen Wand 

1.  Drücke die **<img src="images/Arch_Wall.svg" width=16px> [Arch Wand](Arch_Wall/de.md)**Schltfläche oder drücke die **W**- und **A**-Tasten
2.  Klicke einen ersten Punkt in der 3D-Ansicht oder gib eine Koordinate ein.
3.  Klicke einen zweiten Punkt in der 3D-Ansicht oder gib eine weitere Koordinate ein.

### Zeichnen einer Wand auf einem ausgewählten Objekt 

1.  Wähle ein oder mehrere Basisgeometrieobjekte (Entwurfsobjekt, Skizze, usw.)
2.  Drücke die **<img src="images/Arch_Wall.svg" width=16px> [Architektur Wand](Arch_Wall/de.md)** Schaltfläche, oder drücke die **W** und dann **A** Tasten
3.  Passe die benötigten Eigenschaften wie Höhe oder Breite an.

## Optionen

-   Wände haben die gemeinsamen Eigenschaften und Verhaltensweisen aller [Architektur Komponenten](Arch_Component/de.md).
-   Die Höhe, Dicke und Ausrichtung einer Wand können während des Zeichnens über das Aufgabenpaneel festgelegt werden.
-   Wenn eine Wand an eine bestehende Wand gefangen wird, werden beide Wände zu einer Wand verbunden. Die Art und Weise, wie die beiden Wände miteinander verbunden werden, hängt von ihren Eigenschaften ab: Wenn sie die gleiche Breite, Höhe und Ausrichtung haben und wenn die Option \"Basisskizzen verbinden\" in den Architektur Voreinstellungen aktiviert ist, wird die resultierende Wand ein einziges Objekt sein, das auf einer Skizze basiert, die aus mehreren Segmenten besteht. Andernfalls wird die letztere Wand der ersten als Zusatz hinzugefügt.
-   Drücke **X**, **Y** oder **Z** nach dem ersten Punkt, um den zweiten Punkt auf der gegebenen Achse zu beschränken.
-   Um Koordinaten manuell einzugeben, gib einfach die Zahlen und drücke dann **Eingabe** zwischen jeder X, Y und Z Komponente.
-   Drücke **R** oder klicken das Kontrollkästchen, um die **Relativ** Schaltfläche zu aktivieren/deaktivieren. Wenn der Relativ Modus eingeschaltet ist, sind die Koordinaten des zweiten Punktes relativ zum ersten Punkt. Wenn nicht, sind sie absolut, ausgehend vom (0,0,0) Ursprungspunkt.
-   Drücke **Umschalten**, während des Zeichnens [beschränken](Draft_Constrain/de.md) des zweiten Punkts horizontal oder vertikal in Bezug zum ersten.
-   Drücke **Esc** oder die **Abbrechen**Schaltfläche, um den aktuellen Befehl abzubrechen.
-   Doppelklicken auf die Wand in der Baumansicht nach ihrer Erstellung erlaubt dir in den Bearbeitungsmodus wechseln und auf deine Additionen und Subtraktionen zuzugreifen und sie zu ändern.
-   Mehrschichtige Wände können leicht erstellt werden, indem mehrere Wände von derselben Grundlinie aus gebaut werden. Durch setzen ihrer Ausrichtungseigenschaft entweder auf links oder rechts und Angae eines Versatz Wertes, kannst du effektiv mehrere Wandschichten konstruieren. Platzieren eines Fensters in einer solchen Wandschicht, wird die Öffnung auf die anderen Wandschichten auf der gleichen Grundlinie übertragen.
-   Wände können auch [Multimaterialien](Arch_MultiMaterial/de.md) verwenden. Wenn ein Multimaterial verwendet wird, wird die Wand mehrschichtig, wobei die durch das Multimaterial vorgegebenen Dicken verwendet werden. Bei jeder Schicht mit einer Dicke von Null wird die Dicke automatisch durch den verbleibenden Raum definiert, der durch den Wert für die Wandbreite definiert ist, nachdem die anderen Schichten abgezogen wurden.
-   Wände können zur Anzeige von Blöcken anstelle eines einzelnen Festkörpers gemacht werden, indem ihre Eigenschaft **Blöcke machen** eingeschaltet wird. Die Größe und der Versatz von Blöcken kann mit verschiedenen Eigenschaften konfiguriert werden, und die Anzahl der Blöcke wird automatisch berechnet. <small>(v0.18)</small> 

## Fangen

Fangen funktioniert etwas anders mit Architektur Wänden als andere Architektur und Entwurf Objekte. Wenn eine Wand ein Grundlinienobjekt hat, verankert sich das Fangen am Basisobjekt und nicht an der Wandgeometrie, so dass Wände leicht an ihrer Grundlinie ausgerichtet werden können. Wenn du jedoch speziell an der Wandgeometrie fangen möchtest, drücken von **Strg** schaltet das Fangen auf das Wandobjekt um.

<img alt="" src=images/Arch_wall_snap.jpg  style="width:780px;"> 
*Zweite Wand gefangen senkrecht zur ersten*

## Eigenschaften

Wand-Objekte erben die Eigenschaften von [Part](Part_Workbench/de.md)-Objekten und haben außerdem die folgenden zusätzlichen Eigenschaften:

-    {{PropertyData/de|Align}}: Die Ausrichtung der Wand an ihrer Basislinie: Left, Right oder Center (links, rechts oder mittig)

-    {{PropertyData/de|Base}}: Das Basisobjekt, auf dem diese Wand gebaut wurde

-    {{PropertyData/de|Face}}: Der Index der Fläche des zu benutzenden Basisobjekts. Falls der Wert nicht gesetzt wurde oder 0 ist, wird das gesamt Objekt benutzt

-    {{PropertyData/de|Force Wire}}: Falls True, und die Wand auf einer Fläche basiert, wird nur die Grenzlinie (border wire) der Fläche benutzt, so dass die Wand die Fläche begrenzt

-    {{PropertyData/de|Length}}: Die Länge der Wand (wird nicht benutzt, wenn die Wand auf einer Fläche basiert)

-    {{PropertyData/de|Width}}: Die Breite der Wand (wird nicht benutzt, wenn die Wand auf einer Fläche basiert)

-    {{PropertyData/de|Height}}: Die Höhe der Wand (wird nicht benutzt, wenn die Wand auf einer Fläche basiert)

-    {{PropertyData/de|Normal}}: Eine Extrusionsrichtung für die Wand. Wenn auf (0,0,0) gesetzt, ist die Extrusionsrichtung automatisch

-    {{PropertyData/de|Offset}}: Dies legt den Abstand zwischen der Wand und ihrer Basislinie fest. Das funktioniert nur, wenn die Align-Eigenschaft auf Right (rechts) oder Left (links) gesetzt ist.


<small>(v0.18)</small> 

-    {{PropertyData/de|Make Blocks}}: Aktiviere dies, damit die Wand aus Bausteinen (blocks) erzeugt wird

-    {{PropertyData/de|Block Length}}: Die Länge jedes Bausteins

-    {{PropertyData/de|Block Height}}: Die Höhe jedes Bausteins

-    {{PropertyData/de|Offset First}}: Der horizontale Abstand der erste Reihe von Bausteinen

-    {{PropertyData/de|Offset Second}}: Der horizontale Abstand der zweiten Reihe von Bausteinen

-    {{PropertyData/de|Joint}}: Die Größe der Fugen zwischen jedem Baustein

-    {{PropertyData/de|Count Entire}}: Die Anzahl von ganzen Bausteinen (read-only)

-    {{PropertyData/de|Count Broken}}: Die Anzahl von geschnittenen (broken) Bausteinen (read-only)

## Skripten


**Siehe auch:**

[Arch API](Arch_API/de.md) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Das Wand-Werkzeug kann in [Makros](macros/de.md) und aus der [Python](Python/de.md)-Konsole heraus durch folgende Funktion angesprochen werden: 
```python
Wall = makeWall(baseobj=None, length=None, width=None, height=None, align="Center", face=None, name="Wall")
```

-   Erzeugt ein `Wall`-Objekt aus dem gegebenen `baseobj`, welches ein [Draft-Objekt](Draft_Workbench/de.md), eine [Skizze](Sketcher_Workbench/de.md), eine Fläche oder ein Körper sein kann.

-   Falls kein `baseobj` angegeben wurde, können die numerische Werte für Länge, Breite und Höhe vorgegeben werden.
    -   Falls angegeben, kann `face` genutzt werden, um den Index einer Fläche des zugrundeliegenden Objekts anzugeben, auf dem diese Wand erstellt wird, anstatt das komplette Objekt zu verwenden.

-    `align`kann auf `"Center"`, `"Left"` oder `"Right"` gesetzt werden.

-   Liefert `None` zurück, falls die Operation fehlschlägt.

Beispiel:


```python
import FreeCAD, Draft, Arch

p1 = FreeCAD.Vector(0, 0, 0)
p2 = FreeCAD.Vector(2000, 0, 0)
baseline = Draft.makeLine(p1, p2)
Wall1 = Arch.makeWall(baseline, length=None, width=150, height=2000)
FreeCAD.ActiveDocument.recompute()

Wall2 = Arch.makeWall(None, length=2000, width=200, height=1000)
Draft.move(Wall2, FreeCAD.Vector(0, -1000, 0))
FreeCAD.ActiveDocument.recompute()
```



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch Wall/de
