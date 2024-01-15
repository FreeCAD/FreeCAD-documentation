# Manual:All workbenches at a glance/zh-cn
{{Manual:TOC}}

对于 FreeCAD 的新用户来说，最大的困难之一是要知道在哪个工作台中找到特定的工具。下表将为您提供最重要的工作台及其工具的概述。请参考 FreeCAD 文档中每个工作台页面以获取更完整的列表。

其中四个工作台也是成对设计的，其中一个完全包含在另一个工作台中：Arch 包含所有 Draft 工具，而PartDesign 包含所有 Sketcher 工具。然而，为了清晰起见，它们在下面是分开列出的。

### Part

Part 工作台提供了处理实体零件的基本工具：原始几何体，例如立方体和球体，以及简单的几何操作和布尔操作。作为与 OpenCasCade（开放级联技术）的主要锚点，Part 工作台为 FreeCAD 的几何系统提供了基础，并且几乎所有其他工作台都会生成基于 Part 的几何体。

  工具                                                                                                      描述                                                 工具                                                                                                       描述
     
  <img alt="" src=images/Part_Box.svg  style="width:32px;"> [盒子](Part_Box.md)                                  绘制一个盒子                                         <img alt="" src=images/Part_Cone.svg  style="width:32px;"> [圆锥](Part_Cone.md)                                绘制一个圆锥
  <img alt="" src=images/Part_Cylinder.svg  style="width:32px;"> [圆柱](Part_Cylinder.md)                   绘制一个圆柱                                         <img alt="" src=images/Part_Sphere.svg  style="width:32px;"> [球体](Part_Sphere.md)                          绘制一个球体
  <img alt="" src=images/Part_Torus.svg  style="width:32px;"> [环面](Part_Torus.md)                            绘制一个环面（圆环）                                 <img alt="" src=images/Part_Primitives.svg  style="width:32px;"> [创建基本几何体](Part_Primitives.md)    创建其他各种参数几何体
  <img alt="" src=images/Part_Builder.svg  style="width:32px;"> [形状生成器](Part_Builder.md)                从基本几何体创建更复杂的形状                         <img alt="" src=images/Part_Fuse.svg  style="width:32px;"> [合并](Part_Fuse.md)                                合并（联合）两个对象
  <img alt="" src=images/Part_Common.svg  style="width:32px;"> [共同部分](Part_Common.md)                     提取两个对象的共同（交集）部分                       <img alt="" src=images/Part_Cut.svg  style="width:32px;"> [切割](Part_Cut.md)                                   从一个对象中切割（减去）另一个对象
  <img alt="" src=images/Part_JoinConnect.svg  style="width:32px;"> [连接](Part_JoinConnect.md)          连接围合对象的内部空间                               <img alt="" src=images/Part_JoinEmbed.svg  style="width:32px;"> [嵌入连接](Part_JoinEmbed.md)             将一个围合对象嵌入到另一个围合对象中
  <img alt="" src=images/Part_JoinCutout.svg  style="width:32px;"> [切割连接](Part_JoinCutout.md)         在对象的墙壁上创建一个切割，用于放置另一个围合对象   <img alt="" src=images/Part_Extrude.svg  style="width:32px;"> [拉伸](Part_Extrude.md)                       拉伸对象的平面面片
  <img alt="" src=images/Part_Fillet.svg  style="width:32px;"> [圆角](Part_Fillet.md)                         圆角化对象的边缘                                     <img alt="" src=images/Part_Revolve.svg  style="width:32px;"> [旋转](Part_Revolve.md)                       围绕轴线旋转一个对象（非实体），创建一个实体
  <img alt="" src=images/Part_Section.svg  style="width:32px;"> [剖面](Part_Section.md)                      使用剖面平面与对象相交，创建一个剖面                 <img alt="" src=images/Part_CrossSections.svg  style="width:32px;"> [横截面](Part_CrossSections.md)   沿着对象创建多个横截面
  <img alt="" src=images/Part_Chamfer.svg  style="width:32px;"> [倒角](Part_Chamfer.md)                      倒角化对象的边缘                                     <img alt="" src=images/Part_Mirror.svg  style="width:32px;"> [镜像](Part_Mirror.md)                          在给定的镜像平面上镜像选定的对象
  <img alt="" src=images/Part_RuledSurface.svg  style="width:32px;"> [生成曲面](Part_RuledSurface.md)   在选定的曲线之间创建生成曲面                         <img alt="" src=images/Part_Sweep.svg  style="width:32px;"> [扫描](Part_Sweep.md)                             沿着路径扫描一个或多个剖面
  <img alt="" src=images/Part_Loft.svg  style="width:32px;"> [放样](Part_Loft.md)                               从一个剖面放样到另一个剖面                           <img alt="" src=images/Part_Offset.svg  style="width:32px;"> [偏移](Part_Offset.md)                          创建原始对象的缩放副本
  <img alt="" src=images/Part_Thickness.svg  style="width:32px;"> [厚度](Part_Thickness.md)                为形状的面片赋予厚度                                                                                                                                            

### Draft

Draft 工作台提供基本的 2D CAD 绘图工具，如直线、圆等，以及一系列通用的便捷工具，如移动、旋转或缩放。它还提供了几种绘图辅助功能，如网格和捕捉。它主要用于绘制 Arch 对象的指引线，但也可以作为FreeCAD 的\"瑞士军刀\"使用。

  工具                                                                                                         描述                                     工具                                                                                                          描述
     
  <img alt="" src=images/Draft_Line.svg  style="width:32px;"> [直线](Draft_Line.md)                               在两点之间绘制一条线段                   <img alt="" src=images/Draft_Wire.svg  style="width:32px;"> [线段](Draft_Wire.md)                                绘制由多条线段（折线）组成的线段
  <img alt="" src=images/Draft_Circle.svg  style="width:32px;"> [圆](Draft_Circle.md)                           从中心和半径绘制一个圆                   <img alt="" src=images/Draft_Arc.svg  style="width:32px;"> [弧线](Draft_Arc.md)                                   从中心、半径、起始角度和终止角度绘制一个弧线段
  <img alt="" src=images/Draft_Ellipse.svg  style="width:32px;">[椭圆](Draft_Ellipse.md)                       从两个角点绘制一个椭圆                   <img alt="" src=images/Draft_Polygon.svg  style="width:32px;"> [多边形](Draft_Polygon.md)                     从中心和半径绘制一个正多边形
  <img alt="" src=images/Draft_Rectangle.svg  style="width:32px;"> [矩形](Draft_Rectangle.md)                从两个对角点绘制一个矩形                 <img alt="" src=images/Draft_Text.svg  style="width:32px;"> [文本](Draft_Text.md)                                绘制多行文本注释
  <img alt="" src=images/Draft_Dimension.svg  style="width:32px;"> [标注](Draft_Dimension.md)                绘制一个尺寸标注                         <img alt="" src=images/Draft_BSpline.svg  style="width:32px;"> [B 样条曲线](Draft_BSpline.md)                 从一系列点绘制 B 样条曲线
  <img alt="" src=images/Draft_Point.svg  style="width:32px;"> [点](Draft_Point.md)                              插入一个单点                             <img alt="" src=images/Draft_ShapeString.svg  style="width:32px;"> [复合图形](Draft_ShapeString.md)       复合图形工具可以在当前文档中的给定点处插入代表文本字符串的复合图形
  <img alt="" src=images/Draft_Facebinder.svg  style="width:32px;"> [面绑定](Draft_Facebinder.md)           从现有对象的选择面创建一个新对象         <img alt="" src=images/Draft_BezCurve.svg  style="width:32px;"> [贝塞尔曲线](Draft_BezCurve.md)              从一系列点绘制贝塞尔曲线
  <img alt="" src=images/Draft_Move.svg  style="width:32px;"> [移动](Draft_Move.md)                               将对象从一个位置移动或复制到另一个位置   <img alt="" src=images/Draft_Rotate.svg  style="width:32px;"> [旋转](Draft_Rotate.md)                          围绕点旋转对象一定角度
  <img alt="" src=images/Draft_Offset.svg  style="width:32px;"> [偏移](Draft_Offset.md)                         将对象偏移到一定距离                     <img alt="" src=images/Draft_Trimex.svg  style="width:32px;"> [修剪、延伸或挤出](Draft_Trimex.md)              修剪、延伸或挤出一个对象
  <img alt="" src=images/Draft_Upgrade.svg  style="width:32px;"> [升级](Draft_Upgrade.md)                      将或连接对象转换为更高级别的对象         <img alt="" src=images/Draft_Downgrade.svg  style="width:32px;"> [降级](Draft_Downgrade.md)                 将或分离对象转换为较低级别的对象
  <img alt="" src=images/Draft_Scale.svg  style="width:32px;"> [缩放](Draft_Scale.md)                            相对于一个点缩放对象                     <img alt="" src=images/Draft_Shape2DView.svg  style="width:32px;"> [形状 2D 视图](Draft_Shape2DView.md)   创建一个二维对象，它是另一个对象的平面视图
  <img alt="" src=images/Draft_Draft2Sketch.svg  style="width:32px;"> [草图转换](Draft_Draft2Sketch.md)   将草图对象转换为草图或反之               <img alt="" src=images/Draft_OrthoArray.svg  style="width:32px;"> [矩形阵列](Draft_OrthoArray.md)          从一个对象创建一个矩形阵列
  <img alt="" src=images/Draft_Clone.svg  style="width:32px;"> [复制](Draft_Clone.md)                            创建对象的链接副本                       <img alt="" src=images/Draft_Mirror.svg  style="width:32px;"> [镜像](Draft_Mirror.md)                          沿一条线镜像对象

### Sketcher

Sketcher 工作台包含用于构建和编辑复杂 2D 对象的工具，称为草图(sketch)。这些草图内的几何形状可以通过使用约束来精确地定位和关联。这些草图(sketch)对象主要是 PartDesign 几何体的构建模块，但在 FreeCAD 各处都有用。


<div class="mw-translate-fuzzy">

  工具                                                                                                                                                   描述                                                                             工具                                                                                                                                                  描述
     
  <img alt="" src=images/Sketcher_CreatePoint.png  style="width:32px;"> [Point](Sketcher_CreatePoint.md)                                          画出一点                                                                         <img alt="" src=images/Sketcher_Line.png  style="width:32px;"> [Line](Sketcher_CreateLine.md)                                                         以 2 个点绘制线段
  <img alt="" src=images/Sketcher_Arc.png  style="width:32px;"> [Arc](Sketcher_CreateArc.md)                                                              以中心，半径，起始角度和结束角度绘制弧段                                         <img alt="" src=images/Sketcher_CreateArc3Point.png  style="width:32px;"> [Arc 3 points](Sketcher_Create3PointArc.md)                      以两个端点和圆周上的另一个点绘制弧段
  <img alt="" src=images/Sketcher_Circle.png  style="width:32px;"> [Circle](Sketcher_CreateCircle.md)                                                  以中心和半径绘制一个圆                                                           <img alt="" src=images/Sketcher_CreateCircle3Point.png  style="width:32px;"> [ Circle 3 points](Sketcher_Create3PointCircle.md)         以圆周上的三个点绘制一个圆
  <img alt="" src=images/Sketcher_CreateEllipse.png  style="width:32px;"> [Ellipse](Sketcher_CreateEllipseByCenter.md)                          按中心点，主要半径点和小半径点绘制椭圆                                           <img alt="" src=images/Sketcher_CreateEllipse3Point.png  style="width:32px;"> [Ellipse 3 points](Sketcher_CreateEllipseBy3Points.md)   根据大直径（2 点）和小半径点绘制椭圆
  <img alt="" src=images/Sketcher_CreateArcOfEllipse.png  style="width:32px;"> [Arc of ellipse](Sketcher_CreateArcOfEllipse.md)            按中心点，主要半径点，起点和终点绘制椭圆弧                                       <img alt="" src=images/Sketcher_CreatePolyline.png  style="width:32px;"> [Polyline](Sketcher_CreatePolyline.md)                             绘制由多个线段组成的线，有多种绘图模式
  <img alt="" src=images/Sketcher_CreateRectangle.png  style="width:32px;"> [Rectangle](Sketcher_CreateRectangle.md)                          以 2 个相对的点绘制一个矩形                                                      <img alt="" src=images/Sketcher_CreateTriangle.png  style="width:32px;"> [Triangle](Sketcher_CreateTriangle.md)                             绘制圈在构造几何圆中的正三角形
  <img alt="" src=images/Sketcher_CreateSquare.png  style="width:32px;"> [Square](Sketcher_CreateSquare.md)                                      绘制圈在构造几何圆中的正方形                                                     <img alt="" src=images/Sketcher_CreatePentagon.png  style="width:32px;"> [Pentagon](Sketcher_CreatePentagon.md)                             绘制圈在构造几何圆中的正五边形
  <img alt="" src=images/Sketcher_CreateHexagon.png  style="width:32px;"> [Hexagon](Sketcher_CreateHexagon.md)                                  绘制圈在构造几何圆中的正六边形                                                   <img alt="" src=images/Sketcher_CreateHeptagon.png  style="width:32px;"> [Heptagon](Sketcher_CreateHeptagon.md)                             绘制圈在构造几何圆中的正七边形
  <img alt="" src=images/Sketcher_CreateOctagon.png  style="width:32px;"> [Octagon](Sketcher_CreateOctagon.md)                                  绘制圈在构造几何圆中的正八边形                                                   <img alt="" src=images/Sketcher_CreateSlot.png  style="width:32px;"> [Slot](Sketcher_CreateSlot.md)                                             通过选择一个半圆的中心和另一个半圆的端点绘制一个长腰孔
  <img alt="" src=images/Sketcher_CreateFillet.png  style="width:32px;"> [Fillet](Sketcher_CreateFillet.md)                                      在相交于一点的两条线之间制作圆角                                                 <img alt="" src=images/Sketcher_Trimming.png  style="width:32px;"> [Trimming](Sketcher_Trimming.md)                                               相对于选定点，修剪直线，圆或圆弧
  <img alt="" src=images/Sketcher_External.png  style="width:32px;"> [External geometry](Sketcher_External.md)                                       创建链接到外部几何体的边                                                         <img alt="" src=images/Sketcher_ToggleConstruction.png  style="width:32px;"> [Construction mode](Sketcher_ToggleConstruction.md)        切换元素是否处于构造模式。构造对象不会用于 3D 几何操作，只有在编辑包含它的 Sketch 时才可见。
  <img alt="" src=images/Constraint_PointOnPoint.png  style="width:32px;"> [Coincident](Sketcher_ConstrainCoincident_‎.md)                      让一个点固定于（与之重合）一个（或多个已经重合的）其他点上。                     <img alt="" src=images/Constraint_PointOnObject.png  style="width:32px;"> [Point on object](Sketcher_ConstrainPointOnObject.md)            将点绑定到另一个对象（例如直线，圆弧或轴线）上。
  <img alt="" src=images/Constraint_Vertical.png  style="width:32px;"> [Vertical](Sketcher_ConstrainVertical_‎.md)                                  将选定的线或折线元素约束到真正的垂直方向。在应用此约束之前，可以选择多个对象。   <img alt="" src=images/Constraint_Horizontal.png  style="width:32px;"> [Horizontal](Sketcher_ConstrainHorizontal.md)                          将选定的线或折线元素约束到真正的水平方向。在应用此约束之前，可以选择多个对象。
  <img alt="" src=images/Constraint_Parallel.png  style="width:32px;"> [Parallel](Sketcher_ConstrainParallel.md)                                   约束两条或更多条线，彼此平行。                                                   <img alt="" src=images/Constraint_Perpendicular.png  style="width:32px;"> [Perpendicular](Sketcher_ConstrainPerpendicular.md)              约束两条线彼此垂直，或约束线在弧的端点与弧垂直。
  <img alt="" src=images/Constraint_Tangent.png  style="width:32px;"> [Tangent](Sketcher_ConstrainTangent.md)                                       在两个选定实体之间创建相切约束，或在两个线段之间创建共线约束。                   <img alt="" src=images/Constraint_EqualLength.png  style="width:32px;"> [Equal length](Sketcher_ConstrainEqual.md)                           约束两个选定实体彼此相等。如果在圆或弧上使用，则它们的半径将设置为相等。
  <img alt="" src=images/Constraint_Symmetric.png  style="width:32px;"> [Symmetric](Sketcher_ConstrainSymmetric.md)                               相对某线约束两个点对称，或者相对第三个选定点约束前两个选定点对称。               <img alt="" src=images/Sketcher_ConstrainLock.png  style="width:32px;"> [Lock](Sketcher_ConstrainLock.md)                                    通过设置相对于原点的垂直和水平距离来约束所选对象，从而锁定它的位置。
  <img alt="" src=images/Constraint_HorizontalDistance.png  style="width:32px;"> [Horizontal distance](Sketcher_ConstrainDistanceX.md)   指定两点或线段端点之间的水平距离。如果仅选择了一个对象，则设置为与原点的距离。   <img alt="" src=images/Constraint_VerticalDistance.png  style="width:32px;"> [Vertical distance](Sketcher_ConstrainDistanceY.md)        指定两点或线段端点之间的竖直距离。如果仅选择了一个对象，则设置为与原点的距离。
  <img alt="" src=images/Constraint_Length.png  style="width:32px;"> [Distance](Sketcher_ConstrainDistance.md)                                       约束所选线的长度，或约束两个点之间的距离。                                       <img alt="" src=images/Constraint_Radius.png  style="width:32px;"> [Radius](Sketcher_ConstrainRadius.md)                                          通过约束半径来定义选定圆弧或圆的半径。
  <img alt="" src=images/Constraint_InternalAngle.png  style="width:32px;"> [Internal anglr](Sketcher_ConstrainAngle.md)                      定义两条选定线之间的内角。                                                       <img alt="" src=images/Sketcher_MapSketch.png  style="width:32px;"> [Map sketch](Sketcher_MapSketch.md)                                          将草图映射到先前选定的实体的面
  <img alt="" src=images/Sketcher_MergeSketch.png  style="width:32px;"> [Merge](Sketcher_MergeSketches.md)                                        合并两个或多个草图                                                               <img alt="" src=images/Sketcher_MirrorSketch.png  style="width:32px;"> [Mirror](Sketcher_MirrorSketch.md)                                     镜像某草图中选定的元素


</div>

### Part Design 

Part Design 工作台包含用于构建实体零件的高级工具，还包含 Sketcher 中的所有工具。由于Part Design 工作台只能生成实体形状（Part Design的第一规则），因此在设计用于制造的部品或用于 3D 打印的零件时，Part Design 是主工作台，您将始终获得可打印的对象。

  工具                                                                                                                           描述                               工具                                                                                                                              描述
     
  <img alt="" src=images/PartDesign_Pad.svg  style="width:32px;"> [拉伸](PartDesign_Pad.md)                                     从选定的草图拉伸出一个固体对象     <img alt="" src=images/PartDesign_Pocket.svg  style="width:32px;"> [凸台](PartDesign_Pocket.md)                               从选定的草图创建一个凸台，该草图必须映射到现有固体对象的面
  <img alt="" src=images/PartDesign_Revolution.svg  style="width:32px;"> [旋转体](PartDesign_Revolution.md)              围绕轴创建一个实体对象             <img alt="" src=images/PartDesign_Groove.svg  style="width:32px;"> [凹槽](PartDesign_Groove.md)                               围绕轴创建一个凹槽
  <img alt="" src=images/PartDesign_Fillet.svg  style="width:32px;"> [圆角](PartDesign_Fillet.md)                            圆角化对象的边缘                   <img alt="" src=images/PartDesign_Chamfer.svg  style="width:32px;"> [倒角](PartDesign_Chamfer.md)                            对象的边缘倒角
  <img alt="" src=images/PartDesign_Draft.svg  style="width:32px;"> [斜面](PartDesign_Draft.md)                               对对象的面施加角度斜面             <img alt="" src=images/PartDesign_Mirrored.svg  style="width:32px;"> [镜像](PartDesign_Mirrored.md)                         在平面或面上镜像特征
  <img alt="" src=images/PartDesign_LinearPattern.svg  style="width:32px;"> [线性阵列](PartDesign_LinearPattern.md)   创建特征的线性阵列                 <img alt="" src=images/PartDesign_PolarPattern.svg  style="width:32px;"> [极坐标阵列](PartDesign_PolarPattern.md)       创建特征的极坐标阵列
  <img alt="" src=images/PartDesign_Scaled.svg  style="width:32px;"> [比例缩放](PartDesign_Scaled.md)                        将特征缩放到不同的大小             <img alt="" src=images/PartDesign_MultiTransform.svg  style="width:32px;"> [多重变换](PartDesign_MultiTransform.md)   允许创建任何其他变换的组合，并应用于模型的特征
  <img alt="" src=images/PartDesign_WizardShaft.svg  style="width:32px;"> [轴向向导](PartDesign_WizardShaft.md)         从值表生成轴，并允许分析力和力矩   <img alt="" src=images/PartDesign_InvoluteGear.svg  style="width:32px;"> [渐开线齿轮向导](PartDesign_InvoluteGear.md)   允许您创建几种类型的齿轮

### Arch

Arch 工作台包含用于处理 [BIM](https://en.wikipedia.org/wiki/Building_information_modeling) 项目（土木工程和建筑）的工具，还包含 Draft 工作台中的所有工具。Arch 工作台的主要用途是创建 BIM 对象或为使用其他工作台构建的对象提供 BIM 属性，以便导出到[IFC](https://en.wikipedia.org/wiki/Industry_Foundation_Classes) 里。

  工具                                                                                         描述                                       工具                                                                                                      描述
     
  <img alt="" src=images/Arch_Wall.svg  style="width:32px;"> [墙体](Arch_Wall.md)                  从头开始创建墙体或使用选定的对象作为基础   <img alt="" src=images/Arch_Structure.svg  style="width:32px;"> [结构体](Arch_Structure.md)              从头开始创建结构元素或使用选定的对象作为基础
  <img alt="" src=images/Arch_Rebar.svg  style="width:32px;"> [钢筋](Arch_Rebar.md)               在选定的结构元素中创建钢筋加固             <img alt="" src=images/Arch_Floor.svg  style="width:32px;"> [地板](Arch_Floor.md)                            创建包括选定对象的地板
  <img alt="" src=images/Arch_Building.svg  style="width:32px;"> [建筑](Arch_Building.md)      创建包括选定对象的建筑                     <img alt="" src=images/Arch_Site.svg  style="width:32px;"> [场地](Arch_Site.md)                               创建包括选定对象的场地
  <img alt="" src=images/Arch_Window.svg  style="width:32px;"> [窗户](Arch_Window.md)            使用选定对象作为基础创建窗户               <img alt="" src=images/Arch_SectionPlane.svg  style="width:32px;"> [剖面平面](Arch_SectionPlane.md)   将剖面平面对象添加到文档中
  <img alt="" src=images/Arch_Axis.svg  style="width:32px;"> [轴线系统](Arch_Axis.md)              向文档添加轴线系统                         <img alt="" src=images/Arch_Roof.svg  style="width:32px;"> [屋顶](Arch_Roof.md)                               从选定的面创建倾斜的屋顶
  <img alt="" src=images/Arch_Space.svg  style="width:32px;"> [空间](Arch_Space.md)               在文档中创建空间对象                       <img alt="" src=images/Arch_Stairs.svg  style="width:32px;"> [楼梯](Arch_Stairs.md)                         在文档中创建楼梯对象
  <img alt="" src=images/Arch_Panel.svg  style="width:32px;"> [面板](Arch_Panel.md)               从选定的2D对象创建面板对象                 <img alt="" src=images/Arch_Frame.svg  style="width:32px;"> [框架](Arch_Frame.md)                            从选定的布局创建框架对象
  <img alt="" src=images/Arch_Equipment.svg  style="width:32px;"> [设备](Arch_Equipment.md)   创建设备或家具对象                         <img alt="" src=images/Arch_SetMaterial.svg  style="width:32px;"> [材质](Arch_SetMaterial.md)          将材质属性分配给选定对象
  <img alt="" src=images/Arch_Schedule.svg  style="width:32px;"> [日程表](Arch_Schedule.md)    创建不同类型的日程表                       <img alt="" src=images/Arch_CutPlane.svg  style="width:32px;"> [剖面平面](Arch_CutPlane.md)               根据平面剖面切割对象
  <img alt="" src=images/Arch_Add.svg  style="width:32px;"> [添加](Arch_Add.md)                     向组件添加对象                             <img alt="" src=images/Arch_Remove.svg  style="width:32px;"> [移除](Arch_Remove.md)                         从组件中减去或移除对象
  <img alt="" src=images/Arch_Survey.svg  style="width:32px;"> [测量](Arch_Survey.md)            进入或离开测量模式                                                                                                                                   



### 其他内置工作台

上面概括介绍了 FreeCAD 最重要的几个工具，但还有更多工作台可用，包括：

-   [TechDraw 工作台](TechDraw_Workbench.md) 用于从 3D 模型生成技术图纸。
-   [Mesh 工作台](Mesh_Workbench.md) 可以处理 [多边形网格](https://en.wikipedia.org/wiki/Polygon_mesh)。虽然网格不是 FreeCAD 中首选的几何类型，因为它们缺乏精度和对曲线的支持，但网格仍然具有许多用途，并且在 FreeCAD 中得到了完全支持。网格工作台还提供了许多将零件转换为网格和将网格转换为零件的工具。
-   [Raytracing 工作台](Raytracing_Workbench.md) 提供了与外部渲染器（如 povray 或 luxrender）进行交互的工具。在 FreeCAD 内部，该工作台允许您从模型中生成高质量的渲染图像。
-   [Spreadsheet 工作台](Spreadsheet_Workbench.md) 允许创建和操作电子表格数据，这些数据可以从 FreeCAD 模型中提取。电子表格单元格还可以在 FreeCAD 的许多区域中引用，允许将它们用作主数据结构。
-   [FEM 工作台](FEM_Workbench.md) 处理 [有限元分析](https://en.wikipedia.org/wiki/Finite_element_method)，允许进行 FEM 计算的预处理和后处理，并以图形方式显示结果。



### 外部工作台

还有许多其他由 FreeCAD 社区成员制作的非常有用的工作台。虽然它们未包含在标准的 FreeCAD 安装中，但它们可以很容易地作为插件安装。它们都在 [FreeCAD-addons](https://github.com/FreeCAD/FreeCAD-addons) 存储库中引用。其中最发达的包括：

-   [图纸标注工作台](https://github.com/hamish2014/FreeCAD_drawing_dimensioning) 提供许多新工具，可直接在图纸上工作，并允许您添加尺寸、注释和其他技术符号，并对它们的外观进行精确控制。**图纸标注工作台已不再维护。**
-   [紧固件工作台](https://github.com/shaise/FreeCAD_FastenersWB) 提供了各种现成的紧固件对象，如螺钉、螺栓、杆、垫圈和螺帽。有许多选项和设置可供选择。
-   [A2plus](https://github.com/kbwbe/A2plus) 工作台提供了一系列用于安装和处理 [装配体](https://en.wikipedia.org/wiki/Assembly_modelling) 的工具。

**延伸阅读**

-   [完整的工作台列表](Workbenches.md)
-   [Part 工作台](Part_Workbench.md)
-   [Draft 工作台](Draft_Workbench.md)
-   [Sketcher and Part Design 工作台](PartDesign_Workbench.md)
-   [Arch 工作台](Arch_Workbench.md)
-   [TechDraw 工作台](TechDraw_Workbench.md)
-   [FEM 工作台](FEM_Workbench.md)
-   [FreeCAD-addons 存储库](https://github.com/FreeCAD/FreeCAD-addons)



---
⏵ [documentation index](../README.md) > Manual:All workbenches at a glance/zh-cn
