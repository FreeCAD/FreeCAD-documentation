# <img alt="Part workbench icon" src=images/Workbench_Part.svg  style="width:64px;"> Part Module/zh-cn


{{TOCright}}

## Introduction


<div class="mw-translate-fuzzy">

## 简介

FreeCAD的实体建模能力都是基于 [Open Cascade Technology](http://en.wikipedia.org/wiki/Open_Cascade_Technology) (OCCT)内核一种具有创建与处理高级3D几何体等特性的专业级CAD系统。[零件工作台（Part Workbench）是一种建立于OCCT库之上的层级](Part_Workbench.md)，为用户提供了访问OCCT几何图元与函数的功能。每种工作台(如[底图工作台](Draft_Workbench.md), [草图工作台](Sketcher_Workbench.md), [零件设计工作台等等](PartDesign_Workbench.md))的一切2D与3D绘制功能其实都是基于零件工作台暴露出的函数实现的。因此，可以认为零件工作台是FreeCAD建模功能的核心组件。


</div>

A more detailed discussion of Part workbench versus Part Design workbench can be found here: [Part and Part Design](Part_and_PartDesign.md).


<div class="mw-translate-fuzzy">

以零件工作台创建的对象相对简单；为了构建更为复杂的几何图形，可以为之运用布尔运算(并集与减运算)。此建模范式就是尽人皆知的[构造实体几何](constructive_solid_geometry.md) (CSG) 工作流程，它是早期CAD系统中所用的传统方法。另一方面，[零件设计工作台（PartDesign Workbench）还提供了更为现代的工作流程来构建几何图形](PartDesign_Workbench.md)：它利用参数化方式来定义草图，再将其挤压成型为基本的实体对象，最后通过参数化变换([特征编辑](feature_editing.md))来修改模型，直到用户获取预期的最终模型为止。


</div>


<div class="mw-translate-fuzzy">

零件对象比[网格工作台（Mesh Workbench）创建的网格对象更为复杂](Mesh_Workbench.md)，因为用户可以对前者执行更为高级的操作，如连续的布尔运算、修改历史与参数化处理。


</div>

<img alt="" src=images/Part_Workbench_relationships.svg  style="width:600px;">


<div class="mw-translate-fuzzy">



*零件工作台是最基础的层级，它为FreeCAD中的其他工作台暴露出OCCT的各种绘制函数*


</div>

## 工具


<div class="mw-translate-fuzzy">

这些工具皆位于**Part**菜单。


</div>


<div class="mw-translate-fuzzy">

### 图元


</div>

以下这些工具用于创建图元对象。


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Part_Box.png  style="width:32px;"> [Box](Part_Box.md): 根据指定的规格绘制一个立方体
-   <img alt="" src=images/Part_Cylinder.png  style="width:32px;"> [Cylinder](Part_Cylinder.md): 根据指定的规格绘制一个圆柱体
-   <img alt="" src=images/Part_Sphere.png  style="width:32px;"> [Sphere](Part_Sphere.md): 根据指定的规格绘制一个球体
-   <img alt="" src=images/Part_Cone.png  style="width:32px;"> [Cone](Part_Cone.md): 根据指定的规格绘制一个圆锥体
-   <img alt="" src=images/Part_Torus.png  style="width:32px;"> [Torus](Part_Torus.md): 根据指定的规格绘制一个环面（torus）（圆环 (ring)）
-   <img alt="" src=images/Part_CreatePrimitives.png  style="width:32px;"> [CreatePrimitives](Part_CreatePrimitives.md): 一种用于创建各类参数化几何图元的工具
-   <img alt="" src=images/Part_Shapebuilder.png  style="width:32px;"> [Shapebuilder](Part_Shapebuilder.md): 一种利用各种参数化几何图元创建更加复杂几何图形的工具


</div>

-   <img alt="" src=images/Part_Cylinder.svg  style="width:32px;"> [Cylinder](Part_Cylinder.md): Creates a cylinder.

-   <img alt="" src=images/Part_Sphere.svg  style="width:32px;"> [Sphere](Part_Sphere.md): Creates a sphere.

-   <img alt="" src=images/Part_Cone.svg  style="width:32px;"> [Cone](Part_Cone.md): Creates a cone.

-   <img alt="" src=images/Part_Torus.svg  style="width:32px;"> [Torus](Part_Torus.md): Creates a torus.

-   <img alt="" src=images/Part_Tube.svg  style="width:32px;"> [Tube](Part_Tube.md): Creates a tube. <small>(v0.19)</small> 

-   <img alt="" src=images/Part_Primitives.svg  style="width:32px;"> [Create primitives\...](Part_Primitives.md): A tool to create one of the following primitives:
    -   <img alt="" src=images/Part_Plane.svg  style="width:32px;"> [Plane](Part_Plane.md): Creates a plane.
    -   <img alt="" src=images/Tree_Part_Box_Parametric.svg  style="width:32px;"> [Box](Part_Box.md): Creates a box. This object can also be created with the <img alt="" src=images/Part_Box.svg  style="width:32px;"> [Box](Part_Box.md) tool.
    -   <img alt="" src=images/Tree_Part_Cylinder_Parametric.svg  style="width:32px;"> [Cylinder](Part_Cylinder.md): Creates a cylinder. This object can also be created with the <img alt="" src=images/Part_Cylinder.svg  style="width:32px;"> [Cylinder](Part_Cylinder.md) tool.
    -   <img alt="" src=images/Tree_Part_Cone_Parametric.svg  style="width:32px;"> [Cone](Part_Cone.md): Creates a cone. This object can also be created with the <img alt="" src=images/Part_Cone.svg  style="width:32px;"> [Cone](Part_Cone.md) tool.
    -   <img alt="" src=images/Tree_Part_Sphere_Parametric.svg  style="width:32px;"> [Sphere](Part_Sphere.md): Creates a sphere. This object can also be created with the <img alt="" src=images/Part_Sphere.svg  style="width:32px;"> [Sphere](Part_Sphere.md) tool.
    -   <img alt="" src=images/Part_Ellipsoid.svg  style="width:32px;"> [Ellipsoid](Part_Ellipsoid.md): Creates a ellipsoid.
    -   <img alt="" src=images/Tree_Part_Torus_Parametric.svg  style="width:32px;"> [Torus](Part_Torus.md): Creates a torus. This object can also be created with the <img alt="" src=images/Part_Torus.svg  style="width:32px;"> [Torus](Part_Torus.md) tool.
    -   <img alt="" src=images/Part_Prism.svg  style="width:32px;"> [Prism](Part_Prism.md): Creates a prism.
    -   <img alt="" src=images/Part_Wedge.svg  style="width:32px;"> [Wedge](Part_Wedge.md): Creates a wedge.
    -   <img alt="" src=images/Part_Helix.svg  style="width:32px;"> [Helix](Part_Helix.md): Creates a helix.
    -   <img alt="" src=images/Part_Spiral.svg  style="width:32px;"> [Spiral](Part_Spiral.md): Creates a spiral.
    -   <img alt="" src=images/Part_Circle.svg  style="width:32px;"> [Circle](Part_Circle.md): Creates a circular arc.
    -   <img alt="" src=images/Part_Ellipse.svg  style="width:32px;"> [Ellipse](Part_Ellipse.md): Creates an elliptical arc.
    -   <img alt="" src=images/Part_Point.svg  style="width:32px;"> [Point](Part_Point.md): Creates a point.
    -   <img alt="" src=images/Part_Line.svg  style="width:32px;"> [Line](Part_Line.md): Creates a line.
    -   <img alt="" src=images/Part_RegularPolygon.svg  style="width:32px;"> [Regular polygon](Part_RegularPolygon.md): Creates a regular polygon.

-   <img alt="" src=images/Part_Builder.svg  style="width:32px;"> [Shape builder\...](Part_Builder.md): Creates shapes from various primitives.


<div class="mw-translate-fuzzy">

## 修改对象


</div>


<div class="mw-translate-fuzzy">

这些工具用于修改已存在的对象。通过它们即可选取待修改的对象。


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Part_Extrude.png  style="width:32px;"> [Extrude](Part_Extrude.md): 将对象的平面端面挤压成型
-   <img alt="" src=images/Part_Revolve.png  style="width:32px;"> [Revolve](Part_Revolve.md): 通过令一（非实体）对象绕某轴旋转来创建另一个实体对象
-   <img alt="" src=images/Part_Mirror.png  style="width:32px;"> [Mirror](Part_Mirror.md): 根据指定的镜面对选中的对象进行镜像操作
-   <img alt="" src=images/Part_Fillet.png  style="width:32px;"> [Fillet](Part_Fillet.md): 为对象的边倒(圆)角
-   <img alt="" src=images/Part_Chamfer.png  style="width:32px;"> [Chamfer](Part_Chamfer.md): 为对象的边倒角
-   <img alt="" src=images/Part_RuledSurface.png  style="width:32px;"> [Ruled Surface](Part_RuledSurface.md):
-   <img alt="" src=images/Part_Loft.png  style="width:32px;"> [Loft](Part_Loft.md): 对轮廓进行放样操作（放样成另一种轮廓）
-   <img alt="" src=images/Part_Sweep.png  style="width:32px;"> [Sweep](Part_Sweep.md): 沿路径对一个或多个轮廓进行扫描


</div>

-   <img alt="" src=images/Part_Revolve.svg  style="width:32px;"> [Revolve](Part_Revolve.md): Creates a solid by revolving an object (not a solid) around an axis.

-   <img alt="" src=images/Part_Mirror.svg  style="width:32px;"> [Mirror](Part_Mirror.md): Mirrors the selected object across a mirror plane.

-   <img alt="" src=images/Part_Fillet.svg  style="width:32px;"> [Fillet](Part_Fillet.md): Fillets (rounds) edges of an object.

-   <img alt="" src=images/Part_Chamfer.svg  style="width:32px;"> [Chamfer](Part_Chamfer.md): Chamfers edges of an object.

-   <img alt="" src=images/Part_MakeFace.svg  style="width:32px;"> [Make face from wires](Part_MakeFace.md): Makes a face from a set of wires (contours). <small>(v0.19)</small> 

-   <img alt="" src=images/Part_RuledSurface.svg  style="width:32px;"> [Ruled Surface](Part_RuledSurface.md): Creates a ruled surface.

-   <img alt="" src=images/Part_Loft.svg  style="width:32px;"> [Loft](Part_Loft.md): Lofts from one profile to another.

-   <img alt="" src=images/Part_Sweep.svg  style="width:32px;"> [Sweep](Part_Sweep.md): Sweeps one or more profiles along a path.

-   <img alt="" src=images/Part_Section.svg  style="width:32px;"> [Section](Part_Section.md): Creates a section by intersecting an object with a section plane.

-   <img alt="" src=images/Part_CrossSections.svg  style="width:32px;"> [Cross sections\...](Part_CrossSections.md): Creates one or more cross-sections through an object.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Part_CompOffsetTools.png  style="width:48px;"> [Offset tools](Part_CompOffsetTools.md):
    -   <img alt="" src=images/Part_Offset.png  style="width:32px;"> [3D Offset](Part_Offset.md): 根据原始几何形状在特定的距离处构建一个平行的副本。
    -   <img alt="" src=images/Part_Offset2D.png  style="width:32px;"> [2D Offset](Part_Offset2D.md): 根据原始连线在特定的距离处创建一个平行的副本，或者缩放一个平面端面。(v0.17)


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Part_Thickness.png  style="width:32px;"> [Thickness](Part_Thickness.md): 镂空一个实体，在选中的面上留下开口。


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Part_ProjectionOnSurface.png  style="width:32px;"> [Projection on surface](Part_ProjectionOnSurface.md): 向表面上投影logo、文本或任意表面、连线、边。可以为投影部分创建一个示例或连线。(v0.19)


</div>

-   <img alt="" src=images/Part_EditAttachment.svg  style="width:32px;"> [Attachment](Part_EditAttachment.md): Attaches an object to another object.

### Boolean

These tools perform boolean operations.

-   <img alt="" src=images/Part_CompCompoundTools.png  style="width:48px;"> [Compound Tools](Part_CompCompoundTools.md):
    -   <img alt="" src=images/Part_Compound.svg  style="width:32px;"> [Make compound](Part_Compound.md): Creates a compound from the selected objects.
    -   <img alt="" src=images/Part_ExplodeCompound.svg  style="width:32px;"> [Explode Compound](Part_ExplodeCompound.md): Splits up compounds.
    -   <img alt="" src=images/Part_Compound‏‎Filter.svg  style="width:32px;"> [Compound Filter](Part_Compound‏‎Filter.md): Extracts the individual pieces from compounds.

-   <img alt="" src=images/Part_Boolean.svg  style="width:32px;"> [Boolean](Part_Boolean.md): 在对象上执行布尔运算

-   <img alt="" src=images/Part_Cut.svg  style="width:32px;"> [Cut](Part_Cut.md): Cuts (subtracts) one object from another.

-   <img alt="" src=images/Part_Fuse.svg  style="width:32px;"> [Fuse](Part_Fuse.md): Fuses (unions) two objects.

-   <img alt="" src=images/Part_Common.svg  style="width:32px;"> [Common](Part_Common.md): Extracts the common (intersection) part of two objects.

-   <img alt="" src=images/Part_CompJoinFeatures.png  style="width:48px;"> [Join features](Part_CompJoinFeatures.md):
    -   <img alt="" src=images/Part_JoinConnect.svg  style="width:32px;"> [Connect](Part_JoinConnect.md): Connects interiors of walled objects.
    -   <img alt="" src=images/Part_JoinEmbed.svg  style="width:32px;"> [Embed](Part_JoinEmbed.md): Embeds a walled object into another walled object.
    -   <img alt="" src=images/Part_JoinCutout.svg  style="width:32px;"> [Cutout](Part_JoinCutout.md): Creates a cutout in a wall of an object for another walled object.

-   <img alt="" src=images/Part_CompSplittingTools.png  style="width:48px;"> [Splitting tools](Part_CompSplittingTools.md):
    -   <img alt="" src=images/Part_BooleanFragments.svg  style="width:32px;"> [Boolean fragments](Part_BooleanFragments.md): Creates all pieces obtained from Boolean operations.
    -   <img alt="" src=images/Part_SliceApart.svg  style="width:32px;"> [Slice apart](Part_SliceApart.md): Slices and splits an object by intersecting it with other objects.
    -   <img alt="" src=images/Part_Slice.svg  style="width:32px;"> [Slice](Part_Slice.md): Slices an object by intersecting it with other objects.
    -   <img alt="" src=images/Part_XOR.svg  style="width:32px;"> [XOR](Part_XOR.md): Removes space shared by an even number of objects.

### Measure

-   <img alt="" src=images/Part_Measure_Linear.svg  style="width:32px;"> [Measure Linear](Part_Measure_Linear.md): Creates a linear measurement.

-   <img alt="" src=images/Part_Measure_Angular.svg  style="width:32px;"> [Measure Angular](Part_Measure_Angular.md): Creates an angular measurement.

-   <img alt="" src=images/Part_Measure_Refresh.svg  style="width:32px;"> [Measure Refresh](Part_Measure_Refresh.md): Updates all measurements.

-   <img alt="" src=images/Part_Measure_Clear_All.svg  style="width:32px;"> [Clear All](Part_Measure_Clear_All.md): Clears all measurements.

-   <img alt="" src=images/Part_Measure_Toggle_All.svg  style="width:32px;"> [Toggle All](Part_Measure_Toggle_All.md): Shows or hides all measurements.

-   <img alt="" src=images/Part_Measure_Toggle_3D.svg  style="width:32px;"> [Toggle 3D](Part_Measure_Toggle_3D.md): Shows or hides 3D measurements.

-   <img alt="" src=images/Part_Measure_Toggle_Delta.svg  style="width:32px;"> [Toggle Delta](Part_Measure_Toggle_Delta.md): Shows or hides delta measurements.


<div class="mw-translate-fuzzy">

### 其他工具


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Part_Import.svg  style="width:32px;"> [Import](Part_Import/zh-cn.md): 您可利用此工具为当前文档添加\*.IGES、\*.STEP、\*.BREP文档。


</div>

-   <img alt="" src=images/Part_Export.svg  style="width:32px;"> [Export](Part_Export.md): Exports to \*.IGES, \*.STEP, or \*.BREP files.

-   <img alt="" src=images/Part_BoxSelection.svg  style="width:32px;"> [Box selection](Part_BoxSelection.md): Selects faces from a rectangular area.

-   <img alt="" src=images/Part_ShapeFromMesh.svg  style="width:32px;"> [Shape from Mesh](Part_ShapeFromMesh.md): Creates a shape object from a mesh object.

-   <img alt="" src=images/Part_PointsFromMesh.svg  style="width:32px;"> [Points from mesh](Part_PointsFromMesh.md): Creates a shape object made of points from a mesh object. <small>(v0.19)</small> 

-   <img alt="" src=images/Part_MakeSolid.svg  style="width:32px;"> [Convert to solid](Part_MakeSolid.md): Converts a shape object to a solid object.

-   <img alt="" src=images/Part_ReverseShapes.svg  style="width:32px;"> [Reverse shapes](Part_ReverseShapes.md): Flips the normals of all faces of selected objects.

-   Create a copy:
    -   <img alt="" src=images/Part_SimpleCopy‎.svg  style="width:32px;"> [Create simple copy](Part_SimpleCopy.md): Creates a simple copy of a selected object.
    -   <img alt="" src=images/Part_TransformedCopy.svg  style="width:32px;"> [Create transformed copy](Part_TransformedCopy.md): Creates a transformed copy of a selected object. <small>(v0.19)</small> 
    -   <img alt="" src=images/Part_ElementCopy.svg  style="width:32px;"> [Create shape element copy](Part_ElementCopy.md): Creates a copy from an element (vertex, edge, face) of a selected object. <small>(v0.19)</small> 
    -   <img alt="" src=images/Part_RefineShape.svg  style="width:32px;"> [Refine shape](Part_RefineShape.md): Cleans faces by removing unnecessary lines.

-   <img alt="" src=images/Part_CheckGeometry.svg  style="width:32px;"> [Check geometry](Part_CheckGeometry.md): Checks the geometry of selected objects for errors.

-   <img alt="" src=images/Part_Defeaturing.svg  style="width:32px;"> [Defeaturing](Part_Defeaturing.md): Removes features from an object.

### Context menu items 

-   <img alt="" src=images/Std_SetAppearance.svg  style="width:32px;"> [Appearance](Std_SetAppearance.md): Determines the appearance of a whole object (color, transparency etc.).

-   <img alt="" src=images/Part_FaceColors.svg  style="width:32px;"> [Set colors](Part_FaceColors.md): Assigns colors to individual faces of objects.

## 首选项


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Preferences-import-export.svg  style="width:32px;"> [Preference \...](Import_Export_Preferences.md) 导入 导出


</div>

## 脚本


<div class="mw-translate-fuzzy">


**参见:**

[零件脚本](Part_scripting.md)


</div>


<div class="mw-translate-fuzzy">

## 教程

-   [从STL或OBJ文件中导入数据](Import_from_STL_or_OBJ.md) : 如何在FreeCAD中导入STL/OBJ文件。
-   [导出STL或OBJ文件](Export_to_STL_or_OBJ.md) : 如何从FreeCAD中导出STL/OBJ文件
-   [Whiffle球教程](Whiffle_Ball_tutorial.md) : 如何使用零件模块


</div>

-   [Import from STL or OBJ](Import_from_STL_or_OBJ.md) : How to import STL/OBJ files in FreeCAD
-   [Export to STL or OBJ](Export_to_STL_or_OBJ.md) : How to export STL/OBJ files from FreeCAD
-   [Whiffle Ball tutorial](Whiffle_Ball_tutorial.md) : How to use the Part Module



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > [Part](Part_Workbench.md) > Part Module/zh-cn
