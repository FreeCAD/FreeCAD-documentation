# Release notes 0.11/de
Dies ist eine Zusammenfassung der wichtigsten Änderungen und Neuerungen der Ausgabe 0.11 von FreeCAD. Eine komplette Liste befindet sich [hier](http://www.freecadweb.org/tracker/changelog_page.php).

<img alt="" src=images/FreeCAD011.png  style="width:800px;">

Ein Bildschirmfoto der Version 0.11

### Allgemein

-   Das [FreeCAD Übersetzungsprojekt](http://crowdin.net/project/freecad) erfuhr große Unterstützung durch viele Menschen auf der ganzen Welt und nun kann FreeCAD mit nicht weniger als 15 Sprachen ausgeliefert werden: Englisch, Deutsch, Französisch, Italienisch, Schwedisch, Spanisch, Portugiesisch, Russisch, Ukrainisch, Norwegisch, Afrikaans, Finnisch, Chinesisch, Kroatisch und Niederländisch. An vielen weiteren Sprachen für die nächste Ausgabe wird gearbeitet.

![](images/release011-translation.jpg )

-   Verschiedene Verbesserungen hat FreeCAD in allen Bereichen erfahren, zum Beispiel ermöglicht der Hierarchiebaum von nun an komplexe Objektstapel, um die Geometriehistorie einwandfrei, gut zugänglich und veränderbar zu halten. Neue Python-API-Verbesserungen erlauben es Objekten besser mit dem Baum zu interagieren, ihr eigenes Verhalten zu bestimmen, Symbole, usw.

![](images/release011-dependency.jpg )

-   Der Kopieren/Einfügen-Mechanismus wurde ebenfalls deutlich verbessert, um das Kopieren/Einfügen von Objekten zwischen Dokumenten zu ermöglichen.
-   Die [Teil Werkbank](Part_Workbench/de.md) weist neue Werkzeuge wie Spiegelung, Kantenverrundung und Fasen auf.

### Skizze und Teilkonstruktion 

-   Der Beschränkungslöser der [Skizzierungswerkbank](Sketcher_Workbench.md) wurde vollkommen neu geschrieben. Der Skizzierer, auch wenn noch nicht vollständig, weist bereits eine gute Auswahl an Werkzeugen für Linien, Rechtecke und Beschränkungen wie das Zusammentreffen von Punkten, Parallelität, feste Länge oder horizontale bzw. vertikale Beschränkungen auf.
-   Zusätzlich zu dem Skizzierer, ermöglicht eine neue TeilKonstruktion Werkbank das schnelle erstellen von Körpern auf Skizzen. Von nun an grundsätzlich ist in FreeCAD alles parametrisch, d.h. Sie können jederzeit zu Änderungen zurückkehren und sämtliche darauf basierende Geometrie wird automatisch angepasst.

![](images/release011-sketcher.jpg )

![](images/Movie.png ) Beispiele: [Skizzierer Demo](http://www.youtube.com/watch?v=hvXupH5bA0E) • [TeilKonstruktion Demo](http://www.youtube.com/watch?v=7ih9Jp3OAwA)

### Roboter-Simulation 

-   Die [Roboter Werkbank](Robot_Workbench/de.md) wurde um viele GUI Werkzeuge erweitert und ist nun ziemlich funktional. Sie erlaubt die einfache Simulation der Bewegungen von Industrierobotern.

![](images/release011-robot.jpg )

### 2D drafting 

-   Snapping has been greatly optimized and now works pretty fast, even on complex objects
-   The \"Trim/Extend\" tool can now be called \"Trim/Extend/Extrude\", since it allows you to quickly extrude single faces, offering a convenient shortcut to the standard Part Extrude tool
-   The Draft-to-Drawing sheet workflow has also been enhanced, all the Draft workbench objects can now be placed on a Drawing page, and they all offer the same level of comfort as standard Part objects, offering the ability to change their position, rotation and scale on the fly. They also offer some extra features, such as hatch pattern fillings

![](images/release011-draft-drawing.jpg )

-   The Draft workbench also offers new tools such as regular polygons and bSplines
-   There is also a new Edit tool, allowing to edit the geometry of most of the Draft objects

![](images/release011-draft.jpg )

-   Dimensions can now have their text edited and moved, and wires can have an end arrow, allowing to use them as leaders
-   Several commands such as move, rotate or dimensioning now allow you to do several copies without exiting the tool
-   The Draft workbench also gained a python [API](Draft_API.md).
-   The DXF importer now support block attributes

![](images/Movie.png ) Examples: [Draft module demo](http://www.youtube.com/watch?v=Q7cG-LQK8Ps)

### Images

-   The image workbench now features an ImagePlane object, allowing you to display an image file inside the 3D scene, that can be used for example to construct geometry on top of scanned blueprints

### Documentation

-   The [FreeCAD manual](Online_Help_Toc.md) now has several well advanced translations. Check the main page!


{{languages/de | {{en|Release_notes_0.11}} {{es|Release_notes_0.11/es}} {{fr|Release_notes_0.11/fr}} {{it|Release_notes_0.11/it}} {{pl|Release_notes_0.11/pl}} {{ru|Release_notes_0.11/ru}} }}

_ _ _

---
[documentation index](../README.md) > [News](Category_News.md) > Release notes 0.11/de
