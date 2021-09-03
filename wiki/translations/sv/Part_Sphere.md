---
- GuiCommand:/sv   Name:Part Sphere   Name/sv:Part Sphere   MenuLocation:Part -> Sphere   |Workbenches:[SeeAlso:[[Part_CreatePrimitives/sv|Part_CreatePrimitives](Part_Workbench/sv___Part_Module]],Complete.md)---


</div>

## Description

Creates a simple parametric sphere, with position, angle1, angle2, angle3 and radius parameters.

<img alt="" src=images/SimpleSphere.jpg  style="width:400px;">

## Usage

1.  Switch to the <img alt="" src=images/Workbench_Part.svg  style="width:16px;"> [Part Workbench](Part_Workbench.md)
2.  There are several ways to invoke the command:
    -   Press the **<img src="images/Part_Sphere.svg" width=16px> Sphere** button in the toolbar.
    -   Select the {{MenuCommand|Part → Primitives → <img src="images/Part_Sphere.svg" width=16px> Sphere}} from the menu bar.

**Result:** The sphere will be positioned at origin (point 0,0,0) on creation. The angle parameters permit to make a portion of sphere instead of a full sphere (they are set to 360° by default).

The properties of the object can be edited, either in the [Property editor](Property_editor.md) or by double-clicking the object in the [Tree view](Tree_view.md).

## Properties

### Data


{{TitleProperty|Sphere}}

-    **Radius:**Radius of the sphere

-    **Angle 1:**1nd angle to cut / define the sphere

-    **Angle 2:**2nd angle to cut / define the sphere

-    **Angle 3:**3rd angle to cut / define the sphere

Because it is quite difficult to explain the meaning of the parameters angle 1, angle 2, angle 3, the picture below gives an explanation about these parameters with following values: angle 1 = -45°, angle 2 = 45° and angle 3= 90°.

<img alt="" src=images/SphereCutThreeAngles.jpg  style="width:400px;">





 
