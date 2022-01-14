---
- GuiCommand:
   Name:Curves SketchOnSurface
   MenuLocation:Surfaces → Sketch on Surface
   Workbenches:[Curves](Curves_Workbench.md)
---

# Curves SketchOnSurface/en

## Description

This tool maps a sketch onto a face, like a label on a bottle. The sketch must be actually attached to a face (see Sketch.Support). The `Map` mode of the sketch has no effect on the result.

<img alt="" src=images/Curves_SketchOnSurface_demo.png  style="width:600" height="400px;"> 
*Above: shows the `Sketch_on_surface* object applied to the cylinder face (left) and the source sketch in edit mode (right)`

## Usage

1.  Switch to the <img alt="" src=images/Curves_workbench_icon.svg  style="width:24px;"> [Curves](Curves_Workbench.md) workbench (install from <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Addon Manager](Std_AddonMgr.md) is necessary, if not previously installed)
2.  There are 2 methods to use the SketchOnSurface tool:

    You already have a sketch that you want to map on a face:

    1.  Attach the sketch to the target face.
    2.  Edit the sketch and add a Construction (blue) rectangle around the geometries.
        -   This rectangle will be the parametric bounds of the face.
    3.  Exit edit mode.
    4.  Select the sketch and activate SketchOnSurface by either:
        1.  Pressing on the <img alt="" src=images/Curves_SketchOnSurface.svg  style="width:24px;"> button
        2.  Using the **Surfaces → Sketch on Surface** entry in the Curves menu

    You have no sketch to map yet:

    1.  Select the target face in the [3D view](3D_view.md)
    2.  Activate SketchOnSurface by either:
        1.  Pressing on the <img alt="" src=images/Curves_SketchOnSurface.svg  style="width:24px;"> button
        2.  Using the **Surfaces → Sketch on Surface** entry in the Curves menu

        :   A \"Sketch on surface\" object appears in the [Combo view](Combo_view.md).
        :   Click on this object to make \"Mapped sketch\" appear below.
        :   Click on the space bar to make \"Mapped sketch\" active. With a double click on \"Mapped sketch\", a blue frame appears. The given dimensions of the blue frame are corresponding to the surface of the object on which you want to map your sketch. The sketch will be placed perpendicular to the surface to be covered.
        :   Draw a SketchOnSurface object on this sketch, the blue frame, like a usual sketch and constrain it 100% (recommended).
        :   Close the sketch - important.
        :   A SketchOnSurface object will be created upon this sketch on the surface of your object.
    3.  Edit the sketch and add geometries inside the blue construction bounds.

## Options

-   Fill Extrusion: When the Thickness value is not null, this will generate lofting faces (the blue faces in the above screenshot).
-   Fill Faces: This will fill all the geometrical figures closed in faces (the red faces in the above screenshot).
-   Offset: This will push the shapes mapped above into the target face. Do not put an offset greater than the thickness, it makes the face disappear on the inside.
-   Thickness: If not null, this will give thickness to the surfaces created above.

## Properties

## Limitations

The blue construction lines of the sketch are part of the sketch even if they are not visible when the sketch is closed and even if the blue lines exceed the blue construction frame. The complete sketch will automatically scale so that it is no larger than the area to be covered.

## Scripting





{{Curves Tools navi

}}

---
[documentation index](../README.md) > Curves SketchOnSurface/en
