# <img alt="Symbol des externen Arbeitsbereichs KicadStepUp" src=images/Kicad-StepUp-tools-WB.svg  style="width   *64px;"> KicadStepUp Workbench/de


{{TOCright}}

## Einleitung

Der Arbeitsbereich KicadStepUp zielt darauf ab, sowohl KiCad- als auch FreeCAD-Benutzer bei der Zusammenarbeit mit der elektrischen (ECAD) und mechanischen (MCAD) Konstruktion zu unterstützen.

## Hintergrund


<div class="mw-translate-fuzzy">

Kicad ([Webseite](https   *//kicad.org/)) ist ein Opensource-Programmpaket für die Automatisierung der Konstruktion von elektronischen Schaltungen. Es ermöglicht, einen elektrische Schalkreis zu entwerfen und eine ein- oder mehrlagige Leiterplatte mit Hilfe einer umfangreichen Bibliothek von Teilen zu erstellen. Das Großartige daran ist, dass die Verwendung von FreeCAD mit dem Arbeitsbereich KicadStepUp der offizielle Kicad-Weg ist, um 3D-Teile für elektrische Komponenten für Kicad zu erstellen. Die Bibliotheken werden [hier](https   *//kicad.github.io/) gehostet, damit jeder Teile erstellen und einchecken kann.


</div>


<div class="mw-translate-fuzzy">

KiCADs GUI-Philosophie ist im Vergleich zu FreeCAD etwas anders, vor allem, wenn es darum geht, Elemente zu erstellen und sie zu verschieben. Da Kicad jedoch seit Jahren in der Produktion eingesetzt wird, gibt es eine ausgezeichnete Dokumentation, z.B. ein sehr gutes \"Getting Started\" Dokument. Zusätzlich hat jedes Werkzeug seine eigene Anleitung.


</div>


<div class="mw-translate-fuzzy">

Wenn man [Kicad](https   *//kicad.org/) noch nicht kennt, wird empfohlen, eine eigenständige Leiterplatte gemäß dem [Leitfaden für den Einstieg](https   *//docs.kicad-pcb.org/5.1/en/getting_started_in_kicad/getting_started_in_kicad.pdf) zu erstellen, um die verwendeten Konzepte zu verstehen. Obwohl einige Themen wie das Hinzufügen von neuen Schaltplänen und Lötflächenrastern (engl.   * footprints, wörtlich   * Fußabdrücke) zu einer lokalen Bibliothek für den Anfänger wenig interessant zu sein scheinen, stößt man in der Praxis oft schnell darauf, wenn man ein ernsthaftes Projekt beginnt.

Für alle diese [Kicad](https   *//kicad-pcb.org/)-Konzepte findet man im Arbeitsbereich KicadStepUp diverse Funktionen. Wenn man diese kennt, ist es viel einfacher zu verstehen, wie man diesen Arbeitsbereich benutzt.


</div>

For all these [KiCad](https   *//kicad.org/) concepts one can find a feature of some sort in the KicadStepUp workbench. So knowing those makes it a lot easier to understand how to use this workbench.

## Funktionen


{{emphasis|In Bearbeitung}}


<div class="mw-translate-fuzzy">

-   Lade die kicad Platine und Teile in FreeCAD und exportiere sie in STEP (oder IGES) für eine vollständige ECAD MCAD Zusammenarbeit
-   Lade die kicad_mod Lötflächenraster in FreeCAD, um das mechanische Modell einfach und präzise am kicad Lötflächenraster auszurichten
-   Konvertiere das STEP 3D Modell von Teilen, Platinen und Gehäusen in VRML mit Materialeigenschaften für die optimale Verwendung in kicad
-   Überprüfe Überschneidungen und Kollisionen für Gehäuse- und Lötflächenraster Gestaltung
-   Konstruiere eine neue Leiterplattenkante mit FreeCAD Skizzierer und SCHIEBE dies auf eine bestehende kicad_pcb Platine
-   ZIEHE eine Leiterplattenkante von einer kicad_pcb Platine, Bearbeite sie in FC Skizzierer und SCHIEBE diese Kante zurück nach kicad
-   Entwirf ein neues Lötflächenraster in FreeCAD, um die Leistungsfähigkeit von Skizze in Lötflächenrastern zu nutzen
-   Erzeuge Blender kompatible VRML Dateien


</div>

<img alt="" src=images/ECAD-MCAD-collaboration.png  style="width   *800px;">

## Einrichtung


<div class="mw-translate-fuzzy">

KicadStepUp ist Teil der [externen Arbeitsbereiche](external_workbenches/de.md) und kann automatisch mit dem <img alt="" src=images/Std_AddonMgr.svg  style="width   *24px;"> [FreeCAD Addon-Manager](Std_AddonMgr/de.md), der mit FreeCAD 0.17 mitgeliefert wird, unter dem Menüpunkt **Werkzeuge → Addon-Manager** installiert werden.


</div>

## Anwendung


{{emphasis|In Bearbeitung}}

### Allgemeine Herangehensweise 


<div class="mw-translate-fuzzy">

Die Grundidee von KicadStepUp ist es, Daten zwischen den beiden Anwendungen zu synchronisieren. Für den Heimgebrauch hat man vielleicht FreeCAD und Kicad gleichzeitig geöffnet. Im professionellen Einsatz arbeitet man mit den gleichen Dateien (z.B. auf einem zentralen Server) und hat Spezialisten für mechanisches CAD (MCAD), die in FreeCAD arbeiten, und Elektronikexperten für elektrisches CAD (ECAD).


</div>


<div class="mw-translate-fuzzy">

KicadStepUp wandelt Standard-FreeCAD-Dateien in Kicad-Dateien um und umgekehrt. Auf diese Weise kann jede Anwendung mit ihren angestammten Datendateien arbeiten. Projekte können verwendet werden, ohne dass die andere Anwendung oder KicadStepUp installiert ist. Das ist auch der Grund, dass kein Zusatzprogramm auf der Kicad Seite benötigt wird.


</div>


<div class="mw-translate-fuzzy">

Um die feinen Details des Arbeitsablaufs zu verstehen, ist es hilfreich zu wissen, dass die Unterschiede zwischen den beiden Programmen einige Schwierigkeiten für einen vollständigen Datenaustausch mit sich bringen.
Ein Beispiel ist, dass der Skizzierer, der in Kicad verwendet wird, um den Umriss der Platine zu definieren, im Vergleich zum FreeCAD-Sketcher viel begrenzter ist, d. h. um den Modellinhalt hin und her zu kopieren darf der Inhalt des Modells nicht komplexer sein, als der Kicad-Skizzierer verarbeiten kann. Aus der Sicht von FreeCAD bedeutet das, dass man möglicherweise Daten verliert. KicadStepUp bietet Workarounds, die möglicherweise schwieriger zu verstehen sind, wenn man nicht über diesen Hintergrund verfügt.


</div>

### Grundlegender Arbeitsablauf 


<div class="mw-translate-fuzzy">

Eine Zusammenarbeit kann mit einem neuen oder einem bestehenden Projekt begonnen werden. Wir betrachten hier ein neues Projekt, um die Dinge einfach zu halten   *


</div>

1.  Create a new KiCad Project anywhere you like. Lets name it \"KsuTest\"
2.  Open the PCB Editor and create on the layer \"Edit.Cuts\" a closed outline. Shape does not matter, we will overwrite it anyway.
3.  Create a new FreeCAD file for the PCB, the name does not matter. \*
4.  Create a sketch with an outline of the desired PCB. Lets name it \"pcb design\" (but could be any other name) and put at least one circle into it for a hole.

       *   you may use any FreeCAD features to include holes, cutouts, and outer shape to other components you might have. We assume here you would use Sketcher features as Dimensioning, Constraints and Work geometry in your sketch.
       *   If you are using PartDesign Workbench for creating the sketch there is no need to create a PartDesign body, since we are not going to pad this sketch.
5.  Switch to the KicadStepUp Workbech
6.  Select the \"pcb design\" sketch
7.  Select the Toolbar button \"Push Sketch to PCB Edge\" or the menu *ksu PushPull/ksu Push Sketch to PCB*
    -   first a dialog will open with defaults \"Edge.Cuts\" for layer and \"0.16\" for line width. Keep those defaults.
    -   next a file dialog will open. Click to your KiCad \"KsuTest\" project, where you should see a file \"KsuTest.kucad_pcb\". That is the PCB file with the temporary outline we created before. Select it and confirm to replace the old file.
        Now a dialog should say \"new Edge pushed to kicad board!\"

           *   if you forgot the 2nd step, the push operation might fail as a pcb file must exist and it must not be empty.
8.  Close and re-open the PCB Editor in KiCad. \*\*

       *   The shape from the FreeCAD sketch should appear.
9.  Go over the circle with the mouse and press *m* on the keyboard to move the circle. Click to place it in another position. Press the \"Save\" toolbar button on the top left.
10. Switch to FreeCAD and select in the KicadStepUp Workbech the tool button \"Pull Sketch from PCB\" or the menu *ksu PushPull/ksu Pull Sketch from PCB*
    -   first dialog with default layer \"Edge.Cuts\" and three choices will open. Select choice \"replace PCB and Sketch in current document\" \*\*\*
    -   next a file dialog should show again the file \"KsuTest.kucad_pcb\". Select it and press *Open*

           *   You should see your PCB as a 3D model. Note that the hole has moved compared to your \"pcb design\" sketch.
           *   In the tree appears a new structure with a yellow *Part Container* with the KiCad Filename and within another *Part Container* with \"Board_Geoms_e63b\" (the part with the number probably different). In the second container there are the following three files. Do not change any names in that structure, because KicadStepUp uses them to find the parts to update.
           *   Do not forget to save your file




    Local_CS_e63b      the PCB origin.
                         same as the origin in "pcb design" sketch
    Pcb_e63b           3D object with the PCB.
                          Don't edit, it will be overwritten by KicadStepUp
    PCB_Sketch_e63b    sketch with all parts of "pcb design" sketch that KiCad recognized.
                          all others were deleted. Also note that if you change this sketch
                          and recalculate, the 3D object will not change.

Try to make another PushPull round trip   * adjust your \"pcb design\" sketch to the changes from KiCad, add some other change and start again. Do that a few times to appreciate how quickly and naturally this procedure becomes in a very short time.


<div class="mw-translate-fuzzy">

Jetzt kannst du die neue 3D Leiterplattendatei verwenden, um 3D Komponenten wie Steckverbinder, Taster, Schalter, Verschlüsse usw. auszurichten, oder du fügst diese zu deiner Baugruppe hinzu, wenn du ein größeres Projekt hast.


</div>


<div class="mw-translate-fuzzy">

Dies zeigt nur die sehr grundlegende Arbeitsweise von KicadStepUp. Dir fehlt an dieser Stelle noch vieles, z.B. Lötflächenrastern und 3D Teile. Aber von hier aus ist es viel einfacher, KicadStepUp auf eigene Faust zu erkunden. Verwende die Dokumentations PDF Datei im Menü *ksu Tools/Demo*


</div>


   *   \'\'Notes   *
    -   As long as the name of the created structure (and its parts) is unchanged, any workflow interactions will just update the structure. If you change any names, a new structure will be created each time.
    -   It is not required to have KiCad running to update KiCad project files. Actually, KiCad does not even have to be installed on the PC.
    -   The standard approach is to use the same sketch on both sides, KiCad and Freecad. Any changes will be synchronized to the other application. This is the most natural and clean way to work with KicadStepUp .
        However, this causes a problem if you want to use any of the following features in your sketch to define your PCB shape   * dimensions, geometry constraints, construction geometry (blue lines), or external linked geometry. There is no clean way to do this, because KiCad does not know any of those features. That means that on the round trip between the applications, any of those features will be deleted. There is no real solution for that problem, just a selection of one of several workarounds. So if you want to use any of those features, that means you must define the PCB shape in FreeCAD only and sync in one direction toward KiCad. Any outline changes done in KiCad need to be added manually on the FreeCAD side. This might make sense, e.g. if future changes from the mechanical side are much more likely than from the electrical side. There several ways to do it   *
        -   Put the design sketch inside the KicadStepUp structure, and select \"replace PCB and keep Sketch in curr. doc\" every time you import back from Kicad.
        -   Keep the design sketch outside the KicadStepUp structure. Ignore the sketch imported from KiCad.

       *   The second choice has the advantage that changes in KiCad can be traced to the original sketch, and the FreeCAD sketch is protected against an accidentally wrong import choice. The described workflow uses this approach to make sure the issue is well understood. From there it\'s easy to switch to modifying the KicadStepUp supplied sketch with none of the more advanced FreeCAD features.

    -   To use KicadStepUp with a FreeCAD assembly (\> V0.19) you could add a new file for the PCB. After the workflow above has been run once add the 3D object for the PCB to your assembly like any other mechanical part. Make sure you save the file when it was updated by KicadStepUp (Important   * KicadStepUp writes to FreeCAD memory, not to FreeCAD files).

\'\'


<div class="mw-translate-fuzzy">

Bitte schau den [kicad StepUp Spickzettel](https   *//github.com/easyw/kicadStepUpMod/blob/master/demo/kicadStepUp-cheat-sheet.pdf) für die anderen Funktionen an.


</div>

## Referenzen

-   Autor   * Github   * [\@easyw](https   *//github.com/easyw) \| FreeCAD Foren   * [kicad StepUp   * ECAD MCAD bidirektionale Zusammenarbeit](https   *//forum.freecadweb.org/viewtopic.php?f=24&t=14276)
-   Quellcode auf GitHub   * <https   *//github.com/easyw/kicadStepUpMod>

## Nebenbemerkung zu Externen Arbeitsbereichen 

FreeCAD Arbeitsbereiche sind einfach in [Python](Python/de.md) zu programmieren, daher gibt es viele Leute, die zusätzliche Arbeitsbereiche außerhalb der FreeCAD Hauptentwickler entwickeln.

Die Seite [externe Arbeitsbereiche](external_workbenches/de.md) enthält einige Informationen und Anleitungen zu einigen von ihnen, und das Projekt [FreeCAD Erweiterungen](https   *//github.com/FreeCAD/FreeCAD-addons) hat sich zum Ziel gesetzt, diese zu sammeln und sie von FreeCAD aus leicht installierbar zu machen.

Neue Arbeitsbereiche sind in der Entwicklung, bleib dran!




[Category   *Addons](Category_Addons.md) [Category   *External Workbenches](Category_External_Workbenches.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Addons](Category_Addons.md) > [External Workbenches](Category_External Workbenches.md) > KicadStepUp Workbench/de
