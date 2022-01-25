# Manual:Preparing models for 3D printing/de
{{Manual:TOC/de}}

Einer der Haupteinsatzbereiche von FreeCAD ist die Herstellung von Objekten aus der realen Welt. Diese können in FreeCAD entworfen und dann auf verschiedene Weise realisiert werden, z.B. indem sie anderen Personen mitgeteilt werden, die sie dann bauen, oder, immer häufiger, direkt an einen [3D Drucker](https://en.wikipedia.org/wiki/3D_printing) oder eine [CNC Fräse](https://en.wikipedia.org/wiki/Milling_%28machining%29) geschickt werden. Dieses Kapitel zeigt dir, wie du deine Modelle für den Versand an diese Maschinen vorbereiten kannst.

Wenn du beim Modellieren vorsichtig warst, sind die meisten Schwierigkeiten, auf die du beim Drucken deines Modells in 3D stoßen könntest, bereits vermieden worden. Dies betrifft im Wesentlichen:

-   Stelle sicher, dass deine 3D Objekte **fest** sind. Objekte der realen Welt sind fest, das 3D Modell muss ebenfalls fest sein. Wir haben in früheren Kapiteln gesehen, dass FreeCAD dir in dieser Hinsicht sehr hilft und dass die [PartDesign Arbeitsbereich](PartDesign_Workbench/de.md) dich benachrichtigt, wenn du eine Operation durchführst, die verhindert, dass dein Modell fest bleibt. Der [Part Arbeitsbereich](Part_Workbench/de.md) enthält auch ein <img alt="" src=images/Part_CheckGeometry.svg  style="width:16px;"> [Überprüfe Geometrie](Part_CheckGeometry/de.md) Werkzeug das praktisch ist zur weiteren Prüfung auf mögliche Fehler.
-   vergewissere dich über die **Abmessungen** deiner Objekte. Ein Millimeter ist in der Praxis ein Millimeter. Jede Abmessung ist wichtig.
-   Kontrolle der **Verringerung**. Kein 3D Druck- oder CNC Frässystem kann FreeCAD Dateien direkt übernehmen. Die meisten von ihnen verstehen nur eine Maschinensprache namens [G-Code](https://en.wikipedia.org/wiki/G-code). G-Code hat Dutzende von verschiedenen Dialekten, jede Maschine oder jeder Anbieter hat normalerweise seinen eigenen. Die Konvertierung deiner Modelle in G-Code kann einfach und automatisch erfolgen, aber du kannst sie auch manuell durchführen, wobei du die volle Kontrolle über die Ausgabe hast. In jedem Fall wird während des Prozesses unvermeidlich ein gewisser Qualitätsverlust Ihres Modells auftreten. Wenn du in 3D druckst, musst du immer sicherstellen, dass dieser Qualitätsverlust unter deinen Mindestanforderungen bleibt.

Im Folgenden gehen wir davon aus, dass die ersten beiden Kriterien erfüllt sind und dass du von nun an in der Lage bist, feste Objekte mit korrekten Abmessungen herzustellen. Wir werden nun sehen, wie wir den dritten Punkt angehen können.

### Exportieren zu Zerschneidern 

Dies ist die Technik, die am häufigsten für den 3D-Druck verwendet wird. Das 3D Objekt wird in ein anderes Programm (den Zerschneider) (engl.: Slicer) exportiert, das den G-Code aus dem Objekt generiert, indem es es in dünne Schichten zerlegt (daher der Name), die die Bewegungen reproduzieren, die der 3D Drucker ausführen wird. Da viele dieser Drucker selbstgebaut sind, gibt es oft kleine Unterschiede von einem zum anderen. Diese Programme bieten in der Regel erweiterte Konfigurationsmöglichkeiten, die dir erlauben die Ausgabe genau auf die Funktionen deines 3D Druckers zuzuschneiden.

Tatsächlich ist der 3D Druck jedoch ein zu umfangreiches Thema für dieses Handbuch. Aber wir werden sehen, wie diese Zerschneider exportiert und verwendet werden können, um zu überprüfen, ob die Ausgabe korrekt ist.

### Umwandeln von Objekten in Polygonnetze 

Keiner der Zerschneider wird zu diesem Zeitpunkt direkt die Volumenkörpergeometrie übernehmen, wie wir sie in FreeCAD erzeugen. Daher müssen wir jedes Objekt, das wir in 3D drucken wollen, zuerst in ein [Polygonnetz](https://de.wikipedia.org/wiki/Polygonnetz) konvertieren, das der Zerschneider öffnen kann. Glücklicherweise ist die Konvertierung eines Netzes in einen Volumenkörper ein komplizierter Vorgang, während im Gegenteil die Konvertierung eines Volumenkörpers in ein Netz sehr einfach ist. Alles, worauf wir achten müssen, ist, dass genau hier die oben erwähnte Verschlechterung eintritt. Wir müssen überprüfen, ob die Verschlechterung innerhalb akzeptabler Grenzen bleibt.

Die gesamte Netz Handhabung wird in FreeCAD von einem anderen spezifischen Arbeitsbereich durchgeführt, dem [Arbeitsbereich Polygonnetz](Mesh_Workbench/de.md). Dieser Arbeitsbereich enthält zusätzlich zu den wichtigsten Werkzeugen zur Konvertierung zwischen Teil- und Netzobjekten verschiedene Hilfsprogramme zur Analyse und Reparatur von Netzen. Obwohl die Arbeit mit Netzen nicht im Mittelpunkt von FreeCAD steht, musst du dich bei der 3D Modellierung oft mit Netzobjekten befassen, da deren Verwendung unter anderen Anwendungen sehr weit verbreitet ist. Dieser Arbeitsbereich erlaubt dir sie vollständig in FreeCAD zu bearbeiten.

-   Lass uns eines der Objekte konvertieren, die wir in den vorherigen Kapiteln modelliert haben, wie z.B. das Lego Stück (das am Ende des vorherigen Kapitels heruntergeladen werden kann).
-   Öffne die FreeCAD Datei, die das Lego Stück enthält.
-   Wechsle zum [Netz Arbeitsbereich](Mesh_Workbench/de.md)
-   Wähle den Legostein
-   Wähle das Menü **Netze → Netz aus Form erzeugen**
-   Es öffnet sich ein Aufgabenpaneel mit mehreren Optionen. Einige zusätzliche Vernetzungsalgorithmen (Mefisto oder Netgen) sind möglicherweise nicht verfügbar, je nachdem, wie deine Version von FreeCAD kompiliert wurde. Der Standard Vernetzungsalgorithmus wird immer vorhanden sein. Er bietet weniger Möglichkeiten als die beiden anderen, ist aber für kleine Objekte, die in die maximale Druckgröße eines 3D Druckers passen, völlig ausreichend.

![](images/Exercise_meshing_01.jpg )

-   Wähle den **Standard** Netzbearbeiter und belasse den Abweichungswert auf dem Standardwert von **0,10**. Drücke **Ok**\'.
-   Es wird ein Netzobjekt erstellt, das sich genau über unserem Festkörperobjekt befindet. Entweder verbirg den Festkörper oder du verschiebst eines der Objekte zur Seite, so dass du beide vergleichen kannst.
-   Ändere die Eigenschaft **Ansicht → Anzeigemodus** des neuen Netzobjekts in **Flache Linien**, um zu sehen, wie die Triangulation stattgefunden hat.
-   Wenn du mit dem Ergebnis nicht zufrieden bist und denkst, dass es zu grob ist, kannst du den Vorgang wiederholen und den Abweichungswert verringern. Im Beispiel unten verwendet das linke Netz den Standardwert **0,10**\', während das rechte Netz **0,01**\' verwendet:

![](images/Exercise_meshing_02.jpg )

In den meisten Fällen werden die Standardwerte jedoch ein zufriedenstellendes Ergebnis liefern.

-   Wir können jetzt unser Netz in ein Netzformat exportieren, wie z.B. [STL](https://en.wikipedia.org/wiki/STL_%28file_format%29), das derzeit das am weitesten verbreitete Format beim 3D-Druck ist, indem wir das Menü **Datei → Export** benutzen und das STL-Dateiformat wählen.

Wenn du keinen 3D Drucker besitzt, ist es normalerweise sehr einfach, kommerzielle Dienste zu finden, die die gedruckten Objekte drucken und dir per Post zusenden. Zu den berühmten gehören [Shapeways](http://www.shapeways.com/) und [Sculpteo](http://www.sculpteo.com/), aber du wirst in deiner eigenen Stadt normalerweise viele andere finden. In allen größeren Städten findest du heutzutage [FabLabor](https://de.wikipedia.org/wiki/FabLab)e, das sind Werkstätten, die mit einer Reihe von 3D Fertigungsmaschinen ausgestattet sind, fast immer mit mindestens einem 3D Drucker. Fab Labore sind in der Regel Gemeinschaftsräume, in denen du deren Maschinen je nach Fab Labor kostenpflichtig oder kostenlos nutzen kannst, in denen du aber auch lernst, sie zu benutzen, und in denen du andere Aktivitäten rund um die 3D Fertigung fördern kannst.

### Verwendung von Slic3r 

[Slic3r](http://slic3r.org/) ist eine Anwendung, die STL Objekte in G-Code umwandelt, der direkt an 3D Drucker gesendet werden kann. Wie FreeCAD ist es kostenlos, quelloffen und läuft unter Windows, Mac OS und Linux. Die korrekte Konfiguration für den 3D Druck ist ein komplizierter Prozess, bei dem du gute Kenntnisse über deinen 3D Drucker haben musst. Daher ist es nicht sehr nützlich, G-Code zu erzeugen, bevor du tatsächlich druckst (Deine G-Code Datei funktioniert möglicherweise nicht gut auf einem anderen Drucker), aber es ist trotzdem nützlich für uns, zu überprüfen, ob unsere STL Datei problemlos gedruckt werden kann.

Dies ist unsere exportierte STL Datei, die in Slic3r geöffnet wurde. Durch verwenden des **Vorschau** Reiters und bewegen des rechten Schiebereglers, können wir den Pfad visualisieren, dem der 3D Druckkopf folgen wird, um unser Objekt zu konstruieren.

![](images/Exercise_meshing_03.jpg )

### Verwendung der Cura Erweiterung 

[Cura](https://ultimaker.com/en/products/cura-software) ist eine weitere freie und quelloffene Zerschneider Anwendung für Windows, Mac und Linux, die vom Hersteller des 3D Druckers [Ultimaker](https://ultimaker.com) gepflegt wird. Einige FreeCAD Benutzer haben einen [Cura Arbeitsbereich](https://github.com/cblt2l/FreeCAD-CuraEngine-Plugin) erstellt, der intern Cura verwendet. Der Cura Arbeitsbereich ist über das [FreeCAD Erweiterung](https://github.com/FreeCAD/FreeCAD-addons)s Repositorium verfügbar. Um den Cura Arbeitsbereich zu verwenden, musst du auch Cura selbst installieren, das nicht im Arbeitsbereich enthalten ist.

Sobald du sowohl Cura als auch den Cura Arbeitsbereich installiert hast, kannst du damit die G-Code Datei direkt aus den Part Objekten erzeugen, ohne diese in Polygonnetze umwandeln zu müssen und ohne eine externe Anwendung öffnen zu müssen. Die Erzeugung einer weiteren G-Code Datei aus unserem Lego Baustein, diesmal mit dem Cura Arbeitsbereich erfolgt wie folgt

-   Lade die Datei mit unserem Lego Stein (sie kann am Ende des vorherigen Kapitels heruntergeladen werden)
-   Wechsle zum [Cura Arbeitsbereich](https://github.com/cblt2l/FreeCAD-CuraEngine-Plugin)
-   Richte den Druckerbereich ein, indem du das Menü **3D Drucken → 3D Druckerdefinition erstellen** wählst. Da wir nicht wirklich drucken werden, können wir die Einstellungen so belassen, wie sie sind. Die Geometrie des Druckbettes und der verfügbare Platz werden in der 3D Ansicht angezeigt.
-   Bewege den Legostein an eine geeignete Stelle, z.B. in die Mitte des Druckbettes. Denke daran, dass PartDesign Objekte nicht direkt verschoben werden können, daher musst du entweder seine allererste Skizze (das erste Rechteck) verschieben oder eine Kopie verschieben (und drucken), die mit dem [Part → Erzeuge einfache Kopie](Part_SimpleCopy/de.md) Werkzeug erstellt werden kann. Die Kopie kann z.B. mit <img alt="" src=images/Draft_Move.svg  style="width:16px;"> [Entwurf → Bewegen](Draft_Move/de.md) verschoben werden.
-   Wähle das zu druckende Objekt und wähle das Menü **3D Drucken → Zerschneiden mit Cura Maschine**.
-   Vergewissere dich, dass der Pfad zur ausführbaren Cura Datei in dem sich öffnenden Aufgabenreiter korrekt eingestellt ist. Da wir nicht wirklich drucken werden, können wir alle anderen Optionen so lassen, wie sie sind. Drücke **Ok**. Es werden zwei Dateien im gleichen Verzeichnis wie deine FreeCAD-Datei erzeugt, eine STL-Datei und eine G-Code Datei.

![](images/Exercise_meshing_05.jpg )

-   Der generierte G-Code kann zur Überprüfung auch wieder in FreeCAD importiert werden (unter Verwendung des slic3r Präprozessors).

### Erzeugung von G-Code 


**'''Warnung:''' Dieser Abschnitt wurde für FreeCAD 0.16 erstellt. Es wurden erhebliche Änderungen bei der Pfaderstellung vorgenommen. Bitte beachte die Dokumentation der [Pfad Arbeitsbereich](Path_Workbench/de.md) im Allgemeinen oder das Tutorium wie [Pfadbegehung](Path_Walkthrough_for_the_Impatient/de.md)!**

FreeCAD bietet auch fortgeschrittenere Möglichkeiten, G-Code direkt zu erzeugen. Dies ist oft viel komplizierter als die Verwendung automatischer Werkzeuge, wie wir oben gesehen haben, hat aber den Vorteil, dass du die Ausgabe vollständig kontrollieren kannst. Bei der Verwendung von 3D Druckern ist dies normalerweise nicht erforderlich, wird aber beim CNC Fräsen sehr wichtig, da die Maschinen viel komplexer sind.

Die G-Code Pfadgenerierung in FreeCAD erfolgt mit dem [Pfad Arbeitsbereich](Path_Workbench/de.md). Sie enthält Werkzeuge, die vollständige Maschinenpfade erzeugen, und andere, die nur Teile eines G-Code Projekts erzeugen, die dann zu einer ganzen Fräsbearbeitung zusammengesetzt werden können.

Die Generierung von CNC Fräsbahnen ist ein weiteres Thema, das viel zu umfangreich ist, um in dieses Handbuch zu passen. Wir werden daher zeigen, wie man ein einfaches Bahnprojekt erstellt, ohne sich um die meisten Details einer echten CNC Bearbeitung zu kümmern.

-   Lade die Datei, die unser Lego Stück enthält, und wechsle zum [Pfad Arbeitsbereich](Path_Workbench/de.md).
-   Da das letzte Stück keine rechteckige Oberseite mehr enthält, verbirg das letzte Lego Stück und zeig das erste würfelförmige Polster an, das wir gemacht haben und das eine rechteckige Oberseite hat.
-   Wähle die obere Fläche und drücke die <img alt="" src=images/Path_Profile.svg  style="width:16px;"> [Profil](Path_Profile/de.md) Schaltfläche.
-   Setze seine **Versatz** Eigenschaft auf 1 mm.

![](images/Exercise_path_01.jpg )

-   Dann duplizieren wir diese erste Schleife ein paar Mal, damit das Werkzeug den ganzen Block herausschneidet. Wähle den Profil Pfad, und drücke die <img alt="" src=images/Path_Array.svg  style="width:16px;"> [Anordnung](Path_Array/de.md) Schaltfläche.
-   Setze die **Kopien** Eigenschaft der Anordnung auf 8 und seinen **Versatz** auf -2 mm in Z Richtung, und verschiebe die Platzierung der Anordnung um 2 mm in Z Richtung, so dass der Schnitt etwas oberhalb des Polsters beginnt und auch die Höhe der Punkte einschließt.

![](images/Exercise_path_02.jpg )

-   Jetzt haben wir einen Pfad definiert, der, wenn die Fräsmaschine ihm folgt, ein rechteckiges Volumen aus einem Materialblock herausfräst. Nun müssen wir den Raum zwischen den Punkten herausschneiden, um sie freizulegen. Blende das Polster aus und zeige das letzte Stück wieder an, damit wir die Fläche zwischen den Punkten auswählen können.
-   Wähle die obere Fläche und drücke die <img alt="" src=images/Path_Pocket_Shape.svg  style="width:16px;"> [Taschenform](Path_Pocket_Shape/de.md) Schaltfläche. Setze die Eigenschaft **Versatz** auf 1 mm und die Eigenschaft **Rückzugshöhe** auf 20 mm. Das ist die Höhe, bis zu der der Fräser beim Wechsel von einer Schleife zur anderen fährt. Andernfalls könnte der Fräser direkt durch einen unserer Punkte schneiden:

![](images/Exercise_path_03.jpg )

-   Noch einmal: Erstelle eine Anordnung. Wähle das Taschen Objekt aus, und drücke die <img alt="" src=images/Path_Array.svg  style="width:16px;"> [Anordnung](Path_Array/de.md) Schaltfläche. Setze die Anzahl der **Kopien** auf 1 und den **Versatz** auf -2 mm in Z Richtung. Verschiebe die Platzierung der Anordnung um 2 mm in Z Richtung. Unsere beiden Operationen sind nun abgeschlossen:

![](images/Exercise_path_04.jpg )

-   Nun müssen diese beiden Vorgänge nur noch zu einem einzigen zusammengefügt werden. Dies kann mit einem [Pfad Auftrag](Path_Job/de.md) geschehen. Drücke die <img alt="" src=images/Path_Job.svg  style="width:16px;"> [Pfadauftrag](Path_Job/de.md) Schaltfläche.
-   Setze die Eigenschaft **Platzierungen verwenden** des Projekts auf True, da wir die Platzierung der Anordnungen geändert haben, und wir möchten daß dies im Projekt berücksichtigt wird.
-   Ziehe in der Baumansicht die beiden Anordnungen per Ziehen & Ablegen in das Projekt. Du kannst die Anordnungen innerhalb des Projekts bei Bedarf neu anordnen, indem du darauf doppelklickst.
-   Das Projekt kann nun in G-Code exportiert werden, indem du es auswählst, das Menü **Datei -\> Exportieren** wählst, das G-Code Format auswählst und im sich öffnenden Aufklappdialog ein Nach-Bearbeitungsskript entsprechend deiner Maschine auswählst.

Es gibt viele Anwendungen, um das reale Schneiden zu simulieren, eine davon, die ebenfalls plattformübergreifend und quelloffen, wie FreeCAD ist, ist [Camotics](http://camotics.org/).

**Herunterladen**

-   Die in dieser Übung erzeugte STL Datei: <https://github.com/yorikvanhavre/FreeCAD-manual/blob/master/files/lego.stl>
-   Die während dieser Übung erstellte Datei: <https://github.com/yorikvanhavre/FreeCAD-manual/blob/master/files/path.FCStd>
-   Die in dieser Übung erzeugte G-Code Datei: <https://github.com/yorikvanhavre/FreeCAD-manual/blob/master/files/lego.gcode>

**Mehr lesen**

-   [Der Netz Arbeitsbereich](Mesh_Workbench/de.md)
-   [Das STL Dateiformat](https://en.wikipedia.org/wiki/STL_%28file_format%29)
-   [Slic3r](http://slic3r.org/)
-   [Cura](https://ultimaker.com/en/products/cura-software)
-   [Der Cura Arbeitsbereich](https://github.com/cblt2l/FreeCAD-CuraEngine-Plugin)
-   [Der Pfad Arbeitsbereich](Path_Workbench/de.md)
-   [Camotics](http://camotics.org/)

### Videos

-   [Wie man FreeCAD für den 3D Druck verwendet \| Verwendung des Realthunder Zweigs](https://www.youtube.com/playlist?list=PL6Fiih6ItYsWCE20KtUJYpiDPrCA2rVpN) Eine Video Wiedergabeliste von Maker Tales über die Verwendung von FreeCAD für den 3D Druck.



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Path](Category_Path.md) > [Mesh](Category_Mesh.md) > [Tutorials](Category_Tutorials.md) > Manual:Preparing models for 3D printing/de
