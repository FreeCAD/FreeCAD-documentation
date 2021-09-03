


{{VeryImportantMessage|Diese Seite verfolgt neue Funktionen, die der Entwicklungsversion von FreeCAD, die derzeit 0.20 ist, hinzugefügt werden. Wenn das Einfrieren der Funktionen von 0.20 eintritt, lösche diese Meldungen und füge keine weiteren Funktionen zu dieser Seite hinzu. FreeCAD 0.20 wird voraussichtlich im Jahr 202x veröffentlicht werden.}}


{{VeryImportantMessage|!!! Alle Bilder auf dieser Seite müssen den Suffix {{FileName|_relnotes_0.20}} verwenden !!!}}


<div style="text-align:center; background:#e0e0ee; margin:1em 7em; padding:0.5em 2em; border:2px solid #bb7736;">

Fehlen Funktionen? Erwähne sie im [Versionshinweise für v0.20](https://forum.freecadweb.org/viewtopic.php?f=10&t=34586) Forumsbeitrag.

Siehe [Hilf FreeCAD](Help_FreeCAD.md) für Wege, zu FreeCAD beizutragen.


</div>


{{TOCright}}

**FreeCAD 0.19** wurde veröffentlicht auf *\'DD Month 202x*, hole es von der [Herunterladen](Download/de.md) Seite. Dies ist eine Zusammenfassung der interessantesten Änderungen. Die vollständige Liste der Änderungen kann im [MantisBT bugtracker FC 0.20 Änderungsprotokoll](https://www.freecadweb.org/tracker/changelog_page.php?version_id=78) eingesehen werden.

Ältere FreeCAD Versionshinweise findest du unter [Funktionsübersicht](Feature_list/de#Versionshinweise.md).

## Höhepunkte

## Allgemeines

### Python 3 und Qt5 

### Bekannte Probleme 

### Entwicklung

Um [FreeCAD unter Windows kompilieren](Compile_on_Windows/de.md), gibt es verschiedene Libpacks (vorgepackte Bibliotheken):

-   Libpack für Windows mit Qt xx, OCC yy, und Python zz

Weitere Neuigkeiten zur Entwicklung:

### Dokumentation

### Bekannte Begrenzungen 

## Benutzeroberfläche


<div class="mw-translate-fuzzy">

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Der Navigationswürfel wurde überarbeitet, um diese neuen Funktionen zu ermöglichen:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| -   Es gibt jetzt Kantenflächen, um die Szene in Winkeln von 45° zu betrachten.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| -   Die neue Voreinstellungsoption [Nächste Drehung](Preferences_Editor/de#Navigation.md) erlaubt es, die Szene in der nächstgelegenen sinnvollen Position zu betrachten. Wenn sie ausgeschaltet ist, wird das Anklicken einer Würfelfläche immer an der gleichen Position angezeigt, unabhängig davon, in welchem Würfelzustand du dich befandest, als du die Fläche angeklickt hast. Klicke auf das Bild auf der linken Seite, um zu sehen, was das bedeutet. Versuche die gleiche Klicksequenz wie im Bild ohne die Option *Drehen zum nächstgelegenen*, um den Unterschied zu erleben. |
| -   Wenn du auf den Punkt oben rechts im Würfel klickst, kannst du schnell die Rückansicht der aktuellen Szene sehen.                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| -   Die Größe des Würfels kann über die Einstellungsoption [Würfelgröße](Preferences_Editor/de#Navigation.md) angepasst werden.                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [Forumsdiskussion](https://forum.freecadweb.org/viewtopic.php?f=3&t=52118), [pull request \#4502](https://github.com/FreeCAD/FreeCAD/pull/4502).                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


</div>

  -------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![](images/Improved_tooltips_relnotes_0.20.gif )   Tooltips now display the command name in the title, making it easier for new users to look for help. At the end of the tooltip the \"internal\" command name is added in parentheses: *(Std\_WhatsThis)*. This is also the name of the page that documents the command in the Wiki. [Forum discussion](https://forum.freecadweb.org/viewtopic.php?f=34&t=58747), [pull request \#4978](https://github.com/FreeCAD/FreeCAD/pull/4978).
  -------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Weitere Verbesserungen der Benutzeroberfläche 

-   Es ist nun möglich, die Ansicht des [Abhängigkeitsgraphen](Std_DependencyGraph/de.md) mit der Maus zu verschieben. [Forumsdiskussion](https://forum.freecadweb.org/viewtopic.php?f=3&t=34791), [pull request \#4638](https://github.com/FreeCAD/FreeCAD/pull/4638).
-   Es wurde ein Problem behoben, bei dem die Verwendung eines Stifttabletts (z.B. Wacom Tablett) so langsam war, dass es völlig unbrauchbar wurde. [Forumsdiskussion](https://forum.freecadweb.org/viewtopic.php?f=8&t=45046), [pull request \#4687](https://github.com/FreeCAD/FreeCAD/pull/4687).

## Anwendung::Verknüpfung und Zusammenbau 

## Kernsystem, Anwendung, Basis und Gui Namensräume 

## Erweiterungsverwalter


<div class="mw-translate-fuzzy">

## Arbeitsbereich Architektur 


</div>

## Arbeitsbereich Entwurf 

### Weitere Entwurf Verbesserungen 

-   Es ist nun möglich, einen [Entwurf Draht](Draft_Wire/de.md) über das [Entwurf Bearbeiten](Draft_Edit/de.md) Kontextmenü umzukehren. [Forumsdiskussion](https://forum.freecadweb.org/viewtopic.php?f=23&t=58643&start=20), [pull request \#4811](https://github.com/FreeCAD/FreeCAD/pull/4811).

## Arbeitsbereich FEM 


<div class="mw-translate-fuzzy">

  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  <img alt="" src=images/FEM_Gmsh-MeshSizeFromCurvature.png  style="width:384px;">Wirkung von *Netzweite von Krümmung*; links: auf 12 gesetzt, rechts: deaktiviert                 Es gibt eine neue Eigenschaft für den [Gmsh](FEM_MeshGmshFromShape/de.md) Vernetzer. Die Anzahl der Netzelemente pro $2\pi$ mal dem Radius der Krümmung kann angegeben werden. Der Standardwert ist 12. Um ein feineres Netz an kleinen Ecken oder Löchern zu erhalten, kann dieser Wert erhöht werden, um bessere Ergebnisse zu erzielen. Diese Funktion erfordert Gmsh 4.8 oder eine neuere Version. [Forumsdiskussion](https://forum.freecadweb.org/viewtopic.php?f=18&t=56401), [pull request \#4596](https://github.com/FreeCAD/FreeCAD/pull/4596)
  <img alt="" src=images/FEM_Gmsh-RecombinationAlgorithm.png  style="width:384px;">Auswirkung des rcombination Algorithmus; links: mit *Simple*, rechts: mit *Simple full-quad*   FreeCAD erlaubt nun die Auswahl eines Algorithmus sowie die 3D Netzrekombination für den [Gmsh](FEM_MeshGmshFromShape.md) Vernetzers. Für weitere Details über die Rekombination von Netzelementen siehe [diese Wiki Seite](FEM_MeshGmshFromShape/de#Element_Rekombination.md). [Pull request \#4706](https://github.com/FreeCAD/FreeCAD/pull/4706)
  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


</div>

### Weitere FEM Verbesserungen 

-   The element order of [Gmsh](FEM_MeshGmshFromShape.md) meshes can be changed via the mesh dialog. [PR \#4660](https://github.com/FreeCAD/FreeCAD/pull/4660)
-   Material cards can now contain values for the electrical conductivity. [PR \#4647](https://github.com/FreeCAD/FreeCAD/pull/4647)
-   Material cards added for Nitrogen and Argon. [PR \#4649](https://github.com/FreeCAD/FreeCAD/pull/4649)
-   Support for the [Gmsh](FEM_MeshGmshFromShape.md) mesh algorithms \"HXT\" (3D) and \"Packing Parallelograms\" (2D) added. [PR \#4654](https://github.com/FreeCAD/FreeCAD/pull/4654)
-   Allow to set for the [Gmsh](FEM_MeshGmshFromShape#Properties.md) property **High Order Optimize** a certain algorithm. [PR \#4705](https://github.com/FreeCAD/FreeCAD/pull/4705)

## Import

## Materialhandhabung

## Polygonnetze

### Weitere Verbesserungen 

## OpenSCAD Arbeitsbereich 

Interoperability with OpenSCAD has been improved, adding support for several operations missing from earlier versions (linear extrude with rotations, rotational extrusions). Several operations are modified to provide improved FreeCAD object equivalents, particularly for twisted extrusions. Surface generation from discrete data was modified to give more OpenSCAD-like results, rather than splined surfaces.

## Arbeitsbereich Formteil 

### Weitere Verbesserungen 

-   The dialog to edit [Cylinders](Part_Cylinder.md) allows now to specify an angle in respect to the normal of the chosen attachment plane. This way one can create skew cylinders. [Pull request \#4708](https://github.com/FreeCAD/FreeCAD/pull/4708)

## Arbeitsbereich PartDesign 

  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  <img alt="" src=images/PD_Pad-Length-alog-direction_relnotes_0.20.gif  style="width:384px;">Effect of the new option *Length along sketch normal*.Click on the image to show the animation.   There is a new option to pad a certain length along the direction. The length is either measured along the sketch normal or along the custom direction. [Forum discussion](https://forum.freecadweb.org/viewtopic.php?f=17&t=50466), [pull request \#3893](https://github.com/FreeCAD/FreeCAD/pull/3893)
  <img alt="" src=images/PartDesign_Cylinder_direction_relnotes_0.20.png  style="width:384px;">                                                                                                                                The dialog to edit [Cylinder](PartDesign_AdditiveCylinder.md) (additive and subtractive) allows now to specify an angle in respect to the normal of the chosen attachment plane. This way one can create skew cylinders. [pull request \#4708](https://github.com/FreeCAD/FreeCAD/pull/4708)
  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Weitere Verbesserungen 

-   The [Helix](PartDesign_AdditiveHelix.md) feature has the new mode **Height-Turns-Growth** to create flat spirals. [Forum thread](https://forum.freecadweb.org/viewtopic.php?f=19&t=56378) [PR \#4590](https://github.com/FreeCAD/FreeCAD/pull/4590)
-   The [Sprocket](PartDesign_Sprocket.md) feature can now create also ISO-normed sprockets. [Forum thread](https://forum.freecadweb.org/viewtopic.php?f=22&t=44525#p478369) [PR \#4478](https://github.com/FreeCAD/FreeCAD/pull/4478)

## Arbeitsbereich Pfad 

## Arbeitsbereich Rendern 

## Arbeitsbereich Skizzierer 


<div class="mw-translate-fuzzy">

  ----------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  <img alt="" src=images/SketcherSplitExample2.png )                                                  Neue ![](images/Sketcher_Split.svg  style="width:24px;"> [Aufteilen](Sketcher_Split/de.md) Funktion zum Aufteilen bestehender Linien oder Bögen. [Forumsdiskussion](https://forum.freecadweb.org/viewtopic.php?f=9&t=55412) [pull request \#4420](https://github.com/FreeCAD/FreeCAD/pull/4420)
  <img alt="" src=images/SketcherCreateRoundedRectangleExample.png )                  Neues ![](images/Sketcher_CreateOblong.svg  style="width:24px;"> [Abgerundetes Rechteck](Sketcher_CreateOblong.md) Werkzeug zum Erstellen von Rechtecken mit abgerundeten Ecken. [Forumsdiskussion](https://forum.freecadweb.org/viewtopic.php?f=17&t=59210) [Main pull request \#4835](https://github.com/FreeCAD/FreeCAD/pull/4835)
  <img alt="" src=images/SketcherCreateCenteredRectangleExample.png  style="width:384px;">   Neu <img alt="" src=images/Sketcher_CreateRectangle_Center.svg  style="width:24px;"> [Zentriertes Rechteck](Sketcher_CreateRectangle_Center/de.md) Werkzeug um Rechtecke über einen Mittelpunkt zu definieren. [Main commit](https://github.com/FreeCAD/FreeCAD/commit/8b4acf11c2caf53cc1cb8dccd8bb6de8516f4492)
  <img alt="" src=images/Radiam_anim.gif  style="width:384px;">                                                         Neu <img alt="" src=images/Sketcher_ConstrainRadiam.svg  style="width:24px;"> [Radiam](Sketcher_ConstrainRadiam/de.md) Funktion zur automatischen Zuweisung von Gewicht auf B-Spline Pol, Durchmesser auf Vollkreis oder Radius auf Bogen. Unterstützung von Mehrfachauswahl als Durchmesser/Radius Werkzeuge. [Forumsdiskussion](https://forum.freecadweb.org/viewtopic.php?f=3&t=57584&start=20#p509485) [Haupt-Pull-Request \#4855](https://github.com/FreeCAD/FreeCAD/pull/4855)
  <img alt="" src=images/SketcherRemoveAxesAlignmentResult.png )                          Neues ![](images/Sketcher_RemoveAxesAlignment.svg  style="width:24px;"> [Achsenausrichtung entfernen](Sketcher_RemoveAxesAlignment/de.md) Beschränkungswerkzeug zum Entfernen der Achsenausrichtung unter Beibehaltung der Beschränkungsbeziehung der Auswahl. [Main commit](https://github.com/FreeCAD/FreeCAD/commit/3c593a33cedc3e6a42928d9087f8a160852cc685)
  ----------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


</div>

### Weitere Verbesserungen 

-   Überarbeitete Stutzen Unterstützung:

[Pull Anfrage](https://github.com/FreeCAD/FreeCAD/pull/4330) [Forumsdiskussion](https://forum.freecadweb.org/viewtopic.php?f=10&t=54441) \<\-- Benötigt Screencasts

-   Das Verhalten des <img alt="" src=images/Sketcher_CreateSlot.svg  style="width:24px;"> [Schlitz](Sketcher_CreateSlot/de.md) hat sich geändert. Schlitze können nun durch die Definition des Zentrums beider Halbkreise erstellt werden. [Pull Anfrage](https://github.com/FreeCAD/FreeCAD/pull/4843) [Forumsdiskussion](https://forum.freecadweb.org/viewtopic.php?f=17&t=59243&p=508658#p508658)
-   Die Sichtbarkeitsautomatik erlaubt es, Skizzierer im [Abschnittsmodus](Sketcher_ViewSection/de.md) zu öffnen, wenn man in den Bearbeitungsmodus wechselt. [Pull Anfrage](https://github.com/FreeCAD/FreeCAD/pull/4742) [Forumsdiskussion](https://forum.freecadweb.org/viewtopic.php?f=3&t=57056)
-   Sichtbarkeits Automatisierung erlaubt es, die Kamera in den [Orthographic mode](Std_OrthographicCamera/de.md) zu zwingen, wenn man den Editiermodus betritt. [Pull request](https://github.com/FreeCAD/FreeCAD/pull/4778) [Forumsdiskussion](https://forum.freecadweb.org/viewtopic.php?f=22&t=44747)

### Fehlerberichtigungen

-   Fix \'Reference\' option not working for radius/diameter at creation time [PR for radius](https://github.com/FreeCAD/FreeCAD/pull/4744) [PR for diameter](https://github.com/FreeCAD/FreeCAD/pull/4832) [Forum discussion](https://forum.freecadweb.org/viewtopic.php?f=3&t=57584)

## Arbeitsbereich Tabellenkalkulation 

-   It is now possible to select in the row/column context-menu at what positions new rows/columns will be inserted. Furthermore, when selecting several rows/columns, the row/column context-menu offers now to insert as many new rows/columns as selected. [pull request \#4704](https://github.com/FreeCAD/FreeCAD/pull/4704).

## Arbeitsbereich Start 

## Arbeitsbereich Oberfläche 

## Arbeitsbereich TechDraw 

### Weitere TechDraw Verbesserungen 

## Internet

## Zusätzliche Module 

### 3D Druckwerkzeuge 

### A2plus

### Assembly3

### Assembly4

### ArchitekturTexturen

### BOLTSFC

### Arbeitsbereich GekrümmteFormen 

### Dodo (ehemals Flamingo) 

### Befestigungselemente

### Polygonnetz Remodellierung Arbeitsbereich 

### MOOC Arbeitsbereich 

### KnotenEditor (PyFlow) 

### Wege, PyTrails, Abbiege, pivy\_trackers, und Geomatik 

[Category:News{{\#translation:}}](Category:News.md) [Category:Documentation{{\#translation:}}](Category:Documentation.md) [Category:Releases{{\#translation:}}](Category:Releases.md)
