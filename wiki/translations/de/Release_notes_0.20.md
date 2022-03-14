# Release notes 0.20/de
<div class="mw-translate-fuzzy">


**Diese Seite verfolgt neue Funktionen, die der Entwicklungsversion von FreeCAD, die derzeit 0.20 ist, hinzugefügt werden. Wenn das Einfrieren der Funktionen von 0.20 eintritt, lösche diese Meldungen und füge keine weiteren Funktionen zu dieser Seite hinzu. FreeCAD 0.20 wird voraussichtlich im Jahr 202x veröffentlicht werden.**


</div>


**!!! Alle Bilder auf dieser Seite müssen den Suffix {{FileName|_relnotes_0.20** verwenden !!!}}


{{Message|
Fehlen Funktionen? Erwähne sie im [https://forum.freecadweb.org/viewtopic.php?f&#61;10&t&#61;56135 Versionshinweise für v0.20] Forumsbeitrag.

Siehe [Hilf FreeCAD](Help_FreeCAD/de.md) für Wege, zu FreeCAD beizutragen.
}}


{{TOCright}}


<div class="mw-translate-fuzzy">

**FreeCAD 0.19** wurde veröffentlicht auf *\'DD Month 202x*, hole es von der [Herunterladen](Download/de.md) Seite. Dies ist eine Zusammenfassung der interessantesten Änderungen. Die vollständige Liste der Änderungen kann im [MantisBT bugtracker FC 0.20 Änderungsprotokoll](https://www.freecadweb.org/tracker/changelog_page.php?version_id=78) eingesehen werden.


</div>

Ältere FreeCAD Versionshinweise findest du unter [Funktionsübersicht](Feature_list/de#Versionshinweise.md).

## Höhepunkte

## Allgemeines


<div class="mw-translate-fuzzy">

### Entwicklung


</div>

Since this release FreeCAD can only be compiled using Qt 5 and Python 3.

Um [FreeCAD unter Windows kompilieren](Compile_on_Windows/de.md), gibt es verschiedene Libpacks (vorgepackte Bibliotheken):

-   Libpack für Windows mit Qt xx, OCC yy, und Python zz

Lowest supported Python version is 3.6.9 according to this [FC forum thread](https://forum.freecadweb.org/viewtopic.php?f=10&t=62701).

Supported operating systems:

-   Windows 7, 8 and 10
-   Linux Ubuntu Bionic Beaver (18.04) and Focal Fossa (20.04)
-   MacOS minimum version 10.12 Sierra

### Bug/Issue Tracker 

The FreeCAD bug tracker was moved to GitHub: <https://github.com/FreeCAD/FreeCAD/issues>

**Note:** Only bug reports with a prior forum discussion will be considered. Reports without this will be closed.

### freecad.org

We are happy that the project [KiCAD](https://www.kicad.org/), through the [KiCAD services corp.](https://www.kipro-pcb.com/), sponsored us the domain freecad.org. Now all FreeCAD websites are available under [freecadweb.org](https://freecadweb.org) and [freecad.org](https://freecad.org).

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
|                                                                                          | In the image the *Hole001* object was selected and then its                                                                                      |
|                                                                                          | dependencies were added to the selection via the context menu.                                                                                   |
+++

+++
| <img alt="" src=images/Part_SectionCut_example_relnotes_0.20.png  style="width:200px;"> | The new tool **[Section Cut](Part_SectionCut.md)** allows to get non-hollow and also persistent cuts of parts and assemblies.             |
|                                                                                                         | [Forum discussion](https://forum.freecadweb.org/viewtopic.php?f=27&t=52441), [Pull request \#4118](https://github.com/FreeCAD/FreeCAD/pull/4118). |
+++

### Weitere Verbesserungen Benutzeroberfläche 


<div class="mw-translate-fuzzy">

-   Es ist nun möglich, die Ansicht des [Abhängigkeitsgraphen](Std_DependencyGraph/de.md) mit der Maus zu verschieben. [Forumsdiskussion](https://forum.freecadweb.org/viewtopic.php?f=3&t=34791), [pull request \#4638](https://github.com/FreeCAD/FreeCAD/pull/4638).
-   Es wurde ein Problem behoben, bei dem die Verwendung eines Stifttabletts (z.B. Wacom Tablett) so langsam war, dass es völlig unbrauchbar wurde. [Forumsdiskussion](https://forum.freecadweb.org/viewtopic.php?f=8&t=45046), [pull request \#4687](https://github.com/FreeCAD/FreeCAD/pull/4687).


</div>


<div class="mw-translate-fuzzy">

## Kernsystem, Anwendung, Basis und Gui Namensräume 


</div>

### Core

   
  <img alt="" src=images/Object_selection_relnotes_0.20.png  style="width:384px;">   When using **Edit → Copy** or **Edit → Duplicate selection** for an object with dependencies there is a new **Use Original Selections** button in the object selection dialog. Click this button to copy/duplicate only the objects you originally selected prior to opening the dialog, ignoring dependencies and ignoring any actions you might have taken while the dialog was open, such as checking or unchecking some of the checkboxes. The effect is the same as if you had unchecked all the checkboxes next to the objects you did not originally select and pressed OK. Note: special care should be taken when copying/duplicating TechDraw Pages. It is recommended to also copy/duplicate all of the children of the Page (Templates, Views, Dimensions, etc.). Otherwise changes to one of the Pages will also impact the other page, for example, deleting one of the Views in one Page also removes it from the other Page. Deleting one of the pages will also remove all the content from the other Page if copies of the content are not also made.
   

   
  <img alt="" src=images/PrefPacks_relnotes_0.20.png  style="width:384px;">   A new type of add-on called a [Preference Pack](Preference_Packs.md) was added, allowing a subset of a user preferences (user.cfg) file to be saved, distributed, and easily applied by other users. Preference Packs can be use to distribute \"Themes,\" for example, by allowing a developer to include both a Qt stylesheet for widgets as well as a set of other colors and styles for items in the user interface that cannot be set using a stylesheet (e.g. text colors in the Python editor or report view, etc.). Anything that can be configured via a user.cfg file can be set using a Preference Pack. [Forum discussion](https://forum.freecadweb.org/viewtopic.php?f=17&t=62477)
   

   
  <img alt="" src=images/Autoload_relnotes_0.20.png  style="width:384px;">   The \"Workbenches\" preference panel was modified to support the ability to \"autoload\" workbenches on FreeCAD startup.
   

### API


<div class="mw-collapsible mw-collapsed toccolours">

#### New Python API 


<div class="mw-collapsible-content">

-   *Circle2dPy::getCircleCenter*: Gets the circle center defined by three points. [commit 3dc91fa2](https://github.com/FreeCAD/FreeCAD/commit/3dc91fa2)

-   *ComplexGeoDataPy::applyRotation*: Applies an additional rotation to the placement. [commit 32592de8](https://github.com/FreeCAD/FreeCAD/commit/32592de8)
-   *ComplexGeoDataPy::applyTranslation*: Applies an additional translation to the placement. [commit 32592de8](https://github.com/FreeCAD/FreeCAD/commit/32592de8)
-   *ComplexGeoDataPy::countSubElements*: Returns the number of elements of a type. [commit 32592de8](https://github.com/FreeCAD/FreeCAD/commit/32592de8)
-   *ComplexGeoDataPy::getElementTypes*: Returns a list of element types. [commit 32592de8](https://github.com/FreeCAD/FreeCAD/commit/32592de8)
-   *ComplexGeoDataPy::getFaces*: Returns a tuple of points and triangles with a given accuracy. [commit 32592de8](https://github.com/FreeCAD/FreeCAD/commit/32592de8)
-   *ComplexGeoDataPy::getLines*: Returns a tuple of points and lines with a given accuracy. [commit 32592de8](https://github.com/FreeCAD/FreeCAD/commit/32592de8)
-   *ComplexGeoDataPy::getLinesFromSubelement*: Returns vertexes and lines from a sub-element. [commit 32592de8](https://github.com/FreeCAD/FreeCAD/commit/32592de8)
-   *ComplexGeoDataPy::getPoints*: Returns a tuple of points and normals with a given accuracy. [commit 32592de8](https://github.com/FreeCAD/FreeCAD/commit/32592de8)
-   *ComplexGeoDataPy::transformGeometry*: Applies a transformation to the underlying geometry. [commit 32592de8](https://github.com/FreeCAD/FreeCAD/commit/32592de8)

-   *ControlPy::showModelView*: Shows the model view. [commit 033bf619](https://github.com/FreeCAD/FreeCAD/commit/033bf619)

-   *DocumentPy::clearDocument*: Clears the whole document. [commit 526dc1a0](https://github.com/FreeCAD/FreeCAD/commit/526dc1a0)
-   *DocumentPy::getFileName*: For a regular document it returns its file name property. For a temporary document it returns its transient directory. [commit 526dc1a0](https://github.com/FreeCAD/FreeCAD/commit/526dc1a0)
-   *DocumentPy::getProgramVersion*: Gets the program version that a project file was created with. [commit 526dc1a0](https://github.com/FreeCAD/FreeCAD/commit/526dc1a0)
-   *DocumentPy::isClosable*: Checks if the document can be closed. [commit 526dc1a0](https://github.com/FreeCAD/FreeCAD/commit/526dc1a0)
-   *DocumentPy::isSaved*: Checks if the document is saved. [commit 526dc1a0](https://github.com/FreeCAD/FreeCAD/commit/526dc1a0)
-   *DocumentPy::isTouched*: Checks if any object is in touched state. [commit 526dc1a0](https://github.com/FreeCAD/FreeCAD/commit/526dc1a0)
-   *DocumentPy::mustExecute*: Checks if any object must be recomputed. [commit 526dc1a0](https://github.com/FreeCAD/FreeCAD/commit/526dc1a0)
-   *DocumentPy::purgeTouched*: Purges the touched state of all objects. [commit 526dc1a0](https://github.com/FreeCAD/FreeCAD/commit/526dc1a0)
-   *DocumentPy::setClosable*: Sets a flag that allows or forbids to close a document. [commit 526dc1a0](https://github.com/FreeCAD/FreeCAD/commit/526dc1a0)

-   *DrawPagePy::requestPaint*: Paints a TechDraw page. [commit 79f9fb68](https://github.com/FreeCAD/FreeCAD/commit/79f9fb68)

-   *HLRBRep\_AlgoPy*: To access Part\'s hidden line removal (HLR). [commit 73a98671](https://github.com/FreeCAD/FreeCAD/commit/73a98671)
-   *HLRBRep\_PolyAlgoPy*: To access Part\'s poly hidden line removal (HLR). [commit ea85cf5e](https://github.com/FreeCAD/FreeCAD/commit/ea85cf5e)
-   *HLRToShapePy*: To access Part\'s hidden line removal (HLR). [commit 73a98671](https://github.com/FreeCAD/FreeCAD/commit/73a98671)
-   *PolyHLRToShapePy*: To access Part\'s poly hidden line removal (HLR). [commit ea85cf5e](https://github.com/FreeCAD/FreeCAD/commit/ea85cf5e)

-   *MDIViewPy::printPdf*: Prints a PDF. [commit c93031da](https://github.com/FreeCAD/FreeCAD/commit/c93031da)
-   *MDIViewPy::printPreview*: Prints a preview. [commit c93031da](https://github.com/FreeCAD/FreeCAD/commit/c93031da)
-   *MDIViewPy::printView*: Prints a view. [commit c93031da](https://github.com/FreeCAD/FreeCAD/commit/c93031da)
-   *MDIViewPy::redoActions*: Redoes actions. [commit c93031da](https://github.com/FreeCAD/FreeCAD/commit/c93031da)
-   *MDIViewPy::undoActions*: Undoes actions. [commit c93031da](https://github.com/FreeCAD/FreeCAD/commit/c93031da)

-   *PrecisionPy*: To access the precision defined by the OpenCascade kernel. [commit 20b86e55](https://github.com/FreeCAD/FreeCAD/commit/20b86e55)

-   *PropertyContainerPy::setDocumentationOfProperty*: Sets the documentation string of a dynamic property of this class. [commit 8cf3cf33](https://github.com/FreeCAD/FreeCAD/commit/8cf3cf33)
-   *PropertyContainerPy::setGroupOfProperty*: Set the name of the group of a dynamic property. [commit 8cf3cf33](https://github.com/FreeCAD/FreeCAD/commit/8cf3cf33)

-   *PythonWorkbenchPy::reloadActive*: Reload the active workbench after changing menus or toolbars. [commit 0bbc253d](https://github.com/FreeCAD/FreeCAD/commit/0bbc253d)

-   *RotationPy::fromEuler*: Sets the Euler angles of a rotation or gets the Euler angles in a given sequence for a rotation. [commit 951a0be9](https://github.com/FreeCAD/FreeCAD/commit/951a0be9)
-   *RotationPy::toEulerAngles*: Gets the Euler angles in a given sequence for this rotation.. [commit c1454dfb](https://github.com/FreeCAD/FreeCAD/commit/c1454dfb)

-   *SpreadsheetViewPy*: To access spreadsheets. [commit 6e713628](https://github.com/FreeCAD/FreeCAD/commit/6e713628)

-   *UnitsApi::sToNumber*: Converts a quantity or float to a string. [commit befbd95d](https://github.com/FreeCAD/FreeCAD/commit/befbd95d)

-   *View3DInventorPy::getCornerCrossSize*: Returns current corner axis cross size. [commit 9d15df29](https://github.com/FreeCAD/FreeCAD/commit/9d15df29)
-   *View3DInventorPy::setPopupMenuEnabled*: Enables popup menu. [commit 9def811a](https://github.com/FreeCAD/FreeCAD/commit/9def811a)
-   *View3DInventorPy::isCornerCrossVisible*: Returns current corner axis cross visibility. [commit 9d15df29](https://github.com/FreeCAD/FreeCAD/commit/9d15df29)
-   *View3DInventorPy::isPopupMenuEnabled*: Returns if popup menu is enabled. [commit 9def811a](https://github.com/FreeCAD/FreeCAD/commit/9def811a)
-   *View3DInventorPy::projectPointToLine*: Projects the given 2d point to a line. [commit b6527a70](https://github.com/FreeCAD/FreeCAD/commit/b6527a70)
-   *View3DInventorPy::setCornerCrossSize*: Defines corner axis cross size. [commit 9d15df29](https://github.com/FreeCAD/FreeCAD/commit/9d15df29)
-   *View3DInventorPy::setCornerCrossVisible*: Defines corner axis cross visibility. [commit 9d15df29](https://github.com/FreeCAD/FreeCAD/commit/9d15df29)

-   *ViewProviderSpreadsheetPy*: To handle spreadsheet cells.[commit 16bbe123](https://github.com/FreeCAD/FreeCAD/commit/16bbe123) and [commit 093f15dc](https://github.com/FreeCAD/FreeCAD/commit/093f15dc)


</div>

#### Changed API 

-   *MeshObject::trim(base, normal)* was changed to *MeshPy::trimByPlane(base, normal)*: Trims the mesh with a given plane. [commit 837de28e](https://github.com/FreeCAD/FreeCAD/commit/837de28e)


</div>

## Erweiterungsverwalter

   
  <img alt="" src=images/AddonManagerExpanded_relnotes_0.20.png  style="width:400px;">   The [Addon Manager](Std_AddonMgr.md) was modified to support the distribution of Preference Packs, and to display information found in an addon\'s metadata. The Addon Manager also includes improved support for Addons whose source code is located at several different git hosting locations. Networking support was improved to provide more robust handling of SSL connections and support for proxies requiring authentication. Support was added for automatically adding macro buttons to the toolbar after installing, for disabling Addons without removing them, and for switching which git branch of an Addon is checked out. Finally, the user interface was modified to improve searching and display of different list filters.
   

## Arbeitsbereich Architektur 

+++
| <img alt="" src=images/ArchWindow_Placement_1r_relnotes_0.20.png  style="width:250px;"> <img alt="" src=images/ArchWindow_Placement_2r_relnotes_0.20.png  style="width:250px;"> | **SketchArch workbench**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                         | With the <img alt="" src=images/Attach_in_SketchArch.svg  style="width:20px;"> [Attach Feature](https://github.com/paullee0/FreeCAD_SketchArch) it is now possible to place <img alt="" src=images/Arch_Window.svg  style="width:20px;"> [Windows](Arch_Window.md) and <img alt="" src=images/Arch_Equipment.svg  style="width:20px;"> [Equipment](Arch_Equipment.md) parametrically and intuitively in relation to <img alt="" src=images/Arch_Wall.svg  style="width:20px;"> [Walls](Arch_Wall.md). To use this feature the experimental external <img alt="" src=images/SketchArch_Workbench.svg  style="width:20px;"> [SketchArch Workbench](https://github.com/paullee0/FreeCAD_SketchArch) must be installed. [Add-on and ReadMe on Github](https://github.com/paullee0/FreeCAD_SketchArch) (Not yet available in the [Add-on Manager](Std_AddonMgr.md)). |
|                                                                                                                                                                                                                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                         | [Forum discussion](https://forum.freecadweb.org/viewtopic.php?f=23&t=50802)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
+++

+++
| <img alt="" src=images/NewArchStructureProperties_relnotes_0.20.jpg  style="width:250px;"> | **New properties in the Arch Structure objects**                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                               | **BasePerpendicularToTool**: it copies the Base (extrusion profile) at the beginning of the Tool (extrusion path) and places it perpendicular to the first edge of the tool. It is the same as attaching the Base with MapMode=NormalToEdge, but its automatic and allows to reuse the same Base object for multiple Structures. When BasePerpendicularToTool = True, more properties control the placement of the Base relative to the Tool axis. They are shown in the attached image.     |
|                                                                                                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                               | **ToolOffsetFirst** and **ToolOffsetLast**: extend/trim the Structure at the start and end respectively (the real length of the Structure is available in the ComputedLength readonly property)                                                                                                                                                                                                                                                                                              |
|                                                                                                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                               | -   BaseRotation: rotate the Base (the rotation is around the Base\'s \"(0,0)\" point which is the center for [Arch Profiles](Arch_Profile.md), the origin for Sketches and usually the first point for [Draft Wires](Draft_Wire.md))                                                                                                                                                                                                                                        |
|                                                                                                               | -   BaseOffsetX and BaseOffsetY: move the Base (extrusion profile)                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                               | -   BaseMirror: mirror the Base (extrusion profile)                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                               | A new command **Create multiple Arch Structure** was also added. It uses the first selected object as a Base, and creates Arch Structures objects for every Edge of the other selected objects. Then, the properties of individual Structure objects can be adjusted in the Property editor. This command was added for workflow with a master Sketch (there is risk of topological naming problem unless you create non-parametric copy of the master Sketch or use Realthunder\'s version) |
|                                                                                                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                               | [Forum discussion](https://forum.freecadweb.org/viewtopic.php?f=23&t=43228&start=60), [Pull request \#3229](https://github.com/FreeCAD/FreeCAD/pull/3229)                                                                                                                                                                                                                                                                                                                                    |
+++

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

-   Support for linear buckling analyses was added. [Pull request \#4379](https://github.com/FreeCAD/FreeCAD/pull/4379)
-   A new constraint was added: **Model → Mechanical Constraints → [<img src=images/FEM_ConstraintCentrif.svg style="width:16px"> [Constraint Centrif](FEM_ConstraintCentrif.md)**. [Pull request \#4738](https://github.com/FreeCAD/FreeCAD/pull/4738)
-   A new solver was added: **Solve → [<img src=images/FEM_SolverMystran.svg style="width:16px"> [Solver Mystran](FEM_SolverMystran.md)**. Multiple commits.
-   A new constraint was added: **Model → Mechanical Constraints → [<img src=images/FEM_ConstraintSpring.svg style="width:16px"> [Constraint Spring](FEM_ConstraintSpring.md)**. [Pull request \#4982](https://github.com/FreeCAD/FreeCAD/pull/4982)
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

New options were added to support running either FreeCAD, OpenSCAD, or both, in sandboxed environments such as AppImages and Snap packages: data can now be transferred to and from OpenSCAD via the standard temporary directory mechanism, via a user-specified temp directory that both executables have access to, or new to OpenSCAD 2021.1, via a \"stdout pipe\" mechanism, bypassing temporary files entirely.

**Add OpenSCAD element** - now has additional options

Load    - load a scad file
Save    - save a scad file
Refresh - Update FreeCAD view
Clear   - Clear text input

There is also a text box for feedback of OpenSCAD errors.

![](images/OpenSCAD_AddElement_relnotes_0.20.png )

## Arbeitsbereich Formteil 

   
  <img alt="" src=images/Part_Extrusion-inner-structures_relnotes_0.20.png  style="width:384px;">Tapered extrusion of a sketch with an inner structure.   A tapered [extrusion](Part_Extrude.md) of inner structures now creates usable results. Previously, inner structures were extruded as if they were stand-alone and not part of a structure. [Pull request \#5367](https://github.com/FreeCAD/FreeCAD/pull/5367)
   

### Weitere Formteil Verbesserungen 

-   The dialog to edit [Cylinders](Part_Cylinder.md) now allows to specify an angle relative to the normal of the chosen attachment plane. This way one can create skew cylinders. [Pull request \#4708](https://github.com/FreeCAD/FreeCAD/pull/4708)

## Arbeitsbereich PartDesign 

+++
| <img alt="" src=images/PD_Pad-Length-along-reference_relnotes_0.20.gif  style="width:384px;">Padding along an edge from the model.Click on the image to show the animation.                                                                     | There is a new option to pad along the direction of an edge in the 3D model. [Pull request \#4685](https://github.com/FreeCAD/FreeCAD/pull/4685)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
+++
| <img alt="" src=images/PartDesign_Chamfer_Face_Selection_relnotes_0.20.png  style="width:384px;">                                                                                                                                                                           | When Distance and Angle is specified in the [Chamfer](PartDesign_Chamfer.md) tool and faces are selected, the distance will be applied along the selected faces. Likewise if two distances are specified then Size 1 will be applied along the selected face. This behaviour can be swapped to the other face using the flip direction button. [Forum discussion](https://forum.freecadweb.org/viewtopic.php?f=19&t=62084), [Pull request \#5039](https://github.com/FreeCAD/FreeCAD/pull/5039)                                                                                                                                                                                                                                                                     |
+++
| <img alt="" src=images/PartDesign_Loft_Vertex_relnotes_0.20.png  style="width:384px;">A loft with multiple sections, the final one is a vertex.                                                                                                                      | It is now possible to create an [Additive](PartDesign_AdditiveLoft.md) or [Subtractive Loft](PartDesign_SubtractiveLoft.md), or an [Additive](PartDesign_AdditivePipe.md) or [Subtractive Pipe](PartDesign_SubtractivePipe.md) towards, or from, a [Vertex](Glossary#V.md) of either a sketch or a body. This allows to create pyramids for example.**Note**: Vertices in sketches are created as construction geometry. To use them as endpoints of lofts, you must first [change them to normal geometry](Sketcher_ToggleConstruction.md). [Pull request \#5170](https://github.com/FreeCAD/FreeCAD/pull/5170) (for lofts), [Pull request \#5193](https://github.com/FreeCAD/FreeCAD/pull/5193) (for pipes) |
+++
| <img alt="" src=images/PD_Pad-Taper-angle_relnotes_0.20.png  style="width:384px;">A tapered pocket within a non-tapered pad.                                                                                                                                             | The dialog for [Pad](PartDesign_Pad.md) and [Pocket](PartDesign_Pocket.md) offers to set a taper angle for the extrusion. [Pull request \#5357](https://github.com/FreeCAD/FreeCAD/pull/5357)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
+++
| <img alt="" src=images/PD_Pocket-direction_relnotes_0.20.gif  style="width:384px;">Pocketing along different directions.Click on the image to show the animation.                                                                                         | It is now possible to specify the direction for the pocket extrusion. [Pull request \#5164](https://github.com/FreeCAD/FreeCAD/pull/5164)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
+++
| <img alt="" src=images/PartDesign_Cylinder_direction_relnotes_0.20.png  style="width:384px;">                                                                                                                                                                                   | The dialog to edit [Cylinders](PartDesign_AdditiveCylinder.md) (additive and subtractive) now allows to specify an angle relative to the normal of the chosen attachment plane. This way one can create skew cylinders. [Pull request \#4708](https://github.com/FreeCAD/FreeCAD/pull/4708)                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
+++
| <img alt="" src=images/PartDesign_Helix_Growth_relnotes_0.20.png  style="width:384px;">                                                                                                                                                                                               | The [Helix](PartDesign_AdditiveHelix.md) feature has the new mode **Height-Turns-Growth** to create flat spirals. [Forum thread](https://forum.freecadweb.org/viewtopic.php?f=19&t=56378) [Pull request \#4590](https://github.com/FreeCAD/FreeCAD/pull/4590)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
+++
| <img alt="" src=images/PartDesign_Islands-Extrude_relnotes_0.20.png  style="width:384px;">A single Pad and a single [Revolution](PartDesign_Revolution.md) with nested profiles. The base block is only there to ensure that the part is a single solid. | All PartDesign features that can extrude sketches can now handle sketches with nested profiles that form islands. For example it is possible to revolve a sketch consisting of 3 nested circles with the same center point.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                       | **Note**: Extruding nested profiles only works if the result is still a single body. [Pull request \#6381](https://github.com/FreeCAD/FreeCAD/pull/6381)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
+++
| <img alt="" src=images/PD_Pad-Length-alog-direction_relnotes_0.20.gif  style="width:384px;">Effect of the new option *Length along sketch normal*.Click on the image to show the animation.                                                      | There is a new option to pad a certain length along the direction. The length is either measured along the sketch normal or along the custom direction. [Forum discussion](https://forum.freecadweb.org/viewtopic.php?f=17&t=50466), [Pull request \#3893](https://github.com/FreeCAD/FreeCAD/pull/3893)                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
+++
| <img alt="" src=images/PartDesign_Hole_thread_relnotes_0.20.PNG  style="width:384px;">                                                                                                                                                                                                 | The [Hole](PartDesign_Hole.md) feature can now model true threads. [Forum thread](https://forum.freecadweb.org/viewtopic.php?f=34&t=54240) [Pull request \#4274](https://github.com/FreeCAD/FreeCAD/pull/4274)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
+++
|                                                                                                                                                                                                                                                                                                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
+++

### Weitere PartDesign Verbesserungen 

-   In the [Helix](PartDesign_AdditiveHelix.md) feature one can now also use the sketch normal as axis. [Pull request \#5199](https://github.com/FreeCAD/FreeCAD/pull/5199)
-   The [Sprocket](PartDesign_Sprocket.md) feature can now also create ISO-normed sprockets. [Forum thread](https://forum.freecadweb.org/viewtopic.php?f=22&t=44525#p478369) [Pull request \#4478](https://github.com/FreeCAD/FreeCAD/pull/4478)
-   The [Loft](PartDesign_AdditiveLoft.md) and [Pipe](PartDesign_AdditivePipe.md) features now allow using the body\'s faces for sections. [Pull request \#5155](https://github.com/FreeCAD/FreeCAD/pull/5155)
-   It is now possible to select several faces before calling the [Pad](PartDesign_Pad.md) or [Pocket](PartDesign_Pocket.md) dialog. In this case the first selected face will be used to determine the default padding/pocketing direction. [commit d34a5616](https://github.com/FreeCAD/FreeCAD/commit/d34a5616a2b38c96ad05f9a0763ba7504dfb814d)
-   In the [Chamfer](PartDesign_Chamfer.md) and [Fillet](PartDesign_Fillet.md) dialogs all edges of a body can be selected via the context menu while in Add mode. [Pull request \#5269](https://github.com/FreeCAD/FreeCAD/pull/5269)
    When you selected a 3D object before clicking the icon to create a fillet or chamfer, all object edges will automatically be selected. [Pull request \#5328](https://github.com/FreeCAD/FreeCAD/pull/5328)
-   [Chamfer](PartDesign_Chamfer.md) and [Fillet](PartDesign_Fillet.md) dialogs now each have a new Use all edges checkbox, which is connected to the Use All Edges property for these objects. When the box is checked the property is set to True, when unchecked the property is set to False. When Use All Edges is True there is protection against the [topological naming problem](Topological_naming_problem.md) because then all of the edges of the base object are used regardless of how many edges there are. [Pull request \#5340](https://github.com/FreeCAD/FreeCAD/pull/5340)
-   Plane selection when [adding a new sketch](PartDesign_NewSketch.md) can now be achieved with a single-click in the 3D View. [Pull request](https://github.com/FreeCAD/FreeCAD/pull/5408) [Forum discussion](https://forum.freecadweb.org/viewtopic.php?f=19&t=65020)
-   When a PartDesign tool is run without an active body, FreeCAD now offers to activate a body or create a new one. [Pull request \#4949](https://github.com/FreeCAD/FreeCAD/pull/4949)
-   The [Face Colors](Part_FaceColors.md) tool is now also available from the PartDesign workbench.

## Arbeitsbereich Pfad 

-   The Extensions feature was added to the [Adaptive](Path_Adaptive.md) operation. [Pull request \#4388](https://github.com/FreeCAD/FreeCAD/pull/4388)
-   The [Helix](Path_Helix.md) operation was refactored and Extra offset property was added to it. [Pull request \#5405](https://github.com/FreeCAD/FreeCAD/pull/5405)
-   The check if the current schema is using minutes for velocity expression and appropriate warning were added. [Pull request \#6357](https://github.com/FreeCAD/FreeCAD/pull/6357)
-   External threads were added to the thread milling operation. [Pull request \#6485](https://github.com/FreeCAD/FreeCAD/pull/6485)
-   The stability of engraving on sketches was improved. [Pull request \#6394](https://github.com/FreeCAD/FreeCAD/pull/6394)
-   The visibility of path objects was made more natural. [Pull request \#4911](https://github.com/FreeCAD/FreeCAD/pull/4911)

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
-   Improved navigation using the **Tab** and **Enter** keys.
-   Improved interface for cutting and pasting blocks of cells.

## Arbeitsbereich Start 

## Arbeitsbereich Oberfläche 

## Arbeitsbereich TechDraw 

   
  <img alt="" src=images/TechDraw_ExtensionExample_relnotes_0.20.png  style="width:400px;">   More than 30 new tools, so-called [Extensions](TechDraw_Workbench#Extensions.md), are now available. They offer new cosmetic features to enhance drawings.
   

### Weitere TechDraw Verbesserungen 

-   It is now possible to [Share](TechDraw_ShareView.md) and [Move](TechDraw_MoveView.md) [Views](TechDraw_Workbench#Views.md) between pages.
-   When there are several [Pages](TechDraw_PageDefault.md) and a [View](TechDraw_View.md), [ProjectionGroup](TechDraw_ProjectionGroup.md) etc. is added, there is now a dialog to ask to what page the view should be added. [Pull request \#5309](https://github.com/FreeCAD/FreeCAD/pull/5309).
-   A new format specifier *%w* was added to print the given number of digits after dot and remove any trailing zeros. [Pull request \#5401](https://github.com/FreeCAD/FreeCAD/pull/5401).
-   The new *%w* format specifier is now the default. And the format specifier preference was moved from the Advanced tab to the Dimension tab. [Pull request \#6504](https://github.com/FreeCAD/FreeCAD/pull/6504).
-   Flipped diagonal hatch was added for the [Geometric Hatch](TechDraw_GeometricHatch.md) tool. [Pull request \#6429](https://github.com/FreeCAD/FreeCAD/pull/6429).
-   There is a new option to show a grid in a [page](TechDraw_PageDefault.md). Several related [preferences](TechDraw_Preferences#Grid.md) have been introduced. [Pull request \#6465](https://github.com/FreeCAD/FreeCAD/pull/6465).

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
