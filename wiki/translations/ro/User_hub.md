# <img alt="" src=images/User_hub.png  style="width:64px;"> User hub/ro



Aceasta este zona principală de ajutor pentru noii veniți la FreeCAD.


<div class="mw-translate-fuzzy">

Rețineți că, la fel ca FreeCAD în sine, aceste pagini sunt în continuă dezvoltare, motiv pentru care în prezent există încă o documentație lipsă sau învechită .


</div>


<div class="mw-translate-fuzzy">

Dacă doriți să contribuiți la FreeCAD, consultați pagina [ Help FreeCAD](Help_FreeCAD.md). Dacă doriți să editați acest wiki, solicitați un cont wiki cu permisiuni de editor [în forum](https://forum.freecadweb.org/viewtopic.php?f=21&t=6830) și citiți [ WikiPages ](WikiPages.md) pentru regulile generale pe care ar trebui să le urmați.


</div>

Dacă doriți să știți cum a început dezvoltarea FreeCAD cu ani în urmă vizitați pagina [History](History.md) .




<div class="mw-translate-fuzzy">



## Utilizare FreeCAD 


</div>



### Introducere


<div class="mw-translate-fuzzy">

-   [Application Overview](About_FreeCAD.md): O privire generală a FreeCAD
-   [Installing](Installing.md): How to install FreeCAD on [Windows](Install_on_Windows.md), [Linux](Install_on_Linux.md) and [Mac](Install_on_Mac.md)
-   [Installing help files](Installing_Helpfile.md): how to install the offline documentation which is based on this wiki.
-   [Getting started](Getting_started.md): A quick overview of the available tools
-   [FAQ](FAQ.md): Frequently asked questions
-   [Tutorials](Tutorials.md) acoperind diferite părți ale FreeCAD


</div>

#### Migrating from other software? 

-   [Workarounds](Workarounds.md)
-   [Migrating to FreeCAD from Fusion360](Migrating_to_FreeCAD_from_Fusion360.md)
-   [Migrating to FreeCAD from OnShape](Migrating_to_FreeCAD_from_OnShape.md)
-   [Migrating to FreeCAD from SolidWorks](Migrating_to_FreeCAD_from_SolidWorks.md)
-   [Migrating to FreeCAD from Revit](Migrating_to_FreeCAD_from_Revit.md)
-   [FreeCAD BIM migration guide](https://yorik.uncreated.net/blog/2020-010-freecad-bim-guide)
-   [BIM applications compatibility table](BIM_application_compatibility_table.md)




<div class="mw-translate-fuzzy">

### Basic Application 


</div>


<div class="mw-translate-fuzzy">

-   [Mouse Model](Mouse_Model.md): Utilizarea mouse-ului pentru a naviga în spațiul 3D
-   [Document structure](Document_structure.md): How a FreeCAD document is organized
-   [Preferences](Preferences_Editor.md) and [Customization](Interface_Customization.md): How you can configure FreeCAD to your needs
-   [Properties](Property_editor.md): How objects properties work in FreeCAD
-   [Workbench Concept](Workbenches.md): How the FreeCAD interface is organized
-   [Macros](Macros.md): How to easily automate often repeated tasks
-   [File formats](Import_Export.md): Diferitele formate de fișiere pe care FreeCAD le poate citi și scrie


</div>




<div class="mw-translate-fuzzy">

### Ateliere

These are the base workbenches bundled with every installation of FreeCAD:


</div>

[Workbenches](Workbenches.md) are collections of tools used for specific tasks. These are the base workbenches bundled with every FreeCAD installation:

-   <img alt="" src=images/Freecad.svg  style="width:32px;"> [Standard tools](Std_Base.md). These commands and tools are present in all workbenches.

-   <img alt="" src=images/Workbench_Assembly.svg  style="width:32px;"> The [Assembly Workbench](Assembly_Workbench.md) for building and solving mechanical assemblies. <small>(v1.0)</small> 

-   <img alt="" src=images/Workbench_BIM.svg  style="width:32px;"> The [BIM Workbench](BIM_Workbench.md) for working with architectural elements and creating [BIM](https://en.wikipedia.org/wiki/Building_information_modeling) models. It combines the Arch Workbench and the formerly external BIM Workbench available in {{VersionMinus|0.21}}.

-   <img alt="" src=images/Workbench_CAM.svg  style="width:32px;"> The [CAM Workbench](CAM_Workbench.md) is used to produce G-Code instructions. This workbench was called \"Path Workbench\" in {{VersionMinus|0.21}}.

-   <img alt="" src=images/Workbench_Draft.svg  style="width:32px;"> The [Draft Workbench](Draft_Workbench.md) contains 2D tools and basic 2D and 3D CAD operations.

-   <img alt="" src=images/Workbench_FEM.svg  style="width:32px;"> The [FEM Workbench](FEM_Workbench.md) provides Finite Element Analysis (FEA) workflow.

-   <img alt="" src=images/Workbench_Inspection.svg  style="width:32px;"> The [Inspection Workbench](Inspection_Workbench.md) is made to give you specific tools for examination of shapes. Still in the early stages of development.

-   <img alt="" src=images/Workbench_Material.svg  style="width:32px;"> The [Material Workbench](Material_Workbench.md) handles the FreeCAD material system. <small>(v1.0)</small> 

-   <img alt="" src=images/Workbench_Mesh.svg  style="width:32px;"> The [Mesh Workbench](Mesh_Workbench.md) for working with triangulated meshes.

-   <img alt="" src=images/Workbench_OpenSCAD.svg  style="width:32px;"> The [OpenSCAD Workbench](OpenSCAD_Workbench.md) for interoperability with OpenSCAD and repairing [constructive solid geometry](Constructive_solid_geometry.md) (CSG) model history.

-   <img alt="" src=images/Workbench_Part.svg  style="width:32px;"> The [Part Workbench](Part_Workbench.md) for working with geometric primitives and boolean operations.

-   <img alt="" src=images/Workbench_PartDesign.svg  style="width:32px;"> The [Part Design Workbench](PartDesign_Workbench.md) for building Part shapes from sketches.

-   <img alt="" src=images/Workbench_Points.svg  style="width:32px;"> The [Points Workbench](Points_Workbench.md) for working with point clouds.

-   <img alt="" src=images/Workbench_Reverse_Engineering.svg  style="width:32px;"> The [Reverse Engineering Workbench](Reverse_Engineering_Workbench.md) is intended to provide specific tools to convert shapes/solids/meshes into parametric FreeCAD-compatible features.

-   <img alt="" src=images/Workbench_Robot.svg  style="width:32px;"> The [Robot Workbench](Robot_Workbench.md) for studying robot movements. Currently unmaintained.

-   <img alt="" src=images/Workbench_Sketcher.svg  style="width:32px;"> The [Sketcher Workbench](Sketcher_Workbench.md) for working with geometry-constrained sketches.

-   <img alt="" src=images/Workbench_Spreadsheet.svg  style="width:32px;"> The [Spreadsheet Workbench](Spreadsheet_Workbench.md) for creating and manipulating spreadsheet data.

-   <img alt="" src=images/Workbench_Surface.svg  style="width:32px;"> The [Surface Workbench](Surface_Workbench.md) provides tools to create and modify surfaces. It is similar to the [Part Builder](Part_Builder.md) Face from edges option.

-   <img alt="" src=images/Workbench_TechDraw.svg  style="width:32px;"> The [TechDraw Workbench](TechDraw_Workbench.md) for producing technical drawings from 3D models.

-   <img alt="" src=images/Workbench_Test.svg  style="width:32px;"> The [Test Framework Workbench](Testing.md) is for debugging FreeCAD.




<div class="mw-translate-fuzzy">

### Macrocomenzi

Power users have written various macros to enhance FreeCAD with more capabilities. For a list of the macros refer to the [macros recipes](macros_recipes.md) page. For instructions how to install the macros refer to the [How to install macros](How_to_install_macros.md) tutorial.


</div>

[Macros](Macros.md) are relatively small snippets of [Python](Python.md) code that perform a simple or a complex task that is not available in the base FreeCAD system.

Power users have written various [macros](macros.md) to enhance FreeCAD with more capabilities.

Since FreeCAD 0.17, many macros can be installed using the [Addon Manager](Std_AddonMgr.md). For a list of the macros refer to the [Macros recipes](Macros_recipes.md) page. For manual installation see [How to install macros](How_to_install_macros.md).




<div class="mw-translate-fuzzy">

### Ateliere Externes 

Utilizatorii cu experiență au extins FreeCAD cu diverse ateliere de lucru externe personalizate, care nu sunt integrate în codul sursă FreeCAD, dar sunt ușor de instalat pe o instalare FreeCAD deja existentă. [See here](External_workbenches.md) pentru o prezentare generală a bancilor de lucru disponibile deja.Pentru instrucțiuni despre instalarea acestor ateliere de lucru, consultați tutorialul[How to install additional workbenches](How_to_install_additional_workbenches.md).


</div>

When many macros or functions are developed together, and are organized in toolbars and menus, they can become a new workbench.

[External workbenches](External_workbenches.md) are collections of functions that are not part of the base FreeCAD system, usually developed by experienced users, and targeting a particular need.

Since FreeCAD 0.17, many workbenches can be installed using the [Addon Manager](Std_AddonMgr.md). For manual installation see [How to install additional workbenches](How_to_install_additional_workbenches.md).



## Referințe


<div class="mw-translate-fuzzy">

-   [Commands Reference](List_of_Commands.md): A complete list of the available FreeCAD commands.


</div>

## Online Help 


<div class="mw-translate-fuzzy">

Acesta este ajutorul online oficial al FreeCAD. Rețineți că întregul sistem de ajutor online se află în prezent în procesare. Acesta va fi folosit pentru a genera un fișier .CHM, care va fi distribuit cu pachetele binare ale FreeCAD. În momentul în care ajutorul online sintetizează unele dintre cele mai complete secțiuni ale acestui wiki.

-   [ Online help system - Table of Contents](Online_Help_Toc.md)


</div>



## Suplimentar


<div class="mw-translate-fuzzy">

-   The [Power users hub](Power_users_hub.md) is the place to go if you would like to see more advanced use of FreeCAD
-   The [FreeCAD Community Portal](FreeCAD_Community_Portal.md) lists projects made by community members around FreeCAD.
-   Don\'t understand a term or phrase as used in FreeCAD? Try the [Glossary](Glossary.md) page.


</div>



---
⏵ [documentation index](../README.md) > [Hubs](Category_Hubs.md) > User hub/ro
