# Release notes 0.16/de
FreeCAD 0.16 wurde am 18. April 2016 veröffentlicht, man kann es von der [Github](https://github.com/FreeCAD/FreeCAD/releases)-Seite herunterladen. Dies ist eine Zusammenfassung der interessantesten Änderungen. Die komplette Liste der Änderungen kann man im [Mantis changelog](http://www.freecadweb.org/tracker/changelog_page.php) finden. Ältere Versionen: [0.15](Release_notes_0.15/de.md) - [0.14](Release_notes_0.14/de.md) - [0.13](Release_notes_0.13/de.md) - [0.12](Release_notes_0.12/de.md) - [0.11](Release_notes_0.11/de.md)
<img alt="" src=images/Satnogs_Rotator_FreeCAD.jpg  style="width:1024px;">


<center>

Satnogs Rotator (https://satnogs.org/)


</center>

## Highlights

**Expression support** wurde eingeführt. Es erlaubt das Definieren von Formel-gestützten Beziehungen zwischen Objekteigenschaften. \"Expression support\" ist ein großer Sprung vorwärts, um bessere parametrische Modelle in FreeCAD zu erstellen. Expressions bietet ein benutzerfreundliches Interface, um Modelle zu erstellen, die durch eine Tabelle (mittels Spreadsheet Workbench) gesteuert werden.

<img alt="" src=images/Expressions-demo.png  style="width:300px;">

\"Sketcher Solver (Skizzen-Gleichungslöser)\" wurde im Verhalten stark verbessert. Es wurde nicht nur schneller und stabiler, auch sollten nun keine Abstürze mehr bei unlösbaren Skizzen erfolgen. Automatischer Neuaufbau der Skizzen nach jeder geringfügigen Änderung kann nun abgeschaltet werden, was das flüssige Editieren von Skizzen mit sehr vielen Abhängigkeiten erlaubt.

<img alt="" src=images/Sketcher-v0.16-demo.png  style="width:300px;">

FreeCAD unterstützt nun Touchscreen 3D Navigation. Dies ermöglicht es, FreeCAD ohne eine Maus auf einem Laptop mit Touchscreen und Stift zu benutzen, abseits des Schreibtisches.

Der Arbeitsbereich \"FEM\" hat ebenfalls viele Verbesserungen erhalten. Er hat sich bewährt zur Durchführung von verschiedenen Arten mechanischer Analysen.

<img alt="" src=images/Multiple_material.jpg  style="width:700px;">

## Allgemein

-   Unterstützung für Ausdrücke/Formeln
-   Drei neue Navigations-Stile: Gesture-Navigation (mit Touchscreen-Unterstützung unter Windows), Maya Navigation und OpenCascade Navigation
-   Personalisierung der Arbeitsbereich-Liste (Liste kann umgeordnet werden, und jeder Arbeitsberich der Liste kann ausgeblendet werden)
-   Wiederherstellungs-Werkzeug
-   Neue Speicherungs-Optionen(Rückgängig, Speichern einer Kopie)
-   Neugestaltung der Homepage

## Arbeitsbereich \"Part\" (Formteil) 

-   Neue Werkzeuge um Objekte mit einer Wandstärke (z.B. Rohre) zu verbinden: [Connect](Part_JoinConnect.md), [Embed](Part_JoinEmbed.md) und [Cutout](Part_JoinCutout.md)
-   Neues Werkzeug: Erstelle Fläche von Skizze (parametrisch)

## Arbeitsbereiche \"Part Design\" und \"Sketcher\" 

-   Neues Werkzeug: Umschalt-Modus für [Reference/Driving constraints](Sketcher_ToggleDrivingConstraint/de.md)
-   Neues Merkmal: Continous creation mode
-   Neues Merkmal: Gesteuerte Beschränkungen
-   Starker Geschwindigkeitszuwachs
-   Erweiterte Kontrolle des Gleichungslösers (Solvers)
-   Neue Merkmale: Werkzeuge für Duplizieren, Spiegeln und Orthogonales Array
-   Unterstützung für [expressions/formulas](Expressions.md) in Beschränkungen und Eigenschaften

## Spreadsheet Workbench 

-   Neue Funktionen: round (runden), trunc (kürzen), ceil (Decke) und floor (Boden)

## Draft Workbench 

-   **Neuer DXF importer**: Der Arbeitsbereich \"Draft\" hat nun einen brandneuen DXF-Importer, komplett in C++ programmiert, übernommen von [HeeksCad](https://github.com/Heeks/heekscad), welcher nun nicht mehr externe Komponenten herunterzuladen braucht, und ist nun viel schneller und kann auch viel größere DXF-Dateien laden. Eine Option in den DXF-Einstellungen erlaubt nun, falls nötig, die Umschaltung zum alten Import.
-   Ein neues **[Mirror tool](Draft_Mirror.md)** erlaubt ein Spiegeln von Objekten \"auf Draft Art\".
-   Viele **DXF-Vorlagen** wurden zu den entsprechenden SCG-Vorlagen hinzugefügt und erleichtern so den Export von Zeichnungen nach DXF.
-   [Rectangles](Draft_Rectangle.md),[wires and lines](Draft_Wire.md) können nun **unterteilt** werden und erlauben so eine Menge neuer Körper-Kombinationen.

<img alt="" src=images/Draft_subdivisions.jpg  style="width:1024px;">

## Arbeitsbereich \"Drawing\" 

-   Ein neues Werkzeug namens **[spreadsheet view](Drawing_SpreadsheetView/de.md)** erlaubt es nun, einen Bereich von Zellen eines [Tabellenblatts](Spreadsheet_Workbench/de.md) auf ein Zeichnungsblatt zu platzieren.

<img alt="" src=images/Drawing_spreadsheetview.jpg  style="width:1024px;">

## Arbeitsbereich \"Arch\" 

-   **[Materials support](Arch_SetMaterial.md)**: Arch Objekte können nun mit [material](material.md) versehen werden, welches das FreeCAD-interne Materialschema benutzt. Diese Materialien werden auch in anderen Arbeitsbereichen benutzt. Diese Materialien unterstützen komplett den IFC Im- und Export.
-   Das Werkzeug **[Section plane](Arch_SectionPlane.md)** kann nun Schnitte in 3D durchführen und den Bereich in Echtzeit anzeigen.

<img alt="" src=images/Arch_clip_plane.jpg  style="width:1024px;">

-   Mehrere Verbesserungen am **IFC importer** wie z.B. neue Optionen für große IFC-Dateien, bessere Unterstützung für Extrusionen (werden nun beim Import bereits erkannt) und kurvigen Segementen, ebenso wie Unterstützung von 2D Bemerkungen. Der Import von Analytical IFC wurde hinzugefügt. Im Moment wird der Import von allen geometrischen Darstellungen von allen analytischen Objekten unterstützt.
-   Bessere **Vernetzungsoptionen** für DAE und IFC-Formate.
-   Ein neues Werkzeug [Arch Schedule/de](Arch_Schedule/de.md) erlaubt es verschiedene Arten von Stücklisten von einem BIM-Modell zu erstellen.
-   **IFC attributes** können nun importiert, editiert und exportiert werden. Dies ist im Wesentlichen ein Spreadsheet-Objekt angehängt an ein Arch-Objekt.

## Arbeitsbereich FEM 

-   **GUI** FEM Befehle haben nun Tastaturkürzel. Ein Einstellungen-Dialog für FEM wurde eingeführt. Der Pfad zur Calculix-Exe ist eine der Benutzer-Einstellungen
-   **GUI analysis container** Unterpunkte der Analyse unterstützen nun Drag & Drop. Sie können in einen Container und aus einem Container heraus bewegt werden. Da es nun Unterstützung von mehreren Analysen gibt, können die Unterpunkte zu einer anderen Analyse verschoben werden. Mehrere Beschränkungen können nun in einer einzigen Studie erstellt werden.
-   **GUI one click analysis** Eine Ein-Klick-Analyse wurde der Benutzeroberfläche hinzugefügt. Sie löscht die Ergebnisse, schreibt ein Calculix-Input-File und führt die Analyse für den erkannten Solver durch. Es wird überprüft, ob \"multithreading\" für Calculix zur Verfügung steht und benutzt die maximal mögliche Anzahl an Threads.
-   **Input file** FreeCADs eingebauter Editor unterstützt das Bearbeiten von Calculix input files (\*.inp). Syntax highlighting wurde ebenfalls implementiert.
-   **Netgen mesh object** Die Benutzeroberfläche und der Eigenschaften-Editor von netgen mesh objects wurde überarbeitet. Tetraeder-Vernetzung mit Elementen ersten und zweiter Ordnung wird genauso unterstützt wie das Anpassen von Vernetzungs-Parametern.
-   **Constraint force and constraint fix objects** Es ist nun möglich, Kräfte und Einspannungen auf Kanten und (Eck-)Punkte zu geben.
-   **Constraint pressure object** Ein neues Objekt für Druck-Belastung auf Flächen wurde hinzugefügt. Der Druck (Kraft pro Fläche) wird direkt an Calculix übergeben, was bedeutet, die Belastung der Knoten wird nicht von FreeCAD, sondern von Calculix berechnet.
-   **Constraint prescribed displacement object** Ein neues Objekt für vorgegebene Verschiebungen wurde hinzugefügt. Die vordefinierten Verschiebungen können Ecken, Kanten und Flächen zugeordnet werden.
-   **Beam section object** Das neue beam section Objekt erlaubt eine rechteckige Schnittfläche für Balken-FEM. Unterschiedliche Schnitte in einer einzigen Analyse werden unterstützt, indem Referenz-Objekte für jeden Schnitt definiert werden.
-   **Shell thickness object** Das neue shell thickness Objekt erlaubt das Definieren von Schalendicken. Wie in den Balkenschnitten werden auch hier durch das Definieren von Referenz-Objekten mehrere Schalendicken in einer Analyse unterstützt.
-   **Material object** Mehrere Materialien werden unterstützt für Ecken, Schalen und Volumenkörper-Netze. Wie bei den Beam section- und den Shell thickness-Objekten wird ein angemessenes FEM-Netz benötigt, um das Material zu benutzen.
-   **Solver object** Eine Grundlage für mehrere Solver-Objekte wurde geschaffen. Alle Unterpunkte können von einer Analyse zur anderen verschoben/kopiert werden.
-   **Frequency analysis** Eine Frequenzanalyse kann durchgeführt werden, die Anzahl der Eigenfrequenzen und der Eigenschwingungen kann in dem Einstellungs-Fenster angepasst werden.
-   *\' View provider*\' Schalen und Balken-FEM-Netze können in FreeCAD angezeigt werden und so auch die Ergebnisse der Analysen.
-   **Python API** Methoden, um mit FEM-Netzen zu arbeiten und eine Analyse aus Python heraus zu generieren, wurden hinzugefügt.
-   **GMSH Macro** Eine interessante externe Entwicklung ist das [Macro\_GMSH](Macro_GMSH.md), welches es ermöglicht, GMSH zur Vernetzung zu benutzen. Sehr nützlich für alle, denen es nicht möglich ist, FreeCAD mit Netgen zu kompilieren, um Schalen oder Kanten vernetzen zu können.
-   **General Improvements** Aufgrund der starken Entwicklungsaktivitäten konnten sehr viele Verbesserungen am Basis-Code des FEM-Modules eingebracht werden.

## Arbeitsbereich \"Path\" 

![](images/Exercise_path_02.jpg )

Ein neuer [Path Workbench/Path-Arbeitsbereich](Path_Workbench/Path-Arbeitsbereich.md) wurde in FreeCAD hinzugefügt. Dieser Arbeitsbereich, obwohl immer noch stark in der Entwicklung, hat bereits einige CAM-Operationen implementiert und erlaubt es, komplette G-Code ([1](https://de.wikipedia.org/wiki/Computerized_Numerical_Control#DIN/ISO-Programmierung_bzw._G-Code)) Programme für eine große Anzahl CNC-Maschinen zu exportieren.

In seinem momentanen Zustand erlaubt es der Arbeitsbereich, Profile und Taschen mit Objekten aus dem [Part](Part_Workbench/de.md)-Arbeitsbereich zu erstellen, komplexe Pfade zu erstellen durch Aneinanderfügen mehrerer Teilpfade, den Inhalt der G-Code Programme der Pfade zu betrachten und editieren, eine Werkzeugliste zu verwalten und beim Im- und Export von G-Code zwischen verschiedenen pre-processing- und post-processing-Skripten zu wählen. Es stellt bereits eine komplette [python API](Path_scripting/de.md) zur Verfügung.

## Zusätzliche Module 

Eine Reihe neuer [addons workbenches](https://github.com/FreeCAD/FreeCAD-addons) wurde von Community-Mitgliedern zur Verfügung gestellt. Diese Arbeitsbereiche sind sehr leicht in eine bestehende FreeCAD-Installation einzubinden. Unter den neuen Arbeitsbereichen sind z.B.:

-   Eine [Animation Workbench](https://github.com/microelly2/Animation), die es ermöglicht, Animationen von FreeCAD-Modellen zu erstellen, indem man die Bewegung einer Kamera definiert und eine Reihe von Bildern exportiert.
-   Ein [Kerkythea exporter macro](https://github.com/marmni/FreeCAD-Kerkythea) ermöglicht den Export der FreeCAD-Modelle zu dem freien [Kerkythea renderer](http://www.kerkythea.net/cms/).
-   Ein in der Entwicklung befindliches [Menu](http://forum.freecadweb.org/viewtopic.php?f=22&t=10892%7CPie) ist ebenfalls verfügbar.
-   Außerdem wurde ein [addons repository](https://github.com/FreeCAD/FreeCAD-addons) geschaffen, um alle interessanten Arbeitsbereiche, Module und Makros rund um FreeCAD zu sammeln. Diese Datenbank stellt auch einen Installer bereit, der sich um Installation und Update der Einträge kümmert.

![](images/Macro_installer_02.jpg )

[Category:News](Category:News.md) [Category:Documentation](Category:Documentation.md) [Category:Releases](Category:Releases.md)

---
[documentation index](../README.md) > [News](Category:News.md) > Release notes 0.16/de
