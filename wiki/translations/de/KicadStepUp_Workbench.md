# KicadStepUp Workbench/de



<div class="mw-translate-fuzzy">

Symbol Externer Arbeitsbereich KicadStepUp


</div>


{{TOCright}}

## Einführung

KicadStepUp Arbeitsbereich zielt darauf ab, sowohl KiCad als auch FreeCAD Benutzer bei der Zusammenarbeit mit der elektrischen (ECAD) und mechanischen (MCAD) Konstruktion zu unterstützen.

## Hintergrund

Kicad ([Webseite](https://kicad-pcb.org/)) ist eine Opensource Elektronikkonstruktionsautomatisierungsfamilie. Sie ermöglicht es, eine elektrische Schaltung zu entwerfen und eine ein oder mehrlagige Leiterplatte mit einer umfangreichen Bibliothek von Teilen zu erstellen. Das Tolle daran ist, dass die Verwendung des FreeCAD und KicadStepUp Arbeitsbereichs der offizielle Weg ist, um 3D Teile für elektrische Komponenten für Kicad zu erstellen. Die Bibliotheken werden bereitgestellt durch [hier](https://kicad.github.io/), so dass jeder Teile erstellen und einbuchen kann.

KiCADs GUI Philosophie ist im Vergleich zu FreeCAD etwas anders, vor allem, wenn es darum geht, Elemente zu erstellen und sie zu verschieben. Da Kicad jedoch seit Jahren in der Produktion eingesetzt wird, gibt es eine ausgezeichnete Dokumentation, z.B. ein sehr gutes \"Getting Started\" Dokument. Zusätzlich hat jedes Werkzeug sein eigenes Handbuch.

Wenn man [Kicad](https://kicad-pcb.org/) noch nicht kennt, empfiehlt es sich, eine eigenständige Leiterplatte gemäß dem [Leitfaden für den Einstieg](https://docs.kicad-pcb.org/5.1/en/getting_started_in_kicad/getting_started_in_kicad.pdf) zu erstellen, um die Konzepte zu verstehen. Obwohl einige Themen wie das Hinzufügen von neuen Schaltplänen und Lötflächenrastern (engl.:footprints, wörtlich: Fußabdrücke) zu einer lokalen Bibliothek für den Anfänger wenig interessant zu sein scheinen, stößt man in der Praxis oft schnell darauf, wenn man ein ernsthaftes Projekt beginnt.

Für alle diese [Kicad](https://kicad-pcb.org/) Konzepte findet man im KicadStepUp Arbeitsbereich eine Art von Funktion. Wenn man diese also kennt, ist es viel einfacher zu verstehen, wie man diesen Arbeitsbereich benutzt.

## Funktionen


{{emphasis|In Bearbeitung}}

-   Lade die kicad Platine und Teile in FreeCAD und exportiere sie in STEP (oder IGES) für eine vollständige ECAD MCAD Zusammenarbeit
-   Lade die kicad\_mod Lötflächenraster in FreeCAD, um das mechanische Modell einfach und präzise am kicad Lötflächenraster auszurichten
-   Konvertiere das STEP 3D Modell von Teilen, Platinen und Gehäusen in VRML mit Materialeigenschaften für die optimale Verwendung in kicad
-   Überprüfe Überschneidungen und Kollisionen für Gehäuse- und Lötflächenraster Gestaltung
-   Konstruiere eine neue Leiterplattenkante mit FreeCAD Skizzierer und SCHIEBE dies auf eine bestehende kicad\_pcb Platine
-   ZIEHE eine Leiterplattenkante von einer kicad\_pcb Platine, Bearbeite sie in FC Skizzierer und SCHIEBE diese Kante zurück nach kicad
-   Entwirf ein neues Lötflächenraster in FreeCAD, um die Leistungsfähigkeit von Skizze in Lötflächenrastern zu nutzen
-   Erzeuge Blender kompatible VRML Dateien

<img alt="" src=images/ECAD-MCAD-collaboration.png  style="width:800px;">

## Einrichtung

KicadStepUp ist Teil der [externen Arbeitsbereiche](external_workbenches/de.md) und kann automatisch mit dem <img alt="" src=images/AddonManager.svg  style="width:24px;"> installiert werden. [FreeCAD Erweiterungsverwalter](Addon_Manager/de.md), der mit FreeCAD 0.17 mitgeliefert wird, unter dem Menüpunkt **Werkzeuge → Erweiterungsverwalter** installiert werden.


<div class="mw-translate-fuzzy">

## Anwendung


{{emphasis|In Bearbeitung}}


</div>


{{emphasis|In progress}}

### General Approach 


<div class="mw-translate-fuzzy">

### Allgemeiner Ansatz 

Die Grundidee von KicadStepUp ist es, Daten zwischen den beiden Anwendungen zu synchronisieren. Für den Heimgebrauch hast du vielleicht FreeCAD und Kicad gleichzeitig geöffnet. Im professionellen Einsatz arbeitest du mit den gleichen Dateien (z.B. auf einem zentralen Server) und hast Spezialisten für mechanisches CAD (MCAD), die in FreeCAD arbeiten, und Elektronikexperten für elektrisches CAD (ECAD).


</div>

KicadStepUp wandelt Standard FreeCAD Dateien in Kicad Dateien um und umgekehrt. Auf diese Weise kann jede Anwendung mit ihren natürlichen Datendateien arbeiten. Projekte können verwendet werden, ohne dass die andere Anwendung oder KicadStepUp installiert ist. Das ist auch der Grund, dass kein Zusatzprogramm auf der Kicad Seite benötigt wird.

Um die feinen Details des Arbeitsablaufs zu verstehen, ist es hilfreich zu wissen, dass die Unterschiede zwischen den beiden Programmen einige Schwierigkeiten für einen vollständigen Datenaustausch mit sich bringen.
Ein Beispiel ist, dass der Skizzierer, der in Kicad verwendet wird, um den Umriss der Platine zu definieren, im Vergleich zum FreeCAD Skizzierer viel begrenzter ist, so dass der Inhalt des Modells nicht komplexer sein kann, als der Kicad Skizzierer verarbeiten kann. Aus der Sicht von FreeCAD bedeutet das, dass du möglicherweise Daten verlierst. KicadStepUp bietet Umgehungsmöglichkeiten, die möglicherweise schwieriger zu verstehen sind, wenn du nicht über diesen Hintergrund verfügst.

### Basic Workflow 


<div class="mw-translate-fuzzy">

### Grundlegender Arbeitsablauf 

Eine Zusammenarbeit kann mit einem neuen oder einem bestehenden Projekt begonnen werden. Wir betrachten hier ein neues Projekt, um die Dinge einfach zu halten:


</div>

1.  Create a new Kicad Project anywhere you like. Lets name it \"KsuTest\"
2.  Open the PCB Editor and create on the layer \"Edit.Cuts\" a closed outline. Shape does not matter, we will overwrite it anyway.
3.  Create a new FreeCAD file for the PCB, the name does not matter. \*
4.  Create a sketch with an outline of the desired PCB. Lets name it \"pcb design\" (but could be any other name) and put at least one circle into it for a hole.

    :   you may use any FreeCAD features to include holes, cutouts and outer shape to other components you might have. We assume here you would use Sketcher features as Dimensioning, Constraints and Work geometry in your sketch.
    :   If you are using PartDesign WB for creating the sketch there is no need to create a PartDesign body, since we are not going to pad this sketch.
5.  Switch to the KicadStepUp Workbech
6.  Select the \"pcb design\" sketch
7.  Select the Toolbar button \"Push Sketch to PCB Edge\" or the menu *ksu PushPull/ksu Push Sketch to PCB*
    -   first a dialog will open with defaults \"Edge.Cuts\" for layer and \"0.16\" for line width. Keep those defaults.
    -   next a file dialog will open. Click to your Kicad \"KsuTest\" project, where you should see a file \"KsuTest.kucad\_pcb\". That is the PCB file with the temporary outline we created before. Select is and confirm to replace the old file.
        Now a dialog should say \"new Edge pushed to kicad board!\"

        :   if you forgot the 2nd step, you the push operation might fail as a pcb file must exist and it must not be empty.
8.  Cloase and re-open the PCB Editor in Kicad. \*\*

    :   The shape from the FreeCAD sketch should appear.
9.  go over the circle with the mouse and press *m* on the keyboard to move the circle. Click to place to another position. Press the save toolbar button on the top left.
10. Switch to FreeCAD and select in the KicadStepUp Workbech the tool button \"Pull Sketch from PCB\" or the menu *ksu PushPull/ksu Pull Sketch from PCB*
    -   first dialog with default layer \"Edge.Cuts\" and three choices will open. Select choice \"replace PCB and Sketch in current document\" \*\*\*
    -   next a file dialog should show again the file \"KsuTest.kucad\_pcb\". Select it and press *Open*

        :   You should see your PCB as 3D model. Note that the hole has moved compared to you \"pcb design\" sketch.
        :   In the tree appears a new structure with a yellow *Part Container* with the Kicad Filename and within another *Part Container* with \"Board\_Geoms\_e63b\" (the part with the number probably different). In the second container there are the following three files. Do not change any names in that structure, because KicadStepUp uses them to find the parts to update.
        :   Do not forget to save your file




    Local_CS_e63b      the PCB origin. 
                         same as the origin in "pcb design" sketch
    Pcb_e63b           3D object with the PCB. 
                          Don't edit, it will be overwritten by KicadStepUp 
    PCB_Sketch_e63b    sketch with all part of "pcb design" sketch that Kicad recognized. 
                          all other were deleted. Also note that if you change this sketch
                          and recalculate 3D object will not change.

Try to make another PushPull round trip: adjust you \"pcb design\" sketch to the changes from Kicad, add some other change and start again. Do that a few times to appreciate how quickly and naturally this procedure becomes in a very short time.

Jetzt kannst du die neue 3D Leiterplattendatei verwenden, um 3D Komponenten wie Steckverbinder, Taster, Schalter, Verschlüsse usw. auszurichten, oder du fügst diese zu deiner Baugruppe hinzu, wenn du ein größeres Projekt hast.

Dies zeigt nur die sehr grundlegende Arbeitsweise von KicadStepUp. Dir fehlt an dieser Stelle noch vieles, z.B. Lötflächenrastern und 3D Teile. Aber von hier aus ist es viel einfacher, KicadStepUp auf eigene Faust zu erkunden. Verwende die Dokumentations PDF Datei im Menü *ksu Tools/Demo*

:   \'\'Notes:
    -   As long as the name of the created strucure (and its parts) is unchanged any workflow interactions will just update the structure. If you change any names, a new structure will be created each time.
    -   It is not required to have Kicad running to update Kicad project files. Actually, Kicad does not even have to be installed on the PC.
    -   The standard approach is to use the same sketch on both sides Kicad and Freecad. Any changes will be synchronized to the other application. This is the most natural and clean way to work with KicadStepUp
        However, this causes a problem if you want to use any of the following features in your sketch definting you PCB shape: dimensions, geometry constraints, work geometry (blue lines) or external linked geometry. There is no clean way to do this, because Kicad does not know any of the features. That means that on the round trip between the applications any of those features will be deleted. There is not real solution for that problem, just a selection of one of several workarounds. So if you want to use any of those features that means you define the PCB shape in FreeCAD only and sync in one way to Kicad. Any outline changes done in Kicad need to be added manually on the FreeCAD side. This might make sense, e.g. if future changes from the mechanical side are much more likely than from the electrical side. There several ways to do it
        -   Put the design sketch inside the KicadStepUp structure, an select \"replace PCB and keep Sketch in curr. doc\" every time you import back from Kicad.
        -   Keep the design sketch outside the KicadStepUp structure. Ignore the sketch imported from Kicad.

    :   The second choice has the advantag that changes in Kicad can be traced to the original sketch and the FreeCAD sketch is protected against an accidently wrong import choice. The described workflow uses this approach to make sure the issue is well understood. From there its easy to switch to modifying the KicadStepUp supplied sketch with none of the more advanced FreeCAD features.

    -   To use KicadStepUp with a FreeCAD assembly (\> V0.19) you could add a new file for the PCB. After the workflow above has been run once add the 3D object for the PCB to your assembly like any other mechanical part. Make sure you save the file when it was updated by KicadStepUp (KicadStepUp writes to FreeCAD memory not to FreeCAD files).

\'\'

Bitte schau den [kicad StepUp Spickzettel](https://github.com/easyw/kicadStepUpMod/blob/master/demo/kicadStepUp-cheat-sheet.pdf) für die anderen Funktionen an.

## Referenzen

-   Autor: Github: [\@easyw](https://github.com/easyw) \| FreeCAD Foren: [kicad StepUp: ECAD MCAD bidirektionale Zusammenarbeit](https://forum.freecadweb.org/viewtopic.php?f=24&t=14276)
-   Quellcode auf GitHub: <https://github.com/easyw/kicadStepUpMod>

## Nebenbemerkung zu Externen Arbeitsbereichen 

FreeCAD Arbeitsbereiche sind einfach in [Python](Python/de.md) zu programmieren, daher gibt es viele Leute, die zusätzliche Arbeitsbereiche außerhalb der FreeCAD Hauptentwickler entwickeln.

Die Seite [externe Arbeitsbereiche](external_workbenches/de.md) enthält einige Informationen und Anleitungen zu einigen von ihnen, und das Projekt [FreeCAD Erweiterungen](https://github.com/FreeCAD/FreeCAD-addons) hat sich zum Ziel gesetzt, diese zu sammeln und sie von FreeCAD aus leicht installierbar zu machen.

Neue Arbeitsbereiche sind in der Entwicklung, bleib dran!




[Category:Addons](Category:Addons.md) [Category:External Workbenches](Category:External_Workbenches.md)
