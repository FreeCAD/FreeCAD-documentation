---
 GuiCommand:
   Name: Arch CurtainWall
   Name/de: Arch Vorhangfassade
   MenuLocation: 3D/BIM , Vorhangfassade
   Workbenches: BIM_Workbench/de
   Shortcut: **C** **W**
   Version: 0.19
   SeeAlso: 
---

# Arch CurtainWall/de



## Beschreibung

Das Werkzeug **Arch Vorhangfassade** erstellt eine [Vorhangfassade](https://de.wikipedia.org/wiki/Vorhangfassade), indem es eine Grundfläche in viereckige Flächen unterteilt, dann vertikale Pfosten an den vertikalen Kanten und horizontale Pfosten an den horizontalen Kanten erzeugt und die Zwischenräume zwischen den Pfosten mit Platten füllt.

<img alt="" src=images/Arch_CurtainWall_example.png  style="width:780px;">

Vorhangwände können aus jeder Art von bestehendem Objekt erstellt werden, wobei alle Flächen des Objekts unterteilt werden. Es funktioniert daher am besten, wenn es mit einem Objekt verwendet wird, das nur eine Fläche hat. Typischerweise würdest du zuerst eine Fläche erstellen, vorzugsweise mit genau 4 Kanten, die den Bereich repräsentiert, den du mit einer Vorhangwand füllen möchtest, und dann das Werkzeug anwenden.

Vorhangwände können auch aus einem linearen Objekt, wie z. B. einer Linie, einem Bogen oder einer Polylinie, aufgebaut werden, wie das normale Werkzeug [Wand](Arch_Wall/de.md).

Flächen, die eine doppelte Krümmung haben, oder Flächen mit mehr als 4 Kanten funktionieren auch, aber das Ergebnis ist weniger vorhersehbar.

Die Flächen werden in viereckige Facetten aufgeteilt. Wenn die 4 Punkte der Facette koplanar sind, wird eine quadratische Facette erzeugt. Wenn nicht, wird sie in zwei Dreiecke geteilt und ein diagonaler Pfosten wird hinzugefügt.

Falls Sie eine unregelmäßige Unterteilung benötigen, ist es auch möglich, ein eigenes unterteiltes Objekt zu bauen, z. B. mit [Arch Gitter](Arch_Grid/de.md), und die vertikale und horizontale Unterteilung der Vorhangfassade auf 1 zu setzen.

Du kannst das Vorhangwand Werkzeug auch ohne ein ausgewähltes Objekt verwenden. In diesem Fall kannst du eine Grundlinie zeichnen, die dann vertikal extrudiert wird, um die Fläche zu bilden, auf der die Vorhangwand aufgebaut wird.



## Anwendung



### Zeichnung einer Vorhangwand von Grund auf 

1.  Sicherstellen, dass nichts ausgewählt ist.
2.  Es gibt mehrere Möglichkeiten, das Werkzeug aufzurufen:
    -   Die Schaltfläche **<img src="images/Arch_CurtainWall.svg" width=16px> [Vorhangfassade](Arch_CurtainWall/de.md)** drücken.
    -   Den Menüeintrag **3D/BIM → <img src="images/Arch_CurtainWall.svg" width=16px> Vorhangfassade** auswählen.
    -   Das Tastaturkürzel **C** dann **W**.
3.  Einen ersten Punkt in der 3D-Ansicht anklicken oder eine Koordinate eingeben.
4.  Einen zweiten Punkt in der 3D-Ansicht anklicken oder eine Koordinate eingeben.
5.  Die erforderlichen Eigenschaften einstellen.



### Erstellung einer Vorhangwand aus einem gewählten Objekt 

1.  Ein oder mehrere Basisgeometrieobjekte (Draft-Objekt, Skizze, usw.) auswählen.
2.  Das Werkzeug wie oben beschrieben aufrufen.
3.  Die erforderlichen Eigenschaften anpassen.



## Optionen

-   Fassaden teilen die gemeinsamen Eigenschaften und Verhaltensweisen aller [Arch Komponenten](Arch_Component/de.md)
-   Fassadenriegel können aus einem automatischen Rechteckprofil (setze ihre **Mullion Size**-Eigenschaften) oder aus einem benutzerdefinierten Profil (setze die **Mullion Profile**-Eigenschaft) erstellt werden. Die Riegel können mittig über jeder Kante oder durch das Deaktivieren der **Center Profile**-Eigenschaft relativ zum Ursprungspunkt (0,0,0) platziert werden. Wenn du bspw. ein Profil geringfügig hinter den Paneelen platzieren möchtest, würdest du dieses Profil geringfügig unter den Ursprungspunkt (0,0,0) ziehen
-   Fassaden unterstützen [Mehrfachmaterialien](Arch_MultiMaterial/de.md). Innerhalb des Mehrfachmaterials wird die **Frame**-Ebene für die Riegel verwendet und die **Glass panel**-Ebene für Glasscheiben oder **Solid panel**, falls keine Glasscheibenebene im Mehrfachmaterial existiert
-   Fassaden können auf einem linearen Objekt wie einer Linie, einem Bogen oder einem Linienzug basieren. In diesem Fall wird - intern - eine Basisoberfläche durch extrudieren des linearen Objekts entlang der durch die **Vertical Direction**-Eigenschaft vorgegebenen Richtung erstellt, in der durch die **Height**-Eigenschaft vorgegebenen Länge.



## Eigenschaften

Vorhangfassaden erben die Eigenschaften von [Arch Komponenten](Arch_Component/de.md) (Component-Objekte) und besitzen auch die folgenden zusätzlichen Eigenschaften:

-    {{PropertyData/de|Vertical Mullion Number}}:Die Anzahl der vertikalen Pfosten

-    {{PropertyData/de|Vertical Mullion Alignment}}: Ob das Profil der vertikalen Fenster-Riegel zur Oberfläche ausgerichtet wird

-    {{PropertyData/de|Vertical Sections}}: Die Anzahl der vertikalen Teile dieser Vorhangfassade

-    {{PropertyData/de|Vertical Mullion Height}}: Die Höhe der vertikalen Fassaden-Riegel, falls kein Profil ausgewählt wird

-    {{PropertyData/de|Vertical Mullion Width}}: Die Breite der vertikalen Fassaden-Riegel, falls kein Profil ausgewählt wird

-    {{PropertyData/de|Vertical Mullion Profile}}: Ein Profil für vertikale Fassaden-Riegel (deaktiviert vertikale Riegel-Abmessungen)

-    {{PropertyData/de|Override Edges}}: ({{Version/de|1.0}}) Eingegeben werden die Indexzahlen von Kanten von ArchSketch-/Sketch-Basisgeometrien (im Bearbeitungsmodus). Ausgewählte Kanten werden eingesetzt, um die Form dieser Arch-Vorhangfassade zu erstellen (anstatt standardmäßig alle Kanten zu verwenden). ; wird ignoriert, wenn Base-ArchSketch die ausgewählten Kanten zur Verfügung stellt. ERWEITERUNG durch ArchSketch: GUI-Werkzeug \'Edit Curtain Wall\' wird durch das externe <img alt="" src=images/SketchArch_Workbench.svg  style="width:16px;"> [SketchArch Add-on](https://github.com/paullee0/FreeCAD_SketchArch) zur Verfügung gestellt, um den Anwender die Werte interaktiv eingeben zu lassen. \'Toponaming-Tolerant\' wenn ArchSketch als Basis eingesetzt wird (und das SketchArch Add-on installiert ist). Warnung: Nicht \'Toponaming-Tolerant\' wenn nur eine Skizze eingesetzt wird. (Siehe Forum - <https://forum.freecad.org/viewtopic.php?t=73018&start=40#p756554>)

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

Vorhangfassaden sind praktisch in Verbindung mit [Arch Wänden](Arch_Wall/de.md), um Fachwerkwände (Wände mit einer inneren strukturellen Ebene bestehend aus Rahmen, üblicherweise Holz oder Metall, anstelle eines homogenen Materials wie Beton oder Ziegeln) zu erstellen.

<img alt="" src=images/Frame_wall_example.png  style="width:780px;">

Die nachfolgend beschriebene Prozedur erstellt eine Wand und eine Vorhangfassade basierend auf der gleichen Basislinie, gibt der Wand dann ein Mehrfachmaterial, das einen leeren Platz lässt, wo die Vorhangfassade platziert wird.

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



## Skripten


**Siehe auch:**

[Arch API](Arch_API/de.md) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Das Werkzeug Vorhangfassade kann in [Makros](Macros/de.md) und von der [Python](Python/de.md)-Konsole aus mit den folgenden Funktionen verwendet werden:


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





{{BIM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > Arch CurtainWall/de
