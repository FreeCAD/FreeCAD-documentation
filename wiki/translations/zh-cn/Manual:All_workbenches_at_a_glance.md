





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
  <img alt="" src=images/Part_Box.png  style="width:32px;"> [Box](Part_Box.md)                                        绘制长方体                                         <img alt="" src=images/Part_Cone.png  style="width:32px;"> [Cone](Part_Cone.md)                                                    绘制圆锥
  <img alt="" src=images/Part_Cylinder.png  style="width:32px;"> [Cylinder](Part_Cylinder.md)                    绘制圆柱体                                         <img alt="" src=images/Part_Sphere.png  style="width:32px;"> [Sphere](Part_Sphere.md)                                            绘制球体
  <img alt="" src=images/Part_Torus.png  style="width:32px;"> [Torus](Part_Torus.md)                                绘制圆环体（环）                                   <img alt="" src=images/Part_CreatePrimitives.png  style="width:32px;"> [Create primitives](Part_CreatePrimitives.md)   创建各种其他参数化的几何图元
  <img alt="" src=images/Part_Shapebuilder.png  style="width:32px;"> [Shape builder](Part_Shapebuilder.md)   从基元创建更复杂的形状                             <img alt="" src=images/Part_Union.png  style="width:32px;"> [Union](Part_Union.md)                                                熔合 (合并) 两个对象
  <img alt="" src=images/Part_Common.png  style="width:32px;"> [Common](Part_Common.md)                            提取两个对象的公共（交叉）部分                     <img alt="" src=images/Part_Cut.png  style="width:32px;"> [Cut](Part_Cut.md)                                                        从另一个对象中剪切（减去）一个对象
  <img alt="" src=images/Part_JoinConnect.png  style="width:32px;"> [JonConnect](Part_JoinConnect.md)         连接围墙物体的内部                                 <img alt="" src=images/Part_JoinEmbed.png  style="width:32px;"> [JoinEmbed](Part_JoinEmbed.md)                                将围墙物体对象嵌入另一个围墙物体对象中
  <img alt="" src=images/Part_JoinCutout.png  style="width:32px;"> [Join Cutout](Part_JoinCutout.md)           在围墙物体对象的墙上剪切一块来创建另一个围墙对象   <img alt="" src=images/Part_Extrude.png  style="width:32px;"> [Extrude](Part_Extrude.md)                                        拉伸对象的一个平面
  <img alt="" src=images/Part_Fillet.png  style="width:32px;"> [Fillet](Part_Fillet.md)                            做物体的圆角（圆孤）边缘                           <img alt="" src=images/Part_Revolve.png  style="width:32px;"> [Revolve](Part_Revolve.md)                                        围绕轴旋转对象（非实体）来创建一个实体对象
  <img alt="" src=images/Part_Section.png  style="width:32px;"> [Section](Part_Section.md)                        将对象与剖切面相交来创建横截面                     <img alt="" src=images/Part_SectionCross.png  style="width:32px;"> [SectionCross](Part_SectionCross.md)                    沿对象的一个方向创建多个横截面
  <img alt="" src=images/Part_Chamfer.png  style="width:32px;"> [Chamfer](Part_Chamfer.md)                        给物体的边缘做倒角                                 <img alt="" src=images/Part_Mirror.png  style="width:32px;"> [Mirror](Part_Mirror.md)                                            相对给定镜像平面镜像选定对象
  <img alt="" src=images/Part_RuledSurface.png  style="width:32px;"> [Ruled Surface](Part_RuledSurface.md)   在所选曲线之间创建一个有规则的曲面                 <img alt="" src=images/Part_Sweep.png  style="width:32px;"> [Sweep](Part_Sweep.md)                                                沿路径扫略一个或多个轮廓
  <img alt="" src=images/Part_Loft.png  style="width:32px;"> [Part\_Loft](Part_Loft.md)                              从一个轮廓渐变到另一个轮廓                         <img alt="" src=images/Part_Offset.png  style="width:32px;"> [Offset](Part_Offset.md)                                            创建原始对象的缩放过的副本
  <img alt="" src=images/Part_Thickness.png  style="width:32px;"> [Thickness](Part_Thickness.md)                为形状的面指定厚度                                                                                                                                                                    


</div>

### Draft

Draft 工作台提供了执行基本 2D CAD 绘图任务的工具：直线，圆圈，等等，以及一些通用的便捷工具，例如移动，旋转和缩放，另外还提供了几种绘图辅助工具，例如网格和捕捉。Draft 工作台主要用于绘制Arch 对象的引导线，但是也可以当作 FreeCAD 的"瑞士军刀"。


<div class="mw-translate-fuzzy">

  工具                                                                                                                    描述                                            工具                                                                                                               描述
  ----------------------------------------------------------------------------------------------------------------------- ----------------------------------------------- ------------------------------------------------------------------------------------------------------------------ ------------------------------------------------------------------
  <img alt="" src=images/Draft_Line.png  style="width:32px;"> [Line](Draft_Line.md)                                      在 2 个点之间绘制线段                           <img alt="" src=images/Draft_Wire.png  style="width:32px;"> [Wire](Draft_Wire.md)                                 绘制由多个线段组成的线（折线）
  <img alt="" src=images/Draft_Circle.png  style="width:32px;"> [Circle](Draft_Circle.md)                              以中心和半径绘制一个圆                          <img alt="" src=images/Draft_Arc.png  style="width:32px;"> [Arc](Draft_Arc.md)                                     以中心，半径，起始角度和结束角度绘制弧段
  <img alt="" src=images/Draft_Ellipse.png  style="width:32px;">[Ellipse](Draft_Ellipse.md)                           以两个角点绘制一个椭圆                          <img alt="" src=images/Draft_Polygon.png  style="width:32px;"> [Polygon](Draft_Polygon.md)                     以中心和半径绘制正多边形
  <img alt="" src=images/Draft_Rectangle.png  style="width:32px;"> [Rectangle](Draft_Rectangle.md)                  以 2 个相对的点绘制一个矩形                     <img alt="" src=images/Draft_Text.png  style="width:32px;"> [Text](Draft_Text.md)                                 绘制多行文本注释
  <img alt="" src=images/Draft_Dimension.png  style="width:32px;"> [Dimension](Draft_Dimension.md)                  绘制尺寸标注                                    <img alt="" src=images/Draft_BSpline.png  style="width:32px;"> [BSpline](Draft_BSpline.md)                     以一系列的点绘制 B 样条曲线
  <img alt="" src=images/Draft_Point.png  style="width:32px;"> [Point](Draft_Point.md)                                  插入一个点                                      <img alt="" src=images/Draft_ShapeString.png  style="width:32px;"> [Shapestring](Draft_ShapeString.md)     ShapeString 工具在当前文档的给定点处插入表示文本字符串的复合形状
  <img alt="" src=images/Draft_Facebinder.png  style="width:32px;"> [Facebinder](Draft_Facebinder.md)              从现有对象上的选定面创建新对象                  <img alt="" src=images/Draft_BezCurve.png  style="width:32px;"> [Bezier Curve](Draft_BezCurve.md)             以一系列的点绘制贝塞尔曲线
  <img alt="" src=images/Draft_Move.png  style="width:32px;"> [Move](Draft_Move.md)                                      将对象从一个位置移动或复制到另一个位置          <img alt="" src=images/Draft_Rotate.png  style="width:32px;"> [Rotate](Draft_Rotate.md)                         围绕某点旋转对象一定角度
  <img alt="" src=images/Draft_Offset.png  style="width:32px;"> [Offset](Draft_Offset.md)                              将对象偏移特定距离                              <img alt="" src=images/Draft_Trimex.png  style="width:32px;"> [Trimex](Draft_Trimex.md)                         修剪，延伸或拉伸物体
  <img alt="" src=images/Draft_Upgrade.png  style="width:32px;"> [Upgrade](Draft_Upgrade.md)                          将对象转换或连接到更高级别的对象                <img alt="" src=images/Draft_Downgrade.png  style="width:32px;"> [Downgrade](Draft_Downgrade.md)             将对象转换或分离为较低级别的对象
  <img alt="" src=images/Draft_Scale.png  style="width:32px;"> [Scale](Draft_Scale.md)                                  相对某点缩放对象                                <img alt="" src=images/Draft_Shape2DView.png  style="width:32px;"> [Shape 2D View](Draft_Shape2DView.md)   创建一个 2D 对象，它是另一个对象的扁平视图
  <img alt="" src=images/Draft_Draft2Sketch.png  style="width:32px;"> [Draft to Sketch](Draft_Draft2Sketch.md)   将草稿(draft)对象转换为草图(sketch)，反之亦然   <img alt="" src=images/Draft_Array.png  style="width:32px;"> [Array](Draft_Array.md)                             将对象创建为极坐标阵列或矩形阵列
  <img alt="" src=images/Draft_PathArray.png  style="width:32px;"> [Path Array](Draft_PathArray.md)                 沿路径放置副本来将对象创建为阵列                <img alt="" src=images/Draft_Clone.png  style="width:32px;"> [Clone](Draft_Clone.md)                             为对象创建带链接的副本
  <img alt="" src=images/Draft_Mirror.png  style="width:32px;"> [Mirror](Draft_Mirror.md)                              沿一条线镜像对象                                                                                                                                                   


</div>

### Sketcher

Sketcher 工作台包含用于构建和编辑复杂 2D 对象的工具，称为草图(sketch)。这些草图内的几何形状可以通过使用约束来精确地定位和关联。这些草图(sketch)对象主要是 PartDesign 几何体的构建模块，但在 FreeCAD 各处都有用。


<div class="mw-translate-fuzzy">

  工具                                                                                                                                                            描述                                                                             工具                                                                                                                                                      描述
  --------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------
  <img alt="" src=images/Sketcher_CreatePoint.png  style="width:32px;"> [Point](Sketcher_CreatePoint.md)                                               画出一点                                                                         <img alt="" src=images/Sketcher_Line.png  style="width:32px;"> [Line](Sketcher_CreateLine.md)                                                         以 2 个点绘制线段
  <img alt="" src=images/Sketcher_Arc.png  style="width:32px;"> [Arc](Sketcher_CreateArc.md)                                                                   以中心，半径，起始角度和结束角度绘制弧段                                         <img alt="" src=images/Sketcher_CreateArc3Point.png  style="width:32px;"> [Arc 3 points](Sketcher_Create3PointArc.md)                      以两个端点和圆周上的另一个点绘制弧段
  <img alt="" src=images/Sketcher_Circle.png  style="width:32px;"> [Circle](Sketcher_CreateCircle.md)                                                       以中心和半径绘制一个圆                                                           <img alt="" src=images/Sketcher_CreateCircle3Point.png  style="width:32px;"> [ Circle 3 points](Sketcher_Create3PointCircle.md)         以圆周上的三个点绘制一个圆
  <img alt="" src=images/Sketcher_CreateEllipse.png  style="width:32px;"> [Ellipse](Sketcher_CreateEllipseByCenter.md)                               按中心点，主要半径点和小半径点绘制椭圆                                           <img alt="" src=images/Sketcher_CreateEllipse3Point.png  style="width:32px;"> [Ellipse 3 points](Sketcher_CreateEllipseBy3Points.md)   根据大直径（2 点）和小半径点绘制椭圆
  <img alt="" src=images/Sketcher_CreateArcOfEllipse.png  style="width:32px;"> [Arc of ellipse](Sketcher_CreateArcOfEllipse.md)                 按中心点，主要半径点，起点和终点绘制椭圆弧                                       <img alt="" src=images/Sketcher_CreatePolyline.png  style="width:32px;"> [Polyline](Sketcher_CreatePolyline.md)                             绘制由多个线段组成的线，有多种绘图模式
  <img alt="" src=images/Sketcher_CreateRectangle.png  style="width:32px;"> [Rectangle](Sketcher_CreateRectangle.md)                               以 2 个相对的点绘制一个矩形                                                      <img alt="" src=images/Sketcher_CreateTriangle.png  style="width:32px;"> [Triangle](Sketcher_CreateTriangle.md)                             绘制圈在构造几何圆中的正三角形
  <img alt="" src=images/Sketcher_CreateSquare.png  style="width:32px;"> [Square](Sketcher_CreateSquare.md)                                           绘制圈在构造几何圆中的正方形                                                     <img alt="" src=images/Sketcher_CreatePentagon.png  style="width:32px;"> [Pentagon](Sketcher_CreatePentagon.md)                             绘制圈在构造几何圆中的正五边形
  <img alt="" src=images/Sketcher_CreateHexagon.png  style="width:32px;"> [Hexagon](Sketcher_CreateHexagon.md)                                       绘制圈在构造几何圆中的正六边形                                                   <img alt="" src=images/Sketcher_CreateHeptagon.png  style="width:32px;"> [Heptagon](Sketcher_CreateHeptagon.md)                             绘制圈在构造几何圆中的正七边形
  <img alt="" src=images/Sketcher_CreateOctagon.png  style="width:32px;"> [Octagon](Sketcher_CreateOctagon.md)                                       绘制圈在构造几何圆中的正八边形                                                   <img alt="" src=images/Sketcher_CreateSlot.png  style="width:32px;"> [Slot](Sketcher_CreateSlot.md)                                             通过选择一个半圆的中心和另一个半圆的端点绘制一个长腰孔
  <img alt="" src=images/Sketcher_CreateFillet.png  style="width:32px;"> [Fillet](Sketcher_CreateFillet.md)                                           在相交于一点的两条线之间制作圆角                                                 <img alt="" src=images/Sketcher_Trimming.png  style="width:32px;"> [Trimming](Sketcher_Trimming.md)                                               相对于选定点，修剪直线，圆或圆弧
  <img alt="" src=images/Sketcher_External.png  style="width:32px;"> [External geometry](Sketcher_External.md)                                            创建链接到外部几何体的边                                                         <img alt="" src=images/Sketcher_ToggleConstruction.png  style="width:32px;"> [Construction mode](Sketcher_ToggleConstruction.md)        切换元素是否处于构造模式。构造对象不会用于 3D 几何操作，只有在编辑包含它的 Sketch 时才可见。
  <img alt="" src=images/Constraint_PointOnPoint.png  style="width:32px;"> [Coincident](Sketcher_ConstrainCoincident_‎.md)                          让一个点固定于（与之重合）一个（或多个已经重合的）其他点上。                     <img alt="" src=images/Constraint_PointOnObject.png  style="width:32px;"> [Point on object](Sketcher_ConstrainPointOnObject.md)            将点绑定到另一个对象（例如直线，圆弧或轴线）上。
  <img alt="" src=images/Constraint_Vertical.png  style="width:32px;"> [Vertical](Sketcher_ConstrainVertical_‎.md)                                      将选定的线或折线元素约束到真正的垂直方向。在应用此约束之前，可以选择多个对象。   <img alt="" src=images/Constraint_Horizontal.png  style="width:32px;"> [Horizontal](Sketcher_ConstrainHorizontal.md)                          将选定的线或折线元素约束到真正的水平方向。在应用此约束之前，可以选择多个对象。
  <img alt="" src=images/Constraint_Parallel.png  style="width:32px;"> [Parallel](Sketcher_ConstrainParallel.md)                                        约束两条或更多条线，彼此平行。                                                   <img alt="" src=images/Constraint_Perpendicular.png  style="width:32px;"> [Perpendicular](Sketcher_ConstrainPerpendicular.md)              约束两条线彼此垂直，或约束线在弧的端点与弧垂直。
  <img alt="" src=images/Constraint_Tangent.png  style="width:32px;"> [Tangent](Sketcher_ConstrainTangent.md)                                            在两个选定实体之间创建相切约束，或在两个线段之间创建共线约束。                   <img alt="" src=images/Constraint_EqualLength.png  style="width:32px;"> [Equal length](Sketcher_ConstrainEqual.md)                           约束两个选定实体彼此相等。如果在圆或弧上使用，则它们的半径将设置为相等。
  <img alt="" src=images/Constraint_Symmetric.png  style="width:32px;"> [Symmetric](Sketcher_ConstrainSymmetric.md)                                    相对某线约束两个点对称，或者相对第三个选定点约束前两个选定点对称。               <img alt="" src=images/Sketcher_ConstrainLock.png  style="width:32px;"> [Lock](Sketcher_ConstrainLock.md)                                    通过设置相对于原点的垂直和水平距离来约束所选对象，从而锁定它的位置。
  <img alt="" src=images/Constraint_HorizontalDistance.png  style="width:32px;"> [Horizontal distance](Sketcher_ConstrainDistanceX.md)        指定两点或线段端点之间的水平距离。如果仅选择了一个对象，则设置为与原点的距离。   <img alt="" src=images/Constraint_VerticalDistance.png  style="width:32px;"> [Vertical distance](Sketcher_ConstrainDistanceY.md)        指定两点或线段端点之间的竖直距离。如果仅选择了一个对象，则设置为与原点的距离。
  <img alt="" src=images/Constraint_Length.png  style="width:32px;"> [Distance](Sketcher_ConstrainDistance.md)                                            约束所选线的长度，或约束两个点之间的距离。                                       <img alt="" src=images/Constraint_Radius.png  style="width:32px;"> [Radius](Sketcher_ConstrainRadius.md)                                          通过约束半径来定义选定圆弧或圆的半径。
  <img alt="" src=images/Constraint_InternalAngle.png  style="width:32px;"> [Internal anglr](Sketcher_ConstrainAngle.md)                           定义两条选定线之间的内角。                                                       <img alt="" src=images/Constraint_SnellsLaw.png  style="width:32px;"> [Snell\'s law](Sketcher_ConstrainSnellsLaw.md)                           约束两条线以遵守折射定律来模拟通过界面的光
  <img alt="" src=images/Constraint_InternalAlignment.png  style="width:32px;"> [Internal alignment](Sketcher_ConstrainInternalAlignment.md)   将所选元素与选定形状对齐（例如，线段作为椭圆的主轴）                             <img alt="" src=images/Sketcher_MapSketch.png  style="width:32px;"> [Map sketch](Sketcher_MapSketch.md)                                          将草图映射到先前选定的实体的面
  <img alt="" src=images/Sketcher_MergeSketch.png  style="width:32px;"> [Merge](Sketcher_MergeSketches.md)                                             合并两个或多个草图                                                               <img alt="" src=images/Sketcher_MirrorSketch.png  style="width:32px;"> [Mirror](Sketcher_MirrorSketch.md)                                     镜像某草图中选定的元素


</div>

### Part Design 

Part Design 工作台包含用于构建实体零件的高级工具，还包含 Sketcher 中的所有工具。由于Part Design 工作台只能生成实体形状（Part Design的第一规则），因此在设计用于制造的部品或用于 3D 打印的零件时，Part Design 是主工作台，您将始终获得可打印的对象。


<div class="mw-translate-fuzzy">

  工具                                                                                                                                     描述                               工具                                                                                                                                        描述
  ---------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------
  <img alt="" src=images/PartDesign_Pad.png  style="width:32px;"> [Pad](PartDesign_Pad.md)                                            用选定草图拉伸出实体对象           <img alt="" src=images/PartDesign_Pocket.png  style="width:32px;"> [Pocket](PartDesign_Pocket.md)                                   用选定的草图创建一个凹坑。草图必须贴附于现有实体对象的面
  <img alt="" src=images/PartDesign_Revolution.png  style="width:32px;"> [Revolution](PartDesign_Revolution.md)                通过围绕轴旋转草图来创建实体       <img alt="" src=images/PartDesign_Groove.png  style="width:32px;"> [Groove](PartDesign_Groove.md)                                   通过围绕轴旋转草图来创建凹槽
  <img alt="" src=images/PartDesign_Fillet.png  style="width:32px;"> [Fillet](PartDesign_Fillet.md)                                给对象的边缘做圆角                 <img alt="" src=images/PartDesign_Chamfer.png  style="width:32px;"> [Chamfer](PartDesign_Chamfer.md)                               给对象的边缘做倒角
  <img alt="" src=images/PartDesign_Draft.png  style="width:32px;"> [Draft](PartDesign_Draft.md)                                    给对象的面一个拔模角度             <img alt="" src=images/PartDesign_Mirrored.png  style="width:32px;"> [Mirrored](PartDesign_Mirrored.md)                           相对于平面或表面镜像某些特征
  <img alt="" src=images/PartDesign_LinearPattern.png  style="width:32px;"> [Linear pattern](PartDesign_LinearPattern.md)   创建特征的线性阵列                 <img alt="" src=images/PartDesign_PolarPattern.png  style="width:32px;"> [Polar pattern](PartDesign_PolarPattern.md)          创建特征的极坐标阵列
  <img alt="" src=images/PartDesign_Scaled.png  style="width:32px;"> [Scaled](PartDesign_Scaled.md)                                将特征缩放到不同的大小             <img alt="" src=images/PartDesign_MultiTransform.png  style="width:32px;"> [Multitransform](PartDesign_MultiTransform.md)   允许使用其他变换的任意组合创建模式
  <img alt="" src=images/PartDesign_WizardShaft.png  style="width:32px;"> [Shaft wizard](PartDesign_WizardShaft.md)           通过值表生成轴，可以分析力和力矩   <img alt="" src=images/PartDesign_InvoluteGear.png  style="width:32px;"> [Involute gear wizard](PartDesign_InvoluteGear.md)   创建多种类型的齿轮


</div>

### Arch

Arch 工作台包含用于处理 [BIM](https://en.wikipedia.org/wiki/Building_information_modeling) 项目（土木工程和建筑）的工具，还包含 Draft 工作台中的所有工具。Arch 工作台的主要用途是创建 BIM 对象或为使用其他工作台构建的对象提供 BIM 属性，以便导出到[IFC](https://en.wikipedia.org/wiki/Industry_Foundation_Classes) 里。


<div class="mw-translate-fuzzy">

  Tool                                                                                                  Description                            Tool                                                                                                               Description
  ----------------------------------------------------------------------------------------------------- -------------------------------------- ------------------------------------------------------------------------------------------------------------------ --------------------------------------------
  <img alt="" src=images/Arch_Wall.png  style="width:32px;"> [Wall](Arch_Wall.md)                       从头开始创建墙或使用选定对象作为基础   <img alt="" src=images/Arch_Structure.png  style="width:32px;"> [Structure](Arch_Structure.md)                从头开始创建结构元素或使用选定对象作为基础
  <img alt="" src=images/Arch_Rebar.png  style="width:32px;"> [Rebar](Arch_Rebar.md)                   在选定的结构元素中创建钢筋             <img alt="" src=images/Arch_Floor.png  style="width:32px;"> [Floor](Arch_Floor.md)                                创建包含所选对象的楼板
  <img alt="" src=images/Arch_Building.png  style="width:32px;"> [Building](Arch_Building.md)       创建包含所选对象的建筑物               <img alt="" src=images/Arch_Site.png  style="width:32px;"> [Site](Arch_Site.md)                                    创建包含所选对象的场地
  <img alt="" src=images/Arch_Window.png  style="width:32px;"> [Window](Arch_Window.md)               使用所选对象作为基础创建门窗           <img alt="" src=images/Arch_SectionPlane.png  style="width:32px;"> [Section plane](Arch_SectionPlane.md)   将截面平面对象添加到文档中
  <img alt="" src=images/Arch_Axis.png  style="width:32px;"> [Axis](Arch_Axis.md)                       将轴系统添加到文档中                   <img alt="" src=images/Arch_Roof.png  style="width:32px;"> [Roof](Arch_Roof.md)                                    以选定的面创建倾斜屋顶
  <img alt="" src=images/Arch_Space.png  style="width:32px;"> [Space](Arch_Space.md)                   在文档中创建一个空间对象               <img alt="" src=images/Arch_Stairs.png  style="width:32px;"> [Stairs](Arch_Stairs.md)                            在文档中创建阶梯对象
  <img alt="" src=images/Arch_Panel.png  style="width:32px;"> [Panel](Arch_Panel.md)                   从选定的 2D 对象创建面板对象           <img alt="" src=images/Arch_Frame.png  style="width:32px;"> [Frame](Arch_Frame.md)                                从选定的布局创建框架对象
  <img alt="" src=images/Arch_Equipment.png  style="width:32px;"> [Equipment](Arch_Equipment.md)   创建设备或家具对象                     <img alt="" src=images/Arch_SetMaterial.png  style="width:32px;"> [Material](Arch_SetMaterial.md)           将材质属性赋予选定对象
  <img alt="" src=images/Arch_Schedule.png  style="width:32px;"> [Schedule](Arch_Schedule.md)       创建不同类型的计划                     <img alt="" src=images/Arch_CutPlane.png  style="width:32px;"> [Cut plane](Arch_CutPlane.md)                   根据计划切割对象
  <img alt="" src=images/Arch_Add.png  style="width:32px;"> [Add](Arch_Add.md)                           将对象添加到组件                       <img alt="" src=images/Arch_Remove.png  style="width:32px;"> [Remove](Arch_Remove.md)                            从组件中减去或删除对象
  <img alt="" src=images/Arch_Survey.png  style="width:32px;"> [Survey](Arch_Survey.md)               进入或离开调查模式                                                                                                                                        


</div>

### Drawing


<div class="mw-translate-fuzzy">

Drawing 工作台处理 2D 工程图纸的创建和操作，用于在 2D 平面上显示 3D 工作成果。然后，可以将这些图纸 SVG 或 DXF 格式，用其它 2D 应用程序打开，也可导出为 PDF 文件，或者打印出来。


</div>

The Drawing Workbench handles the creation and manipulation of 2D drawing sheets, used for displaying views of your 3D work in 2D. These sheets can then be exported to 2D applications in SVG or DXF formats, to a PDF file or printed.

  工具                                                                                                                    描述                                          工具                                                                                                                描述
  ----------------------------------------------------------------------------------------------------------------------- --------------------------------------------- ------------------------------------------------------------------------------------------------------------------- ----------------------------------------
  <img alt="" src=images/Drawing_Landscape_A3.png  style="width:32px;"> [New sheet](Drawing_Landscape_A3.md)   创建一张新的图纸                              <img alt="" src=images/Drawing_View.png  style="width:32px;"> [View](Drawing_View.md)                            在活动图纸中插入所选对象的视图
  <img alt="" src=images/Drawing_Annotation.png  style="width:32px;"> [Annotation](Drawing_Annotation.md)        向当前图纸添加注释                            <img alt="" src=images/Drawing_Clip.png  style="width:32px;"> [Clip](Drawing_Clip.md)                            将剪辑组添加到当前图纸（？）
  <img alt="" src=images/Drawing_Openbrowser.png  style="width:32px;"> [Open browser](Drawing_Openbrowser.md)   在浏览器中打开当前工作表的预览                <img alt="" src=images/Drawing_Orthoviews.png  style="width:32px;"> [Ortho views](Drawing_Orthoviews.md)   在当前工程图纸上自动创建对象的正交视图
  <img alt="" src=images/Drawing_Symbol.png  style="width:32px;"> [Symbol](Drawing_Symbol.md)                        在当前工程图纸上添加 SVG 文件的内容作为符号   <img alt="" src=images/Drawing_DraftView.png  style="width:32px;"> [Draft view](Drawing_DraftView.md)       在当前图纸中插入所选对象的特殊草稿视图
  <img alt="" src=images/Drawing_Save.png  style="width:32px;"> [Save](Drawing_Save.md)                                将当前工作表保存为 SVG 文件                                                                                                                                       

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




