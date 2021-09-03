 <img alt="" src=images/User_hub.png  style="width:64px;">

------------------------------------------------------------------------

\_\_NOTOC\_\_


<div class="mw-translate-fuzzy">

Tato část je hlavní nápověda pro nováčky ve FreeCADu.


</div>


<div class="mw-translate-fuzzy">

Mějte prosím na paměti, že stejně jako sám FreeCAD, jsou tyto stránky průběžně ve vývoji. FreeCAD se již teď vyznačuje mnoha zajímavými nástroji pro koncové uživatele a další jsou průběžně přidávány, což je důvodem proč stále ještě chybí finální nebo aktuální dokumentace pro koncového uživatele.


</div>

If you\'d like to contribute to FreeCAD, please [donate](donate.md), and see the [Help FreeCAD](Help_FreeCAD.md) page for other ways to contribute. If you\'d like to edit this wiki, request a wiki account with editor permissions [in the forum](https://forum.freecadweb.org/viewtopic.php?f=21&t=6830), and read the [WikiPages](WikiPages.md) for the general guidelines that you should follow.

If you would like to know how FreeCAD started years ago visit the [History](History.md) page.


<div class="mw-translate-fuzzy">

A máte-li nějaké poznatky, které byste rádi viděli i zde, není důvod abyste nepřispěli a nepomohli nám tento manuál vylepšit. Přejděte na stránku [Nápověda FreeCADu](Help_FreeCAD/cs.md) , která Vám s tím pomůže začít. \_\_NOTOC\_\_

## Použití FreeCADu 


</div>

### Úvod


<div class="mw-translate-fuzzy">

-   [O aplikaci](About_FreeCAD/cs.md): Základní přehled FreeCADu
-   [Instalace](Installing/cs.md): Jak instalovat FreeCAD na [Windows](Install_on_Windows/cs.md), [Unix/Linux](Install_on_Unix/cs.md) a [Mac](Install_on_Mac/cs.md)
-   [Začínáme](Getting_started/cs.md): Rychlý přehled dostupných nástrojů
-   [FAQ](FAQ/cs.md): Často kladené otázky


</div>

See also:

-   [Migrating to FreeCAD from Fusion360](Migrating_to_FreeCAD_from_Fusion360.md)


<div class="mw-translate-fuzzy">

### Základy aplikace 


</div>


<div class="mw-translate-fuzzy">

-   [Model myši](Mouse_Model/cs.md): Použití myši k navigaci ve 3D prostoru
-   [Struktura dokumentu](Document_structure/cs.md): Jak je organizován dokument FreeCADu
-   [Volby](Preferences_Editor/cs.md) a [přizpůsobení](Interface_Customization/cs.md): Jak nakonfigurujete FreeCAD pro Vaše potřeby
-   [Vlastnosti](Property_editor/cs.md): Jak fungují vlastnosti objketů ve FreeCADu
-   [Workbench Concept/cs\|Pracovní plocha](Workbenches.md): Jak je organizováno prostředí FreeCADu
-   [Makra](Macros/cs.md): Jak snadno zautomatizovat často opakované úlohy


</div>


<div class="mw-translate-fuzzy">

### Pracovní plochy 


</div>

[Workbenches](Workbenches.md) are collections of tools used for specific tasks. These are the base workbenches bundled with every FreeCAD installation:

-   <img alt="" src=images/Freecad.svg  style="width:32px;"> [Std Base](Std_Base.md). This is not really a workbench, but rather a category of \'standard\' commands and tools that can be used in all workbenches.

-   <img alt="" src=images/Workbench_Arch.svg  style="width:32px;"> The [Arch Workbench](Arch_Workbench.md) for working with architectural elements.

-   <img alt="" src=images/Workbench_Draft.svg  style="width:32px;"> The [Draft Workbench](Draft_Workbench.md) contains 2D tools and basic 2D and 3D CAD operations.

-   <img alt="" src=images/Workbench_FEM.svg  style="width:32px;"> The [FEM Workbench](FEM_Workbench.md) provides Finite Element Analysis (FEA) workflow.

-   <img alt="" src=images/Workbench_Image.svg  style="width:32px;"> The [Image Workbench](Image_Workbench.md) for working with bitmap images.

-   <img alt="" src=images/Workbench_Inspection.svg  style="width:32px;"> The [Inspection Workbench](Inspection_Workbench.md) is made to give you specific tools for examination of shapes. It is still under development.

-   <img alt="" src=images/Workbench_Mesh.svg  style="width:32px;"> The [Mesh Workbench](Mesh_Workbench.md) for working with triangulated meshes.

-   <img alt="" src=images/Workbench_OpenSCAD.svg  style="width:32px;"> The [OpenSCAD Workbench](OpenSCAD_Workbench.md) for interoperability with OpenSCAD and repairing [constructive solid geometry](constructive_solid_geometry.md) (CSG) model history.

-   <img alt="" src=images/Workbench_Part.svg  style="width:32px;"> The [Part Workbench](Part_Workbench.md) for working with CAD parts.

-   <img alt="" src=images/Workbench_PartDesign.svg  style="width:32px;"> The [Part Design Workbench](PartDesign_Workbench.md) for building Part shapes from sketches.

-   <img alt="" src=images/Workbench_Path.svg  style="width:32px;"> The [Path Workbench](Path_Workbench.md) is used to produce G-Code instructions. It is still under development.

-   <img alt="" src=images/Workbench_Points.svg  style="width:32px;"> The [Points Workbench](Points_Workbench.md) for working with point clouds.

-   <img alt="" src=images/Workbench_Raytracing.svg  style="width:32px;"> The [Raytracing Workbench](Raytracing_Workbench.md) for working with ray-tracing (rendering).

-   <img alt="" src=images/Workbench_Reverse_Engineering.svg  style="width:32px;"> The [Reverse Engineering Workbench](Reverse_Engineering_Workbench.md) is intended to provide specific tools to convert shapes/solids/meshes into parametric FreeCAD-compatible features. It is still under development.

-   <img alt="" src=images/Workbench_Robot.svg  style="width:32px;"> The [Robot Workbench](Robot_Workbench.md) for studying robot movements.

-   <img alt="" src=images/Workbench_Sketcher.svg  style="width:32px;"> The [Sketcher Workbench](Sketcher_Workbench.md) for working with geometry-constrained sketches.

-   <img alt="" src=images/Workbench_Spreadsheet.svg  style="width:32px;"> The [Spreadsheet Workbench](Spreadsheet_Workbench.md) for creating and manipulating spreadsheet data.

-   <img alt="" src=images/Workbench_Start.svg  style="width:32px;"> The [Start Center Workbench](Start_Workbench.md) allows you to quickly jump to one of the most common workbenches.

-   <img alt="" src=images/Workbench_Surface.svg  style="width:32px;"> The [Surface Workbench](Surface_Workbench.md) provides tools to create and modify surfaces. It is similar to the [Part Builder](Part_Builder.md) Face from edges option.

-   <img alt="" src=images/Workbench_TechDraw.svg  style="width:32px;"> The [TechDraw Workbench](TechDraw_Workbench.md) for producing technical drawings from 3D models. It is the successor of the [Drawing Workbench](Drawing_Workbench.md).

-   <img alt="" src=images/Workbench_Test.svg  style="width:32px;"> The [Test Framework Workbench](Testing.md) is for debugging FreeCAD.

-   <img alt="" src=images/Workbench_Web.svg  style="width:32px;"> The [Web Workbench](Web_Workbench.md) provides you with a browser window instead of the [3D view](3D_view.md) within FreeCAD.

### Macros

[Macros](Macros.md) are relatively small snippets of [Python](Python.md) code that perform a simple or a complex task that is not available in the base FreeCAD system.

Power users have written various [macros](macros.md) to enhance FreeCAD with more capabilities.

Since FreeCAD 0.17, many macros can be installed using the [Addon Manager](Std_AddonMgr.md). For a list of the macros refer to the [Macros recipes](Macros_recipes.md) page. For manual installation see [How to install macros](How_to_install_macros.md).

### External workbenches 

When many macros or functions are developed together, and are organized in toolbars and menus, they can become a new workbench.

[External workbenches](External_workbenches.md) are collections of functions that are not part of the base FreeCAD system, usually developed by experienced users, and targeting a particular need.

Since FreeCAD 0.17, many workbenches can be installed using the [Addon Manager](Std_AddonMgr.md). For manual installation see [How to install additional workbenches](How_to_install_additional_workbenches.md).

## Reference


<div class="mw-translate-fuzzy">

-   [Seznam příkazů](List_of_Commands/cs.md): Kompletní seznam dostupných příkazů FreeCADu.


</div>

## Online nápověda 


<div class="mw-translate-fuzzy">


</div>


<div class="mw-translate-fuzzy">

Toto je oficiální online nápověda FreeCADu. Mějte prosím na paměti, že celý systém online nápovědy je v současné době přepracováván. Tento systém nápovědy bude použit pro generování .CHM souboru, který bude distribuován s binárním balíčkem FreeCADu. Právě teď je online nápověda sestavována z některých nejkompletnějších sekcí této wiki.

-   [Systém online nápovědy - Obsah](Online_Help_Toc/cs.md)


</div>

## Dále


<div class="mw-translate-fuzzy">

-   [Rozšířené uživatelské centrum](Power_users_hub/cs.md) je místo kam se můžete podívat na další možnosti využití FreeCADu
-   [Architektonické práce](http://yorik.uncreated.net/guestblog.php?tag=freecad): Příklad jak FreeCAD může začít získávat svou pozici v architektonické práci\...
-   Jestli chcete pomoci FreeCADu, podívejte se na stránku [Nápověda FreeCADu](Help_FreeCAD.md).
-   [FreeCAD Komunitní portál](FreeCAD_Community_Portal.md) zobrazuje seznam projektů vytvořených členy komunity kolem FreCADu.
-   Don\'t understand a term or phrase as used in FreeCAD? Try the [Glossary](Glossary.md) page.


</div>




[Category:Hubs{{\#translation:}}](Category:Hubs.md)
