# <img alt="Defeaturing workbench icon" src=images/Defeaturing_workbench_icon.svg  style="width:64px;"> Defeaturing Workbench/en

## Introduction




<img alt="" src=images/Defeaturing_workbench_icon.svg  style="width:24px;"> [Defeaturing Workbench](Defeaturing_Workbench.md) is an add-on workbench intended for editing STEP models, removing of the selected features from the model. It is an [external workbench](External_Workbenches.md) and therefore not part of the standard FreeCAD install.

## Features

-   Features a set of tools to edit a Shape or a STEP model, removing hole(s), face(s), simplifying the model, changing the tolerance, applying Fuzzy Boolean operations etc\...
-   There are also tools to create more solid shape(s), from edge(s), face(s) or shell(s).
-   It is also possible to use direct modeling of the model, when the history of operations is unavailable. (This is the case for 3D STEP models).
-   Useful in situations to quickly remove proprietary details of the model before sharing it. See [Defeaturing](Defeaturing.md)

Note: More advance Defeaturing tools can be used if [OCC7.3](OpenCASCADE.md) is available.

## Installation

### Automatic (recommended) 

Using the FreeCAD <img alt="" src=images/AddonManager.svg  style="width:24px;"> [Addon Manager](Std_AddonMgr.md) available in v0.17+ via **Tools → Addon Manager**. Search for the <img alt="" src=images/Defeaturing_workbench_icon.svg  style="width:24px;"> Defeaturing workbench icon. The Addon Manager also notifies the user when a new version of this Addon is available.

### Manually

See [How to install additional workbenches](How_to_install_additional_workbenches.md)

### Supports

-   FreeCAD v0.15 4671
-   FreeCAD v0.16 \>= 6712
-   FreeCAD v0.17 \>= 13522
-   FreeCAD v0.18+

## References

-   Author: Github: [\@easyw](https://github.com/easyw) \| FreeCAD Forums: [1](https://forum.freecadweb.org/viewtopic.php?f=9&t=29506)
-   Source code on github: <https://github.com/easyw/Defeaturing_WB>
-   FC forum thread <https://forum.freecadweb.org/viewtopic.php?t=29506>

## Tools

![Defeaturing tools dialog](images/Defeaturing_WB.png )

<img alt="" src=images/Defeaturing_Tools.svg  style="width:32px;"> Defeaturing Tools are located in a separate mask.

-   <img alt="" src=images/DefeatWB_Tools_rmv_hole.png  style="width:32px;"> [Remove Holes](DefeatWB_Tools_rmv_hole.md): remove Hole from Face
-   <img alt="" src=images/DefeatWB_Tools_rmv_listed_Faces.png  style="width:32px;"> [Remove listed Faces](DefeatWB_Tools_rmv_listed_Faces.md): remove \'in List\' Faces
-   <img alt="" src=images/DefeatWB_Tools_add_Faces_listed_Edges.png  style="width:32px;"> [Add Faces from \'in List\' Edges](DefeatWB_Tools_add_Faces_listed_Edges.md): add Faces from \'in List\' Edges
-   <img alt="" src=images/DefeatWB_Tools_select_Faces_Param_Defeat.png  style="width:32px;"> [Select Faces to be Parametric defeatured](DefeatWB_Tools_select_Faces_Param_Defeat.md): select Faces to be Parametric defeatured
-   <img alt="" src=images/DefeatWB_Tools_create_copy_listed_edges.png  style="width:32px;"> [Create a copy of the \'in List\' Edges ](DefeatWB_Tools_create_copy_listed_edges.md): create a copy of the \'in List\' Edges

-   <img alt="" src=images/DefeatWB_Tools_copy_Faces_listed_faces.png  style="width:32px;"> [copy Faces from \'in List\' Faces ](DefeatWB_Tools_copy_Faces_listed_faces.md): copy Faces from \'in List\' Faces
-   <img alt="" src=images/DefeatWB_Tools_offset_face.png  style="width:32px;"> [ offset face](DefeatWB_Tools_offset_face.md): offset face
-   <img alt="" src=images/DefeatWB_Tools_offset_edge.png  style="width:32px;"> [offset edge](DefeatWB_Tools_offset_edge.md): offset edge

-   <img alt="" src=images/DefeatWB_Tools_make_solid_listed_faces.png  style="width:32px;"> [Make Solid from in List Faces](DefeatWB_Tools_make_solid_listed_faces.md): make Solid from in List Faces
-   <img alt="" src=images/DefeatWB_Tools_make_solid_faces_selected_objects.png  style="width:32px;"> [Make Solid from the Faces of the selected Objects](DefeatWB_Tools_make_solid_faces_selected_objects.md): make Solid from the Faces of the selected Objects
-   <img alt="" src=images/DefeatWB_Tools_select_one_object_2_make_solid_step_proc.png  style="width:32px;"> [Make Solid from in List Faces](DefeatWB_Tools_select_one_object_2_make_solid_step_proc.md): select ONE object to try to make a Solid through STEP import/export process
-   <img alt="" src=images/DefeatWB_Tools_Connect.png  style="width:32px;"> [Connect](DefeatWB_Tools_Connect.md): connect
-   <img alt="" src=images/DefeatWB_Tools_clean_face_rmv_holes.png  style="width:32px;"> [clean Face(s) removing holes and merging Outwire](DefeatWB_Tools_clean_face_rmv_holes.md): clean Face(s) removing holes and merging Outwire

-   <img alt="" src=images/DefeatWB_Tools_show_listed_edges.png  style="width:32px;"> [show \'in List' Edge(s)](DefeatWB_Tools_show_listed_edges.md): show \'in List' Edge(s)
-   <img alt="" src=images/DefeatWB_Tools_show_listed_faces.png  style="width:32px;"> [show \'in List' Face(s)](DefeatWB_Tools_show_listed_faces.md): show \'in List' Face(s)
-   <img alt="" src=images/DefeatWB_Tools_refine.png  style="width:32px;"> [refine](DefeatWB_Tools_refine.md): refine
-   <img alt="" src=images/DefeatWB_Tools_simple_copy.png  style="width:32px;"> [simple copy](DefeatWB_Tools_simple_copy.md): simple copy
-   <img alt="" src=images/DefeatWB_Tools_parametric_refine.png  style="width:32px;"> [parametric Refine](DefeatWB_Tools_parametric_refine.md): parametric Refine

-   <img alt="" src=images/DefeatWB_Tools_geometry_check.png  style="width:32px;"> [geometry check](DefeatWB_Tools_geometry_check.md): geometry check
-   <img alt="" src=images/DefeatWB_Tools_get_Tolerance_value.png  style="width:32px;"> [get Tolerance value](DefeatWB_Tools_get_Tolerance_value.md): get Tolerance value
-   <img alt="" src=images/DefeatWB_Tools_set_Tolerance_value.png  style="width:32px;"> [set Tolerance value](DefeatWB_Tools_set_Tolerance_value.md): set Tolerance value

-   <img alt="" src=images/DefeatWB_Tools_make_edges_selected_vertexes.png  style="width:32px;"> [make Edge from selected Vertexes](DefeatWB_Tools_make_edges_selected_vertexes.md): make Edge from selected Vertexes
-   <img alt="" src=images/DefeatWB_Tools_reset_placement.png  style="width:32px;"> [reset Placement](DefeatWB_Tools_reset_placement.md): reset Placement
-   <img alt="" src=images/DefeatWB_Tools_show_hide_typeId_shape.png  style="width:32px;"> [show/hide TypeId of the Shape](DefeatWB_Tools_show_hide_typeId_shape.md): show/hide Type Id of the Shape
-   <img alt="" src=images/DefeatWB_Tools_help.png  style="width:32px;"> [help](DefeatWB_Tools_help.md): help

-   <img alt="" src=images/DefeatWB_Tools_Fuzzy_Cut.png  style="width:32px;"> [Fuzzy Cut](DefeatWB_Tools_Fuzzy_Cut.md): Fuzzy Cut
-   <img alt="" src=images/DefeatWB_Tools_Fuzzy_Union.png  style="width:32px;"> [Fuzzy Union](DefeatWB_Tools_Fuzzy_Union.md): Fuzzy Union
-   <img alt="" src=images/DefeatWB_Tools_Fuzzy_Common.png  style="width:32px;"> [Fuzzy Common](DefeatWB_Tools_Fuzzy_Common.md): Fuzzy Common

## Video Tutorials 

### Defeaturing

Removing Features using OCC7.3 new tools

[480px\|left\|thumb \|link=<https://raw.githubusercontent.com/easyw/FreeCAD-tutorials/master/testing-files/removing-holes.mp4%7CDefeaturing-WB>: removing-features (holes)](Image:Defeaturing-WB-@Work_v3.png.md)

[480px\|left\|thumb \|link=<https://youtu.be/yrTtWFakAyE> \|alt=Defeaturing-WB-@Work\|YouTube: Defeaturing tools - Simplifying the model](Image:Defeaturing-WB-@Work_v1.png.md)

[480px\|left\|thumb \|link=<https://youtu.be/vgQwGI6Fk6Q%7CYouTube>: Defeaturing tools - Multi-select faces for defeaturing](Image:Defeaturing-WB-@Work_v2.png.md)

[480px\|left\|thumb \|link=<https://raw.githubusercontent.com/easyw/FreeCAD-tutorials/master/testing-files/removing-fillet-chamfer.mp4%7CDefeaturing-WB> - removing-fillet-chamfer](Image:Defeaturing-WB-@Work_v4.png.md)

[480px\|left\|thumb \|link=<https://peertube.mastodon.host/videos/watch/c6bc5abd-2eb7-48c7-af67-c4d8e6783872%7CDefeaturing-WB> - overview-features (in german language)](Image:Defeaturing-WB-@Work_v5.png.md)

[480px\|left\|thumb \|link=<https://raw.githubusercontent.com/easyw/FreeCAD-tutorials/master/testing-files/parametric-defeaturing.mp4%7CDefeaturing-WB> - parametric-defeaturing](Image:Defeaturing-WB-@Work_v6.png.md) 

### Repairing

-   Sew a Shape
-   Removing or Simplify Faces
-   Remove Holes or Pockets
-   Read or Change Tolerance
-   make Fuzzy Boolean operations

## External workbenches 

FreeCAD workbenches are easy to program in [Python](Python.md), there are therefore many people developing additional workbenches outside of the FreeCAD main developers.

The [external workbenches](external_workbenches.md) page has some information and tutorials on some of them, and the [FreeCAD Addons](https://github.com/FreeCAD/FreeCAD-addons) project aims at gathering them and making them easily installable from within FreeCAD.

New workbenches are in development, stay tuned!



---
⏵ [documentation index](../README.md) > [Addons](Category_Addons.md) > [External Workbenches](Category_External Workbenches.md) > Defeaturing Workbench/en
