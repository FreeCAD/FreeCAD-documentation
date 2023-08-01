---
- GuiCommand:
   Name:Image CreateImagePlane
   MenuLocation:
   Workbenches:[Image](Image_Workbench.md)
   SeeAlso:[Image Open](Image_Open.md), [Image Scaling](Image_Scaling.md)
---

# Image CreateImagePlane/zh-cn

## 描述


<div class="mw-translate-fuzzy">

利用[创建图像平面工具可导入](Image_CreateImagePlane.md)[位图图像](bitmap.md)，并将它置于XY、YZ或XZ平面之中。


</div>


<div class="mw-translate-fuzzy">

## 如何使用


</div>


<div class="mw-translate-fuzzy">

1.  按下**<img src="images/Image_CreateImagePlane.svg" width=16px> [Image Plane](Image_CreateImagePlane.md)**按钮。
2.  从系统中选择希望导入的图像。
3.  选择放置图像的平面，指定偏移值，再点击**OK**。


</div>

生成的ImagePlane（图像平面）对象所采用的比例是1像素:1毫米；为了令图像显示效果更佳，应当令其具有足够的分辨率。


<div class="mw-translate-fuzzy">

在导入图像时，为了令图像稍处于工作平面之后，您应当为之添加`-0.1 mm`的偏移量；这将令采用[底图或](Draft_Workbench.md)[草图工具对图像进行的描边工作](Sketcher_Workbench.md)（在其上侧进行描绘）进行得更为顺利。


</div>


<div class="mw-translate-fuzzy">

如果在导入图片伊始没有添加偏移量，其位置仍可通过[属性编辑器进行调整](property_editor.md)。


</div>

## 属性


{{Properties Title|Base}}


<div class="mw-translate-fuzzy">


{{Properties Title|Base}}

-    **Position**: 指定图像平面的基准点（base point）坐标。

-    **Angle**: 指定图像平面的旋转角度。

-    **Axis**: 指定旋转轴。


</div>


{{Properties Title|Image Plane}}


<div class="mw-translate-fuzzy">


{{Properties Title|Image Plane}}

-    **XSize**: 指定图像平面的宽度。

-    **YSize**: 指定图像平面的高度。

-    **Image Plane**: 指定用于此图像平面的对应图像。


</div>





{{Image Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [Image](Image_Workbench.md) > Image CreateImagePlane/zh-cn
