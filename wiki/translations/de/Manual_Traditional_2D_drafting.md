# Manual:Traditional 2D drafting/de
{{Manual:TOC}}

Der Arbeitsbereich Draft von FreeCAD fungiert als Brücke zwischen 2D-Zeichnen und 3D-Modellierung und ist damit einzigartig im Vergleich zu herkömmlichen 2D-CAD-Systemen wie AutoCAD. Während FreeCAD in einer vollständig 3D-Umgebung arbeitet, ist der Arbeitsbereich Draft so konzipiert, dass er Benutzern vertraute 2D-Zeichenwerkzeuge bietet und gleichzeitig die Flexibilität eines reibungslosen Übergangs zwischen 2D-Skizzen und 3D-Objekten bietet. Du kannst beispielsweise benutzerdefinierte Arbeitsebenen festlegen, um auf bestimmten Oberflächen oder in bestimmten Ausrichtungen zu zeichnen, was die Konstruktion parametrischer Modelle ermöglicht. Da FreeCAD parametrisch ist, werden alle an den Abmessungen vorgenommenen Änderungen automatisch im gesamten Projekt aktualisiert.

Eine der Stärken des Arbeitsbereichs Draft ist sein umfassender Werkzeugsatz, der sowohl grundlegende Zeichen- als auch erweiterte Änderungswerkzeuge umfasst. Diese Werkzeuge können nicht nur zum 2D-Zeichnen, sondern auch zum Bearbeiten von Objekten im 3D-Raum verwendet werden. Du kannst Arbeitsebenen festlegen, Raster definieren und Randbedingungen anwenden, um sicherzustellen, dass die geometrischen Beziehungen in deinem gesamten Entwurf erhalten bleiben. Draft-Objekte können mithilfe von Einrastmodi und einer Vielzahl von Randbedingungen geändert und neu positioniert werden, was präzises Zeichnen erheblich erleichtert.

Einige der im Arbeitsbereich Draft enthaltenen Werkzeuge:

1.  Zeichenwerkzeuge:

-   <img alt="" src=images/Draft_Line.svg  style="width:16px;"> [Linie](Draft_Line/de.md), <img alt="" src=images/Draft_Wire.svg  style="width:16px;"> [Linienzug](Draft_Wire/de.md) (Polylinie): Mit diesen Werkzeugen kannst du gerade Liniensegmente oder durchgehende Linienzüge erstellen, die eingeschränkt und in 3D-Formen umgewandelt werden können.
-   <img alt="" src=images/Draft_Circle.svg  style="width:16px;"> [Kreis](Draft_Circle/de.md), <img alt="" src=images/Draft_Ellipse.svg  style="width:16px;"> [Ellipse](Draft_Ellipse/de.md) und <img alt="" src=images/Draft_Arc.svg  style="width:16px;"> [Kreisbogen](Draft_Arc/de.md): Werden verwendet, um grundlegende kreisförmige und elliptische Formen zu definieren, mit Optionen zur weiteren Bearbeitung.

1.  Manipulationswerkzeuge:

-   <img alt="" src=images/Draft_Move.svg  style="width:16px;"> [Verschieben](Draft_Move/de.md), <img alt="" src=images/Draft_Rotate.svg  style="width:16px;"> [Drehen](Draft_Rotate/de.md) oder <img alt="" src=images/Draft_Scale.svg  style="width:16px;"> [Skalieren](Draft_Scale/de.md): Diese Operationen funktionieren sowohl in 3D als auch in 2D und bieten Flexibilität bei der Positionierung von Objekten.
-   <img alt="" src=images/Draft_Offset.svg  style="width:16px;"> [Versetzen](Draft_Offset/de.md): Ähnlich wie bei herkömmlichen CAD-Systemen kannst du hiermit parallele Linien oder Kurven erstellen.
-   <img alt="" src=images/Draft_Trimex.svg  style="width:16px;"> [Trimex](Draft_Trimex/de.md) und <img alt="" src=images/Draft_Stretch.svg  style="width:16px;"> [Strecken](Draft_Stretch/de.md): Modifiziere Linien und Formen, indem du sie kürzt oder verlängerst, sodass sie andere Objekte schneiden oder treffen.
-   <img alt="" src=images/Draft_Mirror.svg  style="width:16px;"> [Spiegeln](Draft_Mirror/de.md) und <img alt="" src=images/Draft_Array.svg  style="width:16px;"> [Anordnung](Draft_Array/de.md): Diese Werkzeuge replizieren und strukturieren Objekte, ideal für sich wiederholende Komponenten.

Das Einrastsystem in FreeCADs Arbeitsbereich Draft ist auf Präzision ausgelegt. Egal, ob du in 2D oder 3D arbeitest, du kannst auf kritischen Punkten wie Endpunkten, Mittelpunkten und Kreiszentren einrasten, was die Positionierung von Elementen relativ zueinander erleichtert. Modi wie senkrecht, tangential und auf Schnittpunkt einrasten verbessern die Präzision noch weiter. In Kombination mit der Arbeitsebene und dem Rastersystem gewährleisten diese Werkzeuge die genaue Ausrichtung von Objekten und Komponenten.

Die parametrische Natur von FreeCAD ermöglicht die Anwendung von Beschränkungen auf entworfene Elemente, wodurch sichergestellt wird, dass die geometrischen Beziehungen erhalten bleiben. Du kannst beispielsweise Linien parallel oder senkrecht zeichnen und feste Abstände zwischen Elementen festlegen. Diese Beschränkungen können später angepasst werden, sodass Designänderungen im gesamten Projekt reibungslos und konsistent erfolgen. Der Arbeitsbereich Draft lässt sich auch nahtlos in andere FreeCAD-Arbeitsbereiche integrieren, wie z. B. Sketcher, das für eingeschränkteres parametrisches 2D-Design entwickelt wurde, und TechDraw, das technische 2D-Zeichnungen für Dokumentationszwecke erstellt.

Zu den erweiterten Funktionen des Arbeitsbereichs Draft gehört die Möglichkeit, Dateien in Formaten wie DXF und SVG zu importieren und zu exportieren, sodass du mit Benutzern anderer CAD-Programme arbeiten oder Designs mit ihnen teilen kannst. Python-Skripting erweitert die Fähigkeiten von FreeCAD zusätzlich und ermöglicht dir die Automatisierung von Aufgaben oder die Erstellung benutzerdefinierter Arbeitsabläufe. Du kannst Skripte schreiben, die Entwurfsobjekte auf der Grundlage bestimmter geometrischer Regeln generieren und so sich wiederholende Aufgaben rationalisieren.

Um den Arbeitsablauf und die Möglichkeiten des Arbeitsbereichs Draft zu präsentieren, werden wir eine einfache Übung durchlaufen, deren Ergebnis diese kleine Zeichnung sein wird, die den Grundriss eines kleinen Hauses zeigt, das nur eine Küchenzeile enthält (ein ziemlich absurder Grundriss, aber wir können hier machen, was wir wollen, nicht wahr?):

![](images/Exercise_cabin_01.jpg )

-   Wechsle zum Arbeitsbereich **Draft**
-   Wie bei allen technischen Zeichenanwendungen ist es ratsam, deine Umgebung richtig einzurichten, da du dadurch viel Zeit sparst. Wenn du deine Erfahrung in dem Arbeitsbereich Draft personalisieren möchtest, kannst du dies ganz einfach tun, indem du verschiedene Einstellungen im Draft-Einstellungsfenster anpasst, indem du zu **Bearbeiten → Einstellungen → Draft** gehst. In dieser Übung werden wir jedoch so vorgehen, als ob diese Einstellungen auf deinem Standardwerten belassen würden.

![](images/FreeCAD_DraftPreferences.png )

-   Mit dem Draft Einstellungen Paneel in FreeCAD kannst du verschiedene Aspekte deiner 2D-Zeichenumgebung anpassen. In den **Allgemeinen Einstellungen** kannst du die Standardarbeitsebene definieren, die Dezimalgenauigkeit anpassen und die Standardlinienbreite, -art und -farbe für Objekte festlegen. Im Abschnitt **Raster und Einrasten** kannst du die Rastersichtbarkeit und den Abstand und die Einrastmodi steuern, was eine präzise Ausrichtung und Positionierung von Elementen ermöglicht. Mit den Optionen für den **Visuellen Stil** kannst du das Erscheinungsbild von Objekten und des Rasters anpassen, einschließlich Linien- und Füllfarben. In **Text und Abmessungen** kannst du die Standardtextgröße, -schriftart und -farbe für Anmerkungen konfigurieren und so die Übersichtlichkeit technischer Zeichnungen gewährleisten.

![](images/Draft_toolbars.png )

-   Alle Einrast-Schaltflächen zu setzen ist bequem, es macht aber auch das Zeichnen langsamer, weil mehr Berechnungen durchgeführt werden, während du den Mauszeiger bewegst. Es ist oftmals besser, nur die zu setzen, die du tatsächlich benötigst.

-   Beginnen wir damit, den **Konstruktionsmodus** einzuschalten, der es uns ermöglicht, einige Richtlinien zu zeichnen, auf denen wir unsere endgültige Geometrie zeichnen werden. Du kannst dies tun, indem du auf den Befehl <img alt="" src=images/Draft_ToggleConstructionMode.svg  style="width:24px;"> [Konstruktionsmodus umschalten](Draft_ToggleConstructionMode/de.md) klickst.
-   Wenn du möchtest, kannst du die Arbeitsebene auf XY einstellen. Dadurch wird die Arbeitsebene gesperrt und sichergestellt, dass sie auf der XY-Ebene bleibt, unabhängig davon, wie du die Ansicht änderst. Wenn du dies nicht tun möchtest, passt sich die Arbeitsebene automatisch an die aktuelle Ansicht an. Dies bedeutet, dass du sicherstellen musst, dass du dich in der Draufsicht befindest, wenn du auf der XY-Ebene (Bodenebene) zeichnen möchtest, um unbeabsichtigte Ausrichtungsänderungen zu vermeiden.

Jetzt können wir zum Arbeitsbereich [Part](Part_Workbench/de.md) wechseln und mit der Erstellung des ersten Tischbeins beginnen.

-   Drücke die Schaltfläche <img alt="" src=images/Draft_Rectangle.svg  style="width:24px;"> 
**Rechteck**
-   Zeichne ein 2 x 2 Meter großes Rechteck, beginnend bei Punkt (0,0,0), und lass die Z-Koordinate auf Null. Du kannst diesen gesamten Vorgang effizient mit der Tastatur abschließen, ohne die Maus zu benötigen. Gib einfach ein:
    -   **re**, **Enter**, **Enter**, **Enter**, 2m, **Enter**, 2m, **Enter**, 0 und **Enter**.

Dieser tastaturgesteuerte Arbeitsablauf beschleunigt das Zeichnen, insbesondere bei sich wiederholenden Aufgaben oder präzisen Eingaben, und ist daher ideal für Benutzer, die ihren Arbeitsablauf optimieren möchten. Du kannst die Tastenanschläge für jedes Objekt anzeigen, indem du mit der Maus über die entsprechende Schaltfläche fahrst.

-   Dupliziere dieses Rechteck um 15 cm nach innen. Verwende dazu das Werkzeug <img alt="" src=images/Draft_Offset.svg  style="width:16px;"> [Versetzen](Draft_Offset/de.md), schalte den Kopiermodus ein und gib einen Abstand von 15 cm ein:

![](images/Exercise_cabin_02.png )

-   Wir können dann mit dem Werkzeug <img alt="" src=images/Draft_Line.svg  style="width:16px;"> [Linie](Draft_Line/de.md) ein paar vertikale Linien zeichnen, um festzulegen, wo unsere Türen und Fenster platziert werden (beachte, dass das Kontrollkästchen „relativer" Modus für diesen Schritt deaktiviert sein sollte). Die Kreuzung dieser Linien mit unseren beiden Rechtecken ergibt nützliche Schnittpunkte, an denen wir unsere Wände ausrichten können. Zeichne die erste Linie, indem du die folgenden Punkte definierst:
    -   **P1** (15 cm, 1 m, 0) und **P2** (15 cm, 3 m, 0).
-   Wir werden diese Linie nun fünfmal duplizieren. Drücke auf das Werkzeug <img alt="" src=images/Draft_Move.svg  style="width:16px;"> [Verschieben](Draft_Move/de.md), während der Modus <img alt="" src=images/Draft_Clone.svg  style="width:16px;"> [Klonen](Draft_Clone/de.md) aktiviert ist. Stelle sicher, dass der **Relative Modus** aktiviert ist. Der Kopiermodus stellt sicher, dass jede Bewegung eine neue Linie erstellt, anstatt die ursprüngliche zu verschieben, während der Relativmodus es dir ermöglicht, Bewegungen basierend auf relativen Entfernungen zu definieren, was die Positionierung erleichtert, ohne dass genaue Koordinaten berechnet werden müssen. Beginne mit der Auswahl der ursprünglichen Linie und starte den Verschiebungsvorgang, indem du einen beliebigen Startpunkt auswählst, z. B. (0,0,0). Führe nach jeder Bewegung den nächsten Vorgang auf der neu erstellten Linie aus, sodass jede Kopie auf der vorherigen aufbaut. Definiere die relativen Endpunkte für jede neue Linie
    -   line001: x: 10 cm
    -   line002: x: 120 cm
    -   line003: x: -55 cm, y: -2 m
    -   line004: x: 80 cm
    -   line005: x: 15 cm

![](images/Exercise_cabin_03.jpg )

-   Das ist alles, was wir jetzt brauchen, damit wir den Konstruktionsmodus ausschalten können. Überprüfe, ob die gesamte Konstruktionsgeometrie in einer „Konstruktions"-Gruppe platziert wurde, sodass sie später ganz einfach ausgeblendet oder sogar vollständig gelöscht werden kann.
-   Zeichnen wir nun unsere beiden Wandstücke mit dem Werkzeug <img alt="" src=images/Draft_Wire.svg  style="width:16px;"> [Linienzug](Draft_Wire/de.md). Stelle sicher, dass das <img alt="" src=images/Draft_Snap_Intersection.svg  style="width:16px;"> [Einrasten auf Schnittpunkt](Draft_Snap/de.md) aktiviert ist, da wir an den Schnittpunkten unserer Linien und Rechtecke einrasten müssen. Zeichne zwei Linienzüge wie folgt, indem du auf alle Punkte ihrer Konturen klickst. Um sie zu schließen, klick entweder erneut auf den ersten Punkt oder drücke die Schaltfläche **Schließen**:

![](images/Exercise_cabin_04.jpg )

-   Wir können den Wänden ein schönes Schraffurmuster geben. Wähle beide Wände aus, stelle sicher, dass ihre Eigenschaft **Fläche erstellen** (auf der Registerkarte Daten) auf **WAHR** eingestellt ist, stelle dann ihre Eigenschaft **Muster** (auf der Registerkarte Ansicht) auf **Einfach** und ihre **Mustergröße** nach deinen Wünschen ein, zum Beispiel **0,005**.

![](images/Draft_Pattern.png )

-   Wir können die Konstruktionsgeometrie jetzt ausblenden, indem wir mit der rechten Maustaste auf die Gruppe „Konstruktion" klicken und „Auswahl ausblenden" wählen.
-   Lass uns jetzt die Fenster und Türen zeichnen. Stelle sicher, dass der <img alt="" src=images/Draft_Snap_Midpoint.svg  style="width:16px;"> [Einrasten auf Mittelpunkt](Draft_Snap/de.md) aktiviert ist, und zeichne sechs Linien, wie unten gezeigt:

![](images/Exercise_cabin_06.jpg )

-   Wir ändern jetzt die Türlinie, um ein Symbol für eine geöffnete Tür zu erstellen. Beginne, indem du die Linie mit dem Werkzeug <img alt="" src=images/Draft_Rotate.svg  style="width:16px;"> [Drehen](Draft_Rotate/de.md) drehst. Klicke auf den Endpunkt der Linie als Drehmittelpunkt, gib ihm einen Startwinkel von **0** und einen Endwinkel von **-90**.
-   Erstelle dann den Öffnungsbogen mit dem Werkzeug <img alt="" src=images/Draft_Arc.svg  style="width:16px;"> [Kreisbogen](Draft_Arc/de.md). Wähle denselben Punkt als Drehmittelpunkt, den wir im vorherigen Schritt als Mittelpunkt verwendet haben, klicke auf den anderen Punkt der Linie, um den Radius anzugeben, und dann auf die Start- und Endpunkte wie folgt:

![](images/Exercise_cabin_07.jpg )

-   Wir können jetzt anfangen, Möbel zu platzieren. Lass uns zunächst eine Theke platzieren, indem wir ein Rechteck von der oberen linken Innenecke aus zeichnen und ihm eine Breite von 170 cm und eine Höhe von -60 cm geben. Im Bild unten ist die Eigenschaft **Transparenz** des Rechtecks ​​auf 80 % eingestellt, um ihm ein schönes Möbelaussehen zu verleihen.
-   Fügen wir dann eine Spüle und ein Kochfeld hinzu. Das Zeichnen dieser Art von Symbolen von Hand kann sehr mühsam sein und sie sind normalerweise leicht im Internet zu finden, beispielsweise unter <http://www.cad-blocks.net>. Im Abschnitt **Downloads** weiter unten haben wir der Einfachheit halber eine Spüle und ein Kochfeld aus diesem Projekt herausgelöst und als DXF-Dateien gespeichert. Du kannst diese beiden Dateien herunterladen, indem du die unten stehenden Links besuchst, mit der rechten Maustaste auf die Schaltfläche **Raw** klickst und dann **Speichern unter** wählst.
-   Das Einfügen einer DXF-Datei in ein geöffnetes FreeCAD-Dokument kann entweder durch Auswahl der Menüoption **Datei → Importieren** oder durch Ziehen und Ablegen der DXF-Datei aus deinem Datei-Explorer in das FreeCAD-Fenster erfolgen. Der Inhalt der DXF-Dateien wird möglicherweise nicht genau in der Mitte deiner aktuellen Ansicht angezeigt, je nachdem, wo sie sich in der DXF-Datei befanden. Du kannst das Menü **Ansicht → Standardansichten → Alles anpassen** verwenden, um herauszuzoomen und die importierten Objekte zu finden. Füge die beiden DXF-Dateien ein und verschiebe sie an eine geeignete Stelle auf der Tischplatte:

![](images/Exercise_cabin_08.jpg )

-   Wir können jetzt mit dem Werkzeug <img alt="" src=images/Draft_Dimension.svg  style="width:16px;"> [Abmessung](Draft_Dimension/de.md) einige Maße platzieren. Um ein Maß zu erstellen, wähle zunächst drei Punkte aus: Der erste Punkt legt den Startpunkt der Messung fest, der zweite Punkt definiert den Endpunkt und der dritte Punkt bestimmt, wo die Maßlinie und der Text platziert werden. Indem du diese Punkte sorgfältig anklickst, stellst du sicher, dass das Maß den Abstand zwischen den beiden ausgewählten Punkten genau wiedergibt. Wenn du das Maß perfekt horizontal oder vertikal halten möchtest, auch wenn Start- und Endpunkt nicht ausgerichtet sind, halte die **Umschalt**-Taste gedrückt, während du auf den zweiten Punkt klickst. Dadurch wird das Maß in der gewünschten Ausrichtung fixiert. Du kannst das Maß weiter verfeinern, indem du Eigenschaften wie Textgröße, Genauigkeit und Farbe im Eigenschaften-Fenster anpasst und so sicherstellen, dass die Maße den visuellen und technischen Standards deines Projekts entspricht.
-   Du kannst die Position eines Maßtextes ändern, indem du in der Strukturansicht auf das Maß doppelklickst. Ein Kontrollpunkt ermöglicht dir, den Text grafisch zu verschieben. In unserer Übung wurden die „0,15"-Texte zur besseren Übersichtlichkeit verschoben.
-   Du kannst den Inhalt des Maßtexts ändern, indem du die Eigenschaft **Override** bearbeitest. In unserem Beispiel wurden die Texte der Tür- und Fenstermaße bearbeitet, um ihre Höhen anzugeben:

![](images/Exercise_cabin_09.jpg )

-   Fügen wir mit dem Werkzeug <img alt="" src=images/Draft_Text.svg  style="width:16px;"> [Text](Draft_Text/de.md) einige Beschreibungstexte hinzu. Klicke auf einen Punkt, um den Text zu positionieren, und gib dann die Textzeilen ein. Drücke nach jeder Zeile die Eingabetaste. Drücke zum Beenden zweimal die Eingabetaste.
-   Die Hinweislinien, die die Texte mit dem von dir beschriebenen Element verbinden, werden einfach mit dem Werkzeug Linienzug erstellt. Zeichne Linienzüge, beginnend an der Textposition, zu der zu beschreibenden Stelle. Sobald dies erledigt ist, kannst du am Ende der Linienzüge einen Punkt oder Pfeil hinzufügen, indem du deren Eigenschaft **End Arrow** auf **TRUE** setzt.

![](images/Exercise_cabin_10.jpg )

-   Unsere Zeichnung ist nun fertig! Angesichts der Anzahl der Objekte im Entwurf ist es eine gute Idee, etwas aufzuräumen und neu zu strukturieren, bevor wir ihn als abgeschlossen betrachten. Wenn du alles in klare, logische Gruppen einteilst, bleibt das Projekt nicht nur gut strukturiert, sondern es wird auch für andere wesentlich einfacher, sich in der Datei zurechtzufinden und sie zu verstehen. Indem du verwandte Elemente -- wie Möbel, Geräte oder architektonische Merkmale -- gruppierst, kannst du das Layout vereinfachen und die Übersichtlichkeit des Entwurfs verbessern. Dadurch werden auch zukünftige Änderungen oder Anpassungen viel einfacher handhabbar, insbesondere wenn das Projekt geteilt oder gemeinsam bearbeitet werden muss. Darüber hinaus sorgt eine saubere Struktur dafür, dass jeder, der die Zeichnung überprüft, bestimmte Elemente schnell finden kann, ohne einen überfüllten Arbeitsbereich durchsuchen zu müssen, was letztendlich zu einem professionelleren und ausgefeilteren Endprodukt beiträgt. Wenn du dir jetzt die zusätzliche Zeit zum Ordnen nimmst, kannst du später viel Zeit und Mühe sparen.:

![](images/Draft_Organised.png )

-   Wir können unsere Arbeit nun ausdrucken, indem wir sie auf ein Zeichenblatt legen, was wir später in diesem Handbuch zeigen werden, oder unsere Zeichnung direkt in andere CAD-Anwendungen exportieren, indem wir sie in eine DXF-Datei exportieren. Wähle einfach unsere Gruppe „Grundriss", wähle das Menü **Datei → Exportieren** und wähle das Format **Autodesk DXF**. Die Datei kann dann in jeder anderen 2D-CAD-Anwendung wie [LibreCAD](http://www.librecad.org) geöffnet werden. Abhängig von den Konfigurationen der einzelnen Anwendungen stellst du möglicherweise einige Unterschiede fest.

![](images/Exercise_cabin_12.jpg )

-   Der wichtigste Aspekt des Arbeitsbereichs Draft ist jedoch, dass die von dir erstellte 2D-Geometrie als Grundlage für die Erstellung von 3D-Objekten dienen kann. Du kannst diese Formen ganz einfach mit dem Werkzeug <img alt="" src=images/Part_Extrude.svg  style="width:16px;"> [Extrudieren](Part_Extrude/de.md) des Arbeitsbereichs [Part](Part_Workbench/de.md) in 3D extrudieren. Wenn du lieber im Arbeitsbereich Draft bleiben möchtest, kannst du alternativ das Werkzeug <img alt="" src=images/Draft_Trimex.svg  style="width:16px;"> [Trimex](Draft_Trimex/de.md) verwenden, das Trimm-, Verlängerungs- und Extrusionsfunktionen kombiniert. Das Trimex-Werkzeug führt im Grunde eine Part-Extrusion im Hintergrund durch, tut dies jedoch „auf die Draft-Art", sodass du die Extrusionslänge visuell anzeigen und einrasten kannst, was dir mehr Kontrolle und Präzision gibt, wenn du direkt in Ihrer Zeichenumgebung arbeitest. Diese Flexibilität macht den Übergang von 2D zu 3D nahtlos und intuitiv, insbesondere für diejenigen, die mit 2D-Arbeitsabläufen vertraut sind, und bietet dennoch erweiterte 3D-Modellierungsfunktionen.
-   Durch Drücken der Schaltfläche <img alt="" src=images/Draft_SelectPlane.svg  style="width:16px;"> [Arbeitsebene](Draft_SelectPlane/de.md), nachdem du eine Fläche eines Objekts ausgewählt hast, kannst du die Arbeitsebene auch an einer beliebigen Stelle platzieren und so Draft-Objekte in verschiedenen Ebenen zeichnen, beispielsweise oben auf den Wänden. Diese können dann extrudiert werden, um andere 3D-Festkörper zu bilden. Experimentiere damit, die Arbeitsebene auf einer der oberen Flächen der Wände zu platzieren, und zeichne dann dort oben einige Rechtecke.

![](images/Exercise_cabin_13.jpg )

-   Alle Arten von Öffnungen können auch ganz einfach erstellt werden, indem du Draft-Objekte auf die Flächen von Wänden zeichnest, diese dann extrudierst und sie dann mit den Booleschen Werkzeugen des Arbeitsbereichs Part von einem anderen Festkörper subtrahierst, wie wir im vorherigen Kapitel gesehen haben.

Grundsätzlich bietet der Arbeitsbereich Draft einen grafischeren und intuitiveren Ansatz zum Erstellen grundlegender Vorgänge, ähnlich denen im Arbeitsbereich Part. Im Arbeitsbereich Part müssen beim Positionieren von Objekten häufig Parameter wie die Platzierungswerte (für Position, Drehung usw.) manuell angepasst werden, was dir eine präzise Kontrolle gibt, sich aber manchmal weniger intuitiv anfühlen kann, insbesondere bei schnellen Bearbeitungen. Im Gegensatz dazu kannst du im Arbeitsbereich Draft dieselben Vorgänge visuell auf dem Bildschirm ausführen, wodurch das Verschieben, Drehen und Bearbeiten von Objekten direkt am Arbeitsplatz mit Einrastwerkzeugen und relativen Positionierungsoptionen einfacher wird.

In diesem Unterschied ergänzen sich die Arbeitsbereiche. Der Arbeitsbereich Draft ist ideal für schnelles, interaktives Design, da du Objekte zeichnen und positionieren kannst, ohne ständig präzise numerische Werte eingeben zu müssen. Der Arbeitsbereich Part hingegen bietet eine detailliertere, parametrische Kontrolle über Objekteigenschaften und ist daher besser für hochpräzise Anpassungen geeignet, insbesondere bei Konstruktions- oder technischen Designprojekten.

Das Schöne an FreeCAD ist, dass du dich nicht zwischen dem einen oder dem anderen entscheiden musst. Du kannst [benutzerdefinierte Symbolleisten](Interface_Customization/de.md) erstellen, indem du Werkzeuge aus den Arbeitsbereichen Draft und Part kombinierst. So hast du die Flexibilität, je nach Bedarf zwischen grafischen und parametrischen Methoden zu wechseln. So kannst du das Beste aus beiden Welten nutzen -- schnelle Bildschirmanpassungen aus dem Arbeitsbereich Draft und die Präzision des Arbeitsbereichs Part -- je nach den Anforderungen deines Projekts. Darüber hinaus kannst du deinen Arbeitsablauf durch die Verwendung von Tastaturkürzeln und benutzerdefinierten Symbolleisten beschleunigen, sodass du problemlos zwischen verschiedenen Vorgängen wechseln kannst, ohne deinen Entwurfsprozess zu unterbrechen.



## Herunterladen

-   Die während dieser Übung erstellte Datei: <https://github.com/yorikvanhavre/FreeCAD-manual/blob/master/files/cabin.FCStd>
-   Die DXF-Datei der Spüle: <https://github.com/yorikvanhavre/FreeCAD-manual/blob/master/files/sink.dxf>
-   Die DXF-Datei des Kochfelds: <https://github.com/yorikvanhavre/FreeCAD-manual/blob/master/files/cooktop.dxf>
-   Die während dieser Übung erstellte endgültige DXF-Datei: <https://github.com/yorikvanhavre/FreeCAD-manual/blob/master/files/cabin.dxf>



## Verwandt

-   [Arbeitsbereich Draft](Draft_Workbench/de.md)
-   [Einrasten](Draft_Snap/de.md)
-   [Die Draft-Arbeitsebene](Draft_SelectPlane/de.md)



---
⏵ [documentation index](../README.md) > [Tutorials](Category_Tutorials.md) > [Draft](Category_Draft.md) > Manual:Traditional 2D drafting/de
