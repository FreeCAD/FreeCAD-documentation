---
- GuiCommand:/de
   Name:Arch CurtainWall
   Name/de:Arch Vorhangfassade
   MenuLocation:Arch → Vorhandene Fassade
   Workbenches:[Arch](Arch_Workbench/de.md)
   Shortcut:**C** **W**
   Version:0.19
   SeeAlso:[Arch Wand](Arch_Wall/de.md), [Arch Gitter](Arch_Grid/de.md)
---

# Arch CurtainWall/de



## Beschreibung

Dieses Werkzeug erstellt eine [Vorhangfassade](https://de.wikipedia.org/wiki/Vorhangfassade), indem es eine Grundfläche in viereckige Flächen unterteilt, dann vertikale Pfosten an den vertikalen Kanten und horizontale Pfosten an den horizontalen Kanten erzeugt und die Zwischenräume zwischen den Pfosten mit Paneelen füllt.

<img alt="" src=images/Arch_CurtainWall_example.png  style="width:780px;">

Vorhangwände können aus jeder Art von bestehendem Objekt erstellt werden, wobei alle Flächen des Objekts unterteilt werden. Es funktioniert daher am besten, wenn es mit einem Objekt verwendet wird, das nur eine Fläche hat. Typischerweise würdest du zuerst eine Fläche erstellen, vorzugsweise mit genau 4 Kanten, die den Bereich repräsentiert, den du mit einer Vorhangwand füllen möchtest, und dann das Werkzeug anwenden.

Vorhangwände können auch aus einem linearen Objekt, wie z. B. einer Linie, einem Bogen oder einer Polylinie, aufgebaut werden, wie das normale Werkzeug [Wand](Arch_Wall/de.md).

Flächen, die eine doppelte Krümmung haben, oder Flächen mit mehr als 4 Kanten funktionieren auch, aber das Ergebnis ist weniger vorhersehbar.

Die Flächen werden in viereckige Facetten aufgeteilt. Wenn die 4 Punkte der Facette koplanar sind, wird eine quadratische Facette erzeugt. Wenn nicht, wird sie in zwei Dreiecke geteilt und ein diagonaler Pfosten wird hinzugefügt.

Falls Sie eine unregelmäßige Unterteilung benötigen, ist es auch möglich, ein eigenes unterteiltes Objekt zu bauen, z. B. mit [Arch Gitter](Arch_Grid/de.md), und die vertikale und horizontale Unterteilung der Vorhangfassade auf 1 zu setzen.

Du kannst das Vorhangwand Werkzeug auch ohne ein ausgewähltes Objekt verwenden. In diesem Fall kannst du eine Grundlinie zeichnen, die dann vertikal extrudiert wird, um die Fläche zu bilden, auf der die Vorhangwand aufgebaut wird.



## Anwendung



### Zeichnung einer Vorhangwand von Grund auf 

1.  Stelle sicher, dass nichts ausgewählt ist
2.  Drücke die Schaltfläche **<img src="images/Arch_CurtainWall.svg" width=16px> [Arch Vorhangfassade](Arch_CurtainWall/de.md)
** oder drücke die Tasten **C** und dann **W**
3.  Klicke auf einen ersten Punkt in der 3D-Ansicht oder gib eine Koordinate ein
4.  Klicke auf einen zweiten Punkt in der 3D-Ansicht oder gib eine Koordinate ein
5.  Stelle die benötigten Eigenschaften ein



### Erstellung einer Vorhangwand aus einem gewählten Objekt 

1.  Wähle ein oder mehrere Basisgeometrieobjekte (Entwurfsobjekt, Skizze, usw.).
2.  Drücke die **<img src="images/Arch_CurtainWall.svg" width=16px> [Arch Vorhangfassade](Arch_CurtainWall/de.md)**, oder drücke die Tasten **C** und dann **W**.
3.  Stelle die benötigten Eigenschaften ein.



## Optionen


<div class="mw-translate-fuzzy">

-   Fassaden teilen die gemeinsamen Eigenschaften und Verhaltensweisen aller [Arch Komponenten](Arch_Component/de.md)
-   Fassadenriegel können aus einem automatischen Rechteckprofil (setze ihre **Mullion Size**-Eigenschaften) oder aus einem benutzerdefinierten Profil (setze die **Mullion Profile**-Eigenschaft) erstellt werden. Die Riegel können mittig über jeder Kante oder durch das Deaktivieren der **Center Profile**-Eigenschaft relativ zum Ursprungspunkt (0,0,0) platziert werden. Wenn du bspw. ein Profil geringfügig hinter den Paneelen platzieren möchtest, würdest du dieses Profil geringfügig unter den Ursprungspunkt (0,0,0) ziehen
-   Fassaden unterstützen [Mehrfachmaterialien](Arch_MultiMaterial/de.md). Innerhalb des Mehrfachmaterials wird die **Frame**-Ebene für die Riegel verwendet und die **Glass panel**-Ebene für Glasscheiben oder **Solid panel**, falls keine Glasscheibenebene im Mehrfachmaterial existiert
-   Fassaden können auf einem linearen Objekt wie einer Linie, einem Bogen oder einem Linienzug basieren. In diesem Fall wird - intern - eine Basisoberfläche durch extrudieren des linearen Objekts entlang der durch die **Vertical Direction**-Eigenschaft vorgegebenen Richtung erstellt, in der durch die **Height**-Eigenschaft vorgegebenen Länge.


</div>



## Eigenschaften


<div class="mw-translate-fuzzy">

Vorhangfassaden erben die Eigenschaften von [Arch Komponenten](Arch_Component/de.md) Objekten und habe ebenfalls die folgenden zusätzlichen Eigenschaften:


</div>

-    {{PropertyData/de|Vertical Mullion Number}}:Die Anzahl der vertikalen Pfosten

-    {{PropertyData/de|Vertical Mullion Alignment}}: Ob das Profil der vertikalen Fenster-Riegel zur Oberfläche ausgerichtet wird

-    {{PropertyData/de|Vertical Sections}}: Die Anzahl der vertikalen Teile dieser Vorhangfassade

-    {{PropertyData/de|Vertical Mullion Height}}: Die Höhe der vertikalen Fassaden-Riegel, falls kein Profil ausgewählt wird

-    {{PropertyData/de|Vertical Mullion Width}}: Die Breite der vertikalen Fassaden-Riegel, falls kein Profil ausgewählt wird

-    {{PropertyData/de|Vertical Mullion Profile}}: Ein Profil für vertikale Fassaden-Riegel (deaktiviert vertikale Riegel-Abmessungen)

-    {{PropertyData/de|Horizontal Mullion Number}}: Die Anzahl der horizontalen Pfosten

-    {{PropertyData/de|Horizontal Mullion Alignment}}: Ob das Profil der horizontalen Fenster-Riegel zur Oberfläche ausgerichtet wird

-    {{PropertyData/de|Horizontal Sections}}: Die Anzahl der horizontalen Teile dieser Vorhangfassade

-    {{PropertyData/de|Horizontal Mullion Height}}: Die Höhe der horizontalen Fassaden-Riegel, falls kein Profil ausgewählt wird

-    {{PropertyData/de|Horizontal Mullion Width}}: Die Breite der horizontalen Fassaden-Riegel, falls kein Profil ausgewählt wird

-    {{PropertyData/de|Horizontal Mullion Profile}}: Ein Profil für horizontale Fassaden-Riegel (deaktiviert horizontale Riegel-Abmessungen)

-    {{PropertyData/de|Diagonal Mullion Number}}: Die Anzahl der diagonalen Pfosten

-    {{PropertyData/de|Diagonal Mullion Size}}: Die Größe der diagonalen Fassaden-Riegel, falls kein Profil ausgewählt wird

-    {{PropertyData/de|Diagonal Mullion Profile}}: Ein Profil für diagonale Fassaden-Riegel (deaktiviert diagonale Riegel-Abmessungen)

-    {{PropertyData/de|Panel Number}}: Die Anzahl der Paneele

-    {{PropertyData/de|Panel Thickness}}: Die Dicke der Paneele

-    {{PropertyData/de|Swap Horizontal Vertical}}: Tauscht horizontale und vertikale Linien

-    {{PropertyData/de|Refine}}: Führt Subtraktionen zwischen Komponenten aus, so dass keine Überlappungen bestehen

-    {{PropertyData/de|Center Profiles}}: Profil über Kanten zentrieren oder nicht

-    {{PropertyData/de|Vertical Direction}}: Die vom Objekt benutzte Referenz, um vertikale/horizontale Richtungen zu ermitteln. Halte es nah an der Richtung deiner Vorhangfassade

-    {{PropertyData/de|Height}}: Die Höhe dieser Vorhangfassade, falls sie auf einem linearen Objekt basiert

-    {{PropertyData/de|Host}}: Das Ursprungsobjekt dieser Vorhangfassade. Die Vorhangfassade erscheint in der Baumansicht eingebettet im Ursprungsobjekt (keine andere Aktion wird durchgeführt)



## Erstellen von Vorhangfassaden 


<div class="mw-translate-fuzzy">

Vorhangfassaden sind praktisch in Verbindung mit [Arch Wänden](Arch_Wall/de.md), um Fachwerkwände (Wände mit einer inneren strukturellen Ebene bestehend aus Rahmen, üblicherweise Holz oder Metall, anstelle eines homogenen Materials wie Beton oder Ziegeln) zu erstellen.


</div>

<img alt="" src=images/Frame_wall_example.png  style="width:780px;">

Die nachfolgend beschriebene Prozedur erstellt eine Wand und eine Vorhangfassade basierend auf der gleichen Basislinie, gibt der Wand dann ein Mehrfachmaterial, das einen leeren Platz lässt, wo die Vorhangfassade platziert wird.


<div class="mw-translate-fuzzy">

1.  Erstelle eine normale [Arch Wand](Arch_Wall/de.md), z.B. durch anklicken zweier Punkte eines bestehenden linearen Objekts
2.  Wähle das Basisobjekt der neu erstellten Arch Wand
3.  Drücke die **<img src="images/Arch_CurtainWall.svg" width=16px> [Arch Vorhangfassade](Arch_CurtainWall/de.md)**-Schaltfläche oder drücke die **C**-, dann die **W**-Taste, um eine Vorhangfassade aus derselben Basislinie wie die Wand zu erstellen
4.  Stelle sicher, dass sowohl die Wand als auch die Vorhangfassade die gleiche **Height** (Höhe) haben
5.  Setze die Anzahl der **horizontal sections** (horizontalen Abschnitte) der Vorhangfassade auf Null, falls du nur vertikale Rahmen haben möchtest
6.  Setze die gewünschte Werte für **horizontal mullion width** (horizontale Riegelbreite) und **horizontal mullion height** (horizontale Riegelhöhe) oder nutze ein **mullion profile** (Riegelprofil)
7.  Bereite zwei (oder mehr) [Materialien](Arch_SetMaterial/de.md) vor, eins für die Paneele, und eins für die Lücken, in denen der Rahmen sein wird
8.  Erstelle ein [Mehrfachmaterial](Arch_MultiMaterial/de.md) und nutze dabei eine Ebene des Paneel-Materials, eine mit dem Leermaterial mit einem negativen Breitenwert (der dafür sorgt, dass es nicht gezeichnet wird), der mit der vertikalen Riegelhöhe der Vorhangfassade übereinstimmt, und einer weiteren Ebene mit Paneel-Material
9.  Füge das Mehrfachmaterial zur Wand hinzu
10. Setze die **Host**-Eigenschaft der Vorhangfassade auf die Wand, die wir zuerst erstellt haben


</div>



## Skripten


**Siehe auch:**

[Arch API](Arch_API/de.md) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).


<div class="mw-translate-fuzzy">

Das Vorhangfassaden Werkzeug kann in [Makros](macros/de.md) und aus der [Python](Python/de.md) Konsole aus mit folgender Funktion verwendet werden:


</div>


```python
MyCurtainWall = makeCurtainWall(baseobj)
```

Beispiel:


```python
import FreeCAD, Draft, Arch

p1 = FreeCAD.Vector(0, 0, 0)
p2 = FreeCAD.Vector(2000, 0, 0)
baseline = Draft.makeLine(p1, p2)
baseface = FreeCAD.ActiveDocument.addObject('Part::Extrusion','Extrusion')
baseface.Base = baseline
baseface.DirMode = "Normal"
baseface.LengthFwd = 2000
curtainwall = Arch.makeCurtainWall(baseface)
curtainWall.VerticalSections = 6
FreeCAD.ActiveDocument.recompute()
```



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch CurtainWall/de
