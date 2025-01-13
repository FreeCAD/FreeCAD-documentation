# PartDesign Preferences/en
## Introduction

The <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Part Workbench](Part_Workbench.md) and the <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [PartDesign Workbench](PartDesign_Workbench.md) use the same preferences. They can be found in the [Preferences Editor](Preferences_Editor.md). In the menu select **Edit → Preferences...** and then **<img src="images/Preferences-part_design.svg" width=16px> Part/Part Design**. This group is only available if one of the workbenches has been loaded in the current FreeCAD session.

Some advanced preferences can only be changed in the [Parameter editor](Std_DlgParameter.md). See [Fine-tuning](Fine-tuning#PartDesign_Workbench.md).

This page has been updated for version 1.0.

## Available preferences 

There are three pages: [General](#General.md), [Shape view](#Shape_view.md) and [Shape appearance](#Shape_appearance.md).

### General

<img alt="" src=images/Preferences_PartDesign_Page_General.png  style="width:400px;">

On this page you can specify the following:

+++
| Name                                                                                | Description                                                                                                                                                                                                             |
+=====================================================================================+=========================================================================================================================================================================================================================+
|                                                                      | If checked, the [Boundary representation](https://en.wikipedia.org/wiki/Boundary_representation) (BRep) of the model is [validated](Part_CheckGeometry.md) after [boolean operations](Part_Boolean.md). |
| **Automatically check model after boolean operation**                   |                                                                                                                                                                                                                         |
|                                                                                  |                                                                                                                                                                                                                         |
+++
|                                                                      | If checked, the model is [refined](Part_RefineShape.md) after [boolean operations](Part_Boolean.md).                                                                                                    |
| **Automatically refine model after boolean operation**                  |                                                                                                                                                                                                                         |
|                                                                                  |                                                                                                                                                                                                                         |
+++
|                                                                      | If checked, the model is [refined](Part_RefineShape.md) after changes to source sketches of objects.                                                                                                            |
| **Automatically refine model after sketch-based operation**             |                                                                                                                                                                                                                         |
|                                                                                  |                                                                                                                                                                                                                         |
+++
|                                                                      | If checked, Bodies can have multiple solids. <small>(v1.0)</small>                                                                                                                                               |
| **Allow multiple solids in Part Design Body by default (experimental)** |                                                                                                                                                                                                                         |
|                                                                                  |                                                                                                                                                                                                                         |
+++

### Shape view 

<img alt="" src=images/Preferences_PartDesign_Page_Shape_view.png  style="width:400px;">

On this page you can specify the following:

+++
| Name                                                                  | Description                                                                                                                                                                                                                            |
+=======================================================================+========================================================================================================================================================================================================================================+
|                                                        | The maximum [linear deflection](https://www.opencascade.com/doc/occt-7.3.0/overview/html/occt_user_guides__modeling_algos.html#occt_modalg_11_2) of the [tessellated](#Tessellation.md) objects from their surface.            |
| **Maximum deviation depending on the model bounding box** |                                                                                                                                                                                                                                        |
|                                                                    |                                                                                                                                                                                                                                        |
+++
|                                                        | The maximum [angular deflection](https://www.opencascade.com/doc/occt-7.3.0/overview/html/occt_user_guides__modeling_algos.html#occt_modalg_11_2) from one [tessellated](#Tessellation.md) object section to the next section. |
| **Maximum angular deflection**                            |                                                                                                                                                                                                                                        |
|                                                                    |                                                                                                                                                                                                                                        |
+++

### Shape appearance 

<img alt="" src=images/Preferences_PartDesign_Page_Shape_appearance.png  style="width:400px;">

An explanation of the colors can be found [here](Part_ColorPerFace#Usage.md).

On this page you can specify the following:

+++
| Name                                   | Description                                                                                                                                                                                                          |
+========================================+======================================================================================================================================================================================================================+
|                         | The diffuse color for new shapes. If the option **Random** is set, a random color is used instead.                                                                                         |
| **Shape color**            |                                                                                                                                                                                                                      |
|                                     |                                                                                                                                                                                                                      |
+++
|                         | The ambient color for new shapes. <small>(v1.0)</small>                                                                                                                                                       |
| **Ambient shape color**    |                                                                                                                                                                                                                      |
|                                     |                                                                                                                                                                                                                      |
+++
|                         | The emissive color for new shapes. <small>(v1.0)</small>                                                                                                                                                      |
| **Emissive shape color**   |                                                                                                                                                                                                                      |
|                                     |                                                                                                                                                                                                                      |
+++
|                         | The specular color for new shapes. <small>(v1.0)</small>                                                                                                                                                      |
| **Specular shape color**   |                                                                                                                                                                                                                      |
|                                     |                                                                                                                                                                                                                      |
+++
|                         | The transparency for new shapes. <small>(v0.21)</small>                                                                                                                                                       |
| **Shape transparency**     |                                                                                                                                                                                                                      |
|                                     |                                                                                                                                                                                                                      |
+++
|                         | The shininess for new shapes. <small>(v1.0)</small>                                                                                                                                                           |
| **Shape shininess**        |                                                                                                                                                                                                                      |
|                                     |                                                                                                                                                                                                                      |
+++
|                         | The line color for new shapes.                                                                                                                                                                                       |
| **Line color**             |                                                                                                                                                                                                                      |
|                                     |                                                                                                                                                                                                                      |
+++
|                         | The line thickness for new shapes.                                                                                                                                                                                   |
| **Line width**             |                                                                                                                                                                                                                      |
|                                     |                                                                                                                                                                                                                      |
+++
|                         | The color for new [vertices](Glossary#Vertex.md).                                                                                                                                                            |
| **Vertex color**           |                                                                                                                                                                                                                      |
|                                     |                                                                                                                                                                                                                      |
+++
|                         | The size for new [vertices](Glossary#Vertex.md).                                                                                                                                                             |
| **Vertex size**            |                                                                                                                                                                                                                      |
|                                     |                                                                                                                                                                                                                      |
+++
|                         | The color of [bounding boxes](Property_editor#View.md) in the 3D view.                                                                                                                                       |
| **Bounding box color**     |                                                                                                                                                                                                                      |
|                                     |                                                                                                                                                                                                                      |
+++
|                         | The font size of [bounding boxes](Property_editor#View.md) in the 3D view. <small>(v1.0)</small>                                                                                                      |
| **Bounding box font size** |                                                                                                                                                                                                                      |
|                                     |                                                                                                                                                                                                                      |
+++
|                         | If checked, the color of the interior side of faces will be the same as the exterior side. If not checked either the [backlight color](Preferences_Editor#3D_View.md), if enabled, or black is used instead. |
| **Two-side rendering**     |                                                                                                                                                                                                                      |
|                                     |                                                                                                                                                                                                                      |
+++
|                         | The text color for new document annotations.                                                                                                                                                                         |
| **Text color**             |                                                                                                                                                                                                                      |
|                                     | Currently these annotations can only be added by using the [Python console](Python_console.md):                                                                                                              |
|                                        |                                                                                                                                                                                                                      |
|                                        | obj = App.ActiveDocument.addObject("App::Annotation", "Label")                                                                                                                                                     |
+++

## Tessellation

In order to display an object efficiently its surface is [tessellated](https://en.wikipedia.org/wiki/Tessellation_(computer_graphics)), i.e. it is displayed with some small deviations from its real surface. This applies not only to PartDesign models, but also to other objects in FreeCAD.

There is a lower limit for the tessellation of 0.01%. If you really want to spend the additional time you can reduce the lower limit even further by opening the [Parameter editor](Std_DlgParameter.md).

In the Parameter editor navigate to **BaseApp → Preferences → Mod → Part**, right-click on **MeshDeviation**, and choose **Change value** from the context menu. Set the value to the minimum tessellation of your choice. Please keep in mind that the value is in %, i.e. for a value of 0.005% you have to enter {{Value|0.00005}}. The smallest possible value is {{Value|1e-7}}. Note that in the [Preferences Editor](Preferences_Editor.md) you will still see 0.01% even if you have set a lower value.





{{PartDesign Tools navi

}}



---
⏵ [documentation index](../README.md) > [Preferences](Category_Preferences.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Preferences/en
