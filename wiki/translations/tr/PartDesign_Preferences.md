





{{TOCright}}

## Introduction

The <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [PartDesign Workbench](PartDesign_Workbench.md) and the <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Part Workbench](Part_Workbench.md) use the same preferences. They can be found in the <img alt="" src=images/Preferences-part_design.svg  style="width:24px;"> **Part design** section of the [Preferences editor](Preferences_Editor.md). This section will only be available if one of the workbenches has been loaded in the current FreeCAD session.

## Available preferences {#available_preferences}

There are three tabs: General, Shape view, and Shape appearance.

### General

On the *General* tab you can specify the following:

+-------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Name                                                                    | Description                                                                                                                                                                                                            |
+=========================================================================+========================================================================================================================================================================================================================+
|                                                          | If checked, the [Boundary representation](https://en.wikipedia.org/wiki/Boundary_representation) (BRep) of the model is [validated](Part_CheckGeometry.md) after [boolean operations](Part_Boolean.md) |
| {{MenuCommand|Automatically check model after boolean operation}}       |                                                                                                                                                                                                                        |
|                                                                      |                                                                                                                                                                                                                        |
+-------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                          | If checked, the model is [refined](Part_RefineShape.md) after [boolean operations](Part_Boolean.md)                                                                                                    |
| {{MenuCommand|Automatically refine model after boolean operation}}      |                                                                                                                                                                                                                        |
|                                                                      |                                                                                                                                                                                                                        |
+-------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                          | If checked, the model is [refined](Part_RefineShape.md) after changes to source sketches of objects                                                                                                            |
| {{MenuCommand|Automatically refine model after sketch-based operation}} |                                                                                                                                                                                                                        |
|                                                                      |                                                                                                                                                                                                                        |
+-------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

![](images/Preferences_Part_design_Tab_General.png )

### Shape view {#shape_view}

On the *Shape view* tab you can specify the following:

+-----------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Name                                                                  | Description                                                                                                                                                                                                                     |
+=======================================================================+=================================================================================================================================================================================================================================+
|                                                        | Maximum [linear deflection](https://www.opencascade.com/doc/occt-7.3.0/overview/html/occt_user_guides__modeling_algos.html#occt_modalg_11_2) of the [tesselated](#Tesselation.md) objects from their surface            |
| {{MenuCommand|Maximum deviation depending on the model bounding box}} |                                                                                                                                                                                                                                 |
|                                                                    |                                                                                                                                                                                                                                 |
+-----------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                        | Maximum [angular deflection](https://www.opencascade.com/doc/occt-7.3.0/overview/html/occt_user_guides__modeling_algos.html#occt_modalg_11_2) from one [tesselated](#Tesselation.md) object section to the next section |
| {{MenuCommand|Maximum angular deflection}}                            |                                                                                                                                                                                                                                 |
|                                                                    |                                                                                                                                                                                                                                 |
+-----------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

![](images/Preferences_Part_design_Tab_Shape_view.png )

### Shape appearance {#shape_appearance}

On the *Shape appearance* tab you can specify the following:

+------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Name                               | Description                                                                                                                                                                                                               |
+====================================+===========================================================================================================================================================================================================================+
|                     | Color for new shapes. If the option {{MenuCommand|Random}} is set, a random color is used instead.                                                                                                          |
| {{MenuCommand|Shape color}}        |                                                                                                                                                                                                                           |
|                                 |                                                                                                                                                                                                                           |
+------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                     | Line color for new shapes                                                                                                                                                                                                 |
| {{MenuCommand|Line color}}         |                                                                                                                                                                                                                           |
|                                 |                                                                                                                                                                                                                           |
+------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                     | Line thickness for new shapes                                                                                                                                                                                             |
| {{MenuCommand|Line width}}         |                                                                                                                                                                                                                           |
|                                 |                                                                                                                                                                                                                           |
+------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                     | Color for new [vertices](Glossary#Vertex.md)                                                                                                                                                                      |
| {{MenuCommand|Vertex color}}       |                                                                                                                                                                                                                           |
|                                 |                                                                                                                                                                                                                           |
+------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                     | Size for new [vertices](Glossary#Vertex.md)                                                                                                                                                                       |
| {{MenuCommand|Vertex size}}        |                                                                                                                                                                                                                           |
|                                 |                                                                                                                                                                                                                           |
+------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                     | Color of [bounding boxes](Property_editor#View.md) in the 3D view                                                                                                                                                 |
| {{MenuCommand|Bounding box color}} |                                                                                                                                                                                                                           |
|                                 |                                                                                                                                                                                                                           |
+------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                     | If checked, the color of the interior side of faces will be the same as the exterior side. If not checked either the [backlight color](Preferences_Editor#3D_View.md), if enabled, or black will be used instead. |
| {{MenuCommand|Two-side rendering}} |                                                                                                                                                                                                                           |
|                                 |                                                                                                                                                                                                                           |
+------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                     | Text color for document annotations. There is currently no dialog to add annotations to documents. Annotations can only be added using the Python console with this command:                                              |
| {{MenuCommand|Text color}}         |                                                                                                                                                                                                                           |
|                                 | obj=App.ActiveDocument.addObject("App::Annotation", "Label")                                                                                                                                                            |
|                                    |                                                                                                                                                                                                                           |
|                                    | This console is shown using the menu {{MenuCommand|View → Panels → Python console}}.                                                                                                                        |
+------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

![](images/Preferences_Part_design_Tab_Shape_appearance.png )

## Tesselation

In order to display an object efficiently its surface is [tesselated](https://en.wikipedia.org/wiki/Tessellation_(computer_graphics)), i.e. it is displayed with some small deviations from it real surface. This applies not only to PartDesign models, but also to other objects in FreeCAD.

There is a lower limit for the tesselation of 0.01%. If you really want to spend the additional time you can reduce the lower limit even further by opening the menu {{MenuCommand|Tools → Edit parameters...}} This opens the parameter editor where you navigate to {{MenuCommand|BaseApp → Preferences → Mod → Part}}.

Right click on **Mesh deviation** choose in the context menu **Change value**. Set the value to the minimum tesselation of your choice. Please keep in mind that the value is in %, i.e. for a value of 0.005% you have to enter \"0.00005\". The smallest value possible is 1e-7. **Note:** In the preferences menu you will still see 0.01% even if you set a lower value.





{{PartDesign Tools navi

}} 

[Category:Preferences{{\#translation:}}](Category:Preferences.md)
