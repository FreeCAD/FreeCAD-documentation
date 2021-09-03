


{{TutorialInfo/de
|Topic= Modellierung eines Architektur Panels
|Level= Anfänger
|Time= 60 Minuten
|Author= Yorik
|FCVersion=
|Files=
}}

Dies ist ein Mehrfach-Posting eines [Tutorials](http://opensourceecology.org/wiki/FreeCAD_Architecture_Tutorial), das zuerst auf [Open-Source Ecology](http://opensourceecology.org) erschienen ist.

## Präsentation von FreeCAD 

<img alt="" src=images/Arch_panel_tutorial_01.jpg  style="width:800px;">

FreeCAD ist ein parametrisches 3D Modellierungsprogramm. Parametrische Modellierung erlaubt es Dir, einfach Dein Design zu modifizieren, indem Du in deiner Modellierungshistorie zurückgehst und die Parameter änderst. FreeCAD ist Opensource (LGPL Lizenz) und sehr modular, erlaubt dadurch umfangreiche Erweiterung und Anpassung, dank der intensiven Nutzung der Python Programmiersprache.

-   FreeCAD Webseite: <http://www.freecadweb.org/>
-   FreeCAD Dokumentations Wiki: <http://www.freecadweb.org/wiki/index.php?title=Main_Page/de>
-   FreeCAD Arbeitsbereiche: <http://www.freecadweb.org/wiki/index.php?title=Workbench_Concept/de>
-   FreeCAD Forum: <http://forum.freecadweb.org/>
-   Erste Schritte mit FreeCAD: <http://www.freecadweb.org/wiki/index.php?title=Getting_started/de>
-   Architektur Tutorium: <http://www.freecadweb.org/wiki/index.php?title=Arch_tutorial/de>

## FreeCAD installieren 

Du hast die Möglichkeit, die letzte stabile Version (im Juli 2018 die Version 0.16) oder eine Entwicklerversion (momentan 0.17) zu installieren. Tatsächlich sind Entwicklerversionen normalerweise ziemlich stabil, und Du wirst ernsthaft ermuntert, eine Entwicklerversion auszuprobieren, solange Du keinen bestimmten Grund hast, es nicht zu tun. Wenn Du Entwicklerversionen selbst herunterlädst, dann solltest Du von Zeit zu Zeit nachsehen und neu installieren/aktualisieren, um von den Verbesserungen zu profitieren, weil die FreeCAD Entwicklung ziemlich zügig vorangeht.

-   Auf Windows: Lade die aktuellste Version für Deine Windowsversion (32- oder 64-Bit) von [1](https://github.com/FreeCAD/FreeCAD/releases). Doppelklicke zur Installation der Datei (Anm. d. Ü.: 0.16 ist die letzte Version für XP).
-   Auf Mac OS: Lade die aktuellste Version von [2](https://github.com/FreeCAD/FreeCAD/releases). Doppelklicke zur Installation der Datei.
-   Auf Ubuntu: Die von Ubuntu bereitgestellte Version ist normalerweise veraltet, daher raten wir, stattdessen das von der FreeCAD Gemeinschaft gewartetet PPA zu verwenden.
-   Auf anderen Plattformen: In den am meisten verwendeten Linux Distriutionen (Debian, Fedora, etc.) ist FreeCAD in den offiziellen Software Repositorien enthalten. Es mag allerdings nicht immer die aktuellste Version sein. Falls die von Dir benötigte Version nicht verfügbar ist, ist Deine einzige Option, FreeCAD selbst zu kompilieren (Anweisungen auf der FreeCAD Webseite)

## Zusätzliche optionale Inhalte 

-   IFC Import/Export aktivieren: Um Projekte ins/vom IFC Dateiformat zu exportieren bzw. importieren, verlässt sich FreeCAD auf den ifcOpenShell Importeur, den Du separat von [3](http://ifcopenshell.org/python.html) herunterladen musst. Achte darauf, eine Python 2.7-basierte Version zu verwenden, das ist die gleiche für FreeCAD verwendete Python Version.
-   Drawing dimensioning workbench: Ein zusätzlicher Arbeitsbereich für FreeCad, der viele zweckmäßige Werkzeuge zum Hinzufügen von Bemaßungen und Anmerkungen zu FreeCADs 2D Zeichenblättern bietet: <https://github.com/hamish2014/FreeCAD_drawing_dimensioning> (Installationshinweise auf der Webseite)
-   Assembly2 workbench: Ein zusätzlicher Arbeitsbereich für FreeCAD, der eine Reihe von wichtigen Baugruppen Werkzeugen bietet: <https://github.com/hamish2014/FreeCAD_assembly2> (Installationshinweise auf der Webseite)

## Schnellstarthinweise

Die Sammlung der im FreeCAD Wiki verfügbaren Tutorien ist immer noch sehr spärlich. Allerdings nutzen viele Mitglieder der FreeCAD Gemeinschaft youtube, um Video Tutorien zu veröffentlichen. Achte darauf, dass Du FreeCAD-bezogenen Inhalt auf youtube suchst, das ist sicherlich die beste Quelle für Lernmaterial.

FreeCAD ist eine sehr technische Anwendung und die Lernkurve kann sehr steil sein. Vertraue auf Tutorien und das Dokumentations Wiki und zögere nicht, im Forum Fragen zu stellen, wenn Du ein bestimmtes Problem hast. Auf klar gestellte Fragen gibt es normalerweise sehr schnelle und umfangreiche Antworten.

### Eine sehr grobe Liste von Dingen, die Du wissen musst 

-   Die FreeCAD Oberfläche ist in Arbeitsbereiche unterteilt. Arbeitsbereiche sind einfach Werkzeugsammlungen (Symbolleisten von Knöpfen und Menüs), die zusammengefasst sind, normalerweise für eine bestimmte Aufgabe. Wenn Du zu einem anderen Arbeitsbereich wechselst, zeigt Dir die Oberfläche die Werkzeuge dieses Arbeitsbereichs. Aber der Inhalt Deines 3D Dokuments ändert sich nicht. Du arbeitest immer noch am gleichen Dokument und an den gleichen Objekten.

-   FreeCAD ist immer noch in Entwicklung, es gibt immer noch viele Softwarefehler, und die Anwendung könnte manchmal abstürzen. Sichere oft und aktiviere Sicherungsdateien in Bearbeiten → Einstellungen → Dokument

-   Die meisten FreeCAD Objekte sind parametrisch. Das bedeutet, dass ihre Geometrien automatisch aus einer Reihe von Parametern erstellt werden. Diese Parameter sind immer in der Eigenschaften Ansicht änderbar. Sie sind immer unterteilt in die Parameter, die die Geometrie selbst beeinflussen (Datenreiter) und die Parameter, die nur die Anzeige des Objekts (Ansichtsreiter) beeinflussen. Allerdings sind durch andere Anwendungen erzeugte und in FreeCAD importierte Objekte nicht durch Parameter definiert und deshalb nicht änderbar.

-   Einige Arbeitsbereiche (PartDesign und Arch) sind gemacht, um nur mit Volumenkörpern arbeiten, und sie werden die Arbeit an Objekten verweigern, die keine Volumenkörper sind. Eine gute Faustregel ist, möglichst nur mit Volumenkörpern zu arbeiten.

-   Obwohl FreeCAD Netzobjekte importieren und mit ihnen arbeiten kann (Netz Arbeitsbereich), ist es vorrangig gedacht, mit einem fortgeschritteneren Objekttyp namens brep zu arbeiten, der von den meisten Arbeitsbereichen genutzt wird (Part, PartDesign, Draft, Sketcher, Arch). Wenn Netz-basierte Dateien (.dae, .orb, .stl\...) importiert werden, musst du diese Objekte in der Regel erst in brep konvertieren, bevor du mit ihnen etwas Interessantes machen kannst. Volumenkörper-basierte Dateiformate (.step, .iges) erzeugen beim Import in FreeCAD direkt brep Objekte. 2D Formate (.dxf, .svg) erzeugen ebenfalls brep Inhalte.

-   FreeCAD hat verschiedene Wege oder Arten, um die Maustasten zu nutzen. Diese Arten können in den Einstellungen gesetzt werden oder ändern sich während der Laufzeit durch Rechtsklicken auf den Hintergrund der 3D Ansicht. Sie sind beschrieben auf <http://www.freecadweb.org/wiki/index.php?title=Mouse_Model>. Die am besten geeigneten Modi für CAD Arbeiten sind CAD oder Gesten.

## Übung: Eine Dachhaut modellieren 

Um einen typischen Arbeitsablauf in FreeCAD zu zeigen, modellieren wir ein Dachpaneel wie auf <http://opensourceecology.org/wiki/MicroHouse_4_Roof_-_Module_-_Build_Instructions> beschrieben. Dazu beginnen wir mit dem Zeichnen der verschiedenen Teile in einer 2D beschränkten Skizze, dann nutzen wir das spezielle Arch Fensterobjekt, das in der Lage ist, komplexe 3D Objekte aus einer 2D Skizze zu erstellen, die die Konturen mehrerer Teile enthält. Da wir schließlich kein Fenster, sondern ein Dachpaneel benötigen, werden wir unser Fensterobjekt einfach in einen anderen Arch Typ konvertieren.

### 1. Öffne FreeCAD, dann setze die bevorzugten Einheiten auf \"imperial\" 

Im Menü Bearbeiten → Einstellungen → Allgemein → Einheiten → Einheitsystem (Anm. d. Ü.: Um Unklarheiten zu vermeiden, wurde im Text die Einheit \"in\" durch \"Inch\" ersetzt).

### 2. Wechsel\' zum Sketcher-Arbeitsbereich und erstelle eine neue Skizze in der XY-Ebene 

![](images/Arch_panel_tutorial_02.jpg )

Solange es keinen bestimmten Grund gibt, es nicht zu tun, wirst Du Deine 2D-Skizzen normalerweise immer auf dem Boden beginnen, um den Ursprung (0,0) herum. Dann wird das daraus generierte 3D-Objekt in Position gedreht/rotiert.

### 3. Zeichne zwei Rechtecke. Setze auf jedem eine vertikale Beschränkung von 16 feet und eine horizontale Beschränkung von 2 inches 

![](images/Arch_panel_tutorial_03.jpg )

Mach\' Dir beim Zeichnen keine Gedanken über die Abmessungen der Teile, denn die Beschränkungen werden die Größen entsprechend anpassen. Um eine (horizontale oder vertikale) Beschränkung hinzuzufügen, kannst Du entweder eine Linie oder (mit gedrückter **Strg**) zwei Punkte auswählen.

### 4. Sobald Deine beiden Rechtecke die richtige Größe haben, setze eine vertikale Beschränkung von 0 zwischen ihre Eckpunkte und eine horizontale Beschränkung von 4 feet 

![](images/Arch_panel_tutorial_04.jpg )

Dies stellt sicher, dass unsere beiden Rechtecke richtig positioniert sind in Relation zueinander.

### 5. Füge zwei zusätzliche 2 inch x 6 inch Teile hinzu 

![](images/Arch_panel_tutorial_05.jpg )

Füge zwei weitere Rechtecke hinzu und wiederhole den Vorgang. Beachte, dass wir im obigen Beispiel die Länge der Teile nicht angegeben, sondern eine Längenbeschränkung zwischen den Endpunkten und den langen vertikalen Teilen getroffen und eine schmale Lücke von 0,05 Inch zwischen ihnen gelassen haben. Der Grund dafür ist, dass FreeCAD die Vierecke (loops) falsch ermitteln könnte, wenn sich die Rechtecke berühren würden, und wir dadurch merkwürdige Ergebnisse beim Arch-Fenster-Werkzeug erhalten würden. Dieser kleine Trick stellt sicher, dass jedes Rechteck vom Arch-Fenster-Werkzeug als ein unabhängiges Viereck erkannt wird.

### 6. Die Eckverstärkungsstücke hinzufügen 

![](images/Arch_panel_tutorial_06.jpg )

Das Gleiche nochmal. Mach\' sie 6 Inch breit und mit einem Abstand von 0,05 Inch zu den anderen Rechtecken.

### 7. Zeichne sieben dazwischenliegende Verstärkungsteile mit einer Breite von 2 Inch und setze eine Festlegung bei 0,05 Inch von den linken und rechten Endpunkten der vertikalen Rechtecke (oder bei 0 Inch der Endpunkte der anderen horizontalen Rechtecke) 

![](images/Arch_panel_tutorial_07.jpg )

Abhängig von Deinem System kann es sein, dass FreeCAD beginnt, neue Beschränkungen langsamer zu verarbeiten. Dies ist der Nachteil, wenn man beschränkte Objekte benutzt, dass sie schnell eine Menge von Systemressourcen schlucken. Du musst immer entscheiden, ob Du sie wirklich brauchst. Du kannst auch Beschränkungen löschen, wenn sie nicht mehr benötigt werden. Diese Abmessungen werden nicht mehr festgesetzt, aber solange du die Teile nicht verschiebst, werden sie sich nicht ändern. Bei Bedarf kannst du auch später immer Beschränkungen wieder hinzufügen.

### 8. Berechne den Abstand zwischen den sieben Verstärkungsteilen und setze vertikale Beschränkungen zwischen sie 

In unseren Fall ist die Gesamtlänge 192 inch, minus die beiden Endstücke (2 x 2 inch) und die beiden Eckverstärkungen (2 x 6 inch), also 192 - (4 + 12) = 176. Abzüglich der sieben Verstärkungsteile (7 x 2 inch) bleiben 162. Dividiert durch 8 ergibt das den Platz zwischen den Verstärkungsteilen: 20,25 inch.

![](images/Arch_panel_tutorial_08.jpg )

### 9. Eine vollständig beschränkte Skizze erreichen 

Im rechten Paneel (Aufgabenreiter in der Combo Ansicht \--\> Löser Meldungen) kannst Du die Meldung \"\... 2 Freiheitsgrade\" sehen. Das bedeutet, dass unsere Skizze nicht vollständig beschränkt ist (es gibt noch zwei \"Wege\", sie zu verformen). Denn auch wenn sich jetzt kein Teil davon im Verhältnis zu den anderen bewegen kann, kann sich die ganze Skizze immer noch vertikal und horizontal bewegen. Um dies zu verhindern, können wir einfach einen seiner Eckpunkte nehmen, den Ursprungspunkt des Gitters wählen (wo sich die grüne und die rote Achse schneiden) und die Schaltfläche Punktbeschränkung drücken. Dadurch wird unsere Skizze grün, d.h. sie ist vollständig beschränkt, kein Teil davon kann sich mehr bewegen.

![](images/Arch_panel_tutorial_09.jpg )

Dies ist tatsächlich nicht absolut notwendig. Es ist aber immer besser, die exakte Position der Objekte im Auge zu behalten (wir sind nun sicher, dass unsere Ecke am Punkt (0,0) ist). Falls später etwas schiefgeht oder wir die Position eines Objekts herausfinden müssen, das auf dieser Skizze basiert, ist das nützlich.

Wir können jetzt die \"Schliessen\" Taste drücken und unsere Basiskizze ist erstellt:

![](images/Arch_panel_tutorial_10.jpg )

### 10. Wechsle zum Arch Arbeitsbereich und drücke, wenn die Skizze ausgewählt ist, die \"Fenster\" Schaltfläche 

Unsere Skizze ist nun verschwunden, und eines ihrer Rechtecke ist leicht zu einem massiven Stück extrudiert worden.:

![](images/Arch_panel_tutorial_11.jpg )

Obwohl das falsch aussieht, liegt das einfach daran, dass das Arch Fenster Werkzeug ein Standardteil aus dem größten Viereck gemacht hat, das es in der Basisskizze finden konnte. Wir werden das bald korrigieren. Beachte, dass die Skizze nicht verschwunden ist, sondern einfach ausgeschaltet und vom neuen Elternobjekt \"geschluckt\" wurde. Du kannst es weiterhin in der Baumansicht finden, indem Du das Fenster Objekt expandierst und die Sichtbarkeit durch Drücken der Leertaste ein-/ausschaltest.

### 11. Bearbeite die Fensterkomponenten, durch doppelklicken in der Baumansicht 

![](images/Arch_panel_tutorial_12.jpg )

Durch Doppelklicken des Fensters wird die Skizze wieder sichtbar und wir können ihr Aussehen ändern: Auf der linken Seite eine Liste der Vierecke in der Basisskizze, auf der rechten die darauf erzeugten Volumenkörper.

Beginne mit dem Entfernen des \"Standard\" Stücks.

Dann wähle das erste Viereck (Wire0). Es wird in der 3D-Ansicht hervorgehoben. Drücke den \"Hinzufüge\"-Button, um ein neues Teil daraus zu erzeugen. Gib ihm einen Namen, stell\' sicher, dass der richtige Draht gesetzt ist und setze die Dicke auf 6 Inch. Der Z-Abstand sollte bei 0 bleiben, weil wir es \"auf dem Boden\" platzieren wollen.

Der \"Typ\" Wert wird verwendet, um dem Fenster Materialien zuzuordnen (noch nicht implementiert), so dass du derzeit bei \"Rahmen\" bleiben kannst.

![](images/Arch_panel_tutorial_13.jpg )

Dann drücke \"Erstelle/aktualisiere Komponente\". Manchmal errät FreeCAD die Richtung der Extrusion nicht richtig, so dass Du Deine Komponente ändern und den 6 Inch-Wert auf -6 setzen musst.

Wiederhole das für alle benötigen Teile:

![](images/Arch_panel_tutorial_14.jpg )

Beim Schließen des Edit-Panels erhalten wir das obige Objekt. Beachte, dass standardmäßig Fenster-Objekte semitransparent dargestellt werden. Da dies tatsächlich kein Fenster wird, können wir das durch Ändern des Transparency-Wertes auf 0 in den Ansicht-Eigenschaften abstellen.

### 12. Die Verkleidung hinzufügen 

Jetzt haben wir unseren Rahmen, aber nicht das Basis-Panel selbst. Um das zu erledigen, ist der beste Weg, unsere Basisskizze zu öffnen und ein neues Rechteck hinzuzufügen. Denke allerdings daran, keine Ecke dieses Rechtecks mit einer Ecke anderer Rechtecke übereinstimmen zu lassen, um unser Fenster-Objekt nicht durcheinander zu bringen, was es erfordern könnte, die ganze Reihe von Komponenten erneut zu erstellen, wenn sich die Reihenfolge der Vierecke ändern würde.

Wir können daher dieses neue Rechteck 0,05 Inch innerhalb des Umkreises festlegen. Das erfordert, dass wir vier neue Beschränkungen erstellen.

Wir können dann unser Fenster erneut ändern und neue Komponenten hinzufügen. Wir sehen, dass ein neuer Draht gefunden wurde. Dieses Mal werden wir ihn nutzen, um ein 8mm Polycarbonat-Panel (beachte, dass Du ohne Probleme verschiedene Einheiten in FreeCAD mischen kannst und \"8mm\" als Dicke angeben kannst, selbst wenn Du in Inch arbeitest). Wir werden ihm außerdem einen Z-Abstand von 0,05 Inch geben, so dass er einen geringen Abstand vom Rahmen hat, nur damit alle Teile unseres Objekts den gleichen Abstand haben.

![](images/Arch_panel_tutorial_15.jpg )

Wir können nun eine weitere Komponente erstellen, die ebenfalls auf dem gleichen Draht basiert, um ein weiteres Panel auf unserem Rahmen zu erzeugen. Dieses Mal geben wir ihm einen Z-Abstand von 6,05 Inch. Unser Panel ist endlich fertig:

![](images/Arch_panel_tutorial_16.jpg )

### 13. Das Fenster in einen anderen Typ von Arch Komponente ändern 

Das ist zu diesem Zeitpunkt nicht wirklich nötig, aber es könnte später wichtig werden, wenn wir exportieren oder mit anderen konstruktions-orientierten Anwendungen arbeiten, z.B. via IFC, denn dann wollen wir nicht, dass unser Panel als ein Fenster erkannt wird.

Der Arch-Arbeitsbereich von FreeCAD bietet einen einfachen Weg, damit umzugehen, dadurch dass jeder Objekttyp immer zu einem anderen werden kann, indem er die Basis eines anderen Typ ist. In diesem Fall wird unser Fenster zu einem Panel-Objekt, einfach durch auswählen des Fensters und drücken des Panel-Werkzeugs.

![](images/Arch_panel_tutorial_17.jpg )

Beachte, dass sich die Farbe des entstehenden Panels geändert hat, weil die Materialunterstützung in FreeCAD und im Arch-Modul noch unvollständig sind. Wenn sie fertig ist, wird so etwas richtig behandelt.

### 14. Duplizieren des Panels 

Unser Panel kann auf verschiedene Weisen dupliziert und kopiert werden, z.B. durch Kopieren/Einfügen. Aber ein interessanterer Weg ist die Nutzung des Draft-Clone-Werkzeugs (auch im Arch-Arbeitsbereich verfügbar, genau wie alle anderen Draft-Werkzeuge). Das Clone-Werkzeug behält die Beziehung zwischen dem Basisobjekt und dem Klon, so dass sich Änderungen am Basisobjekt auch auf die Klone auswirken.

![](images/Arch_panel_tutorial_18.jpg )

In der aktuellen Entwicklerversion von FreeCAD sind Klone von Arch-Objekten nun auch selbst Arch-Objekte.

### 15. Drehen und Positionieren des Panels 

Solange der Assembly-Arbeitsbereich von FreeCAD noch nicht fertig ist, müssen wir unsere Teile manuell positionieren, entweder durch manipulieren der Placement-Eigenschaft oder durch Nutzen des Draft-Move-and-Rotate-Werkzeugs, was im Moment nur visuelle Wege der Änderung des Placements von Objekten erlaubt.

Beide Draft-Move-and-Rotate-Werkzeuge nutzen das Draft-Einrast-System. Verschiedene Einrastpositionen (Endpunkte, Mittelpunkte, etc.) sind verfügbar, können ein-/ausgeschaltet werden, und erlauben sehr genaue Positionierungen und Rotationen.

![](images/Arch_panel_tutorial_19.jpg )

![](images/Arch_panel_tutorial_20.jpg )


{{Tutorials navi

}}   {{Sketcher Tools navi}} 
