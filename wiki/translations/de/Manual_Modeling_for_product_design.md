# Manual:Modeling for product design/de
{{Manual:TOC}}

Der Arbeitsbereich [PartDesign](PartDesign_Workbench/de.md) in FreeCAD ist ein vielseitiges Werkzeug zum Erstellen parametrischer 3D-Modelle, besonders nützlich für Festkörperkonstruktionen. Er ermöglicht, mit 2D-Skizzen zu beginnen, die dann zu 3D-Objektenwerden, wenn man Werkzeuge zum Erstellen von <img alt="" src=images/PartDesign_Pad.svg  style="width:16px;"> [Blöcken](PartDesign_Pad/de.md), <img alt="" src=images/PartDesign_Revolution.svg  style="width:16px;"> [Drehkörpern](PartDesign_Revolution/de.md), und <img alt="" src=images/PartDesign_Pocket.svg  style="width:16px;"> [Vertiefungen](PartDesign_Pocket/de.md) einsetzt. Dieser Arbeitsbereich ist unverzichtbar für die Konstruktion von Bauteilen, die eine hohe Genauigkeit und eine parametrische Steuerung erfordern, da beim Ändern einer Skizze oder eines Formelements automatisch das ganze Modell aktualisiert wird.

Einer der Hauptvorteile des Arbeitsbereichs PartDesign ist seine Eignung zur Erstellung von Bauteilen für den 3D-Druck. Da 3D-Drucker wasserdichte Festkörpermodelle erfordern, sorgt der Arbeitsbereich PartDesign dafür, dass alle Formelemente in einem einzelnen zusammenhängenden Körper verbleiben. Dies verhindert üblicherweise Probleme wie Lücken oder überlappende Flächen, die während der Aufbereitung für den 3D-Druck (slicing) zu Problemen führen können. Ist die Konstruktion ersteinmal komplett, kann sie als STL-Datei gespeichert werden. (STL, ein Dateiformat, das die meisten 3D-Drucker unterstützen) Dies macht den Arbeitsbereich PartDesign zur ersten Wahl für die Erstellung qualitativ hochwertiger druckbarer Objekte, ob Prototypen, funktionierende Bauteile oder aufwändige Modelle für den 3D-Druck.

Um zu darzustellen, wie der Arbeitsbereich PartDesign funktioniert, lasst uns diesen wohlbekannten [Lego](https://de.wikipedia.org/wiki/Lego)-Baustein erstellen. Unter [Grundlegende PartDesign-Anleitung 0.19](Basic_Part_Design_Tutorial_019/de.md) findet sich ein weiteres Bespiel, wenn man ein anderes Objekt ausprobieren möchte.

![](images/FreeCAD_Exercise1_RedBrick.png )

Wir werden jetzt ausschließlich die Werkzeuge der Arbeitsbereiche [Sketcher](Sketcher_Workbench/de.md) und [PartDesign](PartDesign_Workbench/de.md) verwenden. Da auch alle Werkzeuge des Arbeitsbereichs Sketcher im Arbeitsbereich PartDesign enthalten sind, können wir in PartDesign bleiben und müssen nicht zwischen den beiden hin und her wechseln.

In FreeCADs Arbeitsereich PartDesign werden Objekte hauptsächlich auf Skizzen aufgebaut, die aus Linienabschnitten bestehen wie (gerade) Linien, Kreisbögen oder Ellipsen sowie einer Reihe von Randbedingungen. Diese Randbedingungen legen bestimmte geometrische Regeln für die Skizze fest und können sowohl auf die Linienabschnitte selbst als auch auf bestimmenden Punkte wie Endpunkte oder Mittelpunkte angewendet werden. Zum Beispiel hält die Randbedingung Vertikal festlegen, auf eine Linie angewandt, diese genau senkrecht fest oder die Randbedingung Sperren, auf einen Punkt angewandt, hält diesen auf seiner Position fest und verhindert, dass er verschoben werden kann.

Eine Skizze wird als vollständig bestimmt angesehen, wenn jeder Punkt durch eine geeignete Anzahl von Randbedingungen auf seiner Position gehalten wird, was bedeutet, dass sich kein Teil der Skizze mehr frei bewegen kann. Eine vollständige bestimmte Skizze ist optimal, da sie sicherstellt, dass ihre Ausführung sinnvoll festgelegt und stabil ist und im weiteren Konstruktionsprozess vorhersagbare Änderungen ermöglicht. Andererseits kann dies zu Konflikten in der Geometrie führen, wenn mehr Randbedingungen als nötig hinzugefügt werden (d.h. die Skizze überbestimmt ist). FreeCAD warnt den Anwender vor jeder überzähligen oder widersprüchlichen Randbedingung, da Überbestimmtheit in folgenden Konstruktionsschritten, wie Extrudieren oder Ausschneiden, zu Problemen führen kann.

Das Hinzufügen der richtigen Randbedingungen, ist der Schlüssel zum Erstellen eines stabilen, parametrischen Modells. Durch besonnenes Ausbalancieren der Randbedingungen können Skizzen einfach geändert oder eingestellt werden ohne die Geometrie zu zerstören. Diese Steuerung macht den Arbeitsbereich Part Design zu einem Leistungsfähigen Werkzeug für genaues, parametrisches Modellieren, besonders für Aufgaben wie 3D-Druck, bei dem das Unterhalten geometrischer Beziehungen entscheident ist, um genaue funktionierende Bauteile zu erstellen.

Skizzen haben einen Bearbeitungsmodus, in dem ihre Geometrie und Randbedingungen verändert werden können. Wenn die Bearbeitung abgeschlossen ist und der Bearbeitungsmodus verlassen wurde, verhalten sich Skizzen wie jedes andere FreeCAD-Objekt und können als Bausteine für alle Part-Design-Werkzeuge eingesetzt werden aber auch in anderen Arbeitsbereichen, wie [Part](Part_Workbench/de.md) oder [Arch](Arch_Workbench/de.md). Der Arbeitsbereich [Draft](Draft_Workbench/de.md) hat auch ein Werkzeug, das Draft-Objekte in Skizzen umwandelt und umgekehrt.

-   Zum Arbeitsbereich <img alt="" src=images/Workbench_PartDesign.svg  style="width:16px;"> [Part Design](PartDesign_Workbench/de.md) wechseln.
-   Die Schaltfläche <img alt="" src=images/PartDesign_NewSketch.svg  style="width:16px;"> [Skizze erstellen](PartDesign_NewSketch/de.md) drücken und die **XY**-Ebene auswählen, die die \"Bodenebene\" darstellt. Die Skizze wird erstellt und sofort in den Bearbeitungsmodus versetzt; die Ansicht wird so gedreht, dass man orthogonal auf die Skizze blickt.
-   Ein Rechteck zeichnen, indem die Schaltfläche <img alt="" src=images/Sketcher_CreateRectangle.svg  style="width:16px;"> [Rechteck erstellen](Sketcher_CreateRectangle/de.md) gedrückt wird und zwei Eckpunkte angeklickt werden. Die Beiden Punkte können an beliebiger Stelle gesetzt werden, da ihre korrekte Position im nächste Schritt festgelegt wird.
-   Wir stellen fest, dass einige Randbedingungen automatisch zu unserem Rechteck hinzugefügt wurden: Den horizontalen und vertikalen Abschnitten wurden die Randbedingungen Horizontal festlegen bzw. Vertikal festlegen zugeordnet. Außerdem wurden in jeder Ecke die Eckpunkte mit der Randbedingung Koinzidenz festlegen zusammengeheftet. Wir können versuchen das Rechteck zu bewegen, indem seine Kanten mit der Maus gezogen werden. Dabei beachtet die gesamte Geometrie weiterhin die Randbedingungen.
-   Jetzt ist unsere Skizze unterbestimmt, da ihr noch vier Randbedingungen fehlen: jeweils eine für die Länge, die Breite sowie die X- und Y-Positionierung. Durch die fehlenden Randbedingungen kann die Skizze (das Rechteck) frei entlang den X- und Y-Achsen bewegt werden. Bis diese Randbedingungen festgelegt werden, ist die Geometrie nicht fest verankert, d.h. die Größe sowie die Lage der Skizze bleiben einstellbar. Um die Skizze vollständig zu bestimmen, müssen wir Randbedingungen hinzufügen, die die Werte festlegen und die Skizze verankern.

![](images/FreeCAD_Exercise1_re_UC.png )

-   Jetzt werden wir drei weitere Randbedingungen hinzufügen:
    -   Einen der vertikalen Abschnitte auswählen und die Schaltfläche <img alt="" src=images/Sketcher_Dimension.svg  style="width:16px;"> [Bemaßung](Sketcher_Dimension/de.md) drücken; im Dialog für die Länge 23.7mm eingeben.
    -   Einen der horizontalen Abschnitte auswählen und dieselbe Schaltfläche wie vorher drücken; im Dialog für die Länge 47.7mm eingeben.
    -   Schließlich den oberen linken Eckpunkt des Rechtecks auswählen, danach den Ursprungspunkt (der Punkt an der Stelle, wo sich die rote und die grüne Achse schneiden) und den unteren rechten Eckpunkt. Die Schaltfläche <img alt="" src=images/Sketcher_ConstrainSymmetric.svg  style="width:16px;"> [Symmetrisch festlegen](Sketcher_ConstrainSymmetric/de.md) drücken, um das Rechteck symmetrisch zu den X- und Y-Achsen auszurichten. Dies stellt sicher, dass das Rechteck auf dem Ursprungspunkt zentriert bleibt, reduziert seinen Bewegungsbereich und erhält die Symmetrie über beide Achsen.
-   Wir stellen fest, dass das Rechteck jetzt grün eingefärbt ist, was anzeigt, dass es vollständig bestimmt ist. Das heißt, dass jetzt jeder Teil der Skizze, einschließlich ihrer Position, Größe und Form komplett festgelegt und verankert ist. Es ist generell eine gute Vorgehensweise Skizzen vollständig zu bestimmen, da dies dabei hilft, die Kontrolle über die Konstruktion zu behalten und ungewollte Änderungen während folgender Arbeitsschritte zu vermeiden.

![](images/FreeCAD_Exercise1_re.png )

-   Unsere Skizze ist nun bereit und wir können den Bearbeitungsmodus durch Drücken der Schaltfläche **Schließen** oben im Aufgaben-Fenster oder einfach durch Drücken der **Esc**-Taste verlassen. Wenn es später nötig ist, dann können wir jederzeit in der Baumansicht mit einem Doppelklick auf die Skizze oder mit einem Rechtsklick und Auswahl der Menüoption Skizze bearbeiten im Kontextmenü wieder in den Bearbeitungsmodus wechseln.
-   Lasst uns das Teil mit dem Werkzeug <img alt="" src=images/PartDesign_Pad.svg  style="width:16px;"> [Block](PartDesign_Pad/de.md) extrudieren und dabei einen Abstand von 14,4 mm angeben. Die anderen Optionen bleiben bei ihren Vorgabewerten:

![](images/FreeCAD_Exercise1_padding.png )

-   Das Werkzeug **Pad** ist dem Werkzeug <img alt="" src=images/Part_Extrude.svg  style="width:16px;"> [Part Extrude](Part_Extrude/de.md) des Arbeitsbereichs <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Part](Part_Workbench/de.md) ähnlich, aber mit einem einscheidenden Unterschied: Ein Block ist immer mit seiner Skizze verknüpft und kann nicht unabhängig davon bewegt werden. Um einen Block zu versetzen, muss die Skizze, auf der er basiert, versetzt werden; das stellt sicher, dass Der Block sicher befestigt bleibt. Das Pad wird immer Bestandteil desselben Körpers sein und gewährleistet eine durchgängige Konstruktion; dies ist besonders nützlich für komplizierte Bauteile, für die Formelemente schrittweise aufeinander aufgebaut und ausgerichtet werden müssen. Dies stabilisiert eine Konstruktion, besonders wenn man sicherstellen möchte, dass alles korrekt ausgerichtet und verankert bleibt.

-   Lasst uns acht Zylinder auf der Deckfläche der Bausteins erstellen. Zuerst die die Deckfläche des Bausteins auswählen, dann die Option <img alt="" src=images/Std_AlignToSelection.svg  style="width:16px;"> [Auf die Auswahl ausrichten](Std_AlignToSelection/de.md) anklicken, um die Ansicht auf diese Fläche auszurichten. Dies stellt eine deutliche und direkte Ansicht bereit, die das Positionieren der Zylinder vereinfacht.
-   Die Schaltfläche <img alt="" src=images/PartDesign_NewSketch.svg  style="width:16px;"> [New Sketch](PartDesign_NewSketch/de.md) anklicken. die neue Skizze wird direkt auf der Deckfläche erstellt.
-   Zwei <img alt="" src=images/Sketcher_Circle.svg  style="width:16px;"> [Kreise](Sketcher_CreateCircle/de.md) an beliebiger Stelle erstellen.
-   Beide Kreismittelpunkte und die X-Achse (rote Linie) auswählen. Dann die Schaltfläche <img alt="" src=images/Sketcher_ConstrainSymmetric.svg  style="width:16px;"> [Symmetrisch festlegen](Sketcher_ConstrainSymmetric/de.md) anklicken.
-   Beide Kreismittelpunkte auswählen und die Schaltfläche <img alt="" src=images/Sketcher_ConstrainEqual.svg  style="width:16px;"> [Gleichheit festlegen](Sketcher_ConstrainEqual/de.md) anklicken.
-   Mit dem Werkzeug <img alt="" src=images/Sketcher_Dimension.svg  style="width:16px;"> [Bemaßung](Sketcher_Dimension/de.md) den Durchmesser eines Kreises auf 7.2 mm festlegen. Da wir schon für beide Kreise die Gleichheit der Durchmesser festgelegt haben, muss der Durchmesser des zweiten Kreises nicht eingegeben werden; er wird automatisch an den ersten angepasst.
-   Jetzt müssen die Kreise relativ zu den Kanten der Fläche positioniert werden. Wir können aber keine Punkte auf der Kante direkt auswählen, sondern müssen das Werkzeug <img alt="" src=images/Sketcher_External.svg  style="width:16px;"> [Externe Geometrie](Sketcher_External/de.md) einsetzen, um auf die Flächenkanten zu referenzieren; dies ermöglicht uns, die Kreise präzise im Bezug auf die Fläche festzulegen. Die Schaltfläche drücken und die linke Kante der Fläche auswählen. Diese Kante wird jetzt rot hervorgehoben und es können Referenzpunkte von ihr erstellt werden; dies ermöglicht, die Kreise präzise zu den Flächenrändern auszurichten.
-   Jetzt können X- und Y-Abstände des einen Mittelpunktes auf 6 mm festgelegt werden. Da die Lage beide Kreise zueinander festgelegt sind, wird der zweite entsprechend ausgerichtet.

![](images/FreeCAD_Exercise1_TopFaceSketch.png )

-   Wir stellen wieder einmal fest, dass die Skizze vollständig bestimmt ist, wenn Lage und Abmessungen jedes Objekts der Skizze festgelegt sind. Dadurch sind wir wieder auf der sicheren Seite. Wir können die erste Skizze nun ändern, aber alles, was wir danach getan haben, wird konsistent bleiben.
-   Wir verlassen den Bearbeitungsmodus, selektieren diese neue Skizze und legen einen <img alt="" src=images/PartDesign_Pad.svg  style="width:16px;"> [Block](PartDesign_Pad/de.md) mit 2,7 mm an:

![](images/FreeCAD_Exercise1_topCylPad.png )

-   Da wir die Deckfläche des Basisblocks als Grundlage für diese neue Skizze verwendet haben, wird jeder Part Design-Vorgang korrekt oberhalb dieser Basisform aufbauen. Die zwei Kreise sind keine unabhängige Objekte; sie werden direkt von dem vorhandenen Block aus extrudiert. Dies ist der Hauptvorteil der Arbeit im Arbeitsbereich Part Design Workbench; solange sichergestellt ist, dass jeder Schritt auf dem vorherigen aufbaut, wird letztlich auch ein einzelner, zusammenhängender Festkörper erstellt.
-   Wir können jetzt unsere zwei Gnubbel viermal duplizieren. Dazu den zuletzt erstellten Block auswählen.
-   Die Schaltfläche <img alt="" src=images/PartDesign_LinearPattern.svg  style="width:16px;"> [Lineares Muster](PartDesign_LinearPattern/de.md) drücken.
-   Eine Länge von 36 mm (dies ist die \"Spannweite\", über die wir die Kopien gleichmäßig verteilen wollen) für die Richtung \"Horizontale Skizzenachse\" eingeben, und 4 Vorkommen einstellen:

![](images/FreeCAD_Exercise1_topPattern.png )

-   Wir werden jetzt den Baustein mit dem Werkzeug <img alt="" src=images/PartDesign_Pocket.svg  style="width:16px;"> [Vertiefung](PartDesign_Pocket/de.md) aushöhlen. Dies ist die PartDesign-Version von [Part Differenz](Part_Cut/de.md). Zum Erstellen einer Vertiefung, legen wir eine Skizze auf der Bodenfläche unseres Bausteins an.
-   Die Bodenfläche auswählen und die Schaltfläche <img alt="" src=images/PartDesign_NewSketch.svg  style="width:16px;"> [Skizze erstellen](PartDesign_NewSketch/de.md) drücken.
-   Ein <img alt="" src=images/Sketcher_CreateRectangle.svg  style="width:16px;"> [Rechteck](Sketcher_CreateRectangle/de.md) auf der Fläche zeichnen.
-   Eine Randbedingung <img alt="" src=images/Sketcher_ConstrainSymmetric.svg  style="width:16px;"> [Symmetrisch festlegen](Sketcher_ConstrainSymmetric/de.md) hinzufügen; dafür den linken oberen Eckpunkt des Rechtecks auswählen, dann den Skizzenursprung (der Punkt an dem sich die rote und die grüne Achse schneiden) und den rechten unteren Eckpunkt.
-   \[Image:Sketcher_External.svg\|16px\]\] [Externe Geometrie](Sketcher_External/de.md) auswälen und die linke Kante der Bodenfläche anklicken. Die Linie wird rot hervorgehoben.
-   Den horizontalen und vertikalen Abstand des Rechtecks zum rechten oberen Punkt mit dem Werkzeug <img alt="" src=images/Sketcher_Dimension.svg  style="width:16px;"> [Bemaßung](Sketcher_Dimension/de.md) auf 1,8 festlegen.

![](images/FreeCAD_Exercise1_BottomRec.png )

-   Drei <img alt="" src=images/Sketcher_Circle.svg  style="width:16px;"> [Kreise](Sketcher_CreateCircle/de.md) erstellen; dabei sicherstellen, dass sich ihre Mittelpunkte auf der X-Achse (rote Linie) befinden.
-   Alle drei Kreise auswählen und <img alt="" src=images/Sketcher_ConstrainEqual.svg  style="width:16px;"> [equa/delGleichheit festlegen](Sketcher_ConstrainEqual.md) anklicken.
-   Den Durchmesser auf 9,765 mm setzen.
-   Den Abstand des Mittelpunktes des linken Kreises zur Bodenkante des Rechtecks, das wir zuvor erstellt haben, auf 10,2 mm setzen.
-   Den Abstand zwischen dem linken und dem mittleren Kreis auf 12 mm setzen. Diesen Schritt wiederholen, um den Abstand zwischen dem mittleren und dem rechten Kreis auch auf 12 mm zu setzen.

![](images/FreeCAD_Exercise1_BottomOuterCirc.png )

-   Wir sind fast fertig.
-   Drei zusätzliche <img alt="" src=images/Sketcher_Circle.svg  style="width:16px;"> [Kreise](Sketcher_CreateCircle/de.md) erstellen; dabei sicherstellen, dass jeder neue Kreis konzentrisch zu einem der zuvor gezeichneten liegt. Alternativ können die Kreise an beliebiger Stelle angelegt werden und mit dem Werkzeug <img alt="" src=images/Sketcher_ConstrainCoincident.svg  style="width:16px;"> [Koinzident festlegen](Sketcher_ConstrainCoincident/de.md) ihre Mittelpunkte auf denen der vorhanden Kreise positionieren.
-   Alle drei Kreise auswählen und <img alt="" src=images/Sketcher_ConstrainEqual.svg  style="width:16px;"> [Gleichheit festlegen](Sketcher_ConstrainEqual/de.md) anklicken.
-   Den Durchmesser eines Kreises auf 7,2 mm setzen.
-   Jetzt können wir die Skizze verlassen.

![](images/FreeCAD_Exercise1_bottomSketchCom.png )

-   Die gesamte Skizze auswählen, das Werkzeug <img alt="" src=images/PartDesign_Pocket.svg  style="width:16px;"> [Vertiefung](PartDesign_Pocket/de.md) anklicken und die Länge auf 12 mm setzen.

![](images/FreeCAD_Exercise1_BottomPad.png )

-   Das war\'s. Unser Baustein ist fertig. Soll seine Farbe geändert werden, kann dies im Reiter **Ansicht** erledigt werden.

![](images/FreeCAD_Exercise1_redBrick2.png )

Wir können erkennen, dass unsere Modellhistorie in der Baumansicht ziemlich umfangreich geworden ist. Dies ist unglaublich wertvoll, weil es uns ermöglicht, jeden einzelnen Schritt des Konstruktionsprozesses jederzeit erneut aufzurufen und zu ändern. Zum Beispiel das Anpassen dieses Modells zum Erstellen eines Bausteins mit 2x2 Knöpfen anstatt 2x4, wäre ein Klacks; wir müssten lediglich ein paar Einstellungen für die Abmessungen und die Anzahl von Wiederholungen in den Anordnungen ändern, das reicht. Die gleiche Flexibilität ermöglicht uns größere Bausteine zu erstellen, die es im originalen Lego-System nicht gibt. Die parametrische Natur von FreeCAD macht es einfach, vorhandene Modelle zu verändern, man hat die volle Kontrolle eine Konstruktion nach Bedarf anzupassen oder zu erweitern.

Aber wir könnten auch die Historie loswerden wollen, zum Beispiel wenn wir eine Burg mit diesem Baustein modellieren wollen, und wir diese ganze Historie nicht 500 Mal in unserer Datei haben möchten.

Es gibt zwei einfache Wege, um die Historie loszuwerden, einer ist die Nutzung des Werkzeugs [Einfache Kopie erstellen](Part_SimpleCopy/de.md) aus dem Arbeitsbereich [Part](Part_Workbench/de.md), der eine Kopie unseres Teils erstellt, die nicht mehr von der Historie abhängt (die ganze Historie kann hinterher gelöscht werden), der andere Weg ist das Exportieren des Teils als STEP-Datei und das Zurückimportieren dieser Datei.

**Herunterladen**

-   Das durch diese Übung produzierte Modell: <https://github.com/yorikvanhavre/FreeCAD-manual/blob/master/files/lego.FCStd>

**Mehr lesen**

-   [Der Skizzierer](Sketcher_Workbench/de.md)
-   [Der Part Design Arbeitsbereich](PartDesign_Workbench/de.md)
-   [Der Assembly2 Arbeitsbereich](https://github.com/hamish2014/FreeCAD_assembly2)



---
⏵ [documentation index](../README.md) > [Tutorials](Category_Tutorials.md) > Manual:Modeling for product design/de
