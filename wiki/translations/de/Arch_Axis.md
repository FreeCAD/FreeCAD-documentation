---
- GuiCommand:/de
   Name:Arch Axis
   Name/de:Arch Achse
   MenuLocation:Architektur → Achse
   Workbenches:[Arch](Arch_Workbench/de.md)
   Shortcut:**A** **X**
   SeeAlso:[Achsensystem](Arch_AxisSystem/de.md), [Arch Gitter](Arch_Grid/de.md)
---

## Beschreibung

Das **<img src="images/Arch_Axis.svg" width=16px> [Architektur Achsen](Arch_Axis/de.md)** Werkzeug ermöglicht es dir, eine Reihe von Achsen im aktuellen Dokument zu platzieren. Der Abstand und der Winkel zwischen den Achsen ist anpassbar, ebenso wie der Nummerierungsstil. Die Achsen dienen hauptsächlich als Referenzen, auf die Objekte gefangen werden, können aber auch zusammen mit **<img src="images/Arch_Axis_System.svg" width=16px> [ Architektur AchsenSysteme](Arch_AxisSystem.md)** verwendet werden und kann auch von anderen Architekturobjekten referenziert werden, um parametrische Anordnungen, z.B. von Trägern oder Stützen, zu erstellen. **<img src="images/Arch_Grid.svg" width=16px> [Architektur Gitter](Arch_Grid/de.md)** können auch an Stellen von Achsen verwendet werden.

<img alt="" src=images/Arch_Axis_example.jpg  style="width:600px;"> 
*Zwei Achsenobjekte, die rechtwinklig zueinander ausgerichtet sind, um ein Raster zu erzeugen*

## Anwendung

1.  Drücke die **<img src="images/Arch_Axis.svg" width=16px>[Architektur Achsen](Arch_Axis/de.md)** Taste oder drücke **A** dann **X** Tasten.
2.  [Bewegen](Draft_Move/de.md)/[Drehen](Draft_Rotate/de.md) das Achsensystem in die gewünschte Position.
3.  Rufe den Bearbeitungsmodus durch doppelklicken des Achsensystems in der Baumansicht auf, um dessen Einstellungen wie Anzahl der Achsen, Abstände und Winkel zwischen den Achsen anzupassen.

## Optionen

-   Jede Achse in der Abfolge hat ihren eigenen Abstand und Winkel in Bezug auf die vorherige Achse. Dies ermöglicht sehr komplexe Systeme wie nicht-orthogonale Systeme, polare Systeme oder jede Art von nicht-uniformem System.
-   Durch Doppelklicken auf die Achse in der Baumansicht erlaubt das bearbeiten der Abstände, Winkel und Beschriftungen jeder Achse
-   Achslänge, Größe der Blasen und Nummerierungsstile sind direkt über die Eigenschaften des Achsensystems anpassbar.
-   Jede Achse kann auch eine Beschriftung anzeigen, die auch über den Dialog des Aufgabenpaneel bearbeitet werden kann.

## Eigenschaften

-    {{PropertyData/de|Länge}}: die Länge der Achsen

-    **Limit**: Falls größer als Null, wird jede Achse als zwei Linien in der gegebenen Länge dargestellt anstatt als eine durchgehende Linie <small>(v0.20)</small> 

-    {{PropertyView/de|Blasengröße}}: die Größe der Achsenblasen

-    {{PropertyView/de|Nummerierungsstil}}: Wie die Achsen nummeriert sind: 1,2,3, A,B,C, usw..

-    {{PropertyView/de|Blasenposition}}: Wo die Blase auf der Achse platziert ist: Am Startpunkt, Endpunkt, beide oder keiner.

-    {{PropertyView/de|Schriftname}}: Einen Schrifttyp, um die Blasennummer und/oder eine Beschriftung anzubringen

-    {{PropertyView/de|Schriftgröße}}: nur die Größe des Beschriftungstextes (der Blasentext wird durch die Blasengröße bestimmt)

-    {{PropertyView/de|Beschriftung anzeigen}}: Schaltet die Anzeige der Etikettentexte ein/aus

## Verwendung als Abschnittsmarkierung {#verwendung_als_abschnittsmarkierung}

Durch setzen der **Blasenposition**-Eigenschaft auf **Pfeil links/rechts** oder **Strich links/rechts** wird die Achse einen gefüllten Pfeil oder einen Strich anstatt der Blase anzeigen, so dass sie als eine Abschnittsmarkierung genutzt werden kann <small>(v0.20)</small> 

## Skripten


**Siehe auch:**

[Arch API](Arch_API/de.md) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Das Achsenwerkzeug kann in [Makros](macros/de.md) und aus der [Python](Python/de.md) Konsole heraus durch folgende Funktion angesprochen werden: 
```python
Axes = makeAxis(num=5, size=1000, name="Axes")
```

-   Erzeugt ein `Axes` Objekt basierend auf der gegebenen Anzahl `num` der Achsen und dem Abstand `size` zwischen benachbarten Achsen.

Beispiel:


```python
import Draft, Arch

Axes = Arch.makeAxis(5, 1000)

Axes.ViewObject.LineWidth = 3
Axes.ViewObject.BubbleSize = 200
Axes.ViewObject.FontSize = 150

Axes2 = Arch.makeAxis(6, 500)

Axes2.ViewObject.LineWidth = 2
Axes2.ViewObject.BubbleSize = 200
Axes2.ViewObject.FontSize = 150
Axes2.ViewObject.NumberingStyle = "A,B,C"
FreeCAD.ActiveDocument.recompute()

Axes2.Length = 6000
Draft.rotate(Axes2, -90)
Draft.move(Axes2, FreeCAD.Vector(-1000, 2500, 0))
FreeCAD.ActiveDocument.recompute()
```





 
