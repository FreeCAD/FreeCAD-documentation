# Manual:Traditional modeling, the CSG way/zh-cn
<div class="mw-translate-fuzzy">





</div>


{{Manual:TOC/zh-cn}}

CSG 代表[构造实体几何](https://en.wikipedia.org/wiki/Constructive_solid_geometry)，描述了使用实体 3D 几何的最基本方式，即使用诸如并集、差集、或交集之类的布尔运算，向实体对象添加和移除部分实体，达成创建复杂对象的目的。


<div class="mw-translate-fuzzy">

本手册前面提到，一方面，FreeCAD 可以处理多种类型的几何体；另一方面，我们使用 FreeCAD 设计的 3D 对象，是真实世界的对象。因此，这里首选的、最有用的类型，毫无疑问，是实体，是 [BREP](https://en.wikipedia.org/wiki/Boundary_representation) 几何体，主要由[Part 工作台来处理](Part_Workbench.md)。 [多边形网格](https://en.wikipedia.org/wiki/Polygon_mesh)仅由点和三角形构成，与此不同，BREP 对象的面由数学曲线定义，无论缩放比例如何，都保证有绝对的精度。


</div>

![](images/Mesh_vs_brep.jpg )

两者之间的差异，类似于位图和矢量图像之间的差异。与位图图像一样，多边形网格的曲面划分为一系列的点。如果你贴近观察，或者将它打印得非常大，你会发现它不是曲面而是切面。在矢量图像和 BREP 数据里，曲线上任何点的位置都不会存储在几何体中，而是在运行中即时精确计算。

在 FreeCAD 中，所有基于 BREP 的几何都由另一个开源软件 [OpenCasCade](https://en.wikipedia.org/wiki/Open_Cascade_Technology) 处理。FreeCAD 与 OpenCasCade 内核之间的主要接口是 Part 工作台。大多数其他工作台在 Part 工作台的基础上构建其功能。

其他工作台通常提供了更高级的工具来构建和操作几何体，实际上都操纵的是 Part 对象，因此非常有必要了解这些对象的内部工作机制，并且能够使用 Part 工具。一些更智能的工具无法正确解决的问题，Part 工具因为更简单，经常可以帮你解决。

为了说明 Part 工作台的工作原理，我们将仅使用 CSG 操作对模型建模（螺钉除外，因为我们将使用一个插件，里面有尺寸，在下一章中介绍）。

![](images/Exercise_table_complete.jpg )


<div class="mw-translate-fuzzy">

让我们创建一个新文档（ **Ctrl + N** 或菜单 **File -\> New Document**）来保存我们设计的桌子。该文档最初在 Combo View 面板的 Model 选项卡中称为"unnamed"，但如果将文档（ **Ctrl+Shift+S** 或 菜单 File -\> Save As）保存为称作"table.fcstd" 的新 FreeCAD 文档，文档便重命名为"table"，更清楚地标识了该项目。


</div>

现在我们切换到 Part 工作台，开始创建我们的第一个桌腿。


<div class="mw-translate-fuzzy">

-   按下 <img alt="" src=images/Part_Box.png  style="width:16px;"> **Cube** 按钮
-   选择 Cube，然后设置以下属性（在 **Data** 选项卡中）：
    -   长度：80mm（或 8cm，或 0.8m，FreeCAD 可以使用任何单位）
    -   宽度：80mm
    -   高度：75cm
-   按 **Ctrl+C** 然后按 **Ctrl+V**（或菜单 Edit -\> Copy 然后 Paste）复制 Cube（没有任何变化，因为第二个对象与第一个重合。）
-   选择已创建的名为 Cube001 的新对象（单击左侧 **Model** 选项卡中的 Cube001）
-   编辑其 Placement 属性来更改其位置：
    -   位置 x：8mm
    -   位置 y：8mm


</div>

你应该得到了两个高高的立方体，一个与另一个相距 8毫米。

![](images/Exercise_table_01.jpg )


<div class="mw-translate-fuzzy">

现在我们可以从另一个中减去一个：选择**第一个**，即**保留**的那个，然后，按下 CTRL 键，选择**另一个**，即将被**减去**的那个（顺序很重要），然后按下 <img alt="" src=images/Part_Cut.png  style="width:16px;"> **Cut** 按钮。


</div>

![](images/Exercise_table_02.jpg )

注意创建的对象，称为"Cut"。"Cut"仍然包含我们用作运算子的两个立方体。实际上，文档中仍然存在两个"Cube\"，仅被隐藏并在树视图中的"Cut"对象的分组中，仍然可以通过展开"Cut"对象旁边的箭头来选择它们。如果需要，可以右键单击来将它们显示出来，或更改它们的属性。

You can use Cut -tool and other Boolean tools also through \"Combo view\" with <img alt="" src=images/Part_Boolean.svg  style="width:16px;"> [Boolean](Part_Boolean.md). It gives more explicit but longer way to do it.

-   我们复制基础立方体 6 次，创建另外三个脚。由于它仍然复制在剪贴板里，可以简单地粘贴（Ctrl + V）6次。

然后改变它们的位置，数据如下：

-   -   Cube002：x：0，y：80cm
    -   Cube003：x：8mm，y：79.2cm
    -   Cube004：x：120cm，y：0
    -   Cube005：x：119.2cm，y：8mm
    -   Cube006：x：120cm，y：80cm
    -   Cube007：x：119.2cm，y：79.2cm

-   做另外三个切割，首先选择"host"立方体，然后选择要切除的立方体。我们有了四个 Cut 对象。

![](images/Exercise_table_03.jpg )

你可能一直在想，可以将完整的脚重复三次，而不必复制基础立方体六次。完全正确，在 FreeCAD 中，有很多方法可以实现相同的结果。这是一个宝贵的经验，值得记住。因为随着我们接触到更复杂的对象，某些操作可能无法提供正确的结果，经常需要尝试其他方法。


<div class="mw-translate-fuzzy">

-   我们使用相同的 Cut 方法为螺钉打孔。由于需要 8 个洞，每个脚两个，我们本来可以制作 8 个物体作减法。然而让我们探索一下其他方法，制作4个管子，这些管子被两个脚重复使用。所以让我们用 <img alt="" src=images/Part_Cylinder.png  style="width:16px;"> **Cylinder** 创建四个管子。这次同样的，你可以先造一个，然后作复制。给所有圆柱体的半径设为 6mm。需要旋转它们，这也是通过 Data 选项卡下的**Placement** 属性完成的。\'\'（ **注意**：在设置 Angle *之前* 更改 Axis 属性，否则旋转不会生效）\'\' ：
    -   Cylinder: height: 130cm, angle: 90°, axis: x:0,y:1,z:0, position: x:-10mm, y:40mm, z:72cm
    -   Cylinder001: height: 130cm, angle: 90°, axis: x:0,y:1,z:0, position: x:-10mm, y:84cm, z:72cm
    -   Cylinder002: height: 90cm, angle: 90°, axis: x:-1,y:0,z:0, position: x:40mm, y:-10mm, z:70cm
    -   Cylinder003: height: 90cm, angle: 90°, axis: x:-1,y:0,z:0, position: x:124cm, y:-10mm, z:70cm


</div>

![](images/Exercise_table_04.jpg )

注意到圆柱体比需要的长一些。这是因为，与所有基于实体的 3D 应用程序一样，FreeCAD 中的布尔运算有时对于面与面重合的情况过于敏感，可能会失败。通过做得长一些，可以让自己处于安全的一侧。

-   下面做差集。选择第一条腿，然后按住 CTRL 键，选择其中一根穿过它的管，按 **Cut** 按钮。孔做好了，管被隐藏。在树视图中展开穿好孔的脚，就会找到这根管。
-   选择此隐藏管穿过的另一只脚，然后重复上面的操作，这次按住 Ctrl，在树视图中选择管，因为它在 3D 视图中隐藏了（也可以再次显示它，然后在 3D 视图中选择它）。对其它的脚重复这一操作，直到每个脚都有两个孔。

![](images/Exercise_table_05.jpg )

你看，做每只脚都是一长串的操作。所有这些操作都保持着参数化，可以随时更改任意操作的任何参数。在FreeCAD 中，常常将这一堆参数化的操作称为"建模历史"，因为它实际上包含了你所执行操作的所有历史记录。

FreeCAD 的另一个特点是 3D 对象的概念和 3D 操作的概念 倾向于融合为同一个东西。剪切既是一个操作，同时也是由此操作产生的 3D 对象。在 FreeCAD 中，这称为"特征"，而不是对象或操作。

-   下面做桌面，就是一个简单的木块。另造一个 **Box**，长度：126cm，宽度：86cm，高度：8cm，位置：x：10mm，y：10mm，z：67cm。在 **View** 选项卡中，更改其 **Shape Color** 属性，改为漂亮的褐色，木质的颜色。

![](images/Exercise_table_06.jpg )

请注意，虽然腿的厚度为 8mm，但我们将它放置在距离桌子 10mm 处，在它们之间留出了 2mm。 当然，这不是必需的，不会发生在真正的桌子上。但在"组装"模型中这种操作是常见的，可以帮助那些看模型的人理解哪些是独立的部分，需要以后手动连接在一起。

现在我们的五件部品已经完成了，是时候给他们更专有的，而不是"Cut015"这类的名称了。右键单击树视图中的对象（或按 **F2**），可以将它们重命名，改为对自己，或以后打开文件的其他人，更有意义的内容。人们常说，相比于你建模它们的方式，简单地给你的对象赋予正确的名称要重要得多。


<div class="mw-translate-fuzzy">

-   下面安装几颗螺丝。有一个由 FreeCAD 社区成员开发的非常有用的插件，称为[紧固件](https://github.com/shaise/FreeCAD_FastenersWB)，你可以在[FreeCAD 插件](https://github.com/FreeCAD/FreeCAD-addons)库中找到。这使得插入螺钉变得非常容易。其他工作台的安装很容易，在插件页面上有说明。
-   Fasteners 工作台安装完毕并重新启动 FreeCAD 后，它将显示在工作台列表中，可以切换进去。要在一个孔中添加螺钉，首先选择这个孔的圆形边缘。


</div>

![](images/Exercise_table_07.jpg )

然后我们可以按下紧固件工作台上的一个螺钉按钮，例如 **EN 1665 Hexagon bolt with flanges, heavy series**。螺钉放好，与孔对齐，并自动选择直径以匹配这个孔的尺寸。有时螺钉是倒置的，可以通过翻转其 **invert** 特性来纠正。也可以将其偏移设置为 2mm，遵循在桌面和桌腿之间使用的同样的规则。

![](images/Exercise_table_08.jpg )

-   对所有孔重复此操作，桌子就完成了。

**Part对象的内部结构**

如上所述，FreeCAD 中不仅可以选择整个对象，还可以选择其中的一部分，例如螺孔的圆形边框。现在是时候快速了解一下在 FreeCAD 内部如何构建 Part 对象了。生成 Part 几何体的每个工作台都基于以下内容：

-   **顶点**：是构建所有其它对象用的点（通常是端点）。例如，一条线段有两个顶点。
-   **边**：是线性的几何体，如直线，圆弧，椭圆或 [NURBS](https://en.wikipedia.org/wiki/Non-uniform_rational_B-spline) 曲线，通常有两个顶点，但是某些特殊情况下只有一个（例如一个封闭的圆圈）。
-   **线**：是在端点相连接的一系列边，可以包含任何类型的边，可以闭合，也可以不闭合。
-   **面**：可以是平面的或弯曲的，可以由一个闭合的线所形成，作为面的边界，或者在面具有孔的情况下，由多个边来形成面。
-   **壳**：只是在边相连接的一组面，可以是开放的，也可以是封闭的。
-   **实体**：当一个壳紧紧关闭时，或者说没有"泄漏"，就成了实体。实体有内外的概念。许多工作台依赖于此，确保生成的对象可以在现实世界中建造出来。
-   **复合物**：是其他形状的聚集体。无论那些形状的原始类型如何，最终形成了这个单一形状。

在 3D 视图中，可以选择单个**vertices**, **edges** 或 **faces**。选择其中一个即选中了整个对象。

**关于共享设计的说明**

看到上面的桌子，你也许认为它的设计不好。用桌面固定桌腿的方式可能太弱了。你也许想要添加加固件，或者只是有其他想法可以使其更好。这里，分享就有趣了。你可以从下面的链接下载本练习中制作的文件，修改它，让它更好。然后，如果你共享改进后的文件，其他人便可能会进一步改善它，或者在他们的项目中使用这个精心设计的桌子。你的设计可能会给别人提供其他想法，也许会有助于一点点地创造一个更美好的世界......

**下载**

-   本练习中生成的文件：https://github.com/yorikvanhavre/FreeCAD-manual/blob/master/files/table.FCStd

**延伸阅读**


<div class="mw-translate-fuzzy">

-   [Part 工作台](Part_Workbench.md)
-   [FreeCAD 插件库](https://github.com/FreeCAD/FreeCAD-addons)
-   [Fasteners 工作台](https://github.com/shaise/FreeCAD_FastenersWB)


</div>


<div class="mw-translate-fuzzy">





</div>



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Tutorials](Category_Tutorials.md) > Manual:Traditional modeling, the CSG way/zh-cn
