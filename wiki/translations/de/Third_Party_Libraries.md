# Third Party Libraries/de
{{TOCright}}

## Übersicht

Dies sind Bibliotheken, die FreeCAD als Abhängigkeiten von Dritten während der Kompilierung verwendet. Sie sind normalerweise [dynamisch gelinkte Bibliotheken](https   *//en.wikipedia.org/wiki/Dynamic_loading) und haben eine Erweiterung `.so` in Linux/MacOS und `.dll` in Windows, und werden von ihren Kopfdateien `.h` oder`.hpp` oder ähnlichem begleitet. Wenn eine modifizierte Bibliothek oder eine Hülle erforderlich ist, muss der Code der modifizierten Bibliothek oder der Hülle Teil des FreeCAD Quellcodes werden und zusammen mit diesem kompiliert werden.

Die Abhängigkeiten müssen im System installiert werden, bevor Du mit der Kompilierung fortfahren kannst; siehe [Kompilieren unter Linux](Compile_on_Linux/de.md), [Kompilieren unter Windows](Compile_on_Windows/de.md), und [Kompilieren unter MacOS](Compile_on_MacOS/de.md) für weitere Informationen.

Wenn du unter Windows kompilierst, ziehe es in Betracht, die [LibPack](#LibPack/de.md) zu verwenden, anstatt zu versuchen, die Bibliotheken einzeln zu installieren.

## Verweise


<div class="mw-translate-fuzzy">

++++
| Name der Bibliothek | Notwendige Version      | Verweis für den Bezug                                                         |
+=====================+=========================+===============================================================================+
| Python              | \>= 3.6                 | <http   *//www.python.org/>                                                      |
++++
| Boost               | \>= 1.33                | <http   *//www.boost.org/>                                                       |
++++
| OpenCASCADE         | \>= 7.3                 | <http   *//www.opencascade.org>                                                  |
++++
| Qt                  | \>= 5.4                 | <https   *//www.qt.io/>                                                          |
++++
| Shiboken2           |          | <https   *//wiki.qt.io/Qt_for_Python/Shiboken>                                   |
|                     | **same as Qt** |                                                                               |
|                     |                      |                                                                               |
++++
| PySide2             |          | <https   *//wiki.qt.io/Qt_for_Python/Shiboken>                                   |
|                     | **same as Qt** |                                                                               |
|                     |                      |                                                                               |
++++
| Coin3D              | \>= 3.x                 | <https   *//github.com/coin3d/coin/coin/wiki/Home>                               |
++++
| SoQt (deprecated)   | \>= 1.2                 | <https   *//github.com/coin3d/soqt/>                                             |
++++
| Quarter             | \>= 1.0                 | <https   *//github.com/coin3d/quarter>                                           |
++++
| Pivy                | \>= 0.6.5               | <https   *//github.com/coin3d/pivy/>                                             |
++++
| FreeType            | \>= XXX                 | XXX                                                                           |
++++
| PyCXX               | \>= XXX                 | XXX                                                                           |
++++
| KDL                 | \>= XXX                 | XXX                                                                           |
++++
| Point Cloud Library | \>= XXX                 | XXX                                                                           |
++++
| Salome SMESH        | \>= XXX                 | XXX                                                                           |
++++
| VTK                 | \>= 6.0                 | XXX                                                                           |
++++
| Xerces-C++          | \>= 3.0                 | <https   *//xerces.apache.org/xerces-c/>                                         |
++++
| Eigen3              | \>= 3.0                 | <http   *//eigen.tuxfamily.org/index.php?title=Main_Page>                        |
++++
| Zipios++            | \>= 0.1.5               | <https   *//snapwebsites.org/project/zipios>, <https   *//github.com/Zipios/Zipios> |
++++
| Zlib                | \>= 1.0                 | <http   *//www.zlib.net/>, <https   *//github.com/madler/zlib>                      |
++++
| libarea             | \>= 0.0.20140514-1      | <https   *//github.com/danielfalck/libarea>                                      |
++++
|                     |                         |                                                                               |
++++


</div>

## Details

### Python

**Version   *** 3.3 oder höher

**Lizenz   *** Python 3.3 Lizenz


**Python 2 wurde 2019 nicht mehr gebräuchlich. Die weitere Entwicklung von FreeCAD wird ausschließlich mit Python 3 erfolgen; die Kompatibilität mit Python 2 wird nicht getestet, so dass alte Arbeitsbereiche und Makros, die diese Version verwenden, aktualisiert werden müssen, da sie sonst möglicherweise nicht mehr funktionieren. Bitte melde dich auf der [https   *//forum.freecadweb.org/ FreeCAD forum] wenn Du auf Probleme mit Python 3 stösst.**

Python ist eine beliebte Allzweck-Skriptsprache, die unter Linux und Open-Source-Software weit verbreitet ist. In FreeCAD wird Python während der Kompilierung und auch zur Laufzeit auf unterschiedliche Weise verwendet. Es wird verwendet

-   um Testskripte zu schreiben, um auf verschiedene Bedingungen, wie z.B. Speicherlecks, zu testen, um die Funktionalität der Software nach Änderungen sicherzustellen, für Prüfungen nach Fertigstellung und Testabdeckungstests,
-   zum Schreiben von [Makros](macros/de.md) und zur Makroaufnahme,
-   zur Implementierung von Anwendungslogik für Standardpakete,
-   um Hilfswerkzeuge wie den [Addon-Manager](Std_AddonMgr/de.md) zu implementieren,
-   um ganze Arbeitsbereiche wie [Draft](Draft_Workbench/de.md) und [Arch](Arch_Workbench/de.md) zu implementieren,
-   um Pakete dynamisch zu laden,
-   die Regeln für Gestaltung umzusetzen (Wissensverarbeitung),
-   um ausgefallene Internet Wechselwirkungen wie Arbeitsgruppen und PDM durchzuführen

Unter Linux ist Python normalerweise bereits in deiner Distribution installiert. Für Windows kannst Du eine vorkompilierte Binärdatei von [Python.org](http   *//www.python.org/) beziehen oder [ActiveState Python](http   *//www.activestate.com/) verwenden, obwohl es schwieriger ist, die Fehlerdiagnosebibliotheken von letzterer zu bekommen.

Python wurde aus verschiedenen Gründen als Skriptsprache für FreeCAD gewählt   *

-   Es ist mehr objektorientiert als Perl und Tcl.
-   Der Code ist lesbarer als Perl und Visual Basic.
-   Es ist einfacher in eine andere Anwendung einzubetten, im Gegensatz zu z.B. Java.

Zusammenfassend kann man sagen, dass Python gut dokumentiert ist, und dass es einfach in eine C++ Anwendung eingebettet und erweitert werden kann. Es ist außerdem gut getestet und wird von der Open Source Gemeinschaft stark unterstützt. Lies mehr über Python und durchsuche die offizielle Dokumentation unter [Python.org](http   *//www.python.org).

### Boost

**Version   *** 1.33 oder höher

**Lizenz   *** Boost Software Lizenz - Version 1.0

Die Boost C++ Bibliotheken sind Sammlungen von Fachkollegen geprüften, Open Source Bibliotheken, die die Funktionalität von C++ erweitern. Sie sind für ein breites Spektrum von Anwendungen gedacht und für eine gute Zusammenarbeit mit der C++ Standardbibliothek geeignet. Die Boost Lizenz soll ihre Verwendung sowohl in quelloffenen als auch in quellgeschlossenen Projekte fördern.

Aufgrund ihrer Popularität und Stabilität wurden viele Boost Bibliotheken für die Einbindung in den C++11 Standard akzeptiert, und weitere sind für die Aufnahme in nachfolgende C++ Standards geplant.

Um Effizienz und Flexibilität zu gewährleisten, macht Boost umfangreichen Gebrauch von Vorlagen. Boost hat umfangreiche Arbeiten und Forschungen zur generischen Programmierung und Metaprogrammierung in C++ durchgeführt. Lies mehr über Boost, indem Du die [Boost Homepage](http   *//www.boost.org/) besuchst.

### OpenCASCADE Technologie 

**Version   *** 6.7 oder höher

**Lizenz   *** Version 6.7.0 und später unterliegen der [GNU Lesser General Public License (LGPL) Version 2.1 mit zusätzlicher Ausnahme](https   *//www.opencascade.com/content/licensing). Frühere Versionen verwenden die [Open CASCADE Technologie Öffentliche Lizenz](https   *//www.opencascade.com/content/occt-public-license).

Die OpenCASCADE Technologie (OCCT) ist ein vollwertiger, professioneller CAD Kernel. Er wurde 1993 entwickelt und ursprünglich unter dem Namen CAS.CADE von Matra Datavision in Frankreich für die Anwendungen Strim (Styler) und Euclid Quantum entwickelt. Im Jahr 1999 wurde es als Open Source Software veröffentlicht, und seitdem heißt es OpenCASCADE.

OCCT ist ein großer und komplexer Satz von C++ Bibliotheken, die die von einer CAD Anwendung benötigte Funktionalität bereitstellen   *

-   Ein kompletter STEP konformer Geometriekern.
-   Ein topologisches Datenmodell und die benötigten Funktionen zur Arbeit mit Formen (Schneiden, Verschmelzen, Extrudieren und viele andere).
-   Standardimport- und -exportprozessoren für Dateien wie STEP, IGES, VRML.
-   Ein 2D und 3D Betrachter mit Auswahlunterstützung.
-   Eine Dokumenten und Projektdatenstruktur mit Unterstützung für Speichern und Wiederherstellen, externe Verknüpfung von Dokumenten, Neuberechnung der Konstruktionshistorie (parametrische Modellierung) und die Möglichkeit, neue Datentypen als Erweiterungspaket dynamisch zu laden.

Es gibt zwei Hauptversionen von OpenCASCADE, die in verschiedenen Linux-Distributionen existieren. Eine wird von den ursprünglichen Entwicklern vertrieben; sie ist als OCCT bekannt und wird unter den Namen `occ` oder `occt` gepackt. Die andere Version ist die \"Gemeinschafts Edition\", abgekürzt OCE, und wird normalerweise unter dem Namen `oce` gefunden. FreeCAD kann gegen beide Versionen kompilieren, seit 2016 empfiehlt FreeCAD jedoch, gegen die offiziellen OCCT Bibliotheken und nicht gegen die OCE-Bibliotheken zu kompilieren. Der Grund dafür ist, dass der Gemeinschafts Edition wichtige Fehlerbehebungen und Funktionen fehlen, die die Benutzung von FreeCAD verbessern.

Um mehr zu erfahren, besuche die [OpenCASCADE Webseite](http   *//www.opencascade.org).

### Qt

**Version   *** 4.1 oder höher

**Lizenz   *** GPL v2.0/v3.0 oder kommerziell; ab Version 4.5 auch LPGL v2.1.

Qt ist eines der populärsten Werkzeugsätze für grafische Benutzeroberflächen (GUI), die in der Open Source Welt verfügbar sind. FreeCAD verwendet diesen Werkzeugsatz um die Programmoberfläche zu zeichnen. Hierfür ist die Qt Designer Anwendung sehr nützlich, da sie es Entwicklern erlaubt, die Dialoge und Fenster schnell zu zeichnen, sie als XML Ressource Dateien zu exportieren und diese Schnittstellen zur Laufzeit zu laden.

Weitere Informationen zu den Qt-Bibliotheken und deren Programmierdokumentation findest Du unter [Qt-Dokumentation](https   *//doc.qt.io/?hsCtaTracking=f641fd1a-772b-4957-964b-dad954b8d702%7C46c97dac-f1f6-49b3-ae46-8070fc35ea13).

##### Shiboken2 und Pyside2 

Shiboken ist der Python Bindungsgenerator, den Qt für Python zur Erstellung des PySide Moduls verwendet, d.h. es ist das System, das verwendet wird, um die Qt C++ API der Sprache Python auszusetzen.

Die ursprünglichen Shiboken und PySide Pakete waren für die Verwendung mit Python 2 und Qt4 gedacht; da diese beiden Versionen 2019 als veraltet gelten, verwende bitte Shiboken2 und PySide2, die mit Python 3 und Qt5 funktionieren. Die Neuentwicklung von FreeCAD erfolgt mit Python 3 und Qt5, daher ist die Kompatibilität mit Python 2 und Qt4 nach FreeCAD 0.18 nicht mehr gewährleistet.

Lies mehr über Shiboken und Pyside auf [Qt für Python](https   *//wiki.qt.io/Qt_for_Python/Shiboken).

### Coin3D

**Version   *** 3.0 oder höher

**Lizenz   *** BSD 3-Klausel Lizenz

Coin3D ist eine hochgradige 3D Grafikbibliothek mit einer C++ Programmierschnittstelle. Sie verwendet szenegraphische Datenstrukturen, um Echtzeit Grafiken für alle Arten von wissenschaftlichen und technischen Visualisierungsanwendungen zu erstellen.

Coin3D basiert auf dem Industriestandard OpenGL Sofortmodus Wiedergabe Bibliothek und fügt Abstraktionen für übergeordnete Grundelemente hinzu, bietet 3D Interaktivität und enthält viele komplexe Optimierungsfunktionen für schnelle Wiedergabe, die für den Anwendungsprogrammierer transparent sind.

Coin3D ist kompatibel mit der Open Inventor 2.1 API von SGI. Diese API hat sich zur De-facto Standard Grafikschnittstelle für die 3D Visualisierung in der wissenschaftlichen und technischen Gemeinschaft entwickelt. Sie hat sich seit dem Jahr 2000 als ein wichtiger Baustein in tausenden von Ingenieuranwendungen weltweit bewährt.

Coin3D (Open Inventor) wird als 3D Betrachter in FreeCAD verwendet, da der OpenCASCADE Betrachter (AIS und Graphics3D) insbesondere bei großflächigem Ingenieurwissenschaftlichen Wiedergabe, Einschränkungen und Leistungsengpässe aufweist; andere Dinge wie Texturen oder volumetrische Wiedergabe werden vom OpenCASCADE Betrachter nicht vollständig unterstützt.

Coin3D ist über eine Vielzahl von Plattformen anwendbar   * UNIX, Linux, BSD, MacOS X und Microsoft Windows Betriebssysteme. Um mehr über diese Bibliothek zu lesen, besuche [Coin3D homepage](https   *//github.com/coin3d/coin).

#### SoQt (veraltet) 

**Version   *** 1.2.0 oder höher

**Lizenz   *** BSD 3-Klausel Lizenz

SoQt ist die Coin3D (Open Inventor) Anbindung an den Qt GUI Werkzeugkasten.

SoQt wird in FreeCAD nicht mehr verwendet, es wurde durch Quarter ersetzt, welches eine neuere Qt Bindung ist.

#### Quarter

**Version   *** 1.0 oder höher

**Lizenz   *** BSD 3-Klausel Lizenz

Quarter ist eine neuere Coin3D Bindung an den Qt Werkzeugkasten. Eine Version davon ist im Quellcode von FreeCAD enthalten, so dass es zusammen mit diesem kompiliert wird.

#### Pivy

**Version   *** 0.6.3 oder höher

**Lizenz   *** BSD 3-Klausel Lizenz

[Pivy](Pivy/de.md) ist eine Bibliothek, die die Coin3d Bibliothek zur Verwendung in [Python](Python/de.md) umhüllt. Sie wird nicht benötigt, um FreeCAD zu bauen oder zu starten, aber sie wird als Laufzeit Abhängigkeit von der [Arbeitsbereich Entwurf](Draft_Workbench/de.md), und von anderen Arbeitsbereichen, die sie intern verwenden, wie [Arch](Arch_Workbench/de.md) und [BIM](BIM_Workbench/de.md) benötigt.

Wenn du diese Arbeitsbereiche nicht benutzen willst, brauchst du Pivy nicht.

### Ply

**Version   *** 3.11 oder höher

**Lizenz   *** BSD 3-Klausel Lizenz

Ply ist der Python-Lex-Yacc Parser. Er wird als Laufzeitabhängigkeit von der [OpenSCAD Arbeitsbereich](OpenSCAD_Workbench/de.md) verwendet. Wenn du diesen Arbeitsbereich nicht verwendest, benötigst du dieses Paket möglicherweise nicht.

Für weitere Informationen siehe [Ply homepage](https   *//www.dabeaz.com/ply/).

### Xerces-C++ 

**Version   *** 3.0 oder höher

**Lizenz   *** Apache Software Lizenz Version 2.0

Xerces-C++ ist ein validierender XML Parser, der in einer portablen Untermenge von C++ geschrieben ist. Xerces-C++ macht es einfach, deiner Anwendung die Möglichkeit zu geben, XML Daten zu lesen und zu schreiben. Eine gemeinsame Bibliothek wird für das Parsen, Generieren, Manipulieren und Validieren von XML Dokumenten bereitgestellt. Xerces-C++ ist konform mit der XML 1.0 Empfehlung und den damit verbundenen Standards.

The parser is used for saving and restoring parameters in FreeCAD. For more information see [Xerces-C++ homepage](https   *//xerces.apache.org/xerces-c/).

### Eigen3

**Version   *** 3.0 oder höher

**Lizenz   *** Ab der Version 3.1.1 ist sie unter der [Mozilla Public License 2.0](http   *//www.mozilla.org/MPL/2.0) lizenziert. Frühere Versionen waren unter der [GNU Lesser General Public License 3](https   *//www.gnu.org/licenses/lgpl-3.0.en.html) lizenziert.

Eigen ist eine C++ Vorlagenbibliothek für lineare Algebra   * Matrizen, Vektoren, numerische Löser und verwandte Algorithmen.

Wenn Du nur Eigen verwenden möchtest, kannst Du die Kopfzeilen Dateien sofort verwenden. Es gibt keine binäre Bibliothek zum Verknüpfen und keine konfigurierte Kopfzeilen Datei. Eigen ist eine reine Vorlagen Bibliothek, die in den Kopfzeilen definiert ist.

Eigen wird in FreeCAD für viele Vektoroperationen im 3D Raum verwendet. Um mehr zu erfahren, besuche [Eigen Homepage](http   *//eigen.tuxfamily.org/index.php?title=Main_Page).

### Zipios++

**Version   *** 0.1.5 oder höher

**Lizenz   *** GNU Lesser General Public License 2.1

Zipios++ ist eine C++ Bibliothek zum Lesen und Schreiben von `.zip` Dateien. Der Zugriff auf einzelne Einträge erfolgt über Standard C++ iostreams. Ein einfaches, schreibgeschütztes virtuelles Dateisystem, das reguläre Verzeichnisse und `.zip` Dateien einhängt, wird ebenfalls zur Verfügung gestellt. Die Struktur und die öffentliche Schnittstelle von Zipios++ basiert lose auf dem `java.util.zip` Paket von Java.

FreeCADs ursprüngliches Dateiformat `.FCstd` ist in Wirklichkeit eine `.zip` Datei, die andere Datentypen darin speichert und komprimiert, wie z.B. BREP und XML Dateien. Daher wird Zipios++ zum Speichern und Öffnen von komprimierten Archiven, einschließlich FreeCAD Dateien, verwendet.

Eine Kopie von Zipios++ ist im Quellcode von FreeCAD enthalten, so dass es zusammen mit diesem kompiliert wird. Wenn Du eine externe Zipios++-Bibliothek verwenden willst, die von deinem Betriebssystem zur Verfügung gestellt wird, kannst Du -DFREECAD_USE_EXTERNAL_ZIPIOS=ON mit `cmake` setzen.

Zipios++ verwendet die Zlib Bibliothek, um die eigentliche Dekomprimierung von Dateien durchzuführen.

#### Zlib

**Version   *** 1.0 oder höher

**Lizenz   *** zlib lizenz

Zlib ist als eine freie, verlustfreie, universell einsetzbare Datenkompressionsbibliothek für die Verwendung auf jeder Computer Hardware und jedem Betriebssystem konzipiert. Sie implementiert den `DEFLATE` Kompressionsalgorithmus, der üblicherweise in `.zip` und `.gzip` Dateien verwendet wird.

A copy of this library is included in the source code of FreeCAD so it is compiled together with it.

### libarea

**Version   *** 0.0.20140514-1 oder höher

**Lizenz   *** BSD 3-Klausel Lizenz

Libarea ist eine Software Bibliothek zur Berechnung von Profil- und Taschenoperationen, die in der computerunterstützten Fertigung (CAM) eingesetzt werden. Sie wurde von Dan Heeks für sein HeeksCNC Projekt erstellt.

Eine Kopie der Bibliothek ist im Quellcode der [Path Arbeitsbereich](Path_Workbench.md) enthalten, so dass sie zusammen mit dieser kompiliert wird.

## LibPack

LibPack ist ein praktisches Paket mit den gesammelten Bau Abhängigkeiten von FreeCAD. Es wird nur benötigt, wenn Du FreeCAD unter Windows mit Visual Studio 2015 und höher kompilierst. Du kannst das aktuelle LibPack auf der [releases page](https   *//github.com/FreeCAD/FreeCAD/releases) finden.

Wenn du unter Linux arbeitest, brauchst du das LibPack nicht, da du die Abhängigkeiten aus den Repositorien deiner Distribution beziehen kannst, wie auf der [Kompilieren unter Linux](Compile_on_Linux/de.md)-Seite erwähnt.

### FreeCAD 12.1.2 

Siehe die Ankündigung im Forum   * [Neue Libpacks für Windows mit Qt5.12, OCC7.3 und Python 3.6 von apeltauer](https   *//forum.freecadweb.org/viewtopic.php?f=4&t=35789)

Siehe die Ankündigung im Forum   * [Neue Libpacks für Windows mit Qt5.12, OCC7.3 und Python 3.6 von apeltauer](https   *//forum.freecadweb.org/viewtopic.php?f=4&t=35789) Es enthält unter anderem Boost 1.67, Coin3D 4.0.0a, Eigen3, Open CASCADE Technologie 7.3.0, Python 3.6.8, PySide2, Qt 5.12.1, Salome SMESH, Shiboken2, vtk7, Xerces-C, Zipios++, zlib 1.2.11





 

[Category   *Developer Documentation](Category_Developer_Documentation.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > Third Party Libraries/de
