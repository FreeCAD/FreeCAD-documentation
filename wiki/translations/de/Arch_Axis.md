---
 GuiCommand:
   Name: Arch Axis
   Name/de: Arch Achse
   MenuLocation: Anmerkung , Achse
   Workbenches: BIM_Workbench/de
   Shortcut: **A** **X**
   SeeAlso: Arch_AxisSystem/de, Arch_Grid/de
---

# Arch Axis/de



## Beschreibung

Das **<img src="images/Arch_Axis.svg" width=16px> [Arch Achse](Arch_Axis/de.md)** Werkzeug ermöglicht es dir, eine Reihe von Achsen im aktuellen Dokument zu platzieren. Der Abstand und der Winkel zwischen den Achsen ist anpassbar, ebenso wie der Nummerierungsstil. Die Achsen dienen hauptsächlich als Referenzen, auf die Objekte gefangen werden, können aber auch zusammen mit **<img src="images/Arch_Axis_System.svg" width=16px> [Arch Achsensystem](Arch_AxisSystem.md)** verwendet werden. Sie können auch von anderen Architekturobjekten referenziert werden, um parametrische Anordnungen, z.B. von Trägern oder Stützen, zu erstellen. **<img src="images/Arch_Grid.svg" width=16px> [Arch Gitter](Arch_Grid/de.md)** können auch an Stellen von Achsen verwendet werden.

<img alt="" src=images/Arch_Axis_example.jpg  style="width:600px;"> 
*Zwei Achsenobjekte, die rechtwinklig zueinander ausgerichtet sind, um ein Raster zu erzeugen*



## Anwendung

1.  Die Schaltfläche **<img src="images/Arch_Axis.svg" width=16px>[Achse](Arch_Axis/de.md)** drücken oder das Tastaturkürzel **A** dann **X**.
2.  Das Achsensystem in die gewünschte Position [Verschieben](Draft_Move/de.md)/[Drehen](Draft_Rotate/de.md) .
3.  Den Bearbeitungsmodus durch Doppelklicken des Achsensystems in der Baumansicht aufrufen, um dessen Einstellungen wie Anzahl der Achsen, Abstände und Winkel zwischen den Achsen anzupassen.



## Optionen

-   Jede Achse in der Abfolge hat ihren eigenen Abstand und Winkel in Bezug auf die vorherige Achse. Dies ermöglicht sehr komplexe Systeme wie nicht-orthogonale Systeme, polare Systeme oder jede Art von nicht-uniformem System.
-   Durch Doppelklicken auf die Achse in der Baumansicht erlaubt das bearbeiten der Abstände, Winkel und Beschriftungen jeder Achse.
-   Achslänge, Größe der Blasen und Nummerierungsstile sind direkt über die Eigenschaften des Achsensystems anpassbar.
-   Jede Achse kann auch eine Beschriftung anzeigen, die über den Dialog des Aufgabenbereichs bearbeitet werden kann.



## Eigenschaften

-    {{PropertyData/de|Länge}}: die Länge der Achsen

-    **Limit**: Falls größer als Null, wird jede Achse als zwei Linien in der gegebenen Länge dargestellt anstatt als eine durchgehende Linie <small>(v0.20)</small> 

-    {{PropertyView/de|Blasengröße}}: die Größe der Achsenblasen

-    {{PropertyView/de|Nummerierungsstil}}: Wie die Achsen nummeriert sind: 1,2,3, A,B,C, usw..

-    {{PropertyView/de|Blasenposition}}: Wo die Blase auf der Achse platziert ist: Am Startpunkt, Endpunkt, beide oder keiner.

-    {{PropertyView/de|Schriftname}}: Einen Schrifttyp, um die Blasennummer und/oder eine Beschriftung anzubringen

-    {{PropertyView/de|Schriftgröße}}: nur die Größe des Beschriftungstextes (der Blasentext wird durch die Blasengröße bestimmt)

-    {{PropertyView/de|Beschriftung anzeigen}}: Schaltet die Anzeige der Etikettentexte ein/aus



## Verwendung als Abschnittsmarkierung 

Durch setzen der Eigenschaft **Bubble Position** auf **Arrow left/right** oder **Bar left/right** wird die Achse einen gefüllten Pfeil oder einen Strich anstatt der Blase anzeigen, so dass sie als Schnittmarkierung genutzt werden kann {{Version/de|0.20}}



## Skripten


**Siehe auch:**

[Arch API](Arch_API/de.md) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Das Werkzeug Achse kann in [Makros](Macros/de.md) und von der [Python](Python/de.md)-Konsole aus mit der folgenden Funktion verwendet werden:


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



---
⏵ [documentation index](../README.md) > Arch Axis/de
