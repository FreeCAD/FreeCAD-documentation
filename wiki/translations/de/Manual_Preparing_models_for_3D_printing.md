# Manual:Preparing models for 3D printing/de
{{Manual:TOC}}

Ein Hauptverwendungszweck von FreeCAD ist das Entwerfen von Objekten, aus denen echte Produkte der realen Welt erstellt werden können. Diese Entwürfe können mit anderen geteilt werden, um sie Herzustellen oder, immer häufiger, um sie direkt an einem [3D-Drucker](https://en.wikipedia.org/wiki/3D_printing) oder eine [CNC-Fräse](https://en.wikipedia.org/wiki/Milling_%28machining%29) zu schicken, um sie automatisiert herzustellen. MIt FreeCAD können präzise, detaillierte Modelle erstellt werden, die sich für verschiedene Produktionsmethoden eignen. Dieses Kapitel führt durch den Prozess, die Modelle für solche Maschinen vorzubereiten und stellt sicher, dass sie den erforderlichen Vorgaben für erfolgreiche Herstellung entsprechen, egal ob in Team- oder Einzelarbeit.

Wenn du beim Modellieren vorsichtig warst, sind die meisten Herausforderungen im Zusammenhang mit 3D-Druck der Modelle schon minimiert. Die Hauptpunkte die wir betrachten beinhalten:

-   **Sicherstellen, dass 3D-Objekte Festkörper sind**: Wie Objekte der realen Welt, sollte auch das Modell \"fest\" sein, also ein Festkörper. FreeCAD, und besonders der Arbeitsbereich PartDesign, hilft dabei, dass ein Modell während des gesamten Konstruktionsprozesses ein Festkörper bleibt. Das Programm warnt den Anwender, wenn ein Objekt in etwas anderes als ein Festkörper umgewandelt wird. Außerdem stellt der Arbeitsbereich Part ein Werkzeug <img alt="" src=images/Part_CheckGeometry.svg  style="width:16px;"> [Geometrie überprüfen](Part_CheckGeometry/de.md) bereit, das ermöglicht potentielle Fehler Probleme zu entdecken, die den 3D-Drockprozess beeinflussen.

-   **Bestätigung der Genauigkeit der Abmessungen**: Präzision ist entscheidend -- was du in FreeCAD entwirfst, wird direkt in reale Maße umgesetzt. Ein Millimeter in FreeCAD ist ein Millimeter im physischen Objekt, daher muss jede Abmessung sorgfältig bedacht und überprüft werden, um die Genauigkeit sicherzustellen.

-   **Verwalten von Qualitätseinbußen**: Es ist wichtig, sich daran zu erinnern, dass kein 3D-Drucker oder CNC-Fräser FreeCAD-Dateien direkt verarbeiten kann. Diese Maschinen verwenden G-Code, eine Maschinensprache mit verschiedenen Dialekten, je nach Maschine oder Hersteller. Die Konvertierung deines Modells in G-Code kann oft automatisch über Slicer-Software erfolgen, aber du hast auch die Möglichkeit, dies für mehr Kontrolle manuell durchzuführen. Bei dieser Konvertierung ist jedoch ein gewisser Detail- oder Qualitätsverlust unvermeidlich, insbesondere wenn das Modell zum Drucken in ein Mesh-Format konvertiert wird. Du musst sicherstellen, dass diese Qualitätseinbußen innerhalb akzeptabler Grenzen bleiben und die Funktionalität oder das Erscheinungsbild deines endgültigen Objekts nicht beeinträchtigen.

-   **Kompatibilität des Exportformats**: Beim 3D-Druck ist STL das am häufigsten verwendete Format, aber es konvertiert dein Modell automatisch in ein Netz aus Dreiecken, was zu einem gewissen Detailverlust führen kann. Beim Exportieren in STL ist es wichtig, die richtige Auflösung zu wählen und zwischen Detailerhaltung und Dateigröße abzuwägen. Ebenso sind für die CNC-Bearbeitung Formate wie STEP oder IGES vorzuziehen, da sie die ursprüngliche geometrische Integrität des Designs besser beibehalten als STL. Die Wahl des richtigen Formats stellt sicher, dass die Konvertierung in G-Code präzise bleibt.

-   **Netzanalyse und -kalibrierung**: Bevor du dein Modell in einen Slicer oder CNC-Werkzeugpfadgenerator exportierst, ist es ratsam, eine Netzanalyse mit dem Arbeitsbereich [Mesh](Mesh_Workbench/de.md) von FreeCAD durchzuführen, um Unregelmäßigkeiten, nicht-manifold Kanten oder andere Netzprobleme zu erkennen, die den Herstellungsprozess erschweren könnten. Stelle außerdem auch bei einem perfekten Modell sicher, dass dein 3D-Drucker oder deine CNC-Maschine richtig kalibriert ist (z. B. für Bettnivellierung, Schrittmotoreinstellungen oder Extruderkonfiguration), um Qualitätsprobleme im Endprodukt zu vermeiden.

In den folgenden Abschnitten gehen wir davon aus, dass du dich bereits um die Erstellung von Volumenmodellen mit den richtigen Abmessungen gekümmert hast. Unser Fokus verlagert sich nun auf die Verwaltung des Konvertierungsprozesses in G-Code, um sicherzustellen, dass dein Modell die erforderliche Qualität für den 3D-Druck oder die CNC-Bearbeitung beibehält. Wenn du diese Überlegungen berücksichtigst, bist du besser gerüstet, um erfolgreiche physische Objekte direkt aus deinem FreeCAD-Modellen zu erstellen.



### Exportieren zu den Zerschneidern 

Die gängigste Methode zur Vorbereitung eines 3D-Modells für den Druck besteht darin, das 3D-Objekt aus FreeCAD in eine spezielle Software namens Slicer zu exportieren. Der Slicer generiert G-Code, indem er das Modell in dünne Schichten aufteilt, denen der 3D-Drucker folgt, um das Objekt Schicht für Schicht aufzubauen. Da viele 3D-Drucker -- insbesondere selbstgebaute oder Bastlermodelle -- einzigartige Konfigurationen haben, bieten Slicer-Programme eine breite Palette erweiterter Einstellungen. Mit diesen Einstellungen kannst du wichtige Parameter wie Schichthöhe, Druckgeschwindigkeit, Fülldichte und Stützstrukturen anpassen und so sicherstellen, dass der G-Code auf die spezifischen Funktionen und Fähigkeiten deines Druckers zugeschnitten ist.

Viele Slicer bieten auch Simulations- und Druckvalidierungsfunktionen, die für die Vorschau des Druckvorgangs von unschätzbarem Wert sind. Du kannst den Werkzeugweg für jede Schicht visualisieren, was dabei hilft, potenzielle Probleme wie Überhänge zu erkennen, die möglicherweise Stützen benötigen, oder Bereiche, in denen die Kühlung möglicherweise nicht ausreicht. Diese Validierung vor dem Druck stellt sicher, dass dein Modell vor Beginn des Drucks richtig vorbereitet ist, wodurch Fehldrucke oder Materialverschwendung vermieden werden.

Slicer liefern oft zusätzliche Informationen, wie z. B. die Schätzung der Druckzeit, des Materialverbrauchs und der Kosten basierend auf dem verwendeten Filament oder Harz. Auf diese Weise kannst du fundierte Entscheidungen über den Druckvorgang treffen und Einstellungen für mehr Effizienz oder Materialeinsparung optimieren. Obwohl die tieferen Feinheiten des 3D-Drucks -- wie Maschinenkalibrierung, Materialauswahl und Nachbearbeitung -- über den Rahmen dieses Handbuchs hinausgehen, konzentrieren wir uns darauf, wie du dein FreeCAD-Modell ordnungsgemäß exportieren und Slicer-Software verwendest, um sicherzustellen, dass die Ausgabe korrekt und für deinen spezifischen Drucker optimiert ist.



### Umwandeln von Objekten in Polygonnetze 

Keiner der derzeit verfügbaren Slicer kann die in FreeCAD erstellte Volumengeometrie direkt verarbeiten. Slicer wie Cura und PrusaSlicer arbeiten mit [mesh](https://en.wikipedia.org/wiki/Polygon_mesh)-basierten Formaten wie STL, OBJ oder 3MF, die die Oberflächengeometrie des Objekts mithilfe eines Netzwerks aus Dreiecken darstellen. Um ein in FreeCAD erstelltes Modell verwenden zu können, muss es daher zunächst in ein Mesh-Format konvertiert werden, das diese Slicer interpretieren können.

Das am häufigsten verwendete Format für den 3D-Druck ist STL. Ein Grund, warum STL bevorzugt wird, ist seine Einfachheit -- es stellt die 3D-Geometrie als Netz aus Dreiecken dar, ohne komplexe Details wie Farben, Materialien oder Texturen einzuschließen. Dieser minimalistische Ansatz stellt sicher, dass STL-Dateien leichtgewichtig und mit praktisch allen Slicern und 3D-Druckern kompatibel sind, was es zum Industriestandard macht. Obwohl OBJ und 3MF ebenfalls unterstützt werden, können sie zusätzliche Informationen wie Texturen und Materialien enthalten, die für die meisten 3D-Druckaufgaben unnötig sind und den Slice-Prozess erschweren können.

Glücklicherweise ist die Konvertierung eines festen Objekts in ein Netz in FreeCAD unkompliziert, auch wenn die Rückkonvertierung eines Netzes in einen festen Gegenstand ein komplizierterer Vorgang ist. Während des Konvertierungsprozesses ist es wichtig zu bedenken, dass die Qualität des Modells möglicherweise etwas nachlässt, insbesondere wenn komplexe Geometrie auf ein einfaches dreieckiges Netz reduziert wird. Du musst sicherstellen, dass diese Verschlechterung innerhalb akzeptabler Grenzen bleibt, um die Genauigkeit deines gedruckten Objekts zu erhalten.

In FreeCAD übernimmt der [Mesh Workbench](Mesh_Workbench.md) alle Mesh-bezogenen Aufgaben. Dieser Workbench enthält nicht nur Werkzeuge zum Konvertieren zwischen Part- und Mesh-Objekten, sondern auch zum Analysieren und Reparieren von Meshes. Obwohl die Mesh-Manipulation nicht der Hauptfokus von FreeCAD ist, wird sie bei der Vorbereitung von Modellen für den 3D-Druck unverzichtbar. Mesh-Objekte werden in anderen Anwendungen häufig verwendet, und der Mesh Workbench ermöglicht es dir, diese Objekte vollständig zu verwalten und anzupassen, um sicherzustellen, dass sie für den nächsten Schritt im Druckprozess bereit sind.

-   Lass uns das Lego-Stück, das wir im letzten Kapitel erstellt haben, in ein STL-Netz umwandeln. Die Geometrie kann am Ende des Kapitels heruntergeladen werden.
-   Öffne die FreeCAD-Datei, die das Lego-Stück enthält.
-   Wechsle zur [Mesh Workbench](Mesh_Workbench.md)
-   Wähle den Lego-Stein aus
-   Wähle das Menü **Meshes → Create Mesh from Shape**
-   Ein Aufgabenfenster mit mehreren Optionen wird geöffnet. Einige zusätzliche Netzalgorithmen (Mefisto oder Netgen) sind möglicherweise nicht verfügbar, je nachdem, wie deine Version von FreeCAD kompiliert wurde. Der Standard-Netzalgorithmus ist immer vorhanden. Er bietet weniger Möglichkeiten als die beiden anderen, ist aber für kleine Objekte, die in die maximale Druckgröße eines 3D-Druckers passen, völlig ausreichend.

![](images/FreeCAD_MeshLego.png )

-   Wähle den **Standard**-Mesher und belasse den Abweichungswert auf dem Standardwert von **0,10**. Drücke **Ok**.
-   Es wird ein Mesh-Objekt genau über unserem festen Objekt erstellt. Verstecke entweder das feste Objekt oder verschiebe eines der Objekte zur Seite, damit du beide vergleichen kannst.
-   Ändere die Eigenschaft **Ansicht → Anzeigemodus** des neuen Mesh-Objekts in **Flache Linien**, um zu sehen, wie die Triangulation erfolgte.
-   Wenn du nicht zufrieden bist und das Ergebnis zu grob findest, kannst du den Vorgang wiederholen und den Abweichungswert verringern. Im folgenden Beispiel wurde für das linke Mesh der Standardwert von **0,10** verwendet, während für das rechte **0,01** verwendet wird:

![](images/Exercise_meshing_02.jpg )

In den meisten Fällen werden die Standardwerte jedoch ein zufriedenstellendes Ergebnis liefern.

-   Wir können jetzt unser Netz in ein Netzformat exportieren, wie z.B. [STL](https://en.wikipedia.org/wiki/STL_%28file_format%29), das derzeit das am weitesten verbreitete Format beim 3D-Druck ist, indem wir das Menü **Datei → Export** benutzen und das STL-Dateiformat wählen.

In FreeCAD bietet der Mesh Workbench mehrere Algorithmen zum Konvertieren eines Volumenmodells in ein Mesh, darunter Standard, Mefisto, Netgen und Gmsh. Der Standardalgorithmus wird häufig für kleine bis mittelgroße Objekte verwendet, da er ein Gleichgewicht zwischen Geschwindigkeit und Meshqualität bietet. Beim Erstellen eines Meshs gibt es zwei kritische Parameter die Oberflächenabweichung und die Winkelabweichung. Die Oberflächenabweichung steuert, wie genau das Mesh der ursprünglichen Geometrie folgt, wobei kleinere Werte ein feineres, genaueres Mesh ergeben, aber möglicherweise zu größeren Dateien führen. Die Winkelabweichung definiert, wie viel Abweichung basierend auf Änderungen der Winkel des Modells zulässig ist, insbesondere bei Kurven und scharfen Kanten. Andere Optionen wie die relative Oberflächenabweichung ermöglichen es dir, die Präzision dynamisch basierend auf dem Maßstab des Modells anzupassen, Funktionen wie das Anwenden von Flächenfarben oder das Definieren von Mesh-Segmenten nach Farbe sind für erweitertes Rendering oder das Gruppieren verschiedener Bereiche des Modells nützlich. Sobald das Mesh generiert ist, kann es in Formate wie STL, OBJ oder 3MF exportiert werden, die für die Vorbereitung von Modellen für den 3D-Druck unerlässlich sind. Die Netzqualität ist entscheidend, um sicherzustellen, dass 3D-Drucker das Modell richtig interpretieren. Daher kann die Auswahl des richtigen Netzalgorithmus und der richtigen Abweichungseinstellungen das endgültige Druckergebnis erheblich beeinflussen.



### Verwendung von PrusaSlicer 

[PrusaSlicer](https://github.com/prusa3d/prusaslicer/releases) ist eine Anwendung, die STL-, OBJ- und 3MF-Objekte in G-Code umwandelt, der direkt an 3D-Drucker gesendet werden kann. Wie FreeCAD ist es kostenlos, Open Source und für Windows, Mac OS und Linux verfügbar. Obwohl es von Prusa Research entwickelt und für Prusa-3D-Drucker optimiert wurde, kann PrusaSlicer mit fast jedem 3D-Drucker verwendet werden, was es für eine Vielzahl von Maschinen vielseitig einsetzbar macht. PrusaSlicer basiert auf Slic3r, der ursprünglichen Slicer-Software, jedoch mit erheblichen Verbesserungen und häufigeren Updates. Slic3r wird nicht mehr aktiv aktualisiert, während PrusaSlicer sich weiterentwickelt und neue Funktionen wie adaptive Schichthöhen, Baumunterstützung und verbesserte Druckstrategien hinzufügt.

Die korrekte Konfiguration eines Slicers für den 3D-Druck ist ein komplexer Prozess, der ein gutes Verständnis der Fähigkeiten deines 3D-Druckers erfordert. Während das Generieren von G-Code ohne dieses Wissen zu einer Datei führen kann, die auf anderen Druckern nicht gut funktioniert, bietet PrusaSlicer dennoch eine hervorragende Möglichkeit, zu überprüfen, ob deine STL-Datei richtig formatiert und druckbar ist. Die Simulationsfunktionen des Slicers ermöglichen dir eine Vorschau der G-Code-Pfade und eine Überprüfung auf mögliche Druckprobleme, bevor du mit dem eigentlichen Druck beginnst.

Dies ist unsere exportierte STL-Datei, die in PrusaSlicer geöffnet wurde. Durch einfaches Drücken der Schaltfläche „Schneiden" teilt die Software Ihr Modell in Schichten auf, generiert die Werkzeugpfade für den 3D-Drucker und wendet die erforderlichen Geschwindigkeits- und Temperatureinstellungen an. Sie berechnet die Füllung, die Stützstrukturen und die Umfänge und erstellt dann den G-Code, der detaillierte Anweisungen für den Drucker enthält. Du kannst das geschnittene Modell Schicht für Schicht in der Vorschau anzeigen, die geschätzte Druckzeit und den Filamentverbrauch überprüfen und schließlich den G-Code für den eigentlichen Druckvorgang speichern oder an deinen Drucker senden.

![](images/FreeCAD_PrusaSlicer.png )

Neben PrusaSlicer gibt es noch viele andere Slicer-Softwareoptionen für den 3D-Druck. [Cura](https://ultimaker.com/fr/software/ultimaker-cura/), entwickelt von Ultimaker, ist einer der beliebtesten Open-Source-Slicer und unterstützt eine große Bandbreite an Druckern mit umfassenden Anpassungsmöglichkeiten. [Simplify3D](https://www.simplify3d.com/) ist ein kostenpflichtiger Slicer, der für seine erweiterten Funktionen und effiziente Werkzeugweggenerierung bekannt ist. [MatterControl](https://www.matterhackers.com/store/l/mattercontrol/sk/MKZGTDW6) ist ein Open-Source-Slicer, der auch grundlegende CAD-Tools enthält, während [IdeaMaker](https://www.raise3d.com/fr/ideamaker/) eine benutzerfreundliche Oberfläche mit adaptiven Schichthöhen bietet, die von Raise3D entwickelt wurde. Schließlich bietet [OrcaSlicer](https://github.com/SoftFever/OrcaSlicer), eine neuere Open-Source-Option basierend auf PrusaSlicer und Bambu Studio, zusätzliche Funktionen für verschiedene Drucker. Jeder Slicer hat einzigartige Stärken, sodass die beste Wahl von bestimmten Druckermodellen und Druckanforderungen abhängt.



### G-code generieren 

Der <img alt="" src=images/Workbench_CAM.svg  style="width:16px;"> [CAM Workbench](CAM_Workbench/de.md) in FreeCAD bietet erweiterte Optionen zum Generieren von G-Code direkt für CNC-Maschinen und bietet mehr Flexibilität und Kontrolle im Vergleich zu automatischen Slicing-Tools, wie sie für den 3D-Druck verwendet werden. Während 3D-Druck-Slicer ein Modell mit minimalem Aufwand automatisch in G-Code umwandeln können, erfordert das CNC-Fräsen viel mehr Benutzereingriff, um eine präzise Kontrolle über die Werkzeugwege, Geschwindigkeiten, Tiefen und andere Bearbeitungsparameter zu gewährleisten. Dies macht den CAM Workbench unverzichtbar für Aufgaben, die fein abgestimmten G-Code erfordern, insbesondere für das CNC-Fräsen, bei dem die Komplexität der Maschine und die Vielfalt der Vorgänge (wie Schneiden, Bohren und Konturieren) eine sorgfältige Planung erfordern.

Im CAM Workbench ist die G-Code-Pfadgenerierung hochgradig anpassbar. Sie bietet Tools zum Generieren vollständiger Maschinenpfade für verschiedene Vorgänge. Alternativ kannst du auch partielle G-Code-Segmente erstellen und diese zu einem vollständigen Fräsvorgang zusammenfügen. Dieser modulare Ansatz ermöglicht es dir, jeden Schritt des Bearbeitungsprozesses anzupassen und die Werkzeugpfade hinsichtlich Effizienz, Materialtyp und spezifischen Maschinenfunktionen zu optimieren.

Der CAM-Prozess ist tatsächlich viel komplexer als der 3D-Druck, da CNC-Maschinen andere Werkzeuge verwenden und Materialabtrag, Werkzeuggeometrie und Sicherheitsmargen berücksichtigen müssen, die alle manuell konfiguriert werden. In FreeCAD erfordert das Erstellen eines einfachen CAM-Projekts das Definieren von Werkzeugpfaden, Anpassen von Schnitttiefen, Auswählen geeigneter Werkzeuge und Konfigurieren von Arbeitsversatz, Vorschub und Geschwindigkeit. Im Gegensatz zu Slicer-Software, die die meisten dieser Aufgaben automatisch erledigt, überlässt dir der CAM Workbench die Kontrolle, wodurch er zwar sehr anpassbar, aber auch komplexer ist.

Obwohl das Erstellen von CNC-Fräspfaden ein zu umfassendes Thema ist, um es hier im Detail zu behandeln, zeigen wir dir, wie du ein einfaches CAM-Projekt in FreeCAD erstellst. Obwohl wir uns nicht auf jedes Detail der realen CNC-Bearbeitung konzentrieren, führt dich dieser Leitfaden in die wesentlichen Schritte ein und zeigt den erforderlichen Aufwand, um genaue und effiziente Ergebnisse zu gewährleisten. Diese zusätzliche Komplexität ist für CNC-Projekte unerlässlich, bei denen Präzision und Anpassbarkeit entscheidend sind, um die gewünschten Bearbeitungsergebnisse zu erzielen.

-   Lade die Datei mit unserem Lego-Teil und wechsle zum <img alt="" src=images/Workbench_CAM.svg  style="width:16px;"> [CAM Workbench](CAM_Workbench/de.md).
-   Klicke auf die Schaltfläche <img alt="" src=images/CAM_Job.svg  style="width:16px;"> [Job](CAM_Job.md) und wähle unser Lego-Teil aus.
-   Da dieser Abschnitt kein ausführliches Tutorial zur CAM Workbench bieten soll, verwenden wir die Standardwerte. Wenn du ein ausführlicheres Tutorial wünscht, lies bitte [CAM Walkthrough](CAM_Walkthrough_for_the_Impatient.md). Denke daran, dass in der CAM Workbench automatisch ein Rohkörper um dein Objekt herum erstellt wird, der das Rohmaterial darstellt, das bearbeitet wird. Derzeit erstreckt sich dieser Rohkörper 1 mm in alle Richtungen vom Objekt.

![](images/FreeCAD_CAM1.png )

-   Der erste Schritt besteht darin, das unnötige Material rund um unser Objekt zu entfernen. In dieser Phase beginnen wir mit einem massiven Block Rohmaterial und müssen den Legostein aus diesem Block herausarbeiten. Bei diesem Vorgang werden die Werkzeugpfade definiert, die das überschüssige Material nach und nach abschneiden und die gewünschte Form des Legosteins hinterlassen.

-   Das folgende Bild zeigt das Setup des FreeCAD CAM Workbench für die Bearbeitung eines Legosteins. Der Modellbaum enthält Volumenmodellierungsoperationen wie Pad, Pocket und LinearPattern, die zum Formen des Teils verwendet wurden. Es wird ein Job erstellt, der unter „Operationen" Werkzeugpfade enthält, die definieren, wie das Material aus dem Rohling entfernt wird. Für die Bearbeitung wird das Standardwerkzeug ausgewählt und der Modellkörper stellt das 3D-Teil dar, an dem gearbeitet wird. Dieses Setup bereitet das Objekt für die Generierung von G-Code zur Steuerung der CNC-Maschine vor.

![](images/FreeCAD_CAMtree.png )

-   Bevor wir mit dem Abschneiden des überschüssigen Materials beginnen, nehmen wir einige Anpassungen am zu verwendenden Fräswerkzeug vor. Obwohl du in der CAM Workbench benutzerdefinierte Werkzeuge definieren kannst, ändern wir der Einfachheit halber das Standardwerkzeug. Dadurch wird sichergestellt, dass die Einstellungen für unser Projekt optimiert sind, ohne dass ein neues Werkzeug von Grund auf neu erstellt werden muss.

-   Klicke auf den Text **TC:Default Tool**. Dadurch wird der **Tool Controller Editor** geöffnet. Ändere die Vorschubgeschwindigkeiten und Spindelgeschwindigkeiten wie im Bild gezeigt. Die Vorschubgeschwindigkeiten für horizontales und vertikales Schneiden sind auf 2000 mm/min eingestellt, während die Spindeldrehzahl bei Vorwärtsdrehung auf 2000 U/min eingestellt ist. Diese Einstellungen steuern die Bewegung und Schnittgeschwindigkeit des Werkzeugs während des Bearbeitungsvorgangs.

![](images/FreeCAD_toolController.png )

-   Doppelklicke auf das Werkzeug selbst und ändere seinen Durchmesser auf 1 mm.
-   Jetzt können wir beginnen, das überschüssige Material aus dem Block zu entfernen und nach und nach die Lego-Geometrie herauszuarbeiten. Dieser Vorgang umfasst die von uns festgelegten Werkzeugpfade, um sicherzustellen, dass die endgültige Form dem beabsichtigten Design entspricht.
-   Klicke auf das <img alt="" src=images/CAM_Profile.svg  style="width:16px;"> [Profil](CAM_Profile/de.md). Mit dieser Option wird das unnötige Material rund um den Umfang des Teils herausgearbeitet, wodurch die äußeren Grenzen effektiv geformt werden, um die allgemeinen Abmessungen des Lego-Stücks zu erreichen.
-   Normalerweise musst du keine der Standardwerte ändern, außer dem **Zusätzlichen Versatz** auf der Registerkarte „Operation". Stelle diese Option auf 1 mm ein, um sicherzustellen, dass das verbleibende Objekt korrekt den Grenzen des Legos entspricht.
-   Sobald du auf **Übernehmen** klickst, solltest du diese grünen Linien um das Objekt herum sehen können. Diese Linien visualisieren den Pfad, dem unser Schneidobjekt beim Schneiden des ursprünglichen Blocks folgt.

![](images/FreeCAD_CAMProfile.png )

-   Unser nächster Schritt ist die Erstellung der 6 extrudierten Zylinder auf der Oberseite des Legosteins.
-   Wähle die Oberseite und klicke auf die Schaltfläche <img alt="" src=images/CAM_Pocket_Shape.svg  style="width:16px;"> [Taschenform](CAM_Pocket_Shape/de.md). Aktiviere auf der Registerkarte **Erweiterungen** die Option Erweiterungen und klicke auf die Kante der Oberseite (normalerweise sollte diese automatisch im Feld für die Standardlänge hinzugefügt werden).
-   Gib schließlich auf der Registerkarte **Operation** -1,5 mm in das Feld **Erweiterung übergeben** ein und ändere die Musteroption in einen ZigZagOffset.
-   Drücke **Übernehmen** und schließe dann die Registerkarte.
-   Auf ähnliche Weise können wir die drei Zylinder auf der Unterseite des Legosteins erstellen.
-   Wir können die Schritte beim Fräsen des Objekts leicht visualisieren, indem wir die Option <img alt="" src=images/CAM_SimulatorGL.svg  style="width:16px;"> [SimulatorGL](CAM_SimulatorGL.md) verwenden.

**Downloads**

-   Die in dieser Übung generierte STL-Datei: <https://github.com/yorikvanhavre/FreeCAD-manual/blob/master/files/lego.stl>
-   Die während dieser Übung generierte Datei: <https://github.com/yorikvanhavre/FreeCAD-manual/blob/master/files/path.FCStd>
-   Die in dieser Übung generierte G-Code-Datei: <https://github.com/yorikvanhavre/FreeCAD-manual/blob/master/files/lego.gcode>

**Read more**

-   [Der Arbeitsbereich Mesh](Mesh_Workbench/de.md)
-   [Das STL-Dateiformat](https://en.wikipedia.org/wiki/STL_%28file_format%29)
-   [Slic3r](http://slic3r.org/)
-   [Cura](https://ultimaker.com/en/products/cura-software)
-   [Der Arbeitsbereich Cura](https://github.com/cblt2l/FreeCAD-CuraEngine-Plugin)
-   [Der Arbeitsbereich CAM](CAM_Workbench/de.md)
-   [Camotics](http://camotics.org/)

### Videos

-   [Wie man FreeCAD für den 3D Druck verwendet \| Verwendung des Realthunder Zweigs](https://www.youtube.com/playlist?list=PL6Fiih6ItYsWCE20KtUJYpiDPrCA2rVpN) Eine Video Wiedergabeliste von Maker Tales über die Verwendung von FreeCAD für den 3D Druck.



---
⏵ [documentation index](../README.md) > [CAM](Category_CAM.md) > [Mesh](Category_Mesh.md) > [Tutorials](Category_Tutorials.md) > Manual:Preparing models for 3D printing/de
