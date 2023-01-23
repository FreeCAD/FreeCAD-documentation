---
- GuiCommand:
   Name:Part Builder
   MenuLocation:Part → Shape builder...
   Workbenches:[Part](Part_Workbench.md)
   SeeAlso:[Part Primitives](Part_Primitives.md)
---

# Part Builder/zh-cn

## Description


<div class="mw-translate-fuzzy">

## 描述

一种利用各种参数化几何图元来创建更为复杂形状的工具。


</div>




<div class="mw-translate-fuzzy">

## 用法

本工具可以令您通过下列选项来创建几何形状

1.  由两个顶点构成的边
2.  由多个顶点构成的面
    1.  在3D视图里选中围成面的多个顶点
    2.  选择所创建的面是否为平面
    3.  点击** Create**按钮
    4.  即可在3D视图中创建目标对象，且列于树状视图中
3.  由多条边构成的连线 <small>(v0.18)</small> 
    1.  在3D视图里选中一系列邻边
    2.  点击** Create**按钮
4.  由多条边构成的面
    1.  在3D视图里选中一系列围成目标面的闭合边
    2.  选择所创建的面是否为平面
    3.  点击** Create**按钮
    4.  目标对象将被创于3D视图中，且列于树状视图中
5.  由多个面构成的壳
    1.  在3D视图中选中所需的诸面
    2.  选择是否需要对形状进行细化（refine shape）
    3.  选择是否将所有的面都包括进壳中
    4.  点击** Create**按钮
    5.  即可在3D视图里创建目标对象，并列于树状视图中
6.  由壳围成的实体
    1.  选择是否需要对形状进行细化
    2.  点击** Create**按钮
    3.  即可在3D视图中创建目标对象，并将其列于树状视图中


</div>

This tool can create the following objects:

### Edge from two vertices 

1.  Select two vertices
2.  Click on **Create**

![](images/Edge_from_verts-1.gif )

### Wire from edges 

1.  Select a set of adjacent edges in the [3D view](3D_view.md)
2.  Click on **Create**

![](images/Wire_from_edges-1.gif )

### Face from vertices 

1.  Select vertices bounding the face in the [3D view](3D_view.md)
2.  Select if face should be planar
3.  Click on **Create**
4.  Object will be created in [3D view](3D_view.md) and will be listed in [tree view](Tree_view.md)

![](images/Face_from_verts.gif )

### Face from edges 

1.  Select a closed set of edges bounding the face in the [3D view](3D_view.md)
2.  Select if face should be planar
3.  Click on **Create**
4.  Object will be created in [3D view](3D_view.md) and will be listed in [tree view](Tree_view.md)

![](images/Face_from_edges.gif )

### Shell from faces 

1.  Select faces in the [3D view](3D_view.md)
2.  Select if the shape should be refined
3.  Select if all faces should be included in shell
4.  Click on **Create**
5.  Object will be created in [3D view](3D_view.md) and will be listed in [tree view](Tree_view.md)

### Solid from shell 

1.  Select if the shape should be refined
2.  Click on **Create**
3.  Object will be created in [3D view](3D_view.md) and will be listed in [tree view](Tree_view.md)

## Notes


<div class="mw-translate-fuzzy">

## 备注

一种可能采用的工作流：

-   利用底图工作台中的工具（例如线条或连线）来绘制一个目标形状的线框模型。
-   利用（形状构建工具中的）\"face from edges（根据边创建面）\"选项创建所有的面
-   利用\"shell from faces（根据面创建壳）\"选项创建一个壳
-   利用\"solid from shell（根据壳创建实体）\"选项创建一个实体


</div>



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Builder/zh-cn
