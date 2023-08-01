# PartDesign Preferences/hr
## Introduction

The <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Part Workbench](Part_Workbench.md) and the <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [PartDesign Workbench](PartDesign_Workbench.md) use the same preferences. They can be found in the <img alt="" src=images/Preferences-part_design.svg  style="width:24px;"> **Part/Part design** section of the [Preferences editor](Preferences_Editor.md). This section will only be available if one of the workbenches has been loaded in the current FreeCAD session.

## Available preferences 

There are four tabs: General, Shape view, Shape appearance and Measure.

### General


<div class="mw-translate-fuzzy">

### Prikaz Oblika 


</div>

+++
| Name                                                                    | Description                                                                                                                                                                                                             |
+=========================================================================+=========================================================================================================================================================================================================================+
|                                                          | If checked, the [Boundary representation](https://en.wikipedia.org/wiki/Boundary_representation) (BRep) of the model is [validated](Part_CheckGeometry.md) after [boolean operations](Part_Boolean.md). |
| **Automatically check model after boolean operation**       |                                                                                                                                                                                                                         |
|                                                                      |                                                                                                                                                                                                                         |
+++
|                                                          | If checked, the model is [refined](Part_RefineShape.md) after [boolean operations](Part_Boolean.md).                                                                                                    |
| **Automatically refine model after boolean operation**      |                                                                                                                                                                                                                         |
|                                                                      |                                                                                                                                                                                                                         |
+++
|                                                          | If checked, the model is [refined](Part_RefineShape.md) after changes to source sketches of objects.                                                                                                            |
| **Automatically refine model after sketch-based operation** |                                                                                                                                                                                                                         |
|                                                                      |                                                                                                                                                                                                                         |
+++

![](images/Preferences_Part_design_Tab_General.png )

### Shape view 

On the *Shape view* tab you can specify the following:

+++
| Name                                                                  | Description                                                                                                                                                                                                                        |
+=======================================================================+====================================================================================================================================================================================================================================+
|                                                        | Maximum [linear deflection](https://www.opencascade.com/doc/occt-7.3.0/overview/html/occt_user_guides__modeling_algos.html#occt_modalg_11_2) of the [tessellated](#Tessellation.md) objects from their surface.            |
| **Maximum deviation depending on the model bounding box** |                                                                                                                                                                                                                                    |
|                                                                    |                                                                                                                                                                                                                                    |
+++
|                                                        | Maximum [angular deflection](https://www.opencascade.com/doc/occt-7.3.0/overview/html/occt_user_guides__modeling_algos.html#occt_modalg_11_2) from one [tessellated](#Tessellation.md) object section to the next section. |
| **Maximum angular deflection**                            |                                                                                                                                                                                                                                    |
|                                                                    |                                                                                                                                                                                                                                    |
+++

![](images/Preferences_Part_design_Tab_Shape_view.png )

### Shape appearance 

On the *Shape appearance* tab you can specify the following:

+++
| Name                               | Description                                                                                                                                                                                                               |
+====================================+===========================================================================================================================================================================================================================+
|                     | Color for new shapes. If the option **Random** is set, a random color is used instead.                                                                                                          |
| **Shape color**        |                                                                                                                                                                                                                           |
|                                 |                                                                                                                                                                                                                           |
+++
|                     | Transparency for new shapes <small>(v0.21)</small> .                                                                                                                                                               |
| **Shape transparency** |                                                                                                                                                                                                                           |
|                                 |                                                                                                                                                                                                                           |
+++
|                     | Line color for new shapes.                                                                                                                                                                                                |
| **Line color**         |                                                                                                                                                                                                                           |
|                                 |                                                                                                                                                                                                                           |
+++
|                     | Line thickness for new shapes.                                                                                                                                                                                            |
| **Line width**         |                                                                                                                                                                                                                           |
|                                 |                                                                                                                                                                                                                           |
+++
|                     | Color for new [vertices](Glossary#Vertex.md).                                                                                                                                                                     |
| **Vertex color**       |                                                                                                                                                                                                                           |
|                                 |                                                                                                                                                                                                                           |
+++
|                     | Size for new [vertices](Glossary#Vertex.md).                                                                                                                                                                      |
| **Vertex size**        |                                                                                                                                                                                                                           |
|                                 |                                                                                                                                                                                                                           |
+++
|                     | Color of [bounding boxes](Property_editor#View.md) in the 3D view.                                                                                                                                                |
| **Bounding box color** |                                                                                                                                                                                                                           |
|                                 |                                                                                                                                                                                                                           |
+++
|                     | If checked, the color of the interior side of faces will be the same as the exterior side. If not checked either the [backlight color](Preferences_Editor#3D_View.md), if enabled, or black will be used instead. |
| **Two-side rendering** |                                                                                                                                                                                                                           |
|                                 |                                                                                                                                                                                                                           |
+++
|                     | Text color for document annotations. There is currently no dialog to add annotations to documents. Annotations can only be added using the Python console with this command:                                              |
| **Text color**         |                                                                                                                                                                                                                           |
|                                 | obj = App.ActiveDocument.addObject("App::Annotation", "Label")                                                                                                                                                          |
|                                    |                                                                                                                                                                                                                           |
|                                    | This console is shown using the menu **View → Panels → Python console**.                                                                                                                        |
+++

![](images/Preferences_Part_design_Tab_Shape_appearance.png )

### Measure

These preferences control the appearance of measurements created with the [Measure tools](Part_Workbench#Measure.md) available in the [Part Workbench](Part_Workbench.md) and [PartDesign Workbench](PartDesign_Workbench.md).

On the *Measure* tab (<small>(v0.21)</small> ) you can specify the following:

+++
| Name                                     | Description                                                          |
+==========================================+======================================================================+
|                           | Color for 3D linear dimensions.                                      |
| **3D color**                 |                                                                      |
|                                       |                                                                      |
+++
|                           | Color for delta dimensions (parallel to the global X, Y and Z axes). |
| **Delta color**              |                                                                      |
|                                       |                                                                      |
+++
|                           | Color for angular dimensions.                                        |
| **Angular color**            |                                                                      |
|                                       |                                                                      |
+++
|                           | Font size in pixels.                                                 |
| **Font size**                |                                                                      |
|                                       |                                                                      |
+++
|                           | If checked, font style bold is used.                                 |
| **Bold**                     |                                                                      |
|                                       |                                                                      |
+++
|                           | If checked, font style italic is used.                               |
| **Italic**                   |                                                                      |
|                                       |                                                                      |
+++
|                           | The font to use.                                                     |
| **Font name**                |                                                                      |
|                                       |                                                                      |
+++
|                           | Press this button to update existing measurements.                   |
| **Refresh existing measurements** |                                                                      |
|                                       |                                                                      |
+++

![](images/Preferences_Part_design_Tab_Measure.png )

## Tessellation

In order to display an object efficiently its surface is [tessellated](https://en.wikipedia.org/wiki/Tessellation_(computer_graphics)), i.e. it is displayed with some small deviations from it real surface. This applies not only to PartDesign models, but also to other objects in FreeCAD.

There is a lower limit for the tessellation of 0.01%. If you really want to spend the additional time you can reduce the lower limit even further by opening the menu **Tools → Edit parameters...** This opens the parameter editor where you navigate to **BaseApp → Preferences → Mod → Part**.

Right click on **Mesh deviation** choose in the context menu **Change value**. Set the value to the minimum tessellation of your choice. Please keep in mind that the value is in %, i.e. for a value of 0.005% you have to enter \"0.00005\". The smallest value possible is 1e-7. **Note:** In the preferences menu you will still see 0.01% even if you set a lower value.





{{PartDesign Tools navi

}}



---
⏵ [documentation index](../README.md) > [Preferences](Category_Preferences.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Preferences/hr
