# Feature list/de
<div class="mw-translate-fuzzy">

Dies ist eine umfangreiche, aber nicht vollständige Liste von Funktionen, die FreeCAD einführt. Wenn du einen Blick in die Zukunft werfen willst, schau dir den [Entwicklungsfahrplan](Development_roadmap/de.md) an, um einen schnellen Überblick über das zu bekommen, was als nächstes kommt. Auch die [Bildschirmfotos](Screenshots/de.md) sind eine nette Anlaufstelle.


</div>


{{TOCright}}

## Versionshinweise


<div class="mw-translate-fuzzy">

-   [Version 0.20](Release_notes_0.20/de.md) - Zu definieren
-   [Version 0.19](Release_notes_0.19/de.md) - März 2021
-   [Version 0.18](Release_notes_0.18/de.md) - März 2019
-   [Version 0.17](Release_notes_0.17/de.md) - April 2018
-   [Version 0.16](Release_notes_0.16/de.md) - April 2016
-   [Version 0.15](Release_notes_0.15/de.md) - März 2015
-   [Version 0.14](Release_notes_0.14/de.md) - März 2014
-   [Version 0.13](Release_notes_0.13/de.md) - Januar 2013
-   [Version 0.12](Release_notes_0.12.md) - Dezember 2011
-   [Version 0.11](Release_notes_0.11/de.md) - März 2011


</div>

## Schlüsselfunktionen


<div class="mw-translate-fuzzy">

-   ![](images/Feature1.jpg ) Ein vollständiger [Open CASCADE Technologie](https   *//de.wikipedia.org/wiki/Open_CASCADE_Technology)-basierter **Geometriekernel**, der komplexe 3D Arbeitsabläufe auf komplexen Formtypen ermöglicht, mit eigener Unterstützung für Konzepte wie [Begrenzungsflächenmodell](https   *//de.wikipedia.org/wiki/Boundary_Representation) (BREP), [Nicht-uniforme rationale B-Splines](https   *//de.wikipedia.org/wiki/Non-Uniform_Rational_B-Spline) (NURBS) Kurven und Oberflächen, eine ausgedehnter Bereich von geometrischen Gebilden, boolesche Operationen und [Verrundungen](https   *//en.wikipedia.org/wiki/Fillet_(mechanics)), und eingebaute Unterstützung der Formate [STEP](https   *//de.wikipedia.org/wiki/Standard_for_the_exchange_of_product_model_data) und [IGES](https   *//de.wikipedia.org/wiki/Initial_Graphics_Exchange_Specification) 
-   ![](images/Feature3.jpg ) Ein vollständig **parametrisches Modell**. Alle FreeCAD Objekte sind von sich aus parametrisch, d.h. ihre Form kann auf [Eigenschaften](Property/de.md) basieren oder sogar von anderen Objekten abhängen. Alle Änderungen werden bei Bedarf neu berechnet und durch einen Rückgängig/Wiederholen Stapel aufgezeichnet. Neue Objekttypen lassen sich leicht hinzufügen und können sogar [voll in Python programmiert](Scripted_objects/de.md) werden.
-   ![](images/Feature4.jpg ) Eine **modulare Architektur**, die es Zusatzprogramm Erweiterungen (Module) erlaubt, Funktionalität der Kernanwendung hinzuzufügen. Eine Erweiterung kann so komplex sein wie eine ganz neue, in C++ programmierte Anwendung oder so einfach wie ein [Python Skript](Power_users_hub/de.md) oder selbstaufgezeichnete [Makros](Macros/de.md). Du hast vollständigen Zugriff auf fast jeden Teil von FreeCAD über den eingebauten **Python** Interpreter, Makros oder externe Skripte, sei es [Geometrieerstellung und Transformation](Topological_data_scripting/de.md), die 2D oder 3D Darstellung dieser Geometrie ([Szenengraph](scenegraph/de.md)) oder sogar das [FreeCAD Oberfläche](PySide/de.md) 
-   ![](images/Feature5.jpg ) Import/Export in **Standardformate** wie [STEP](http   *//en.wikipedia.org/wiki/ISO_10303), [IGES](http   *//en.wikipedia.org/wiki/IGES), [OBJ](http   *//en.wikipedia.org/wiki/Obj), [STL](http   *//en.wikipedia.org/wiki/STL_%28file_format%29), [DXF](http   *//en.wikipedia.org/wiki/Dxf), [SVG](http   *//en.wikipedia.org/wiki/Svg), \[<http   *//en.wikipedia>. org/wiki/STL\_(file\_format) STL\], [DAE](http   *//en.wikipedia.org/wiki/COLLADA), [IFC](http   *//en.wikipedia.org/wiki/Industry_Foundation_Classes) oder [OFF](http   *//people.sc.fsu.edu/~jburkardt/data/off/off.html), [NASTRAN](http   *//en.wikipedia.org/wiki/NASTRAN), [VRML](http   *//en.wikipedia.org/wiki/VRML) zusätzlich zu FreeCADs eigenem **[FCStd](File_Format_FCStd/de.md)** Dateiformat. Das Niveau der Kompatibilität zwischen FreeCAD und einem bestimmten Dateiformat kann variieren, da es von dem Modul abhängt, das es implementiert.
-   ![](images/Feature7.jpg ) Ein [Skkizzierer](Sketcher_Workbench/de.md) mit integriertem Beschränkungslöser, der dir das skizzieren geometrisch-beschränkter 2D Formen erlaubt. Die mit dem Sizzierer erstellten beschränkten 2D Formen können dann als Basis für die Erstellung anderer Objekte durchweg in FreeCAD verwendet werden.
-   ![](images/Feature9.jpg ) Ein [Robotersimulations](Robot_Workbench/de.md) Modul, das dir erlaubt Roboterbewegungen in einer grafischen Umgebung studieren zu können.
-   ![](images/Feature8.jpg ) Ein [Arbeitsbereich TechnischeZeichnung](TechDraw_Workbench/de.md) mit Optionen für Detailansichten, Querschnittsansichten, Bemaßung u.a., das dir erlaubt 2D Ansichten von vorhandenen 3D Modellen erzeugen zu können. Das Modul erzeugt dann exportfertige SVG oder PDF Dateien. Ein älteres [Zeichnungsmodul](Drawing_Workbench/de.md) mit spärlichen Gui-Befehlen, aber einer leistungsfähigen Python Funktionalität ist ebenfalls vorhanden.
-   ![](images/Feature-raytracing.jpg ) Ein [Bildsynthes](Raytracing_Workbench/de.md) Modul, das 3D Objekte zum Rendern mit externen Renderern exportieren kann. Es unterstützt derzeit nur [povray](http   *//en.wikipedia.org/wiki/POV-Ray) und [LuxRender](http   *//en.wikipedia.org/wiki/LuxRender), soll aber in Zukunft auf andere Renderer erweitert werden.
-   ![](images/Feature-arch.jpg ) Ein [Architektur](Arch_Workbench/de.md) Modul, das [Bauwerksdatenmodellierung](https   *//de.wikipedia.org/wiki/Building_Information_Modeling) (BIM) ähnliche Arbeitsabläufe ermöglicht, mit [Industry Foundation Classes](https   *//de.wikipedia.org/wiki/Industry_Foundation_Classes) (IFC) Kompatibilität.
-   ![](images/Feature-CAM.jpg ) Ein [Pfad Modul](Path_Workbench/de.md) für die mechanische Bearbeitung für [Computerunterstützte Fertigung](https   *//de.wikipedia.org/wiki/Computer-aided_manufacturing) (CAM). Durch Verwendung des Pfadmoduls kannst du den [G-Code](http   *//en.wikipedia.org/wiki/G-code), der zur Steuerung der Zielmaschine verwendet wird, ausgeben, anzeigen und anpassen. 
-   ![](images/Feature_spreadsheet.png ) Eine [Integrierte Kalkulationstabelle](Spreadsheet_Workbench/de.md) und ein [Ausdruck Syntaxanalysierer](Expressions/de.md), die zur Steuerung formelbasierter Modelle und zur Organisation von Modelldaten an einem zentralen Ort verwendet werden können.


</div>

## Allgemeine Funktionen 

-   **Multiplattform**. FreeCAD läuft und verhält sich auf Windows, Linux, macOS und anderen Plattformen genau gleich.

-   **Vollständige GUI Anwendung**. FreeCAD hat eine komplette grafische Benutzeroberfläche basierend auf dem [Qt](http   *//www.qt.io/) Rahmenwerk, mit einem 3D Betrachter basierend auf [Open Inventor](https   *//de.wikipedia.org/wiki/Open_Inventor); die ein schnelles Rendern von 3D Szenen und eine sehr zugängliche Darstellung von Szenegraphen erlaubt.

-   **läuft auch als Kommandozeilen Anwendung**. Im Kommandozeilenmodus läuft FreeCAD ohne seine Oberfläche, aber mit all seinen Geometriewerkzeugen. In diesem Modus hat es einen relativ geringen Speicherplatzbedarf und kann zum Beispiel als Server verwendet werden, um Inhalte für andere Anwendungen zu produzieren.

-   **kann als ein [Python Modul](Embedding_FreeCAD/de.md)**. FreeCAD kann in jede Anwendung importiert werden, die Python Skripte ausführen kann. Wie im Befehlszeilenmodus ist der Oberflächenteil von FreeCAD nicht verfügbar, aber alle Geometriewerkzeuge sind zugänglich.


<div class="mw-translate-fuzzy">

-   **Arbeitsbereich Konzept**. In der FreeCAD Oberfläche, sind Werkzeuge in [Arbeitsbereichen](Workbenches/de.md) gruppiert. Dies erlaubt dir nur die Werkzeuge anzeigen, die für eine bestimmte Aufgabe benötigt werden, wodurch der Arbeitsbereich übersichtlich und reaktionsschnell bleibt und die Anwendung schnell geladen werden kann.


</div>

-   **Zusatzprogramm/Modul Rahmenwerk für spätes Laden von Funktionen/Daten-Typen**. FreeCAD ist unterteilt in eine Kernanwendung mit Modulen, die nur bei Bedarf geladen werden. Fast alle Werkzeuge und Geometrietypen sind in Modulen hinterlegt. Module verhalten sich wie Zusatzprogramme; zusätzlich zum verzögerten Laden können einzelne Module zu einer bestehenden FreeCAD Installation hinzugefügt oder von ihr entfernt werden.

-   **parametrisch assoziative Dokumentobjekte**. Alle Objekte in einem FreeCAD Dokument können durch Parameter festgelegt werden. Diese Parameter können jederzeit geändert und neu berechnet werden. Da Objektbeziehungen gewahrt werden, wirkt sich die Änderung eines Objekts automatisch auf alle abhängigen Objekte aus.

-   **parametrische Grundelementerstellung**. Grundelementobjekte wie Kasten, Kugel, Zylinder usw. können durch die Angabe ihrer Geometriebeschränkungen erstellt werden.


<div class="mw-translate-fuzzy">

-   **Grafische Änderungsabläufe**. FreeCAD kann Translation, Rotation, Skalierung, Spiegelung, Versatz (entweder trivial oder wie in [Jung/Shin/Choi](https   *//www.researchgate.net/publication/240754626_Self-intersection_Removal_in_Triangular_Mesh_Offsetting) beschrieben) oder Formänderung in jeder Ebene des 3D Raums durchführen.


</div>

-   **[Konstruktive Festkörpergeometrie](Constructive_solid_geometry/de.md) (Boolesche Operationen)**. FreeCAD kann konstruktive Volumengeometrieoperationen durchführen (Vereinigung, Differenz, Schnittmenge).


<div class="mw-translate-fuzzy">

-   **grafische Erstellung von Planargeometrie**. Linien, Drähte, Rechtecke, B-Splines, kreisförmige oder elliptische Bögen können grafisch in jeder Ebene des 3D Raums erzeugt werden.


</div>

-   **Modellierung mit geraden oder gedrehten** **Extrusionen**, **Abschnitten** und **Verrundungen**.

**topologische Komponenten** wie **Knoten**, **Kanten**, *\'Drähte* und **Ebenen**.


<div class="mw-translate-fuzzy">

-   **Prüfen und Reparieren**. FreeCAD verfügt über Werkzeuge zum Testen von Netzen (Festkörper Test, Nicht zwei Sammler Test, Selbstverschneidetest) und zum Reparieren von Netzen (Lochfüllung, einheitliche Ausrichtung).


</div>


<div class="mw-translate-fuzzy">

-   **Anmerkungen**. FreeCAD kann Anmerkungen für Text oder Bemaßungen einfügen.


</div>

-   **Rückgängig/Wiederherstellen Rahmenwerk**. Alles in FreeCAD ist rückgängig zu machen/wiederherstellbar, mit Benutzerzugriff auf den Rückgängig Stapel. Mehrere Schritte können gleichzeitig rückgängig gemacht werden.

-   **Transaktionsorientiert**. Der Rückgängig/Wiederherstellen Stapel bevorratet Dokumenttransaktionen und nicht einzelne Aktionen, jedem Werkzeug erlaubend, genau festzulegen, was rückgängig gemacht oder wiederhergestellt werden muss.

-   **Einbau [Skripterstellung](Scripting/de.md) Rahmenwerk**. FreeCAD verfügt über einen eingebauten [Python](http   *//www.python.org/) Interpreter mit einer API, die fast jeden Teil der Anwendung, die Oberflächee, die Geometrie und die Darstellung dieser Geometrie im 3D Betrachter abdeckt. Der Interpreter kann sowohl komplexe Skripte als auch einzelne Befehle ausführen; ganze Module können vollständig in Python programmiert werden.


<div class="mw-translate-fuzzy">

-   **eingebaute Python Konsole**. Der Python Interpreter schließt eine Konsole mit Syntaxhervorhebung, Autovervollständigung und einen Klassenbrowser ein. Python Befehle können direkt in FreeCAD ausgegeben werden und geben sofort Ergebnisse zurück, erlaubt es Skriptschreibern, Funktionalität im laufenden Betrieb zu testen, den Inhalt von FreeCADs Modulen zu erforschen und auf einfache Weise mehr über FreeCAD Interna zu erfahren.


</div>


<div class="mw-translate-fuzzy">

-   **spiegelt die Benutzerinteraktion**. Alles, was der Benutzer in der FreeCAD Oberfläche macht, führt Python Code aus, der auf der Konsole ausgegeben und in Makros aufgezeichnet werden kann.


</div>

-   **Vollständige [Makro](Macros/de.md) Aufzeichnungs und Bearbeitungs** Fähigkeiten. Die Python Befehle, die ausgegeben werden, wenn der Benutzer die Oberfläche verändert, können aufgezeichnet, bei Bedarf bearbeitet und für eine spätere Wiederholung gespeichert werden.


<div class="mw-translate-fuzzy">

-   **Verbund (ZIP basiertes) Dokument Speicherformat**. FreeCAD Dokumente werden mit der **.[FCStd](File_Format_FCStd/de.md)** Erweiterung gespeichert. Das Dokument kann viele verschiedene Arten von Informationen wie Geometrie, Skripte oder Miniaturansichtssymbole enthalten. Die **.FCStd** Datei ist selbst ein zip Behälter; eine gespeicherte FreeCAD Datei ist bereits komprimiert.


</div>

-   **vollständig anpassbare/skriptfähige grafische Benutzeroberfläche**. Die [Qt](https   *//www.qt.io)-basierte Oberfläche von FreeCAD ist über den Python Interpreter vollständig zugänglich. Neben einfachen Funktionen, die FreeCAD selbst Arbeitsbereichen zur Verfügung stellt, ist das gesamte Qt Rahmenwerk zugänglich. Der Benutzer kann jede beliebige Operation auf der GUI ausführen, wie z.B. das Erstellen, Hinzufügen, Andocken, Ändern oder Entfernen von Widgets und Werkzeugleisten.

-   **Vorschaubildner** (derzeit nur Linux Systeme) FreeCAD Dokumentensymbole zeigen den Inhalt der Datei in den meisten Dateimanager Anwendungen wie Gnomes Nautilus an.


<div class="mw-translate-fuzzy">

-   **modularer MSI Installierer**. Das FreeCAD Installationsprogramm ermöglicht eine flexible Installation auf Windows Systemen. Pakete für Ubuntu Systeme werden ebenfalls gepflegt.


</div>

## Extra Workbenches 


<div class="mw-translate-fuzzy">

## Zusätzliche Arbeitsbereiche 

Erfahrene Nutzer haben verschiedene [externe Arbeitsbereiche](external_workbenches/de.md) entwickelt.


</div>







[Category   *User Documentation](Category_User_Documentation.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [User Documentation](Category_User Documentation.md) > Feature list/de
