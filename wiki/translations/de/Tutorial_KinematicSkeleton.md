---
 TutorialInfo:e
   Topic: Assembly3, ein Kinematik-Skelett
   Level: Grundwissen über Assembly3 und Sketcher ist hilfreich
   FCVersion: 0.20 und neuer
   Time: 40 Minuten
   Author: User:FBXL5
   SeeAlso: Tutorial_KinematicAssembly/de, Tutorial_KinematicController/de
---

# Tutorial KinematicSkeleton/de





## Einleitung

In dieser Anleitung geht es darum, einen einfachen 2D-Mechanismus zu erstellen und daran 3D-Objekte zu befestigen, hauptsächlich mit den Werkzeugen des externen Arbeitsbereichs <img alt="" src=images/Assembly3_workbench_icon.svg  style="width:16px;"> [Assembly3](Assembly3_Workbench/de.md).

Diese Anleitung verwendet nicht das Skeleton-Sketch-Prinzip (siehe Assembly3 [Create-Skeleton-Sketch](https://github.com/realthunder/FreeCAD_assembly3/wiki/Create-Skeleton-Sketch) auf GitHub).

Stattdessen werden <img alt="" src=images/PartDesign_Body.svg  style="width:16px;"> [PartDesign Bodies](PartDesign_Body/de.md) (Körper) verwendet, die jeweils nur eine <img alt="" src=images/Workbench_Sketcher.svg  style="width:16px;"> [Skizze](Sketcher_Workbench/de.md) enthalten, um einen 2D-Mechanismus aufzubauen, ein **Skizzen-Skelett**.

Die Maße und die Farben wurden von der Anleitung [SolveSpace tutorial](http://solvespace.com/linkage.pl) übernommen, auf die sich auch die Assembly3-GitHub-Seite bezieht (siehe oben).

## Skizzen-Skelett 

Dieses sogenannte Skizzen-Skelett besteht aus mehreren einzelnen <img alt="" src=images/PartDesign_Body.svg  style="width:16px;"> [Körpern](PartDesign_Body/de.md) und einem <img alt="" src=images/Assembly_New_Assembly.svg‎‎  style="width:16px;"> [Assembly](Assembly3_CreateAssembly.md)-Container. Um weitere Objekte befestigen zu können, wird jeder Körper in einen eigenen Assembly-Container gepackt.

### 2D-Body-Objekte 

Die Körper (Bodies) und ihre Skizzen, die in diesem Zusammenbau (auch Baugruppe genannt) verwendet werden:

-   Eine Grundplatte (grün)
-   Eine Kurbel (blau)
-   Zwei bewegliche Scheiben (rot und grau)
-   Vier Verbindungsstangen (weiß, gelb, lila und braun)

<img alt="" src=images/Assembly3_SketchSkeleton-01.png  style="width:400px;"> 
*Alle acht Skizzen sind unterschiedlich eingefärbt und durch das Verschieben ihrer übergeordneten Körper, manuell positioniert*

Die Form kann von dem tatsächlichen Teil abweichen, aber die Position der Geometrien, die die Gelenke festlegen, müssen genau sein.

### Assembly-Container 

#### Übergeordneter Zusammenbau 

Um die Positionen aller Körper festzusetzen oder zu steuern, braucht man ein <img alt="" src=images/Assembly_New_Assembly.svg‎‎  style="width:16px;"> Assembly-Objekt. Das fügt dem Konstruktionsbaum in der [Baumansicht](Tree_view/de.md) einen Ast für den Zusammenbau hinzu.

-   Die Schaltfläche **<img src="images/Assembly_New_Assembly.svg‎‎" width=16px> [Create assembly](Assembly3_CreateAssembly/de.md)** drücken, um einen Zusammenbauast in der [Baumansicht](Tree_view/de.md) zu erstellen.

### Unterbaugruppen

Diese Aktion wiederholt man, um für jeden Körper (Body) ein Assembly-Objekt zu erstellen, in dessen Parts-Container das jeweilige Body-Objekt gezogen wird. Danach setzt man den Körper in seiner Baugruppe fest:

1.  Das Assembly-Objekt aktivieren (Doppelklick).
2.  Einen Kreis/Bogen auswählen, der zum Body-Objekt gehört.
3.  Die Schaltfläche **<img src="images/Assembly_ConstraintLock.svg‎‎" width=16px> [Create "Locked" constraint](Assembly3_ConstraintLock/de.md)** drücken, um den Körper innerhalb seiner Unterbaugruppe festzusetzen.

Die Kurbelbaugruppe sollte beispielsweise so aussehen:

<img alt="" src=images/Assembly3_SketchSkeleton-25.png  style="width:500px;"> 
*Der Unterbaugruppenast der Kurbel in der Baumansicht und die Kurbel mit ihrem festgesetzten Element in der 3D-Ansicht*

#### Konstruktionsbaum

In der Baumansicht werden alle Unterbaugruppenäste in den Parts-Container des übergeordneten Assembly-Objekts gezogen.

<img alt="" src=images/Assembly3_SketchSkeleton-26.png  style="width:300px;"> 
*Zusammenbauast in der Baumansicht*

Jetzt sind sie bereit, angeordnet zu werden.

### Festgesetzte Grundplatte 

Als Erstes braucht man ein unbewegliches Teil. Um die Grundplatte komplett festzusetzen, würde man normalerweise eine Fläche auswählen, aber in diesem Falle funktioniert es auch mit einem Kreis.

1.  Einen Kreis der Grundplatte auswählen.
2.  Die Schaltfläche **<img src="images/Assembly_ConstraintLock.svg‎‎" width=16px> [Create "Locked" constraint](Assembly3_ConstraintLock.md)** drücken, um die Grundplatte festzusetzen.

<img alt="" src=images/Assembly3_SketchSkeleton-02.png  style="width:300px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Assembly3_SketchSkeleton-03.png  style="width:300px;"> 
*Der ausgewählte Kreis → Die festgesetzte Grundplatte mit dem erzeugten Element-Objekt dessen Element-Koordinatemsystem (EKS) angezeigt wird (grün)*

### Gelenke

Für scharnierartige Gelenke wählt man einen Kreis aus jeder Skizze aus und verwendet die Randbedingung <img alt="" src=images/Assembly_ConstraintCoincidence.svg‎‎  style="width:16px;"> [Plane Coincidence](Assembly3_ConstraintCoincidence/de.md). Diese setzt nicht nur die XY-Ebenen beider Elemente komplanar zueinander fest, sondern setzt auch ihre Z-Achsen fluchtend (kollinear) fest.

1.  Jeweils einen Kreis der zu verbindenden Objekte auswählen.
2.  Die Schaltfläche **<img src="images/Assembly_ConstraintCoincidence.svg‎‎" width=16px> [Create "Plane Coincidence" constraint](Assembly3_ConstraintCoincidence/de.md)** drücken.

#### Grundplatte - Kurbel 

<img alt="" src=images/Assembly3_SketchSkeleton-04.png  style="width:300px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Assembly3_SketchSkeleton-05.png  style="width:300px;"> 
*Kreise auf Grundplatte und Kurbel ausgewählt → Verschobene Kurbel mit den erzeugten Element-Objekten und angezeigtem EKSen (grün)*

#### Grundplatte - Obere Scheibe 

<img alt="" src=images/Assembly3_SketchSkeleton-06.png  style="width:300px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Assembly3_SketchSkeleton-07.png  style="width:300px;"> 
*Kreise der Grundplatte und der oberen Scheibe ausgewählt → Verschobene Obere Scheibe*

zuvor erstellte Gelenke erkennt man an der Darstellung ihrer Randbedingungen (rot).

#### Kurbel - Stange 1 

<img alt="" src=images/Assembly3_SketchSkeleton-08.png  style="width:300px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Assembly3_SketchSkeleton-09.png  style="width:300px;"> 
*Kreise der Kurbel und der Stange 1 ausgewählt → Verschobene Stange 1 und verschwenkte Kurbel*

#### Obere Scheibe - Stange 1 

Das letzte Gelenk in dieser kinematischen Kette verbindet zwei Elemente, deren Z-Richtungen schon festgelegt sind, so dass nur noch eine Randbedingung <img alt="" src=images/Assembly_ConstraintPointOnLine.svg‎‎  style="width:16px;"> [Point on line](Assembly3_ConstraintPointOnLine/de.md) fehlt

1.  Jewils einen Kreis der zu verbindenden Objekte auswählen.
2.  Die Schaltfläche **<img src="images/Assembly_ConstraintPointOnLine.svg‎‎" width=16px> [Create "PointOnLine" constraint](Assembly3_ConstraintPointOnLine/de.md)** drücken.

<img alt="" src=images/Assembly3_SketchSkeleton-10.png  style="width:300px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Assembly3_SketchSkeleton-11.png  style="width:300px;"> 
*Kreise der Oberen Scheibe und der Stange 1 ausgewählt → Verschobene Stange 1, und verschwenkte Kurbel und Obere Scheibe*

Wenn die Z-Achsen dreier Elemente oder Gelenke Parallel verlaufen und auf derselben virtuellen Ebene liegen, kann der Gleichungslöser bei ihrer Neuausrichtung in einem folgenden Schritt versagen, da er nicht entscheiden kann, in welche Richtung das mittlere Gelenk geschwenkt werden soll. Dies könnte der Fall sein, für das ausgewählte Element der Stange 1, dem Kurbel-Stange 1-Gelenk und dem Grundplatte-Kurbel-Gelenk, wie sie hier vorliegen. Wenn es so ist, mussman dem Löser helfen und ein Objekt (z.B. die Kurbel) mit dem Werkzeug <img alt="" src=images/Assembly_AxialMove.svg  style="width:16px;"> [Axial move](Assembly3_AxialMove/de.md) von Hand drehen.

#### Obere Scheibe - Stange 2 

Eine weitere kinematische (Teil-)Kette startet mit den Randbedingungen <img alt="" src=images/Assembly_ConstraintCoincidence.svg‎‎  style="width:16px;"> [Plane Coincidence](Assembly3_ConstraintCoincidence/de.md).

<img alt="" src=images/Assembly3_SketchSkeleton-12.png  style="width:300px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Assembly3_SketchSkeleton-13.png  style="width:300px;"> 
*Kreise der Oberen Scheibe (oder der Grundplatte) und der Stange 2 ausgewählt → Verschobene Stange 2*

#### Stange 2 - Untere Scheibe 

<img alt="" src=images/Assembly3_SketchSkeleton-14.png  style="width:300px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Assembly3_SketchSkeleton-15.png  style="width:300px;"> 
*Kreise der Stange 2 und der Unteren Scheibe ausgewählt → Verschobene Untere Scheibe und verschwenkte Stange 2*

#### Obere Scheibe - Stange 3 

<img alt="" src=images/Assembly3_SketchSkeleton-16.png  style="width:300px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Assembly3_SketchSkeleton-17.png  style="width:300px;"> 
*Kreise der Oberen Scheibe und der Stange 3 ausgewählt → Verschobene Stange 3 und umgeordnete obere kinematische Teilkette*

#### Untere Scheibe - Stange 3 

Und auch diese kinematische (Teil-)Kette wird mit der Randbedingung <img alt="" src=images/Assembly_ConstraintPointOnLine.svg‎‎  style="width:16px;"> [Point on line](Assembly3_ConstraintPointOnLine/de.md) geschlossen.

<img alt="" src=images/Assembly3_SketchSkeleton-18.png  style="width:300px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Assembly3_SketchSkeleton-19.png  style="width:300px;"> 
*Kreise der Unteren Scheibe und der Stange 3 ausgewählt → Verschobene Stange 3 und umgeordnete kinematische Teilketten*

Zum Verbinden beider Kinematischer Teilketten wird Stange 4 verwendet, mit der Randbedingung <img alt="" src=images/Assembly_ConstraintCoincidence.svg‎‎  style="width:16px;"> [Plane Coincidence](Assembly3_ConstraintCoincidence/de.md) an einem Ende und der Randbedingung <img alt="" src=images/Assembly_ConstraintPointOnLine.svg‎‎  style="width:16px;"> [Point on line](Assembly3_ConstraintPointOnLine/de.md) am anderen.

#### Kurbel - Stange 4 

<img alt="" src=images/Assembly3_SketchSkeleton-20.png  style="width:300px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Assembly3_SketchSkeleton-21.png  style="width:300px;"> 
*Kreise der Kurbel und der Stange 4 ausgewählt → Verschobene Stange 4*

#### Untere Scheibe - Stange 4 

<img alt="" src=images/Assembly3_SketchSkeleton-22.png  style="width:300px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Assembly3_SketchSkeleton-23.png  style="width:300px;"> 
*Kreise der Unteren Scheibe und der Stange 4 ausgewählt → Verschobene Stange 4 und endgültige Anordnung des kinematischen Zusammenbaus*

### Antrieb

Da Assembly3 keine Möglichkeiten bietet, kinematische Zusammenbauten zu steuern, braucht man externe Hilfe, wie diese [Kinematiksteuerung](Tutorial_KinematicController/de.md). Damit diese Steuerung benutzt werden kann, muss das Label einer Randbedingung mit dem Suffix {{Incode|"Driver"}} markiert werden, um sie zu einer antreibenden Randbedingung (einen Antrieb) zu machen. Es kann zur Verdeutlichung durch ein {{Incode|"."}} oder {{Incode|"-"}} abgetrennt werden, da die Steuerung nur prüft, ob das Label mit {{Incode|"Driver"}} endet.

Dafür wird das Label des Grundplatte-Kurbel-Gelenks zu {{Incode|Base-Crank.Driver}} geändert.

### Fertiges Skelett 

Der fertige kinematische Zusammenbau mit deaktivierter Darstellung von Elementen und Randbedingungen sollte ungefähr so aussehen:

<img alt="" src=images/Assembly3_SketchSkeleton-24.png  style="width:500px;"> 
*Fertiger Zusammenbau in der [Baumansicht](Tree_view/de.md) und der [3D-Ansicht](3D_view/de.md)*

<img alt="" src=images/Assembly3_SketchSkeleton-27.gif  style="width:500px;"> 
*GIF-Animation, erstellt aus einer, mit der [Kinematiksteuerung](Tutorial_KinematicController/de.md) gespeicherten, Bildfolge*

## 3D-Geometrie befestigen 

Meine Erwartungen bezüglich der Befestigung eines neuen Objekts an einem Basisobjekt, das zu einem kinematischen Zusammenbau gehört, sahen ungefähr so aus:

-   Ein neues Objekt wird im Parts-Container des Basisobjekts abgelegt.
-   Die Position des neuen Objekts wird mit Bezug zum Basisobjekt ausgerichtet.
-   Festhalten des relativen Abstands und der Ausrichtung durch Aktivieren der Randbedingung Attachment.

Aber das wäre zu einfach gewesen.

Das Werkzeug <img alt="" src=images/Assembly_ConstraintAttachment.svg‎‎  style="width:16px;"> [Assembly3 ConstraintAttachment](Assembly3_ConstraintAttachment/de.md), wie alle Assembly3-Werkzeuge für Randbedingungen, baut für Positionierungsaufgaben auf der Verwendung von Element-Objekten und ihren Element-Koordinatensystemen (EKS) auf.

Daher ist das Befestigen von Objekten nur ein weiterer Weg Objekte zu einer (Unter-)Baugruppe hinzuzufügen.

Und so befestigt man z.B. Stange 4-3D an Stange 4:

Die Objekte haben unterschiedliche Ausrichtungen und das 3D-Objekt sollte einen Abstand zum 2D-Objekt haben.

1.  Ein neues Objekt in den Parts-Container des Basisobjekts ablegen.
2.  Zwei zusammenpassende Kreise oder Bögen auswählen.
3.  Die Schaltfläche **<img src="images/Assembly_ConstraintAttachment.svg‎‎" width=16px> [Create "Attachment" constraint](Assembly3_ConstraintAttachment/de.md)** drücken.

:   <img alt="" src=images/Assembly3_SketchSkeleton-28.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Assembly3_SketchSkeleton-29.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Assembly3_SketchSkeleton-30.png  style="width:200px;">



*Stange 4 (festgesetzt) und Stange 4-3D → Bögen ausgewählt → Veschobene Stange 4-3D (beide EKSe befinden sich an derselben Stelle, mit identischer Ausrichtung.)*

Es ist nun offensichtlich, dass das Werkzeug <img alt="" src=images/Assembly_ConstraintAttachment.svg‎‎  style="width:16px;"> [Assembly3 ConstraintAttachment](Assembly3_ConstraintAttachment.md) den Abstand und die Ausrichtung zwischen den beiden Objekten ignoriert.

Auf jeden Fall ist die Position jetzt festgeleg und es müssen nur noch der Winkel manuell angepasst und der gewünschte Abstand festgelegt werden:

-   Die {{PropertyData/de|Offset, Angle}} des ersten Elementes im Attachment-Container ändern, um die Ausrichtung anzupassen.
-   Die {{PropertyData/de|Offset, Position, z}} desselben Elements ändern, um einen Abstand festzulegen.

Falls die Eigenschaften des zweiten Elements geändert werden, erfolgt die Bewegung des Winkels und des Abstands in umgekehrter Richtung.

:   <img alt="" src=images/Assembly3_SketchSkeleton-30.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Assembly3_SketchSkeleton-31.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Assembly3_SketchSkeleton-32.png  style="width:200px;">



*Wie angefügt → Winkel angepasst → Abstand festgelegt*

Wenn an jedes 2D-Objekt ein 3D-Objekt angefügt wurde, könnte es ungefähr so aussehen:

<img alt="" src=images/Assembly3_SketchSkeleton-33.gif  style="width:500px;">

## Hinweise

Der Abschnitt [3D-Geometrie_befestigen](#3D-Geometrie_befestigen.md) kratzt nur an der Oberfläche des Themas Erweiterung von Unterbaugruppen und andere Randbedingungen oder Kombinationen von Randbedingungen können passender sein als die Randbedingung Attachment.

Es ist wichtig, dass ein kinematischer Zusammenbau nur in kleinen Schritten bewegt wird, da sonst der Gleichungslöser aufgibt und versagt. Es is fast unmöglich <img alt="" src=images/Assembly_Move.svg‎‎  style="width:16px;"> [Move part](Assembly3_MovePart/de.md) oder <img alt="" src=images/Assembly_AxialMove.svg‎‎  style="width:16px;"> [Axial move](Assembly3_AxialMove/de.md) für diese Aufgabe zu verwenden.

Die Randbedingung <img alt="" src=images/Assembly_ConstraintCoincidence.svg‎‎  style="width:16px;"> [Assembly3_ConstraintCoincidence](Assembly3_ConstraintCoincidence/de.md) wird dazu verwendet, den kinematischen Zusammenbaut anzutreiben, ihre {{PropertyData/de|Angle}} (durch die {{PropertyData/de|Lock Angle}} aktiviert) akzeptiert positive oder negative Gleitkommazahlen größer als 360 und kann daher mehrere vollständige Drehungen ausführen.



---
⏵ [documentation index](../README.md) > Tutorial KinematicSkeleton/de
