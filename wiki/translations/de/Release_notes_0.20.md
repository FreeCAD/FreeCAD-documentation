# Release notes 0.20/de
**Diese Seite verfolgt neue Funktionen, die der Entwicklungsversion von FreeCAD, die derzeit 0.20 ist, hinzugefügt werden. Wenn das Einfrieren der Funktionen von 0.20 eintritt, lösche diese Meldungen und füge keine weiteren Funktionen zu dieser Seite hinzu. FreeCAD 0.20 wird voraussichtlich im Jahr 202x veröffentlicht werden.**


**!!! Alle Bilder auf dieser Seite müssen den Suffix {{FileName|_relnotes_0.20** verwenden !!!}}


{{Message|
Fehlen Funktionen? Erwähne sie im [https://forum.freecadweb.org/viewtopic.php?f&#61;10&t&#61;56135 Versionshinweise für v0.20] Forumsbeitrag.

Siehe [Hilf FreeCAD](Help_FreeCAD/de.md) für Wege, zu FreeCAD beizutragen.
}}


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

Lowest supported Python version is 3.6.9 according to this [FC forum thread](https://forum.freecadweb.org/viewtopic.php?f=10&t=62701).

Supported Operating Systems:

-   Windows 7, 8 and 10
-   Linux Ubuntu Bionic Beaver (18.04) and Focal Fossa (20.04)
-   MacOS minimum version 10.12 Sierra

Weitere Neuigkeiten zur Entwicklung:

### Dokumentation

### Bekannte Begrenzungen 

## Benutzeroberfläche


<div class="mw-translate-fuzzy">

+++
| ![](images/Navi_Cube_relnotes_0.20.gif ) | Der Navigationswürfel wurde überarbeitet, um diese neuen Funktionen zu ermöglichen:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                | -   Es gibt jetzt Kantenflächen, um die Szene in Winkeln von 45° zu betrachten.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                | -   Die neue Voreinstellungsoption [Nächste Drehung](Preferences_Editor/de#Navigation.md) erlaubt es, die Szene in der nächstgelegenen sinnvollen Position zu betrachten. Wenn sie ausgeschaltet ist, wird das Anklicken einer Würfelfläche immer an der gleichen Position angezeigt, unabhängig davon, in welchem Würfelzustand du dich befandest, als du die Fläche angeklickt hast. Klicke auf das Bild auf der linken Seite, um zu sehen, was das bedeutet. Versuche die gleiche Klicksequenz wie im Bild ohne die Option *Drehen zum nächstgelegenen*, um den Unterschied zu erleben. |
|                                                                | -   Wenn du auf den Punkt oben rechts im Würfel klickst, kannst du schnell die Rückansicht der aktuellen Szene sehen.                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                | -   Die Größe des Würfels kann über die Einstellungsoption [Würfelgröße](Preferences_Editor/de#Navigation.md) angepasst werden.                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                | [Forumsdiskussion](https://forum.freecadweb.org/viewtopic.php?f=3&t=52118), [pull request \#4502](https://github.com/FreeCAD/FreeCAD/pull/4502).                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
+++


</div>

   
  ![](images/Improved_tooltips_relnotes_0.20.gif )   Tooltips now display the command name in the title, making it easier for new users to look for help. At the end of the tooltip the \"internal\" command name is added in parentheses: *(Std\_WhatsThis)*. This is also the name of the page that documents the command in the Wiki. [Forum discussion](https://forum.freecadweb.org/viewtopic.php?f=34&t=58747), [Pull request \#4978](https://github.com/FreeCAD/FreeCAD/pull/4978).
   

   
  <img alt="" src=images/Std_UserEditMode_relnotes_0.20.gif  style="width:384px;">   The new [Std UserEditMode](Std_UserEditMode.md) command allows the user to choose an edit mode that will be used when an object is double-clicked in the [Tree view](Tree_view.md). Click the image at the left so see an animation of the selection. If a selected edit mode is not applicable, the object\'s default edit mode is used instead. [Pull request \#5110](https://github.com/FreeCAD/FreeCAD/pull/5110).
   

+++
| ![](images/Dependencies-selection_relnotes_0.20.png ) | The [Tree view](Tree_view.md) context menu has the new entry **Add dependent objects to selection**.           |
|                                                                                          | [Forum discussion](https://forum.freecadweb.org/viewtopic.php?f=8&t=13566), [Pull request \#4133](https://github.com/FreeCAD/FreeCAD/pull/4133). |
|                                                                                          |                                                                                                                                                  |
|                                                                                          | In the image the *Hole001* object was selected by the user and then                                                                              |
|                                                                                          | its dependencies were added to the selection via the context menu.                                                                               |
+++

### Weitere Verbesserungen Benutzeroberfläche 


<div class="mw-translate-fuzzy">

-   Es ist nun möglich, die Ansicht des [Abhängigkeitsgraphen](Std_DependencyGraph/de.md) mit der Maus zu verschieben. [Forumsdiskussion](https://forum.freecadweb.org/viewtopic.php?f=3&t=34791), [pull request \#4638](https://github.com/FreeCAD/FreeCAD/pull/4638).
-   Es wurde ein Problem behoben, bei dem die Verwendung eines Stifttabletts (z.B. Wacom Tablett) so langsam war, dass es völlig unbrauchbar wurde. [Forumsdiskussion](https://forum.freecadweb.org/viewtopic.php?f=8&t=45046), [pull request \#4687](https://github.com/FreeCAD/FreeCAD/pull/4687).


</div>

## Kernsystem, Anwendung, Basis und Gui Namensräume 

   
  <img alt="" src=images/Object_selection_relnotes_0.20.png  style="width:384px;">   When using **Edit → Copy** or **Edit → Duplicate selection** for an object with dependencies there is a new **Use Original Selections** button in the object selection dialog. Click this button to copy/duplicate only the objects you originally selected prior to opening the dialog, ignoring dependencies and ignoring any actions you might have taken while the dialog was open, such as checking or unchecking some of the checkboxes. The effect is the same as if you had unchecked all the checkboxes next to the objects you did not originally select and pressed OK. Note: special care should be taken when copying/duplicating TechDraw Pages. It is recommended to also copy/duplicate all of the children of the Page (Templates, Views, Dimensions, etc.). Otherwise changes to one of the Pages will also impact the other page, for example, deleting one of the Views in one Page also removes it from the other Page. Deleting one of the pages will also remove all the content from the other Page if copies of the content are not also made.
   

-   A new type of add-on called a [Preference Pack](Preference_Packs.md) was added, allowing a subset of a user preferences (user.cfg) file to be distributed and applied. [Forum discussion](https://forum.freecadweb.org/viewtopic.php?f=17&t=62477), [Pull request \#4787](https://github.com/FreeCAD/FreeCAD/pull/4787)

## Erweiterungsverwalter

## Arbeitsbereich Architektur 

++++
| <img alt="" src=images/ArchWindow_Placement_1r_relnotes_0.20.png  style="width:250px;"> | <img alt="" src=images/ArchWindow_Placement_2r_relnotes_0.20.png  style="width:250px;"> | -   With the <img alt="" src=images/Attach_in_SketchArch.svg  style="width:20px;"> [Attach Feature](https://github.com/paullee0/FreeCAD_SketchArch) it is now possible to place <img alt="" src=images/Arch_Window.svg  style="width:20px;"> [Windows](Arch_Window.md) and <img alt="" src=images/Arch_Equipment.svg  style="width:20px;"> [Equipment](Arch_Equipment.md) parametrically and intuitively in relation to <img alt="" src=images/Arch_Wall.svg  style="width:20px;"> [Walls](Arch_Wall.md). To use this feature the experimental external <img alt="" src=images/SketchArch_Workbench.svg  style="width:20px;"> [SketchArch Workbench](https://github.com/paullee0/FreeCAD_SketchArch) must be installed. |
|                                                                                                         |                                                                                                         | -   [Forum discussion](https://forum.freecadweb.org/viewtopic.php?f=23&t=50802), [Add-on and ReadMe on Github](https://github.com/paullee0/FreeCAD_SketchArch) (Not yet available in the [Add-on Manager](Std_AddonMgr.md)).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
++++

## Arbeitsbereich Entwurf 

-   A **Global** checkbox was added to the task panel of many drafting commands. Checking it allows input of coordinates in the global coordinate system even if the [working plane](Draft_SelectPlane.md) is not aligned with the global XY plane.

-   The <img alt="" src=images/Draft_Hatch.svg  style="width:24px;"> [Draft Hatch](Draft_Hatch.md) command was introduced. It creates hatches on the faces of a selected object using patterns from AutoCAD PAT files.

-   The <img alt="" src=images/Draft_AddNamedGroup.svg  style="width:24px;"> [Draft AddNamedGroup](Draft_AddNamedGroup.md) command was introduced. The <img alt="" src=images/Draft_AddToGroup.svg  style="width:24px;"> [Draft AddToGroup](Draft_AddToGroup.md) command was extended with the same functionality.

-   Work on the <img alt="" src=images/Draft_SetStyle.svg  style="width:24px;"> [Draft SetStyle](Draft_SetStyle.md) command, still in progress in FreeCAD version 0.19, was completed.

-   A double-click edit option was added for <img alt="" src=images/Draft_Text.svg  style="width:24px;"> [Draft Texts](Draft_Text.md). It opens the same edit task panel used when creating a text.

-   For <img alt="" src=images/Draft_Dimension.svg  style="width:24px;"> [Draft Dimensions](Draft_Dimension.md) the {{Value|arch}} **Unit Override** for imperial architectural dimensions was introduced.

-   <img alt="" src=images/Draft_Shape2DView.svg  style="width:24px;"> [Draft Shape2DView](Draft_Shape2DView.md) objects now have an **Auto Update** property. Setting it to {{False}} can be useful if there are many Draft Shape2DViews in a document or if they are complex.

-   It is now possible to reverse a [Draft Wire](Draft_Wire.md) via the <img alt="" src=images/Draft_Edit.svg  style="width:24px;"> [Draft Edit](Draft_Edit.md) context menu. [Forum discussion](https://forum.freecadweb.org/viewtopic.php?f=23&t=58643&start=20), [Pull request \#4811](https://github.com/FreeCAD/FreeCAD/pull/4811).

### Weitere Entwurf Verbesserungen 

-   Behoben [Entwurf Fang Gitter](Draft_Snap_Grid/de.md), wenn sich der Mauszeiger über einer Fläche befindet. [Forumsdiskussion](https://forum.freecad.org/viewtopic.php?f=23&t=62274). [Git commit](https://github.com/FreeCAD/FreeCAD/commit/1761eb8ce).

-   New [Draft Texts](Draft_Text.md) are now aligned with the [working plane](Draft_SelectPlane.md), [Pull request \#5092](https://github.com/FreeCAD/FreeCAD/pull/5092).

-   Support for two DWG converters was added: [LibreDWG](https://www.gnu.org/software/libredwg) and [QCAD pro](https://qcad.org/en/qcad-command-line-tools#dwg2dwg). See [Import Export Preferences](Import_Export_Preferences#DWG.md) and [FreeCAD and DWG Import](FreeCAD_and_DWG_Import.md) for more information.

## Arbeitsbereich FEM 


<div class="mw-translate-fuzzy">

   
  <img alt="" src=images/FEM_Gmsh-MeshSizeFromCurvature_relnotes_0.20.png  style="width:384px;"> Wirkung von *Netzweite von Krümmung*; links: auf 12 gesetzt, rechts: deaktiviert                 Es gibt eine neue Eigenschaft für den [Gmsh](FEM_MeshGmshFromShape/de.md) Vernetzer. Die Anzahl der Netzelemente pro $2\pi$ mal dem Radius der Krümmung kann angegeben werden. Der Standardwert ist 12. Um ein feineres Netz an kleinen Ecken oder Löchern zu erhalten, kann dieser Wert erhöht werden, um bessere Ergebnisse zu erzielen. Diese Funktion erfordert Gmsh 4.8 oder eine neuere Version. [Forumsdiskussion](https://forum.freecadweb.org/viewtopic.php?f=18&t=56401), [pull request \#4596](https://github.com/FreeCAD/FreeCAD/pull/4596)
  <img alt="" src=images/FEM_Gmsh-RecombinationAlgorithm_relnotes_0.20.png  style="width:384px;"> Auswirkung des rcombination Algorithmus; links: mit *Simple*, rechts: mit *Simple full-quad*   FreeCAD erlaubt nun die Auswahl eines Algorithmus sowie die 3D Netzrekombination für den [Gmsh](FEM_MeshGmshFromShape.md) Vernetzers. Für weitere Details über die Rekombination von Netzelementen siehe [FEM NetzGmshAusForm](FEM_MeshGmshFromShape/de#Element_Rekombination.md). [Pull request \#4706](https://github.com/FreeCAD/FreeCAD/pull/4706)
   


</div>

### Weitere FEM Verbesserungen 

-   A new solver was added: **Solve → [<img src=images/FEM_SolverMystran.svg style="width:16px"> [Solver Mystran](FEM_SolverMystran.md)**. Multiple commits.
-   A new constraint was added: **Model → Geometrical Constraints → [<img src=images/FEM_ConstraintSpring.svg style="width:16px"> [Constraint Spring](FEM_ConstraintSpring.md)**. [Pull request \#4982](https://github.com/FreeCAD/FreeCAD/pull/4982)
-   The element order of [Gmsh](FEM_MeshGmshFromShape.md) meshes can be changed via the mesh dialog. [Pull request \#4660](https://github.com/FreeCAD/FreeCAD/pull/4660)
-   Material cards can now contain values for the electrical conductivity. [Pull request \#4647](https://github.com/FreeCAD/FreeCAD/pull/4647)
-   Material cards added for Nitrogen and Argon. [Pull request \#4649](https://github.com/FreeCAD/FreeCAD/pull/4649)
-   Support for the [Gmsh](FEM_MeshGmshFromShape.md) mesh algorithms \"HXT\" (3D) and \"Packing Parallelograms\" (2D) added. [Pull request \#4654](https://github.com/FreeCAD/FreeCAD/pull/4654)
-   Allow to set for the [Gmsh](FEM_MeshGmshFromShape#Properties.md) property **High Order Optimize** a certain algorithm. [Pull request \#4705](https://github.com/FreeCAD/FreeCAD/pull/4705)
-   Nonlinear solid materials with simple hardening can now have an arbitrary number of yield points. [Pull request \#5024](https://github.com/FreeCAD/FreeCAD/pull/5024)
-   Allow modal adding/removal of geometric entities to constraints acting on boundaries. [Pull request \#5117](https://github.com/FreeCAD/FreeCAD/pull/5117)
-   Most FEM constraint dialogs now behave uniformly and provide the same 3D object selection features. [Pull request \#5391](https://github.com/FreeCAD/FreeCAD/pull/5391)

## Import

## Materialhandhabung

## Polygonnetze

### Improved support for NASTRAN GRID elements 

The Mesh import tool now supports the high-precision \"GRID\*\" element. The standard-precision \"GRID\" element was also improved, now supporting both space-delimited numeric input as well as fixed-field-width input, per the NASTRAN95 format documentation.

### Weitere Polygonnetz Verbesserungen 

Fixed false negatives during self-intersection tests when facets are coplanar: [Pull request \#5002](https://github.com/FreeCAD/FreeCAD/pull/5002).

## OpenSCAD Arbeitsbereich 

Interoperability with OpenSCAD has been improved, adding support for several operations missing from earlier versions (linear extrude with rotations, rotational extrusions). Several operations are modified to provide improved FreeCAD object equivalents, particularly for twisted extrusions. Surface generation from discrete data was modified to give more OpenSCAD-like results, rather than splined surfaces.

**Add OpenSCAD element** - now has additional options

Load    - load a scad file
Save    - save a scad file
Refresh - Update FreeCAD view
Clear   - Clear text input

There is also a text box for feedback of OpenSCAD errors.

## Arbeitsbereich Formteil 

### Weitere Formteil Verbesserungen 

-   The dialog to edit [Cylinders](Part_Cylinder.md) allows now to specify an angle in respect to the normal of the chosen attachment plane. This way one can create skew cylinders. [Pull request \#4708](https://github.com/FreeCAD/FreeCAD/pull/4708)

## Arbeitsbereich PartDesign 

   
  <img alt="" src=images/PD_Pocket-direction_relnotes_0.20.gif  style="width:384px;">Pocketing along different directions.Click on the image to show the animation.                                      It is now possible to specify the direction for the pocket extrusion. [Pull request \#5164](https://github.com/FreeCAD/FreeCAD/pull/5164)
  <img alt="" src=images/PD_Pad-Length-along-reference_relnotes_0.20.gif  style="width:384px;">Padding along an edge from the model.Click on the image to show the animation.                  There is a new option to pad along the direction of an edge in the 3D model. [Pull request \#4685](https://github.com/FreeCAD/FreeCAD/pull/4685)
  <img alt="" src=images/PD_Pad-Length-alog-direction_relnotes_0.20.gif  style="width:384px;">Effect of the new option *Length along sketch normal*.Click on the image to show the animation.   There is a new option to pad a certain length along the direction. The length is either measured along the sketch normal or along the custom direction. [Forum discussion](https://forum.freecadweb.org/viewtopic.php?f=17&t=50466), [Pull request \#3893](https://github.com/FreeCAD/FreeCAD/pull/3893)
  <img alt="" src=images/PartDesign_Cylinder_direction_relnotes_0.20.png  style="width:384px;">                                                                                                                                The dialog to edit [Cylinder](PartDesign_AdditiveCylinder.md) (additive and subtractive) allows now to specify an angle in respect to the normal of the chosen attachment plane. This way one can create skew cylinders. [Pull request \#4708](https://github.com/FreeCAD/FreeCAD/pull/4708)
  <img alt="" src=images/PartDesign_Chamfer_Face_Selection_relnotes_0.20.png  style="width:384px;">                                                                                                                        When Distance and Angle is specified in the [Chamfer](PartDesign_Chamfer.md) tool and faces are selected, the distance will be applied along the selected faces. Likewise if two distances are specified then Size 1 will be applied along the selected face. This behaviour can be swapped to the other face using the flip direction button. [Forum discussion](https://forum.freecadweb.org/viewtopic.php?f=19&t=62084), [Pull request \#5039](https://github.com/FreeCAD/FreeCAD/pull/5039)
  <img alt="" src=images/PartDesign_Loft_Vertex_relnotes_0.20.png  style="width:384px;">                                                                                                                                              It is now possible to create an [Additive Loft](PartDesign_AdditiveLoft.md), [Subtractive Loft](PartDesign_SubtractiveLoft.md), [Additive Pipe](PartDesign_AdditivePipe.md) or [Subtractive Pipe](PartDesign_SubtractivePipe.md) towards or from a [Vertex](Glossary#V.md) of either a sketch or a body. This allows for example to create pyramids. [Pull request \#5170](https://github.com/FreeCAD/FreeCAD/pull/5170) (for lofts), [Pull request \#5193](https://github.com/FreeCAD/FreeCAD/pull/5193) (for pipes)
  <img alt="" src=images/PartDesign_Helix_Growth_relnotes_0.20.png  style="width:384px;">                                                                                                                                            The [Helix](PartDesign_AdditiveHelix.md) feature has the new mode **Height-Turns-Growth** to create flat spirals. [Forum thread](https://forum.freecadweb.org/viewtopic.php?f=19&t=56378) [Pull request \#4590](https://github.com/FreeCAD/FreeCAD/pull/4590)
   

### Weitere PartDesign Verbesserungen 

-   In the [Helix](PartDesign_AdditiveHelix.md) feature one can now also use the sketch normal as axis. [Pull request \#5199](https://github.com/FreeCAD/FreeCAD/pull/5199)
-   The [Sprocket](PartDesign_Sprocket.md) feature can now create also ISO-normed sprockets. [Forum thread](https://forum.freecadweb.org/viewtopic.php?f=22&t=44525#p478369) [Pull request \#4478](https://github.com/FreeCAD/FreeCAD/pull/4478)
-   The [Loft](PartDesign_AdditiveLoft.md) and [Pipe](PartDesign_AdditivePipe.md) features now allow using the body\'s faces for sections. [Pull request \#5155](https://github.com/FreeCAD/FreeCAD/pull/5155)
-   It is now possible to select several faces before calling the [Pad](PartDesign_Pad.md) or [Pocket](PartDesign_Pocket.md) dialog. In this case the first selected face will be used to determine the default padding/pocketing direction. [commit d34a5616](https://github.com/FreeCAD/FreeCAD/commit/d34a5616a2b38c96ad05f9a0763ba7504dfb814d)
-   In the [Chamfer](PartDesign_Chamfer.md) and [Fillet](PartDesign_Fillet.md) dialogs all edges of a body can be selected via the context menu while in Add mode. [Pull request \#5269](https://github.com/FreeCAD/FreeCAD/pull/5269)
    When you selected a 3D object before clicking the icon to create a fillet or chamfer, all object edges will automatically be selected. [Pull request \#5328](https://github.com/FreeCAD/FreeCAD/pull/5328)

## Arbeitsbereich Pfad 

## Arbeitsbereich Rendern 

## Arbeitsbereich Skizzierer 


<div class="mw-translate-fuzzy">

   
  <img alt="" src=images/SketcherSplitExample2.png )                                                  Neue ![](images/Sketcher_Split.svg  style="width:24px;"> [Aufteilen](Sketcher_Split/de.md) Funktion zum Aufteilen bestehender Linien oder Bögen. [Forumsdiskussion](https://forum.freecadweb.org/viewtopic.php?f=9&t=55412) [pull request \#4420](https://github.com/FreeCAD/FreeCAD/pull/4420)
  <img alt="" src=images/SketcherCreateRoundedRectangleExample.png )                  Neues ![](images/Sketcher_CreateOblong.svg  style="width:24px;"> [Abgerundetes Rechteck](Sketcher_CreateOblong.md) Werkzeug zum Erstellen von Rechtecken mit abgerundeten Ecken. [Forumsdiskussion](https://forum.freecadweb.org/viewtopic.php?f=17&t=59210) [Main pull request \#4835](https://github.com/FreeCAD/FreeCAD/pull/4835)
  <img alt="" src=images/SketcherCreateCenteredRectangleExample.png  style="width:384px;">   Neu <img alt="" src=images/Sketcher_CreateRectangle_Center.svg  style="width:24px;"> [Zentriertes Rechteck](Sketcher_CreateRectangle_Center/de.md) Werkzeug um Rechtecke über einen Mittelpunkt zu definieren. [Main commit](https://github.com/FreeCAD/FreeCAD/commit/8b4acf11c2caf53cc1cb8dccd8bb6de8516f4492)
  <img alt="" src=images/Radiam_anim.gif  style="width:384px;">                                                         Neu <img alt="" src=images/Sketcher_ConstrainRadiam.svg  style="width:24px;"> [Radiam](Sketcher_ConstrainRadiam/de.md) Funktion zur automatischen Zuweisung von Gewicht auf B-Spline Pol, Durchmesser auf Vollkreis oder Radius auf Bogen. Unterstützung von Mehrfachauswahl als Durchmesser/Radius Werkzeuge. [Forumsdiskussion](https://forum.freecadweb.org/viewtopic.php?f=3&t=57584&start=20#p509485) [Haupt-Pull-Request \#4855](https://github.com/FreeCAD/FreeCAD/pull/4855)
  <img alt="" src=images/SketcherRemoveAxesAlignmentResult.png )                          Neues ![](images/Sketcher_RemoveAxesAlignment.svg  style="width:24px;"> [Achsenausrichtung entfernen](Sketcher_RemoveAxesAlignment/de.md) Beschränkungswerkzeug zum Entfernen der Achsenausrichtung unter Beibehaltung der Beschränkungsbeziehung der Auswahl. [Main commit](https://github.com/FreeCAD/FreeCAD/commit/3c593a33cedc3e6a42928d9087f8a160852cc685)
   


</div>

### Weitere Skizzierer Verbesserungen 


<div class="mw-translate-fuzzy">

-   Überarbeitete Stutzen Unterstützung:

[Pull Anfrage](https://github.com/FreeCAD/FreeCAD/pull/4330) [Forumsdiskussion](https://forum.freecadweb.org/viewtopic.php?f=10&t=54441) \<\-- Benötigt Screencasts

-   Das Verhalten des <img alt="" src=images/Sketcher_CreateSlot.svg  style="width:24px;"> [Schlitz](Sketcher_CreateSlot/de.md) hat sich geändert. Schlitze können nun durch die Definition des Zentrums beider Halbkreise erstellt werden. [Pull Anfrage](https://github.com/FreeCAD/FreeCAD/pull/4843) [Forumsdiskussion](https://forum.freecadweb.org/viewtopic.php?f=17&t=59243&p=508658#p508658)
-   Die Sichtbarkeitsautomatik erlaubt es, Skizzierer im [Abschnittsmodus](Sketcher_ViewSection/de.md) zu öffnen, wenn man in den Bearbeitungsmodus wechselt. [Pull Anfrage](https://github.com/FreeCAD/FreeCAD/pull/4742) [Forumsdiskussion](https://forum.freecadweb.org/viewtopic.php?f=3&t=57056)
-   Sichtbarkeits Automatisierung erlaubt es, die Kamera in den [Orthographic mode](Std_OrthographicCamera/de.md) zu zwingen, wenn man den Editiermodus betritt. [Pull request](https://github.com/FreeCAD/FreeCAD/pull/4778) [Forumsdiskussion](https://forum.freecadweb.org/viewtopic.php?f=22&t=44747)


</div>

## Arbeitsbereich Tabellenkalkulation 

   
  <img alt="" src=images/Spreadsheet-Preferences-Spreadsheet_relnotes_0.20.png )   The workbench now has ![](images/Std_DlgPreferences.svg  style="width:24px;"> [Preferences](Spreadsheet_Preferences.md). They are used by the <img alt="" src=images/Spreadsheet_Import.svg  style="width:16px;"> [Spreadsheet Import](Spreadsheet_Import.md) and <img alt="" src=images/Spreadsheet_Export.svg  style="width:16px;"> [Spreadsheet Export](Spreadsheet_Export.md) commands. [Pull request \#5073](https://github.com/FreeCAD/FreeCAD/pull/5073)
   

-   It is now possible to select in the row/column context-menu at what positions new rows/columns will be inserted. [Pull request \#4704](https://github.com/FreeCAD/FreeCAD/pull/4704).

### Weitere Verbesserungen Tabellenkalkulation 

-   Import XLSX (used by [Std Import](Std_Import.md)): Added support for floor and ceil functions. [Pull request \#5015](https://github.com/FreeCAD/FreeCAD/pull/5015).
-   Cell binding: instruct a set of cells to display the contents of another set of cells. Part of [Pull request \#2862](https://github.com/FreeCAD/FreeCAD/pull/2862).
-   Improved navigation using the Tab and Enter keys.
-   Improved interface for cutting and pasting blocks of cells.

## Arbeitsbereich Start 

## Arbeitsbereich Oberfläche 

## Arbeitsbereich TechDraw 

+++
| <img alt="" src=images/TechDraw_ExtensionExample_relnotes_0.20.png  style="width:400px;"> | Several new tools, so-called [Extensions](TechDraw_Workbench#Extensions.md), are now available. They offer new cosmetic features to enhance drawings:                                    |
|                                                                                                             |                                                                                                                                                                                                  |
|                                                                                                             | -   <img alt="" src=images/TechDraw_ExtensionCircleCenterLines.svg  style="width:24px;"> [TechDraw ExtensionCircleCenterLines](TechDraw_ExtensionCircleCenterLines.md) |
|                                                                                                             | -   <img alt="" src=images/TechDraw_ExtensionThreadHoleSide.svg  style="width:24px;"> [TechDraw ExtensionThreadHoleSide](TechDraw_ExtensionThreadHoleSide.md)             |
|                                                                                                             | -   <img alt="" src=images/TechDraw_ExtensionThreadBoltSide.svg  style="width:24px;"> [TechDraw ExtensionThreadBoltSide](TechDraw_ExtensionThreadBoltSide.md)             |
|                                                                                                             | -   <img alt="" src=images/TechDraw_ExtensionThreadHoleBottom.svg  style="width:24px;"> [TechDraw ExtensionThreadHoleBottom](TechDraw_ExtensionThreadHoleBottom.md)     |
|                                                                                                             | -   <img alt="" src=images/TechDraw_ExtensionThreadBoltBottom.svg  style="width:24px;"> [TechDraw ExtensionThreadBoltBottom](TechDraw_ExtensionThreadBoltBottom.md)     |
+++

### Weitere TechDraw Verbesserungen 

-   When there are several [Pages](TechDraw_PageDefault.md) and a [View](TechDraw_View.md), [ProjectionGroup](TechDraw_ProjectionGroup.md) etc. is added, there is now a dialog to ask to what page the view should be added. [Pull request \#5309](https://github.com/FreeCAD/FreeCAD/pull/5309).

## Internet

## Externe Arbeitsbereiche 


**Note:**

these are the new workbenches created in this development cycle, or older workbenches that received updates. See [external workbenches](External_workbenches.md) for more workbenches that can be installed, and which cover a wide variety of topics. If you want to see your workbench added, join the [forum](https://forum.freecadweb.org/index.php) and present your code.

### 3D Druckwerkzeuge 

### A2plus

### Assembly3

### Assembly4

### ArchitekturTexturen

### BOLTSFC

### Arbeitsbereich GekrümmteFormen 

### Dodo (ehemals Flamingo) 

### Befestigungselemente

### FCGear

The [FCGear Workbench](FCGear_Workbench.md) received a couple of improvements

-   For involute gears, the outside (aka tip) and root diameter are exposed as properties ([details](https://github.com/looooo/freecad.gears/pull/69))
-   Gear objects are now [attachable](Part_EditAttachment.md) ([details](https://github.com/looooo/freecad.gears/pull/72))
-   Gear objects can now be used as additive features in PartDesign Bodies ([details](https://github.com/looooo/freecad.gears/pull/74))
-   The creation of gear objects now appears in the undo stack ([details](https://github.com/looooo/freecad.gears/pull/83))

### Polygonnetz Remodellierung Arbeitsbereich 

### MOOC Arbeitsbereich 

### KnotenEditor (PyFlow) 

### Wege, PyTrails, Abbieger, pivy\_trackers, und Geomatik



---
![](images/Right_arrow.png) [documentation index](../README.md) > [News](Category_News.md) > [Documentation](Category_Documentation.md) > [Releases](Category_Releases.md) > Release notes 0.20/de
