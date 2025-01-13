# Manual:Traditional modeling, the CSG way/de
{{Manual:TOC}}

[CSG](https://en.wikipedia.org/wiki/Constructive_solid_geometry) steht für Constructive Solid Geometry und beschreibt die grundlegende Arbeitsweise mit dreidimensionaler Festkörpergeometrie. Dabei werden komplexe Objekte erstellt, indem mithilfe von Booleschen Operationen wie Vereinigung, Subtraktion oder Schnittmenge Teile zu Festkörpern hinzugefügt oder entfernt werden.

Wie bereits früher in diesem Handbuch erläutert, unterstützt FreeCAD verschiedene Geometrietypen. Der bevorzugte und praktischste Typ zum Entwerfen realer 3D-Objekte in FreeCAD ist jedoch die feste [BREP](https://en.wikipedia.org/wiki/Boundary_representation)-Geometrie, die hauptsächlich vom Part Workbench verarbeitet wird. Boundary Representation ist eine Methode zur Darstellung von Formen anhand ihrer räumlichen Grenzen. Sie definiert ein 3D-Objekt durch Angabe seiner Oberflächen, Kanten und Eckpunkte. Die wichtigsten Aspekte von BREP umfassen Flächen, also die Oberflächenelemente des Objekts, Kanten, die Grenzlinien, an denen zwei Flächen aufeinandertreffen, und Eckpunkte, also die Punkte, an denen Kanten zusammenlaufen.

BREP bietet mehrere Vorteile. Erstens definiert es Oberflächen mithilfe mathematischer Gleichungen und ermöglicht so eine präzise und genaue Modellierung. Diese Präzision ist für technische Anwendungen, bei denen genaue Abmessungen erforderlich sind, von entscheidender Bedeutung. Darüber hinaus bietet BREP glatte und detaillierte Oberflächen, im Gegensatz zu [Polygonnetzen](https://en.wikipedia.org/wiki/Polygon_mesh), die gekrümmte Oberflächen mit Facetten annähern. Dies ist vergleichbar mit dem Unterschied zwischen Vektorbildern, die ohne Qualitätsverlust skaliert werden können, und Bitmap-Bildern, die bei Vergrößerung pixelig erscheinen können. BREP behält umfassende topologische Informationen über das Objekt bei, einschließlich der Beziehungen zwischen Flächen, Kanten und Eckpunkten, was für komplexe Operationen wie Boolesche Berechnungen und Abrundungen unerlässlich ist.

Polygonnetze bestehen aus Eckpunkten, Kanten und Flächen, die Dreiecke oder Vierecke bilden. Sie sind einfacher und schneller zu rendern, weisen jedoch keine hohe Präzision auf. Beim Vergrößern oder Drucken in großem Maßstab zeigen Netze Facetten artige Oberflächen statt glatter Kurven. Im Gegensatz dazu verwendet BREP mathematisch definierte Kurven und Oberflächen und bietet so höhere Genauigkeit und Glätte. BREP-Modelle sind für CAD-Anwendungen vorzuziehen, bei denen Präzision unverzichtbar ist.

In FreeCAD wird BREP-basierte Geometrie von [OpenCasCade](https://en.wikipedia.org/wiki/Open_Cascade_Technology) verwaltet, einer Open-Source-Softwarebibliothek. Die primäre Schnittstelle zwischen FreeCAD und dem OpenCasCade-Kernel ist der Arbeitsbereich Part, der als Grundlage für die meisten anderen Arbeitsbereiche dient und grundlegende Werkzeuge zum Erstellen und Bearbeiten von BREP-Objekten bietet. Der Arbeitsbereich Part enthält Werkzeuge zum Erstellen von Grundelementen, wie z. B. Grundformen wie Quader, Zylinder und Kugeln, zum Ausführen von booleschen Verknüpfungen, wie Vereinigen, Schneiden und Differenz, an Formen und zum Durchführen von Transformationen, einschließlich Verschieben, Drehen, Skalieren und Klonen von Objekten.

Während andere Arbeitsbereiche in FreeCAD, wie z. B. die Arbeitsbereiche Part Design und Surface, fortgeschrittenere Werkzeuge zum Erstellen und Bearbeiten von Geometrie bieten, basieren diese auf dem zugrunde liegenden Arbeitsbereich Part. Es ist von Vorteil, wenn man versteht, wie Part-Objekte intern funktionieren, und mit den grundlegenden Part-Werkzeugen vertraut ist. Oft können diese einfacheren Werkzeuge Probleme lösen, die komplexere Werkzeuge möglicherweise nicht effektiv bewältigen können.

![](images/Mesh_vs_brep.jpg )

Der Unterschied zwischen beiden ist vergleichbar mit dem Unterschied zwischen Bitmap- und Vektorbildern. Wie bei Bitmap-Bildern sind die gekrümmten Oberflächen von Polygonnetzen in eine Reihe von Punkten unterteilt. Wenn du genau hinsiehst oder es sehr groß ausdruckst, siehst du keine gekrümmte, sondern eine facettenartige Oberfläche. Sowohl bei Vektorbildern als auch bei BREP-Daten wird die Position eines beliebigen Punkts auf einer Kurve nicht in der Geometrie gespeichert, sondern im laufenden Betrieb mit höchster Präzision berechnet.

Um die Funktionsweise des Arbeitsbereichs Part zu veranschaulichen, modellieren wir diesen Tisch, wobei wir ausschließlich CSG-Operationen verwenden (mit Ausnahme der Schrauben, für die wir eines der Addons verwenden, und der Abmessungen, die wir im nächsten Kapitel sehen werden):

![](images/Exercise_table_complete.jpg )

Erstellen wir ein neues Dokument (**Strg+N** oder Menü **Datei → Neu**), um unseren Tabellenentwurf zu speichern. Das Dokument wird zunächst auf der Registerkarte „Modell" im Bedienfeld „Combo-Ansicht" als „unbenannt" bezeichnet, aber wenn du das Dokument (**Strg+Umschalt+S** oder Menü **Datei → Speichern unter**) als neues FreeCAD-Dokument mit dem Namen „table.FCStd" speichest, wird das Dokument in „table" umbenannt, was das Projekt klarer identifiziert. Wir werden mit mm als Längeneinheit arbeiten. Du kannst dies nach Belieben ändern, indem du das Menü in der unteren rechten Ecke verwendest.

Jetzt können wir zum Arbeitsbereich [Part](Part_Workbench/de.md) wechseln und mit der Erstellung des ersten Tischbeins beginnen.

-   Die Schaltfläche <img alt="" src=images/Part_Box.svg  style="width:16px;"> **Quader** drücken
-   Den Würfel auswählen und dann die folgenden Eigenschaften festlegen (auf der Registerkarte **Daten**):
    -   Länge: 80 mm
    -   Breite: 80 mm
    -   Höhe: 750 mm
-   Den Würfel duplizieren, indem **Strg+C** und dann **Strg+V** gedrückt wird (oder die Menüeinträge **Bearbeiten → Kopieren** und **Einfügen** ausgewählt werden). (Es wird keine Änderung sichtbar sein, da das zweite Objekt das erste überlagert.)
-   Das neu erstellte Objekt mit dem Namen Cube001 auswählen (auf der linken Registerkarte Modell auf Cube001 klicken).
-   Seine Position ändern, indem seine Eigenschaft Placement bearbeitet wird:
    -   Position x: 8 mm
    -   Position y: 8 mm

Du solltest jetzt zwei hohe Quader erhalten, der eine 8 mm vom anderen entfernt:

![](images/Exercise_table_01.jpg )

-   Jetzt können wir den einen vom anderen subtrahieren: den **ersten** auswählen, das ist der, der **übrig** bleibt, dann mit gedrückter Strg-Taste, den **anderen** auswählen, der subtrahiert wird (die Reihenfolge ist wichtig) und drücke die Schaltfläche <img alt="" src=images/Part_Cut.svg  style="width:16px;"> **Differenz**:

![](images/Exercise_table_02.jpg )

Beachte, dass das neu erzeugte Objekt, \"Cut\" benannt, noch die beiden Quader enthält, die wir als Operanden benutzt haben. Tatsächlich sind die beiden Quader weiterhin im Dokument, sie wurden einfach versteckt und in der Baumansicht unterhalb des Cut-Objekts angeordnet. Du kannst sie durch expandieren des Pfeils neben dem Cut-Objekt noch auswählen, und durch rechtsklicken wieder sichtbar machen oder jede beliebige Eigenschaft ändern.

Du kannst das Werkzeug Differenz und andere Werkzeuge für boolesche Verknüpfungen auch über die „Combo-Ansicht" mit <img alt="" src=images/Part_Boolean.svg  style="width:16px;"> [Boolesche Verknüpfung](Part_Boolean/de.md) verwenden. Dies ergibt einen eindeutigeren aber längeren Arbeitsablauf.

-   Erstellen wir nun die drei anderen Füße, indem wir unseren Basiswürfel noch 6 Mal duplizieren. Da er immer noch kopiert ist, können wir ihn einfach 6 Mal einfügen (Strg+V). Ihre Position wie folgt ändern:
    -   Cube002: x: 0, y: 800 mm
    -   Cube003: x: 8 mm, y: 792 mm
    -   Cube004: x: 1200 mm, y: 0
    -   Cube005: x: 1192 mm, y: 8 mm
    -   Cube006: x: 120 mm, y: 800 mm
    -   Cube007: x: 1192 mm, y: 792 mm

-   Nun führen wir die drei anderen Schnitte aus, indem wir zuerst den „Host"-Würfel auswählen und dann den Würfel, der (aus ihm) herausgeschnitten werden soll. Wir haben jetzt vier Cut-Objekte:

![](images/Exercise_table_03.jpg )

Du hast vielleicht gedacht, dass wir, anstatt den Basiswürfel sechsmal zu duplizieren, den gesamten Fuß dreimal hätten duplizieren können. Das ist völlig richtig, denn wie immer gibt es in FreeCAD viele Möglichkeiten, das gleiche Ergebnis zu erzielen. Das ist eine wertvolle Sache, die man sich merken sollte, denn wenn wir zu komplexeren Objekten übergehen, führen einige Operationen möglicherweise nicht zum richtigen Ergebnis und wir müssen oft andere Wege ausprobieren.

-   Wir werden jetzt mit derselben Schnittmethode Löcher für die Schrauben bohren. Da wir 8 Löcher brauchen, zwei in jedem Fuß, könnten wir 8 zu subtrahierende Objekte herstellen. Lass uns stattdessen andere Möglichkeiten erkunden und 4 Rohre herstellen, die von zwei Füßen wiederverwendet werden. Erstellen wir also vier Rohre mit dem <img alt="" src=images/Part_Cylinder.svg  style="width:16px;"> **Zylinder**-Werkzeug. Du kannst auch hier nur ein Rohr herstellen und es anschließend duplizieren. Gib allen Zylindern einen Radius von 6 mm. Dieses Mal müssen wir sie drehen, was ebenfalls über die Eigenschaft **Platzierung** unter der Registerkarte Daten erfolgt *(**Hinweis:** ändere die Eigenschaft Achse*bevor*du den Winkel festlegst, sonst wird die Drehung nicht angewendet)*:
    -   Zylinder: Höhe: 1300 mm, Winkel: 90°, Achse: x:0, y:1, z:0, Position: x:-10 mm, y:40 mm, z: 720 mm
    -   Zylinder001: Höhe: 1300 mm, Winkel: 90°, Achse: x:0, y:1, z:0, Position: x:-10 mm, y:840 m, z: 720 mm
    -   Zylinder002: Höhe: 900 mm, Winkel: 90°, Achse: x:-1, y:0, z:0, Position: x:40 mm, y:-10 mm, z: 700 m
    -   Zylinder003: Höhe: 900 mm, Winkel: 90°, Achse: x:-1, y:0, z:0, Position: x:1240 mm, y:-10 mm, z:700 mm

![](images/Exercise_table_04.jpg )

Du wirst feststellen, dass die Zylinder etwas länger sind als erforderlich. Der Grund ist, dass, wie in allen Festkörper-basierten 3D-Applikationen, boolesche Verknüpfungen in FreeCAD teilweise überempfindlich auf Fläche-auf-Fläche-Situationen reagieren und fehlschlagen könnten. Deshalb bringen wir uns auf die sichere Seite.

-   Jetzt führen wir die Subtraktionen durch. Wähle den ersten Fuß aus, und wähle dann bei gedrückter STRG-Taste eines der Rohre aus, die ihn kreuzen, und drücke die Schaltfläche **Differenz**. Das Loch wird gemacht und das Rohr ausgeblendet. Finde es in der Baumansicht, indem du den durchbohrten Fuß erweiterst.
-   Wähle einen anderen Fuß aus, der von diesem ausgeblendeten Rohr durchbohrt wurde, und wiederhole den Vorgang, indem du dieses Mal die Strg+Taste drückst und das Rohr in der Baumansicht auswählst, da es in der 3D-Ansicht ausgeblendet ist (Du kannst es auch wieder sichtbar machen und in der 3D-Ansicht auswählen). Wiederhole dies für die anderen Füße, bis jeder von ihnen seine zwei Löcher hat:

![](images/Exercise_table_05.jpg )

Wie man sieht, ist jeder Fuß das Ergebnis einer ziemlich langen Reihe von Operationen. All dies bleibt parametrisch, und Du kannst jederzeit jeden Parameter in jeder der alten Operationen ändern. In FreeCAD bezeichnen wir diesen Haufen als \"Modellierungshistorie\", denn er enthält in der Tat die komplette Historie der durchgeführten Operationen.

Eine weitere Eigentümlichkeit von FreeCAD ist, dass das Konzept von 3D-Objekten und das Konzept von 3D-Operationen dazu neigen, sich in das gleiche Ding zu integrieren. Cut ist zur gleichen Zeit eine Operation (boolesche Differenz) und das aus dieser Operation resultierende 3D-Objekt. In FreeCAD wird dies eher ein \"Formelement\" genannt, als Objekt oder Operation.

Jetzt machen wir die Tischplatte, es wird ein einfacher Holzblock sein, machen wir es mit einem weiteren **Quader**:

-   Box: Länge: 1260 mm, Breite: 860 mm, Höhe: 80 mm, Position: x: 10 mm, y: 10 mm, z: 670 mm.

Auf der Registerkarte **Ansicht** kannst du ihr eine schöne bräunliche, holzähnliche Farbe geben, indem du ihre Eigenschaft **Formfarbe** änderst:

Nachdem unsere fünf Teile fertig sind, ist es Zeit, ihnen bessere Bezeichnungen zu geben als \"Cut015\". Durch rechtklicken der Objekte in der Baumansicht (oder Drücken von **F2**) kannst Du sie in etwas umbenennen, was für Dich oder eine andere Person, die die Datei später öffnet, aussagekräftiger ist. Es wird oft gesagt, dass das Vergeben von sinnvollen Namen für die Objekte viel wichtiger ist als sie zu modellieren.

-   Wir werden nun ein paar Schrauben anbringen. Es gibt heutzutage eine extrem nützliche Erweiterung, die von einem Mitglied der FreeCAD-Gemeinschaft entwickelt wurde, das Du im [FreeCAD addons](https://github.com/FreeCAD/FreeCAD-addons) Repositorium findest, [Fasteners](https://github.com/shaise/FreeCAD_FastenersWB) genannt, welche das Einfügen von Schrauben sehr vereinfacht. Das Installieren von zusätzlichen Arbeitsbereichen ist einfach und auf den Seiten der [Erweiterungen](Std_AddonMgr/de.md) beschrieben.
-   Sobald Du den Arbeitsbereich Fasteners installiert und FreeCAD erneut gestartet hast, wird er in der Liste der Arbeitsbereiche erscheinen und wir können dorthin wechseln. Das Hinzufügen einer Schraube zu einem unserer Löcher erfolgt zuerst durch Auswählen der Kreislinie unseres Loches:

![](images/FastenerWorkbench.png )

-   Dann können wir einen der Schraubenknöpfe des Arbeitsbereichs Fasteners drücken, zum Beispiel die **EN 1665 Sechskantschraube mit Flansch, schwere Reihe**. Die Schraube wird platziert und an unserem Loch ausgerichtet, und der Durchmesser wird automatisch passend zur Größe unseres Lochs ausgewählt. Manchmal wird die Schraube verkehrt herum platziert, was wir korrigieren können, indem wir ihre **umgekehrt** Eigenschaft umdrehen. Wir können ihren Versatz auch auf 2 mm einstellen, um derselben Regel zu folgen, die wir zwischen der Tischplatte und den Füßen verwendet haben:

![](images/FastenerWorkbench_sel.png )

-   Wiederhole dies für alle Löcher und unser Tisch ist fertig!

Wie bereits erwähnt, kannst du in FreeCAD dasselbe Ergebnis erzielen, indem du unterschiedliche Schritte ausführst. Um dies zu demonstrieren, erstellen wir denselben Tisch mit einer anderen Methode. Denke daran, es gibt keinen richtigen oder falschen Weg -- nur individuelle Kreativität.

Wir beginnen auf ähnliche Weise: indem wir einen Würfel mit den folgenden Abmessungen erstellen: Länge 80 mm, Breite 8 mm und Höhe 750 mm

-   Erstelle einen Würfel, indem du die Schaltfläche <img alt="" src=images/Part_Box.svg  style="width:16px;"> **Quader** auswählst und die folgenden Eigenschaften festlegst (auf der Registerkarte **Daten**):
    -   Länge: 80 mm
    -   Breite: 8 mm
    -   Höhe: 750 mm
-   Als Nächstes erstellen wir einen <img alt="" src=images/Part_Cylinder.svg  style="width:16px;"> **Zylinder** mit den folgenden Eigenschaften:
    -   Radius: 6 mm, Höhe: 100 mm, Winkel: 90°, Achse: x: 1, y: 0, z: 0, Position: x: 40 mm, y: 40 mm, z: 720 mm
-   Als Nächstes wenden wir das Schneidewerkzeug an. Wähle den Würfel aus und wähle mit gedrückter STRG-Taste den Zylinder aus. Beachte, dass die Reihenfolge wichtig ist, um zu definieren, welches bleibt. Drücke dann die Schaltfläche <img alt="" src=images/Part_Cut.svg  style="width:16px;"> **Differenz**.
-   Wir kopieren und fügen dann das ausgeschnittene Objekt ein, indem wir **Strg+C** und dann **Strg+V** drücken (oder das Menü **Bearbeiten → Kopieren** und **Einfügen**):
    -   Winkel: 90°, Achse: x: 0, y: 0, z: 1, Position: x: 8 mm
-   Wähle die beiden Objekte aus und wende das Werkzeug <img alt="" src=images/Part_Fuse.svg  style="width:16px;"> **Vereinigung** an. Jetzt sind die beiden Objekte verschmolzen und wir haben einen Fuß.
-   Kopiere und füge das verschmolzene Bein ein und positioniere es bei
    -   Winkel: 90°, Achse: x: 0, y: 0, z: 1, Position y: 800 mm.
-   Wähle die beiden Füße aus und erstelle einen <img alt="" src=images/Part_Compound.svg  style="width:16px;"> **Verbund**.
-   Kopiere den Verbund und füge ihn ein. Positioniere ihn an folgender Stelle:
    -   Winkel: 180°, Achse: x:0, y:0, z:1, Position x: 1200 mm, y: 800 mm. Wir haben unsere Füße.

Lass uns die Tischplatte erstellen.

-   Erstelle einen Quader mit den Abmessungen:
    -   Länge: 752 mm
    -   Breite: 1184 mm
    -   Höhe: 784 mm
    -   Position x: 8 mm, y: 8 mm, z: 670 mm.

Nun machen wir genauso weiter wie zuvor, wenn wir Schrauben hinzufügen möchten (hoffentlich möchten wir das).

![](images/Tabble_alternative_complete.png )

**Die interne Struktur von Teilobjekten**

Wie wir oben gesehen haben, ist es in FreeCAD möglich, nicht nur ganze Objekte, sondern auch Teile davon auszuwählen, wie beispielsweise den kreisförmigen Rand unseres Schraubenlochs. Dies ist ein guter Zeitpunkt, um einen kurzen Blick darauf zu werfen, wie Part-Objekte intern konstruiert werden. Jeder Arbeitsbereich, der Part-Geometrie erzeugt, basiert auf Folgendem:

-   **Knotenpunkte** (kurz Knoten): Dies sind Punkte (normalerweise Endpunkte), auf denen alles andere aufbaut. Eine Linie hat beispielsweise zwei Knoten (engl. vertices).
-   **Kanten**: Die Kanten sind linienförmige Geometrien wie Linien, Bögen, Ellipsen oder [NURBS](https://en.wikipedia.org/wiki/Non-uniform_rational_B-spline)-Kurven. Sie haben normalerweise zwei Knoten, aber einige Sonderfälle haben nur einen (z. B. ein geschlossener Kreis).
-   **Kantenzüge**: Ein Kantenzug ist eine Folge von Kanten, die durch ihre Endpunkte (Knoten) verbunden sind. Er kann Kanten beliebigen Typs enthalten und geschlossen sein oder nicht.
-   **Flächen**: Flächen können eben oder gekrümmt sein und können durch einen geschlossenen Kantenzug gebildet werden, der den Rand der Fläche bildet, oder durch mehrere, falls die Fläche Löcher hat.
-   **Schalen**: Schalen sind einfach eine Gruppe von Flächen, die durch ihre Kanten verbunden sind. Sie können offen oder geschlossen sein.
-   **Festkörper**: Wenn eine Hülle dicht verschlossen ist, das heißt, sie hat kein \"Leck\", wird sie zu einem Festkörper. Festkörper beinhalten die Vorstellung von innen und außen. Viele Workbenches verlassen sich darauf, um sicherzustellen, dass die von ihnen hergestellten Objekte in der realen Welt gebaut werden können.
-   **Verbundobjekte**: Verbundobjekte sind einfach Anhäufungen anderer Formen, unabhängig von ihrer Art, zu einer einzigen Form.

In der 3D-Ansicht kannst du einzelne **Knotenpunkte**, **Kanten** oder **Flächen** auswählen. Wenn du eine davon auswählst, wird gleichzeitig das gesamte Objekt ausgewählt.

**Eine Anmerkung zu geteiltem Design**

Vielleicht siehst du dir den Tisch oben an und denkst, dass sein Design nicht gut ist. Die Verbindung der Füße mit der Tischplatte ist wahrscheinlich zu schwach. Vielleicht möchtest du Verstärkungsteile hinzufügen oder hast einfach andere Ideen, um ihn zu verbessern. Hier wird das Teilen interessant. Du kannst die während dieser Übung erstellte Datei über den unten stehenden Link herunterladen und ändern, um sie zu verbessern. Wenn du diese verbesserte Datei dann teilst, können andere sie möglicherweise noch besser machen oder deinen gut gestalteten Tisch in ihren Projekten verwenden. Dein Design könnte dann anderen Menschen neue Ideen geben, und vielleicht hast du ein kleines bisschen dazu beigetragen, eine bessere Welt zu schaffen \...

**Downloads**

-   Die in dieser Übung erstellte Datei: <https://github.com/yorikvanhavre/FreeCAD-manual/blob/master/files/table.FCStd>

**Lies mehr**

-   Der Arbeitsbereich [Part](Part_Workbench/de.md)
-   [Das FreeCAD Erweiterungs Repositorium](https://github.com/FreeCAD/FreeCAD-addons)
-   Der Arbeitsbereich [Fasteners](https://github.com/shaise/FreeCAD_FastenersWB)



---
⏵ [documentation index](../README.md) > [Tutorials](Category_Tutorials.md) > Manual:Traditional modeling, the CSG way/de
