# TechDraw Section Examples
## Introduction

The <img alt="" src=images/Workbench_TechDraw.svg  style="width:24px;"> [TechDraw workbench](TechDraw_Workbench.md) made a big step forward regarding the generation of **section views**. To not overload the reference pages this page\'s intention is to give examples and supply proper naming for the performed tasks.

I\'m doing my best to find the correct terms, but since I\'m not a native speaker it\'s your turn to fix my mistakes if you find one.

## Sections

Sections or section views are used to look inside an object to show details that are invisible or hard to recognise from views with hidden lines enabled.

Usually there is a projection group showing a simple object from at least 2 directions for a complete graphical description; complex objects require more views to describe each detail, the hardly visible and the oddly positioned ones.

One of the existing views will be used as a base view where you draw a section line to define how to derive a section view. That is the way for manually drafting and how it is done by most CAD software. **FreeCAD does not work like that yet!**

## Sections the FreeCAD way 

It is not yet (version 1.0) implemented to draw a section line in a 2D view and transfer information such as position and angle back into 3D space.

Instead FreeCAD provides a **Set View Direction** widget in the [Task panel](Task_panel.md) plus either a **Section Plane Location** widget for simple sections or an **Object Selection** widget and a **Projection Strategy** within the Section Parameters for complex sections. (see [Simple section](TechDraw_SectionView#Usage.md) and [Complex section](TechDraw_SectionView#Usage.md))

## Example Object 

This object has no use at all except to describe the different kinds of section representations.

:   (BTW, I rather use the word object than part to avoid confusion with a <img alt="" src=images/Std_Part.svg  style="width:24px;"> [Std Part](Std_Part.md))

 <img alt="" src=images/TechDraw_ExampleSection-01.png  style="width:400px;">  
*A projection group containing 3 views of the object plus a 3D image substituting an ISO(metric) view*

## Simple sections 

Simple sections use a single section plane to cut through the whole object.

Any section view requires a base view (**Base View** property) to position a section plane when using <img alt="" src=images/TechDraw_SectionView.svg  style="width:24px;"> [Insert Section View](TechDraw_SectionView.md) for simple sections. The vertical axis of the section plane is always the normal of the base view and the horizontal axis of the section plane is parallel to the section line. Usually the section view is oriented with its horizontal axis also parallel to the section line. The angle between section line and the base view\'s horizontal axis is controlled by widgets of the Set View Direction area:

 <img alt="" src=images/TechDraw_ComplexSection_Taskview2.png  style="width:200px;"> 

The View Direction as Angle combo-box allows to set an arbitrary angle and the four buttons are used to cut the object at preset angles perpendicular to the horizontal and vertical view axes:

 <img alt="" src=images/Section-up.svg  style="width:32px;"> 90°, <img alt="" src=images/Section-down.svg  style="width:32px;"> 270°, <img alt="" src=images/Section-left.svg  style="width:32px;"> 180°, <img alt="" src=images/Section-right.svg  style="width:32px;"> 0° 

### Horizontal section 

Section A-A (section up)

 <img alt="" src=images/TechDraw_ExampleSection-02.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/TechDraw_ExampleSection-03.png  style="width:200px;">   <img alt="" src=images/TechDraw_ExampleSection-04.png  style="width:200px;">  
*Base View and Section A-A in its proper position*

Section B-B (section down)

 <img alt="" src=images/TechDraw_ExampleSection-02.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/TechDraw_ExampleSection-05.png  style="width:200px;">   <img alt="" src=images/TechDraw_ExampleSection-06.png  style="width:200px;">  
*Base View and Section B-B in its proper position*

### Vertical section 

Section C-C (section left)

 <img alt="" src=images/TechDraw_ExampleSection-02.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/TechDraw_ExampleSection-07.png  style="width:200px;">   <img alt="" src=images/TechDraw_ExampleSection-08.png  style="width:300px;">  
*Base View and Section C-C in its proper position after being rotated by 90°*

Section D-D (section right)

 <img alt="" src=images/TechDraw_ExampleSection-02.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/TechDraw_ExampleSection-09.png  style="width:200px;">   <img alt="" src=images/TechDraw_ExampleSection-10.png  style="width:300px;">  
*Base View and Section D-D in its proper position after being rotated by -90°*

### Arbitrary section 

Section E-E (section at an arbitrary angle)

 <img alt="" src=images/TechDraw_ExampleSection-02.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/TechDraw_ExampleSection-11.png  style="width:200px;">   <img alt="" src=images/TechDraw_ExampleSection-12.png  style="width:300px;">  
*Base View and Section E-E in its proper position after being rotated by -60°*

By default the section plane goes through the global origin (3D) which means the section line goes through the origin of the view. To get an offset section line (and plane respectively) we can change the values within the Section Plane Location widget.

 <img alt="" src=images/TechDraw_ExampleSection-16.png  style="width:300px;">

<img alt="" src=images/TechDraw_ExampleSection-17.png  style="width:300px;">  
*Here the section line was moved 22 mm in X and 14 mm in Y direction (without proof that the hole centers were met); the automatically generated Z value has no influence in this case*

### Auxiliary view 

FreeCAD is lacking a specific tool to derive auxiliary views from base views, but <img alt="" src=images/TechDraw_SectionView.svg  style="width:24px;"> [Insert Section View](TechDraw_SectionView.md) can handle that, too:

Using Section E-E from above and changing the mentioned values to X = {{Value|40 mm}} and Y = {{Value|-23 mm}} the section line/plane doesn\'t cut the object anymore and the section view turns into an auxiliary view. (Be careful when you change the values. Large steps tend to crash FreeCAD!)

 <img alt="" src=images/TechDraw_ExampleSection-12.png  style="width:300px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/TechDraw_ExampleSection-18.png  style="width:300px;">  
*Section E-E like in the example above + moved section line/plane → View E*

The label was edited manually. The section line and one arrow have to be hidden in followig steps since one single arrow is enough to properly define an auxiliary view.

### Notes

-   The examples are created using weekly build 0.21 - 31155 with first angle and ISO selected.
-   Both horizontal section views are oriented as expected.
-   Both vertical section views need to be rotated manually to be oriented as expected.
-   For arbitrary sections the section line and also the section view need to be rotated manually. It is irritating that the angles are not equal.
-   On this occasion realised that horizontal and vertical center lines are oriented according to the page but not the view and so cannot be used to align base and section view, as I would expect.
-   If you double-click the Section E-E object in the Tree view to edit the section line angle you will find 29.89° instead of 30° in the combo-box. What has happened to the value?
-   Applying an offset to a section line/plane is a bit complicated, because it can only be moved along global axes and not according to (local) view axes.
-   If the section plane comes to lie outside the object FreeCAD crashes without warning.

:   Edit: On a closer look I realised that it wasn\'t the placement outside the object but too large steps of movement when using the mouse wheel. Knowing this enables us to create auxiliary views as well.

## Simple sections in use 

### Single Section 

If there is only one section view on a drawing and it is plain to see that the object is cut along a center line, the section line including the arrows and the view title may be omitted.

 <img alt="" src=images/TechDraw_ExampleSection-13.png  style="width:300px;"> <img alt="" src=images/TechDraw_ExampleSection-14.png  style="width:300px;">  
*Both drawings are to standard*

### Internal section 

A section view may be integrated into the base view. This case doesn\'t need arrows and title as well.

 <img alt="" src=images/TechDraw_ExampleSection-15.png  style="width:200px;"> 

## Complex sections 

A complex section such as an aligned section or an offset section uses more than one plane to cut an object.

The <img alt="" src=images/TechDraw_ComplexSection.svg  style="width:24px;"> [TechDraw ComplexSection](TechDraw_ComplexSection.md) tool requires a base view (DataBase View property) to place several connected section planes to cut through the whole object; these are defined by a 3D polyline. (This tool could handle curves and curved section faces, but curved sections are a rather unusual use case)

The vertical axes of the section planes are always parallel to the normal of the base view. Their horizontal axes are derived from the related segments of the 3D polyline. The orientation of the Section view depends on one of the 3D polyline\'s segments and is influenced by the widgets in the Set View Direction area of the Edit Complex Sections dialog:

 <img alt="" src=images/TechDraw_ComplexSection_Taskview1.png  style="width:" height="250px;"> <img alt="" src=images/TechDraw_ComplexSection_Taskview2.png  style="width:" height="250px;"> 

This tool provides 3 options in the Projection Strategy combo-box to handle the section line segments:

-   Offset (default), only segments perpendicular to the viewing direction are displayed
-   Aligned, all cutting segments are displayed in true length
-   NoParallel, all segments are projected along the same viewing direction. Depending on the angle between segment and viewing direction the projections are shorter than the cut area so that parallel sections are reduced to a line.

### Offset section 

An offset section starts with a base view plus a 3D polyline, a <img alt="" src=images/PartDesign_NewSketch.svg  style="width:16px;"> [sketch](PartDesign_NewSketch.md) in this case.

 <img alt="" src=images/TechDraw_ExampleSection-02.png  style="width:200px;"> <img alt="" src=images/Arch_Add.svg  style="width:16px;"> <img alt="" src=images/TechDraw_ExampleSection-19.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/TechDraw_ExampleSection-20.png  style="width:200px;">  
*Base view + sketch + "View Direction as Angle" set to {{Value|30°* → Base View and Section G-G in its default position}} The view direction angle has to be set to a matching value or it might happen that no section view will be created or that the result will be other than expected.

 <img alt="" src=images/TechDraw_ExampleSection-21.png  style="width:300px;">  
*Base View and Section G-G in its proper position after being rotated by -60°*

### Aligned section 

An aligned section also starts with a base view plus another 3D polyline.

 <img alt="" src=images/TechDraw_ExampleSection-02.png  style="width:200px;"> <img alt="" src=images/Arch_Add.svg  style="width:16px;"> <img alt="" src=images/TechDraw_ExampleSection-22.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/TechDraw_ExampleSection-23.png  style="width:200px;">  
*Base view + sketch + "View Direction as Angle" set to {{Value|20°* and "Projection Strategy" to {{Value|Aligned}} → Base View and Section H-H in its default position}} The view direction angle has to be guessed and set to a nearly matching value or the result could be other than expected.

 <img alt="" src=images/TechDraw_ExampleSection-24.png  style="width:300px;">  
*Base View and Section H-H in a position after being rotated by -60° to be parallel to the lower segment of the section line*

This his how a bad guess result looks like:

 <img alt="" src=images/TechDraw_ExampleSection-25.png  style="width:200px;">  
*Arrows on either side of the section line deliver a strange projection, "View Direction as Angle" was set to {{Value|90°*}}

### Auxiliary view 

The <img alt="" src=images/TechDraw_ComplexSection.svg  style="width:24px;"> [TechDraw ComplexSection](TechDraw_ComplexSection.md) tool can, like the <img alt="" src=images/TechDraw_SectionView.svg  style="width:24px;"> [Insert Section View](TechDraw_SectionView.md) tool, create auxiliary views from base views:

An auxiliary view also starts with a base view plus a single 3D line placed outside the object.

 <img alt="" src=images/TechDraw_ExampleSection-02.png  style="width:200px;"> <img alt="" src=images/Arch_Add.svg  style="width:16px;"> <img alt="" src=images/TechDraw_ExampleSection-26.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/TechDraw_ExampleSection-27.png  style="width:300px;">  
*Base view + 3D line → View I*

The label was edited manually. The view direction (direction of the arrows) has to be extracted from the 3D line manually and you have to find the matching \"View Direction as Angle\" value manually. The section line and one arrow have to be hidden in followig steps since one single arrow is enough to properly define an auxiliary view.

:   There is a lot to do by hand, but it is a working solution, at least.

### NoParallel section 

A NoParallel section is a mixture of aligned and offset sections.

 <img alt="" src=images/TechDraw_ExampleSection-02.png  style="width:200px;"> <img alt="" src=images/Arch_Add.svg  style="width:16px;"> <img alt="" src=images/TechDraw_ExampleSection-30.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/TechDraw_ExampleSection-31.png  style="width:250px;">  
*Base view + sketch → Base View and Section K-K rotated (-85°) and moved* The arrow direction should have been horizontal, but in this case the tool did not work when the value of \"View Direction as Angle\" was set to {{Value|0°}}. And so the sketch was rotated by 5° and said angle was set to {{Value|5°}}, too.

### Comparison NoParallel vs. Offset and Aligned 

 <img alt="" src=images/TechDraw_ExampleSection-32.png  style="width:400px;">  
*Base View and Section K-K in 3 versions: "NoParallel": black hatching, "Offset": blue hatching, "Aligned": red hatching *

To be honest, if the value of \"View Direction as Angle\" of the aligned section was set to 5° exactly the result is faulty. When a section is activated for editing, said value is set to odd 5,14°, and it is confirmed with the check button then the expected result will be displayed.

 <img alt="" src=images/TechDraw_ExampleSection-33.png  style="width:400px;">  
*Same as above with "View Direction as Angle" set to {{Value|5°* exactly. The view direction of the second segment from the top is flipped (the shaft is visible)}}

### Complex one line sections 

One aspect that hasn\'t been focused on is that the length (width) of the section depends on the arrow positions i.e. the section line length. In contrast to simple sections where we have no influence on the section line length, we can control this length through the length of the used 3D line, but the results differ from Offset section to NoParallel section:

 <img alt="" src=images/TechDraw_ExampleSection-34.png  style="width:400px;"> <img alt="" src=images/TechDraw_ExampleSection-35.png  style="width:400px;">  
*Two images displaying the same section line definition. Left: The '''Offset section''' acts similar to a break-out view showing the segment between the arrows as a section while the rest of the object stays uncut. Right: The '''NoParallel section''' only shows the section between the arrows and omits the rest of the object (like a detail section?).*

## Complex sections in use 

### Half section 

A view showing a symmetric object cut on one side of a center line and uncut on the other. The depth is usually defined by another center line.

 <img alt="" src=images/TechDraw_ExampleSection-28.png  style="width:200px;"> <img alt="" src=images/TechDraw_ExampleSection-29.png  style="width:200px;"> <img alt="" src=images/TechDraw_ExampleSection-36.png  style="width:170px;">  
*Left and center: Base view and '''offset''' section view with and without section line arrows and title, both are according to standards. 
Right: Alternative section line; after working out the difference shown with section M-M above*

### Notes 

-   The examples are created using weekly build 0.21 - 31155 with first angle and ISO selected.

:   weekly build 0.21 - 31340 for M-M.

-   The view direction (the orientation of the arrows) has to be found manually.
-   All complex sections have to be rotated manually.
-   A \"View Direction as Angle\" value of 0° exactly does not work for offset sections. (180°, too?)
-   The \"View Direction as Angle\" value will be reset to an odd number whenever a section view is activated to be edited.



---
![](images/Right_arrow.png) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw Section Examples
