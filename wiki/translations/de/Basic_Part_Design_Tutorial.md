---
- TutorialInfo   */de
   Topic   *Modellieren
   Level   *Einsteiger
   Author   *Mark Stephen ([Quick61](User_Quick61.md)) und HarryGeier ([HarryGeier](User_HarryGeier.md))
   Time   *Unter einer Stunde
   FCVersion   *0.17 oder höher
   Files   *[https   *//github.com/FreeCAD/Examples/blob/master/Basic_Part_Design_Tutorial_Example_017_Files/Basic_Part_Design_Tutorial_017.fcstd Grundlagen Part Design für v0.17]
---

# Basic Part Design Tutorial/de






<div class="mw-translate-fuzzy">

Dieses Tutorium führt den neuen Benutzer in einige der Werkzeuge und Techniken ein, die im [Part Design Arbeitsbereich](PartDesign_Workbench/de.md) verwendet werden. Dieses Tutorium ist keine vollständige und umfassende Anleitung für den Part Design Arbeitsbereich und viele der Werkzeuge und Funktionen werden nicht behandelt. In diesem Lernprogramm wird der Benutzer durch die Schritte geführt, die erforderlich sind, um das im Bild unten gezeigte Teil mithilfe von Skizzen zu modellieren.


</div>

![](images/Tut17_final_refined.png )

Ein Video der gesamten Konstruktion ist hier   * <https   *//youtu.be/geIrH1cOCzc>


<div class="mw-translate-fuzzy">

( jeder Abschnitt hat sein eigenes separates Video unten )


</div>

## Bevor du anfängst 

## The Task 


<div class="mw-translate-fuzzy">

## Die Aufgabe 

In diesem Tutorium erstellst du mit dem Part Design Arbeitsbereich ein 3D Volumenmodell des Teils, das in der [Zeichnung](Drawing_Workbench/de.md) unten gezeigt wird. Alle für diese Aufgabe erforderlichen Maße sind vorhanden. Du fängst an mit der Erstellung einer Kernform aus einer Basisskizze und baust dann auf dieser Form auf, indem du so genannte Formelemente hinzufügst. Diese Funktionen fügen dem Festkörper entweder Material hinzu oder entfernen Material aus ihm, indem sie zusätzliche Skizzen und begleitende Formelemente Operationen verwenden. In diesem Tutorium werden nicht alle Funktionen und Werkzeuge verwendet, die im Part Design Arbeitsbereich zur Verfügung stehen, sondern es werden so viele verwendet, dass der Benutzer dieses Tutoriums eine grundlegende Basis erhält, auf der er sein Wissen und seine Fähigkeiten aufbauen kann.


</div>

## Das Bauteil 

![](images/Tutorial_Drawing_Sheet.png )

## Constructing The Part 

### Startup


<div class="mw-translate-fuzzy">

## Konstruieren des Teils 

### Beginn

Stelle zunächst sicher, dass du dich im Part Design Arbeitsbereich befindest. Dort wirst du ein neues Dokument erstellen wollen, falls du dies noch nicht getan hast. Es ist eine gute Angewohnheit, deine Arbeit oft zu speichern, also speichere vor allem das neue Dokument und gib ihm einen beliebigen Namen, den du gerne magst.


</div>


<div class="mw-translate-fuzzy">

Alle Arbeiten in Part Design beginnen mit einem [Körper](Glossary/de#Body.md). Dann bauen wir den Festkörper im Inneren des Körpers auf, indem wir mit einer [Skizze](Glossary/de#Sketch.md) anfangen.

um einen neuen Körper Container zu erstellen und zu aktivieren. *Hinweis   * Dieser Schritt kann ausgelassen werden. Wenn beim Erstellen einer Skizze kein vorhandener Körper gefunden wird, wird automatisch ein neuer erstellt und aktiviert.*

1.  Klicke auf <img alt="" src=images/PartDesign_NewSketch.svg  style="width   *32px;"> [Neue Skizze erstellen](PartDesign_NewSketch/de.md). Dadurch wird die Skizze innerhalb des gerade erstellten Körpers erstellt.
2.  Wir müssen definieren, wo die Skizze angehängt werden soll. Wir werden sie an eine Ebene aus dem [Ursprung](Glossary/de#Origin.md) des Körpers anhängen.
3.  Wähle im Aufgabenreiter in der Combo Ansicht die Option **YZ\_Ebene** in der Liste und drücke **OK**   *


</div>

1.  Click on <img alt="" src=images/PartDesign_Body.svg  style="width   *24px;"> [Create new body](PartDesign_Body.md) to create and activate a new Body Container. 
*Note   * this step can be omitted. When creating a sketch, if no existing Body is found, a new one will be automatically created and activated.*
2.  Click on <img alt="" src=images/PartDesign_NewSketch.svg  style="width   *24px;"> [Create new sketch](PartDesign_NewSketch.md). This will create the sketch within the just created body.
3.  We need to define where the sketch will be attached. We will attach it to a plane from the Body´s [Origin](Glossary#Origin.md).
4.  In the [Tasks tab](Task_panel.md) from the [Combo view](Combo_view.md), select **YZ\_Plane** in the list and press **OK**   *

<img alt="" src=images/Tut17_sketchplanes.png  style="width   *250px;">


<div class="mw-translate-fuzzy">

Hinweis   * Es ist möglich, dass die OK Schaltfläche nicht sichtbar ist, wenn das Seitenpaneel nicht breit genug ist. Du kannst es breiter machen, indem du an seinem rechten Rand ziehst. Bewege den Mauszeiger über den Rand; wenn sich der Zeiger in einen Zwei-Wege Pfeil verwandelt, halte die linke Maustaste gedrückt und ziehe.\'\'


</div>

Sobald du auf OK klickst, wechselt FreeCAD automatisch in den [Skizzierer Arbeitsbereich](Sketcher_Workbench/de.md) und öffnet die Skizze im Bearbeitungsmodus   *

![](images/Tut17_sketcherempty.png )

### Create the sketch 


<div class="mw-translate-fuzzy">

### Die Skizze erstellen 

Als nächstes das ![ 32px](images/_Sketcher_CreatePolyline.svg )[Polylinie](Sketcher_CreatePolyline/de.md) Werkzeug verwenden und eine Form ähnlich der im nächsten Bild erstellen. Es muss nicht perfekt sein, da die endgültige Form durch Einschränkungen erzeugt wird. Sobald die Grundform erstellt ist, werden die Einschränkungen angewandt. Wenn die automatischen Einschränkungen aktiviert sind, werden einige dieser Einschränkungen automatisch angewendet, andernfalls fügt man die folgenden Schritte aus. Doch zuerst muss das Polylinien-Werkzeug durch einen Rechtsklick oder zweimaliges Drücken der **Esc**-Taste verlassen worden sein; der Maus-Cursor sollte von einem Fadenkreuz zurück zum Standard-Pfeil-Cursor gewechselt sein. (Drücken Sie die **Esc**Taste \_nicht\_ ein drittes Mal, sonst wird der Skizzeneditiermodus verlassen. Falls das passiert, auf den Modell-Reiter klicken, dann doppelt auf das Skizzenelement im Baum klicken oder rechts klicken und **Skizze editieren** im Kontextmenü wählen).


</div>


<div class="mw-translate-fuzzy">

1.  Die zwei horizontalen Linien mit der Maus durch Draufklicken auswählen und dann auf die horizontale Bedingung <img alt="" src=images/Constraint_Horizontal.svg  style="width   *32px;"> klicken.
2.  Die vertikale Linie auf der rechten Seite wählen und dann auf die vertikale Einschränkung <img alt="" src=images/Constraint_Vertical.svg  style="width   *32px;"> klicken.
3.  Die Anfangs- und Endpunkte der Polylinie wählen und auf die *Punkt auf Punkt Koinzidenz* Bedingung <img alt="" src=images/Constraint_PointOnPoint.svg  style="width   *32px;"> klicken, um die Polylinie zu schließen.
4.  Wählen Sie die untere horizontale Linie und die rechte vertikale Linie aus und wenden Sie an und ![ 32px](images/_Constraint_EqualLength.png ) Gleichheits-Beschränkung.
5.  Entweder die horizontale oder die vertikale Linie wählen und dann entweder einen entsprechenden horizontalen <img alt="" src=images/Constraint_HorizontalDistance.svg  style="width   *32px;"> oder vertikalen <img alt="" src=images/Constraint_VerticalDistance.svg  style="width   *32px;"> Abstand mit einem Wert von 26 mm eingeben.
6.  Die obere horizontale Linie auswählen und die horizontale Abstandsbeschränkung mit einem Wert von 5 mm eingeben.
7.  Den unteren rechten Endpunkt (Vertex) der horizontalen Linie und dann den Mittelpunkt des Rasters wählen und die *Punkt auf Punkt Koinzidenz* <img alt="" src=images/Constraint_PointOnPoint.svg  style="width   *32px;"> Beschränkung anwenden, um Ihre Form zu fixieren.


</div>

An diesem Punkt sollten Sie eine vollständig eingeschränkte Skizze haben, wie durch die Farbe und die in der Combo-Ansicht angezeigte Nachricht angezeigt. Es sollte jetzt genau wie das Bild unten aussehen.

![](images/Tut17_profile.png )


<div class="mw-translate-fuzzy">

Nun in der Combo-Ansicht auf die Schaltfläche **Schließen** klicken, um den Skizzenbearbeitungsmodus zu verlassen und Skizze aufpolstern <img alt="" src=images/PartDesign_Pad.svg  style="width   *32px;"> (Pad) aus der Symbolleiste im PartDesign-Menü wählen. Das öffnet ein **Aufpolstern**-Menü in der Combo-Ansicht. Leider sind derzeit 2 Begriffe dafür in der Programmübersetzung Aufpolstern = Block = PAD. In diesem Dialogfeld zuerst das Aufklappmenü **Typ** und dann **Zwei Dimensionen** wählen. Die Zeichnung am Anfang dieses Tutorials sagt aus, dass das Teil 53 mm lang ist. Wir erhalten diesen Abstand, indem wir unsere Skizze in beide Richtungen von der Mittelebene aus auffüllen, d.h. es wird symmetrisch bezüglich der Skizzierebene aufgepolstert. Der Grund dafür wird später beim Erstellen von Features klar werden. Zunächst soll das Teil insgesamt 53 mm lang sein, also 26,5 für die erste Längenhälfte und 26,5 für die zweite Längenhälfte eingeben. Alternativ könnte die volle Länge von 53 mm eingegeben und dann auf das Kontrollkästchen **Symmetrisch zu Ebene** geklickt werden. Sobald das erledigt ist, haben wir nun unsere Basis, auf der wir zusätzliche Features hinzufügen werden, um unser Teil zu konstruieren.


</div>

Ein Video der Schritte in diesem Teil des Tutorials ist hier   * <https   *//youtu.be/cUyPnCMeTgg>

### Features with pocket and external geometry 


<div class="mw-translate-fuzzy">

### Formelement *Tasche* und externe Geometrie 

Mit der Maus oder den Ansichtssymbolen drehen Sie das Modell um, so dass Sie seine Rückseite sehen können. Sobald die Rückseite des Teils sichtbar ist, wählen Sie die Rückseite aus, indem Sie darauf klicken, wie im nächsten Bild zu sehen ist.


</div>

![](images/PD_WB_Tutorial003.png )


<div class="mw-translate-fuzzy">

Nachdem die Oberfläche ausgewählt wurde, auf das Symbol **Neue Skizze** in der PartDesign-Menüleiste klicken. Dies wird unsere nächste Skizze auf die Rückseite des Teils positionieren. Nun das Werkzeug ![ 32px](images/Sketcher_CreateRectangle.svg ) **Rechteck** wählen und ein Rechteck auf die Rückseite des Teils auf ähnliche Weise positionieren, wie unten gezeigt. Nun den aufgeführten Schritten folgen und die Skizze einschränken.


</div>


<div class="mw-translate-fuzzy">

1.  Eine der horizontalen Linien auswählen und eine horizontale Abstandseinschränkung mit einem Wert von 5 mm angeben.
2.  Eine der vertikalen Linien wählen und eine vertikale Abstandseinschränkung mit einem Wert von 11 mm angeben.
3.  Das Werkzeug <img alt="" src=images/Sketcher_External.svg  style="width   *32px;"> externe Geometrie wählen.
4.  Den oberen rechten Eckpunkt der Oberfläche anklicken, um einen Punkt aus der externen Geometrie zu erhalten, mit welchem unsere Skizze verknüpft werden soll.


</div>

![](images/tut17_slot_unconstrained.png )

1.  Rechtsklicken Sie zur Beendigung des Externe-Geometrie-Modus
2.  Wählen Sie den gerade mit dem **Externe Geometrie**-Werkzeug erstellten Projektionspunkt und wählen zudem den oberen rechten Eckpunkt des in der Skizze vorhandenen Rechtecks. Durch einen nun folgenden Klick auf **Koinzidenz** <img alt="" src=images/Constraint_PointOnPoint.svg  style="width   *32px;"> sollte die Skizze komplett festgelegt sein und wie das nächste Bild aussehen.

![](images/tut17_slote_constrained.png )


<div class="mw-translate-fuzzy">

Danach auf die Schaltfläche **Schließen** oben in der Registerkarte **Aufgaben** in der Combo-Ansicht klicken und dann **Vertiefung** <img alt="" src=images/PartDesign_Pocket.svg  style="width   *32px;"> aus dem PartDesign-Menü wählen. Leider sind derzeit 2 Begriffe dafür in der Programmübersetzung    * Tasche = Vertiefung = POCKET. Das Werkzeug **Tasche** ist das Gegenteil des **Aufpolstern** (Pad)-Werkzeugs. Während das **Aufpolstern**-Werkzeug dem Teil Material hinzufügt, entfernt das **Vertiefen**-Werkzeug Material aus dem Teil. Beide Operationen werden als Features bezeichnet. In diesem Vertiefen-Vorgang wird aus dem Aufklappmenü **Typ** der Punkt **Durch alle** ausgewählt und dann auf die Schaltfläche OK geklickt.


</div>


<div class="mw-translate-fuzzy">

Für den nächsten Schritt muß \"Pocket\" im Modell Tab der Combo-Ansicht ausgewählt sein. Nun auf **gespiegeltes Objekt erzeugen** ![ 32px](images/_PartDesign_Mirrored.svg ) oder **Spiegeln** im PartDesign-Menü klicken. Im Dialogfeld **Mirrored Parameters** in der Combo-Ansicht die Option **Horizontale Skizzenachse** aus dem Aufklappmenü **Ebene** wählen. Auf OK klicken. Die Mirror-Funktion funktioniert deshalb auf diese Weise, weil das Basis-Feature unseres Modells in beiden Richtungen von der horizontalen Ebene aus, in der ersten Operation mit der Basisskizze aufgepolstert wurde. Wenn alles gut gegangen ist, sollten Sie jetzt ein Teil haben, welches dem Bild unten entspricht, nachdem Sie es in die Vorderansicht gedreht haben.


</div>

![](images/tut17_profilewithslots.png )

Ein Video der Schritte in diesem Teil des Tutorials ist hier   * <https   *//youtu.be/wiGXV9G7mrM>

### Features with pad and external geometry 


<div class="mw-translate-fuzzy">

### Features mit Pad und externer Geometrie 

Sehen Sie sich das Bauteil aus allen Richtungen einmal an und wählen Sie wieder die Rückseite des Teils aus, um die nächste Skizze zuzuordnen.


</div>

![](images/tut17_profilewithslotsrearplane.png )

Wählen Sie **Neue Skizze** und erstellen Sie ein neues Rechteck in dieser, ähnlich wie im folgenden Bild gezeigt. Fahren Sie dann fort, diesem Rechteck dimensionale Einschränkungen hinzuzufügen.

1.  Wählen Sie eine horizontale Linie und wenden Sie eine horizontale Abstandseinschränkung mit einem Wert von 16.7 an.
2.  Wählen Sie eine vertikale Linie aus und wenden Sie eine vertikale Abstandseinschränkung von 7 mm an.
3.  Wählen Sie mit dem Werkzeug Externe Geometrie den oberen linken Eckpunkt der Bauteilfläche aus.

![](images/tut17_sidblockunconstrained.png )

Durch Auswahl der gerade projizierten Ecke und der oberen linken Ecke des Rechtecks werden mit Hilfe der *Koinzidenzeinschränkung* die noch vorhandenen Freiheitsgrade beseitigt und die Skizze vollständig festgelegt.

![](images/tut17_sideblockconstraind.png )

Schließen Sie den Sketcher.

Als nächstes beenden wird diese Skizze und klicken auf *Block* . Im Block-Dialog der Combo-Ansicht wollen wir eine Länge von 26 mm eintragen, wobei wir den Typ als Dimension belassen und dann das Kontrollkästchen *Reversed* markieren. Wenn Sie das Kontrollkästchen *Umgekehrt* verwenden, wird der Block in das Teil und nicht in das Teil verschoben. Diese Operation liefert das folgende Ergebnis.

![](images/tut17_sideblock.png )

Die Mirror-Funktion erneut anwenden, um den zweiten Block zu erhalten. Der erstellte Block muß in der Baumansicht ausgewählt sein. Dann in der Symbolleiste auf **erzeuge gespiegeltes Objekt** oder **Spiegeln** aus dem PartDesign Menü klicken. Wir werden die oben für **Tasche** (pocket) durchgeführte Operation wiederholen und im Aufklappmenü **Ebene** die Option **Horizontale Skizzenachse** auswählen.

![](images/tut17_profilewithsideblocks.png )

Ein Video der Schritte in diesem Teil des Tutorials ist hier   * <https   *//youtu.be/Ido1owp8ubc>

### Feature with pocket and external geometry 


<div class="mw-translate-fuzzy">

### Feature mit Taschen- und Außengeometrie 

An diesem Punkt drehen wir das Teil in der Ansicht nach vorne, wir können sehen, dass unser Teil nun wie das Teil in der bemaßten Zeichnung am Anfang dieses Tutorials aussieht. Sobald Sie die Ansicht der Vorderseite haben, klicken Sie mit der Maus auf die geneigte Oberfläche, um diese auszuwählen, da wir diese für die nächste Skizze verwenden werden.


</div>

![](images/tut17_innerplane.png )


<div class="mw-translate-fuzzy">

Hier werden wir wieder das Rechteck-Werkzeug verwenden und ein Rechteck in unsere Skizze einfügen, und nachdem Sie dies getan haben, wenden Sie die folgenden Bedingungen an.


</div>


<div class="mw-translate-fuzzy">

1.  Wählen Sie eine horizontale Linie und eine vertikale Linie, und klicken Sie nach der Auswahl beider auf die Bedingung **Gleich**.
2.  Wählen Sie entweder eine horizontale oder vertikale Linie und wenden Sie eine entsprechende horizontale oder vertikale Abstandseinschränkung mit einem Wert von 17 mm an.
3.  Wählen Sie mit dem Werkzeug Externe Geometrie den oberen rechten Eckpunkt aus, wie in der Abbildung unten gezeigt.


</div>

![](images/tut17_rechtangleholeunconstrained.png )

Gemäß den Maßen der nachfolgenden Abbildungen sollen folgende Beschränkungen erstellt werden.

1.  Zwischen dem projizierten Eckpunkt und dem oberen, rechten Eckpunkt des Rechtecks eine horizontale Distanz von 7 mm.
2.  Zwischen dem projizierten Eckpunkt und dem oberen, rechten Eckpunkt des Rechtecks eine vertikale Distanz von 11 mm.

Das Ergebnis sollte folgendermaßen aussehen.

![](images/tut17_rectangleholeconstrained.png )

Würde man an dieser Stelle diese Skizze einfach zu einer Tasche ausformen, wäre das resultierende Loch senkrecht zu der geneigten Fläche, welcher es zugeordnet ist, und das ist nicht, was wir wollen.

![](images/tut17_wrongplaneforpocket.png )

Wir möchten, dass das Loch senkrecht zur Rückseite steht, aber die projizierten Abmessungen des Hohlraums von der Rückseite gesehen, sind dann nicht die Abmessungen von 17 mm x 17 mm, welche in der Zeichnung angegeben sind. Man müßte erst die erforderlichen Berechnungen durchführen um die erforderlichen Abmessungen zu erhalten. Oder wir können die in FreeCAD bereitgestellten Tools verwenden, um diese Projektion für uns zu erstellen.

Ein Video der Schritte in diesem Teil des Tutorials ist hier   * <https   *//youtu.be/x4d5nZPWCLQ>


<div class="mw-translate-fuzzy">

Um eine Tasche zu erstellen, die das geneigte Rechteck als Auslass hat, zeichnen wir ein neues Rechteck auf der Rückseite, wobei wir die Projektion des geneigten Rechtecks als externe Referenz verwenden. Bewegen Sie das Bauteil herum, um die Rückseite des Teils zu sehen, und wählen Sie diese aus, um darauf die letzte Skizze zu erstellen.


</div>

![](images/tut17_profilewithsideblocksrearplane.png )


<div class="mw-translate-fuzzy">

Erneut **Neue Skizze** <img alt="" src=images/PartDesign_NewSketch.svg  style="width   *32px;"> aus der Werkzeugleiste im PartDesign-Menü wählen. Im Skizzenbearbeitungsmodus sehen wir nun das skizzierte Rechteck auf der Schräge nicht mehr. Um es auswählbar zu machen, wechseln wir die Combo-Ansicht zur Modell-Registerkarte und wählen die letzte Skizze (Sketch003) auf der geneigten Ebene. Die Leertaste drücken, um diese sichtbar zu machen. Als nächstes die Spiegelfunktion oben (Mirrored001) wählen und wieder mit der Leertaste diese verstecken. Danach sollte das Rechteck in der 3D-Ansicht zu sehen sein. Man kann weiterhin mit der sichtbaren Registerkarte **Modell** arbeiten oder zur Registerkarte **Aufgaben** zurückkehren. Mit dem Werkzeug <img alt="" src=images/_Sketcher_External.svg  style="width   *32px;"> **Externe Geometrie** die oberen und unteren horizontalen Kanten des geneigten Rechtecks aus. Dann mit dem Werkzeug <img alt="" src=images/Sketcher_CreateRectangle.svg  style="width   *32px;"> **Rechteck** ein neues Rechteck der Skizze hinzufügen.


</div>

![](images/tut17_rectangleunconstrained.png )

1.  Den oberen linken Eckpunkt des Rechtecks und den oberen linken Punkt der externen Geometrie wählen und auf die Koinzidenzbedingung klicken.
2.  Den unteren rechten Eckpunkt des neuen Rechtecks und den unteren rechten Punkt der externen Geometrie wählen und auf die Koinzidenzbedingung klicken.

Und das sollte am Ende dabei herauskommen.

![](images/tut17_rectangleconstrained.png )


<div class="mw-translate-fuzzy">

Für den letzten Schritt in diesem Tutorium schließe das Skizziererfenster mit Schließen oder Bearbeitung beenden aus dem Kontextmenü von sketch004 und wähle dann das <img alt="" src=images/PartDesign_Pocket.svg  style="width   *32px;"> Taschen Funktion aus der Werkzeugleiste oder aus dem Menü \"Part Design\" aus. Wähle aus dem Auswahlmenü Typ die Option **Durch alles** und klicke auf die Schaltfläche OK.


</div>

![](images/Tut17_final.png )

An dieser Stelle wirst du einige Linien sehen, die von sich schneidenden Fprmelementen stammen. In diesem Fall überschneidet sich der \"Seitenblock\" mit dem \"Basisprofil\", was ihn als dreieckigen Block über dem Profil erscheinen lässt (d.h. im obigen Bild ist eine zusätzliche Linie auf der rechten Seite des Modells sichtbar). Um diese Linien zu entfernen, kannst du entweder \"Form verfeinern\" in deinen Part Design Einstellungen für die Teilekonstruktion einschalten, oder, um etwas Verarbeitungsgeschwindigkeit zu sparen und trotzdem diese Linien beim Konstruieren zu haben, schalte es bei jedem Formelement einzeln ein. Die Einstellung auf Formelement Ebene kann im \"Daten\" Reiter des Formelements vorgenommen werden. Setze die [\'**\'refine**\' Eigenschaft](Property_editor/de#Daten.md) auf TRUE für das Taschen Formelement Pocket001 , um das Verfeinern aufzurufen.

![](images/Tut17_refine.png ) ![](images/Tut17_final_refined.png )

Ein Video zu diesen Schritten des Tutoriums sind hier   * <https   *//youtu.be/UYI0gvxCYeI>

Dieses Tutorium und dein Modell sind vollständig.

## Zusätzliche Quellen 

-   FreeCAD Datei zum Vergleich (mit 0.17 erstellt) [Herunterladen](https   *//github.com/FreeCAD/Examples/blob/master/Basic_Part_Design_Tutorial_Example_017_Files/Basic_Part_Design_Tutorial_017.fcstd)


{{PartDesign Tools navi

}} {{Sketcher Tools navi}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [PartDesign](Category_PartDesign.md) > [Sketcher](Category_Sketcher.md) > Basic Part Design Tutorial/de
