---
- TutorialInfo   */de
   Topic   * Skizzieren
   Level   * Anfänger
   Time   * 15 Minuten
   Author   *[http   *//freecadweb.org/wiki/index.php?title=User   *Drei Drei]
   FCVersion   *0.16 oder höher
   Files   *
}}

### Einleitung

Dieses Tutorium soll den Leser in den grundlegenden Arbeitsablauf des [PartDesign Arbeitsbereich](PartDesign_Workbench/de.md) einführen. Der Leser wird sehen, wie man 3D Objekte auf der Grundlage von Skizzen erstellt, Subtraktionsoperationen durchführt und wie man bestimmte Formelemente in einem Muster nachbildet.

<img alt="" src=images/Sketcher_tutorial_result.png  style="width   *480px;">

### Anforderungen

-   FreeCAD Version 0.17 oder höher
-   Der Leser hat das [Grundlegende Skizzierer Tutorium](Basic_Sketcher_Tutorial/de.md) abgeschlossen.

### Verfahren

#### Erstellen von 3D Geometrie 

Der Zweck des **PartDesign Arbeitsbereichs** ist es, dem Benutzer die Erstellung von Geometrie im 3D Raum zu ermöglichen. Als solche ist sie mit Werkzeugen ausgestattet, um Skizzen zu nutzen und sie in 3D Objekte umzuwandeln.

Um dies zu erreichen, gibt es zwei Werkzeuge   * <img alt="" src=images/PartDesign_Pad.svg  style="width   *32px;"> [Polster](PartDesign_Pad/de.md) und <img alt="" src=images/PartDesign_Revolution.svg  style="width   *32px;"> [Drehung](PartDesign_Revolution/de.md). Neben ihren subtraktiven Gegenstücken (<img alt="" src=images/PartDesign_Pocket.svg  style="width   *32px;"> [Tasche](PartDesign_Pocket/de.md) und <img alt="" src=images/PartDesign_Groove.svg  style="width   *32px;"> [Nut](PartDesign_Groove/de.md)) bilden sie die meisten der von diesem Arbeitsbereich verwendeten üblichen Aktionen.

1.  Wechsle in den Arbeitsbereich PartDesign.
2.  Mit der Skizze ausgewählt in der [Baumansicht](tree_view/de.md), drücke **[PartDesign Körper](File   *PartDesign_Body.svg   16px]] [[PartDesign_Body/de.md)**, Wähle die Standard XY-Ebene und drücke **OK**. Die Skizze sollte nun innerhalb des Körpers erscheinen.
3.  Wähle <img alt="" src=images/PartDesign_Pad.svg  style="width   *32px;"> [Polster](PartDesign_Pad/de.md)
4.  Setze den Abstand auf 5 mm
5.  Wähle **OK**

Eine andere Möglichkeit zum Erzeugen von 3D Geometrie ist das <img alt="" src=images/PartDesign_Revolution.svg  style="width   *32px;"> [Drehungs](PartDesign_Revolution/de.md) Werkzeug.

<img alt="" src=images/PartDesign_revolution_exercise.png  style="width   *480px;">

1.  Erstelle eine neuen Körper **[PartDesign Körper](File   *PartDesign_Body.svg   16px]] [[PartDesign_Body/de.md)**, und dann eine Skizze auf der Grundlage des obigen Bildes.
2.  Die Skizze kann sich auf jeder beliebigen Ebene befinden, sollte aber mit der horizontalen Achse deckungsgleich sein.
3.  Wähle <img alt="" src=images/PartDesign_Revolution.svg  style="width   *32px;"> [Drehung](PartDesign_Revolution/de.md) <img alt="" src=images/PartDesign_Revolution.png  style="width   *24px;">.
4.  Setze die \"Achse\" auf die \"Horizontale Skizzenachse\"
5.  Setze den Winkel Winkel auf 360°.

#### Subtraktions Merkmale 

Wir beginnen mit der Erstellung einer Skizze mit der Form, die wir subtrahieren wollen.

1.  Wähle die obere flache Seite der \"Drehung\"
2.  Wähle <img alt="" src=images/Sketcher_NewSketch.svg‎‎  style="width   *32px;"> [Neue Skizze](Sketcher_NewSketch/de.md)
3.  Wähle <img alt="" src=images/Sketcher_External.svg  style="width   *32px;"> [Externe Geometrie](Sketcher_External/de.md)
4.  Nähere dich der Kante des Polsters. Ein Bogen sollte hervorgehoben werden
5.  Wähle den Bogen. Ein Bogen in einer anderen Farbe sollte in der Skizze erscheinen
6.  Erzeuge ein Sechseck, das auf demselben Punkt wie der Bogen zentriert ist, und setze den Radius des Referenzkreises auf 5 mm


{{Message| '''Externe Geometrie'''
Wenn ein 3D Element erstellt wurde, ist es möglich, innerhalb einer Skizze Referenzen auf dieses Element zu erstellen.
# Wähle <img src="images/Sketcher_External.svg" width=32px> [Externe Geometrie](Sketcher_External/de.md).
# Nähere dich dem Element, auf das du referenzieren möchtest, z.B. die Kante eines '''Polsters'''.
# Klicke darauf
# Neue Elemente in einer anderen Farbe sollten in der Skizze an der Stelle erscheinen, auf die du Bezug nehmen möchtest.
---

# PartDesign tutorial/de

 
<img alt="" src=images/PartDesign_pocket_exercise.png  style="width   *480px;">

Danach werden wir eine **Taschen** Funktion anwenden.

1.  Wähle die Skizze
2.  Wähle <img alt="" src=images/PartDesign_Pocket.svg  style="width   *32px;"> [Tasche](PartDesign_Pocket/de.md)
3.  Setze den Abstand auf **Durch alles**

#### Muster Merkmale 

Rufe das extrudierte Profil auf, das zu Beginn des Tutoriums erstellt wurde.

1.  Wähle die obere Fläche des Objekts
2.  Erstelle eine neuen Skizze
3.  Erstelle Referenzgeometrie, die mit dem oberen Arm der Figur verknüpft ist
4.  Erstelle einen Kreis, der zum Mittelpunkt des Bezugsbogens beschränkt ist
5.  Setze seinen Radius auf 3 mm
6.  Vertiefe die Skizze durch das gesamte Werkstück

Anstatt für jede Bohrung in der Skizze einen Kreis zu erstellen, werden wir das Konzept der **Muster Formelemente** einführen. Diese Werkzeuge arbeiten, indem sie ein bereits erstelltes Formelement im Werkstück replizieren, das wir in einer linearen oder kreisförmigen Anordnung reproduzieren möchten. Wir werden eine Kombination von **linearen** und **polaren** Mustermerkmalen gleichzeitig verwenden, um das endgültige Werkstück zu erhalten.

1.  Wähle das Taschen Formelement in der **Baumansicht**, das wir gerade erstellt haben.
2.  Wähle <img alt="" src=images/PartDesign_MultiTransform.svg  style="width   *32px;"> [MehrfachUmwandlung](PartDesign_MultiTransform/de.md)

In der Combo Ansicht werden wir nun gebeten, die von uns gewünschten **Umwandlungen** einzuführen. Beachte, dass wir im Menü **MehrfachUmwandlungs Parameter** sehen, dass FreeCAD die Tasche als *\'Original Formelement* identifiziert hat und ein zweites Feld fordert uns auf, *\'es rechts zu klicken*, um die Musterformelemente einzuführen.

1.  Rechtsklicke das Kästchen
2.  Wähle **Lineares Muster hinzufügen**
3.  Setze die **Richtung** auf **Vertikale Skizzenachse**
4.  Setze Länge auf 10 mm
5.  Häufigkeiten bei 2 % belassen
6.  Klicke OK
7.  Rechtsklicke erneut auf das Kästchen, um ein **Polares Muster** hinzuzufügen. Beachte, dass die 3D Ansicht jetzt das lineare Muster hinzugefügt hat.
8.  Setze Häufigkeiten auf 5
9.  Klicke OK zweimal

Nach Abschluss dieser Aufgabe solltest du das folgende Ergebnis haben.

<img alt="" src=images/PartDesign_multitransform_exercise.png  style="width   *480px;">

Wenn nicht, bearbeite den MehrfachUmwandlungs Vorgang erneut, indem du in der Baumansicht darauf doppelklickst. Überprüfe beide Muster Formelemente, um notwendige Modifikationen zu erkennen, wie z.B. die **Achse** und ob die **Richtung** umgekehrt werden muss.

Wir sind jetzt mit dem grundlegenden Workflow für den [PartDesign Arbeitsbereich](PartDesign_Workbench/de.md) fertig.



---
![](images/Right_arrow.png) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign tutorial/de
