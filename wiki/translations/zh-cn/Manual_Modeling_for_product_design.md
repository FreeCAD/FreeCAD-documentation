# Manual:Modeling for product design/zh-cn
{{Manual:TOC}}

[产品设计](https://en.wikipedia.org/wiki/Product_design) 原本是商业术语，但在 3D 领域，通常意味着建模的时候，心里想着将来 [3D 打印](https://en.wikipedia.org/wiki/3D_printing)，或更一般地说，由机器（例如 3D 打印机或 [CNC 机床](https://en.wikipedia.org/wiki/Numerical_control)）制造出来。

在进行 3D 打印时，确保对象是"实体"的非常重要。因为它们将成为真实的、实体的物体，这是显而易见的。当然，它们可以为空心的。但是，您始终需要清楚地知道哪些点在材料内部，哪些点在材料外部，因为 3D 打印机或数控机床需要准确地知道哪些地方填充了材料，哪些没有填充。因此，在 FreeCAD 中，[PartDesign Workbench](PartDesign_Workbench.md) 是构建这些零件的完美工具，因为它将始终为您保证，你的物体是实体，可构建。

为了说明 PartDesign 的工作方式，我们练习建模著名的 [Lego](https://en.wikipedia.org/wiki/Lego) 玩具的这款模型。

![](images/Exercise_lego_01.jpg )

乐高积木有个很酷的特色容易在互联网上获得零件的尺寸，至少对于标准件而言是这样。建模之后，在 3D 打印机上打印，都很容易。带着点耐心（3D 打印通常需要大量的调整和微调），可以制作出完全兼容的部件，完美地匹配原始乐高积木。下面的示例将制作比原始尺寸大 1.5 倍的零件。

这里专门使用 [Sketcher](Sketcher_Workbench.md) 和 [PartDesign](PartDesign_Workbench.md) 工具。由于Sketcher 工作台中的所有工具都包含在 PartDesign 工作台里了，我们可以就在 PartDesign 中工作，不需要在两者之间来回切换。

PartDesign 对象完全基于 **Sketches**。Sketch 是一个 2D 对象，由线段（线，圆弧或椭圆弧）和约束组成。这些约束可以应用于线段，或其端点和中心点，并强制几何元素满足某些规则。例如，可以在线段上施加垂直约束以强制它保持垂直，或者在端点上施加位置（锁定）约束以禁止它移动。当草图的约束数量刚好时，草图的任何点都无法再移动了，称为完全约束的草图。当存在冗余约束时，移除某些约束也不会令几何体允许移动，称为过度约束。这应该避免，如果出现这种情况，FreeCAD 会通知你。

草图具有一个编辑模式，你可以在其中更改其几何形状和约束。完成编辑并退出编辑模式后，草图就会像 FreeCAD 中的任何其他对象一样运行，它们可以作为所有零件设计工具的构建块，也可以在其他如 [Part](Part_Workbench.md) 或 [Arch](Arch_Workbench.md) 工作台中使用。 [Draft workbench](Draft_Workbench.md) 还有一个工具可以将 Draft 对象转换为草图，反之亦然。

-   我们首先建模一个立方体形状，它将成为我们乐高积木的基础。稍后我们将雕刻内部，并在其顶部添加8个点。所以，让我们首先制作一个矩形草图，然后对其进行拉伸：
-   切换到 [PartDesign Workbench](PartDesign_Workbench.md)
-   点击 <img alt="" src=images/Sketcher_NewSketch.svg  style="width:16px;"> [New Sketch](Sketcher_NewSketch.md) 按钮。将出现一个对话框，询问你想在何处创建草图，选择 **XY** 平面，即 \"地面\" 平面。草图将被创建并立即切换到编辑模式，视图将旋转以正交看向你的草图。
-   现在我们可以绘制一个矩形，通过选择 <img alt="" src=images/Sketcher_CreateRectangle.svg  style="width:16px;"> [Rectangle](Sketcher_CreateRectangle.md) 工具并点击两个角点。你可以在任何地方放置这两点，因为他们的正确位置将在下一步中设置。
-   你会注意到，我们的矩形自动添加了一些约束：垂直段收到了垂直约束，水平段收到了水平约束，每个角点都收到了点对点约束，将各段粘合在一起。你可以尝试通过用鼠标拖动其线条来移动矩形，所有的几何形状都会遵守这些约束。

![](images/Exercise_lego_02.jpg )

-   现在，让我们添加三个额外的约束：
    -   选中垂直段中的一个，然后添加一个 <img alt="" src=images/Constraint_VerticalDistance.svg  style="width:16px;"> [垂直距离约束](Sketcher_ConstrainDistanceY.md)。将其设定为 23.7 毫米。
    -   选中水平段中的一个，然后添加一个 <img alt="" src=images/Constraint_HorizontalDistance.svg  style="width:16px;"> [水平距离约束](Sketcher_ConstrainDistanceX.md)。将其设定为 47.7 毫米。
    -   最后，选中角点中的一个，然后选择原点（就是红色和绿色轴线交叉处的点），然后添加一个 <img alt="" src=images/Constraint_PointOnPoint.svg  style="width:16px;"> [重合约束](Sketcher_ConstrainCoincident.md)。矩形将会跳至原点，你的草图会变成绿色，这意味着它现在已经完全被约束了。你可以尝试移动其线条或点，但它们不会再移动。

![](images/Exercise_lego_03.jpg )

请注意，最后一个点对点的约束并非绝对必要。你并不一定要使用完全约束的草图进行工作。然而，如果我们打算将这个块进行3D打印，那么将我们的部件保持在原点附近将是必要的（原点将是打印机头可以移动的空间的中心）。通过添加这个约束，我们确保了我们的部件始终会\"锚定\"在那个原点。

Share

-   现在我们的基础草图已经准备好了，我们可以通过点击任务面板顶部的 **关闭** 按钮或简单地按 **Escape** 键来退出编辑模式。如果后续有需要，我们可以在树状视图中双击草图随时重新进入编辑模式。
-   我们来通过使用 <img alt="" src=images/PartDesign_Pad.svg  style="width:16px;"> [Pad](PartDesign_Pad.md) 工具并设定距离为 14.4 毫米来将其拉伸。其他选项可以保持默认值：

![](images/Exercise_lego_04.jpg )

**Pad** 的行为很像我们在上一章中使用的 [Extrude](Part_Extrude.md) 工具。然而，它们之间还是有一些差异的，主要的差异在于，Pad 不能被移动。它永远附着在它的草图上。如果你想改变 Pad 的位置，你必须移动基础草图。在当前的上下文中，我们希望确保没有任何东西会移出位置，这是一种额外的安全保障。

-   现在，我们将使用 <img alt="" src=images/PartDesign_Pocket.svg  style="width:16px;"> [Pocket](PartDesign_Pocket.md) 工具来挖掘块的内部，这是 PartDesign 版本的 [Part Cut](Part_Cut.md)。为了创建一个口袋，我们将在块的底部面创建一个草图，这将用于移除块的一部分。
-   在选中底部面的情况下，按下 <img alt="" src=images/Sketcher_NewSketch.svg  style="width:16px;"> [新建草图](Sketcher_NewSketch.md) 按钮。
-   在面上画一个矩形。

![](images/Exercise_lego_05.jpg )

-   我们现在将根据底面约束矩形。为了做到这一点，我们需要使用 <img alt="" src=images/Sketcher_External.svg  style="width:16px;"> [外部几何](Sketcher_External.md) 工具 \"导入\" 面的一些边缘。在底面的两条垂直线上使用此工具：

![](images/Exercise_lego_06.jpg )

你会注意到，只有基面的边缘才能通过这个工具添加。当你创建一个带参考面的草图时，会在该面和草图之间创建一个关系，这对于后续操作很重要。你总是可以稍后用 <img alt="" src=images/Sketcher_MapSketch.svg  style="width:16px;"> [映射草图](Sketcher_MapSketch.md) 工具将草图重新映射到另一个面。

-   外部几何并不是 \"真实\" 的，当我们离开编辑模式时，它将被隐藏。但是我们可以用它来放置约束。放置以下 4 个约束：
    -   选择矩形的左上点和导入线的顶点，添加一个 <img alt="" src=images/Constraint_HorizontalDistance.svg  style="width:16px;"> [水平距离约束](Sketcher_ConstrainDistanceX.md)，距离为 1.8 毫米
    -   再次选择矩形的左上点和导入线的顶点，添加一个 <img alt="" src=images/Constraint_VerticalDistance.svg  style="width:16px;"> [垂直距离约束](Sketcher_ConstrainDistanceY.md)，距离为 1.8 毫米
    -   选择矩形的右下点和右导入线的底点，添加一个 <img alt="" src=images/Constraint_HorizontalDistance.svg  style="width:16px;"> [水平距离约束](Sketcher_ConstrainDistanceX.md)，距离为 1.8 毫米
    -   再次选择矩形的右下点和右导入线的底点，添加一个 <img alt="" src=images/Constraint_VerticalDistance.svg  style="width:16px;"> [垂直距离约束](Sketcher_ConstrainDistanceY.md)，距离为 1.8 毫米

![](images/Exercise_lego_07.jpg )

-   退出编辑模式，我们现在可以进行口袋操作：在选中草图的情况下，按 <img alt="" src=images/PartDesign_Pocket.svg  style="width:16px;"> [Pocket](PartDesign_Pocket.md) 按钮。设置长度为 12.6 毫米，这将使我们垫的上面保持 1.8 毫米的厚度（记住，我们垫的总高度是 14.4 毫米）。

![](images/Exercise_lego_08.jpg )

-   我们现在将对顶面的 8 个点进行处理。为了做到这一点，由于它们是同一特性的重复，我们将使用 Part Design Workbench 的便捷工具 <img alt="" src=images/PartDesign_LinearPattern.svg  style="width:16px;"> [线性模式](PartDesign_LinearPattern.md)，它可以建模一次，然后重复形状。
-   首先，选择我们块的顶面

创建一个 <img alt="" src=images/Sketcher_NewSketch.svg  style="width:16px;"> [新草图](Sketcher_NewSketch.md)。

-   创建两个 <img alt="" src=images/Sketcher_Circle.svg  style="width:16px;"> [圆](Sketcher_CreateCircle.md)。
-   对于每个圆，选择它并添加一个半径约束 <img alt="" src=images/Sketcher_ConstrainRadius.svg  style="width:16px;"> [Radius Constraint](Sketcher_ConstrainRadius.md)，每个半径为 3.6 毫米
-   使用 <img alt="" src=images/Sketcher_External.svg  style="width:16px;"> [外部几何](Sketcher_External.md) 工具导入基面的左边缘。
-   在每个圆的中心点和导入边缘的角点之间放置两个垂直约束和两个水平约束，每个约束为 6 毫米，这样每个圆的中心就离面的边界 6 毫米：

![](images/Exercise_lego_09.jpg )

-   注意，当你锁定草图中所有物体的位置和尺寸时，它就会变得完全约束。这总是让你呆在安全的一面。你现在可以改变第一个草图，我们之后做的所有事情都会保持严密。
-   退出编辑模式，选择这个新的草图，创建一个厚度为 2.7 毫米的 <img alt="" src=images/PartDesign_Pad.svg  style="width:16px;"> [垫](PartDesign_Pad.md)：

![](images/Exercise_lego_10.jpg )

-   注意，和之前的口袋一样，由于我们使用了基块的顶面作为这个最新草图的基础，所以我们用这个草图做的任何 PartDesign 操作都会正确地建立在基础形状的顶部：这两个点并不是独立的对象，它们已经直接从我们的砖块中挤出来了。这就是使用 Part Design Workbench 的巨大优势，只要你注意始终在前一步的基础上建立一步，你实际上就在建立一个最终的实体对象。
-   我们现在可以将我们的两个点复制四次，这样我们就得到了八个。选择我们刚刚创建的最新的垫。
-   按下 <img alt="" src=images/PartDesign_LinearPattern.svg  style="width:16px;"> [线性模式](PartDesign_LinearPattern.md) 按钮。
-   在 \"水平草图轴\" 方向上，给出 36 毫米的长度（这是我们希望我们的副本适应的总 \"跨度\"），并使其成为 4 个实例：

![](images/Exercise_lego_11.jpg )

-   Once again, see that this is not just a duplication of an object, it is a \*feature\* of our shape that has been duplicated, the final object is still only one solid object.
-   Now let\'s work on the three \"tubes\" that fill the void we created on the bottom face. We have several possibilities: create a sketch with three circles, pad it then pocket it three times, or create a base sketch with one circle inside the other and pad it to form the complete tube already, or even other combinations. Like always in FreeCAD, there are many ways to achieve the same result. Sometimes one way will not work the way we want, and we must try other ways. Here, we will take the safest approach, and do things one step at a time.
-   Select the face that is at the bottom of the hollow space we carved earlier inside the block.
-   Create a new sketch, add a circle with a radius of 4.8825mm, import the left border of the face, and constrain it vertically and horizontally at 10.2mm from the upper corner of the face:

![](images/Exercise_lego_12.jpg )

If you have trouble to select features hiding part of the model can help. To hide a feature select it from tree view and press Space-key to toggle visibility.

-   Leave edit mode, and pad this sketch with a distance of 12.6mm
-   Create a linear pattern from this last pad, give it a length of 24mm and 3 occurrences. We now have three filled tubes filling the hollow space:

![](images/Exercise_lego_13.jpg )

-   Now let\'s make the final holes. Select the circular face of the first of our three \"pins\"
-   Create a new sketch, import the circular border of our face, create a circle with a radius constraint of 3.6mm, and add a <img alt="" src=images/Constraint_PointOnPoint.svg  style="width:16px;"> [Point on Point Constraint](Sketcher_ConstrainCoincident.md) between the center of the imported circle and our new circle. We now have a perfectly centered circle,and once again fully constrained:

![](images/Exercise_lego_14.jpg )

-   Leave edit mode, and create a pocket from this sketch, with a length of 12.6mm
-   Create a linear pattern from this pocket, with a length of 24mm and 3 occurrences. That\'s the last step, our piece of lego is now complete, so we can give it a nice color to mark our victory!

![](images/Exercise_lego_15.jpg )

You will notice that our modeling history (what appears in the tree view) has become quite long. This is precious because every single step of what we did can be changed later on. Adapting this model for another kind of brick, for example one with 2x2 dots, instead of 2x4, would be a piece of cake, we would just need to change a couple of dimensions and the number of occurrences in linear patterns. We could as easily create bigger pieces that don\'t exist in the original Lego game.

But we could also want to get rid of the history, for example if we are going to model a castle with this brick, and we don\'t want to have this whole history repeated 500 times in our file.

There are two simple ways to get rid of the history, one is using the [Create simple copy](Part_SimpleCopy.md) tool from the [Part Workbench](Part_Workbench.md), which will create a copy of our piece that doesn\'t depend anymore on the history (you can delete the whole history afterwards), the other way is exporting the piece as a STEP file and reimporting it.

**Assembling**

But the best of both worlds also exists, which is the [Assembly2 Workbench](https://github.com/hamish2014/FreeCAD_assembly2), an addon that can be installed from the [FreeCAD-addons](https://github.com/FreeCAD/FreeCAD-addons) repository. This Workbench is named \"2\" because there is also an official built-in Assembly Workbench in development, which is not ready yet. The Assembly2 Workbench, however, already works very well to construct assemblies, and also features a couple of object-to-object constraints which you can use to constrain the position of one object in relation to another. In the example below, however, it will be quicker and easier to position the pieces using <img alt="" src=images/Draft_Move.svg  style="width:16px;"> [Draft Move](Draft_Move.md) and <img alt="" src=images/Draft_Rotate.svg  style="width:16px;"> [Draft Rotate](Draft_Rotate.md) than using the Assembly2 constraints.

-   Save the file as it is now
-   Install the [Assembly2 Workbench](https://github.com/hamish2014/FreeCAD_assembly2) and restart FreeCAD
-   Create a new empty document
-   Switch to the Assembly2 workbench
-   Press the **Import a part from another FreeCAD document** button
-   Select the file we saved above
-   The final piece will be imported in the current document. The Assembly2 workbench will determine automatically what is the final piece in our file that needs to be used, and the new object stays linked to the file. If we go back and modify the contents of the first file, we can press the **Update parts imported into the assembly** button to update the pieces here.
-   By using the **Import a part from another FreeCAD document** button several times, and moving and rotating the pieces (with the Draft tools or by manipulating their Placement property), we can quickly create a small assembly:

![](images/Exercise_lego_16.jpg )

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
