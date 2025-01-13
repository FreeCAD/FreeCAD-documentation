# Manual:Modeling for product design/zh-cn
{{Manual:TOC}}


<div class="mw-translate-fuzzy">

[产品设计](https://en.wikipedia.org/wiki/Product_design) 原本是商业术语，但在 3D 领域，通常意味着建模的时候，心里想着将来 [3D 打印](https://en.wikipedia.org/wiki/3D_printing)，或更一般地说，由机器（例如 3D 打印机或 [CNC 机床](https://en.wikipedia.org/wiki/Numerical_control)）制造出来。


</div>


<div class="mw-translate-fuzzy">

在进行 3D 打印时，确保对象是"实体"的非常重要。因为它们将成为真实的、实体的物体，这是显而易见的。当然，它们可以为空心的。但是，您始终需要清楚地知道哪些点在材料内部，哪些点在材料外部，因为 3D 打印机或数控机床需要准确地知道哪些地方填充了材料，哪些没有填充。因此，在 FreeCAD 中，[PartDesign Workbench](PartDesign_Workbench.md) 是构建这些零件的完美工具，因为它将始终为您保证，你的物体是实体，可构建。


</div>


<div class="mw-translate-fuzzy">

为了说明 PartDesign 的工作方式，我们练习建模著名的 [Lego](https://en.wikipedia.org/wiki/Lego) 玩具的这款模型。


</div>


<div class="mw-translate-fuzzy">

![](images/Exercise_lego_01.jpg )


</div>


<div class="mw-translate-fuzzy">

乐高积木有个很酷的特色容易在互联网上获得零件的尺寸，至少对于标准件而言是这样。建模之后，在 3D 打印机上打印，都很容易。带着点耐心（3D 打印通常需要大量的调整和微调），可以制作出完全兼容的部件，完美地匹配原始乐高积木。下面的示例将制作比原始尺寸大 1.5 倍的零件。


</div>


<div class="mw-translate-fuzzy">

这里专门使用 [Sketcher](Sketcher_Workbench.md) 和 [PartDesign](PartDesign_Workbench.md) 工具。由于Sketcher 工作台中的所有工具都包含在 PartDesign 工作台里了，我们可以就在 PartDesign 中工作，不需要在两者之间来回切换。


</div>

A sketch is considered fully constrained when every point is locked into position by the appropriate number of constraints, meaning no part of the sketch can be moved freely. Achieving a fully constrained sketch is ideal because it ensures the design is well-defined and stable, allowing for predictable changes later in the design process. On the other hand, if more constraints are added than necessary---referred to as an over-constrained sketch---this can cause conflicts in the geometry. FreeCAD will alert you to any redundant or conflicting constraints, as over-constraining can cause issues in further operations like extrusions or cuts.


<div class="mw-translate-fuzzy">

PartDesign 对象完全基于 **Sketches**。Sketch 是一个 2D 对象，由线段（线，圆弧或椭圆弧）和约束组成。这些约束可以应用于线段，或其端点和中心点，并强制几何元素满足某些规则。例如，可以在线段上施加垂直约束以强制它保持垂直，或者在端点上施加位置（锁定）约束以禁止它移动。当草图的约束数量刚好时，草图的任何点都无法再移动了，称为完全约束的草图。当存在冗余约束时，移除某些约束也不会令几何体允许移动，称为过度约束。这应该避免，如果出现这种情况，FreeCAD 会通知你。


</div>

草图具有一个编辑模式，你可以在其中更改其几何形状和约束。完成编辑并退出编辑模式后，草图就会像 FreeCAD 中的任何其他对象一样运行，它们可以作为所有零件设计工具的构建块，也可以在其他如 [Part](Part_Workbench.md) 或 [Arch](Arch_Workbench.md) 工作台中使用。 [Draft workbench](Draft_Workbench.md) 还有一个工具可以将 Draft 对象转换为草图，反之亦然。


<div class="mw-translate-fuzzy">

-   我们首先建模一个立方体形状，它将成为我们乐高积木的基础。稍后我们将雕刻内部，并在其顶部添加8个点。所以，让我们首先制作一个矩形草图，然后对其进行拉伸：
-   切换到 [PartDesign Workbench](PartDesign_Workbench.md)
-   点击 <img alt="" src=images/Sketcher_NewSketch.svg  style="width:16px;"> [New Sketch](Sketcher_NewSketch.md) 按钮。将出现一个对话框，询问你想在何处创建草图，选择 **XY** 平面，即 \"地面\" 平面。草图将被创建并立即切换到编辑模式，视图将旋转以正交看向你的草图。
-   现在我们可以绘制一个矩形，通过选择 <img alt="" src=images/Sketcher_CreateRectangle.svg  style="width:16px;"> [Rectangle](Sketcher_CreateRectangle.md) 工具并点击两个角点。你可以在任何地方放置这两点，因为他们的正确位置将在下一步中设置。
-   你会注意到，我们的矩形自动添加了一些约束：垂直段收到了垂直约束，水平段收到了水平约束，每个角点都收到了点对点约束，将各段粘合在一起。你可以尝试通过用鼠标拖动其线条来移动矩形，所有的几何形状都会遵守这些约束。


</div>


<div class="mw-translate-fuzzy">

![](images/Exercise_lego_02.jpg )


</div>


<div class="mw-translate-fuzzy">

-   现在，让我们添加三个额外的约束：
    -   选中垂直段中的一个，然后添加一个 <img alt="" src=images/Constraint_VerticalDistance.svg  style="width:16px;"> [垂直距离约束](Sketcher_ConstrainDistanceY.md)。将其设定为 23.7 毫米。
    -   选中水平段中的一个，然后添加一个 <img alt="" src=images/Constraint_HorizontalDistance.svg  style="width:16px;"> [水平距离约束](Sketcher_ConstrainDistanceX.md)。将其设定为 47.7 毫米。
    -   最后，选中角点中的一个，然后选择原点（就是红色和绿色轴线交叉处的点），然后添加一个 <img alt="" src=images/Constraint_PointOnPoint.svg  style="width:16px;"> [重合约束](Sketcher_ConstrainCoincident.md)。矩形将会跳至原点，你的草图会变成绿色，这意味着它现在已经完全被约束了。你可以尝试移动其线条或点，但它们不会再移动。


</div>


<div class="mw-translate-fuzzy">

![](images/Exercise_lego_03.jpg )


</div>


<div class="mw-translate-fuzzy">

-   现在我们的基础草图已经准备好了，我们可以通过点击任务面板顶部的 **关闭** 按钮或简单地按 **Escape** 键来退出编辑模式。如果后续有需要，我们可以在树状视图中双击草图随时重新进入编辑模式。
-   我们来通过使用 <img alt="" src=images/PartDesign_Pad.svg  style="width:16px;"> [Pad](PartDesign_Pad.md) 工具并设定距离为 14.4 毫米来将其拉伸。其他选项可以保持默认值：


</div>


<div class="mw-translate-fuzzy">

![](images/Exercise_lego_04.jpg )


</div>


<div class="mw-translate-fuzzy">

**Pad** 的行为很像我们在上一章中使用的 [Extrude](Part_Extrude.md) 工具。然而，它们之间还是有一些差异的，主要的差异在于，Pad 不能被移动。它永远附着在它的草图上。如果你想改变 Pad 的位置，你必须移动基础草图。在当前的上下文中，我们希望确保没有任何东西会移出位置，这是一种额外的安全保障。


</div>


<div class="mw-translate-fuzzy">

-   现在，我们将使用 <img alt="" src=images/PartDesign_Pocket.svg  style="width:16px;"> [Pocket](PartDesign_Pocket.md) 工具来挖掘块的内部，这是 PartDesign 版本的 [Part Cut](Part_Cut.md)。为了创建一个口袋，我们将在块的底部面创建一个草图，这将用于移除块的一部分。
-   在选中底部面的情况下，按下 <img alt="" src=images/Sketcher_NewSketch.svg  style="width:16px;"> [新建草图](Sketcher_NewSketch.md) 按钮。
-   在面上画一个矩形。


</div>

![](images/FreeCAD_Exercise1_TopFaceSketch.png )


<div class="mw-translate-fuzzy">

-   我们现在将根据底面约束矩形。为了做到这一点，我们需要使用 <img alt="" src=images/Sketcher_External.svg  style="width:16px;"> [外部几何](Sketcher_External.md) 工具 \"导入\" 面的一些边缘。在底面的两条垂直线上使用此工具：


</div>


<div class="mw-translate-fuzzy">

![](images/Exercise_lego_06.jpg )


</div>


<div class="mw-translate-fuzzy">

你会注意到，只有基面的边缘才能通过这个工具添加。当你创建一个带参考面的草图时，会在该面和草图之间创建一个关系，这对于后续操作很重要。你总是可以稍后用 <img alt="" src=images/Sketcher_MapSketch.svg  style="width:16px;"> [映射草图](Sketcher_MapSketch.md) 工具将草图重新映射到另一个面。


</div>


<div class="mw-translate-fuzzy">

-   外部几何并不是 \"真实\" 的，当我们离开编辑模式时，它将被隐藏。但是我们可以用它来放置约束。放置以下 4 个约束：
    -   选择矩形的左上点和导入线的顶点，添加一个 <img alt="" src=images/Constraint_HorizontalDistance.svg  style="width:16px;"> [水平距离约束](Sketcher_ConstrainDistanceX.md)，距离为 1.8 毫米
    -   再次选择矩形的左上点和导入线的顶点，添加一个 <img alt="" src=images/Constraint_VerticalDistance.svg  style="width:16px;"> [垂直距离约束](Sketcher_ConstrainDistanceY.md)，距离为 1.8 毫米
    -   选择矩形的右下点和右导入线的底点，添加一个 <img alt="" src=images/Constraint_HorizontalDistance.svg  style="width:16px;"> [水平距离约束](Sketcher_ConstrainDistanceX.md)，距离为 1.8 毫米
    -   再次选择矩形的右下点和右导入线的底点，添加一个 <img alt="" src=images/Constraint_VerticalDistance.svg  style="width:16px;"> [垂直距离约束](Sketcher_ConstrainDistanceY.md)，距离为 1.8 毫米


</div>


<div class="mw-translate-fuzzy">

![](images/Exercise_lego_07.jpg )


</div>


<div class="mw-translate-fuzzy">

-   退出编辑模式，我们现在可以进行口袋操作：在选中草图的情况下，按 <img alt="" src=images/PartDesign_Pocket.svg  style="width:16px;"> [Pocket](PartDesign_Pocket.md) 按钮。设置长度为 12.6 毫米，这将使我们垫的上面保持 1.8 毫米的厚度（记住，我们垫的总高度是 14.4 毫米）。


</div>


<div class="mw-translate-fuzzy">

![](images/Exercise_lego_08.jpg )


</div>


<div class="mw-translate-fuzzy">

-   我们现在将对顶面的 8 个点进行处理。为了做到这一点，由于它们是同一特性的重复，我们将使用 Part Design Workbench 的便捷工具 <img alt="" src=images/PartDesign_LinearPattern.svg  style="width:16px;"> [线性模式](PartDesign_LinearPattern.md)，它可以建模一次，然后重复形状。
-   首先，选择我们块的顶面

创建一个 <img alt="" src=images/Sketcher_NewSketch.svg  style="width:16px;"> [新草图](Sketcher_NewSketch.md)。

-   创建两个 <img alt="" src=images/Sketcher_Circle.svg  style="width:16px;"> [圆](Sketcher_CreateCircle.md)。
-   对于每个圆，选择它并添加一个半径约束 <img alt="" src=images/Sketcher_ConstrainRadius.svg  style="width:16px;"> [Radius Constraint](Sketcher_ConstrainRadius.md)，每个半径为 3.6 毫米
-   使用 <img alt="" src=images/Sketcher_External.svg  style="width:16px;"> [外部几何](Sketcher_External.md) 工具导入基面的左边缘。
-   在每个圆的中心点和导入边缘的角点之间放置两个垂直约束和两个水平约束，每个约束为 6 毫米，这样每个圆的中心就离面的边界 6 毫米：


</div>


<div class="mw-translate-fuzzy">

![](images/Exercise_lego_09.jpg )


</div>


<div class="mw-translate-fuzzy">

-   注意，当你锁定草图中所有物体的位置和尺寸时，它就会变得完全约束。这总是让你呆在安全的一面。你现在可以改变第一个草图，我们之后做的所有事情都会保持严密。
-   退出编辑模式，选择这个新的草图，创建一个厚度为 2.7 毫米的 <img alt="" src=images/PartDesign_Pad.svg  style="width:16px;"> [垫](PartDesign_Pad.md)：


</div>

-   By choosing the completed sketch use the <img alt="" src=images/PartDesign_Pocket.svg  style="width:16px;"> [Pocket](PartDesign_Pocket.md) tool setting the length to 12 mm.

![](images/FreeCAD_Exercise1_BottomPad.png )

-   This is it. Our brick is ready. If you wish to change its color, you can do so by going to the **View tab**.


<div class="mw-translate-fuzzy">

![](images/Exercise_lego_10.jpg )


</div>

You may notice that the modeling history in the tree view has become quite extensive. This is incredibly valuable, as it allows us to revisit and modify any step in the design process at any time. For instance, adapting this model to create a 2x2 brick instead of a 2x4 would be a breeze---just a few adjustments to the dimensions and pattern occurrences would do the trick. This same flexibility allows us to design larger, custom pieces that aren\'t part of the original Lego set. The parametric nature of FreeCAD makes it easy to modify existing models, giving us full control to adapt or expand the design as needed.

But we could also want to get rid of the history, for example, if we are going to model a castle with this brick, and we don\'t want to have this whole history repeated 500 times in our file.

There are two simple ways to get rid of the history, one is using the [Create simple copy](Part_SimpleCopy.md) tool from the [Part Workbench](Part_Workbench.md), which will create a copy of our piece that doesn\'t depend anymore on the history (you can delete the whole history afterwards), the other way is exporting the piece as a STEP file and re-importing it.

**Downloads**

-   The model produced during this exercise: <https://github.com/yorikvanhavre/FreeCAD-manual/blob/master/files/lego.FCStd>

**延伸阅读**

-   [The Sketcher](Sketcher_Workbench.md)
-   [The Part Design Workbench](PartDesign_Workbench.md)
-   [The Assembly2 Workbench](https://github.com/hamish2014/FreeCAD_assembly2)


<div class="mw-translate-fuzzy">





</div>



---
⏵ [documentation index](../README.md) > [Tutorials](Category_Tutorials.md) > Manual:Modeling for product design/zh-cn
