# Manual:All workbenches at a glance/zh-cn
{{Manual:TOC/zh-cn}}


<div class="mw-translate-fuzzy">

FreeCAD 的新用户面临的一个最大困难，是不知道在哪个工作台中找到某个特定工具。下面的表中是最重要的工作台及其工具。更完整的列表，请参阅 FreeCAD 文档中的每个[工作台的页面](Workbenches.md)。


</div>

四个工作台设计成了结对工作，其中一个完全包含在另一个中。Arch 包含所有的 Draft 工具，PartDesign 包含所有的 Sketcher 工具。但是为清楚起见，下面分开来讲。

### Part

Part 工作台提供了处理实体零件的基本工具：基础几何体，例如立方体和球体，以及简单的几何运算和布尔运算。作为与 [OpenCasCade](https://en.wikipedia.org/wiki/Open_Cascade_Technology) 的主要锚点，Part 工作台提供了 FreeCAD 几何系统的基础设施，几乎所有其他工作台都生成基于 Part 的几何对象。


<div class="mw-translate-fuzzy">

  工具                                                                                                               说明                                               工具                                                                                                                               说明
  ------------------------------------------------------------------------------------------------------------------ -------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------
  <img alt="" src=images/Part_Box.png  style="width:32px;"> _                                                    绘制圆锥
  <img alt="" src=images/Part_Cylinder.png  style="width:32px;"> _                                            绘制球体
  <img alt="" src=images/Part_Torus.png  style="width:32px;"> _   创建各种其他参数化的几何图元
  <img alt="" src=images/Part_Shapebuilder.png  style="width:32px;"> _                                                熔合 (合并) 两个对象
  <img alt="" src=images/Part_Common.png  style="width:32px;"> _                                                        从另一个对象中剪切（减去）一个对象
  <img alt="" src=images/Part_JoinConnect.png  style="width:32px;"> _                                将围墙物体对象嵌入另一个围墙物体对象中
  <img alt="" src=images/Part_JoinCutout.png  style="width:32px;"> _                                        拉伸对象的一个平面
  <img alt="" src=images/Part_Fillet.png  style="width:32px;"> _                                        围绕轴旋转对象（非实体）来创建一个实体对象
  <img alt="" src=images/Part_Section.png  style="width:32px;"> _                    沿对象的一个方向创建多个横截面
  <img alt="" src=images/Part_Chamfer.png  style="width:32px;"> _                                            相对给定镜像平面镜像选定对象
  <img alt="" src=images/Part_RuledSurface.png  style="width:32px;"> _                                                沿路径扫略一个或多个轮廓
  <img alt="" src=images/Part_Loft.png  style="width:32px;"> _                                            创建原始对象的缩放过的副本
  <img alt="" src=images/Part_Thickness.png  style="width:32px;"> [Thickness](Part_Thickness.md)                为形状的面指定厚度                                                                                                                                                                    


</div>

### Draft

Draft 工作台提供了执行基本 2D CAD 绘图任务的工具：直线，圆圈，等等，以及一些通用的便捷工具，例如移动，旋转和缩放，另外还提供了几种绘图辅助工具，例如网格和捕捉。Draft 工作台主要用于绘制Arch 对象的引导线，但是也可以当作 FreeCAD 的"瑞士军刀"。


<div class="mw-translate-fuzzy">

  工具                                                                                                                    描述                                            工具                                                                                                               描述
  ----------------------------------------------------------------------------------------------------------------------- ----------------------------------------------- ------------------------------------------------------------------------------------------------------------------ ------------------------------------------------------------------
  <img alt="" src=images/Draft_Line.png  style="width:32px;"> _                                 绘制由多个线段组成的线（折线）
  <img alt="" src=images/Draft_Circle.png  style="width:32px;"> _                                     以中心，半径，起始角度和结束角度绘制弧段
  <img alt="" src=images/Draft_Ellipse.png  style="width:32px;">_                     以中心和半径绘制正多边形
  <img alt="" src=images/Draft_Rectangle.png  style="width:32px;"> _                                 绘制多行文本注释
  <img alt="" src=images/Draft_Dimension.png  style="width:32px;"> _                     以一系列的点绘制 B 样条曲线
  <img alt="" src=images/Draft_Point.png  style="width:32px;"> _     ShapeString 工具在当前文档的给定点处插入表示文本字符串的复合形状
  <img alt="" src=images/Draft_Facebinder.png  style="width:32px;"> _             以一系列的点绘制贝塞尔曲线
  <img alt="" src=images/Draft_Move.png  style="width:32px;"> _                         围绕某点旋转对象一定角度
  <img alt="" src=images/Draft_Offset.png  style="width:32px;"> _                         修剪，延伸或拉伸物体
  <img alt="" src=images/Draft_Upgrade.png  style="width:32px;"> _             将对象转换或分离为较低级别的对象
  <img alt="" src=images/Draft_Scale.png  style="width:32px;"> _   创建一个 2D 对象，它是另一个对象的扁平视图
  <img alt="" src=images/Draft_Draft2Sketch.png  style="width:32px;"> _                             将对象创建为极坐标阵列或矩形阵列
  <img alt="" src=images/Draft_PathArray.png  style="width:32px;"> _                             为对象创建带链接的副本
  <img alt="" src=images/Draft_Mirror.png  style="width:32px;"> [Mirror](Draft_Mirror.md)                              沿一条线镜像对象                                                                                                                                                   


</div>

### Sketcher

Sketcher 工作台包含用于构建和编辑复杂 2D 对象的工具，称为草图(sketch)。这些草图内的几何形状可以通过使用约束来精确地定位和关联。这些草图(sketch)对象主要是 PartDesign 几何体的构建模块，但在 FreeCAD 各处都有用。


<div class="mw-translate-fuzzy">

  工具                                                                                                                                                            描述                                                                             工具                                                                                                                                                      描述
  --------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------
  <img alt="" src=images/Sketcher_CreatePoint.png  style="width:32px;"> _                                                         以 2 个点绘制线段
  <img alt="" src=images/Sketcher_Arc.png  style="width:32px;"> _                      以两个端点和圆周上的另一个点绘制弧段
  <img alt="" src=images/Sketcher_Circle.png  style="width:32px;"> _         以圆周上的三个点绘制一个圆
  <img alt="" src=images/Sketcher_CreateEllipse.png  style="width:32px;"> _   根据大直径（2 点）和小半径点绘制椭圆
  <img alt="" src=images/Sketcher_CreateArcOfEllipse.png  style="width:32px;"> _                             绘制由多个线段组成的线，有多种绘图模式
  <img alt="" src=images/Sketcher_CreateRectangle.png  style="width:32px;"> _                             绘制圈在构造几何圆中的正三角形
  <img alt="" src=images/Sketcher_CreateSquare.png  style="width:32px;"> _                             绘制圈在构造几何圆中的正五边形
  <img alt="" src=images/Sketcher_CreateHexagon.png  style="width:32px;"> _                             绘制圈在构造几何圆中的正七边形
  <img alt="" src=images/Sketcher_CreateOctagon.png  style="width:32px;"> _                                             通过选择一个半圆的中心和另一个半圆的端点绘制一个长腰孔
  <img alt="" src=images/Sketcher_CreateFillet.png  style="width:32px;"> _                                               相对于选定点，修剪直线，圆或圆弧
  <img alt="" src=images/Sketcher_External.png  style="width:32px;"> _        切换元素是否处于构造模式。构造对象不会用于 3D 几何操作，只有在编辑包含它的 Sketch 时才可见。
  <img alt="" src=images/Constraint_PointOnPoint.png  style="width:32px;"> _            将点绑定到另一个对象（例如直线，圆弧或轴线）上。
  <img alt="" src=images/Constraint_Vertical.png  style="width:32px;"> _                          将选定的线或折线元素约束到真正的水平方向。在应用此约束之前，可以选择多个对象。
  <img alt="" src=images/Constraint_Parallel.png  style="width:32px;"> _              约束两条线彼此垂直，或约束线在弧的端点与弧垂直。
  <img alt="" src=images/Constraint_Tangent.png  style="width:32px;"> _                           约束两个选定实体彼此相等。如果在圆或弧上使用，则它们的半径将设置为相等。
  <img alt="" src=images/Constraint_Symmetric.png  style="width:32px;"> _                                    通过设置相对于原点的垂直和水平距离来约束所选对象，从而锁定它的位置。
  <img alt="" src=images/Constraint_HorizontalDistance.png  style="width:32px;"> _        指定两点或线段端点之间的竖直距离。如果仅选择了一个对象，则设置为与原点的距离。
  <img alt="" src=images/Constraint_Length.png  style="width:32px;"> _                                          通过约束半径来定义选定圆弧或圆的半径。
  <img alt="" src=images/Constraint_InternalAngle.png  style="width:32px;"> _                           约束两条线以遵守折射定律来模拟通过界面的光
  <img alt="" src=images/Constraint_InternalAlignment.png  style="width:32px;"> _                                          将草图映射到先前选定的实体的面
  <img alt="" src=images/Sketcher_MergeSketch.png  style="width:32px;"> _                                     镜像某草图中选定的元素


</div>

### Part Design 

Part Design 工作台包含用于构建实体零件的高级工具，还包含 Sketcher 中的所有工具。由于Part Design 工作台只能生成实体形状（Part Design的第一规则），因此在设计用于制造的部品或用于 3D 打印的零件时，Part Design 是主工作台，您将始终获得可打印的对象。


<div class="mw-translate-fuzzy">

  工具                                                                                                                                     描述                               工具                                                                                                                                        描述
  ---------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------
  <img alt="" src=images/PartDesign_Pad.png  style="width:32px;"> _                                   用选定的草图创建一个凹坑。草图必须贴附于现有实体对象的面
  <img alt="" src=images/PartDesign_Revolution.png  style="width:32px;"> _                                   通过围绕轴旋转草图来创建凹槽
  <img alt="" src=images/PartDesign_Fillet.png  style="width:32px;"> _                               给对象的边缘做倒角
  <img alt="" src=images/PartDesign_Draft.png  style="width:32px;"> _                           相对于平面或表面镜像某些特征
  <img alt="" src=images/PartDesign_LinearPattern.png  style="width:32px;"> _          创建特征的极坐标阵列
  <img alt="" src=images/PartDesign_Scaled.png  style="width:32px;"> _   允许使用其他变换的任意组合创建模式
  <img alt="" src=images/PartDesign_WizardShaft.png  style="width:32px;"> _   创建多种类型的齿轮


</div>

### Arch

Arch 工作台包含用于处理 [BIM](https://en.wikipedia.org/wiki/Building_information_modeling) 项目（土木工程和建筑）的工具，还包含 Draft 工作台中的所有工具。Arch 工作台的主要用途是创建 BIM 对象或为使用其他工作台构建的对象提供 BIM 属性，以便导出到[IFC](https://en.wikipedia.org/wiki/Industry_Foundation_Classes) 里。


<div class="mw-translate-fuzzy">

  Tool                                                                                                  Description                            Tool                                                                                                               Description
  ----------------------------------------------------------------------------------------------------- -------------------------------------- ------------------------------------------------------------------------------------------------------------------ --------------------------------------------
  <img alt="" src=images/Arch_Wall.png  style="width:32px;"> _                从头开始创建结构元素或使用选定对象作为基础
  <img alt="" src=images/Arch_Rebar.png  style="width:32px;"> _                                创建包含所选对象的楼板
  <img alt="" src=images/Arch_Building.png  style="width:32px;"> _                                    创建包含所选对象的场地
  <img alt="" src=images/Arch_Window.png  style="width:32px;"> _   将截面平面对象添加到文档中
  <img alt="" src=images/Arch_Axis.png  style="width:32px;"> _                                    以选定的面创建倾斜屋顶
  <img alt="" src=images/Arch_Space.png  style="width:32px;"> _                            在文档中创建阶梯对象
  <img alt="" src=images/Arch_Panel.png  style="width:32px;"> _                                从选定的布局创建框架对象
  <img alt="" src=images/Arch_Equipment.png  style="width:32px;"> _           将材质属性赋予选定对象
  <img alt="" src=images/Arch_Schedule.png  style="width:32px;"> _                   根据计划切割对象
  <img alt="" src=images/Arch_Add.png  style="width:32px;"> _                            从组件中减去或删除对象
  <img alt="" src=images/Arch_Survey.png  style="width:32px;"> [Survey](Arch_Survey.md)               进入或离开调查模式                                                                                                                                        


</div>

### Drawing


<div class="mw-translate-fuzzy">

Drawing 工作台处理 2D 工程图纸的创建和操作，用于在 2D 平面上显示 3D 工作成果。然后，可以将这些图纸 SVG 或 DXF 格式，用其它 2D 应用程序打开，也可导出为 PDF 文件，或者打印出来。


</div>

The Drawing Workbench handles the creation and manipulation of 2D drawing sheets, used for displaying views of your 3D work in 2D. These sheets can then be exported to 2D applications in SVG or DXF formats, to a PDF file or printed.


<div class="mw-translate-fuzzy">

  工具                                                                                                                    描述                                          工具                                                                                                                描述
  ----------------------------------------------------------------------------------------------------------------------- --------------------------------------------- ------------------------------------------------------------------------------------------------------------------- ----------------------------------------
  <img alt="" src=images/Drawing_Landscape_A3.png  style="width:32px;"> _                            在活动图纸中插入所选对象的视图
  <img alt="" src=images/Drawing_Annotation.png  style="width:32px;"> _                            将剪辑组添加到当前图纸（？）
  <img alt="" src=images/Drawing_Openbrowser.png  style="width:32px;"> _   在当前工程图纸上自动创建对象的正交视图
  <img alt="" src=images/Drawing_Symbol.png  style="width:32px;"> _       在当前图纸中插入所选对象的特殊草稿视图
  <img alt="" src=images/Drawing_Save.png  style="width:32px;"> [Save](Drawing_Save.md)                                将当前工作表保存为 SVG 文件                                                                                                                                       


</div>

### 其他内置工作台

上面概括介绍了 FreeCAD 最重要的几个工具，但还有更多工作台可用，包括：


<div class="mw-translate-fuzzy">

-   [Mesh 工作台](Mesh_Workbench.md) 允许使用[多边形网格](https://en.wikipedia.org/wiki/Polygon_mesh)。由于缺乏精度和对曲线的支持，网格不是 FreeCAD 首选的几何体类型，但是网格仍然有很多用途，并且在 FreeCAD 中完全支持。Mesh 工作台还提供了许多 Part-to-Mesh 和 Mesh-to-Part 的工具。
-   [Raytracing 工作台提供了与外部渲染器](Raytracing_Workbench.md)（如 povray 或 luxrender）连接的工具。这个工作台允许您在 FreeCAD 内，从模型生成高质量的渲染图。
-   [Spreadsheet 工作台创建和操作电子表格数据](Spreadsheet_Workbench.md)，这些数据可以从 FreeCAD 模型中提取。你也可以在FreeCAD的许多区域中引用电子表格单元格，可以将它们用作主数据结构。
-   [FEM 工作台处理](FEM_Workbench.md)[有限元分析](https://en.wikipedia.org/wiki/Finite_element_method)，执行预处理和后处理 FEM 计算，以图形方式显示结果。


</div>

### 外部工作台

还有 FreeCAD 社区成员做出的许多非常有用的工作台。虽然这些工作台不包含在标准 FreeCAD 安装包中，但很容易作为插件安装它们。在 [FreeCAD-addons](https://github.com/FreeCAD/FreeCAD-addons) 存储库中引用了这些工作台。其中发展最完整的是：


<div class="mw-translate-fuzzy">

-   [Drawing Dimensioning 工作台](https://github.com/hamish2014/FreeCAD_drawing_dimensioning)提供了许多新工具，可以直接在图纸上工作，并允许您添加尺寸，注释和其他技术符号，可以很好地控制它们的外观。
-   [Fasteners 工作台](https://github.com/shaise/FreeCAD_FastenersWB)提供各种即插即用的紧固件，如螺钉，螺栓，杆，垫圈和螺母。有许多选项和设置可供选择。
-   [Assembly2 工作台](https://github.com/hamish2014/FreeCAD_assembly2)提供了一系列用于装配和使用[装配](https://en.wikipedia.org/wiki/Assembly_modelling)体的工具。


</div>

**延伸阅读**


<div class="mw-translate-fuzzy">

-   [完整的工作台列表](Workbenches.md)
-   [Part 工作台](Part_Workbench.md)
-   [Draft 工作台](Draft_Workbench.md)
-   [Sketcher and Part Design 工作台](PartDesign_Workbench.md)
-   [Arch 工作台](Arch_Workbench.md)
-   [Drawing 工作台](Drawing_Workbench.md)
-   [FEM 工作台](FEM_Workbench.md)
-   [FreeCAD-addons 存储库](https://github.com/FreeCAD/FreeCAD-addons)


</div>

---
[documentation index](../README.md) > Manual:All workbenches at a glance/zh-cn
