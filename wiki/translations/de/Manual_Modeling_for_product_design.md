# Manual:Modeling for product design/de
{{Manual   *TOC/de}}

[Produktdesign](https   *//de.wikipedia.org/wiki/Produktdesign) ist ursprünglich ein kommerzieller Begriff, aber in der 3D-Welt bedeutet er oft, etwas zu modellieren mit der Idee, es per [3D-Druck](https   *//de.wikipedia.org/wiki/3D-Druck), oder allgemeiner, maschinell herzustellen, z.B. mit einem 3D-Drucker oder einer [CNC-Maschine](https   *//de.wikipedia.org/wiki/CNC-Maschine).

Wenn Sie Objekte in 3D drucken, ist es von entscheidender Bedeutung, dass Ihre Objekte **solide** sind. Da sie reale, solide Objekte werden, ist dies offensichtlich. Das verhindert natürlich nicht, dass sie innen hohl sein können. Sie müssen aber immer eine klare Vorstellung davon haben, welcher Punkt im Material ist, und welcher Punkt außerhalb, denn der 3D-Drucker oder die CNC-Maschine muss genau wissen, was mit Material zu füllen ist und was nicht. Aus diesem Grund ist die [PartDesign Workbench](PartDesign_Workbench.md) in FreeCAD das perfekte Werkzeug, um solche Teile zu erstellen, denn es wird sich immer darum kümmern, dass Ihre Objekte solide bleiben und erstellbar.

Um zu illustrieren, wie die PartDesign-Workbench funktioniert, lassen Sie uns dieses wohlbekannte [Lego](https   *//de.wikipedia.org/wiki/Lego)-Teil erstellen   *

![](images/Exercise_lego_01.jpg )

Cool bei Lego-Teilen ist, dass die Abmessungen einfach im Internet zu finden sind, zumindest für die Standardteile. Diese sind ziemlich einfach zu modellieren und mit einem 3D-Drucker auszudrucken, und mit ein wenig Geduld (3D-Druck erfordert oftmals viele Anpassungen und Fein-Tuning) können Sie Teile erstellen, die absolut kompatibel sind und sich perfekt in Original Lego-Blöcke einfügen. Im folgenden Beispiel werden wir ein Teil erstellen, das 1,5 Mal so gross ist wie das Original.

Wir werden jetzt ausschließlich die [Sketcher](Sketcher_Workbench.md)- und [Part Design](PartDesign_Workbench.md)-Werkzeuge benutzen. Weil auch alle Werkzeuge der Sketcher-Workbench in der PartDesign-Workbench enthalten sind, können wir in PartDesign bleiben und müssen nicht zwischen den beiden hin- und herwechseln.

PartDesign-Objekte basieren vollständig auf **Skizzen**. Eine Skizze ist ein 2D-Objekt, bestehend aus linearen Abschnitten (Linien, Kreisbögen oder Ellipsen) und Beschränkungen. Diese Beschränkungen können entweder auf lineare Abschnitte oder ihre Endpunkte oder Mittelpunkte angewandt werden, und zwingen die Geometrie, gewissen Regeln zu folgen. Sie können beispielsweise eine vertikale Beschränkung auf einen Linienabschnitt anwenden, damit dieser vertikal bleibt, oder eine Positions-(Blockierungs)-Beschränkung auf einen Endpunkt legen, damit verhindert wird, dass er sich bewegt. Wenn eine Skizze eine genaue Anzahl von Beschränkungen hat, die für jeden Punkt der Skizze verhindert, dass er sich bewegen kann, dann sprechen wir von einer vollständig eingeschränkten Skizze. Wenn es redundante Beschränkungen gibt, die entfernt werden können, ohne dass die Geometrie bewegt werden kann, dann wird dies überbeschränkt genannt. Dies sollte verhindert werden, und FreeCAD wird Sie informieren, wenn solch ein Fall eintritt.

Skizzen haben einen Editiermodus, in dem die Geometrie und Beschränkungen verändert werden können. Wenn Sie mit dem Editieren fertig sind und den Editiermodus verlassen, verhalten sich Skizzen wie jedes andere FreeCAD-Objekt, und können als Bausteine für alle PartDesign-Werkzeuge, aber auch in anderen Arbeitsbereichen, wie [Part](Part_Workbench/de.md) oder [Arch](Arch_Workbench/de.md) benutzt werden. Der [Draft Arbeitsbereich](Draft_Workbench/de.md) hat ebenfalls ein Werkzeug, das Draft-Objekte in Skizzen konvertiert, und umgekehrt.

-   Lasse uns mit der Modellierung eines kubischen Formteils beginnen, das die Grundlage für unseren Lego Stein wird. Später werden wir die Innenseiten schneiden und die acht Punkte auf der Oberseite hinzufügen. Starten wir also mit einer rechteckigen Skizze, die wir dann extrudieren   *
-   Wechsle zur [PartDesign Arbeitsbereich](PartDesign_Workbench/de.md)
-   Klicken Sie auf den <img alt="" src=images/Sketcher_NewSketch.svg  style="width   *16px;"> [Neue Skizze](Sketcher_NewSketch/de.md) utton. Ein Dialog wird erscheinen, der Sie nach der Skizzenorientierung fragt, wählen Sie die **XY** Ebene, die die Grundebene ist. Die Skizze wird angelegt, und es wird sofort in den Editiermodus geschaltet und die Ansicht wird rotiert, damit Sie orthogonal auf Ihre Skizze blicken.
-   Nun können wir ein Rechteck zeichnen, indem wir das <img alt="" src=images/Sketcher_CreateRectangle.svg  style="width   *16px;"> [Rechteck](Sketcher_CreateRectangle/de.md) Werkzeug auswählen und zwei (gegenüberliegende) Eckpunkte anklicken. Sie können die beiden Punkte irgendwo platzieren, denn die korrekte Position wird im nächsten Schritt festgelegt.
-   Sie werden feststellen, dass für unser Rechteck automatisch eine Reihe von Beschränkungen hinzugefügt wurde   * die vertikalen Abschnitte haben eine vertikale Beschränkung bekommen, die horizontalen eine horizontale Beschränkung und jede Ecke eine Koinzidenz Beschränkung, die die Abschnitte zusammenklebt. Wenn Sie versuchen, das Rechteck zu bewegen, indem Sie mit der Maus an den Linien ziehen, wird die Geometrie durch Einhaltung der Beschränkungen erhalten bleiben.

![](images/Exercise_lego_02.jpg )

-   Lasse uns nun drei weitere Beschränkungen hinzufügen   *
    -   Wähle einen der vertikalen Abschnitte und füge eine <img alt="" src=images/Constraint_VerticalDistance.svg  style="width   *16px;"> [Vertikale Abstandsbeschränkung](Sketcher_ConstrainDistanceY/de.md) hinzu. Gib als Länge 23,7 mm an.
    -   Wähle einen der horizontalen Abschnitte und füge eine <img alt="" src=images/Constraint_HorizontalDistance.svg  style="width   *16px;"> [Horizontale Abstandsbeschränkung](Sketcher_ConstrainDistanceX/de.md) hinzu. Der Wert ist 47,7 mm.
    -   Wähle schließlich einen der Eckpunkte, dann den Ursprung (das ist der Punkt am Schnittpunkt der roten und grünen Achsen), und füge dann eine <img alt="" src=images/Constraint_PointOnPoint.svg  style="width   *16px;"> [Deckungsgleich Beschränkung](Sketcher_ConstrainCoincident/de.md) hinzu. Das Rechteck springt dann zum Ursprung und Deine Skizze wird grün werden, was bedeutet, dass sie nun vollständig beschränkt ist.

Du kannst versuchen, die Linien oder Punkte zu bewegen, aber es wird sich nichts mehr bewegen.

![](images/Exercise_lego_03.jpg )

Beachten Sie, dass die letzte Koinzidenz-Beschränkung nicht absolut notwendig war. Sie sind nie gezwungen, mit vollständig eingeschränkten Skizzen zu arbeiten. Wenn wir diesen Stein in 3D ausdrucken wollen, ist es allerdings notwendig, unseren Stein nahe am Ursprung (dem Mittelpunkt der Fläche, in der sich der Druckkopf bewegen kann) zu platzieren. Durch Hinzufügen dieser Beschränkung stellen wir sicher, dass unser Teil immer mit diesem Ursprung \"verankert\" bleiben wird.

-   Unsere Skizze ist nun bereit, wir können den Editiermodus durch Drücken der **Schließen** Taste oben im Aufgabenbereich oder einfach durch Drücken der **Esc** Taste verlassen. Wenn es später nötig ist, dann können wir jederzeit durch Doppelklicken der Skizze in der Baumansicht wieder in den Editiermodus wechseln.
-   Lassen Sie uns das Teil mit dem <img alt="" src=images/PartDesign_Pad.svg  style="width   *16px;"> [Polster](PartDesign_Pad/de.md) Werkzeug extrudieren und einen Abstand von 14,4 mm angeben. Die anderen Optionen bleiben bei ihren Vorgabewerten   *

![](images/Exercise_lego_04.jpg )

Das **Polster** verhält sich sehr ähnlich wie das [Extrudieren](Part_Extrude/de.md) Werkzeug, das wir im vorigen Kapitel benutzt haben. Es gibt dennoch eine Reihe von Unterschieden, der wichtigste ist, dass ein Block nicht bewegt werden kann. Es ist für immer mit der Skizze verbunden. Wenn Sie die Position des Blocks ändern möchten, dann müssen Sie die zugrunde liegende Skizze ändern. Im aktuellen Kontext, wo wir sicher sein wollen, dass sich nichts aus seiner Position bewegt, ist dies eine zusätzliche Sicherheit.

-   Wir werden nun mit dem <img alt="" src=images/PartDesign_Pocket.svg  style="width   *16px;"> [Tasche](PartDesign_Pocket/de.md) Werkzeug, das die PartDesign Version von [Part Schneiden](Part_Cut/de.md) ist, das Innere des Blocks herausschneiden. Um eine Tasche zu erstellen, werden wir eine Skizze auf der Unterseite unseres Blocks anlegen, die benutzt wird, um einen Teil des Blocks zu entfernen.
-   Während die Unterseite selektiert ist, drücken Sie den <img alt="" src=images/Sketcher_NewSketch.svg  style="width   *16px;"> [Neue Skizze](Sketcher_NewSketch/de.md) Taste.
-   Zeichnen Sie ein Rechteck auf der Fläche.

![](images/Exercise_lego_05.jpg )

-   Wir werden nun das Rechteck in Relation zur Unterseite beschränken. Um dies zu tun, müssen wir einige Kanten der Fläche mit dem <img alt="" src=images/Sketcher_External.svg  style="width   *16px;"> [Externe Geometrie](Sketcher_External/de.md) Werkzeug \"importieren\". Wende dieses Werkzeug auf die beiden vertikalen Linien auf der Unterseite an   *

![](images/Exercise_lego_06.jpg )

Sie werden feststellen, dass lediglich Kanten der ursprünglichen Seite mit diesem Werkzeug hinzugefügt werden können. Wenn Sie eine Skizze mit einer selektierten Seite erstellen, wird eine Verbindung zwischen der Seite und der Skizze erstellt, was wichtig für weitere Operationen ist. Sie können später mit dem <img alt="" src=images/Sketcher_MapSketch.svg  style="width   *16px;"> [Skizze zuordnen](Sketcher_MapSketch/de.md) Werkzeug immer eine Skizze einer weiteren Fläche zuordnen.

-   Die externe Geometrie ist nicht \"real\", sie wird versteckt, wenn wir den Editiermodus verlassen. Wir können sie aber benutzen, um Beschränkungen anzulegen. Legen Sie die vier folgenden Beschränkungen an   *
    -   Selektieren Sie den oberen linken Punkt des Rechtecks und den oberen Punkt der importierten Linie und fügen Sie eine <img alt="" src=images/Constraint_HorizontalDistance.svg  style="width   *16px;"> [Horizontale Abstandsbeschränkung](Sketcher_ConstrainDistanceX/de.md) von 1,8 mm ein
    -   Select Sie erneut den oberen linken Punkt des Rechtecks und den oberen Punkt der importierten Linie und fügen Sie eine <img alt="" src=images/Constraint_VerticalDistance.svg  style="width   *16px;"> [Vertikal Abstandsbeschränkung](Sketcher_ConstrainDistanceY/de.md) von 1,8 mm ein
    -   Selektieren Sie den unteren rechten Punkt des Rechtecks und den unteren Punkt der rechten importierten Linie und fügen Sie eine <img alt="" src=images/Constraint_HorizontalDistance.svg  style="width   *16px;"> [Horizontale Abstandsbeschränkung](Sketcher_ConstrainDistanceX/de.md) von 1,8 mm ein
    -   Select Sie erneut den unteren rechten Punkt des Rechtecks und den unteren Punkt der rechten importierten Linie und fügen Sie eine <img alt="" src=images/Constraint_VerticalDistance.svg  style="width   *16px;"> [Vertikal Abstandsbeschränkung](Sketcher_ConstrainDistanceY/de.md) von 1,8 mm ein

![](images/Exercise_lego_07.jpg )

-   Verlassen Sie den Editiermodus und nun können wir die Taschen-Operation durchführen   * während die Skizze selektiert ist, drücken Sie den <img alt="" src=images/PartDesign_Pocket.svg  style="width   *16px;"> [Tasche](PartDesign_Pocket/de.md) Taste.

Geben Sie eine Länge von 12,6 mm an, was eine Dicke von 1,8 mm für die Oberfläche lässt (da die Gesamthöhe unseres Blocks 14,4 mm ist).

![](images/Exercise_lego_08.jpg )

-   Wir werden nun die acht Knöpfe auf der Oberseite erstellen. Da sie eine Wiederholung einer gleichen Eigenschaft sind, werden wir das praktische <img alt="" src=images/PartDesign_LinearPattern.svg  style="width   *16px;"> [Lineares Muster](PartDesign_LinearPattern/de.md)-Werkzeug benutzen, das es erlaubt, einmalig zu modellieren und die Form zu wiederholen.
-   Starten Sie durch Selektieren der Oberseite unseres Blocks.
-   Erstellen Sie eine <img alt="" src=images/Sketcher_NewSketch.svg  style="width   *16px;"> [Neue Skizze](Sketcher_NewSketch/de.md).
-   Erstellen Sie zwei <img alt="" src=images/Sketcher_Circle.svg  style="width   *16px;"> [Kreise](Sketcher_CreateCircle/de.md).
-   Selektieren Sie jeden Kreis, und fügen Sie jeweils eine <img alt="" src=images/Sketcher_ConstrainRadius.svg  style="width   *16px;"> [Radius Beschränkung](Sketcher_ConstrainRadius/de.md) von 3,6 mm hinzu.
-   Importieren Sie die linke Kante der ursprünglichen Fläche mit dem <img alt="" src=images/Sketcher_External.svg  style="width   *16px;"> [Externe Geometrie](Sketcher_External/de.md) Werkzeug.
-   Legen Sie zwei vertikale und zwei horizontale Beschränkungen von 6 mm zwischen den Mittelpunkten und den Eckpunkten der importierten Kante an, so dass jeder Kreismittelpunkt 6 mm von den Grenzen der Fläche entfernt ist   *

![](images/Exercise_lego_09.jpg )

-   Sie werden bemerken, dass die Skizze (wieder einmal) vollständig eingeschränkt wird, wenn Sie die Lage und Abmessungen jedes Objekts Ihrer Skizze festgelegt haben. Dadurch sind Sie wieder auf der sicheren Seite. Sie können die erste Skizze nun ändern, aber alles, was wir danach getan haben, wird konsistent bleiben.
-   Verlassen Sie den Editiermodus, selektieren Sie diese Skizze und legen Sie ein <img alt="" src=images/PartDesign_Pad.svg  style="width   *16px;"> [Polster](PartDesign_Pad/de.md) mit 2,7 mm an   *

![](images/Exercise_lego_10.jpg )

-   Sie werden bemerken, wie vorhin bei der Tasche, dass jede PartDesign-Operation in dieser Skizze korrekt auf dem ursprünglichen Formteil aufgebaut, denn wir haben die Oberfläche unseres ursprünglichen Blocks als Basis für diese letzte Skizze benutzt   *

Die beiden Knöpfe sind keine unabhängigen Objekte, sie wurden direkt aus unserem Baustein extrudiert. Dies ist der große Vorteil beim Arbeiten mit der PartDesign-Workbench, solange Sie darauf achten, dass ein Schritt auf dem anderen aufbaut, bauen Sie tatsächlich ein endgültig solides Objekt.

-   Wir können nun unsere zwei Knöpfe viermal duplizieren, so dass wir acht bekommen. Selektieren Sie das letzte Pad, das wir gerade erstellt haben.
-   Drücken Sie den <img alt="" src=images/PartDesign_LinearPattern.svg  style="width   *16px;"> [Lineares Muster](PartDesign_LinearPattern/de.md)-Button.
-   Geben Sie \"horizontale Skizzenachse\", als Länge 36 mm (das ist der gesamte \"Abstand\", in den unsere Kopien passen sollen) und vier Vorkommen an   *

![](images/Exercise_lego_11.jpg )

-   Erneut sollten Sie verstehen, dass dies nicht einfach eine Vervielfältigung eines Objekts ist, sondern eine \*Eigenschaft\* unseres Formteils, die dupliziert wurde, das endgültige Objekt ist weiterhin ein einziges solides Objekt.
-   Lassen Sie uns nun an den drei \"Röhren\" arbeiten, die die Leere füllen, die wir auf der Unterseite erzeugt haben. Wir haben verschiedene Möglichkeiten   *

Eine Skizze mit drei Kreisen anlegen, diese aufpolstern und anschließend mit Taschen versehen, oder eine zugrunde liegende Skizze mit zwei ineinander liegenden Kreisen anzulegen, die aufgepolstert werden und dadurch bereits die komplette Röhre bilden, oder sogar andere Kombinationen. Wie immer in FreeCAD gibt es viele Wege, um das gleiche Ergebnis zu erzielen. Manchmal wird ein Weg nicht so funktionieren, wie wir das wollen, so dass wir andere Wege versuchen müssen. Hier werden wir die sicherste Herangehensweise wählen und die Schritte langsam ausführen.

-   Selektieren Sie die Fläche, die auf Unterseite des hohlen Raums ist, den wir vorhin in den Block geschnitten haben.
-   Erstellen Sie eine neue Skizze, fügen Sie einen Kreis mit einem Radius von 4,8825 mm hinzu, importieren Sie die linke Grenze der Fläche und beschränken Sie sie vertikal und horizontal 10,2 mm von der oberen Ecke der Fläche   *

![](images/Exercise_lego_12.jpg )

Wenn du Schwierigkeiten bei der Auswahl von Formelementen hast, kann das Ausblenden eines Teils des Modells helfen. Um ein Formelement auszublenden, wähle es in der Baumansicht aus und drücke die Leertaste, um die Sichtbarkeit umzuschalten.

-   Verlassen Sie den Editiermodus und polstern Sie diese Skizze mit einem Abstand von 12,6 mm auf
-   Erstellen Sie ein lineares Muster dieses letzten Polsters, mit einer Länge von 24 mm und drei Vorkommen. Wir haben jetzt drei gefüllte Röhren, die den leeren Raum füllen   *

![](images/Exercise_lego_13.jpg )

-   Lassen Sie uns die abschließenden Löcher machen. Selektieren die Kreisoberfläche des ersten unserer drei \"Pins\"
-   Erstellen Sie eine neue Skizze, importieren Sie die Kreislinie unserer Fläche, erstellen Sie einen Kreis mit einer Radius-Beschränkung von 3,6 mm und fügen Sie eine <img alt="" src=images/Constraint_PointOnPoint.svg  style="width   *16px;"> [Deckungsgleich Beschränkung](Sketcher_ConstrainCoincident/de.md) zwischen den Kreismittelpunkten des importierten und unseres neuen Kreises. Wir haben nun einen perfekt zentrierten Kreis, und erneut vollständig eingeschränkt   *

![](images/Exercise_lego_14.jpg )

-   Verlassen Sie den Editiermodus und erstellen Sie eine Tasche mit dieser Skizze, mit einer Länge von 12,6 mm
-   Erstellen Sie ein lineares Muster dieser Tasche, mit einer Länge von 24 mm und drei Wiederholungen. Das ist der letzte Schritt, unser Lego-Teil ist nun fertig, so dass wir ihm eine schöne Farbe geben können, um unseren Sieg zu markieren!

![](images/Exercise_lego_15.jpg )

Sie werden feststellen, dass unsere Modellhistorie (die in der Baumansicht erscheint) ziemlich lang geworden ist. Dies ist wertvoll, weil jeder einzelne Schritt, den wir getan haben, später geändert werden kann. Das Anpassen dieses Modells für eine andere Sorte von Baustein, zum Beispiel einen mit 2x2 Knöpfen anstatt 2x4, wäre ein Klacks, wir müssten lediglich ein paar Abmessungen und die Anzahl von Wiederholungen in den linearen Anordnungen ändern. Genauso einfach könnten wir größere Bausteine erstellen, die es im Original-Lego-System nicht gibt.

Aber wir könnten auch die Historie loswerden wollen, zum Beispiel wenn wir eine Burg mit diesem Baustein modellieren wollen, und wir diese ganze Historie nicht 500 Mal in unserer Datei haben möchten.

Es gibt zwei einfache Wege, um die Historie loszuwerden, einer ist die Nutzung des [Erstelle einfache Kopie](Part_SimpleCopy/de.md)-Werkzeugs aus dem [Part Arbeitsbereich](Part_Workbench/de.md), der eine Kopie unseres Teils erstellt, die nicht mehr von der Historie abhängt (Sie können die ganze Historie später löschen), der andere Weg ist das Exportieren des Teils als STEP-Datei und Reimportieren dieser Datei.

**Zusammenbauen**

Aber das Beste aus beiden Welten existiert ebenfalls, das ist die [Assembly2 Workbench](https   *//github.com/hamish2014/FreeCAD_assembly2), eine Erweiterung, die aus dem [FreeCAD Erweiterungen](https   *//github.com/FreeCAD/FreeCAD-addons) Repositorium installiert werden kann. Dieser Arbeitsbereich wurde \"2\" benannt, weil außerdem ein offizielle eingebauter Zusammenbau Arbeitsbereich in der Entwicklung ist, die noch nicht fertig ist. Die Assembly2-Workbench jedoch arbeitet bereits sehr gut, um Baugruppen zu konstruieren, und bietet eine Reihe von Objekt-zu-Objekt Beschränkungen, die Sie benutzen können, um die Position in Relation zu einer anderen zu beschränken. Im folgenden Beispiel jedoch ist es schneller und einfacher, die Teile mithilfe von <img alt="" src=images/Draft_Move.svg  style="width   *16px;"> [Entwurf Versetzen](Draft_Move/de.md) und <img alt="" src=images/Draft_Rotate.svg  style="width   *16px;"> [Entwurf Drehen](Draft_Rotate/de.md) zu positionieren, als die Assembly2-Beschränkungen zu benutzen.

-   Speichern Sie den aktuellen Zustand
-   Installieren Sie die [Assembly2 Arbeitsbereich](https   *//github.com/hamish2014/FreeCAD_assembly2) und starten Sie FreeCAD neu
-   Erstellen Sie ein neues leeres Dokument
-   Wechseln Sie zur Assembly2-Workbench
-   Drücken Sie den **Import a part from another FreeCAD document** Taste
-   Wählen Sie die Datei, die wir gespeichert haben
-   Das endgültige Teil wird in das aktuelle Dokument importiert. Der Assembly2 Arbeitsbereich wird automatisch ermitteln, welches das endgültig zu benutzende Teil in unser Datei ist, und das neue Objekt bleibt mit der Datei verbunden. Wenn wir zurück gehen und den Inhalt der ersten Datei verändern, können wir den **Update parts imported into the assembly** Taste drücken, um die Teile hier zu aktualisieren.
-   Durch mehrfache Nutzung des **Import a part from another FreeCAD document** Taste, bewegen und rotieren der Teile (mit dem Entwurf Werkzeug oder durch manipulieren der Platzierungseigenschaften), können wir schnell eine kleine Baugruppe erstellen   *

![](images/Exercise_lego_16.jpg )

**Herunterladen**

-   Das durch diese Übung produzierte Modell   * <https   *//github.com/yorikvanhavre/FreeCAD-manual/blob/master/files/lego.FCStd>

**Mehr lesen**

-   [Der Skizzierer](Sketcher_Workbench/de.md)
-   [Der Part Design Arbeitsbereich](PartDesign_Workbench/de.md)
-   [Der Assembly2 Arbeitsbereich](https   *//github.com/hamish2014/FreeCAD_assembly2)




[Category   *Tutorials](Category_Tutorials.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Tutorials](Category_Tutorials.md) > Manual:Modeling for product design/de
