---
- TutorialInfo:/de
   Topic:Modellierung
   Level:Anfänger
   Author:[EmmanuelG](User_EmmanuelG.md)
   Time:1 Stunde
   FCVersion:0.16 oder höher
   Files:[https://www.thingiverse.com/thing:2403310 Thingiverse 2403310]
---

# Toothbrush Head Stand/de







## Ein alltägliches Problem 

Elektrische Zahnbürsten kommen selten mit einem Ständer für die Köpfe, während Sie in einer Familie oftmals mehrere Köpfe sehen, die mit einem Gerät benutzt werden. Viele Leute, die ein gemeinsames Problem haben, führen zu einer Vielzahl von Lösungen, wie man u.a. auf Thingiverse sieht (200-800 Projekte befassen sich damit). Hier ist die erste Antwort und wie man sie entwirft.

Dieses Tutorial wird Sie durch die notwendigen Schritte führen, um das in der folgenden Abbildung gezeigte Teil mit Hilfe von grundlegenden Werkzeugen aus dem [Part Design-Arbeitsbereich](PartDesign_Workbench.md) zu modellieren (viele der Werkzeuge und Möglichkeiten werden nicht behandelt).

![](images/TBHS-model.png )



## Erste Idee: Eine Platte 

-   Auf der Startseite von FreeCAD wähle ![](images/Workbench_PartDesign.svg‎‎ ) *Part Design*, oder erstelle ein neues Dokument und wähle den *Part Design* Arbeitsbereich.

![](images/TBHS-0.png )



### Eine Skizze erstellen 

-   Klicke auf <img alt="" src=images/Sketcher_NewSketch.svg  style="width:32px;"> [**Neue Skizze**](Sketcher_NewSketch.md), entweder aus dem kontextbezogenen Aufgabenmenü links oder aus der Werkzeugleiste oben oder aus dem Part Design Menü oben.

<img alt="" src=images/TBHS-1.JPG  style="width:800px;">

Ein Dialog fordert dich auf, die Skizzenausrichtung zu wählen und einen Versatz anzugeben.

-   Wir wählen die XY Ebene wie in der obigen Abbildung gezeigt (diese Orientierung entspricht der üblichen Ebene der meisten 3D Drucker) und drücken dann *OK*.

<img alt="" src=images/TBHS-2.JPG  style="width:800px;">

Du siehst nun die XY Ebene von oben und hast Zugriff auf die Zeichenwerkzeuge.

-   Klicke auf <img alt="" src=images/Sketcher_CreateRectangle.svg  style="width:32px;"> [**Rechteck**](Sketcher_CreateRectangle/de.md).
-   Klicke, um einen ersten Punkt zu platzieren.
-   Klicke, um die gegenüber liegende Ecke zu platzieren.
-   Drücke **ESC** oder drücke die rechte Maustaste, um das Werkzeug zu beenden.

<img alt="" src=images/TBHS-3.JPG  style="width:800px;">

Du hast nun ein schwebendes Rechteck ohne festgelegte Abmessungen.

-   Klicke auf eine Seite des Rechtecks, so dass du Zugriff auf die Beschränkungswerkzeuge rechts neben der Werkzeugleiste hast (abhängig von der Größe Ihres Bildschirms musst du diese nach links ziehen, um sie alle zu sehen)
-   Klicke auf <img alt="" src=images/Constraint_Length.png  style="width:32px;"> [**Abstand**](Sketcher_ConstrainDistance/de.md)
-   Ein Dialog fordert auf, eine Abmessung festzulegen. Gib 80 mm ein, klicke OK.
-   Wiederhole dies mit der anderen Seite des Rechtecks, ebenfalls 80 mm.

<img alt="" src=images/TBHS-4.JPG  style="width:800px;">

Du hast nun ein schwebendes Quadrat.

-   Klicke auf die untere linke Ecke des Quadrats.
-   Klicken auf den Ursprung der XY Ebene (am Schnittpunkt der beiden dicken Linien).
-   Klicke auf <img alt="" src=images/Constraint_PointOnPoint.svg  style="width:32px;"> [**Deckungsgleich**](Sketcher_ConstrainCoincident/de.md).

<img alt="" src=images/TBHS-5.JPG  style="width:800px;">

Du hast nun eine vollständig bestimmte Skizze, wie dir der Löser auf der linken Seite und die Änderung der Farbe anzeigt. Es hat sich bewährt, eine Skizze immer vollständig zu bestimmen.

Eine unterbestimmte Skizze lässt Raum für ungewollte Änderungen, wenn du später etwas anpasst.

Umgekehrt ist eine überbestimmte Skizze auch nicht gut. In diesem Fall warnt dich der Löser vor überflüssigen Beschränkungen, und du solltest einige davon entfernen.

-   Um die Skizze zu verlassen, klicke entweder auf die *Schließen* Schaltfläche auf der linken Seite oder das <img alt="" src=images/Sketcher_LeaveSketch.png  style="width:32px;"> Symbol in der Werkzeugleiste, oder drücke **ESC**.

<img alt="" src=images/TBHS-6.JPG  style="width:800px;">

Du siehst jetzt nur noch das Quadrat, und das kontextbezogene Aufgabenmenü auf der linken Seite zeigt dir mehr Wahlmöglichkeiten als zuvor.



### Einen Block erstellen 

-   Klicke auf <img alt="" src=images/View-axometric.svg  style="width:32px;"> **Axonometrisch** unter den Standardansichten, um besser sehen zu können, was passieren wird.
-   Klicken auf <img alt="" src=images/PartDesign_Pad.svg  style="width:32px;"> **Block**.
-   Gib 4 mm ein und klicke *OK*.

<img alt="" src=images/TBHS-7.JPG  style="width:800px;">

Deine Skizze ist jetzt mit Rauminhalt !



### Eine Skizze darauf erstellen 

-   Wähle die Oberseite

<img alt="" src=images/TBHS-8.JPG  style="width:800px;">

Die Farbe der Seite wechselt und du hast mehr Wahlmöglichkeiten im kontextbezogenen Aufgabenmenü.

-   Klicke auf <img alt="" src=images/Sketcher_NewSketch.svg  style="width:32px;"> **Neue Skizze**. Da eine Fläche ausgewählt wurde, wirst du nicht aufgefordert, eine Ebene zu wählen.

<img alt="" src=images/TBHS-9.JPG  style="width:800px;">

-   Klicke auf <img alt="" src=images/Sketcher_Circle.svg  style="width:32px;"> [**Kreis**](Sketcher_CreateCircle/de.md), klicke, um den Mittelpunkt zu platzieren, bewege den Mauszeiger und klicke, um den Radius festzulegen.
-   Zeichne vier Kreise auf die Platte (von beliebiger Größe)
-   Drücke **ESC** oder die rechte Maustaste, um die Verwendung des Werkzeugs zu beenden.

<img alt="" src=images/TBHS-10.JPG  style="width:800px;">

-   Wähle die Kreise
-   Klicke <img alt="" src=images/Constraint_EqualLength.png  style="width:32px;"> [**Gleiche Länge**](Sketcher_ConstrainEqual/de.md)

<img alt="" src=images/TBHS-11.JPG  style="width:800px;">

Nun haben die Kreise den gleichen Radius.

-   Klicke <img alt="" src=images/Sketcher_External.svg  style="width:32px;"> [**Externe Geometrie**](Sketcher_External/de.md).
-   Klicke auf die vier Seiten des Quadrats, und es werden vier magentafarbene Linien hinzugefügt.

<img alt="" src=images/TBHS-12.JPG  style="width:800px;">

Diese Linien dienen als Referenz, um die Kreise zu positionieren.

-   <img alt="" src=images/Constraint_Length.png  style="width:32px;"> [**Abstand**](Sketcher_ConstrainDistance/de.md) anklicken.
-   Einen Kreismittelpunkt anklicken.
-   Auf eine magentafarbene Linie klicken.
-   Den Abstand eingeben (20 mm von jeder Seite).

<img alt="" src=images/TBHS-13.JPG  style="width:800px;">

-   Klicke auf einen Kreis
-   Klicke auf <img alt="" src=images/Sketcher_ConstrainRadius.svg  style="width:32px;"> [**Radius**](Sketcher_ConstrainRadius/de.md) und setze ihn auf 1,5 mm.

<img alt="" src=images/TBHS-14.JPG  style="width:800px;">

-   Um die Skizze zu verlassen, klicke entweder auf die *Schließen* Schaltfläche zur Linken, oder das <img alt="" src=images/Sketcher_LeaveSketch.png  style="width:32px;"> Symbol in der Werkzeugleiste oder drücke **ESC**.

<img alt="" src=images/TBHS-15.JPG  style="width:800px;">



### Einen Block erstellen 

-   Klicke auf <img alt="" src=images/View-axometric.svg  style="width:32px;"> **Axonometrisch** unter den Standardansichten, um besser sehen zu können, was passieren wird.
-   Klicke auf <img alt="" src=images/PartDesign_Pad.svg  style="width:32px;"> **Block**.
-   Gib 25 mm ein und klicke *OK*.

<img alt="" src=images/TBHS-16.JPG  style="width:800px;">

Du hast die Grundform, sie braucht nur noch den letzten Schliff.



### Ecken abrunden 

-   Halte **STRG** gedrückt und klicke auf die vertikale Kante an jeder Ecke, um die vier auszuwählen.

Zögere nicht, dir zu helfen, indem du den Anzeigemodus (gleich links neben der Axonometrischen Ansicht) umschaltest zwischen <img alt="" src=images/DrawStyleWireFrame.svg  style="width:32px;"> **Drahtgitter** and <img alt="" src=images/DrawStyleFlatLines.svg  style="width:32px;"> **Drahtgitter und Schatten**.

<img alt="" src=images/TBHS-17.JPG  style="width:800px;">

-   Klicke auf <img alt="" src=images/PartDesign_Fillet.svg  style="width:32px;">[**Verrundung**](PartDesign_Fillet/de.md).
-   Setze den Radius auf 20 mm.

<img alt="" src=images/TBHS-18.JPG  style="width:800px;">

Viel besser.



### Es robuster machen 

Wir müssen Material an der Basis der Zylinder hinzufügen, um sie weniger rissanfällig zu machen. Aufgrund der Druckausrichtung werden diese kleinen Flächen an der Verbindungsstelle mit der Basis zerbrechlich sein.

-   Wähle die Kreise an der Basis der Zylinder

<img alt="" src=images/TBHS-19.JPG  style="width:800px;">

-   Klicke auf <img alt="" src=images/PartDesign_Chamfer.svg  style="width:32px;"> [**Fase**](PartDesign_Chamfer/de.md).
-   Setze sie auf 2 mm.

<img alt="" src=images/TBHS-20.JPG  style="width:800px;">



### Kanten anfasen 

-   Wähle die Fläche unter der Basis aus, füge eine <img alt="" src=images/PartDesign_Chamfer.svg  style="width:32px;"> **Fase** von 0,5 mm hinzu

Die erste Plastikschicht wird oft ein wenig zu stark gequetscht, dies gleicht das aus und spart dir Zeit bei der Reinigung des Modells. Wenn die erste Schicht in Ordnung ist, wird es nur schöner.

<img alt="" src=images/TBHS-21.JPG  style="width:800px;">

-   Wähle die Kanten am Rand der oberen Fläche aus (halte **STRG** ).

<img alt="" src=images/TBHS-23.JPG  style="width:800px;">

-   Füge eine <img alt="" src=images/PartDesign_Chamfer.svg  style="width:32px;"> **Fase** von 1 mm hinzu. Dies nur aus ästhetischen Gründen.

<img alt="" src=images/TBHS-22.JPG  style="width:800px;">

Tadaa!



## Als .STL exportieren 

-   Wähle in der Combo-Ansicht auf der linken Seite die Baumansicht anstelle des kontextbezogenen Aufgabenmenüs und klicke auf das letzte Element (die Fase).

<img alt="" src=images/TBHS-24.JPG  style="width:800px;">

-   Jetzt kannst du \"Export\...\" aus dem Dateimenü oben links auswählen und das Dateiformat .STL wählen.
-   Einfach ausdrucken :-)



## Inspiration

Das obige Modell stellt einen guten Startpunkt zur Nutzung von FreeCAD dar, aber als ein Zahnbürstenkopfständer hat es seine Schwächen: aufgrund der Druckausrichtung und der kleinen Oberfläche sind die Stifte bruchgefährdet.

Angeregt durch die Vielfalt der Lösungen, die sich andere Leute ausgedacht haben, werden wir diese zweite Version machen, die viel besser sein wird.

<img alt="" src=images/TBHS-v2.jpg  style="width:800px;">

Keine Sorge, es ist oftmals notwendig, für eine Idee mehrere Überarbeitungen vorzunehmen (z.B.: nachdem der Prototyp auf dem Bild verwendet wurde, haben wir mehr Platz zwischen den Köpfen hinzugefügt, damit sie sich nicht berühren).

In diesem zweiten Teil wirst du auch lernen, mehr Werkzeuge zu benutzen, wie die mächtige *Lineare Wiederholung*.



## Zweite Idee: Ein Band 

-   Erstelle ein neues Dokument und wähle den ![](images/Workbench_PartDesign.svg‎‎ ) *Part Design* Arbeitsbereich.



### Eine Skizze erstellen 

-   Erstelle eine <img alt="" src=images/Sketcher_NewSketch.svg  style="width:32px;"> **Neue Skizze** auf der XY Ebene.

<img alt="" src=images/TBHS-1.JPG  style="width:800px;">

-   Zeichne eine <img alt="" src=images/Sketcher_CreateSlot.svg  style="width:32px;"> [**Nut**](Sketcher_CreateSlot/de.md)
    -   Klicke, um den ersten Mittelpunkt zu platzieren
    -   Bewege den Mauszeiger, um die Länge und den Radius zu definieren
    -   Klicke, um den zweiten Mittelpunkt festzulegen

<img alt="" src=images/TBHS2-1.JPG  style="width:800px;">

Jetzt hast du eine schwebende Nut ohne festgelegte Abmessungen.

-   Klicke auf eine der horizontalen Linien der Nut
-   Klicke auf <img alt="" src=images/Constraint_Length.png  style="width:32px;"> [**Abstand**](Sketcher_ConstrainDistance/de.md)
-   Ein Dialog fordert dich auf, eine Abmessung festzulegen. Gib 75 mm ein, klicke auf OK.
    -   das ist für einen 3 Kopf Ständer, zähle 25 mm für jeden, wenn du mehr willst

<img alt="" src=images/TBHS2-2.JPG  style="width:800px;">

-   Klicke auf einen Punkt der horizontalen Linie
-   Klicke auf einen Punkt der anderen horizontalen Linie
-   Klicke auf <img alt="" src=images/Constraint_Length.png  style="width:32px;"> [**Distanz**](Sketcher_ConstrainDistance/de.md)
-   Ein Dialogfeld fordert dich auf, eine Abmessung festzulegen. Gib 29 mm ein, klicke auf OK.

<img alt="" src=images/TBHS2-3.JPG  style="width:800px;">

-   Zeichne eine <img alt="" src=images/Sketcher_CreateSlot.svg  style="width:32px;"> [**Nut**](Sketcher_CreateSlot/de.md) um die erste Nut herum.

<img alt="" src=images/TBHS2-4.JPG  style="width:800px;">

-   Mache die Mittelpunkte der zweiten Nut deckungsgleich mit den Mittelpunkten der ersten Nut mit <img alt="" src=images/Constraint_PointOnPoint.svg  style="width:32px;"> [**Deckungsgleich**](Sketcher_ConstrainCoincident/de.md).

<img alt="" src=images/TBHS2-5.JPG  style="width:800px;">

-   Klicke auf einen Punkt der horizontalen Linie der ersten Nut
-   Klicke auf einen Punkt der nächsten horizontalen Linie der zweiten Nut
-   Klicke auf <img alt="" src=images/Constraint_Length.png  style="width:32px;"> [**Abstand**](Sketcher_ConstrainDistance/de.md)
-   Ein Dialogfeld fordert dich auf, eine Abmessung festzulegen. Gib 3 mm ein, klicke auf OK.

<img alt="" src=images/TBHS2-6.JPG  style="width:800px;">

-   Um die Skizze vollständig zu beschränken
    -   klicke auf den unteren linken Punkt der zweiten Nut
    -   klicke auf den Ursprung der XY Ebene
    -   klicke auf <img alt="" src=images/Constraint_PointOnPoint.svg  style="width:32px;"> [**Deckungsgleich**](Sketcher_ConstrainCoincident/de.md)

<img alt="" src=images/TBHS2-7.JPG  style="width:800px;">

-   Um die Skizze zu verlassen, klicke entweder auf die *Schließen* Schaltfläche zur Linken oder das <img alt="" src=images/Sketcher_LeaveSketch.png  style="width:32px;"> Symbol in der Werkzeugleiste, oder drücke **ESC**.

<img alt="" src=images/TBHS2-8.JPG  style="width:800px;">



### Einen Block erstellen 

-   Klicken auf <img alt="" src=images/View-axometric.svg  style="width:32px;"> **Axonometrisch** unter den Standardansichten, um besser sehen zu können, was passieren wird.
-   Klicke auf <img alt="" src=images/PartDesign_Pad.svg  style="width:32px;"> **Block**.
-   Gib 30 mm ein und klicke OK.

<img alt="" src=images/TBHS2-9.JPG  style="width:800px;">



### Eine Skizze darauf erstellen 

-   Wähle die Oberseite

<img alt="" src=images/TBHS2-10.JPG  style="width:800px;">

-   Erstelle eine <img alt="" src=images/Sketcher_NewSketch.svg  style="width:32px;"> **Neue Skizze**. Da eine Fläche ausgewählt wurde, wirst du nicht aufgefordert, eine Ebene zu wählen.

<img alt="" src=images/TBHS2-11.JPG  style="width:800px;">

-   Zeichne ein <img alt="" src=images/Sketcher_CreateHexagon.svg  style="width:32px;"> [**Sechseck**](Sketcher_CreateHexagon/de.md)
    -   Klicke, um den Mittelpunkt zu platzieren
    -   Bewege den Mauszeiger, um den Radius zu definieren
    -   Klicke, um den Radius zu festzulegen

<img alt="" src=images/TBHS2-12.JPG  style="width:800px;">

-   Klicke auf eine Kante des Sechsecks
-   Klicke auf <img alt="" src=images/Constraint_Horizontal.svg  style="width:32px;"> [**Horizontal**](Sketcher_ConstrainHorizontal/de.md)

<img alt="" src=images/TBHS2-13.JPG  style="width:800px;">

-   Klicke auf den Mittelpunkt des Sechsecks
-   Klicke auf die horizontale Linie der XY Ebene
-   Klicke auf <img alt="" src=images/Constraint_Length.png  style="width:32px;"> [**Abstand**](Sketcher_ConstrainDistance/de.md)
-   Ein Dialogfeld fordert dich auf, eine Abmessung festzulegen. Gib 15 mm ein und klicke OK.

<img alt="" src=images/TBHS2-14.JPG  style="width:800px;">

-   Klicke auf den Mittelpunkt des Sechsecks
-   Klicke auf die vertikale Linie der XY-Ebene
-   Klicke auf <img alt="" src=images/Constraint_Length.png  style="width:32px;"> [**Abstand**](Sketcher_ConstrainDistance/de.md)
-   Ein Dialogfeld fordert dich auf, eine Abmessung festzulegen. Gib 10 mm ein, klicke auf OK.

<img alt="" src=images/TBHS2-15.JPG  style="width:800px;">

-   Klicke auf den blauen Kreis des Sechsecks
-   Klicke auf<img alt="" src=images/Constraint_Radius.png  style="width:32px;"> [**Radius**](Sketcher_ConstrainRadius/de.md)
-   Ein Dialogfeld fordert dich auf, eine Abmessung festzulegen. Gib 8 mm ein, klicke auf OK.

<img alt="" src=images/TBHS2-16.JPG  style="width:800px;">

-   Um die Skizze zu verlassen, klicke entweder auf die *Schließen* Schaltfläche auf der linken Seite oder das <img alt="" src=images/Sketcher_LeaveSketch.png  style="width:32px;"> Symbol in der Werkzeugleiste, oder drücke **ESC**.

<img alt="" src=images/TBHS2-17.JPG  style="width:800px;">



### Ein Loch erstellen 

-   Klicke auf <img alt="" src=images/View-axometric.svg  style="width:32px;"> **Axonometrisch** unter den Standardansichten, um besser zu sehen, was passieren wird.
-   Klicke auf <img alt="" src=images/PartDesign_Pad.svg  style="width:32px;"> [**Tasche**](PartDesign_Pocket/de.md).
-   Wähle \"zum ersten\" in der Auswahlliste und klicke *OK*.

<img alt="" src=images/TBHS2-18.JPG  style="width:800px;">



### Lineare Wiederholung 

-   Wähle in der Combo Ansicht auf der linken Seite die Baumansicht anstelle des kontextbezogenen Aufgabenmenüs, klicke auf die Taschen Funktion.
-   Klicke auf <img alt="" src=images/PartDesign_LinearPattern.svg  style="width:32px;"> [**Lineares Muster**](PartDesign_LinearPattern/de.md).
-   Setze die Länge auf 55 mm und Häufigkeit auf 3 dann klicke OK.

<img alt="" src=images/TBHS2-19.JPG  style="width:800px;">



### Eine Skizze darauf erstellen 

-   Wähle die Innenseite

<img alt="" src=images/TBHS2-20.JPG  style="width:800px;">

-   Klicke auf <img alt="" src=images/Sketcher_NewSketch.svg  style="width:32px;"> **Neue Skizze**. Da eine Fläche ausgewählt wurde, wirst du nicht aufgefordert, eine Ebene zu wählen.

<img alt="" src=images/TBHS2-21.JPG  style="width:800px;">

-   Klicke auf <img alt="" src=images/Sketcher_Circle.svg  style="width:32px;"> [**Kreis**](Sketcher_CreateCircle/de.md), klicke, um den Mittelpunkt zu positionieren, bewege den Zeiger und klicke, um den Radius festzulegen.

<img alt="" src=images/TBHS2-22.JPG  style="width:800px;">

-   Klicke auf den Mittelpunkt des Kreises
-   Klicke auf die horizontale Linie der XY Ebene
-   Klicke auf<img alt="" src=images/Constraint_Length.png  style="width:32px;"> [**Abstand**](Sketcher_ConstrainDistance/de.md)
-   Ein Dialog fordert dich auf, eine Abmessung festzulegen. Gib 15 mm ein und klicke OK.

<img alt="" src=images/TBHS2-23.JPG  style="width:800px;">

-   Klicke auf den Mittelpunkt des Kreises
-   Klicke auf die vertikale Linie der XY-Ebene
-   Klicke auf <img alt="" src=images/Constraint_Length.png  style="width:32px;"> [**Abstand**](Sketcher_ConstrainDistance/de.md)
-   Ein Dialog fordert dich auf, eine Abmessung festzulegen. Gib 10 mm ein, klicke auf OK.

<img alt="" src=images/TBHS2-24.JPG  style="width:800px;">

-   Klicke auf den Kreis
-   Klicke auf <img alt="" src=images/Constraint_Radius.png  style="width:32px;"> [**Radius**](Sketcher_ConstrainRadius/de.md)
-   Ein Dialogfeld fordert dich auf, eine Abmessung festzulegen. Gib 3.5 mm ein, klicke auf OK.

<img alt="" src=images/TBHS2-25.JPG  style="width:800px;">

-   Um die Skizze zu verlassen, klicke entweder auf die *Schließen* Schaltfläche zur Linken oder das <img alt="" src=images/Sketcher_LeaveSketch.png  style="width:32px;"> Symbol in der Werkzeugleiste, oder drücke **ESC**.

<img alt="" src=images/TBHS2-26.JPG  style="width:800px;">



### Einen Block erstellen 

-   Klicke auf <img alt="" src=images/View-axometric.svg  style="width:32px;"> **Axonometrisch** unter den Standardansichten, um besser sehen zu können, was passieren wird.
-   Klicken auf <img alt="" src=images/PartDesign_Pad.svg  style="width:32px;"> **Block**.
-   Gib 4 mm ein und klicke *OK*.

<img alt="" src=images/TBHS2-27.JPG  style="width:800px;">



### Lineare Wiederholung 

-   Wähle in der Combo Ansicht auf der linken Seite die Baumansicht anstelle des kontextbezogenen Aufgabenmenüs, klicke auf die Polster Funktion.
-   Klicke <img alt="" src=images/PartDesign_LinearPattern.svg  style="width:32px;"> [**Lineares Muster**](PartDesign_LinearPattern/de.md).
-   Setze die Länge auf 55 mm und Häufigkeit auf 3 dann klicke OK.

<img alt="" src=images/TBHS2-28.JPG  style="width:800px;">



### Formschräge

-   Selektieren Sie die Seite jedes runden Blocks

<img alt="" src=images/TBHS2-29.JPG  style="width:800px;">

-   Klicke auf <img alt="" src=images/PartDesign_Draft.svg  style="width:32px;"> [**Formschräge**](PartDesign_Draft/de.md).
-   Setze den Formschrägenwinkel auf 40°.
-   Klicke \"Neutrale Ebene\" und wähle die Seite, auf der die Skizze gezeichnet wurde.
-   Hake \"Entformungsrichtung umkehren\" an.

<img alt="" src=images/TBHS2-30.JPG  style="width:800px;">

Wir hätten eine Fase benutzen können, um etwas Ähnliches zu tun, aber die Entformschräge ist in diesem Fall angebrachter.

Fase = links / Entformschräge = rechts

<img alt="" src=images/TBHS2-30-chamfer.JPG  style="width:200px;"><img alt="" src=images/TBHS2-30-draft.JPG  style="width:200px;">



### Abschlüsse

-   Halte **STRG** gedrückt und wähle die Ober- und Unterseiten.

<img alt="" src=images/TBHS2-31-bottom.JPG  style="width:200px;"><img alt="" src=images/TBHS2-31-top.JPG  style="width:200px;">

-   -   Füge eine <img alt="" src=images/PartDesign_Chamfer.svg  style="width:32px;"> **Fase** von 0,5 mm hinzu.

<img alt="" src=images/TBHS2-31.JPG  style="width:800px;">

Perfekt!



## Als .STL exportieren 

-   Wähle in der Combo Ansicht auf der linken Seite die Baumansicht anstelle des kontextbezogenen Aufgabenmenüs und klicke auf das letzte Element (die Fase).

<img alt="" src=images/TBHS2-32.JPG  style="width:800px;">

-   Jetzt kannst du \"Export \...\" aus dem Dateimenü oben links und daraus das Dateiformat .STL wählen.
-   Drucke es statt der ersten Version oder um diese zu ersetzen, falls sie irgendwann zerbrochen ist ;-).


{{PartDesign Tools navi

}} {{Sketcher Tools navi}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [PartDesign](Category_PartDesign.md) > [Sketcher](Category_Sketcher.md) > Toothbrush Head Stand/de
