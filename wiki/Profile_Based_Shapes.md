# Profile Based Shapes
{{Page_in_progress}}




 



## Temporary section to adjust the content while WIP 

Editor\'s note: There is a mix-up of terms on this page which is confusing. \"Extrusion\" should not be used when discussing swept shapes for example. And \"Prismatic shapes\" and \"Rotated shapes\" should be \"Extruded shapes\" and \"Revolved shapes\" instead.

Author\'s note: It is not to easy to contribute to projects like FreeCAD since the project language Is English and most of us are not native speakers. This leads to strange terms in English that are also hardly translatable into other languages. I\'d like to use technical correct terms rather than terms matching with certain command names.

\- If you just stumbled upon this page and have a solid background on descriptive geometry, please improve the terminology. See Discussion tab of this page. -

-   Extruded parts in the real world are not always rigid and will be forced into shape on assembly. The tools to model these assembled parts depend on the final shape and have different names but they all still represent extruded parts.
-   Sweep shapes, prismatic shapes and rotated shapes are meant in a descriptive geometry sense, but the technical terms might lack precision.
-   I\'m also not happy with the correction of \"invariable\" to \"fixed\" as the latter is has too many other meanings than being invariable (repaired, immobile, static, (problem) solved\...).

Let\' switch to the Discussion tab. 

## Introduction

Apart from a few primitives, modern CAD applications offer two principal ways of creating shapes:

-   **Surface based design**: to design thin walled objects like deep-drawn sheet metal parts where you usually only model the stamp side. The thickness is added in the end when all face elements are in place and connected to create a single surface.
-   **Profile based design**: to design thin walled and solid objects having an fixed cross-section, or thin walled and solid transition objects connecting two or more different profiles.

This page focuses on profile based design, which is one of the principle ways CAD programs use to create 3D shapes. It tries to name and describe several types of shapes, and link to the FreeCAD tools that can be used to create them.

On this page the term **profile** without a suffix is used for an open or closed **2D contour** (line, arc, circle, or polyline).

## Profile based design 

Profiles are usually made of 2D geometry and require additional elements to create 3D shapes.

1.  Another profile (cross-section). The resulting shape will connect the related elements of both profiles. In most cases a copy of the base profile is used and the result has an fixed cross-section.

    :   Some tools accept additional profiles to scale the cross-section or to create a transition between a base profile and different additional profiles.
    :   At some places within FreeCAD (GUI and wiki) section or cross-section is used to distinguish the additional profiles from the base profile.
    :   See [Loft shapes](#Loft_shapes.md) for shapes made of a profile and several cross-sections only.
2.  A control element to position the copy of the base profile in a certain relation to the profile such as:
    -   A vector derived from a 3D line element (axis, edge.) in combination with a length. [Part Extrude](Part_Extrude.md) and [PartDesign Pad](PartDesign_Pad.md) create such vector controlled shapes. See [Prismatic shapes](#Prismatic_shapes.md).

    :   These shapes allow to add a draft to the lateral faces, either through an internal tool option, or an external tool.

    -   An axis to turn the profile around in connection with an angle. [Part Revolve](Part_Revolve.md) and [PartDesign Revolution](PartDesign_Revolution.md) create such rotation controlled shapes. See [Rotated shapes](#Rotated_shapes.md).
    -   A backbone curve (spine) to sweep the profile along [Part Sweep](Part_Sweep.md) and [PartDesign Additive Pipe](PartDesign_AdditivePipe.md) create such spine controlled shapes. See [Sweep shapes](#Sweep_shapes.md).

Filled base profile and end cross-section give a closed shell, sometimes called a volume. Part tools will not create volumes, but will automatically create solid shapes instead.

Open profiles usually result in surface shapes and so they currently cannot be used to create PartDesign features.

### Prismatic shapes 

Prismatic shapes have fixed cross-sections. The profile is distributed along a straight line/vector and we have to decide if we need a surface shape or a solid shape

#### Prismatic surface shapes 

Prismatic surface shapes can be created with <img alt="" src=images/Part_Extrude.svg  style="width:16px;"> [Part Extrude](Part_Extrude.md). The elements of the profile have an influence on the resulting shape:

-   A single straight line results in a planar face.
-   A circle or an arc results in a closed or open cylindric face.
-   A polyline results in a shell, a shape made of connected faces

 <img alt="" src=images/ProfileBased_Example01.png  style="width:300px;"> <img alt="" src=images/ProfileBased_Example02.png  style="width:300px;"> 



*Profiles (green), extrusion vector (yellow), and resulting shapes*

#### Prismatic solid shapes 

Prismatic solid shapes can be created with <img alt="" src=images/Part_Extrude.svg  style="width:16px;"> [Part Extrude](Part_Extrude.md), too if the option **Create solid** is checked, or with <img alt="" src=images/PartDesign_Pad.svg  style="width:16px;"> [PartDesign Pad](PartDesign_Pad.md).

 <img alt="" src=images/ProfileBased_Example03.png  style="width:300px;"> 



*Closed profiles from above and resulting Part shapes with option Create solid enabled*

See [PartDesign Examples](PartDesign_Examples#Prismatic_Primitives.md) for more prismatic solids.

Another tool to to create prismatic solid shapes is provided by the external <img alt="" src=images/Sheetmetal_workbench_icon.svg  style="width:16px;"> [SheetMetal](SheetMetal_Workbench.md) workbench: <img alt="" src=images/SheetMetal_AddBase.svg  style="width:16px;"> [Make Base Wall](SheetMetal_AddBase.md) uses creates planar objects (blanks) from closed contours and unfoldable bent objects from open contours.

 <img alt="" src=images/SheetMetal_AddBase-03.png  style="width:100px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_AddBase-04.png  style="width:100px;"> / <img alt="" src=images/SheetMetal_AddBase-01.png  style="width:100px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_AddBase-02.png  style="width:100px;"> 



*Right: Closed profiles (nested included) result in blanks having a thickness / Left open profiles result in profile objects having a thickness and a length*

### Rotated shapes 

Rotated shapes have fixed cross-sections. The profile is distributed around an axis (which is the same as along a circular line) and we have again to decide if we need a surface shape or a solid shape.

#### Rotatated surface shapes 

Rotatated surface shapes can be created with <img alt="" src=images/Part_Revolve.svg  style="width:16px;"> [Part Revolve](Part_Revolve.md). The elements of the profile have an influence on the resulting shape:

-   A single straight results in a cylindric, a conical, or a planar face.
-   A circle or an arc results in a closed or open section of a torus surface.
-   A polyline results in a rotation shell, a shape made of connected faces of the above types.

 <img alt="" src=images/ProfileBased_Example04.png  style="width:300px;"> <img alt="" src=images/ProfileBased_Example05.png  style="width:300px;"> 



*Profiles (green), rotation axis (yellow), and resulting shapes*

#### Rotatated solid shapes 

Rotatated solid shapes can be created with <img alt="" src=images/Part_Revolve.svg  style="width:16px;"> [Part Revolve](Part_Revolve.md), too if the option **Create solid** is checked, or with <img alt="" src=images/PartDesign_Revolution.svg  style="width:16px;"> [PartDesign Revolution](PartDesign_Revolution.md).

 <img alt="" src=images/ProfileBased_Example06.png  style="width:300px;"> 



*Closed profiles from above and resulting Part shapes with option Create solid enabled → solid*

See [PartDesign Examples](PartDesign_Examples#Circular_Sweep_Objects.md) for rotated solids. (They show profiles distributed along a circular spine, but the resulting shapes are the same as if the profiles were rotated)

### Sweep shapes 

Sweep shapes have fixed cross-sections. The profile is distributed along a spine (a 2D or 3D backbone curve that controlls the location and normal direction of cross-sections) and we have in this case as well to decide if we need a surface shape or a solid shape.

#### Sweep surface shapes 

Sweep surface shapes can be created with <img alt="" src=images/Part_Sweep.svg  style="width:16px;"> [Part Sweep](Part_Sweep.md).

 <img alt="" src=images/ProfileBased_Example07.png  style="width:300px;"> <img alt="" src=images/ProfileBased_Example08.png  style="width:300px;"> 



*Profiles (green), spine (yellow), and resulting shapes)*

#### Sweep solid shapes 

Sweep solid shapes can be created with <img alt="" src=images/Part_Sweep.svg  style="width:16px;"> [Part Sweep](Part_Sweep.md), too if the option **Create solid** is checked, or with <img alt="" src=images/PartDesign_AdditivePipe.svg  style="width:16px;"> [PartDesign AdditivePipe](PartDesign_AdditivePipe.md).

 <img alt="" src=images/ProfileBased_Example09.png  style="width:300px;"> 



*Closed profiles from above and resulting Part shapes with option Create solid enabled*

### Notes on Profiles 

-   Part tools accept several outline objects to be extruded in one operation, but each object is restricted to contain only one contour. Editor\'s note: this only applies to swept shapes.
-   PartDesign tools accept outline objects containing several nested contours as long as the result is a single solid.

### Extrusion objects 

Real world extrusion objects are produced by [extrusion](https://en.wikipedia.org/wiki/Extrusion) i.e. pushing material through a die. The manufacturing condition of such objects is usually modeled using prismatic shapes while sweep shapes are used for their assembled condition. This applies to [rolled](https://en.wikipedia.org/wiki/Rolling_(metalworking)) objects as well.

In relation with CAD to extrude usually means to distribute a profile along a straight line or vector. Even open profiles with no thickness can be extruded, which is impossible in the real world.

 <img alt="" src=images/ProfileBased_Example10.png  style="width:300px;"> 



*An L-shaped rolled and bent frame modelled with <img src="images/Part_Sweep.svg" width=16px> [Part Sweep](Part_Sweep.md), with a mounted sealing profile (a sweep object with a nested contour) made with <img src="images/PartDesign_AdditivePipe.svg" width=16px> [PartDesign AdditivePipe](PartDesign_AdditivePipe.md), both based on the same spline*

Prismatic and rotated shapes can be created with the sweep tools as well if lines and arcs or circles are used as spines. See [PartDesign Examples](PartDesign_Examples#Circular_Sweep_Objects.md).

### Distributing profiles 

What does a CAD application in the background? As stated above, we supply the profile and some kind of spine and the extrusion tools do the uncomfortable work:

-   Creating working planes normal to the spline in each start/end point of spine segments.
-   Copying profiles, i.e. redrawing the profile on a working plane
-   Connecting the related points of profile and cross-section(s) with curves that run parallel to the spine.
-   Filling the faces between a profile segment, a cross-section segment, and two connection lines/curves.
-   Filling faces inside the profile and the last cross-section to close volumes and create solids.

To visualize the steps we use a profile similar to the \"Hamburger Zipfel\" that has taught generations of automotive students how to distribute sealing profiles manually.

 <img alt="" src=images/ProfileBased_Example11.gif  style="width:300px;">  
*Profile (green), spine (yellow), normal planes on start/end points of segments (light blue), cross-sections (light green), connecting curves (grey), and faces (blue) in order of appearance*

FreeCAD\'s sweep tools allow to use profiles that do not lie on planes that are normal to the spine, but they are still controlled by the virtual working planes.This should be avoided as this leads to kinks in the object surfaces:

 <img alt="" src=images/ProfileBased_Example16.png  style="width:300px;">  
*Profile tilted out of the normal plane (purple) and the resulting shape in comparison with the previous example (grey profile and dashed lines); the kinks are clearly visible*

### Notes on spines 

-   Spines alone are not able to control the X direction of the (virtual) working planes and as a consequence the alignment of the cross-sections. Some more conditions apply:
    -   The origin of a (virtual) working plane is on the spine and its normal/Z axis is collinear to the tangent of the spine in this point.
    -   Straight segments keep the direction of X axes parallel (and all normals/Z axes are collinear).
    -   Circular segments keep a constant angle between X axes and the lines connecting origin and arc center.
    -   Arbitrary curve segments work like circular segments in principle but they do not refer to the same (virtual) center point between their limits. Varying center points along the spine may result in unwanted twists of the shape.
-   To control the X direction of the (virtual) working planes independently from internal conditions another curve can be used. <img alt="" src=images/PartDesign_AdditivePipe.svg  style="width:16px;"> [PartDesign AdditivePipe](PartDesign_AdditivePipe.md) has an **Auxiliary** option that uses a guide curve (secondary path) to control the X direction. (Activating the Auxiliary mode opens a \"Profile\" box to add the guide curve)

 <img alt="" src=images/ProfileBased_Example17.png  style="width:300px;"> 



*This example uses a straight spine (yellow) and a guide curve (orange) that is a quarter turn of a helix around the spine to demonstrate the principle how a guide curve twists a profile around the spine*

### Why could extrusions fail? 

A too small radius: If the radius of the spine is too small the cross-sections will intersect resulting in non-manifold geometry, but to a certain degree the sweep tools are able to render a shape anyway:

 <img alt="" src=images/ProfileBased_Example12.png  style="width:300px;"> <img alt="" src=images/ProfileBased_Example13.png  style="width:300px;"> 



*Profile and interesting cross-sections resulting in an impossible shape*

 <img alt="" src=images/ProfileBased_Example14.png  style="width:300px;"> <img alt="" src=images/ProfileBased_Example15.png  style="width:300px;"> 



*View from a different angle and bottom view. If the spine's radius is further decreased so that the yellow face would completely lie inside the shape, the sweep tools can no longer render or update the shape*

### Loft shapes 

Loft shapes connect two or more profiles without a spine so that they in general have varying cross-sections. They are rather used to create a transition shape between profiles. FreeCAD\'s loft tools <img alt="" src=images/Part_Loft.svg  style="width:16px;"> [Part Loft](Part_Loft.md) and <img alt="" src=images/PartDesign_AdditiveLoft.svg  style="width:16px;"> [PartDesign AdditiveLoft](PartDesign_AdditiveLoft.md) use straight lines as connecting curves for two profiles exactly or 3D splines for more than two profiles. To use straight lines with a loft based on more than two profiles we can activate the **Ruled Surface** option.

#### Loft surface shapes 

Loft surface shapes can be created with <img alt="" src=images/Part_Loft.svg  style="width:16px;"> [Part Loft](Part_Loft.md)

#### Loft solid shapes 

Loft solid shapes can be created with <img alt="" src=images/Part_Loft.svg  style="width:16px;"> [Part Loft](Part_Loft.md), too if the **Create solid** option is checked, or with <img alt="" src=images/PartDesign_AdditiveLoft.svg  style="width:16px;"> [PartDesign AdditiveLoft](PartDesign_AdditiveLoft.md).

#### Lofts from identical profiles 

Loft shapes from identical profiles usually don\'t make much sense, but they are included here for a rough comparison with sweep shapes.

 <img alt="" src=images/ProfileBased_Example18.png  style="width:300px;"> <img alt="" src=images/ProfileBased_Example19.png  style="width:300px;"> 



*Profile and cross-sections of the sweep distribution example used as loft profiles (dashed lines erpresent the sweep shape). Right: default settings. Left: Ruled surface option activated*

### Scaled shapes 

### Transition shapes



---
⏵ [documentation index](../README.md) > Profile Based Shapes
