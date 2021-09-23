# <img alt="Image workbench icon" src=images/Workbench_Image.svg  style="width:64px;"> Image Workbench/zh-cn

## 简介


{{TOCright}}


{{TOCright}}

[图像工作台用于管理不同类型的](Image_Workbench.md)[位图图像](bitmap.md)，用户可借此在FreeCAD中打开这些图像。

## 工具

-   <img alt="" src=images/Image-import.svg  style="width:32px;"> [Open](Image_Open.md): 在新的视口中打开图像。
-   <img alt="" src=images/Image-import-to-plane.svg  style="width:32px;"> [Import to plane](Image_CreateImagePlane.md): 将图像导入至3D视图中的平面内。
-   <img alt="" src=images/Image-scale.svg  style="width:32px;"> [Scaling](Image_Scaling.md): 对导入至平面内的图像进行缩放处理。

## 特性

-   与[草图相似](Sketcher_Workbench.md)，我们可将导入的图像附于XY，XZ或YZ主平面之一，并为之调整正、负偏移值。
-   导入图像的比例关系为1像素:1毫米。
-   建议导入具有合理分辨率的图像。

## 工作流程

图形工作台的一个主要用途就是借助[底图或](Draft_Workbench.md)[草图工具对目标图像进行描边](Sketcher_Workbench.md)，即为了基于目标图像的轮廓来生成对应实体。

若要进行描边处理，最好是令图像距工作平面有个较小的负偏移量，例如-0.1 mm。这就意味着图像将稍稍偏于绘制2D几何图形平面的后侧，继而就不会把2D底图/草图绘制在图像上了。

可在导入图像时设置其偏移量，或者在后面的处理流程中通过修改其属性来实现这一点。





{{Image Tools navi

}} 

[Category:Workbenches](Category:Workbenches.md)

---
[documentation index](../README.md) > Image Workbench/zh-cn
