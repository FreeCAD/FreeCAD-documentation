
{{Page in progress}}




{{TutorialInfo/de
|Topic=Modellierung
|Level=Erfahrene Anwender
|Author=domad
|FCVersion=0.19.23300 oder höher
}}

## Zielsetzung in Kürze {#zielsetzung_in_kürze}

Erstelle Punkte, Linien, Kreise, Bögen usw. in TechDraw Ansichten und/oder ganze \"kosmetische\" Zeichnungen mit absoluter Präzision, passend zu den Bemaßungswerkzeugen, mit denen der Arbeitsbereich ausgestattet ist, um konforme und detaillierte technische Zeichnungen zu erzeugen.

## Einführung

Dieses Tutorium führt den erfahrenen Anwender in die fortgeschrittene Nutzung vorhandener Werkzeuge und Techniken aus anderen Arbeitsbereichen ein, um eigentlich fehlende Funktionalität in <img alt="" src=images/Workbench_TechDraw.svg  style="width:24px;"> zu erweitern. [TechDraw Arbeitsbereich](TechDraw_Workbench/de.md). Dieses Tutorium ist keine vollständige und umfassende Anleitung zum TechDraw Arbeitsbereich und viele der Werkzeuge und Möglichkeiten werden nicht behandelt. Es soll dazu beitragen, die Schwierigkeiten zu überwinden, die beim Angeben und Anreichern der technischen Zeichnung mit TechDraw auftreten. Dieses Tutorium führt fortgeschrittene Benutzer durch die Schritte, die erforderlich sind, um anspruchsvolle technische Zeichnungen des Teils aus dem [Grundlagen Part Design Tutorium](Basic_Part_Design_Tutorial/de.md) mit den Zeichenwerkzeugen der

1.  <img alt="" src=images/Workbench_Draft.svg  style="width:24px;"> [Entwurf Arbeitsbereich](Draft_Workbench/de.md) (Linien, Polylinien, Umfänge, Bögen, Splines, Beziers, usw.), insbesondere die Fänge, um auf dem Objekt tatsächlich präzise \"kosmetische Punkte\" zu erzeugen, die dann für die Bemaßung in TechDraw verwendet werden können.
2.  Es ist auch möglich, den <img alt="" src=images/Workbench_Sketcher.svg  style="width:24px;"> [Skizzierer Arbeitsbereich](Sketcher_Workbench/de.md) als
    -   Generator von \"base-sketchTD\" (Skizzengrundlagen für TechDraw) in 2D (z.B. wie Systemdiagramm, Grundrisse, Aufrisse, Ansichten von mechanischen oder allgemeinen Teilen, usw.) oder durch
    -   direkte Verwendung der Skizzen, aus denen die 3D Modelle erstellt wurden, oder durch
    -   durch die Umwandlung des \"Flächenbinders\" in eine Skizze, die mit Hilfe von Entwürfen aus Flächen und/oder Schnitten der 3D Modelle erstellt wurde.
3.  Um bestimmte Schnitte (Schnitte auf verschiedenen Ebenen oder Achsen) zu erhalten, die auf der Seite in TechDraw dargestellt werden sollen (es wird empfohlen, eine Kopie des ursprünglichen 3D Objekts zu verwenden), dann durch die Erstellung von Ebenen (auch auf verschiedenen Achsen) unter Verwendung der

<img alt="" src=images/Workfeature_workbench_icon.svg  style="width:24px;"> [Workfeature Arbeitsbereich](Workfeature_Workbench/de.md), ist es möglich, die Kopie des 3D Objekts <img alt="" src=images/Part_SliceApart.svg  style="width:24px;"> zu schneiden [Part SliceApart](Part_SliceApart/de.md), um die Flächen zu erhalten, die in eine Skizze <img alt="" src=images/Draft_Draft2Sketch.svg  style="width:24px;"> umgewandelt werden sollen. [Entwurf EntwurfZuSkizze](Draft_Draft2Sketch/de.md) umzuwandeln und dann mit Hilfe des Skizzierer Arbeitsbereichs so zu bearbeiten, dass sie für die technische Zeichnung, die wir in TechDraw erstellen möchten, geeignet sind. Der [Workfeature Arbeitsbereich](Workfeature_Workbench/de.md) (und [Makro WorkFeatures](Macro_WorkFeatures/de.md)) sind voller praktischer Zusatzfunktionen, die es uns erlauben, auf einfache Weise Ebenen (theoretisch unendlich in Ausdehnung und Menge) zu erstellen, indem wir drei Punkte (Knoten) auswählen. *(erinnere dich daran, dass für drei durchlaufende Punkte eine und nur eine Ebene durch drei nicht ausgerichtete Punkte geht*\') ist ein geometrisches Axiom, das ohne jede Zweideutigkeit (!) die Gültigkeit und Bedeutung des WorkFeatureDev Werkzeugs zur einfachen Erstellung präziser Pläne. (\**Dies ist durchaus vergleichbar mit dem AutoCAD Schneide Befehl [1](https://knowledge.autodesk.com/support/autocad/learn-explore/caas/CloudHelp/cloudhelp/2019/ENU/AutoCAD-Core/files/GUID-27593C5E-4B89-41F2-872B-927D69517CBF-htm.html), der auf diesem Axiom basiert. Ohne vorher eine neue Ebene zu erstellen, wird eine Schnittebene mit drei Punkten definiert.*)

*Hinweis: Diese Ebenen können durch Überlappung/ Deckungsgleichheit von zwei Kanten unter Verwendung der booleschen Funktion von <img alt="" src=images/Part_Fuse.svg  style="width:24px;"> [Part Vereinigen](Part_Fuse/de.md) zusammengefügt werden.* Die so geformten und entsprechend positionierten Ebenen (gemäß unseren Bestimmungen) werden als **Schneidklingen** verwendet <img alt="" src=images/Part_SliceApart.svg  style="width:24px;"> [Part AuseinanderSchneiden](Part_SliceApart/de.md) zerschneiden unser 3D Objekt entsprechend der gewählten Flächenbestätigung in mehrere Teile.\'\'

## Bevor du anfängst {#bevor_du_anfängst}

Die Arbeitsbereiche, mit denen die Zeichnungen der angehängten Beispiele erstellt werden, sind:
\* <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Teil Arbeitsbereich](Part_Workbench/de.md)

-   <img alt="" src=images/Workbench_Draft.svg  style="width:24px;"> [Arbeitsbereich Entwurf](Draft_Workbench/de.md)
-   <img alt="" src=images/Workbench_Sketcher.svg  style="width:24px;"> [Skizzierer Arbeitsbereich](Sketcher_Workbench/de.md)
-   <img alt="" src=images/Workfeature_workbench_icon.svg  style="width:24px;"> [Workfeature Arbeitsbereich](Workfeature_Workbench/de.md)
-   <img alt="" src=images/Workbench_TechDraw.svg  style="width:24px;"> [TechDraw Arbeitsbereich](TechDraw_Workbench/de.md)

## Die Aufgabe {#die_aufgabe}

Stufen des Verfahrens:

1.  Erstellung des/der 3D Objekts(e) gemäß dem Kanon des traditionellen Modellierens;
2.  Mögliche Erstellung unabhängiger oder einfacher Kopien, z.B. für die Erstellung spezifischer kontinuierlicher Schnitte, die auf mehreren Ebenen oder Achsen positioniert sind, und die dann durch die Verwendung der Funktionen \"Facebinder\", \"Draft to Sketch\", Shape 2D View, usw. erlauben, perfekte \"Skizzen\" zu erstellen, die dann bearbeitet werden, um sie (durch die Erstellung von ad hoc \"kosmetischen Punkten oder Linien\") in TechDraw nutzbar zu machen; diesen Skizzen habe ich den Namen \"base-sketchTD\" gegeben;
3.  Einfügen / Erstellen von \"base-sketchTD\" in die zugehörigen Ebenen (auch mit \"Ziehen und Ablegen\");
4.  Erstellung der Zeichnungsseite mit ihrer Vorlage;
5.  Erstellung der Ansicht mit TechDraw: Wähle die Schicht oder den Gruppierungsordner (der die \"base-sketchTD\" enthält) aus der Struktur aus, klicke dann auf die Schaltfläche \"Ansicht einfügen\"; TechDraw fügt den Inhalt der Ebene oder des Gruppierungsordners in die Ansicht ein. Für eine korrekte Erstellung muss \"base-sketchTD\" senkrecht zur Bildschirmansicht stehen; ich weise darauf hin, dass alles, was wir später in der Ebene oder im Gruppierungsordner hinzufügen, oder Änderungen an der \"base-sketchTD\", in Echtzeit in der TechDraw Ansicht aktualisiert werden. Beachte, dass sich Aktualisierungen und/oder Änderungen auf die bereits eingeführten Abmessungen oder kosmetischen Linien auswirken können, die mit dem spezifischen TechDraw Werkzeug in der Ansicht erstellt wurden.
6.  Sobald die \"base-sketchTD\" in der Ansicht definiert ist, können wir mit den entsprechenden TechDraw Werkzeugen die Bemaßung vornehmen;

Es ist möglich, die \"base-sketchTD\" auch in den Projektionsgruppenansichten einzufügen:

-   Wähle die Projektionsansicht -\> Eigenschaften Reiter -\> Daten -\> \"Projektion\" Aufzeichnungsabschnitt-\> Quelle klicke auf die Schaltfläche mit den drei Punkten und füge direkt die \"base-sketchTD\" oder die Ebene, die sie enthält, hinzu.

:   Es sollte beachtet werden, dass die \"base-sketchTD\" auf der höchsten Fläche des Modells/Objekts positioniert werden muss, da sie sonst verdeckt wird und in TechDraw unsichtbar ist.

Die aus den Ansichten gewonnenen Schnitte scheinen diese Möglichkeit nicht zu haben. Wenn es notwendig ist, präzise kosmetische Punkte zu erzeugen, die für die Bemaßung geeignet sind (z.B. Tangentenpunkte), können diese erzeugt werden:

-   im \"Skizzierer\" durch Konstruktionslinien und Einfügen von Kreisen mit infinitesimalem Durchmesser / Radius (0,00001) an den Enden, diese werden von TechDraw als Punkte / Knoten gesehen, die zur Bemaßung geeignet sind;
-   im Entwurf mit der gleichen Methode in die entsprechende Ebene oder Ordnergruppierung eingefügt werden;

:   Sobald die \"base-sketchTD\" geändert oder das Entwurfsobjekt in der Ebene oder im Gruppierungsordner hinzugefügt wurde, aktualisiert TechDraw die Ansicht automatisch; falls dies nicht geschieht, aktualisiere sie manuell mit dem entsprechenden Befehl.

Um Ausschnittsfüllungen oder Muster einzufügen:
Achte auf die Linien, die auf den Flächen erstellt werden, die zwei oder mehr Kanten schneiden, sie werden von TechDraw als trennende Elemente der Fläche angesehen, die die Erstellung der Füllungen oder Muster beeinflussen. Dies ist z. B. der Fall, wenn die äußeren Linien erstellt werdeen, die das Gewinde einer Bohrung definieren. Diese Linie verhindert, dass die Füllung oder das Muster weiter verläuft und auf die Linie trifft, die das Vorbohrloch definiert. In diesem Fall ist es besser, kosmetische Punkte durch Konstruktionslinien zu erzeugen, indem man Kreise mit infinitesimalem Radius in die Knoten einfügt, die von TechDraw als kosmetische Punkte angesehen werden, und sie dann in TechDraw mit einer kosmetischen Linie durch zwei Punkte verbindet.
Alle Linien und / oder Pfade (einschließlich der kosmetischen), die in den Ansichten angezeigt werden, können in der Formatierung durch den TechDraw Befehl \"Aussehen der ausgewählten Linien ändern\" bearbeitet werden.
Um bestimmte kontinuierliche Abschnitte auf verschiedenen Achsen oder Ebenen zu erstellen, habe ich den \"WorkFeatureDev\" Arbeitsbereich verwendet, der es ermöglicht, \"feste\" Ebenen mit einer Dicke von \"0\" zu erstellen, indem man drei Knoten auswählt. Diese Ebenen können über eine gemeinsame oder überlappende Kante mit Hilfe der booleschen Funktionen des \"Part\" Arbeitsbereichs verbunden werden und anschließend zum Schneiden / Zerlegen des Volumenmodells mit dem Befehl \"Slice apart\" desselben Arbeitsbereichs verwendet werden. Die Flächen der geschnittenen Objekte können mit der \"Facebinder\" Funktion zur Erstellung von \"base-sketchTD \"s genutzt werden, um spezifische Schnittansichten in TechDraw zu erzeugen und somit zu bemaßen und zu detaillieren.
Ich glaube, ich habe jeden \"Trick\" (oder eher jedes System) veröffentlicht, das ich ausprobiert habe, um spezifischere Werkzeuge (die nicht in TechDraw enthalten sind) zu verwenden und qualitativ hochwertige, professionelle technische Zeichnungen ohne Begrenzungen zu erstellen, was der TechDraw Arbeitsbereich effizienter und anpassungsfähiger an jeden Bedarf macht, aller Wahrscheinlichkeit nach gleichwertig (wenn nicht sogar flexibler und leistungsfähiger) als die kommerziellen Kollegen.
Es sollte gesagt werden, was nicht unwichtig ist, dass es mit diesem System möglich ist, ganze 2D Dateien zu erstellen und sie mit TechDraw auf die gleiche Weise zu zitieren wie \"LibreCad\" oder \"Autocad LT\" oder andere zweidimensionale Cads.
Ich hoffe, ich war klar genug (wenn die Übersetzung es zulässt), um das Verfahren (\"Trick / System\") zu erklären, von dem ich glaube, dass es \"einfacher zu tun als zu sagen\" ist, da es darum geht, 2D Zeichnungen in die Ansichten von TD einzugeben, die mit \"Draft\" und / oder mit \"Skizzierer\" erstellt wurden, indem man sie einfach aus der Struktur auswählt und eine Ansicht in TD mit dem entsprechenden Befehl \"Ansicht erstellen\" erstellt; aber ich dachte, ich mache etwas Angenehmes und Technisches, indem ich das Verfahren beschreibe, natürlich auf eine \"vereinfachte\" Weise, um ein Minimum an organisiertem Arbeitsablauf zu schaffen.
Es liegt an jedem von uns, mit Phantasie und Erfindungsreichtum, das Ganze zu optimieren, um das beste Ergebnis zu erzielen.
Ich füge die Dateien einiger Arbeitsablauf Beispiele von technischen Zeichnungen bei (nicht nur mit TechDraw machbar), aus denen die unten gezeigten Bilder entnommen wurden.
In der Hoffnung, nützlich gewesen zu sein, gute Arbeit und gutes Experimentieren!

## Hinweise

## Zukunftsperspektiven

Jedoch könnte der beschriebene Weg den Ausgangspunkt (oder die Idee) darstellen, zusätzlichen Code zu schreiben, um das System zu automatisieren und es direkt in TechDraw mit entsprechenden Schaltflächen-/Befehlsfunktionen zu integrieren.

## Verweise

-   [Makro WorkFeatures](https://wiki.freecadweb.org/Macro_WorkFeatures) Wiki Seite zum Makro
-   [FreeCAD WorkFeature Workbench](https://github.com/Rentlau/WorkFeature-WB) Repositorium zum Quellcode
-   [TechDraw ohne Grenzen = Layout autocad](https://forum.freecadweb.org/viewtopic.php?t=54499) Forumsbeitrag
-   [TechDraw: - come utilizzare gli strumenti Draft/Snaps per creare \" vertici/punti cosmetici\"](https://forum.freecadweb.org/viewtopic.php?f=28&t=53329) Forum Thema in italienischer Sprache


{{Tutorials navi

}} {{TechDraw Tools navi}} 
