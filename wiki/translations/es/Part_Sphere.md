---
- GuiCommand:/es   Name:Part Sphere   Name/es:Part Sphere   MenuLocation:Part -> Sphere   |Workbenches:[SeeAlso:[[Part_CreatePrimitives/es|Part CreatePrimitives](Part_Workbench/es___Part_Module]],Complete.md)---


</div>

## Description


<div class="mw-translate-fuzzy">

Crea una esfera paramétrica simple, con los parámetros de posición, ángulo1, ángulo2, ángulo3 y radio. La esfera se situará en el origen (point 0,0,0). Los parámetros de ángulo permiten crear una porción de la esfera en lugar de la esfera completa (por defecto están establecidos a 360°)


</div>

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





 
