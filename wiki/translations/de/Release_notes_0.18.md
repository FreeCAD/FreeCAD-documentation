# Release notes 0.18/de
FreeCAD 0.18 wurde am 12. März 2019 veröffentlicht, hole es von [GitHub](https://github.com/FreeCAD/FreeCAD/releases/tag/0.18.3). Die vollständige Liste der Änderungen findest du im [MantisBT bugtracker FC 0.18 changelog](https://www.freecadweb.org/tracker/changelog_page.php?version_id=78).

Ältere FreeCAD Versionshinweise findest du unter [Liste der Funktionen](Feature_list#Release_notes/de.md).



## Höhepunkte

Erweiterte [TechDraw](#TechDraw_Workbench/de.md) Werkzeuge

<img alt="Modell von Laurent14" src=images/TechDraw_sheet_screenshot.png  style="width:700px;">




Neue [Skizzierer](#Sketcher_Workbench/de.md) Werkzeuge, stabileres und robustes [PartDesign](#PartDesign_Workbench/de.md)

<img alt="Modell von un1corn" src=images/Part_engine_screenshot.jpg  style="width:700px;">




Verbesserte und erweiterte [Arch und BIM](#Arch_Workbench/de.md) Werkzeuge.

<img alt="Modell von regis" src=images/Arch_work_screenshot.png  style="width:700px;">






## Allgemeines

-   Neugestaltetes Startzentrum
-   Der Dokumentenbaum (Modell Reiter) bietet jetzt 3 Optionen für die Anzeige aller Dokumente, wobei die Option aus dem Menü **Ansicht→ Dokumentenbaum** gesetzt ist:
    -   Einzelnes Dokument (Nur das derzeit aktive Dokument anzeigen)
    -   Multi-Dokument (Anzeige aller Dokumente, wie es bis FreeCAD 0.17 der Fall war)
    -   Komprimieren/Expandieren (das aktive Dokument expandieren und alle anderen komprimieren)
-   Wenn eine Aufgabe aktiv ist und eine Benutzereingabe erfordert, erscheint jetzt ein Symbol mit einem Bleistift auf der Aufgabenreiter und verschwindet, wenn die Aufgabe abgeschlossen ist.
-   Die 3D Ansicht verfügt jetzt über einen neuen **[Navigationswürfel](Navigation_Cube/de.md)**, um die Ansicht schnell auszurichten. Er verfügt außerdem über ein kleines Menü, mit dem die Projektion auf orthografisch oder perspektivisch eingestellt und der Inhalt an die Ansicht angepasst werden kann. Die Platzierung des Navigationswürfels kann in **Einstellungen → Anzeige→ 3D Ansicht** eingestellt und auch ausgeblendet werden.
-   Generische Unterstützung für US Civil / Transportation Engineering Einheiten wurde hinzugefügt. Diese Einheiten umfassen ft, ft\^2, ft\^3, mph und Winkel als Grad/Minuten/Sekunden. Diese Einheiten ermöglichen die Darstellung von feet in dezimaler Form, im Gegensatz zu US Building, das Bruchteile von Zoll erzwingt.
-   Es ist jetzt möglich, ein benutzerdefiniertes Hintergrundbild für das Hauptfenster von FreeCAD mit der Option [**Einstelllungen → Allgemein → Aktivere gekachelter Hintergrund **](Preferences_Editor#General/de.md) festzulegen.

<File:Start> center 0.18 screenshot.jpg\|thumb\|left\|Das neu gestaltete Startzentrum <File:FC018> Navigation Cube.png\|thumb\|left\|Der Navigationswürfel <File:FreeCAD> with background image.jpg\|thumb\|left\|FreeCAD mit einem benutzerdefinierten Hintergrundbild






## Arbeitsbereich Arch 

<img alt="The Arch workbench at work" src=images/Arch_release018_example.jpg  style="width:700px;">

-   [Walls](Arch_Wall.md) can now be displayed as a stack of blocks. There are many options to configure their size and how blocks must be stacked.
-   [Building Parts](Arch_BuildingPart.md) are the new use-for-all Arch container. They can group any number of objects, they can be used to make floors (storeys), buildings (the [Arch Floor](Arch_Floor.md) and [Arch Building](Arch_Building.md) tools now produce Building Parts), or any other group of Arch objects. They can be moved like [Parts](Std_Part.md), and they are [clonable](Draft_Clone.md) and [referencable](Arch_Reference.md)!
-   The [BIM Workbench](BIM_Workbench.md) (added via the [Addon Manager](Std_AddonMgr.md)), is a new external, experimental counterpart of [Arch](Arch_Workbench.md). In it, we test new features and workflows in a more free environment. Be sure to give it a test ride!
-   [Windows](Arch_Window.md) have new presets such as a 4-pane sliding window, plus, if the [Parts Library](https://github.com/FreeCAD/FreeCAD-library/tree/c5eea12cdda7a3e6349323808815f63b0f97ef2e) is installed, all the doors and windows from the library.
-   [Panels](Arch_Panel.md) can now do different kinds of corrugated panels, such as undulated sheets, or even sandwich panels.
-   [Structure](Arch_Structure.md) objects have a new beam drawing mode, which allow you to click two points to place a structural element between them.
-   All IFC types are now available for all Arch objects. Any object can be exported to any other type to IFC.
-   [Window placement](Arch_Window.md) has been fully redesigned. Correctly placing windows in host objects, which was before a real pain to do is now much easier.
-   Dynamic window parameters: The size of the window frames is now a window property, so it is now possible to adjust the thickness of preset windows without the need to edit their components or base sketches.
-   IFC Property Sets are now supported by all Arch objects.
-   The IFC importer and exporter have been greatly enhanced with a wealth of new features: Property sets support, grid support, file compression, shared profiles, groups support, quantity sets, etc\...
-   [Materials](Arch_SetMaterial.md) now support hierarchy, if you give a material another material as father, they appear correctly stacked in the tree.
-   All Arch objects and materials now support classification systems (not yet supported by IFC import/export).
-   [External references](Arch_Reference.md) now allow you to link parts from another FreeCAD file into a FreeCAD file.

-   But there is much more! Check the [Arch/BIM development reports](https://github.com/yorikvanhavre/BIM_Workbench/wiki) to see everything that has been done there this year.



## Arbeitsbereich Entwurf 

<img alt="More precise Draft annotation tools" src=images/Draft_release018_example.jpg  style="width:700px;">

-   The [Draft Scale](Draft_Scale.md) tool has been fully redesigned, and has now more options and is much more comfortable to use
-   The [Draft Text](Draft_Text.md) tool has also been fully redesigned, it now has its own parametric object with many more options. Warning, these new texts are not supported by 0.17
-   [Draft Wires](Draft_Wire.md) now have a right-click option that allows to force-flatten them on their median plane
-   New [Draft Join](Draft_Join.md) tool, which allows you to join individual wires and lines into a single wire
-   New [Draft Split](Draft_Split.md) tool, which splits a line or a wire at a point to create another wire or line
-   Pressing the **** key while drawing in draft mode cycles the snapping object target, allowing you to snap on objects that are obscured by others
-   The Draft AddPoint tool has been improved to more reliably add nodes on lines and wires exactly where you click




## FEM Arbeitsbereich 

### Allgemeine Verbesserungen an der Code Basis 

-   Tonnen von Fehlerbehebungen.
-   Code Refactoring und Reinigung. Beseitigen von doppelten Code.
-   Viele Tippfehler im Code und in den sichtbaren Meldungen behoben.
-   Python 3 Kompatibilitätskorrekturen.
-   Weitere Einheitentests wurden hinzugefügt.
-   Möglichkeit, FreeCAD mit externem, aktuellem SMESH zu kompilieren.

### Werkzeuge

-   Ein Beschneidungsebenen Werkzeug wurde hinzugefügt, um Volumenkörper auswählen zu können, die sich innerhalb anderer Volumenkörper befinden.
-   Der VTK Kettfilter erhielt etwas Zuneigung.
-   Ein Analysetyp für die CalculiX Modellprüfung wurde hinzugefügt.

### Material

Die Materialhandhabung wurde verbessert. Es ist nun möglich, den globalen FreeCAD Materialeditor zu verwenden. Siehe auch [Materialkarten](Release_notes_0.18#Material_Handling/de.md). Dazu wurde die FEM Materialaufgabenkonsole aufpoliert.



## Arbeitsbereich Part 

-   Das [Geometrie prüfen](Part_CheckGeometry/de.md) Werkzeug öffnet jetzt ein kleines Fenster mit einem Fortschrittsbalken und einer **Cancel** Schaltfläche, um die Aufgabe zu beenden, wenn sie zu lange dauert.
-   Das neue [Defeaturing](Defeaturing_Workbench/de.md) Werkzeug basiert auf dem gleichnamigen Werkzeug, das in OCCT 7.3.0 enthalten ist. Es kann ausgewählte Attribute an einem Volumenkörper wie Löcher, Vorsprünge, Lücken, Fasen, Verrundungen usw. entfernen. Weitere Informationen findest du im [3D Model Defeaturing](https://dev.opencascade.org/index.php?q=node/1211) Artikel auf der OCCT Netzseite. Bitte beachte, dass, wenn FreeCAD auf einer älteren Version als OCCT 7.3.0 aufbaut, dieses Werkzeug nicht zur Verfügung steht und ausgegraut wird.

-   Das neue [AuseinanderKappen](Part_SliceApart/de.md) Werkzeug basiert auf dem Werkzeug [Kappen aus Verbund](Part_Slice/de.md) und enthält ein automatisches Sprengen des Verbunds zum einfachen Aufteilen von Objekten.



## Arbeitsbereich PartDesign 

-   Das neue [Lokales koordinatensystem](PartDesign_CoordinateSystem/de.md) Werkzeug ermöglicht jetzt das Hinzufügen einer lokalen Koordinatensystem Visualisierung zu mehreren Bezugsobjekten.



## Arbeitsbereich Pfad 



### Allgemeine Verbesserungen 

-   Pfad kann jetzt G-Code mit ABC Achsenwörtern korrekt anzeigen
-   Verbesserungen am Werkzeugeditor - Vereinfachte Bearbeitung für ausgewählte Werkzeugtypen



### Auftragsverbesserungen

-   Aufträge können jetzt mehrere Basisobjekte haben
-   Die Organisation der Auftragsbehälter wurde verbessert
-   Vorgabewerte für Arbeitsgangseinstellungen können über EinrichtungsBlätter gesteuert werden



### Arbeitsgänge

-   Neue adaptive Ausgleich Bearbeitung
-   Neue Entgrat Bearbeitung
-   neue AchsKarten Verschönerung begrenzt die 4. Achse durch Abbildung einer linearen Richtung auf eine Drehachse
-   Unterstützung für 2D Objekte und individuelles Kantenfräsen durch Gravur und Entgraten
-   RampenEintritt Verschönerung hat jetzt einen konfigurierbaren Startpunkt
-   TaschenForm Bearbeitung kann jetzt \'Umriss verwenden\'.



### Nachbearbeiter

-   grbl_post -- Argument zur Unterdrückung von Werkzeugwechselbefehlen
-   grbl_g81 Nachbearbeiter



## Arbeitsbereich Skizzierer 

<img alt="Skizzierer Ansicht Abschnitt Demo" src=images/Sketch-clip-plane-demo.png  style="width:700px;">

-   Das neue **[View section](Sketcher_ViewSection/de.md)** Werkzeug erzeugt eine Schnittebene, die Materie auf dem Modell entfernt, die sich vor der Skizzierebene befindet. Dies kann nützlich sein, wenn sich die Skizzierebene innerhalb eines Volumenmodells befindet. Durch erneutes Drücken des Schnittwerkzeugs Ansicht wird die Ansicht wieder zur Vollansicht umgeschaltet.
-   Der **Skizzenlöser** profitierte von Verbesserungen und ist nun besser in der Lage, überflüssige und widersprüchliche Abhängigkeiten zu erkennen, insbesondere solche, die durch symmetrische Abhängigkeiten verursacht werden.
-   Neues **[Durchmesser beschränken](Sketcher_ConstrainDiameter/de.md)** Werkzeug hinzugefügt
-   **DoF Finder** ist ein neues Hilfsprogramm, das bei der Suche nach Freiheitsgraden hilft. Im Lösernachrichten Widget in der Aufgabenkonsole wird die übliche Nachricht *Unterbeschränkte Skizze mit x Freiheitsgraden* jetzt den *x Grad*-Text blau unterstrichen. Wenn du darauf klickst, werden in der 3D Ansicht die Elemente, die nicht vollständig beschränkt sind, in grün hervorgehoben.
-   **Skizzierer Auto Remove Redundants** ist ein neues Kontrollkästchen in den Lösernachrichtenfeld. Wenn es aktiviert ist, verhindert es die Erstellung überflüssiger Beschränkungen, wenn der Benutzer skizziert und Abhängigkeiten anwendet, und löscht automatisch die überflüssigen Beschränkungen.
-   Es gibt einen neuen Befehl zum Löschen aller Beschränkungen auf einmal. Er ist im Menü **Skizze → Skizzierwerkzeuge → Alle Beschränkungen löschen** zu finden.
-   Neue Option in **Einstellungen → Skizzierer → Allgemein→ Basislängeneinheiten für unterstütztes Einheitensysteme ausblenden**. Dadurch wird die Einheit für Bemaßungsbeschränkungen im Skizzenbearbeitungsmodus ausgeblendet.
-   Die Größe von Knoten (Punkten) kann jetzt in **Einstellungen → Anzeige → 3D Ansicht → Markergröße** eingestellt werden.
-   Neuer **[Verschieben](Sketcher_Move/de.md)** Befehl, um die gesamte ausgewählte Geometrie vom zuletzt ausgewählten Punkt aus zu verschieben. Auf diesen Befehl kann über die Ausklappliste des Klonwerkzeugs zugegriffen werden.
-   Kontrollkästchen *Erweiterte Informationen* zum Beschränkungslisten Widget hinzugefügt.

Entsprechende Forenverweise:

-   [Jüngste zahlreiche Verbesserungen am Sketcher](https://forum.freecadweb.org/viewtopic.php?f=9&t=29192)
-   [Feature #1632: Erlaubt die Eingabe des Durchmessers anstelle des Radius für die Kreisradiusbeschränkung](https://forum.freecadweb.org/viewtopic.php?f=8&t=29152)
-   [Skizzierermodus zur automatischen Entfernung von Redundanzen](https://forum.freecadweb.org/viewtopic.php?f=9&t=30594)
-   [Beschränkungen erweiterte Benennung](https://forum.freecadweb.org/viewtopic.php?f=10&t=28890)



## Arbeitsbereich Tabellenkalkulation 



## Arbeitsbereich Oberfläche 

## TechDraw Arbeitsbereich 

Der TechDraw Arbeitsbereich erhielt eine Reihe von Ergänzungen und Verbesserungen für v0.18.

-   Neue Export Seite nach Dxf
-   neues Tutorial für TechDraw
-   verbesserte Bemaßungsformatierung für isometrische Ansichten, Winkel, Textposition
-   verbesserte Fehlermeldungen
-   verbesserte Formatierung der Schnittansicht
-   benutzerdefinierte Zeilengruppen erlauben
-   zusätzliche Einstellungen
-   einfachere Auswahl von Rand- und Mittelmarkierungen
-   Ansichtsrichtung basierend auf der aktuellen 3D Ansicht oder der ausgewählten Fläche
-   +/\* Toleranzen zu den Abmessungen hinzugefügt
-   neue 3 Punkt Winkelbemaßung
-   RMB Kontextmenü
-   Tastatur Zoomen (Ctl+/-)
-   Unterstützung für DMS Abmessungen

## Materialhandhabung

<img alt="eine Materialkarte" src=images/Material-Card-018.png  style="width:300px;"> Die Materialhandhabung wurde verbessert. Es ist jetzt möglich, *Materialkarten* für jedes Material zu erstellen. Die Karten können alle Informationen, physikalische Eigenschaften, architektonische Spezifikationen, Internetverknüpfungen, Kommentare usw. enthalten. Die Karten sind Textdateien mit der Dateiendung **.FCMat** und können für alle Arbeitsbereiche von FreeCAD verwendet werden.

FreeCAD stellt Materialkarten für Standardmetalle, Kunststoffe und verschiedene Stahlsorten zur Verfügung.



## Zusätzliche Module 

Einige der neuen Gemeinschaftsmodule, die während des Entwicklungszyklus von 0.18 aktiv entwickelt wurden.

-   [A2plus](A2plus_Workbench.md) is a new workbench to assemble different parts in FreeCAD. It is an extension of the Assembly2 workbench providing an extended color and transparency handling for parts and a new constraint using the center of mass of parts.

-   [Curves](https://github.com/tomate44/CurvesWB), a collection of tools to create and edit NURBS curves and surfaces.

-   [Nurbs](https://github.com/microelly2/freecad-nurbs), a collection of scripts for managing freeform surfaces and curves.

-   [Silk](https://github.com/edwardvmills/Silk), a collection of NURBS surface modeling tools focused on low degree and seam continuity.

-   [Flamingo Workbench](Flamingo_Workbench.md), a set of customized FreeCAD commands and objects that help to speed-up the drawing of frames and pipelines.

-   [Civil Engineering/Transportation Workbench](Civil_Engineering_Workbench.md)

-   [GDT](https://github.com/juanvanyo/FreeCAD-GDT), geometric dimensioning and tolerancing (GD&T).

-   [InventorLoader](https://github.com/jmplonka/InventorLoader) to import Autodesk Inventor files (in progress).

-   [Kicad StepUp Workbench](https://www.freecadweb.org/wiki/KicadStepUp_Workbench) is aimed to help KiCad and FreeCAD users in ECAD and MCAD collaboration.

-   [CadQuery FreeCAD Module](https://github.com/jmwright/cadquery-freecad-module/wiki) is a workbench that allows users to write Python scripts, and is tailored to those based on the CadQuery CAD scripting API. A new code editor is made available, and script variables can be edited dynamically through the use of a parameter dialog. The workbench also adds a menu that includes normal file operations for CadQuery scripts (open, new, close, etc), and example scripts to help users learn new concepts.

-   [Arbeitsbereich Defeaturing](Defeaturing_Workbench/de.md) ist bestimmt für die Bearbeitung importierter STEP Modelle, das Entfernen der ausgewählten Funktionen aus dem Modell



---
![](images/Right_arrow.png) [documentation index](../README.md) > [News](Category_News.md) > [Documentation](Category_Documentation.md) > [Releases](Category_Releases.md) > Release notes 0.18/de
