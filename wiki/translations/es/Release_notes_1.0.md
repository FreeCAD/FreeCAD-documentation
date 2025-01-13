# Release notes 1.0/es
**FreeCAD 1.0** fue liberado el **18 de noviembre del 2024**, consíguelo desde la página [Descarga](Download/es.md). Este es un resumen de las nuevas características y los cambios más interesantes.

Las notas de lanzamiento de versiones anteriores de FreeCAD se pueden encontrar en la [Lista de características](Feature_list/es#Notas_de_lanzamiento.md).


<div lang="en" dir="ltr" class="mw-content-ltr">

## In memoriam: Bradley McLean (bgbsww) 


</div>

Por mucho que estemos encantados de presentarles esta nueva versión, también nos entristece anunciar que nuestro amigo y prolífico desarrollador de FreeCAD [bgbsww](https://github.com/bgbsww) falleció unas semanas antes de que saliera esta versión. Fue uno de los principales arquitectos del esfuerzo de corrección de nombres topológicos, escribió una gran cantidad de código y pruebas adicionales y se convirtió en el especialista en TNP de FreeCAD. También ayudó a prácticamente todos los demás desarrolladores a adaptarse al nuevo algoritmo. Este lanzamiento está dedicado a él.

## General


<div lang="en" dir="ltr" class="mw-content-ltr">

+++
| <img alt="" src=images/TNP_fix_relnotes_1.0.PNG  style="width:320px;"> | The long-standing [Topological naming problem](Topological_naming_problem.md) has finally been addressed thanks to the joint effort and hard work of several developers. [Realthunder\'s algorithm](https://github.com/realthunder/FreeCAD_assembly3/wiki/Topological-Naming-Algorithm) has been carefully implemented and improved to work in the master version of FreeCAD. The project took over a year, and the initial implementation has been finalized with the following PR enabling the improvements. The TNP problem is not completely solved and further improvements will follow in the next version. [Pull request #13705](https://github.com/FreeCAD/FreeCAD/pull/13705) |
+++


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

+++
| <img alt="" src=images/AssemblyExample_relnotes_1.0.png  style="width:320px;"> | FreeCAD has a new built-in [Assembly Workbench](Assembly_Workbench.md), based on the original work done for what we used to call \"[the other FreeCAD](https://www.askoh.com/freecad/what_is_freecad/index.html)\", another software, also named FreeCAD, with motion simulation capabilities created at the same time as ours. The porting has been done by the other FreeCAD\'s author himself, [Dr. Aik-Siong Koh](https://www.askoh.com), and with this dramatic move both FreeCADs are now finally united. Read below for [more information](#Assembly_Workbench.md). [Pull request #10427](https://github.com/FreeCAD/FreeCAD/pull/10427) |
+++


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

+++
| <img alt="" src=images/Freecad.svg  style="width:320px;"> | FreeCAD has a new logo. It was selected from the 5 winners of the public contest. Usage guidelines and a logo kit are available on the [FreeCAD brand guidelines page](https://fpa.freecad.org/handbook/process/logo.html). [Pull request #14284](https://github.com/FreeCAD/FreeCAD/pull/14284) |
+++


</div>



## Interfaz de usuario 

+++
| <img alt="" src=images/Rotation_Center_Indicator_relnotes_1.0.gif  style="width:320px;"> | Se ha agregado un indicador del centro de rotación. Este indicador se muestra cuando se gira la vista arrastrando el mouse. Opcionalmente se puede desactivar en las preferencias. También hay configuraciones para su color, transparencia y tamaño. [Pull request #9909](https://github.com/FreeCAD/FreeCAD/pull/9909) y [Pull request #10790](https://github.com/FreeCAD/FreeCAD/pull/10790) |
+++


<div class="mw-translate-fuzzy">

   
  <img alt="" src=images/Selection_filters_relnotes_1.0.gif  style="width:320px;">Haga clic en la imagen si la animación no inicia.   Se agregaron filtros de selección, facilitando la selección de vértices, aristas y caras. [Pull request #10271](https://github.com/FreeCAD/FreeCAD/pull/10271)
   


</div>


<div class="mw-translate-fuzzy">

+++
| <img alt="" src=images/Tasks_Dockable_relnotes_1.0.png  style="width:320px;"> | Para mayor flexibilidad, el panel de tareas ahora es un widget acoplable independiente, pero el diseño anterior se ha mantenido como predeterminado. [Pull request #10681](https://github.com/FreeCAD/FreeCAD/pull/10681) y [Pull request #10848](https://github.com/FreeCAD/FreeCAD/pull/10848) |
+++


</div>

+++
| <img alt="" src=images/Transform_tool_relnotes_1.0.png  style="width:320px;"> | Se ha mejorado la apariencia de la herramienta de arrastre [Transformar](Std_TransformManip/es.md). Ahora también tiene un conjunto de arrastradores planos para mover objetos a lo largo de los 3 planos predeterminados. [Pull request #10706](https://github.com/FreeCAD/FreeCAD/pull/10706) |
+++


<div lang="en" dir="ltr" class="mw-content-ltr">

+++
| <img alt="" src=images/Overlay_relnotes_1.0.png  style="width:320px;"> | Realthunder\'s feature allowing for the overlay of dock widgets (tree and task transparency) has been added. [Pull request #7888](https://github.com/FreeCAD/FreeCAD/pull/7888) |
+++


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

+++
| <img alt="" src=images/Light_source_relnotes_1.0.png  style="width:320px;"> | The light source position can now be set in the preferences (*Preferences → Display*). [Pull request #11146](https://github.com/FreeCAD/FreeCAD/pull/11146) and [Pull request #15877](https://github.com/FreeCAD/FreeCAD/pull/15877) |
+++


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

+++
| <img alt="" src=images/Preference_tree_relnotes_1.0.png  style="width:320px;"> | The Preferences window was redesigned to replace the tabs with a tree view. [Pull request #11018](https://github.com/FreeCAD/FreeCAD/pull/11018) |
+++


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

+++
| <img alt="" src=images/TabBar_relnotes_1.0.png  style="width:320px;"> | TabBar workbench selector was added. It can be enabled and configured in *Preferences → Workbenches*. [Pull request #12270](https://github.com/FreeCAD/FreeCAD/pull/12270) |
+++


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

+++
| <img alt="" src=images/Unified_measurement_relnotes_1.0.PNG  style="width:320px;"> | A new [universal measurement tool](Std_Measure.md) was added, replacing the old [Part Measure tools](Part_Workbench#Measure.md). [Pull request #9750](https://github.com/FreeCAD/FreeCAD/pull/9750) and following |
+++


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

   
  <img alt="" src=images/Normal_view_relnotes_1.0.gif  style="width:320px;">Click on the image if the animation does not start.   The [Align to selection](Std_AlignToSelection.md) tool was added, making it possible to enter views normal to faces or following edge directions. [Pull request #13906](https://github.com/FreeCAD/FreeCAD/pull/13906)
   


</div>



### Otras mejoras de la interfaz de usuario 


<div lang="en" dir="ltr" class="mw-content-ltr">

-   A project unit system was introduced. [Pull request #9521](https://github.com/FreeCAD/FreeCAD/pull/9521)
-   The [Section Cut](Part_SectionCut.md) tool now also works in a perspective view. [Pull request #10143](https://github.com/FreeCAD/FreeCAD/pull/10143)
-   An option to sort workbenches alphabetically (available after right-clicking in *Preferences → Workbenches*) was added. [Pull request #10363](https://github.com/FreeCAD/FreeCAD/pull/10363)
-   A **Find file** filter and a **Find in files** filter were added to the [Std DlgMacroExecute](Std_DlgMacroExecute.md) dialog. [Pull request #10714](https://github.com/FreeCAD/FreeCAD/pull/10714)
-   The [View menu](Std_View_Menu.md) and the View toolbar have been revised. [Pull request #10761](https://github.com/FreeCAD/FreeCAD/pull/10761)
-   The stop button was removed from the [Macro toolbar](Macros.md). The [record button](Std_DlgMacroRecord.md) now switched to a stop button when recording is in progress. [Pull request #10836](https://github.com/FreeCAD/FreeCAD/pull/10836)
-   The reset button in the Preferences now shows a menu with options to reset the settings at different levels: all, in the current group or in the current tab. [Pull request #10688](https://github.com/FreeCAD/FreeCAD/pull/10688) and [Pull request #11038](https://github.com/FreeCAD/FreeCAD/pull/11038)
-   The Help Module was merged so that it\'s no longer necessary to download an add-on to make use of it. [Pull request #11008](https://github.com/FreeCAD/FreeCAD/pull/11008)
-   Preferences to customize the current theme were added. [Pull request #10238](https://github.com/FreeCAD/FreeCAD/pull/10238)
-   Default selection settings were changed to make the selection of objects in the 3D window easier. [Pull request #11187](https://github.com/FreeCAD/FreeCAD/pull/11187)
-   A meters-only unit scheme named **Meter decimal** was added since the MKS (m/kg/s/degree) system doesn\'t always result in dimensions being displayed in meters - millimeters are still used for values below 0.1 m while for some applications (e.g. civil engineering) a unit system that actually changes the display of all dimensions to meters is useful. [Pull request #11365](https://github.com/FreeCAD/FreeCAD/pull/11365)
-   Additional marker sizes (20, 25 and 30px) were added to *Preferences → Display → 3D View → Marker size* in order to assist users of 4K screens. [Pull request #11524](https://github.com/FreeCAD/FreeCAD/pull/11524)
-   A *Toggle transparency* option was added to the View and context menus to quickly switch transparency on or off for selected objects. [Pull request #10805](https://github.com/FreeCAD/FreeCAD/pull/10805)
-   A Lock toolbars command was added. With it toolbar positions can be locked or unlocked. It is available in the View menu and the toolbar area context menu. [Pull request #11596](https://github.com/FreeCAD/FreeCAD/pull/11596)
-   Default shape color was adjusted to improve the appearance of the models. [Pull request #12380](https://github.com/FreeCAD/FreeCAD/pull/12380) and [Pull request #12488](https://github.com/FreeCAD/FreeCAD/pull/12488)
-   Items within Part and Group containers can now be sorted by drag and drop. [Pull request #12293](https://github.com/FreeCAD/FreeCAD/pull/12293)
-   Visibility icons (eye symbol) are added to tree objects if the Show visibility icon option is checked in *Preferences → Display → UI*. [Pull request #12298](https://github.com/FreeCAD/FreeCAD/pull/12298)
-   A [frozen](Std_ToggleFreeze.md) status (*Toggle freeze* option in the context menu in the [tree](Tree_view.md)) was added, making it possible to turn off the parametric behavior of an object (so that it doesn\'t change even if the objects it depends on change). [Pull request #12580](https://github.com/FreeCAD/FreeCAD/pull/12580)
-   Navigation animations have been improved. Animations now use an easing function and have a fixed duration which can be changed in *Preferences → Display → Navigation*. [Pull request #10881](https://github.com/FreeCAD/FreeCAD/pull/10881) and [Pull request #12205](https://github.com/FreeCAD/FreeCAD/pull/12205)
-   The buttons for the default views are now grouped under a single button. The individual buttons are still available in the additional *Individual views* toolbar. [Pull request #12878](https://github.com/FreeCAD/FreeCAD/pull/12878)
-   The name of the current active document is now also displayed in the window title bar. [Pull request #12035](https://github.com/FreeCAD/FreeCAD/pull/12035)
-   A command to display the [Property View](Property_editor.md) panel was added. [Pull request #12024](https://github.com/FreeCAD/FreeCAD/pull/12024)
-   The integration of 3Dconnexion devices with FreeCAD on Windows was improved. [Pull request #12929](https://github.com/FreeCAD/FreeCAD/pull/12929)
-   A Quick Measure feature was added. It uses the [Status bar](Status_bar.md) to display key measurement information (edge length, face area, distance/angle between points/edges and radius of circular edges/cylindrical faces) about the current selection in the 3D view. [Pull request #12217](https://github.com/FreeCAD/FreeCAD/pull/12217)
-   Toolbars can now be dragged and dropped to the status and menu bars. [Pull request #13571](https://github.com/FreeCAD/FreeCAD/pull/13571)
-   A *Reload stylesheet* button was added to aid the stylesheet development. It doesn\'t belong to any toolbar by default, it has to be added manually from *Tools → Customize → Toolbars → View*. [Pull request #13982](https://github.com/FreeCAD/FreeCAD/pull/13982)
-   Document icons (including the [Open](Std_Open.md) and [Save](Std_Save.md) ones, among others) were improved and unified. [Pull request #13865](https://github.com/FreeCAD/FreeCAD/pull/13865)
-   The [Fit all](Std_ViewFitAll.md) icon was replaced for clarity. [Pull request #14180](https://github.com/FreeCAD/FreeCAD/pull/14180)
-   Multiple core icons (such as [New](Std_New.md)) were improved. [Pull request #14278](https://github.com/FreeCAD/FreeCAD/pull/14278), [Pull request #14434](https://github.com/FreeCAD/FreeCAD/pull/14434) and [Pull request #14154](https://github.com/FreeCAD/FreeCAD/pull/14154)
-   Icons of the Sketcher and Part Design task panel headers were improved. [Pull request #13968](https://github.com/FreeCAD/FreeCAD/pull/13968)
-   In [headless mode](Headless_FreeCAD.md) the interactive Python console now features tab-completion, provided the [readline](https://docs.python.org/3/library/readline.html) module is available. [Pull request #14213](https://github.com/FreeCAD/FreeCAD/pull/14213)
-   An option to display internal names in the tree view was added. It\'s disabled by default and can be activated in *Preferences → Display → UI → Hide Internal Names*. [Pull request #14237](https://github.com/FreeCAD/FreeCAD/pull/14237)
-   The Help button was removed from the Preferences because it was non-functional. [Pull request #14695](https://github.com/FreeCAD/FreeCAD/pull/14695)
-   Default stylesheets were improved significantly and are now offered in two variants other than classic - light and dark. [Pull request #13772](https://github.com/FreeCAD/FreeCAD/pull/13772)
-   The Theme and UI pages in the Display group of the Preferences have been reorganized and combined. Some preferences have been moved to the new Advanced page. [Pull request #14974](https://github.com/FreeCAD/FreeCAD/pull/14974)
-   The Part/Part Design check and refine preferences are now activated by default. [Pull request #14406](https://github.com/FreeCAD/FreeCAD/pull/14406)
-   A new parameter was added - **BaseApp/Preferences/Bitmaps/Theme/UseIconTheme** (boolean): Set to true to force Qt to use icons from the system\'s icon theme. The default is false so FreeCAD will use its own icons. It does not affect other Qt icon theme mechanisms such as system dialogs, buttons and others. Those should always use the icons from the system theme. [Pull request #16018](https://github.com/FreeCAD/FreeCAD/pull/16018)
-   Stylesheet, theme and QtStyle information is now included in *Help → About FreeCAD*. [Pull request #16281](https://github.com/FreeCAD/FreeCAD/pull/16281)
-   Splash screen is now randomly selected on startup from multiple images including user models and presentations of some of the add-on workbenches. [Pull request #16071](https://github.com/FreeCAD/FreeCAD/pull/16071)
-   A safe mode was added and can be activated via *Help → Restart in safe mode*. It temporarily disables user configurations, addons, themes and other customizations to run FreeCAD in a \"factory reset\" state for debugging. [Pull request #16858](https://github.com/FreeCAD/FreeCAD/pull/16858)


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

## File format changes 


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

Although precautions have been taken to guarantee that files created with the new 1.0 version can still be opened in older versions of FreeCAD, some new features introduced in 1.0 cannot be understood by earlier versions, and can cause models saved with 1.0 to break or present problems when opened in earlier versions of FreeCAD. Here is a summary of possible issues you might encounter and their solution. The forum community can also provide help in fixing compatibility issues.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   the **Attachment** property has been renamed to **AttachmentSupport**. This means features relying on that property (most notably models using the Assembly4 addon) will need to be fixed to be opened in an earlier version of FreeCAD. A [macro is available here](Macro_Convert_021.md) to fix those files.


</div>



## Núcleo del sistema y API 


<div lang="en" dir="ltr" class="mw-content-ltr">

### Core


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   Vector functions from the [Vector API](Vector_API.md) can now be used in [Expressions](Expressions.md). [Pull request #8603](https://github.com/FreeCAD/FreeCAD/pull/10237).
-   The Python editor now matches indentation of the previous line when pressing the enter key. [Pull request #11356](https://github.com/FreeCAD/FreeCAD/pull/11356).
-   The name of the property holding the reference object(s) of an attachment has changed from **Support** to **AttachmentSupport**. [Pull request #12714](https://github.com/FreeCAD/FreeCAD/pull/12714).
-   A property container, App::VarSet, has been introduced as a core feature. A VarSet allows users to define properties that can be used in models just as spreadsheet aliases and other previous property containers (Dynamic Data, Path PropertyBags, and Assembly 4 Variables). [Pull Request #12135](https://github.com/FreeCAD/FreeCAD/pull/12135)


</div>

### API



#### Nueva API de Python 


<div lang="en" dir="ltr" class="mw-content-ltr">

-    {{Incode|getUpDirection}}: Gets the up-direction from a View3DInventor view. [Pull request #10060](https://github.com/FreeCAD/FreeCAD/pull/10060)


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

#### Changed Python API 


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   To save/restore custom data from a Python feature, the previously called methods {{Incode|__getstate__}}/{{Incode|__setstate__}} have been renamed to {{Incode|dumps}}/{{Incode|loads}}. This is due to internal changes in Python-3.11. [Pull request #10769](https://github.com/FreeCAD/FreeCAD/pull/10769) and [Pull request #12243](https://github.com/FreeCAD/FreeCAD/pull/12243).


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

## Start


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

The Start Workbench has been replaced by a Start page, a QtWidgets-based app. It can be displayed using the *Help → Start* option. [Pull request #13134](https://github.com/FreeCAD/FreeCAD/pull/13134)


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

The first two pull requests mentioned below belong to the Start Workbench, but have informed the design of the Start page.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

+++
| <img alt="" src=images/Start_page_template_buttons_new_relnotes_1.0.png  style="width:384px;"> | A **New file** section that includes a number of quick-start buttons has been added to the Start Page. [Pull request #10171](https://github.com/FreeCAD/FreeCAD/pull/10171) |
+++


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

+++
| <img alt="" src=images/Start_page_layout_relnotes_1.0.png  style="width:384px;"> | The visual design of the Start Page has been overhauled. It now looks more modern and consistent. [Pull request #10391](https://github.com/FreeCAD/FreeCAD/pull/10391) |
+++


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

+++
| <img alt="" src=images/First_start_relnotes_1.0.png  style="width:384px;"> | A simple first start widget was added and will be extended in the near future. [Pull request #13650](https://github.com/FreeCAD/FreeCAD/pull/13650) |
+++


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

## Assembly Workbench 


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

+++
| <img alt="" src=images/Assembly_relnotes_1.0.png  style="width:384px;"> | A built-in [Assembly workbench](Assembly_Workbench.md) was finally added to FreeCAD. It uses the open-source [Ondsel solver](https://github.com/Ondsel-Development/OndselSolver). Basic functionalities (joints) are already available. Further development is in progress. [Pull request #10427](https://github.com/FreeCAD/FreeCAD/pull/10427), [Pull request #10764](https://github.com/FreeCAD/FreeCAD/pull/10764), [Pull request #12406](https://github.com/FreeCAD/FreeCAD/pull/12406) and more |
+++


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

### Further Assembly improvements 


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   An [Exploded View](Assembly_CreateView.md) was added. [Pull request #12419](https://github.com/FreeCAD/FreeCAD/issues/12419)
-   Assembly icons were updated and the experimental features exposed. [Pull request #13866](https://github.com/FreeCAD/FreeCAD/pull/13866)
-   Angle, Perpendicular and Parallel joints were added. [Pull request #14008](https://github.com/FreeCAD/FreeCAD/pull/14008)
-   A [Bill of Materials](Assembly_CreateBom.md) feature was added. [Pull request #14198](https://github.com/FreeCAD/FreeCAD/pull/14198)
-   Support for the [TNP](Topological_naming_problem.md) mitigation code was added. [Pull request #14674](https://github.com/FreeCAD/FreeCAD/pull/14674)
-   Flexible sub-assemblies support was added. Sub-assemblies added to a parent assembly can be defined as rigid (a solid unit) or flexible (allow movement of their individual components). Manual steps are required for those sub-assemblies added during the development cycle prior to merging this feature. Those assemblies will need to be removed and re-added to their parent assembly. [Pull request #15629](https://github.com/FreeCAD/FreeCAD/pull/15629)


</div>




<div class="mw-translate-fuzzy">

## Entorno de Trabajo Arch 


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

+++
| <img alt="" src=images/bim_relnotes_1.0.png  style="width:384px;"> | The Arch Workbench has finally been merged with [BIM](BIM_Workbench.md), becoming the new BIM workbench. The new BIM workbench keeps all the tools from Arch, and adds a few more, and brings many refinements to the whole BIM and architectural design workflow, plus better setup and management tools, and better IFC support. [Pull request #13783](https://github.com/FreeCAD/FreeCAD/pull/13783) |
+++


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

### Further BIM improvements 


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   Coming from the BIM workbench, some \"all-in-one\" Arch tools have been split into different use cases: The [Arch BuildingPart](Arch_BuildingPart.md) tool has been split into the [BIM Building](Arch_Building.md) and [BIM Level](Arch_Floor.md) tools, the [Arch Structure](Arch_Structure.md) tool has been split into [BIM Column](BIM_Column.md), [BIM Beam](BIM_Beam.md) and [BIM Slab](BIM_Slab.md), and the [Arch Window](Arch_Window.md) tool has been split into [BIM Window](Arch_Window.md) and [BIM Door](BIM_Door.md). Internally, those tools still produce the same object, only with different IFC types and presets applied. [Pull request #13783](https://github.com/FreeCAD/FreeCAD/pull/13783)
-   [NativeIFC](https://github.com/yorikvanhavre/FreeCAD-NativeIFC) has also been merged into the new BIM workbench. With NativeIFC, you can now work on IFC files in FreeCAD natively, with no more translation to and from the FreeCAD file format. Read more on the [NativeIFC](NativeIFC.md) page. [Pull request #13783](https://github.com/FreeCAD/FreeCAD/pull/13783)
-   The [Arch CutPlane](Arch_CutPlane.md) command has been improved. It is now nesting and link aware and the selection is more flexible. Edges can also be selected making the Arch CutLine command obsolete. [Pull request #11254](https://github.com/FreeCAD/FreeCAD/pull/11254) and [Pull request #11792](https://github.com/FreeCAD/FreeCAD/pull/11792)
-   The BIM preferences have been checked and improved. The pages in the [Preferences Editor](Preferences_Editor.md) have a new layout. [Pull request #11940](https://github.com/FreeCAD/FreeCAD/pull/11940) and [Pull request #12038](https://github.com/FreeCAD/FreeCAD/pull/12038)
-   An *Opening only* preset has been added to the [Arch Window](Arch_Window.md) command. [Pull request #12209](https://github.com/FreeCAD/FreeCAD/pull/12209)
-   The [Arch Roof](Arch_Roof.md) object now has a *Subvolume* property. This allows to use a custom solid object as the subtraction volume for a roof. [Pull request #12346](https://github.com/FreeCAD/FreeCAD/pull/12346)
-   Furthermore for an [Arch Roof](Arch_Roof.md) object that uses a solid object as its *Base* an appropriate subtraction volume is now automatically generated. Just as a wire-based roof, such a roof can be subtracted from the walls of a building with [Arch Remove](Arch_Remove.md). [Pull request #13221](https://github.com/FreeCAD/FreeCAD/pull/13221)
-   The [Arch Reference](Arch_Reference.md) tool has been upgraded: reference objects can now use whole file contents instead of having to choose a part, support for DXF and IFC files has been added. [Pull request #13287](https://github.com/FreeCAD/FreeCAD/pull/13287)
-   FreeCAD now has a new BIM example file. [Pull request #14937](https://github.com/FreeCAD/FreeCAD/pull/14937)
-   The new BIM workbench also offers a series of new management tools, to help you set up your project, or bulk manage IFC properties of your objects. Read more on the [BIM Workbench](BIM_Workbench.md) page.
-   [IfcOpenShell](IfcOpenShell.md), another piece of open-source software needed to work with IFC files in FreeCAD, is now bundled in all official installer packages offered by the FreeCAD team. If you get FreeCAD from a third-party provider, such as your Linux distribution, where IfcOpenShell has not made it yet as an official package, the BIM workbench offers a utility tool to download and install IfcOpenShell. And if you have no use for IFC, the BIM workbench still works 100% without IfcOpenShell.
-   The toolbars and menus of the BIM Workbench were reworked. [Pull request #14087](https://github.com/FreeCAD/FreeCAD/pull/14087)


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

## CAM Workbench 


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   The Path Workbench is now named CAM. [Pull request #12665](https://github.com/FreeCAD/FreeCAD/pull/12665)


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

### Further CAM improvements 


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   Rest machining was reimplemented to take input from the G-code of earlier operations (instead of using the internals of [Area](CAM_Area.md) operations). This enables support for rest machining in Area operations after non-Area ones (most notably Adaptive). [Pull request #11939](https://github.com/FreeCAD/FreeCAD/pull/11939)
-   G43 tool height compensation was added to the centroid CAM post-processor. [Pull request #12652](https://github.com/FreeCAD/FreeCAD/pull/12652)
-   A *Feed retract* option was added to drilling operation settings for reaming and boring. [Pull request #13254](https://github.com/FreeCAD/FreeCAD/pull/13254)
-   A new CAM simulator based on low-level OpenGL functions (faster and more precise) was added. [Pull request #13884](https://github.com/FreeCAD/FreeCAD/pull/13884) and [Pull request #15597](https://github.com/FreeCAD/FreeCAD/pull/15597)
-   The [Vcarve](CAM_Vcarve.md) operation was reworked to include features commonly available in other CAM software (Step down, Finishing pass, Head movement optimization and debugVoronoi method) making it possible to drastically improve the carved surface quality while increasing the carving speed up to 50%. [Pull request #14093](https://github.com/FreeCAD/FreeCAD/pull/14093)
-   Machinability material models were added along with several materials. [Pull request #14460](https://github.com/FreeCAD/FreeCAD/pull/14460), [Pull request #15910](https://github.com/FreeCAD/FreeCAD/pull/15910) and [Pull request #16021](https://github.com/FreeCAD/FreeCAD/pull/16021)


</div>



## Entorno de Trabajo Draft 


<div lang="en" dir="ltr" class="mw-content-ltr">

-   A justification option and several related properties have been added to [Draft ShapeStrings](Draft_ShapeString.md). [Pull request #10233](https://github.com/FreeCAD/FreeCAD/pull/10233)
-   [Radial dimensions](Draft_Dimension#Usage_radial_dimension.md) now only show a single arrow. [Pull request #10655](https://github.com/FreeCAD/FreeCAD/pull/10655)
-   An *Oblique Angle* property has been added to [Draft ShapeStrings](Draft_ShapeString.md). [Pull request #10783](https://github.com/FreeCAD/FreeCAD/pull/10783)
-   Support for hyperlinks has been added. Hyperlinks, to local and remote files and URLs, in [Draft Texts](Draft_Text.md) and [Draft Labels](Draft_Label.md) can be opened from the their [Tree view](Tree_view.md) or [3D view](3D_view.md) context menu. [Pull request #10878](https://github.com/FreeCAD/FreeCAD/pull/10878)
-   The [Draft working plane](Draft_SelectPlane.md) code has been reworked. There is now a working plane per 3D view. [Pull request #11010](https://github.com/FreeCAD/FreeCAD/pull/11010)
-   The history feature and the alignment options of the [Draft SelectPlane](Draft_SelectPlane.md) command have been improved. [Pull request #11062](https://github.com/FreeCAD/FreeCAD/pull/11062)
-   The behavior of the [grid](Draft_ToggleGrid.md) has been improved. Its visibility is now stored per 3D view. When switching to a different workbench all grids are hidden (a [fine-tuning](Fine-tuning.md) parameter is available to disable this). [Pull request #11336](https://github.com/FreeCAD/FreeCAD/pull/11336)
-   The Draft preferences have been checked and improved. Some preferences have been added, obsolete preferences have been removed. The pages in the [Preferences Editor](Preferences_Editor.md) have a new layout and show units where applicable. Restarting FreeCAD after changing a Draft preference is no longer required. [Pull request #11379](https://github.com/FreeCAD/FreeCAD/pull/11379), [Pull request #11503](https://github.com/FreeCAD/FreeCAD/pull/11503), [Pull request #11512](https://github.com/FreeCAD/FreeCAD/pull/11512), [Pull request #11550](https://github.com/FreeCAD/FreeCAD/pull/11550), [Pull request #11579](https://github.com/FreeCAD/FreeCAD/pull/11579), [Pull request #11585](https://github.com/FreeCAD/FreeCAD/pull/11585), [Pull request #11677](https://github.com/FreeCAD/FreeCAD/pull/11677), [Pull request #11694](https://github.com/FreeCAD/FreeCAD/pull/11694) and [Pull request #16603](https://github.com/FreeCAD/FreeCAD/pull/16603)
-   A new *Mouse delay* setting has been added to the General Draft preferences. If it\'s non-zero (default is 1 s), after entering a number in one of the task panel input fields, mouse movement will be disabled, and thus won\'t change the value in the input field, for a given time in seconds. Setting a very large value practically disables mouse movement until the command is finished. [Pull request #12624](https://github.com/FreeCAD/FreeCAD/pull/12624)
-   A button to quickly change the color of the grid has been added to the task panel of the [Draft SelectPlane](Draft_SelectPlane.md) command. [Pull request #13051](https://github.com/FreeCAD/FreeCAD/pull/13051)
-   A *Fuse* property has been added to [Draft PointArrays](Draft_PointArray.md), [Draft PathArrays](Draft_PathArray.md) and Draft PathTwistedArrays. [Pull request #13172](https://github.com/FreeCAD/FreeCAD/pull/13172) and [Pull request #13191](https://github.com/FreeCAD/FreeCAD/pull/13191)
-   The button of the [Toggle grid command](Draft_ToggleGrid.md) now behaves like a toggle button, providing visual feedback of the grid status (visible or hidden). [Pull request #14452](https://github.com/FreeCAD/FreeCAD/pull/14452)


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

### Further Draft improvements 


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   [Draft Facebinders](Draft_Facebinder.md) can now handle faces belonging to links and faces nested in [Std Parts](Std_Part.md). [Pull request #11081](https://github.com/FreeCAD/FreeCAD/pull/11081)
-   Several settings have been added to the [Draft SetStyle](Draft_SetStyle.md) command. [Pull request #11593](https://github.com/FreeCAD/FreeCAD/pull/11593), [Pull request #11694](https://github.com/FreeCAD/FreeCAD/pull/11694) and [Pull request #13914](https://github.com/FreeCAD/FreeCAD/pull/13914)
-   Settings have also been added to the [Draft ApplyStyle](Draft_ApplyStyle.md) command. [Pull request #11610](https://github.com/FreeCAD/FreeCAD/pull/11610) and [Pull request #13914](https://github.com/FreeCAD/FreeCAD/pull/13914)
-   Snap, edit and tracker markers now use the [Marker size](Preferences_Editor#3D_View.md) preference. [Pull request #11688](https://github.com/FreeCAD/FreeCAD/pull/11688) and [Pull request #16603](https://github.com/FreeCAD/FreeCAD/pull/16603)
-   Some Draft icons were changed to improve their appearance. [Pull request #13585](https://github.com/FreeCAD/FreeCAD/pull/13585)
-   The [Draft Layer object](Draft_Layer.md) has been updated for the new material handling system. It now has a *Shape Appearance* property and a *Override Shape Appearance Children* property. [Pull request #13949](https://github.com/FreeCAD/FreeCAD/pull/13949)
-   [Draft Fillets](Draft_Fillet.md) can now also be applied to arcs. [Pull request #14774](https://github.com/FreeCAD/FreeCAD/pull/14774)


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

## FEM Workbench 


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

+++
| <img alt="" src=images/FEM_better_legend_labels_relnotes_1.0.JPG  style="width:384px;"> | The position of the color legend labels was adjusted to make the top ones less likely to be covered by the navigation cube. The default font and color of the labels was changed to increase the visibility and preferences were added to allow label color and size modification. [Pull request #10552](https://github.com/FreeCAD/FreeCAD/pull/10552) |
+++


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

+++
| <img alt="" src=images/FEM_stress_component_linearization_relnotes_1.0.png  style="width:384px;"> | The [FEM PostFilterLinearizedStresses](FEM_PostFilterLinearizedStresses.md) command can now use the stress tensor components for linearized stress computations. Previously, only Von Mises, Tresca and principal (major/intermediate/minor) stresses could be used for this. [Pull request #11724](https://github.com/FreeCAD/FreeCAD/pull/11724) |
+++


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

+++
| <img alt="" src=images/Cyclic_symmetry_relnotes_1.0.jpg  style="width:384px;"> | Support for cyclic symmetry via [tie constraint](FEM_ConstraintTie.md) in CalculiX was added, making it possible to analyze models with rotational periodic symmetry using a single repetitive sector. [Pull request #12289](https://github.com/FreeCAD/FreeCAD/pull/12289) |
+++


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

+++
| <img alt="" src=images/2D_analyses_relnotes_1.0.png  style="width:384px;"> | Support for 2D (plane stress, plane strain and axisymmetric) analyses was added for the [CalculiX solver](FEM_SolverCalculixCxxtools.md). They are configured in the same way as simulations with shell elements but there are some additional restrictions described on the aforementioned wiki page. The new *Model Space* option has to be set properly. [Pull request #12562](https://github.com/FreeCAD/FreeCAD/pull/12562) |
+++


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

+++
| <img alt="" src=images/Hex_subdivision_relnotes_1.0.png  style="width:384px;"> | As the first step towards the support for hexahedral elements, their generation using Gmsh subdivision technique is now possible thanks to the new Gmsh property *Subdivision Algorithm*. It can also be used to create quadrilateral elements. [Pull request #12698](https://github.com/FreeCAD/FreeCAD/pull/12698) |
+++


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

+++
| <img alt="" src=images/Pipeline_colors_relnotes_1.0.png  style="width:384px;"> | New View properties were added to the results pipeline objects. Mesh edge color and width can now be changed for the *Surface with Edges* display mode. Node size can be modified for the *Nodes* mode. There is also a transparency setting for all modes. [Pull request #13066](https://github.com/FreeCAD/FreeCAD/pull/13066) |
+++


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

+++
| <img alt="" src=images/Constraint_suppress_relnotes_1.0.png  style="width:384px;"> | FEM constraints can now be suppressed (right-click on a constraint and select *Suppress*) and thus ignored by the solvers. This way, it\'s possible to modify the analysis setup without having to delete the currently not needed constraints. [Pull request #12359](https://github.com/FreeCAD/FreeCAD/pull/12359) |
+++


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

+++
| <img alt="" src=images/Rigid_body_relnotes_1.0.JPG  style="width:384px;"> | Support for the CalculiX\'s [rigid body constraint](FEM_ConstraintRigidBody.md) was added, finally making it possible to simulate torsion of arbitrary components and apply remote loads, among others. [Pull request #13900](https://github.com/FreeCAD/FreeCAD/pull/13900) |
+++


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

### Further FEM improvements 


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   The *Model → Constraints without solver* menu was removed from the GUI. The listed constraints could not be used. [Pull request #10457](https://github.com/FreeCAD/FreeCAD/pull/10457) and [Pull request #10459](https://github.com/FreeCAD/FreeCAD/pull/10459)
-   The word \"constraint\" was removed from the names and descriptions of most features in the FEM workbench to ensure the correct nomenclature. The names were changed in such a way to fit the standards in the FEA industry and to make them intuitive for new users. [Pull request #10519](https://github.com/FreeCAD/FreeCAD/pull/10519) and [Pull request #10799](https://github.com/FreeCAD/FreeCAD/pull/10799)
-   New icons were added for [Solver CalculiX Standard](FEM_SolverCalculixCxxtools.md), [Solver job control](FEM_SolverControl.md) and [Run solver calculations](FEM_SolverRun.md) for greater intuitiveness. [Pull request #10885](https://github.com/FreeCAD/FreeCAD/pull/10885)
-   Solver CalculiX (new framework) was removed from the GUI since it\'s unfinished and unnecessary at the moment. Its examples were also removed. [Pull request #10823](https://github.com/FreeCAD/FreeCAD/pull/10823) and [Pull request #12876](https://github.com/FreeCAD/FreeCAD/pull/12876)
-   The layout of some postprocessing tool task panels was improved to reduce the size of the horizontal space occupied by them. [Pull request #11066](https://github.com/FreeCAD/FreeCAD/pull/11066)
-   The [FEM ConstraintTemperature](FEM_ConstraintTemperature.md) task panel was reworked to fix issues when editing this feature. [Pull request #11126](https://github.com/FreeCAD/FreeCAD/pull/11126)
-   An old issue with the [FEM PostFilterDataAlongLine](FEM_PostFilterDataAlongLine.md) being able to plot only magnitude, not vector components of a selected output variable was finally fixed. [Pull request #10992](https://github.com/FreeCAD/FreeCAD/pull/10992)
-   The [FEM ConstraintForce](FEM_ConstraintForce.md) and [FEM ConstraintPressure](FEM_ConstraintPressure.md) were overhauled to make them work better on the source code side. [Pull request #10935](https://github.com/FreeCAD/FreeCAD/pull/10935) and [Pull request #10923](https://github.com/FreeCAD/FreeCAD/pull/10923)
-   The [FEM PostFilterDataAtPoint](FEM_PostFilterDataAtPoint.md) now has a PointSize property to set the size of the point symbol for more visibility. [Pull request #11054](https://github.com/FreeCAD/FreeCAD/pull/11054)
-   For clarity, the [FEM mesh region](FEM_MeshRegion.md) command was relabeled to *FEM mesh refinement* in the GUI (the command name remains unchanged). [Pull request #11489](https://github.com/FreeCAD/FreeCAD/pull/11489)
-   The magnitude of gravity acceleration can now be changed using the properties of [FEM ConstraintSelfWeight](FEM_ConstraintSelfWeight.md). [Pull request #12044](https://github.com/FreeCAD/FreeCAD/pull/12044)
-   [Contact](FEM_ConstraintContact.md) and [tie constraint](FEM_ConstraintTie.md) were significantly improved. Contact stiffness now uses the correct unit and stick slope value can be specified for friction in contact. Moreover, clearance adjustment can be specified for contact while tie constraint may have adjustment enabled or disabled. [Pull request #12133](https://github.com/FreeCAD/FreeCAD/pull/12133)
-   PaStiX and Pardiso were added to supported [CalculiX matrix solvers](FEM_SolverCalculixCxxtools#Properties.md). They are the fastest ccx solvers but the possibility of using them depends on the CalculiX binary version and available additional libraries. [Pull request #12478](https://github.com/FreeCAD/FreeCAD/pull/12478)
-   The *Beam Reduced Integration* property (set to *true* by default) was added to [CalculiX solver settings](FEM_SolverCalculixCxxtools.md). It enables a reduced integration scheme for beam elements, making it possible to use the pipe beam section and eliminating accuracy issues in analyses with plasticity, among others. [Pull request #12513](https://github.com/FreeCAD/FreeCAD/pull/12513)
-   The unfinished [Nodes set](FEM_CreateNodesSet.md) tool was removed from the GUI. It couldn\'t be used. [Pull request #12611](https://github.com/FreeCAD/FreeCAD/pull/12611)
-   The Check Mesh CalculiX analysis procedure now generates the results mesh properly. [Pull request #12612](https://github.com/FreeCAD/FreeCAD/pull/12612)
-   It was clarified in the task panel that the diameter used by the pipe beam section is the outer diameter. [Pull request #12609](https://github.com/FreeCAD/FreeCAD/pull/12609)
-   The *Beam Shell Result Output 3D* property of the [CalculiX solver](FEM_SolverCalculixCxxtools.md) is now set to *true* by default to provide results for beam elements and provide meaningful results for shell elements. [Pull request #12493](https://github.com/FreeCAD/FreeCAD/pull/12493)
-   Symbols of analysis features are now properly positioned when the Body (or Part container) has modified placement property. [Pull request #12527](https://github.com/FreeCAD/FreeCAD/pull/12527)
-   [Pressure load](FEM_ConstraintPressure.md) is now working properly for shells regardless of the mesh groups setting. This setting can be changed in the Preferences. [Pull request #12437](https://github.com/FreeCAD/FreeCAD/pull/12437)
-   Simple hardening in [FEM MaterialMechanicalNonlinear](FEM_MaterialMechanicalNonlinear.md) was renamed to isotropic hardening. Moreover, kinematic hardening was added. [Pull request #12666](https://github.com/FreeCAD/FreeCAD/pull/12666)
-   Now geometric nonlinearity is not automatically activated and required when a nonlinear material is used. Those are independent forms of nonlinearity. [Pull request #12703](https://github.com/FreeCAD/FreeCAD/pull/12703)
-   Mixed meshes consisting of both triangular and quadrilateral elements are now displayed properly in the results pipeline. [Pull request #12740](https://github.com/FreeCAD/FreeCAD/pull/12740)
-   The *Output Frequency* property was added to [CalculiX solver settings](FEM_SolverCalculixCxxtools.md). It defines the frequency of output writing in increments. [Pull request #12672](https://github.com/FreeCAD/FreeCAD/pull/12672)
-   Second-order quadrilateral elements can now be generated. Previously, the 2nd order Gmsh setting was generating 1st order quad elements because of the lack of a *SecondOrderIncomplete* Gmsh command which is now used internally. Those elements can also be used for 2D analyses. [Pull request #12698](https://github.com/FreeCAD/FreeCAD/pull/12698) and [Pull request #12774](https://github.com/FreeCAD/FreeCAD/pull/12774)
-   The determination of beam cross-section orientation was partially fixed. Due to a bug in the current release of CalculiX, there may still be issues with some orientations. [Pull request #12833](https://github.com/FreeCAD/FreeCAD/pull/12833)
-   Cantilever FEM examples on the Start page were updated and a new one using 1D elements was added. [Pull request #12871](https://github.com/FreeCAD/FreeCAD/pull/12871)
-   The format in which FreeCAD writes the [force constraint](FEM_ConstraintForce.md) is now compatible with the CalculiX format, eliminating rare issues with too long numbers. [Pull request #12932](https://github.com/FreeCAD/FreeCAD/pull/12932)
-   It is now possible to export the [results pipeline](FEM_PostPipelineFromResult.md) to the VTK format. [Pull request #12987](https://github.com/FreeCAD/FreeCAD/pull/12987)
-   New incrementation control properties were added to [CalculiX solver settings](FEM_SolverCalculixCxxtools.md). Currently, in addition to the initial increment size and time period of the step, one can specify minimum and maximum increment size. Also, the *Iterations Thermo Mech Maximum* property was renamed to *Iterations Maximum* as it can now be used for static (non-thermomechanical) analyses too. [Pull request #12662](https://github.com/FreeCAD/FreeCAD/pull/12662)
-   Default [2D element thickness](FEM_ElementGeometry2D.md) was changed from 20 mm to 1 mm as it makes more sense in practice. [Pull request #13077](https://github.com/FreeCAD/FreeCAD/pull/13077)
-   Many FEM icons were significantly improved to reduce their similarity and make it more clear what the tools do. [Pull request #13130](https://github.com/FreeCAD/FreeCAD/pull/13130)
-   The *Thermo Mech Type* property was added to [CalculiX solver settings](FEM_SolverCalculixCxxtools.md). It makes it possible to switch a regular (coupled) thermomechanical analysis to uncoupled or a pure heat transfer one. [Pull request #13296](https://github.com/FreeCAD/FreeCAD/pull/13296)
-   *Min. Size* property was added for [Netgen mesher](FEM_MeshNetgenFromShape.md) to prevent the generation of too small elements when meshing more complex geometries. [Pull request #12794](https://github.com/FreeCAD/FreeCAD/pull/12794)
-   An old issue with a non-functioning symbol scale property for FEM constraints was finally fixed and the *Scale* property can now be used to adjust the size of symbols of a selected constraint. [Pull request #13274](https://github.com/FreeCAD/FreeCAD/pull/13274)
-   Automatic scaling of FEM constraints was improved to better handle very small and very large objects. [Pull request #13586](https://github.com/FreeCAD/FreeCAD/pull/13586)
-   [Heat flux load](FEM_ConstraintHeatflux.md) now has a radiation heat flux mode to model surface radiation to ambient. [Pull request #13466](https://github.com/FreeCAD/FreeCAD/pull/13466)
-   A few unused constraint symbol View properties were removed. [Pull request #13569](https://github.com/FreeCAD/FreeCAD/pull/13569)
-   New view properties (with the main one being *Color Mode*) were added to FEM mesh objects so that custom color and transparency settings for meshes can be saved and restored. [Pull request #13698](https://github.com/FreeCAD/FreeCAD/pull/13698)
-   Now only the last added filter under each results pipeline object is visible by default. [Pull request #13820](https://github.com/FreeCAD/FreeCAD/pull/13820)
-   The task panel tips of several constraints were changed to actually reflect the rules of the geometry selection for those constraints. [Pull request #13921](https://github.com/FreeCAD/FreeCAD/pull/13921) and [Pull request #14002](https://github.com/FreeCAD/FreeCAD/pull/14002)
-   Support for heat flux results from thermomechanical analyses was added to the results pipeline. [Pull request #14019](https://github.com/FreeCAD/FreeCAD/pull/14019)
-   The [Section print feature](FEM_ConstraintSectionPrint.md) was improved, adding support for heat flux and drag stress (not yet available as 3D fluid analyses with CalculiX haven\'t been implemented yet) results. [Pull request #14046](https://github.com/FreeCAD/FreeCAD/pull/14046)
-   [Body heat source](FEM_ConstraintBodyHeatSource.md) can now be used with CalculiX and has two input modes - dissipation rate \[W/kg\] and total power \[W\]. [Pull request #14417](https://github.com/FreeCAD/FreeCAD/pull/14417)
-   The rotation properties of the [Local coordinate system](FEM_ConstraintTransform.md) were replaced with a single *Rotation* property for consistency. [Pull request #14353](https://github.com/FreeCAD/FreeCAD/pull/14353)
-   An [Erase Elements](FEM_CreateElementsSet.md) tool was added to make it possible to hide elements of a mesh selected with a polygon. [Pull request #11492](https://github.com/FreeCAD/FreeCAD/pull/11492)
-   The three FEM examples on the Start page were replaced with one, containing all three variants of the cantilever beam model (1D, 2D and 3D) in [Group](Std_Group.md) containers. [Pull request #15786](https://github.com/FreeCAD/FreeCAD/pull/15786)
-   The redundant *Fix* properties and checkboxes of the [FEM ConstraintDisplacement](FEM_ConstraintDisplacement.md) were removed. [Pull request #15531](https://github.com/FreeCAD/FreeCAD/pull/15531)
-   The behavior of the Cancel buttons in the task panels of the [Gmsh](FEM_MeshGmshFromShape.md) and [Netgen](FEM_MeshNetgenFromShape.md) meshers was fixed so that they can be used to abort ongoing meshing which is particularly important when an initial guess regarding element size is too low. Moreover, the Netgen mesher was implemented, finally making it possible to use it on all systems, including Linux. [Pull request #16515](https://github.com/FreeCAD/FreeCAD/pull/16515) and [Pull request #16433](https://github.com/FreeCAD/FreeCAD/pull/16433)
-   The *Quasi-structured Quad* 2D algorithm missing in the Gmsh mesher was added to it along with other fixes. [Pull request #15624](https://github.com/FreeCAD/FreeCAD/pull/15624)


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

## Material Workbench 


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

+++
| <img alt="" src=images/Materials_relnotes_1.0.png  style="width:384px;"> | The material handling system, including the editor, has been completely reworked. Further improvements in this regard will follow. [Pull request #10690](https://github.com/FreeCAD/FreeCAD/pull/10690) |
+++


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

+++
| <img alt="" src=images/Appearance_preview_relnotes_1.0.png  style="width:384px;"> | Appearance preview was added to show the materials in the same way they will be shown in documents. [Pull request #11628](https://github.com/FreeCAD/FreeCAD/pull/11628) |
+++


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

+++
| <img alt="" src=images/Material_appearance_relnotes_1.0.jpg  style="width:384px;"> | The new material system is now used for appearance properties. [Pull request #13294](https://github.com/FreeCAD/FreeCAD/pull/13294) |
+++


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

### Further Material improvements 


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   Dialogs to view the Appearance and Material properties of an object were added and available as *Inspect Appearance* and *Inspect Material* tools. [Pull request #13967](https://github.com/FreeCAD/FreeCAD/pull/13967)


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

## Part Workbench 


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

+++
| <img alt="" src=images/Part_scale_relnotes_1.0.png  style="width:384px;"> | [Part Scale](Part_Scale.md) tool was added to allow for easy scaling of shapes without having to use tools from the Draft Workbench. [Pull request #10583](https://github.com/FreeCAD/FreeCAD/pull/10583) |
+++


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

+++
| <img alt="" src=images/Part_Mirror_relnotes_1.0.png  style="width:384px;"> | [Part Mirror](Part_Mirror.md) now supports reference objects, such as a [Part Plane](Part_Plane.md) to define an arbitrary mirror plane in addition to the standard XY, XZ, and YZ planes. [Pull request #11535](https://github.com/FreeCAD/FreeCAD/pull/11535) |
+++


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

### Further Part improvements 


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   The *Frenet* property is now enabled by default for the [Part Sweep](Part_Sweep.md) tool to avoid a common rendering issue. [Pull request #11590](https://github.com/FreeCAD/FreeCAD/pull/11590)
-   A new [attachment mode](Part_EditAttachment#Attachment_modes.md) called *Intersection* was added to the Engine Line. It finds the intersection of two planar faces. [Pull request #12328](https://github.com/FreeCAD/FreeCAD/pull/12328)
-   The [Part ProjectionOnSurface](Part_ProjectionOnSurface.md) tool is parametric now. [Pull request #13158](https://github.com/FreeCAD/FreeCAD/pull/13158)
-   Now all the Part icons use the blue theme and the primitives use the same icon for the toolbar and the tree. [Pull request #14074](https://github.com/FreeCAD/FreeCAD/pull/14074)
-   The [Create sketch](Sketcher_NewSketch.md) command was added to the Part toolbar and menu since operations such as extrusion typically use sketches as input. [Pull request #14318](https://github.com/FreeCAD/FreeCAD/pull/14318)
-   A new [attachment mode](Part_EditAttachment#Attachment_modes.md) called *XY parallel to plane* was added to the Engine Plane and Engine 3D. It results in an attachment similar to *Object\'s XY* but with the XY plane translated to pass through a selected vertex. In contrast to the *Translate origin* attachment mode, it does not move the origin in 2D/Sketcher. It can be used with origin planes, datum planes and sketches, but also with any object with a *Placement* property. [Pull request #14372](https://github.com/FreeCAD/FreeCAD/pull/14372)


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

## PartDesign Workbench 


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

+++
| <img alt="" src=images/Revolve_options_relnotes_1.0.png  style="width:384px;"> | More modes were added to the [revolution](PartDesign_Revolution.md) and [groove](PartDesign_Groove.md) features - to first/last, up to face and two dimensions. [Pull request #7193](https://github.com/FreeCAD/FreeCAD/pull/7193) |
+++


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

+++
| <img alt="" src=images/Pad_task_dialog_relnotes_1.0.png  style="width:384px;"> | [Pad](PartDesign_Pad.md) and [pocket](PartDesign_Pocket.md) task panels were improved (reordered UI elements, **Select face** option hidden when unnecessary and so on). [Pull request #10392](https://github.com/FreeCAD/FreeCAD/pull/10392) |
+++


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

+++
| <img alt="" src=images/Pattern_offset_mode_relnotes_1.0.png  style="width:384px;"> | Offset mode was added for [linear](PartDesign_LinearPattern.md) and [polar pattern](PartDesign_PolarPattern.md). The previous mode was renamed **Overall Length**. [Pull request #10377](https://github.com/FreeCAD/FreeCAD/pull/10377) |
+++


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

+++
| <img alt="" src=images/Single_solid_rule_relnotes_1.0.PNG  style="width:384px;"> | Experimental support for multiple solids within a [Body](PartDesign_Body.md) was added. It can be enabled in the preferences (for new Bodies) or in the properties of an existing Body. [Pull request #13960](https://github.com/FreeCAD/FreeCAD/pull/13960) |
+++


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

+++
| <img alt="" src=images/Pad_up_to_shape_relnotes_1.0.PNG  style="width:384px;"> | *Up to shape* mode was added for Pad and Pocket, making it possible to end them on multiple faces, as opposed to *Up to face* mode which allows the selection of only a single face. [Pull request #11392](https://github.com/FreeCAD/FreeCAD/pull/11392) and [Pull request #14433](https://github.com/FreeCAD/FreeCAD/pull/14433) |
+++


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

### Further PartDesign improvements 


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   The *Make thickness inwards* option is now enabled by default for the [Thickness](PartDesign_Thickness.md) tool. [Pull request #7488](https://github.com/FreeCAD/FreeCAD/pull/7488)
-   Datum points now change color when highlighted or selected (like other datums). [Pull request #12439](https://github.com/FreeCAD/FreeCAD/pull/12439)
-   Part Design icons where slightly improved for consistency. [Pull request #13109](https://github.com/FreeCAD/FreeCAD/pull/13109)
-   A *Suppressed* property was added to temporarily disable a feature. [Pull request #12096](https://github.com/FreeCAD/FreeCAD/pull/12096) and [Pull request #12412](https://github.com/FreeCAD/FreeCAD/pull/12412)
-   The Part Design toolbars have been updated - datums and sketch-based actions are grouped now, [Part CheckGeometry](Part_CheckGeometry.md) was added to the toolbar and menu, and the toolbars were split into individual ones to make it possible to rearrange them. [Pull request #13833](https://github.com/FreeCAD/FreeCAD/pull/13833)
-   Now all the Part Design features use the same icons for the toolbar and the tree. [Pull request #14074](https://github.com/FreeCAD/FreeCAD/pull/14074)
-   A new *Transform body* mode was added to Part Design mirror and pattern tools, making it possible to transform the whole base feature\'s shape instead of the individual tool shapes of additive and subtractive features. [Pull request #12589](https://github.com/FreeCAD/FreeCAD/pull/12589)
-   The layout of the [Hole](PartDesign_Hole.md) tool dialog was improved. [Pull request #14031](https://github.com/FreeCAD/FreeCAD/pull/14031)
-   The [Migrate](PartDesign_Migrate.md) tool was removed from GUI since it was only useful for migrations between versions that are now highly outdated. [Pull request #15196](https://github.com/FreeCAD/FreeCAD/pull/15196)


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

## Sketcher Workbench 


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

+++
| <img alt="" src=images/Arc_helper_relnotes_1.0.png  style="width:384px;"> | Implementation of a circle overlay for arcs (to solve the issue of constraints appearing away from them) was completed with a [command to switch them](Sketcher_ArcOverlay.md). [Pull request #9703](https://github.com/FreeCAD/FreeCAD/pull/9703) |
+++


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

   
  <img alt="" src=images/Contextual_dimension_relnotes_1.0.gif  style="width:384px;">Click on the image if the animation does not start.   A contextual [Dimension](Sketcher_Dimension.md) constraint tool was added to enable quick and intuitive dimensioning with a single versatile tool. [Pull request #9810](https://github.com/FreeCAD/FreeCAD/pull/9810)
   


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

   
  <img alt="" src=images/Tool_parameters_relnotes_1.0.gif  style="width:384px;">Click on the image if the animation does not start.   [Tool parameters](Sketcher_Workbench#On-View-Parameters.md) were added to allow dimensioning on the go (when drawing shapes). Depending on the preference setting On-View-Parameters, they can be disabled, reduced to dimensions only (no initial coordinates) or fully enabled. Moreover, modes were added for the shape tools. They can be selected using the M key or a drop-down list in the task panel. Some tools have additional settings in the form of checkboxes in the task panel and additional keyboard shortcuts. Currently, the new features are available for points, lines, arcs, ellipses, rectangles, polygons, slots and B-splines. [Pull request #11048](https://github.com/FreeCAD/FreeCAD/pull/11048), [Pull request #11174](https://github.com/FreeCAD/FreeCAD/pull/11174) and following
   


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

+++
| <img alt="" src=images/Offset_relnotes_1.0.png  style="width:384px;"> | An [Offset](Sketcher_Offset.md) tool was added to allow offsetting curves. [Pull request #11174](https://github.com/FreeCAD/FreeCAD/pull/11174) |
+++


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

+++
| <img alt="" src=images/Three_point_rectangle_relnotes_1.0.png  style="width:384px;"> | Three-point [rectangle](Sketcher_CompCreateRectangles.md) mode was added in two versions - 3 corners or center and 2 corners. [Pull request #11174](https://github.com/FreeCAD/FreeCAD/pull/11174) |
+++


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

+++
| <img alt="" src=images/Arc_slot_relnotes_1.0.png  style="width:384px;"> | An [Arc slot](Sketcher_CreateArcSlot.md) tool was added with two modes (arc ends and flat ends) to allow for the creation of curved slots [Pull request #11174](https://github.com/FreeCAD/FreeCAD/pull/11174) |
+++


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

   
  <img alt="" src=images/Auto_horizontal-vertical_relnotes_1.0.gif  style="width:384px;">Click on the image if the animation does not start.   A [Horizontal/Vertical constraint](Sketcher_ConstrainHorVer.md) was added. It automatically applies horizontal constraint if a line is closer to horizontal orientation or vertical constraint if it\'s closer to vertical orientation. [Pull request #11538](https://github.com/FreeCAD/FreeCAD/pull/11538)
   


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

+++
| <img alt="" src=images/Angle_radius_rendering_relnotes_1.0.png  style="width:384px;"> | Rendering of angle and radius constraints was improved. Angle constraints have full extension lines now. [Pull request #11507](https://github.com/FreeCAD/FreeCAD/pull/11507) |
+++


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

+++
| <img alt="" src=images/Polar_transform_relnotes_1.0.png  style="width:384px;"> | A [Polar transform](Sketcher_Rotate.md) tool was added to allow rotation and circular patterns of sketcher geometries. [Pull request #11264](https://github.com/FreeCAD/FreeCAD/pull/11264) |
+++


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

   
  <img alt="" src=images/Sketcher_copy-cut-paste_relnotes_1.0.gif  style="width:384px;">Click on the image if the animation does not start.   It is now possible to copy/cut and paste sketch geometry (with constraints) using typical keyboard shortcuts: Ctrl+C, Ctrl+X and Ctrl+V. Not only within a single sketch but also between different sketches or even different instances of FreeCAD. The geometry is copied in the form of Python commands so it can be used in other ways too (e.g. shared on the forum). [Pull request #11537](https://github.com/FreeCAD/FreeCAD/pull/11537)
   


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

+++
| <img alt="" src=images/Scale_transform_relnotes_1.0.png  style="width:384px;"> | A [Scale transform](Sketcher_Scale.md) tool was added, making it possible to scale the geometry in the sketch using a selected center point and a scale factor or two reference points. [Pull request #11265](https://github.com/FreeCAD/FreeCAD/pull/11265) |
+++


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

   
  <img alt="" src=images/B-spline_tangency_relnotes_1.0.gif  style="width:384px;">Click on the image if the animation does not start.   Tangency to B-spline edge was added, eliminating the need to use endpoints and various workarounds instead. [Pull request #11853](https://github.com/FreeCAD/FreeCAD/pull/11853)
   


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

+++
| <img alt="" src=images/Sketcher_translate_relnotes_1.0.png  style="width:384px;"> | The [RectangularArray](Sketcher_RectangularArray.md), [Move](Sketcher_Move.md), [Copy](Sketcher_Copy.md) and [Clone](Sketcher_Clone.md) tools were replaced with a single [Array transform](Sketcher_Translate.md) tool. [Pull request #11267](https://github.com/FreeCAD/FreeCAD/pull/11267) |
+++


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

+++
| <img alt="" src=images/Sketcher_chamfer_relnotes_1.0.png  style="width:384px;"> | A [Chamfer](Sketcher_CreateChamfer.md) tool was added with an option to switch to the [Fillet](Sketcher_CreateFillet.md) mode. Moreover, there is no longer a separate Corner-preserving fillet tool. A *Preserve corner* option (checked by default) has been added to the [Sketcher CreateFillet](Sketcher_CreateFillet.md) tool. [Pull request #12898](https://github.com/FreeCAD/FreeCAD/pull/12898) |
+++


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

   
  <img alt="" src=images/New_symmetry_relnotes_1.0.gif  style="width:384px;">Click on the image if the animation does not start.   The [Symmetry](Sketcher_Symmetry.md) tool has been reworked. Now it works by preselecting the geometry and picking a line or point about which the geometry will be mirrored. A preview is shown and the behavior of the tool can be controlled through tool settings. [Pull request #11853](https://github.com/FreeCAD/FreeCAD/pull/11853)
   


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

   
  <img alt="" src=images/Auto_midpoint_relnotes_1.0.gif  style="width:384px;">Click on the image if the animation does not start.   [Symmetric constraint](Sketcher_ConstrainSymmetric.md) is now applied automatically when the midpoint of a line is picked. [Pull request #13147](https://github.com/FreeCAD/FreeCAD/pull/13147)
   


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

+++
| <img alt="" src=images/Sketcher_arc_length_relnotes_1.0.png  style="width:384px;"> | [Distance dimension constraint](Sketcher_ConstrainDistance.md) can now be used for arc length constraints (circular arc has to be preselected). [Pull request #12602](https://github.com/FreeCAD/FreeCAD/pull/12602) |
+++


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

+++
| <img alt="" src=images/Point_color_relnotes_1.0.png  style="width:384px;"> | The rendering color of points is now different depending on whether it\'s a normal point/endpoint (white, now created by default when using the [CreatePoint](Sketcher_CreatePoint.md) tool), a construction point/center point (blue) or a point coincident with another one (red). [Pull request #13098](https://github.com/FreeCAD/FreeCAD/pull/13098) |
+++


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

   
  <img alt="" src=images/Trim_drag_relnotes_1.0.gif  style="width:384px;">Click on the image if the animation does not start.   The [Trim edge](Sketcher_Trimming.md) tool can now be used in hold and drag mode. [Pull request #13188](https://github.com/FreeCAD/FreeCAD/pull/13188)
   


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

### Further Sketcher improvements 


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   Frame mode was added for the Rectangle tool. [Pull request #11174](https://github.com/FreeCAD/FreeCAD/pull/11174)
-   Two new modes were added for the Line tool: *Point, length, angle* and *Point, width, height*. [Pull request #11174](https://github.com/FreeCAD/FreeCAD/pull/11174)
-   [ToggleConstruction](Sketcher_ToggleConstruction.md) and [ToggleDrivingConstraint](Sketcher_ToggleDrivingConstraint.md) icons were changed. Now the former is not so similar to [CarbonCopy](Sketcher_CarbonCopy.md) and both toggle icons change when clicked. [Pull request #11500](https://github.com/FreeCAD/FreeCAD/pull/11500)
-   Sketcher icons were overhauled to unify their appearance (stroke widths, colors and point sizes). [Pull request #11785](https://github.com/FreeCAD/FreeCAD/pull/11785)
-   A new, optional, [unified Coincident constraint tool](Sketcher_ConstrainCoincidentUnified.md) was introduced. This tool combines the [Coincident](Sketcher_ConstrainCoincident.md) and [PointOnObject](Sketcher_ConstrainPointOnObject.md) constraint tools. [Pull request #11494](https://github.com/FreeCAD/FreeCAD/pull/11494)
-   Rendering of arc-angle, line-angle and arc-distance constraints was improved. [Pull request #12012](https://github.com/FreeCAD/FreeCAD/pull/12012)
-   Edge types can now be customized not only by changing the color but also pattern and size. This allows e.g. dashed construction lines. [Pull request #11996](https://github.com/FreeCAD/FreeCAD/pull/11996)
-   The right-click menu is now contextual and also includes B-spline commands. [Pull request #11884](https://github.com/FreeCAD/FreeCAD/pull/11884) and [Pull request #11973](https://github.com/FreeCAD/FreeCAD/pull/11973)
-   Double-clicking an edge now selects all the geometry connected with it. [Pull request #11925](https://github.com/FreeCAD/FreeCAD/pull/11925)
-   The Sketcher toolbars were slightly reorganized for clarity and consistency. [Pull request #13407](https://github.com/FreeCAD/FreeCAD/pull/13407) and [Pull request #13763](https://github.com/FreeCAD/FreeCAD/pull/13763)
-   The [Carbon copy](Sketcher_CarbonCopy.md) tool icons were improved for better visibility. [Pull request #15074](https://github.com/FreeCAD/FreeCAD/pull/15074)


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

## Spreadsheet Workbench 


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

### Further Spreadsheet improvements 


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   Double-clicking a spreadsheet in the Tree view now switches to this workbench. [Pull request #13137](https://github.com/FreeCAD/FreeCAD/pull/13137)
-   The Spreadsheet icons were improved. [Pull request #13996](https://github.com/FreeCAD/FreeCAD/pull/13996)


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

## TechDraw Workbench 


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

+++
| <img alt="" src=images/TechDraw_cosmetic_circle_relnotes_1.0.png  style="width:250px;"> | The [CosmeticCircle](TechDraw_CosmeticCircle.md) tool was added to allow for the creation of cosmetic circles by selecting the center and inputting the radius. [Pull request #10763](https://github.com/FreeCAD/FreeCAD/pull/10763) |
+++


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

+++
| <img alt="" src=images/Arc_length_relnotes_1.0.png  style="width:250px;"> | The [ArcLengthAnnotation](TechDraw_ExtensionArcLengthAnnotation.md) tool was added to create dimension-like annotations of arc length of selected edges. [Pull request #11532](https://github.com/FreeCAD/FreeCAD/pull/11532) |
+++


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

+++
| <img alt="" src=images/Offset_vertex_relnotes_1.0.png  style="width:250px;"> | The [AddOffsetVertex](TechDraw_CommandAddOffsetVertex.md) tool was added to create cosmetic vertices as offsets from selected vertices. [Pull request #11655](https://github.com/FreeCAD/FreeCAD/pull/11655) |
+++


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

+++
| <img alt="" src=images/Broken_view_relnotes_1.0.png  style="width:250px;"> | The [BrokenView](TechDraw_BrokenView.md) tool was added to depict long objects easily. [Pull request #13331](https://github.com/FreeCAD/FreeCAD/pull/13331) |
+++


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

   
  <img alt="" src=images/Techdraw_smart_dimension_relnotes_1.0.gif  style="width:320px;">Click on the image if the animation does not start.   A new context dimension tool was added based on [the one introduced in the Sketcher](Sketcher_Dimension.md). [Pull request #13525](https://github.com/FreeCAD/FreeCAD/pull/13525)
   


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

### Further TechDraw improvements 


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   Sections based on other sections now use the original (uncut) shape by default. This can be changed in section settings to use the previous section instead. [Pull request #10281](https://github.com/FreeCAD/FreeCAD/pull/10281)
-   Cosmetic objects and centerlines can now be deleted by selecting them and pressing the Delete key. Previously, this resulted in the whole view being deleted. [Pull request #10695](https://github.com/FreeCAD/FreeCAD/pull/10695) and [Pull request #10813](https://github.com/FreeCAD/FreeCAD/pull/10813)
-   A new, more intuitive icon was added for the [WeldSymbol](TechDraw_WeldSymbol.md) tool. [Pull request #10936](https://github.com/FreeCAD/FreeCAD/pull/10936)
-   The behavior of the point + edge mode of the [LengthDimension](TechDraw_LengthDimension.md) was corrected. [Pull request #10860](https://github.com/FreeCAD/FreeCAD/pull/10860)
-   A checked state was added for the [ToggleFrame](TechDraw_ToggleFrame.md) button so that a user can see whether the button is activated or not. [Pull request #11240](https://github.com/FreeCAD/FreeCAD/pull/11240)
-   The behavior of the [DecorateLine](TechDraw_DecorateLine.md) tool was improved. Now double-clicking a line invokes this tool. And line styles are correctly restored if the user presses *Cancel*. Previously, there was no difference between pressing *OK* and *Cancel*. [Pull request #11188](https://github.com/FreeCAD/FreeCAD/pull/11188)
-   Color and transparency of faces can now be set per view. [Pull request #11315](https://github.com/FreeCAD/FreeCAD/pull/11315)
-   Multiselection mode was added and can be enabled in Preferences. In this mode, multiple vertices, edges and faces can be selected by left-clicking on them, without having to keep the Ctrl key pressed. [Pull request #11417](https://github.com/FreeCAD/FreeCAD/pull/11417)
-   [ExtensionAreaAnnotation](TechDraw_ExtensionAreaAnnotation.md) can now calculate areas of arbitrary faces. [Pull request #11473](https://github.com/FreeCAD/FreeCAD/pull/11473)
-   Non-continuous lines will now follow the ISO/ANSI standards instead of a Qt line style. A new preference was added to select the standard. [Pull request #11594](https://github.com/FreeCAD/FreeCAD/pull/11594)
-   The behavior of the [AxoLengthDimension](TechDraw_AxoLengthDimension.md) tool was improved. Now, when dimensioning edges parallel to the global coordinate system axes, the actual (3D) value is calculated automatically and inserted into the Format Spec property (as text). [Pull request #11678](https://github.com/FreeCAD/FreeCAD/pull/11678)
-   The [ExtensionPositionSectionView](TechDraw_ExtensionPositionSectionView.md) tool can now be used by selecting an edge in a section view and a vertex in the source view. [Pull request #11797](https://github.com/FreeCAD/FreeCAD/pull/11797)
-   The [ExtensionInsertRepetition](TechDraw_ExtensionInsertRepetition.md) tool, to insert a repeated feature count, was added. [Pull request #12509](https://github.com/FreeCAD/FreeCAD/pull/12509)
-   Small but important usability improvements were made - double-clicking on the TechDraw page now enters this workbench and the TechDraw MoveView tool was replaced by simple drag and drop in the [tree](Tree_view.md). The TechDraw ClipGroupAdd and TechDraw ClipGroupRemove tools were also replaced by tree drag and drop behavior. [Pull request #13063](https://github.com/FreeCAD/FreeCAD/pull/13063)
-   The drawing templates are now automatically filled with available information (like date and title). [Pull request #13005](https://github.com/FreeCAD/FreeCAD/pull/13005)
-   The [Project shape](TechDraw_ProjectShape.md) tool was removed from TechDraw as it\'s inherited from the old Drawing workbench and has nothing to do with a TechDraw page. [Pull request #13655](https://github.com/FreeCAD/FreeCAD/pull/13655)
-   The [Insert View](TechDraw_View.md) tool was improved so that it can handle more object types and settings. This allowed the following tools to be removed from the toolbar: [SpreadsheetView](TechDraw_SpreadsheetView.md), [ArchView](TechDraw_ArchView.md), [Symbol](TechDraw_Symbol.md), [Image](TechDraw_Image.md) and [ProjectionGroup](TechDraw_ProjectionGroup.md). [Pull request #13219](https://github.com/FreeCAD/FreeCAD/pull/13219)
-   Snapping was added to allow automatic alignment of views and dimensions. Snapping can be temporarily disabled with the Alt key modifier. [Pull request #13659](https://github.com/FreeCAD/FreeCAD/pull/13659)
-   Handling of cosmetics was improved in various ways. [Pull request #14216](https://github.com/FreeCAD/FreeCAD/pull/14216)
-   Many TechDraw icons were improved. [Pull request #14873](https://github.com/FreeCAD/FreeCAD/pull/14873) and following
-   The task panel of the [SurfaceFinishSymbols](TechDraw_SurfaceFinishSymbols.md) tool was significantly improved visually. [Pull request #16147](https://github.com/FreeCAD/FreeCAD/pull/16147)


</div>



---
⏵ [documentation index](../README.md) > [News](Category_News.md) > [Documentation](Category_Documentation.md) > [Releases](Category_Releases.md) > Release notes 1.0/es
