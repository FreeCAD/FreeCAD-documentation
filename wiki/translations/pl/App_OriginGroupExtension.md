# App OriginGroupExtension/pl
## Introduction

An [App Origin](App_OriginGroupExtension.md) object, or formally an `App::OriginGroupExtension`, is a class supplying selectable elements that represent the three standard axes (X, Y, Z) and three standard planes (XY, XZ and YZ) to objects that are intended to arrange different types of geometry in space.

<img alt="" src=images/Std_Part.svg  style="width:16px;"> [Std Part](Std_Part.md) [(App Part)](App_Part.md) objects and <img alt="" src=images/PartDesign_Body.svg  style="width:16px;"> [PartDesign Body](PartDesign_Body.md) objects are created with Origin objects by default. If needed, Origin objects can be added to <img alt="" src=images/Assembly_Assembly_Tree.svg  style="width:16px;"> [Assembly](Assembly3_CreateAssembly.md) objects of the <img alt="" src=images/Assembly3_workbench_icon.svg  style="width:16px;"> [Assembly3](Assembly3_Workbench.md) workbench, too.

<img alt="Tree view" src=images/App_OriginGroupExtension_example.png  style="width:200px;"> <img alt="3D view" src=images/App_OriginGroupExtension-02.png  style="width:400px;"> 
*Left: The [tree view](Tree_view.md) showing three objects that use Origin objects. Right: Representation of the Origin elements in the [3D view](3D_view.md).*

The axes and planes are objects of type `App::Line` and `App::Plane` respectively. Each of these elements can be hidden and unhidden individually with the **Space** bar. This can be useful when selecting the correct reference for creating other objects e.g. [Sketches](Sketch.md).

<img alt="" src=images/FreeCAD_core_objects.svg  style="width:800px;">



*Simplified diagram of the relationships between the core objects in the program. Two of them have an Origin object to control the placement of the objects grouped under them.*


{{Document_objects_navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > App OriginGroupExtension/pl
