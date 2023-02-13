# Getting started/sv
{{TOCright}}



## Förord


<div class="mw-translate-fuzzy">

FreeCAD är en CAD/CAE parametrisk modelleringsapplikation. Den är fortfarande i ett tidigt utvecklingsstadium, så förvänta dig inte att du ska kunna använda den till professionellt arbete än.


</div>


<div class="mw-translate-fuzzy">

Men, om du är nyfiken på hur FreeCAD ser ut och vilka funktioner som håller på att utvecklas, så är du välkommen att ladda ned den och testa den. För tillfället finns det redan många funktioner, men gränssnittet för många av dem har ännu inte skapats. detta innebär att om du kan lite om python, så kommer du redan att kunna producera och förändra komplex geometri relativt enkelt. Om inte, så kommer du förmodligen att upptäcka att FreeCAD fortfarande har en del att erbjuda dig. Men, ha tålamod, detta kommer att förändras snart.


</div>


<div class="mw-translate-fuzzy">

Och om du efter att ha testat den har kommentarer, ideer eller åsikter, var vänlig att dela dem med oss på [FreeCAD diskussionsforum](http://forum.freecadweb.org/index.php)!


</div>

See also:

-   [Migrating to FreeCAD from Fusion360](Migrating_to_FreeCAD_from_Fusion360.md)
-   [Which workbench should I choose?](Which_workbench_should_I_choose.md)
-   [Tutorials](Tutorials.md)
-   [Video tutorials](Video_tutorials.md)



## Installation


<div class="mw-translate-fuzzy">

Först av allt (om det inte redan är gjort), ladda ned och installera FreeCAD. Se [Nedladdningssidan](Download/sv.md) för information om nuvarande versioner och updateringar. Det finns färdiga installationspaket för Windows (.msi), Ubuntu & Debian (.deb) openSUSE (.rpm) och Mac OSX.


</div>




<div class="mw-translate-fuzzy">

## Utforska FreeCAD 


</div>

<img alt="" src=images/FreeCAD_interface_base_divisions.svg  style="width:1024px;">


<div class="mw-translate-fuzzy">

![ FreeCAD gränssnittet när du startar den första gången. Se fler [skärmdumpar](images/Screenshots/sv.md) här.](Freecad09-empty.jpg )

FreeCAD är en allmän, allt-i-allo 3D modelleringsapplikation, fokuserad på mekanisk konstruktion och relaterade områden, som andra konstruktionsspecialiteter eller arkitektur. Den är utformad som en plattform för utveckling av vilken 3D applikation som helst, men även för att göra väldigt specifika uppgifter. För det ändamålet så är dess gränssnitt uppdelat i en serie med [Arbetsbänkar](Workbenches/sv.md). Arbetsbänkar gör att du ändrar gränssnittsinnehållet till att endast visa de verktyg som är nödvändiga för en specifik uppgift, uppgiftsgrupper.

FreeCAD gränssnittet kan därför beskrivas som en mycket enkel behållare, med en menyrad, en 3D visningsområde, och några sidopaneler för att visa sceninnehållet eller objektegenskaper. Allt innehåll i dessa paneler kan förändras beroende på arbetsbänken.

När du startar FreeCAD för den första gången, så kommer en \"generell\" arbetsbänk att presenteras för dig, som vi kallar \"komplett arbetsbänk\". Denna arbetsbänk samlar de mognaste verktygen från andra arbetsbänkar. Eftersom FreeCAD är ganska ungt och inte har använts för något specialiserat arbete ännu, så är denna arbetsbänk väldigt smidig för att utforska FreeCAD lättare. Alla verktyg som är tillräckligt bra för att producera geometri finns här.


</div>


**See a full explanation in [Interface](Interface.md).**


:   1\. The [main view area](main_view_area.md), which can contain different tabbed windows, principally the [3D view](3D_view.md).
:   2\. The [3D view](3D_view.md), showing the geometrical objects in the document.
:   3\. The [tree view](tree_view.md) (part of the [combo view](combo_view.md)), showing the hierarchy and construction history of objects in the document; it can also display the [task panel](task_panel.md) for active commands.
:   4\. The [property editor](property_editor.md) (part of the [combo view](combo_view.md)), which allows viewing and modifying properties of the selected objects.
:   5\. The [selection view](selection_view.md), which indicates the objects or sub-elements of objects (vertices, edges, faces) that are selected.
:   6\. The [report view](report_view.md) (or output window), where messages, warnings and errors are shown.
:   7\. The [Python console](Python_console.md), where all the commands executed are printed, and where you can enter [Python](Python.md) code.
:   8\. The [status bar](status_bar.md), where some messages and tooltips appear.
:   9\. The toolbar area, where the toolbars are docked.
:   10\. The [workbench selector](Std_Workbench.md), where you select the active [workbench](workbenches.md).
:   11\. The [standard menu](Standard_Menu.md), which holds basic operations of the program.

The main concept behind the FreeCAD interface is that it is separated into [workbenches](workbenches.md). A workbench is a collection of tools suited for a specific task, such as working with [meshes](Mesh_Workbench.md), or drawing [2D objects](Draft_Workbench.md), or [constrained sketches](Sketcher_Workbench.md). You can switch the current workbench with the [workbench selector](Std_Workbench.md). You can [customize](Interface_Customization.md) the tools included in each workbench, add tools from other workbenches or even self-created tools, that we call [macros](macros.md). Widely used starting points are the [PartDesign Workbench](PartDesign_Workbench.md) and [Part Workbench](Part_Workbench.md).

When you start FreeCAD for the first time, you are presented with the Start page. Here is what it looks like for version 0.19:

<img alt="" src=images/Start_center_0.19_screenshot.png  style="width:600px;">

The Start page allows you to quickly jump to one of the most common workbenches, open one of the recent files, or see the latest news from the FreeCAD world. You can change the default workbench in the [preferences](Preferences_Editor.md).



### Navigera i 3D rymden 

FreeCAD har två olika [navigationslägen](Mouse_Model/sv.md) tillgängliga, som kan ställas in i inställningsdialogen. I standardläget, så utförs **zoomning** med **Mushjulet**, **panorering** med **Mittre musknappen**, och **rotation** med **vänster musknapp** och **Mittre musknappen** samtidigt. Val av ett objekt görs genom att klicka på det med **vänster musknapp**, med **CTRL** nedtryckt om du vill välja flera objekt.

Du har också flera förinställda vyer (Toppvy, Frontvy, etc) tillgängliga i Visa menyn och på verktygslådan Visa, och via numeriska genvägar (**1**, **2**, etc\...)

## [Skript](Scripting/sv.md)

Och slutligen, en av de kraftfullaste funktionerna i FreeCAD är [skript](Scripting/sv.md) miljön. Från den integrerade pythonkonsolen (eller från något externt pythonskript), så får du åtkomst till nästan vilken del som helst av FreeCAD, skapa eller ändra geometri, ändra representationen av dessa objekt i 3D scenen eller förändra FreeCAD\'s gränssnitt. Python skript kan även användas i [makron](Macros/sv.md), vilket erbjuder en lätt metod att skapa anpassade kommandon.

FreeCAD has several [navigation modes](Mouse_navigation.md) available, that change the way you use your mouse to interact with the objects in the 3D view and the view itself. One of them is specifically made for [touchpads](Mouse_navigation#Touchpad_navigation.md), where the middle mouse button is not used. The default navigation mode is [CAD navigation](Mouse_navigation#CAD_navigation.md). You can quickly change the current navigation mode by using the **[<img src=images/NavigationCAD_dark.svg style="width:16px">** button in the [Status bar](Status_bar.md) or by right-clicking an empty area of the [3D view](3D_view.md).

You also have several view presets (top view, front view, etc) available in the View menu, on the View toolbar, and by numeric shortcuts (**1**, **2**, etc\...). By right-clicking on an object or on an empty area of the 3D view, you have quick access to some common operations, such as setting a particular view, or locating an object in the Tree view.

## First steps with FreeCAD 

FreeCAD\'s focus is to allow you to make high-precision 3D models, to keep tight control over those models (being able to go back into modelling history and change parameters), and eventually to build those models (via 3D printing, CNC machining or even construction worksite). It is therefore very different from some other 3D applications made for other purposes, such as animation film or gaming. Its learning curve can be steep, especially if this is your first contact with 3D modeling. If you are struck at some point, don\'t forget that the friendly community of users on the [FreeCAD forum](http://forum.freecadweb.org/index.php) might be able to get you out in no time.

The workbench you will start using in FreeCAD depends on the type of job you need to do: If you are going to work on mechanical models, or more generally any small-scale objects, you\'ll probably want to try the [PartDesign Workbench](PartDesign_Workbench.md). If you will work in 2D, then switch to the [Draft Workbench](Draft_Workbench.md), or the [Sketcher Workbench](Sketcher_Workbench.md) if you need constraints. If you want to do BIM, launch the [Arch Workbench](Arch_Workbench.md). And if you come from the OpenSCAD world, try the [OpenSCAD Workbench](OpenSCAD_Workbench.md). There are also many community-developed [external workbenches](External_workbenches.md) available.

You can switch workbenches at any time, and also [customize](Interface_Customization.md) your favorite workbench to add tools from other workbenches.

## Working with the PartDesign and Sketcher workbenches 

The [PartDesign Workbench](PartDesign_Workbench.md) is made to build complex objects, starting from simple shapes, and adding or removing pieces (called \"features\"), until you get to your final object. All the features you applied during the modelling process are stored in a separate view called the [tree view](Document_structure.md), which also contains the other objects in your document. You can think of a PartDesign object as a succession of operations, each one applied to the result of the preceding one, forming one big chain. In the tree view, you see your final object, but you can expand it and retrieve all preceding states, and change any of their parameter, which automatically updates the final object.

The PartDesign workbench makes heavy use of another workbench, the [Sketcher Workbench](Sketcher_Workbench.md). The sketcher allows you to draw 2D shapes, which are defined by applying Constraints to the 2D shape. For example, you might draw a rectangle and set the size of a side by applying a length constraint to one of the sides. That side then cannot be resized anymore (unless the constraint is changed).

Those 2D shapes made with the sketcher are used a lot in the PartDesign workbench, for example to create 3D volumes, or to draw areas on the faces of your object that will then be hollowed from its main volume. This is a typical PartDesign workflow:

1.  Create a new sketch
2.  Draw a closed shape (make sure all points are joined)
3.  Close the sketch
4.  Expand the sketch into a 3D solid by using the pad tool
5.  Select one face of the solid
6.  Create a second sketch (this time it will be drawn on the selected face)
7.  Draw a closed shape
8.  Close the sketch
9.  Create a pocket from the second sketch, on the first object

Which gives you an object like this:

<img alt="" src=images/Partdesign_example.jpg  style="width:600px;">

At any moment, you can select the original sketches and modify them, or change the extrusion parameters of the pad or pocket operations, which will update the final object.

## Working with the Draft and Arch workbenches 

The [Draft Workbench](Draft_Workbench.md) and [Arch Workbench](Arch_Workbench.md) behave a bit differently than the other workbenches above, although they follow the same rules, which are common to all of FreeCAD. In short, while the Sketcher and PartDesign are made primarily to design single pieces, Draft and Arch are made to ease your work when working with several, simpler objects.

The [Draft Workbench](Draft_Workbench.md) offers you 2D tools somewhat similar to what you can find in traditional 2D CAD applications such as [AutoCAD](https://en.wikipedia.org/wiki/AutoCAD). However, 2D drafting being far away from the scope of FreeCAD, don\'t expect to find there the full array of tools that these dedicated applications offer. Most of the Draft tools work not only in a 2D plane but also in the full 3D space, and benefit from special helper systems such as [Work planes](Draft_SelectPlane.md) and [object snapping](Draft_Snap.md).

The [Arch Workbench](Arch_Workbench.md) adds [BIM](http://en.wikipedia.org/wiki/Building_Information_Modeling) tools to FreeCAD, allowing you to build architectural models with parametric objects. The Arch workbench relies extensively on other modules such as Draft and Sketcher. All the Draft tools are also present in the Arch workbench, and most Arch tools make use of the Draft helper systems.

A typical workflow with Arch and Draft workbenches might be:

1.  Draw a couple of lines with the Draft Line tool
2.  Select each line and press the Wall tool to build a wall on each of them
3.  Join the walls by selecting them and pressing the Arch Add tool
4.  Create a floor object, and move your walls in it from the Tree view
5.  Create a building object, and move your floor in it from the Tree view
6.  Create a window by clicking the Window tool, select a preset in its panel, then click on a face of a wall
7.  Add dimensions by first setting the working plane if necessary, then using the Draft Dimension tool

Which will give you this:

<img alt="" src=images/Arch_workflow_example.jpg  style="width:600px;">

More on the [Tutorials](Tutorials.md) page.

## Addons, Macro and External workbenches 

FreeCAD, as an open source software, offers the possibility to supplement its workbenches with addons.

The [Addon](Addon.md) principle is based on the development of a workbench complement. Any user can develop a function that he or she deems to be missing for her/his own needs or, ultimately, for the community. With the forum, the user can request an opinion, help on the forum. It can share, or not, the object of its development according to copyright rules to define. Free to her/him. To develop, the user has available [scripting](scripting.md) functions.

There are two types of addons:

1.  [Macros](Macros.md): short snippets of Python code that provide a new tool or functionality. Macros usually start as a way to simplify or automate the task of drawing or editing a particular object. If many of these macros are collected inside a directory, the entire directory may be distributed as a new workbench.
2.  [External workbenches](External_workbenches.md): collections of tools programmed in Python or C++ that extend FreeCAD in an important way. If a workbench is sufficiently developed and is well documented, it may be included as one of the base workbenches in FreeCAD. Under [External workbenches](External_workbenches.md), you\'ll find the principle and a list of existing library.

## Scripting

And finally, one of the most powerful features of FreeCAD is the [scripting](scripting.md) environment. From the integrated python console (or from any other external Python script), you can gain access to almost any part of FreeCAD, create or modify geometry, modify the representation of those objects in the 3D scene or access and modify the FreeCAD interface. Python scripting can also be used in [macros](macros.md), which provide an easy method to create custom commands.

## What\'s new 

-   See the [release notes](Feature_list#Release_notes.md) for the detailed list of features.


<div class="mw-translate-fuzzy">


{{docnav/sv|Install on Mac/sv|Mouse Model/sv}}


</div>



---
![](images/Right_arrow.png) [documentation index](../README.md) > Getting started/sv
