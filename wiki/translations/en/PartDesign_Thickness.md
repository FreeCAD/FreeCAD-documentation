---
- GuiCommand   *
   Name   *PartDesign Thickness
   MenuLocation   *Part Design → Apply a dress-up feature → Thickness
   Workbenches   *[PartDesign](PartDesign_Workbench.md)
   Version   *0.17
   SeeAlso   *[Part Thickness](Part_Thickness.md)
---

# PartDesign Thickness/en

## Description

The **Thickness** tool works on a solid Body and transforms it into a thick-walled hollow object with at least one open face, giving to each of its remaining faces a uniform thickness. On some solids it allows you to significantly speed up the work, and avoids making extrusions and pockets.

<img alt="" src=images/PartDesign_Thickness_example.svg  style="width   *600px;"> 
*The thickness tool applied to a face (B) of a solid (A), resulting in the hollow object (C).*

## Usage

1.  Select one or more face(s) on the active Body.
2.  Press the **<img src="images/PartDesign_Thickness.svg" width=24px> '''Thickness'''** button.
3.  Define the **Thickness parameters** (see [Options](#Options.md)).
4.  To add more faces to open, press the **Add face** button and select a face in the [3D view](3D_view.md).
5.  To remove a previously select face, press the **Remove face** button and select a face in the 3D view, or right-click on the Face label in the list and select *Remove*.
6.  Press **OK**.

## Options

-   **Thickness**   * Wall thickness of the resulting object. Set the desired value.
-   **Mode**
    -   *Skin*   * Select this option if you want to get an item like a vase, headless but with the bottom
    -   *Pipe*   * Select this option if you want to get an object like a pipe, headless and bottomless. In this case it may be convenient to select the faces to be deleted before you start the tool. Helping with predefined views buttons or use the numeric keys.
    -   *Recto Verso*   *
-   **Join Type**
    -   *Arc*   * removes the outer edges and creates a fillet with a radius equal to the defined thickness.
    -   *Intersection*   * when faces are offset outward, sharp edges are kept between faces.
-   **Make thickness inwards**   * when checked, faces are offset inward.

## Limitations

-   At least one face to be opened must be selected.
-   If thickness goes inwards, the value must be smaller than the smallest height of the Body.
-   The command may fail with complex shapes. In this context the surface of e.g. a cone has already to be regarded as complex.
    -   [Additive Pipe](PartDesign_AdditivePipe.md) or [Additive Loft](PartDesign_AdditiveLoft.md) may work better to create complex shapes

## Example

1.  Create a Pad from the sketch
2.  Create a second sketch on the XY plane
3.  Create a second Pad from the second sketch

As in the following pictures   *

![](images/Braga-primoPad.png )

![](images/Braga-secondoschizzo.png )

![](images/Braga-secondo_Pad.png )

Then

1.  Select a circular face
2.  Select **<img src="images/PartDesign_Thickness.svg" width=24px> Thickness
**
3.  Add the other circular faces to the selection

Result   * ![](images/Brga-spessore.png )

## Known Errors 

-   BRep\_API   * command not done
-   BRep\_Tool   * no parameter on edge
-   Silently Fails





{{PartDesign Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Thickness/en
