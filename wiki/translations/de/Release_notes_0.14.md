# Release notes 0.14/de
FreeCAD 0.14 wurde am 1. Juli 2014 veröffentlicht. Diese Release notes sind eine Zusammenfassung der wichtigsten Entwicklungen in FreeCAD seit der letzten Version 0.13. Für eine vollständige Liste aller Änderungen siehe [den Mantis Changelog](http://www.freecadweb.org/tracker/changelog_page.php). Alte Versionen: [0.13](Release_notes_0.13/de.md) - [0.12](Release_notes_0.12.md) - [0.11](Release_notes_0.11/de.md)

<img alt="" src=images/Freecad_jeep.png  style="width:1024px;">


<center>

Jeepmodell von Psicofil


</center>

## Allgemeines

### Migration Internet-Auftritt 

Letztendlich wurden alle Webapplicationen von FreeCAD von [SourceForge](http://www.sourceforge.net) zu unserer [eigenen Domain](http://www.freecadweb.org) migriert. Der neue FreeCAD-Internetauftrit findet sich unter <http://www.freecadweb.org>, das Wiki ist nun unter <http://www.freecadweb.org/wiki>, der Bug- und Featuretracker unter <http://www.freecadweb.org/tracker>, und das Forum unter <http://forum.freecadweb.org> erreichbar. Ein Loginaccount aus der Zeit als wir noch auf Sourceforge waren kann in ein Benutzerlogin unserer neuen Services übertragen werden. Alle Daten (Forumseinträge etc.) bleiben erhalten. Hier findet sich eine [Anleitung](http://forum.freecadweb.org/viewtopic.php?f=8&t=4942).

Der einzige Bereich von FreeCAD der auf Sourceforge bleibt ist das Hauptgitrepository. Die Adresse hat sich nicht geändert: <http://sourceforge.net/p/free-cad/code/ci/master/tree/>. Es gibt aber auch ein automatisch erstelltes Spiegelbild auf github unter <http://github.com/FreeCAD/FreeCAD_sf_master>

Um die wunderbare FreeCAD-Gemeinschaft kennenzulernen und sich von dem Talent, der Energie und der Hilfsbereichschaft anstecken zu lassen reicht ein Besuch in unserem [Forum](http://forum.freecadweb.org).

### Migration zu pyside, FreeCAD ist jetzt vollständig LGPL 

Wegen der vielen Komplikationen, die vom Doppellizenzmodell (LGPL und GPL) von FreeCAD und der Tatsache herrühren, dass einige Komponenten von FreeCAD nicht GPL kompatibel sind (insbesondere der OpenCasCade Geometriekernel), haben wir beschlossen, allen noch verbleibenden GPL Code in FreeCAD zu LGPL umzuwandeln. Als ein Ergebnis dieser Anstrengungen wird [PyQt](http://en.wikipedia.org/wiki/PyQt) nicht weiter verwendet, sondern durch [PySide](http://en.wikipedia.org/wiki/PySide) ersetzt. Dieser Wechsel hat keine großen Konsequenzen für die Ersteller von Python Skripten für FreeCAD, da PyQt weiterhin in FreeCAD verwendet werden kann.

Nachdem der Übergang zur LGPL abgeschlossen war, ist OpenCasCade [ebenfalls gewechselt](http://www.opencascade.org/getocc/license/), was die Lizenzprobleme ebenfalls gelöst hätte. Aber jetzt hat FreeCAD ein viel klareres und einheitlicheres Lizenzmodell, dass auch die striktesten Linux Distributionen zufrieden stellen sollte.

### Plugins und externe Projekte: Teile Bibliothek, BOLTS, Eagle importer 

Im letzten Jahr sind einige interessante Nebenprojekte im Umfeld von FreeCAD entstanden. Es wurde begonnen, eine [Teilebibliothek](http://github.com/yorikvanhavre/FreeCAD-library) aufzubauen, die langsam anwächst und eine Sammlung von wiederverwendbaren Teilen enthält, die in eigene FreeCAD Modelle einfügt werden können. Diese Bibliothek kann mit Hilfe eines Makros innerhalb von FreeCAD gestartet und benutzt werden.

Ein ähnliches, aber ambitionierteres Projekt ist [BOLTS](http://bolts-library.org/), ebenfalls eine Teilebibliothek, die aber aus parametrischen Skripten aufgebaut ist, und so in der Lage ist, eine große Vielfalt an parametrischen Teilen zu erzeugen. Obwohl BOLTS unabhängig von spezifischen CAD Applikationen ist, kann es mit Hilfe eines Makros auch innerhalb von FreeCAD verwendet werden. Das folgende Bild zeigt BOLTS in FreeCAD.

<img alt="" src=images/Freecad-bearing.png  style="width:1024px;">

Ein weiteres interessantes externes Projekt ist der [EAGLE importer](http://sourceforge.net/projects/eaglepcb2freecad/), mit dem Leiterplattenentwürfe aus mehreren Anwendungen nach FreeCAD importiert werden können.

### WebGL Export 

FreeCAD kann jetzt eine Szene als [WebGL](http://en.wikipedia.org/wiki/WebGL)-fähige HTML Datei exportieren. Diese Datei enthält einen eingebetteten Viewer, der auf [three.js](http://threejs.org/) basiert, und mit dem die Szene in WebGL-fähigen Browsern ohne Plugins betrachtet werden kann.

### Maßeinheitensystem

Ein [Maßeinheitensystem](units.md) wurde letztendlich in das Grundprogramm FreeCAD implementiert, somit kann es von allen Modulen verwendet werden. In den Einstellungen kann ein Einheitenschema auswählt werden. Im Moment sind Schemata für Millimeter, Meter und imperiale Maßeinheiten verfügbar, aber weitere werden folgen. Sobald ein Schema ausgewählt ist, verwenden die meisten Anzeigen, Eingabefelder und Werkzeuge bevorzugt diese Einheiten. Das Einheitensystem ist sehr flexibel, und Einheiten können an vielen Stellen frei gemischen werden. Zum Beispiel ist es möglich in einem auf Millimeter eingestellen Dokument Längenangaben in Zoll zu machen.

### Formatvorlagen

Die Verwendung von [Formatvorlagen](http://forum.freecadweb.org/viewtopic.php?f=8&t=4700&start=30) (Style Sheets) für das Hintergrundbild des Hauptfensters erlaubt es FreeCAD 0.14 noch stärker an besondere Anforderungen anzupassen. Der Anwender ist nicht mehr auf den grauen Steinhintergrund festgelegt, sondern fast beliebige Bilder oder Kacheln können für den Hintergrund des Hauptfensters verwendet werden.

<img alt="" src=images/Style_Sheets.png  style="width:1024px;">

### Ansichtsmodus

Einige neue Icons wurden zur Standard Ansichtswerkzeugleiste hinzugefügt, die es erlauben, die gesamte 3D Ansicht als Gitternetz oder mit Oberflächen und/oder Kanten anzuzeigen.

### Kantenglättung für 3D Ansicht 

Die Kantenglättung für die 3D Ansicht von FreeCAD hat neue Optionen erhalten, die in den Einstellungen angepasst werden können. Mit einer guten 3D Grafikkarte kann mit hochwertiger Kantenglättung ein sehr viel angenehmeres Erscheinungsbild genossen werden.

## Arbeitsbereich Part 

### Freiformfläche und Sweepen 

Die Funktionen [Part Loft](Part_Loft.md) (Menü Formteil \--\> Freiformfläche) and [Part Sweep/de](Part_Sweep/de.md) (Menü Formteil \--\> Sweepen) wurden verbessert und können nun Objekte, die mit dem [Arbeitsbereich Entwurf](Draft_Workbench/de.md) erstellt wurden, als Profile verwenden.

### Versetzen

Die neue Funktion [Part Offset](Part_Offset.md) (Menü Formteil \--\> Versetzen) erstellt Kopien von einer makierten Form in einer bestimmten Entfernung der Basisform.

### Dicke

Die neue Funktion [Part Thickness](Part_Thickness.md) (Menü Formteil \--\> Dicke) ist jetzt verfügbar. Mit dieser Funktion können Volumenkörper in hohle Objekte gewandelt werden, indem jeder Fläche des Volumenkörpers eine Dicke zugewiesen wird.

### Make Compound 

Der [Arbeitsbereich Partverfügt](Part_Workbench/de.md) jetzt über ein [Verbund herstellen](Part_Workbench/de.md) Werkzeug, der dir erlaubt schnell ein Verbundobjekt aus einem Satz ausgewählter Formen erstellen zu können.

### Part Grundkörper 

Neue Körper wurden zu den [Grundkörpern](Part_CreatePrimitives/de.md) (Menü Formteil \--\> Grundkörper erstellen) hinzugefügt. Prisma, Reguläre Polygone und Spiralen können jetzt sehr einfach durch Eingabe einiger Parameter erstellt werden. Weiterhin können einige Funktionen des [Arbeitsbereichs Entwurf](Draft_Workbench/de.md) auch Nutzen aus der neuen Funktion ziehen und erstellen Grundörper anstatt normale Draftobjekte, wenn die dazugehörige Option in den Einstellungen aktiviert wurde.

![](images/Part_Create_Primitives1.jpeg )

### Messfunktionen

Ein neuer Funktionsbereich Messen wurde dem [Arbeitsbereich Part](Part_Workbench/de.md) hinzugefügt. Werden zwei Formen (Punkte, Kanten oder Flächen) aktiviert, so wird der direkte Abstand und der Abstand entlang der x- und y-Achse angezeigt.

## Arbeitsbereiche PartDesign und Skizze 

### Validate Skizze 

Der [Skizzierer](Sketcher_Workbench/de.md) verfügt jetzt über ein neues [Skizze überprüfen](Sketcher_ValidateSketch/de.md) Werkzeug, das dir bei der Überprüfung einer Skizze hilft, indem es fehlende oder überflüssige Beschränkungen findet. Es kann auch automatisch einige fehlende Beschränkungen hinzufügen, damit deine Skizze vollständig beschränkt wird.

### Zahnradgenerator

Die Funktion [involute gear generator](PartDesign_InvoluteGear.md) (Zahnradgenerator) wurde dem [Arbeitsbereich Part Design](PartDesign_Workbench.md) hinzugeügt, um schnell ein Zahnrad mittels Eingabe einiger Parameter zu erstellen.

## Arbeitsbereich Zeichnung 

### Automatische Projektionen 

Im [Arbeitsbereich Zeichnung](Drawing_Workbench/de.md) wurden einige wunderbare Funktionen hinzugefügt. Mit der Funktion [Orthografische Ansichten einfügen](Drawing_Orthoviews.md) können jetzt alle möglichen Ansichten eingefügt werden. Das Einfügen der einzelnen Ansichten lässt sich viel besser steuern als bisher. Eine weitere Hauptfunktion ist die Unterstützung für die Definition von Zeichnungsgrenzen und Titelgrenzen. Eingefügte Projektionen vermeiden so eine Überschneidung mit dem Blattrand oder mit dem Titel.

<img alt="" src=images/DrawingWB.png  style="width:1024px;">

### Symbole

Im [Arbeitsbereich Zeichnung](Drawing_Workbench/de.md) ist die neue Funktion [Zeichnung Symbol](Drawing_Symbol.md) verfügbar, mit der schnell SVG-Objekte auf dem Zeichnungsblatt abgelegt werden können. Da diese Objekte innerhalb des FreeCAD-Dokumentes gespeichert werden, ist es nicht nötig die SVG-Dateien zusätzlich zur FreeCAD-Datei mit zu speichern.

## Arbeitsbereich Rendering 

### Neue Renderingfunktionen 

<img alt="" src=images/Raytracing_example.jpg  style="width:1024px;">

Dem [Arbeitsbereich Rendering](Raytracing_Workbench.md) wurde auch Beachtung geschenkt. Dabei wurde dessen Symbolleiste überarbeitet. Die alten Icons, mit denen manuell einzelne Povraydateien erzeugt werden konnten, wurden entfernt (im Raytracingmenü sind diese immernoch verfügbar). Der Ablauf zum Erstellen neuer Renderings ist nun ähnlich dem Ablauf der Arbeit mit dem [Arbeitsbereich Zeichnung](Drawing_Workbench.md). Ein neues Projekt wird erstellt, eine Vorlage zugewiesen und die verschiedenen Objektansichten hinzugefügt. Dananch muss nur noch das Rendericon angeklickt werden oder das Projekt als Datei exportiert werden, wenn es außerhalb von FreeCAD gerendert werden soll.

Das [Vorlagensystem](Raytracing_Workbench/de#Templates.md) des Arbeitsbereichs Rendering wurde auch erweitert. Vorlagen lassen sich jetzt einfacher erstellen und verändern.

Die von FreeCAD erstellten \*.pov-Dateien beinhalten neu ein automatisches Seitenverhältnis (auto-aspect ratio). Benutzter brauchen jetzt nicht mehr ein 4:3 Seitenverhältnis in den Renderingeinstellungen einzugeben, oder manuell die Ausgabe zu bearbeiten um das Seitenverhältnis zu ändern um sinnvolle Renderings zu erhalten. Jede Breite und Höhe kann und jetzt problemlos eingegeben werden, ohne dass die gerenderten Objekte zusammengedrückt oder auseinandergezogen werden.

### Unterstützung für Luxrender 

Der [Arbeitsbereich Rendering](Raytracing_Workbench/de.md) unterstützt neben [POV-Ray](http://de.wikipedia.org/wiki/POV-Ray) jetzt auch [LuRender](http://de.wikipedia.org/wiki/LuxRender). Im Gegensatz zu dem [klassischer Raytracer](http://de.wikipedia.org/wiki/Raytracing) POV-Ray ist Luxrender ein [unbiased renderer](http://en.wikipedia.org/wiki/Unbiased_rendering) (unverfälschter Renderer), welcher einerseits zwar viel länger braucht um Szenen zu rendern, andererseits aber auch viel realistischere Lichtverhältnisse erzeugt.

## Arbeitsbereich Tabellenkalkulation 

Der [Arbeitsbereich Tabellenkalkulation](Spreadsheet_Workbench/de.md) wurde in FreCAD neu hinzugefügt. Ein neues 2-dimensionale Tabellenkalkulationsobjekt kann mit der Funktion [spreadsheet](Spreadsheet_Create.md) erstellt werden. Es gibt einen Editor, mit dem der Inhalt des Tabellenkalkulationsobjektes bearbeitet werden kann (Text, Zahlen und einige einfache Formeln werden unterstützt). Weiterhin ist ein spezielles [cell controller](Spreadsheet_Controller.md)-Objekt vorhanden, welches ein Dokument auf bestimmte Objekttypen durchsucht und ein bestimmtes Attribut dieses Objekttypes extrahiert und einen vorgegebenen Bereich von Zellen mit diesem Attribut füllt.

<img alt="" src=images/Arch_tutorial_53.jpg  style="width:1024px;">

## Arbeitsbereich Entwurf 

### Im- und Export von DWG Dateien 

FreeCAD kann nun, Dank des kostenlosen, plattformübergreifenden [ODA File Converter](https://www.opendesign.com/guestfiles/oda_file_converter) in das [DWG-Format](https://en.wikipedia.org/wiki/.dwg) importieren und exportieren. Sobald es installiert ist und sein Pfad in den FreeCAD Entwurf Einstellungen festgelegt wurde, kann FreeCAD es zum Importieren und Exportieren von dwg Dateien verwenden, indem es diese in dxf konvertiert und dann den dxf Importeur und Exporteur für den Entwurf verwendet. Der Import und Export von dwg Dateien hat daher die gleichen Begrenzungen wie das [dxf Format](Draft_DXF/de.md).

### Entwurf zu Zeichnung jetzt auch für Gruppen 

Das Werkzeug [Entwurf zu Zeichnung](Draft_Drawing.md), mit dem man Entwurfsobjekte in eine [Zeichnung](Drawing_Workbench/de.md) einfügen kann, kann jetzt auch auf Gruppen angewandt werden, wodurch weniger Ansichtsobjekten benötigt werden. Indem man Entwurfsobjekte geschickt in Gruppen zusammenfasst, kann man schnell das Erscheinungsbild vieler Objekte auf einer Seite anpassen.

### Überarbeite Bemaßungen 

Das [Bemaßungswerkzeug](Draft_Dimension/de.md) wurde komplett überarbeitet. Bemaßungsobjekte verhalten sich jetzt sehr viel besser und haben neue Eigenschaften erhalten, die es erlauben, sie stärker anzupassen, unter anderem schönere und skalierbare Pfeile, bessere Kontrolle über die Position des Textes und die Richtung der Bemaßung und bessere Unterstützung für das [Zeichnungsmodul](Drawing_Workbench/de.md). Man kann Bemaßungen jetzt in jeder Ebene im 3D Raum positioniere und erhält korrekte Ergebnisse wenn sie mit dem [Draft Drawing](Draft_Drawing.md) Werkzeug auf einer Zeichnung platziert werden.

<img alt="" src=images/Draft_dimensions_recode.jpg  style="width:1024px;">

### Schraffuren

Der [Arbeitsbereich Entwurf](Draft_Workbench/de.md) hat noch eine weitere Funktion erhalten: Schraffuren. Es ist nun möglich auf bestimmten Entwurfsobjekten (solche, die eine Fläche begrenzen, z.B. geschlossene Linienzüge, Rechtecke, Polygone und Kreise) Schraffuren aufzubringen. Im Moment sind nur einige der verbreitetsten Schraffurmuster verfügbar, aber da Muster sehr einfach zu erstellen sind (es sind einfach SVG-Dateien) und der Benutzer eigene Muster hinzufügen kann, wird diese Auswahl schnell wachsen. Entwurfsobjekte mit Mustern werden auch vom [Arbeitsbereich Zeichnung](Drawing_Workbench/de.md) voll unterstützt.

<img alt="" src=images/Draft_hatches.jpg  style="width:1024px;">

### Ellipsen

Unterstützung für [Ellipsen](Draft_Ellipse.md) wurde hinzugefügt. Der Arbeitsbereich Entwurf erlaubt es nun vollständige Ellipsen oder Teile davon zu zeichnen.

### Fasen

Ähnlich wie Abrundung, die in [Version 0.13](Release_notes_0.13/de.md) eingeführt wurden, erhalten Rechtecke, Kantenzüge und Polygone nun eine Faseneigenschaft. Die Fase wirkt vor der Abrundung und beide Eigenschaften können gleichzeitig verwendet werden um einen einfachen Kantenzug schnell in ein komplexes Objekt zu verwandeln, das aus vielen Abschnitten besteht.

### Überarbeitetes Herauf- und Herabstufen 

Die [Herauf-](Draft_Upgrade.md) and [Herabstufen](Draft_Downgrade.md) Werkzeuge waren bisher ein Buch mit sieben Siegeln, bei denen man nie wusste, was das Ergebnis sein würde. Sie wurden überarbeitet und geben nun sehr viel hilfreichere Rückmeldung darüber, was sie getan haben und warum. Sie sind jetzt auch von Python Skripten aus nutzbar, und nicht nur als ganzes, sondern auch ihre internen Operationen, so dass man gezielt eine bestimmte Heraufstufung erzwingen kann.

### Flächengruppen

Ein neues Werkzeug zur Erstellung von [Flächengruppen](Draft_Facebinder.md) wurde hinzufügt, das es erlaubt eine Anzahl von markierten Flächen von unterschiedlichen Objekten in einem neuen Objekt zusammenzufassen. Das neue Objekt bleibt mit den Originalobjekten verknüpft, so dass jede Änderung automatisch in der Flächengruppe übernommen wird. Das sollte vor allem für Anwendungen in der [Architektur](Arch_Workbench/de.md) nützlich sein, da man dort neue Objekte aus den Flächen anderer Objekte erstellen kann.

### Textformen

Das [Textformen](Draft_ShapeString.md) Werkzeug erzeugt planare Objekte aus einem Text und einer TrueType Schriftart. Diese Objekte sind im Unterschied zu anderen Annotationen wie [Draft Text](Draft_Text.md) echte 3D Objekte, die extrudiert werden können, um z.B. Gravuren oder andere Arten von 3D Objekten mit Relieftext zu erstellen.

### Bezierkurven

Zu den bereits vorhandenen [Kreisbogen](Draft_Arc/de.md) und [B-spline](Draft_BSpline/de.md) Kurven gesellt sich ein weiterer Kurventyp: [Bezier Kurven](Draft_BezCurve/de.md). Sie können genauso wie andere Objekte im [Arbeitsbereich Entwurf](Draft_Workbench.md) durch Anklicken von Punkten erstellt werden, außerdem können sie dann [bearbeitet](Draft_Edit/de.md) und ihre Kontrollpunkte verändert werden, was eine präzise Kontrolle der Kurvenform erlaubt.

## Arbeitsbereich Architektur 

### Vorlagen und Profile für Strukturbauteile 

Das [Arch Strukturtool](Arch_Structure/de.md) hat mehrere Verbesserungen erhalten. Es sind nun einige Vorlageprofile vorhanden, wodurch es möglich ist sehr schnell eine Stütze oder einen Träger basierend auf einem Standardprofil wie INP oder HEB zu erstellen. Weiterhin wurde das Platzierungssystem um einen speziellen Fangmodus ([snapping](Draft_Snap.md)) erweitert. Strukturelemente können jetzt auch direkt einen Extrusionspfad haben, was sehr komplexe Bauteile möglich macht. Sehr viele der in [BOLTS](#Plugins_and_side_projects:_Parts_library.2C_BOLTS.2C_Eagle_importer.md) vorhandenen Bauteile (u.a. alle Europäische rechteckige, quadratische und runde Hohlprofile sowie Standarddoppel-T-Profile) können direkt als Arch Struktur erzeugt werden.

### Fenstervorlagen

Dem [Fenstertool](Arch_Window.md) wurde ein neues Vorlagensystem hinzugefügt. Da dieses immernoch auf Skizzen beruht, bleibt die maximale Bearbeitbarkeit erhalten. Dies bedeutet jeder vorstellbare Fenstertyp ist erstellbar. Neu ist, dass aus einer Auswahl von Vorlagefenster ausgewählt werden kann. Es brauchen dann nur noch einige Parameter eingegeben zu werden und das Fenster in eine existierende Wand oder in ein Struktruelement platziert werden. Im Hintergrund wird eine passende Skizze erstellt, was die maximale Bearbeitbarkeit für später sicherstellt.

<img alt="" src=images/Screenshot_arch_window.jpg  style="width:1024px;">

### Räume

Ein neues [Raumobjekt](Arch_Space.md) welches es erlaubt Raumvolumen und Geschossflächen zu errechnen ist jetzt verfügbar. Dieses Raumobjekt umfasst immer einen Volumenkörper, somit ist das Raumvolumen und die Bodenfläche immer bekannt. Raumobjekte können aus einfachen Volumenkörpern oder aus einer Zusammenstellung von Grenzflächen erstellt werden.

### Mehrschichtige Wände 

Durch einen einfachen Trick unterstützt jetzt die Funktion [Wände](Arch_Wall.md) auch den mehrschichtigen Aufbau von Wänden. Mehrere Wände nutzen einfach die selbe Basislinie und werden durch einen Abstand zu dieser Basisline positioniert. Wird dies mit [Arch Rahmen](Arch_Frame.md) kombiniert, können sehr komplexe Ständerwände mit Dämmung erstellt werden. Weiterhin sind die mehrschichtigen Wände so untereinander verknüpft, dass Fensteröffnungen in allen Schichten erstellt werden.

<img alt="" src=images/Screenshot_arch_multiwall.jpg  style="width:1024px;">

### Treppen

Mit dem neu hinzugefügten [Treppentool](Arch_Stairs/de.md) ist es möglich auch komplexe Treppen einfach durch die Eingabe einiger Parameter zu erstellen. Aktuell werden nur gerade Treppen unterstützt, aber die Erweiterung auf andere Formen ist geplant und wurde im Forum bereits diskutiert. Das Treppentool hat viele Einstellparameter wie die Grösse der Setzstufe oder den Treppenlauftyp.

### Bewehrungsstäbe

Das Erstellen von Bewehrungsstabverlegungen wurde mit dem [Arch Rebar](Arch_Rebar.md) Tool eingeführt. Da die Form eines Bewehrungsstabes auf Skizzen basiert, kann nahezu jede ebene Stabform einfach erstellt werden. Auf Basis einer Fläche wird mittels einer Skizze die Form des Bewehrungsstabes festgelegt. Mittels Randabständen, Stababständen und/oder Stabanzahl kann dann die Verlegung des Bewehrungsstabes definiert werden.

<img alt="" src=images/Screenshot_arch_rebar.jpg  style="width:1024px;">

### Rahmen

Rahmensysteme (auch Stabsysteme) werden überall in der Architektur verwendet. Einige Beispiele sind Geländer, Fachwerke, Ständerwände, usw. Mit dem neuen [Rahmentool](Arch_Frame.md) können alle möglichen Varianten von Rahmen erstellt werden. Dies geschieht durch Kombinieren eines Profilobjektes, was jede ebene und extrudierbare Form wie beispielsweise Rechteck oder Kreis haben kann, und eines Layoutobjektes, welches die Extrusionslinien entlang denen die Profilobjekte platziert werden definiert. Die Layoutobjekte werden normalerweise mit dem [Arbeitsbereich Skizze](Sketcher_Workbench/de.md) erstellt. Diese Rahmenbauteile können in Wand- oder Strukturobjekte übergeführt werden.

### Messen

Ein einfaches aber nützliches neues Tool des Architekturarbeitsbereiches ist der [Messmodus](Arch_Survey.md). Wird in diesem Modus auf Punkte, Kanten, Flächen oder ganze Körper geklickt erhält man ihre Höhe, Länge, Fläche oder Volumen. Diese Informationen werden direkt am Modell angezeigt, in die Zwischenablage kopiert und als Text im FreeCAD-Ausgabefenster ausgegeben. Somit ist es sehr einfach diese Werte in andere Programme einzufügen und schnell mengenbasierte Kostenschätzungen zu erstellen.

### Tutorial

Ein neues 35 Seiten umfassendes [Tutorial](Arch_tutorial/de.md) bechreibt den [Arbeitsbereich Architektur](Arch_Workbench/de.md) sehr detailliert an Hand eines vollständigen Beispiels.

### Im- und Export von Ifc-Dateien 

Viel Zeit wurde in die Arbeit an FreeCAD und der Arbeit an [IfcOpenShell](http://www.ifcopenshell.org), welches für die Verarbeitung von Ifc-Dateien im [Arch-Arbeitsbereich](Arch_Workbench/de.md) verwendet wird, investiert. Wenn eine [Entwicklerversion](http://github.com/aothms/IfcOpenShell) von IfcOpenShell verwendet wird, können auch komplexe Geometrieen von Ifc-Dateien importiert werden. Erst ab einer mittleren Dateigrösse von ca. 50 MB (unkomprimiert) steigt die Importdauer expotentiell stark an. Mit der oben genannten Entwicklerversion von IfcOpenShell können auch Modelle aus FreeCAD nach Ifc so exportiert werden, dass die meisten grossen CAD-Programme (oder BIM-Plattformen, wie man heutzutage gerne sagt) diese problemlos importieren können.

## Vollständige Liste 

Die vollständige Liste aller Bugfixes und Neuen Funtionen kann [hier](http://freecadweb.org/tracker/changelog_page.php) nachgelesen werden.



---
⏵ [documentation index](../README.md) > [News](Category_News.md) > [Documentation](Category_Documentation.md) > [Releases](Category_Releases.md) > Release notes 0.14/de
