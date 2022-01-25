---
- GuiCommand:
   Name:Image CreateImagePlane
   MenuLocation:
   Workbenches:[Image](Image_Workbench.md)
   SeeAlso:[Image Open](Image_Open.md), [Image Scaling](Image_Scaling.md)
---

# Image CreateImagePlane/es

## Descripción

The [CreateImagePlane](Image_CreateImagePlane.md) tool imports a [bitmap](bitmap.md) image and places it on one of the XY, YZ or XZ planes.

## Utilización

1.  Press the **<img src="images/Image_CreateImagePlane.svg" width=16px> [Image CreateImagePlane](Image_CreateImagePlane.md)** button.
2.  Select the desired image in your system.
3.  Choose the plane where the image will be placed, give an offset value, and press **OK**.

The resulting ImagePlane object uses the ratio of 1 pixel to 1 millimeter; in order for the image to display well, it should have enough resolution.

When importing the image, you may wish to add an offset of `-0.1 mm` in order to place the image slightly behind the working plane; this will make it easy to trace (draw on top) the image with the [Draft](Draft_Workbench.md) or [Sketcher](Sketcher_Workbench.md) tools.

If no offset is given to the image initially, its position can still be adjusted in the [property editor](Property_editor.md).

## Propiedades


{{Properties Title|Base}}

-    **Position**: specifies the coordinates of the base point of the image plane.

-    **Angle**: specifies the angle of rotation of the image plane.

-    **Axis**: specifies the axis used for the rotation angle.


{{Properties Title|Image Plane}}

-    **XSize**: specifies the width of the image plane.

-    **YSize**: specifies the height of the image plane.

-    **Image Plane**: specifies the image to use for this plane.


<div class="mw-translate-fuzzy">





</div>


{{Image Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Image](Image_Workbench.md) > Image CreateImagePlane/es
