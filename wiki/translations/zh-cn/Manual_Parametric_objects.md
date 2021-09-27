# Manual:Parametric objects/zh-cn
<div class="mw-translate-fuzzy">





</div>


{{Manual:TOC}}

FreeCAD 专为参数化建模而设计。这意味着所创建的几何体不是可以自由雕刻的那种，而是由规则和参数而生成的。例如，可以凭半径和高度生成圆柱体。有了这两个参数，程序便具有了足够的信息来构建这个圆柱体。

FreeCAD 中的参数对象实际上是一小段程序，只要其中一个参数发生变化就会运行。对象可以有很多不同类型的参数：数字（整数，如1,2,3；或浮点值，如3.1416），真实世界的尺寸（1毫米，2.4米，4.5英尺），（x，y，z）坐标，文本字符串（"hello!"），等等。甚至，参数可以是另一个对象。

最后一种类型允许快速构建复杂的操作链，每个新对象以前一个为基础，向其添加新特征。

在下面的示例中，实心立方体（Pad）基于矩形 2D 形状（草图）并拉伸到某个距离。用这两个属性，它通过将基本形状拉伸到给定距离来生成实体形状。然后，就可以使用此对象作为进一步操作的基础，例如在其中一个面上绘制新的 2D 形状（Sketch001），然后做减法拉伸（Pocket），直到获得最终对象。

所有中间操作（2D 形状，凸台，凹坑等）仍然存在，您仍然可以随时更改其任何参数。需要的时候，整个链条将被重建（重新计算）。

![](images/Parametric_objects.jpg )

需要知道两件重要的事情：


<div class="mw-translate-fuzzy">

1.  重新计算并不总是自动的。繁重的操作可能会修改文档的大部分内容，因此需要一些时间，不会自动执行。这里的做法是，对象（以及依赖于它的所有对象）将被打上标记，准备重新计算（树视图中的对象会出现一个小的蓝色图标）。然后，您必须按下重新计算按钮（或** Edit -> Refresh **）以重新计算所有标记的对象。
2.  依赖关系树必须始终单方向流动，禁止循环。（[参见 DAG ](Glossary#Directed_Acyclic_Graph.md)。）A 对象依赖于 B 对象，B 依赖于 C 对象。但是不能是 A 依赖于 B，B 又依赖于 A。这会是循环依赖。但是，您可以拥有许多依赖于同一对象的对象，例如，对象 B 和 C 都依赖于 A。菜单** Tools -> Dependency graph **显示了类似上图中的依赖关系图。检查问题时它可能会很有用。


</div>

并非所有 FreeCAD 中的对象都是参数化的。通常，从其他文件导入的几何体不包含任何参数，它是简单的非参数化的对象。但是，这些通常可以用作新创建的参数化对象的基础或起点，当然，这取决于参数化对象的需要和导入的几何体的质量。

但是，所有对象，无论是否参数化，都有一些基本的参数。例如 Name，在文档中是唯一的，无法编辑；例如 Label，是用户定义名称，可以编辑；例如 [placement](placement.md)，描述了对象在3D空间中的位置。

最后，有一点值得提醒：[很容易在 python 中编程自定义参数化对象](Scripted_objects.md)。

**延伸阅读**


<div class="mw-translate-fuzzy">

-   [属性编辑器](Property_editor.md)
-   [怎样为参数化对象编程](Scripted_objects.md)
-   [在 FreeCAD 中定位对象](Placement.md)
-   [启用依赖关系图](Std_DependencyGraph.md)


</div>


<div class="mw-translate-fuzzy">





</div>

_ _

---
[documentation index](../README.md) > [Poweruser Documentation](Category_Poweruser Documentation.md) > Manual:Parametric objects/zh-cn
