# Release notes 0.15/de
FreeCAD 0.15 wurde am 8. April 2015 veröffentlicht. Dies ist eine Zusammenfassung der interessantesten Entwicklungen. Eine komplette Liste der Änderungen kann unter [Mantis changelog](http://www.freecadweb.org/tracker/changelog_page.php) gefunden werden. Ältere Versionen finden sich unter: [0.14](Release_notes_0.14/de.md) - [0.13](Release_notes_0.13/de.md) - [0.12](Release_notes_0.12.md) - [0.11](Release_notes_0.11/de.md)

<img alt="" src=images/Spark-Plug-Plane.jpg  style="width:1024px;">


<center>

Spark Plug Plane by r-frank


</center>

## Allgemeines

### Suchfeld in der Selektionsansicht 

Das Selektionsfenster erlaubt nun innerhalb der selektierten Objekte zu suchen. Desweiteren hat man nun die Möglichkeit, nur eine Entität zu selektieren oder deselektieren, auf eine Entität zu zoomen oder zu einer Entität in der Baumansicht zu springen.

![](images/FeatureSelectionView.jpg )

### Erweiterte Unterstützung des Einheitensystems 

Das neue [Einheitensystem](Quantity.md) von FreeCAD, das in Version 0.14 eingeführt wurde, wird nun von fast allen Modulen verwendet einschließlich den Modulen [Sketcher](Sketcher_Workbench.md), [Draft](Draft_Workbench.md) oder [Arch](Arch_Workbench.md). Ein paar Bereiche nutzen es noch nicht, aber grundsätzlich kann man nun von einer soliden Unterstützung von Einheiten im gesamten Arbeitsablauf ausgehen.

### Kleinere Verbesserungen 

-   Import/Export hat nun einen Abschnitt unter Edit \> Preferences. All Dateiformate sind nun ihrem eigenen Reiter gruppiert, was das Auffinden der richtigen Optionen für neue Benutzer vereinfacht.
-   Benutzerdefinierte Tastaturkürzel akzeptieren nun bis zu 4 Tasten.
-   FreeCAD unterstützt nun die [VR Occulus Rift](http://forum.freecadweb.org/viewtopic.php?f=9&t=7715) Brille.
-   Unterstützung von globalen Benutzertoolbars: Neben dem Hinzufügen eigener Toolbars mit eigenen Werkzeugen zu jedem Arbeitsbereich ist es nun auch möglich, Toolbars hinzuzufügen, die auf allen Arbeitbereichen sichtbar sind.
-   Neues Bibliothekspaket für Windows mit dem neuesten OCE 0.17.

## Arbeitsbereich Bauteil 

-   Einige neue geometrische Elemente wurden hinzugefügt: Parabel, Parabelbogen, Hyperbel und Hyperbelbogen.

## Arbeitsbereich Bauteil Design & Skizzierer 

### Ellipsen

Der [Skizzierererhielt](Sketcher_Workbench.md) eine solide Unterstützung für Ellipsen. Diese können auf unterschiedliche Arten konstruiert und für nachfolgende Operationen verwendet werden.

![](images/Ellipse-example.png )

### Verbesserte Auswahlwerkzeuge 

Die Skizzierer erhielt eine Reihe von neuen Werkzeugen, die Probleme in Ihren Skizzen diagnostizieren, optimieren oder beheben. Zum Beispiel können Sie nun einfach die Elemente selektieren, die mit einer Beschränkung verbunden sind oder umgekehrt. Ferner können Sie in Konflikt stehende oder redundante Beschränkungen finden.

Die Benutzeroberfläche des Skizzierers erhielt neue Anzeigen und zeigt Ihnen nun eine selektierbare Liste von Elementen in Ihrer Skizze.

### Zusammenführen von Skizzen 

Es ist nun möglich, mit einem Knopfdruck mehrere Skizzen zu einer Skizze zusammenzuführen.

### Verbesserte Skizzeneigenschaften 

Die Eigenschaftsansicht von Skizzierobjekten wurde ebenfalls verbessert. Numerische Skizzenbeschränkungen (Abstand, horizontaler Abstand, vertikaler Abstand) mit Namen erscheinen nun auch direkt in der Eigenschaftsansicht und können dort auch editiert werden, ohne in den Editiermodus wechseln zu müssen.

### Kleinere Verbesserungen 

-   Mehr reguläre Polynome zum Skizzierer hinzugefügt.
-   Neue Beschränkung hinzugefügt: Symmetriebeschränkung senkrecht zur Symmetrieachse.

## Arbeitsbereich Tabellenkalkulation 

Der [Arbeitsbereich Tabellenkalkulation](Spreadsheet_Workbench.md) wurde von Grund auf neu geschrieben. FreeCAD besitzt nun eine moderne, robuste und funktionsreiche Tabellenkalkulation. Ein paar Funkionalitäten der vorhergehenden Version dieses Arbeitsbereichs wurden entfernt, wie etwa der Eigenschaftscontroller. Dies ist eine komplexe Herausforderung, die mehr noch mehr Entwicklungszeit benötigt. Im Moment bietet die neue Tabellenkalkulation bereits weitaus bessere Möglichkeiten, Daten von Ihrem Model zu erhalten.

<img alt="" src=images/Spreadsheet_screenshot.jpg  style="width:640px;">

## Arbeitsbereich 2D Skizze 

### Verwendung von Linienschriftarten im ShapeString 

Für die Nostalgiker alter CAD Software können nun Linienschriftarten (\"sticky fonts\", Buchstaben, die aus Linien anstatt gefüllter Flächen bestehen) mit dem Werkzeug [ShapeString](Draft_ShapeString.md) verwendet werden.

![](images/Stickyfonts.jpg )

### Kleinere Verbesserungen 

-   [Linien](Draft_Line.md) können nun durch ihre Länge und Winkel in der aktuellen Arbeitsebene definiert werden.
-   Relative Erweiterung von Linien für [dimensions](Draft_Snap_Dimensions.md)
-   Unterstützung von [Ellipsen](Sketcher_Ellipse.md)
-   [Array](Draft_Array.md) Objekte können nun verschmolzen werden.

## Arbeitsbereich Zeichnung 

### Export von Zeichnungsseiten nach DXF 

Bis jetzt benutzte das System zum Export von Zeichnungsseiten nach DXF einen sehr komplizierten \"Hack\" um den SVG code zu einem FreeCAD Objekt und dann zurück nach DXF mit den Draft Exportes zu bewerkstelligen. Dies geschieht nun intern innerhalb des Zeichnungsmoduls, was zu schnelleren und zuverlässigeren Ergebnissen führt. Der DXF Export verwendet nun ein [Vorlagensystem](Drawing_templates.md) ähnlich wie SVG Seiten. Wenn Ihre Zeichnung eine bestimmte SVG Vorlage verwendet und es eine DXF Vorlage mit gleichem Namen gibt, wird diese in der DXF Datei verwendet.

![](images/Drawing-dxf-export.jpg )

In der DXF Datei werden die Ansichten als skalierte Blöcke platziert. Dies erlaubt die einfache Rücksetzung auf die 1:1 Skalierung.

### Kleinere Verbesserungen 

-   Es ist nun möglich, Projektionseinstellung von einer existierenden Ansicht wiederzuverwenden, wenn eine neue Zeichnungsansicht erstellt wird.

### Arbeitsbereich Arch 

### Aktualisierter IFC Import/Export 

In FreeCADs [IFC Import](Arch_IFC.md) wurde viel Entwicklungsarbeit gesteckt. Es wurde ausgiebig getestet und massive Verbesserungen vorgenommen. Der alte Python-basierte Import wurde deaktiviert (ist allerdings noch über die Python Konsole erreichbar). FreeCAD benutzt nun ausschließlich und extensiv die allerneueste [version 5](http://ifcopenshell.org/python.html) ([read more](http://ifcopenshell.org/pythonOCC/example1/) about it) von [IfcOpenShell](http://ifcopenshell.org/), die auf allen Hauptplatformen verfügbar ist (Vergewissern Sie sich, dass Sie die richtige Version passend zu Ihrer Python Version der FreeCAD Installation verwenden). Wir profitieren dadurch nun durch viel schnelleren und zuverlässigeren Import, einen einfacheren und saubereren Code (leichetere Erweiterbarkeit) sowie ein paar weiteren Vorteilen wie etwa eine bessere Unterstützung von Kurvenbasierten Objekten und IFC Eigenschaften.

### Neues feature: Objekt mit einer Ebene schneiden 

Diese neue Funktionalität, [Arch CutPlane](Arch_CutPlane.md), macht es möglich, ein Objekt entlang einer Ebene zu schneiden, die durch ein Flächenelement eines anderen Objekts definiert ist. Es ist möglich das Objekt vor oder hinter dieser Fläche abzuscheiden.

![](images/Arch_CutPlane_example.jpg )

### Neues Dachwerkzeug 

Das [Dach](Arch_Roof.md) Werkzeug wurde komplett überarbeitet und bietet nun die Möglichkeit, verschiedene Steigungen für jede Seite das Dachs zu definieren. Ferner kann nun eine Dicke für das Dach sowie die Länge des Dachüberstands festgelegt werden.

![](images/RoofExample.png )

### Panele

Ein neues [Panel](Arch_Panel.md) Objekt wurde zum [Arbeitsbereich Arch](Arch_Workbench.md) hinzugefügt. Es erlaubt die Erzeugung allermöglichen Panel-artigen Objekte und ist besonders nützlich für die Panelkonstruktion wie etwa bei [Wiki Haus](http://www.wikihouse.cc/) oder [Popup Haus](http://www.popup-house.com/) Projekten.

<img alt="" src=images/Arch_Panel_example.jpg  style="width:640px;">

### Möbel

Das neue [Arch Equipment](Arch_Equipment.md) Objekt wurde designt um alle Arten von nicht-strukturellen, alleinstehenden Objekten zu Ihren Architekturprojekten hinzuzufügen. Diese sind zum Beispiel Beleuchtungen, Sanitäreinrichtungen oder Möbel.

### Kleinere Verbesserungen 

-   Der Basispunkt eines [Arch Frame](Arch_Frame.md) Objekts kann nun auf einen spezifischen Vertexpunkt des Profils gesetzt werden.

## Externe Module 

Es gab sehr interessante Entwicklungen an neuen Arbeitsbereichen und Macros, die (noch) nicht in den FreeCAD Quellcode eingeflossen sind aber leicht zu einer existierenen FreeCAD 0.15 Installation hinzugefügt werden können. Anleitungen finden Sie auf den unten erwähnten Seiten.

### Baugruppe 2 

Der [Arbeitsbereich Baugruppe 2](https://github.com/hamish2014/FreeCAD_assembly2) stellt Werkzeuge zur Verfügung, um Baugruppen aus mehreren Bauteilen zu erstellen. Es stellt eine sehr gute Alternative zum offiziellen Arbeitsbereich Baugruppe dar, die noch in der Entwicklung ist (siehe [Forumsthema](http://forum.freecadweb.org/viewtopic.php?f=10&t=8577)).

![](images/Assembly2_example.jpg )

### Zeichungsbemaßung

Der [Arbeitsbereich Zeichnungsbemaßung](https://github.com/hamish2014/FreeCAD_drawing_dimensioning) fügt mächtige Werkzeuge zur Bemaßungs- und Anmerkungserstellung zum Arbeitsbereich Zeichnung (siehe [Forumsthema](http://forum.freecadweb.org/viewtopic.php?f=10&t=8395)).

![](images/Drawing_Dimensioning_example.jpg )

### Arbeitshilfen

Das [WorkFeature Macro](https://github.com/Rentlau/WorkFeature) fügt ein breites Spektrum an Hilfsobjekten wie etwa Konstruktionsebenen oder -achsen hinzu sowie Werkzeuge zur Positionierung und Ausrichtung von Objekten entlang dieser Hilfsobjekte (siehe [Forumsthema](http://forum.freecadweb.org/viewtopic.php?f=22&t=9056)).

<img alt="" src=images/WF.png  style="width:640px;">

[Category:News](Category:News.md) [Category:Documentation](Category:Documentation.md) [Category:Releases](Category:Releases.md)

---
[documentation index](../README.md) > [News](Category:News.md) > Release notes 0.15/de
