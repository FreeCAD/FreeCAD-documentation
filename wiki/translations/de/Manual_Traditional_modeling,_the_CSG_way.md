# Manual:Traditional modeling, the CSG way/de
{{Manual:TOC/de}}

CSG steht für [Konstruktive Festkörpergeometrie](https://de.wikipedia.org/wiki/Constructive_Solid_Geometry) (engl.: Constructive Solid Geometry) und beschreibt den grundlegendsten Weg, mit 3D Volumenkörpergeometrie zu arbeiten, nämlich die Erstellung komplexer Objekte durch Hinzufügen und Entfernen von Teilen zu/von Volumenkörpern mit Hilfe boolescher Operationen wie Vereinigung, Subtraktion oder Schnittmenge.

Wie wir bereits früher in diesem Handbuch gesehen haben, kann FreeCAD viele Arten von Geometrie handhaben, aber die bevorzugte und nützlichste Art für die Art von 3D Objekten, die wir mit FreeCAD entwerfen wollen, d.h. Objekte aus der realen Welt, ist zweifellos die Festkörpergeometrie [Boundary Representation BREP](https://de.wikipedia.org/wiki/Boundary_Representation), die hauptsächlich vom [Part Arbeitsbereich](Part_Workbench/de.md) gehandhabt wird. Im Gegensatz zu [Polygonnetze](https://en.wikipedia.org/wiki/Polygon_mesh), die nur aus Punkten und Dreiecken bestehen, sind die Flächen von BREP Objekten durch mathematische Kurven definiert, was eine absolute Präzision unabhängig vom Maßstab ermöglicht.

![](images/Mesh_vs_brep.jpg )

Der Unterschied zwischen den beiden kann mit dem Unterschied zwischen Bitmap und Vektorgrafiken verglichen werden. Wie bei Bitmap Grafiken sind gewölbte Oberflächen bei Polygonnetzen unterteilt in eine Reihe von Punkten. Wenn du genauer hinsiehst oder es sehr groß ausdruckst, wirst du keine gewölbte, sondern eine facettierte Oberfläche sehen. In Vektorgrafiken und BREP Daten ist die Position eines beliebigen Punktes auf einer Kurve nicht in der Geometrie gespeichert, sondern im Handumdrehen und mit exakter Präzision berechnet.

In FreeCAD werden alle BREP -basierten Geometrien von einem anderen Stück Open Source Software, [OpenCasCade](https://de.wikipedia.org/wiki/Open_CASCADE_Technology), gehandhabt. Die Hauptschnittstelle zwischen FreeCAD und dem OpenCasCade Kern ist der Part Arbeitsbereich. Die meisten anderen Arbeitsbereiche bauen ihre Funktionalität auf dem Part Arbeitsbereich auf.

Obwohl andere Arbeitsbereiche oft fortschrittlichere Werkzeuge zur Erstellung und Bearbeitung von Geometrie bieten, da sie alle tatsächlich Part Objekte bearbeiten, ist es sehr nützlich zu wissen, wie diese Objekte intern arbeiten, und die Part Werkzeuge nutzen zu können, da sie einfacher sind und Ihnen sehr oft helfen können, Probleme zu umgehen, die die intelligenteren Werkzeuge nicht richtig lösen können.

Um die Funktionsweise der Part Arbeitsbereichs zu veranschaulichen, werden wir diesen Tisch modellieren, wobei wir nur CSG Operationen verwenden (mit Ausnahme der Schrauben, für die wir eines der Erweiterungen verwenden werden, und der Abmessungen, wie wir im nächsten Kapitel sehen werden):

![](images/Exercise_table_complete.jpg )

Lass uns ein neues Dokument erstellen (**Strg+N** oder Menü Datei → Neues Dokument), das unsere Tischkonstruktion aufnimmt. Das Dokument heißt zunächst \"unnamed\" im Modellreiter im Combo Ansichtsfeld, aber wenn du das Dokument (**Strg+Umschalt+S**\' oder Menü Datei → Speichern unter) als neues FreeCAD Dokument mit dem Namen \"table.FCStd\" speicherst, wird das Dokument in \"table\" umbenannt, was das Projekt klarer identifiziert.

Jetzt können wir zum [Part Arbeitsbereich](Part_Workbench/de.md) wechseln und mit der Erstellung des ersten Tischbeins beginnen.

-   Drücke die <img alt="" src=images/Part_Box.svg  style="width:16px;"> **Würfel** Schaltfläche
-   Wähle den Würfel, dann setze die folgenden Eigenschaften (im **Daten** Reiter):
    -   Length: 80 mm (oder 8 cm, oder 0.8 m, FreeCAD arbeitet mit jeder Einheit)
    -   Width: 80 mm
    -   Height: 75 cm
-   Dupliziere den Quader durch Drücken von **Strg+C**, dann **Strg+V** (oder Menü Bearbeiten → Kopieren und Einfügen) (Es wird keine Veränderung erkennbar sein, da das zweite Objekt das erste überlagert).
-   Wähle das neu angelegte Objekt mit dem Namen Cube001 aus (Klicke auf Cube001 auf der linken Seite auf dem Modell Reiter)
-   Ändere die Position durch Anpassen der Positionierungseigenschaften:
    -   Position x: 8 mm
    -   Position y: 8 mm

Du solltest jetzt zwei hohe Quader erhalten, der eine 8 mm vom anderen entfernt:

![](images/Exercise_table_01.jpg )

-   Jetzt können wir den einen vom anderen subtrahieren: Wähle den **ersten**, das ist der, der **übrig** bleibt, dann mit gedrückter Strg Taste, wähle den **anderen**, der subtrahiert wird (die Reihenfolge ist wichtig) und drücke die <img alt="" src=images/Part_Cut.svg  style="width:16px;"> **Cut** Schaltfläche:

![](images/Exercise_table_02.jpg )

Beachte, dass das neu erzeugte Objekt, \"Cut\" benannt, noch die beiden Quader enthält, die wir als Operanden benutzt haben. Tatsächlich sind die beiden Quader weiterhin im Dokument, sie wurden einfach versteckt und in der Baumansicht unterhalb des Cut-Objekts angeordnet. Du kannst sie durch expandieren des Pfeils neben dem Cut-Objekt noch auswählen, und durch rechtsklicken wieder sichtbar machen oder jede beliebige Eigenschaft ändern.

Du kannst das Ausschneiden-Werkzeug und andere boolesche Werkzeuge auch über die \"Combo Ansicht\" mit <img alt="" src=images/Part_Booleans.svg  style="width:16px;"> [Boolesche Operationen](Part_Boolean/de.md) verwenden. Es ist eindeutiger, aber länger.

-   Jetzt werden wir die drei anderen Füße durch sechsmaliges duplizieren unseres Basisquaders estellen. Da er bereits kopiert wurde, kannst Du einfach sechs Mal einfügen (Strg-V) drücken. Ändere die Positionen wie folgt:
    -   cube002: x: 0, y: 80cm
    -   cube003: x: 8mm, y: 79.2cm
    -   cube004: x: 120cm, y: 0
    -   cube005: x: 119.2cm, y: 8mm
    -   cube006: x: 120cm, y: 80cm
    -   cube007: x: 119.2cm, y: 79.2cm

-   Jetzt werden wir die drei weiteren Schnitte durchführen, indem zuerst der \"host\" Quader, dann der abzuschneidende gewählt wird. Wir haben jetzt vier Schnitt Objekte:

![](images/Exercise_table_03.jpg )

Vielleicht denkst Du jetzt, dass wir den kompletten Fuß nur dreimal hätten kopieren müssen, anstatt den Basisquader sechsmal zu duplizieren. Das ist wahr, denn wie immer in FreeCAD gibt es viele Wege, um das gleiche Ziel zu erreichen. Es ist wertvoll, sich daran zu erinnern, denn wenn wir zu komplexeren Objekten fortschreiten, gibt es einige Operationen, die möglicherweise nicht das korrekte Ergebnis liefern, und dann müssen wir andere Wege probieren.

-   Wir werden jetzt mit der gleichen Schnitt Methode Löcher für die Schrauben machen. Nachdem wir acht Löcher brauchen, zwei in jedem Fuß, könnten wir acht zu entfernende Objekte erzeugen. Stattdessen werden wir andere Wege beschreiten und vier Röhren erstellen, die für die Löcher in den Füßen wiederverwendet werden. Daher werden wir vier Röhren mit dem <img alt="" src=images/Part_Cylinder.svg  style="width:16px;"> **Zylinder** Werkzeug erstellen. Du kannst wieder nur eine erstellen und später wieder duplizieren. Gib jedem Zylinder einen Radius von 6 mm. Dieses Mal müssen wir sie drehen, was ebenfalls mit der **Placement** Eigenschaft unter dem Daten Reiter gemacht wird *(**Anmerkung**: ändere die Axis Eigenschaft*vor*dem Setzen des Winkels oder die Drehung wird nicht durchgeführt)*:
    -   cylinder: height: 130cm, angle: 90°, axis: x:0,y:1,t:0 position: x:-10mm, y:40mm, z:72cm
    -   cylinder001: height: 130cm, angle: 90°, axis: x:0,y:1,z:0 position: x:-10mm, y:84cm, z:72cm
    -   cylinder002: height: 90cm, angle: 90°, axis: x:-1,y:0,z:0 position: x:40mm, y:-10mm, z:70cm
    -   cylinder003: height: 90cm, angle: 90°, axis: x:-1,y:0,z:0 position: x:124cm, y:-10mm, z:70cm

![](images/Exercise_table_04.jpg )

Du wirst feststellen, dass die Zylinder etwas länger sind als erforderlich. Der Grund ist, dass, wie in allen Volumenkörper-basierten 3D-Applikationen, Boole\'sche Operationen in FreeCAD teilweise überempfindlich auf Fläche-auf-Fläche-Situationen reagieren und fehlschlagen könnten. Deshalb bringen wir uns auf die sichere Seite.

-   Lass uns nun die Subtraktionen durchführen. Wähle den ersten Fuß, dann mit gedrückter Strg Taste eine der ihn kreuzenden Röhren, und drücke den **Cut**-Button. Das Loch ist da und die Röhre wird versteckt. Finde sie in der Baumansicht durch Aufklappen des durchlöcherten Fußes.
-   Wähle den Fuß am anderen Ende der versteckten Röhre, dann wiederhole die Operation, dieses Mal Strg+ Wahl des Rohrs in der Baumansicht, denn in der 3D Ansicht ist sie versteckt (Du kannst sie auch wieder sichtbar machen und sie in der 3D Ansicht auswählen). Wiederhole dies für die anderen Füße, bis jeder von ihnen zwei Löcher hat:

![](images/Exercise_table_05.jpg )

Wie man sieht, ist jeder Fuß das Ergebnis einer ziemlich langen Reihe von Operationen. All dies bleibt parametrisch, und Du kannst jederzeit jeden Parameter in jeder der alten Operationen ändern. In FreeCAD bezeichnen wir diesen Haufen als \"Modellierungshistorie\", denn er enthält in der Tat die komplette Historie der durchgeführten Operationen.

Eine weitere Eigentümlichkeit von FreeCAD ist, dass das Konzept von 3D Objekten und das Konzept von 3D Operationen dazu neigen, sich in das gleiche Ding zu integrieren. Der Cut ist zur gleichen Zeit eine Operation und das aus dieser Operation resultierende 3D Objekt. In FreeCAD wird dies ein \"Formelement\" genannt, eher als Objekt oder Operation.

-   Jetzt werden wir die Tischplatte erstellen, ein einfacher Block aus Holz, also ein weiterer **Quader** mit length: 126cm, width: 86cm, height: 8cm, position: x: 10mm, y: 10mm, z, 67cm. Im **Ansicht** Reiter kannst Du ihm einen schönen Braunton geben, eine holzartige Farbe durch Ändern der **Shape Color**-Eigenschaft:

![](images/Exercise_table_06.jpg )

Beachte, dass wir die Beine 10 mm entfernt platziert haben, obwohl sie nur 8 mm dick sind. Dies ist natürlich nicht notwendig und es wird bei einem realen Tisch auch nicht passieren, aber es üblich, das in dieser Art von \"Baugruppen\"-Modus zu tun, denn es hilft Leuten, die sich das Modell ansehen, zu verstehen, dass es sich um unabhängige Teile handelt, die später manuell zusammengesetzt werden müssen.

Nachdem unsere fünf Teile fertig sind, ist es Zeit, ihnen bessere Bezeichnungen zu geben als \"Cut015\". Durch rechtklicken der Objekte in der Baumansicht (oder Drücken von **F2**) kannst Du sie in etwas umbenennen, was für Dich oder eine andere Person, die die Datei später öffnet, aussagekräftiger ist. Es wird oft gesagt, dass das Vergeben von sinnvollen Namen für die Objekte viel wichtiger ist als sie zu modellieren.

-   Wir werden nun ein paar Schrauben anbringen. Es gibt heutzutage eine extrem nützliche Erweiterung, das von einem Mitglied der FreeCAD Gemeinschaft entwickelt wurde, das Du im [FreeCAD addons](https://github.com/FreeCAD/FreeCAD-addons) Repositorium findest, [Fasteners](https://github.com/shaise/FreeCAD_FastenersWB) genannt, welches das Einfügen von Schrauben sehr vereinfacht. Das Installieren von zusätzlichen Arbeitsbereichen ist einfach und auf den [Erweiterungsseiten ](Std_AddonMgr/de.md) beschrieben.
-   Sobald Du den Arbeitsbereich Verbindungselemente installiert und FreeCAD erneut gestartet hast, wird er in der Arbeitsbereichliste erscheinen und wir können dorthin wechseln. Das Hinzufügen einer Schraube zu einem unserer Löcher erfolgt zuerst durch Auswählen der Kreislinie unseres Loches:

![](images/Exercise_table_07.jpg )

-   Dann klicken wir einen der Schrauben-Buttons aus dem Fastener-Arbeitsbereich, z.B. die **EN 1665 Hexagon bolt with flanges, heavy series**. Die Schraube wird platziert, an unserem Loch ausgerichtet und der Durchmesser wird automatisch an die Größe des Lochs angepasst. Manchmal wird die Schraube spiegelverkehrt platziert, was wir durch Umdrehen des **invert**-Eigenschaftswert korrigieren können. Wir können auch den Offset auf 2 mm setzen, um den gleichen Regeln wie beim Abstand von Tischplatte und Tischbeinen zu folgen:

![](images/Exercise_table_08.jpg )

-   Wiederhole dies für alle Löcher und unser Tisch ist fertig!

**Die interne Struktur von Part-Objekten**

Wie wir oben gesehen haben, ist es in FreeCAD möglich, nicht ganze Objekte auszuwählen, sondern auch Teile davon, wie z.B. die Kreislinie unseres Schraubenlochs. Dies ist eine gute Gelegenheit, um einen schnellen Blick darauf zu werfen, wie Part-Objekte intern konstruiert sind. Jeder Arbeitsbereich, mit dem Part-Geometrien erstellt werden können, besteht aus:

-   **Eckpunkten**: Dies sind Punkte (normalerweise Endpunkte), auf denen der Rest aufgebaut ist. Zum Beispiel hat eine Linie zwei Eckpunkte.
-   **Kanten**: Die Kanten sind lineare Geometrien wie Linien, Kreisbögen, Ellipsen oder [https://de.wikipedia.org/wiki/Non-Uniform_Rational_B-Spline nurbs](https://de.wikipedia.org/wiki/Non-Uniform_Rational_B-Spline_nurbs.md) Kurven. Sie haben normalerweise zwei Eckpunkte, aber in einigen speziellen Fällen nur eine (ein geschlossener Kreis beispielsweise).
-   **Drähte**: Ein Draht ist eine Reihe von Kanten, die durch ihre Endpunkt verbunden sind. Er kann Kanten jedes Typs enthalten und geschlossen sind oder nicht.
-   **Flächen**: Flächen können plan oder gewölbt sein und durch einen geschlossenen Draht geformt werden, der die Grenze der Fläche bildet, oder mehr als einen, falls die Fläche Löcher hat.
-   **Hüllen**: Hüllen sind einfach eine Gruppe von Flächen, die an ihren Kanten verbunden sind. Sie können offen oder geschlossen sein.
-   **Volumenkörper**: Wenn eine Hülle fest verschlossen ist, wenn sie also kein \"Leck\" hat, wird sie ein Volumenkörper. Volumenkörper haben Innen- und Außenseite. Viele Arbeitsbereiche vertrauen darauf, um sicherzustellen, dass die erstellten Objekte in der realen Welt gebaut werden können.
-   **Teileverbünde**: Teileverbünde sind einfach eine Anhäufung von anderen Formen, unabhängig von ihrem Typ, zu einer einzigen Form.

In der 3D-Ansicht kannst Du einzelne **Eckpunkte**, **Kanten** oder **Flächen** auswählen. Die Auswahl eines dieser Objekte wählt das ganze Objekt aus.

**Eine Anmerkung zu geteiltem Design**

Du könntest den Tisch ansehen und denken, dass das Design nicht gut ist. Die Verbindung der Füße mit der Tischplatte ist vielleicht zu schwach. Du könntest verstärkende Teile hinzufügen wollen oder einfach andere Ideen haben, um es zu verbessern. An dieser Stelle wird teilen interessant. Du kannst die während der Übung erstellte Datei unter dem Link herunterladen und sie modifizieren, um sie besser zu machen. Dann, wenn Du diese verbesserte Datei teilst, könnten andere in der Lage sein, sie nochmal zu verbessern oder Deinen gut designten Tisch in ihren Projekten benutzen. Dein Design könnte andere auf andere Ideen bringen und vielleicht hast Du ein winziges Stück geholfen, eine bessere Welt zu schaffen\...

**Downloads**

-   Die in dieser Übung erstellte Datei: <https://github.com/yorikvanhavre/FreeCAD-manual/blob/master/files/table.FCStd>

**Lies mehr**

-   [Der Part Arbeitsbereich](Part_Workbench/de.md)
-   [Das FreeCAD Erweiterungs Repositorium](https://github.com/FreeCAD/FreeCAD-addons)
-   [Der Verbindungselemente Arbeitsbereich](https://github.com/shaise/FreeCAD_FastenersWB)



---
⏵ [documentation index](../README.md) > [Tutorials](Category_Tutorials.md) > Manual:Traditional modeling, the CSG way/de
