# Developer hub/de
![150](images/Crystal_Clear_app_tutorials.png )

Dies ist die Stelle, wenn Du zur Entwicklung der FreeCAD-Software beitragen möchtest.

Diese Seiten sind in einem frühen Stadium. Wenn Du nicht die Informationen findest, nach denen Du suchst oder hilfreiche Informationen an anderer Stelle gefunden hast, auf die wir nicht verwiesen haben, dann hinterlasse bitte einen Kommentar im [Forum](http://forum.freecadweb.org/index.php?sid=5f84150e79db8842e277b042077097ff) und jemand wird danach gucken (oder wenn Du magst, kannst Du diese Seite selbst ändern!).

## Entwicklerdokumentation

Die Entwicklerdokumentation umfasst die folgenden Abschnitte:

### FreeCAD kompilieren 

-   _
-   [Kompilieren mit Docker](Compile_on_Docker.md)
-   [Kompilieren auf Windows](CompileOnWindows/de.md)
-   [Komplieren auf Unix](CompileOnUnix/de.md)
-   [Kompilieren auf Mac OS X](CompileOnMac/de.md)
-   [Lizenz](Licence/de.md) über die FreeCAD Lizenzen
-   [Drittanbieter Bibliotheken](Third_Party_Libraries/de.md)
-   [Drittanbieter Werkzeuge](Third_Party_Tools/de.md)
-   [Programmstart und Konfiguation](Start_up_and_Configuration/de.md)
-   [Quellcode Dokumentation](Source_documentation/de.md)
-   Verwende den [Fehlerverfolger](Tracker/de.md), wenn du ein Problem hast oder glaubst, einen Fehler gefunden zu haben

### Paketerstellung

[Paketerstellung](Packaging/de.md) besteht darin, die kompilierten Binärdateien und Python Quelldateien von FreeCAD zu übernehmen und für die Verwendung in einem bestimmten System zu verteilen.

-   [Linux Paketerstellung](Linux_packaging/de.md)
    -   [Debian Entwicklung](Debian_development/de.md)
    -   [Debian Unstable](Debian_Unstable/de.md)
    -   [Git buildpackage](Git_buildpackage/de.md)
-   [Windows Paketerstellung](Windows_packaging/de.md)
-   [MacOS Paketerstellung](MacOS_packaging/de.md)

### Bau Unterstützungswerkzeuge 

-   Das [FreeCAD Bau Werkzeug](FreeCAD_Build_Tool/de.md)
    -   [Ein Anwendungsmodul hinzufügen](Module_creation/de.md) zu FreeCAD
-   [Fehlersuche](Debugging/de.md) FreeCAD
-   [Testen](Testing/de.md) FreeCAD
-   [Kompilieren (beschleunigen)](Compiling_(Speeding_up)/de.md) FreeCAD
-   [Fortlaufende Integration](Continuous_Integration/de.md)

### FreeCAD ändern 

-   [Den FreeCAD Quellcode](The_FreeCAD_source_code/de.md) verstehen
-   [Patches einreichen](Tracker#Submitting_patches/de.md)
-   [Merkmale](Gui_Command/de.md) zu FreeCAD oder einem Arbeitsbereich hinzufügen
-   [Branding](Branding/de.md) oder *FreeCAD ein unverwechselbares Aussehen geben*
-   [Illustrationen](Artwork/de.md) die wir für FreeCAD erstellen, kannst Du ungehindert wiederverwenden
-   [Illustrationsrichtlinien](Artwork_Guidelines/de.md) Standards für Symbole
-   [FreeCAD übersetzen](Localisation/de.md)
-   [Zusätzliche Python Module](Extra_python_modules/de.md), oder *Wie die Python Funktionalität in FreeCAD erweitern*
-   [Google Summer of Code](Google_Summer_of_Code/de.md) Engagieren über das Schülerförderprogramm von Google
-   [Feinabstimmung](Fine-tuning/de.md) zeigt verschiedene Optionen und Parameterschalter, die Probleme lösen können.

-   [Übersetzen eines externen Arbeitsbereichs](Translating_an_external_workbench/de.md)

### Modul Entwicklerhandbuch 

[FreeCAD Mod Dev Guide](https://github.com/qingfengxia/FreeCAD_Mod_Dev_Guide): Dies ist ein ebook gerade auf github geschrieben , bitte teilen und pull request senden, um beizutragen.

Kapitel:

-   Überblick und Software Architektur
-   Quellcode Struktur
-   Basis und Applikations Module
-   GUI Modul
-   Python Umhüllung
-   Modulares Design
-   FEM Modul Quellen Analyse (C++ und Python gemischt)
-   Entwicklung des CFD Moduls (nur Python)
-   Modul Test und Fehlersuche
-   Code beitragen mit git

Die neueste pdf Vorschau kann aus dem [pdf-Ordner](https://github.com/qingfengxia/FreeCAD_Mod_Dev_Guide/tree/master/pdf) dieses Git Repos heruntergeladen werden.

### Internas

#### OpenCascade Dokumentation 

OpenCascade ist eine Software Entwicklungsplattform für 3D Oberflächen- und Volumenmodellierung, CAD Datenaustausch und Visualisierung, meist in Form von C++ Bibliotheken.

-   [Roman Lygins Tutorien](http://opencascade.wikidot.com/romansarticles)
-   [Komplette Online Dokumentation](https://dev.opencascade.org/cdoc/overview/html/index.html)
-   [Referenzhandbuch](https://dev.opencascade.org/doc/refman/html/index.html)
-   [The openCascade wiki](http://opencascade.wikidot.com) (Enthält gegenwärtig ?? Chinesischen Spam)

#### Dateiformat

_-Geometrie sowie XML-Daten zur Beschreibung des Dokuments enthalten.

#### Skizzierer Löser 

-   [Sketcher Solver Architecture Booklet](https://forum.freecadweb.org/viewtopic.php?f=10&t=36355) (Forum Thread), [source](https://github.com/abdullahtahiriyo/FreeCADBooks/tree/master/FreeCAD_Solver_Architecture) in GitHub.
-   [PlaneGCS solver](https://github.com/FreeCAD/FreeCAD/blob/master/src/Mod/Sketcher/App/planegcs/) im FreeCAD Quellcode; wichtige Dateien sind [GCS.cpp](https://github.com/FreeCAD/FreeCAD/blob/master/src/Mod/Sketcher/App/planegcs/GCS.cpp) und [SubSystem.cpp](https://github.com/FreeCAD/FreeCAD/blob/master/src/Mod/Sketcher/App/planegcs/SubSystem.cpp).
-   [Einige jüngste Skizzierer Verbesserungen](https://forum.freecadweb.org/viewtopic.php?f=9&t=29192).

Der Skizzierer Löser ist nicht perfekt, da es einige Probleme mit numerischer Präzision bei der Verwendung großer Werte gibt, siehe [Abenteuer der Fixierung des Skizzierer Lösers für große Skizzen](https://forum.freecadweb.org/viewtopic.php?f=10&t=40502).

Die Entwicklung einer neuen Löserarchitektur könnte die Verwendung des Lösers sowohl in der [Sketcher Arbeitsbereich](Sketcher_Workbench/de.md) als auch für die Montage von 3D Körpern verbessern. Siehe [Reimplementieren des Beschränkungslösers](https://forum.freecadweb.org/viewtopic.php?f=20&t=40525).

## Fahrplan

FreeCAD, obwohl in bestimmten Bereichen verwendbar, steht am Anfang eines langen Weges in den CAD Mainstream. Es gibt noch viel zu tun um einen Stand zu erreichen, in dem wir mit kommerzieller Software konkurrieren können.

[0.20 Entwicklungszyklus Cycle](0.20_Development_Cycle.md)

## Gemeinschaft

-   [IRC Kanal](irc://chat.freenode.net/freecad) ,synchronisiert mit [gitter channel](https://gitter.im/FreeCAD/FreeCAD)
-   [Entwicklungsforum](https://forum.freecadweb.org/viewforum.php?f=6)

-   [Entwicklungsfahrplan](Development_roadmap/de.md)

## Danksagungen

[Mitwirkende](Contributors/de.md)




_ _

---
[documentation index](../README.md) > [Hubs](Category_Hubs.md) > Developer hub/de
