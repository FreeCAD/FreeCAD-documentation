# Part Workbench/zh-cn
<div lang="en" dir="ltr" class="mw-content-ltr">





</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

<img alt="Part workbench icon" src=images/Workbench_Part.svg  style="width:128px;">


</div>





<div lang="en" dir="ltr" class="mw-content-ltr">

## Introduction


</div>


<div class="mw-translate-fuzzy">

## 简介

FreeCAD的实体建模能力都是基于 [Open Cascade Technology](http://en.wikipedia.org/wiki/Open_Cascade_Technology) (OCCT)内核一种具有创建与处理高级3D几何体等特性的专业级CAD系统。[零件工作台（Part Workbench）](Part_Workbench.md)是一种建立于OCCT库之上的层级，为用户提供了访问OCCT几何图元与函数的功能。每种工作台(如[底图](Draft_Workbench.md)工作台, [草图](Sketcher_Workbench.md)工作台, [零件设计](PartDesign_Workbench.md)工作台等等)的一切2D与3D绘制功能其实都是基于零件工作台暴露出的函数实现的。因此，可以认为零件工作台是FreeCAD建模功能的核心组件。


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

The Part Workbench can also create objects that are not solids, such as faces, shells, and objects with only edges or vertices. It also provides a variety of general purpose tools for geometry manipulation, geometry validation, and making copies.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

The <img alt="" src=images/Workbench_PartDesign.svg  style="width:16px;"> [PartDesign Workbench](PartDesign_Workbench.md) uses an alternative workflow for creating solids. For a detailed discussion of the Part Workbench versus the Part Design Workbench see [Part and Part Design](Part_and_PartDesign.md).


</div>

![](images/Part_Workbench_Example.jpg )



## 工具


<div lang="en" dir="ltr" class="mw-content-ltr">

### Solids toolbar 


</div>

-   <img alt="" src=images/Part_Box.svg  style="width:32px;"> [Box](Part_Box.md): 根据指定的规格绘制一个立方体

-   <img alt="" src=images/Part_Cylinder.svg  style="width:32px;"> [Cylinder](Part_Cylinder.md): 根据指定的规格绘制一个圆柱体

-   <img alt="" src=images/Part_Sphere.svg  style="width:32px;"> [Sphere](Part_Sphere.md): 根据指定的规格绘制一个球体

-   <img alt="" src=images/Part_Cone.svg  style="width:32px;"> [Cone](Part_Cone.md): 根据指定的规格绘制一个圆锥体

-   <img alt="" src=images/Part_Torus.svg  style="width:32px;"> [Torus](Part_Torus.md): 根据指定的规格绘制一个环面（torus）（圆环 (ring)）


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/Part_Tube.svg  style="width:32px;"> [Tube](Part_Tube.md): Creates a tube.


</div>

-   <img alt="" src=images/Part_Primitives.svg  style="width:32px;"> [CreatePrimitives](Part_CreatePrimitives.md): 一种用于创建各类参数化几何图元的工具


<div lang="en" dir="ltr" class="mw-content-ltr">

  - <img alt="" src=images/Part_Plane.svg  style="width:32px;"> [Plane](Part_Plane.md): Creates a plane.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

  - <img alt="" src=images/Part_Box.svg  style="width:32px;"> [Box](Part_Box.md): Creates a box. This object can also be created with the [Box](Part_Box.md) tool.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

  - <img alt="" src=images/Part_Cylinder.svg  style="width:32px;"> [Cylinder](Part_Cylinder.md): Creates a cylinder. This object can also be created with the [Cylinder](Part_Cylinder.md) tool.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

  - <img alt="" src=images/Part_Cone.svg  style="width:32px;"> [Cone](Part_Cone.md): Creates a cone. This object can also be created with the [Cone](Part_Cone.md) tool.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

  - <img alt="" src=images/Part_Sphere.svg  style="width:32px;"> [Sphere](Part_Sphere.md): Creates a sphere. This object can also be created with the [Sphere](Part_Sphere.md) tool.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

  - <img alt="" src=images/Part_Ellipsoid.svg  style="width:32px;"> [Ellipsoid](Part_Ellipsoid.md): Creates a ellipsoid.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

  - <img alt="" src=images/Part_Torus.svg  style="width:32px;"> [Torus](Part_Torus.md): Creates a torus. This object can also be created with the [Torus](Part_Torus.md) tool.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

  - <img alt="" src=images/Part_Prism.svg  style="width:32px;"> [Prism](Part_Prism.md): Creates a prism.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

  - <img alt="" src=images/Part_Wedge.svg  style="width:32px;"> [Wedge](Part_Wedge.md): Creates a wedge.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

  - <img alt="" src=images/Part_Helix.svg  style="width:32px;"> [Helix](Part_Helix.md): Creates a helix.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

  - <img alt="" src=images/Part_Spiral.svg  style="width:32px;"> [Spiral](Part_Spiral.md): Creates a spiral.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

  - <img alt="" src=images/Part_Circle.svg  style="width:32px;"> [Circle](Part_Circle.md): Creates a circular arc.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

  - <img alt="" src=images/Part_Ellipse.svg  style="width:32px;"> [Ellipse](Part_Ellipse.md): Creates an elliptical arc.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

  - <img alt="" src=images/Part_Point.svg  style="width:32px;"> [Point](Part_Point.md): Creates a point.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

  - <img alt="" src=images/Part_Line.svg  style="width:32px;"> [Line](Part_Line.md): Creates a line.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

  - <img alt="" src=images/Part_RegularPolygon.svg  style="width:32px;"> [Regular polygon](Part_RegularPolygon.md): Creates a regular polygon.


</div>

-   <img alt="" src=images/Part_Shapebuilder.svg  style="width:32px;"> [Shapebuilder](Part_Shapebuilder.md): 一种利用各种参数化几何图元创建更加复杂几何图形的工具


<div lang="en" dir="ltr" class="mw-content-ltr">

### Part tools toolbar 


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/Sketcher_NewSketch.svg  style="width:32px;"> [Create sketch](Sketcher_NewSketch.md): Creates a new sketch and opens the [Sketcher Dialog](Sketcher_Dialog.md) to edit it.


</div>

-   <img alt="" src=images/Part_Extrude.svg  style="width:32px;"> [Extrude](Part_Extrude.md): 将对象的平面端面挤压成型

-   <img alt="" src=images/Part_Revolve.svg  style="width:32px;"> [Revolve](Part_Revolve.md): 通过令一（非实体）对象绕某轴旋转来创建另一个实体对象

-   <img alt="" src=images/Part_Mirror.svg  style="width:32px;"> [Mirror](Part_Mirror.md): 根据指定的镜面对选中的对象进行镜像操作


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/Part_Scale.svg  style="width:32px;"> [Scale](Part_Scale.md): Scales one or more shapes. <small>(v1.0)</small> 


</div>

-   <img alt="" src=images/Part_Fillet.svg  style="width:32px;"> [Fillet](Part_Fillet.md): 为对象的边倒(圆)角

-   <img alt="" src=images/Part_Chamfer.svg  style="width:32px;"> [Chamfer](Part_Chamfer.md): 为对象的边倒角


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/Part_MakeFace.svg  style="width:32px;"> [Make face from wires](Part_MakeFace.md): Makes a face from a set of wires (contours).


</div>

-   <img alt="" src=images/Part_RuledSurface.svg  style="width:32px;"> [Ruled Surface](Part_RuledSurface.md):

-   <img alt="" src=images/Part_Loft.svg  style="width:32px;"> [Loft](Part_Loft.md): 对轮廓进行放样操作（放样成另一种轮廓

-   <img alt="" src=images/Part_Sweep.svg  style="width:32px;"> [Sweep](Part_Sweep.md): 沿路径对一个或多个轮廓进行扫描


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/Part_Section.svg  style="width:32px;"> [Section](Part_Section.md): Creates a section by intersecting an object with a section plane.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/Part_CrossSections.svg  style="width:32px;"> [Cross sections\...](Part_CrossSections.md): Creates one or more cross-sections through an object.


</div>

-   <img alt="" src=images/Part_Offset.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Offset:

  - <img alt="" src=images/Part_Offset.svg  style="width:32px;"> [3D Offset](Part_Offset.md): 根据原始几何形状在特定的距离处构建一个平行的副本。

  - <img alt="" src=images/Part_Offset2D.svg  style="width:32px;"> [2D Offset](Part_Offset2D.md): 根据原始连线在特定的距离处创建一个平行的副本，或者缩放一个平面端面。

-   <img alt="" src=images/Part_Thickness.svg  style="width:32px;"> [Thickness](Part_Thickness.md): 镂空一个实体，在选中的面上留下开口。

-   <img alt="" src=images/Part_ProjectionOnSurface.png  style="width:32px;"> [Projection on surface](Part_ProjectionOnSurface.md): 向表面上投影logo、文本或任意表面、连线、边。可以为投影部分创建一个示例或连线。


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/Part_ColorPerFace.svg  style="width:32px;"> [Color per face](Part_ColorPerFace.md): Assigns colors to individual faces of objects.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

### Boolean toolbar 


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/Part_Compound.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Compound:


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

  - <img alt="" src=images/Part_Compound.svg  style="width:32px;"> [Make compound](Part_Compound.md): Creates a compound from the selected objects.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

  - <img alt="" src=images/Part_ExplodeCompound.svg  style="width:32px;"> [Explode compound](Part_ExplodeCompound.md): Splits up compounds.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

  - <img alt="" src=images/Part_CompoundFilter.svg  style="width:32px;"> [Compound Filter](Part_CompoundFilter.md): Extracts the individual pieces from compounds.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Part_Boolean.svg  style="width:32px;"> [Boolean](Part_Boolean.md): 在对象上执行布尔运算


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/Part_Cut.svg  style="width:32px;"> [Cut](Part_Cut.md): Cuts one object from another.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/Part_Fuse.svg  style="width:32px;"> [Union](Part_Fuse.md): Fuses two or more objects.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/Part_Common.svg  style="width:32px;"> [Intersection](Part_Common.md): Extracts the common part of two objects.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/Part_JoinConnect.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Join:


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

  - <img alt="" src=images/Part_JoinConnect.svg  style="width:32px;"> [Connect objects](Part_JoinConnect.md): Connects interiors of walled objects.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

  - <img alt="" src=images/Part_JoinEmbed.svg  style="width:32px;"> [Embed object](Part_JoinEmbed.md): Embeds a walled object into another walled object.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

  - <img alt="" src=images/Part_JoinCutout.svg  style="width:32px;"> [Cutout for object](Part_JoinCutout.md): Creates a cutout in a wall of an object for another walled object.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/Part_BooleanFragments.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Split:


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

  - <img alt="" src=images/Part_BooleanFragments.svg  style="width:32px;"> [Boolean fragments](Part_BooleanFragments.md): Creates all pieces obtained from Boolean operations.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

  - <img alt="" src=images/Part_SliceApart.svg  style="width:32px;"> [Slice apart](Part_SliceApart.md): Slices and splits an object by intersecting it with other objects.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

  - <img alt="" src=images/Part_Slice.svg  style="width:32px;"> [Slice to compound](Part_Slice.md): Slices an object by intersecting it with other objects.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

  - <img alt="" src=images/Part_XOR.svg  style="width:32px;"> [Boolean XOR](Part_XOR.md): Removes space shared by an even number of objects.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/Part_CheckGeometry.svg  style="width:32px;"> [Check geometry](Part_CheckGeometry.md): Checks the geometry of selected objects for errors.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/Part_Defeaturing.svg  style="width:32px;"> [Defeaturing](Part_Defeaturing.md): Removes features from an object.


</div>




<div class="mw-translate-fuzzy">

### 其他工具


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Part_Import.svg  style="width:32px;"> [Import](Part_Import/zh-cn.md): 您可利用此工具为当前文档添加\*.IGES、\*.STEP、\*.BREP文档。


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/Part_Export.svg  style="width:32px;"> [Export CAD file\...](Part_Export.md): Exports to \*.IGES, \*.STEP, or \*.BREP files.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/Part_BoxSelection.svg  style="width:32px;"> [Box selection](Part_BoxSelection.md): Selects faces from a rectangular area.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/Part_ShapeFromMesh.svg  style="width:32px;"> [Create shape from mesh](Part_ShapeFromMesh.md): Creates shapes from mesh objects.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/Part_PointsFromMesh.svg  style="width:32px;"> [Create points object from geometry](Part_PointsFromMesh.md): Creates points objects from geometric objects.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/Part_MakeSolid.svg  style="width:32px;"> [Convert to solid](Part_MakeSolid.md): Creates solids from shape objects.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/Part_ReverseShape.svg  style="width:32px;"> [Reverse shapes](Part_ReverseShape.md): Creates parametric copies with reversed face normals from selected objects.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   Create a copy:


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

  - <img alt="" src=images/Part_SimpleCopy.svg  style="width:32px;"> [Create simple copy](Part_SimpleCopy.md): Creates non-parametric copies of objects.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

  - <img alt="" src=images/Part_TransformedCopy.svg  style="width:32px;"> [Create transformed copy](Part_TransformedCopy.md): Creates non-parametric copies of objects. It is intended for objects nested in containers.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

  - <img alt="" src=images/Part_ElementCopy.svg  style="width:32px;"> [Create shape element copy](Part_ElementCopy.md): Creates non-parametric copies of subelements: vertices, edges and faces.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

  - <img alt="" src=images/Part_RefineShape.svg  style="width:32px;"> [Refine shape](Part_RefineShape.md): Creates parametric copies with a refined shape from selected objects. It removes unnecessary edges from planar and cylindrical faces.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/Part_EditAttachment.svg  style="width:32px;"> [Attachment\...](Part_EditAttachment.md): Attaches an object to one or more other objects.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

## Obsolete tools 


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

### Measure


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

The <img alt="" src=images/Std_Measure.svg  style="width:32px;"> [Std Measure](Std_Measure.md) tool replaces the tools listed below. <small>(v1.0)</small> 


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/Part_Measure_Linear.svg  style="width:32px;"> [Measure Linear](Part_Measure_Linear.md): Creates a linear measurement. Not available in <small>(v1.0)</small> .


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/Part_Measure_Angular.svg  style="width:32px;"> [Measure Angular](Part_Measure_Angular.md): Creates an angular measurement. Not available in <small>(v1.0)</small> .


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/Part_Measure_Refresh.svg  style="width:32px;"> [Measure Refresh](Part_Measure_Refresh.md): Updates all measurements. Not available in <small>(v1.0)</small> .


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/Part_Measure_Clear_All.svg  style="width:32px;"> [Clear All](Part_Measure_Clear_All.md) and [View Measure Clear All](View_Measure_Clear_All.md): Clears all measurements. Not available in <small>(v1.0)</small> .


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/Part_Measure_Toggle_All.svg  style="width:32px;"> [Toggle All](Part_Measure_Toggle_All.md) and [View Measure Toggle All](View_Measure_Toggle_All.md): Shows or hides all measurements. Not available in <small>(v1.0)</small> .


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/Part_Measure_Toggle_3D.svg  style="width:32px;"> [Toggle 3D](Part_Measure_Toggle_3D.md): Shows or hides 3D measurements. Not available in <small>(v1.0)</small> .


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/Part_Measure_Toggle_Delta.svg  style="width:32px;"> [Toggle Delta](Part_Measure_Toggle_Delta.md): Shows or hides delta measurements. Not available in <small>(v1.0)</small> .


</div>



## 首选项


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Preferences-import-export.svg  style="width:32px;"> [Preference \...](Import_Export_Preferences.md) 导入 导出


</div>



## 脚本


<div class="mw-translate-fuzzy">


**参见:**

[零件脚本](Part_scripting.md)


</div>



## 教程

-   [从STL或OBJ文件中导入数据](Import_from_STL_or_OBJ.md) : 如何在FreeCAD中导入STL/OBJ文件。
-   [导出STL或OBJ文件](Export_to_STL_or_OBJ.md) : 如何从FreeCAD中导出STL/OBJ文件
-   [Whiffle球教程](Whiffle_Ball_tutorial.md) : 如何使用零件模块


<div lang="en" dir="ltr" class="mw-content-ltr">





</div>



---
⏵ [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > [Part](Category_Part.md) > Part Workbench/zh-cn
