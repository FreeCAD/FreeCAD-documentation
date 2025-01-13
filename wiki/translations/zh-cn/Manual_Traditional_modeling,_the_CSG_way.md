# Manual:Traditional modeling, the CSG way/zh-cn
{{Manual:TOC}}


<div class="mw-translate-fuzzy">

CSG 代表[Constructive_solid_geometry_构造实体几何](https://en.wikipedia.org/wiki/Constructive_solid_geometry)，描述了处理实体 3D 几何的最基本方法，即通过使用布尔运算（如并集、差集或交集）向/从实体中添加和删除一块来创建复杂对象。


</div>


<div class="mw-translate-fuzzy">

正如我们在本手册中早些时候看到的那样，FreeCAD 可以处理许多类型的几何图形，但对于我们想要使用FreeCAD 设计的那种 3D 物体（即现实世界的物体），首选和最有用的类型无疑是实体 [BREP](https://en.wikipedia.org/wiki/Boundary_representation) 几何图形，主要由[Part 工作台](Part_Workbench.md)处理。与[多边形网格](https://en.wikipedia.org/wiki/Polygon_mesh)不同，BREP 对象的面由数学曲线定义，这实现了在任何尺度下的绝对精度。


</div>


<div class="mw-translate-fuzzy">

![](images/Mesh_vs_brep.jpg )


</div>


<div class="mw-translate-fuzzy">

这两者之间的区别类似于位图和矢量图像之间的区别。与位图图像一样，多边形网格的曲面被分成一系列点。如果您仔细观察，或者将其放大打印，您将看到的不是曲面而是由许多平面组成的表面。在矢量图像和 BREP 数据中，曲线上任何点的位置不是存储在几何图形中，而是根据需要即时计算，具有准确的精度。


</div>


<div class="mw-translate-fuzzy">

在 FreeCAD 中，所有基于 BREP 的几何都由另一个开源软件 [OpenCasCade](https://en.wikipedia.org/wiki/Open_Cascade_Technology) 处理。FreeCAD 与 OpenCasCade 内核之间的主要接口是 Part 工作台。大多数其他工作台在 Part 工作台的基础上构建其功能。 在FreeCAD中，所有基于 BREP 的几何图形都由另一个开源软件[OpenCasCade](https://en.wikipedia.org/wiki/Open_Cascade_Technology) 处理。FreeCAD 和 OpenCasCade 内核之间的主要接口是 Part 工作台。大多数其他工作台都在 Part 工作台的基础上构建其功能。


</div>

While other workbenches in FreeCAD, such as the Part Design and Surface Workbenches, offer more advanced tools for building and manipulating geometry, they rely on the underlying Part Workbench. Understanding how Part objects work internally and being adept with the basic Part tools is beneficial. Often, these simpler tools can resolve issues that more complex tools may not handle effectively.

![](images/Mesh_vs_brep.jpg )

The difference between the two can be compared to the difference between bitmap and vector images. As with bitmap images, polygon meshes have their curved surfaces divided into a series of points. If you look at it closely or print it very large, you will see not a curved but a faceted surface. In both vector images and BREP data, the position of any point on a curve is not stored in the geometry but calculated on the fly, with exact precision.


<div class="mw-translate-fuzzy">

为了说明 Part 工作台的工作原理，我们将仅使用 CSG 操作（除了螺钉，我们将使用其中一个插件，以及尺寸，我们将在下一章中看到）来建模这张桌子：


</div>

![](images/Exercise_table_complete.jpg )


<div class="mw-translate-fuzzy">

让我们创建一个新文档（使用**Ctrl+N**或菜单文件 → 新建文档），以保存我们的桌子设计。文档最初在 Combo View 面板的 Model 选项卡中称为"无标题"，但是如果您将文档保存（使用**Ctrl+Shift+S**或菜单文件 → 另存为），将其保存为名为" table.FCStd"的新 FreeCAD 文档，该文档将被重命名为"table"，这更清楚地标识了项目。


</div>

现在我们切换到 Part 工作台，开始创建我们的第一个桌腿。


<div class="mw-translate-fuzzy">

-   点击<img alt="" src=images/Part_Box.svg  style="width:16px;"> **立方体**按钮
-   选择立方体，然后设置以下属性（在"数据"选项卡中）：
    -   长度：80 毫米（或 8 厘米，或 0.8 米，FreeCAD 可以使用任何单位）
    -   宽度：80 毫米
    -   高度：75 厘米
-   通过按 **Ctrl + C** 然后 **Ctrl + V** 复制立方体（或菜单 编辑 → 复制和粘贴）（不会出现任何变化，因为第二个对象覆盖了第一个对象）。
-   选择新创建的名为 Cube001 的对象（在左侧的 Model 选项卡中单击 Cube001）
-   通过编辑其放置属性更改其位置：
    -   位置 x：8 毫米
    -   位置 y：8 毫米


</div>

你应该得到了两个高高的立方体，一个与另一个相距 8 毫米。

![](images/Exercise_table_01.jpg )

-   现在我们可以将一个几何体从另一个几何体中减去：选择要**保留**的**第一个**体，然后按住CTRL键，选择要**减去**的**另一个**体（顺序很重要），然后按下<img alt="" src=images/Part_Cut.svg  style="width:16px;"> **剪切**按钮：

![](images/Exercise_table_02.jpg )

注意创建的对象，称为"Cut"。"Cut"仍然包含我们用作运算子的两个立方体。实际上，文档中仍然存在两个"Cube\"，仅被隐藏并在树视图中的"Cut"对象的分组中，仍然可以通过展开"Cut"对象旁边的箭头来选择它们。如果需要，可以右键单击来将它们显示出来，或更改它们的属性。


<div class="mw-translate-fuzzy">

您还可以通过"组合视图" <img alt="" src=images/Part_Boolean.svg  style="width:16px;"> [布尔运算](Part_Boolean.md) 来使用剪切工具和其他布尔工具。这给出了更明确但更费力的方式来完成它。


</div>


<div class="mw-translate-fuzzy">

-   我们复制基础立方体 6 次，创建另外三个脚。由于它仍然复制在剪贴板里，可以简单地粘贴（Ctrl + V）6次。

然后改变它们的位置，数据如下：

-   -   Cube002：x：0，y：80cm
    -   Cube003：x：8mm，y：79.2cm
    -   Cube004：x：120cm，y：0
    -   Cube005：x：119.2cm，y：8mm
    -   Cube006：x：120cm，y：80cm
    -   Cube007：x：119.2cm，y：79.2cm


</div>


<div class="mw-translate-fuzzy">

-   做另外三个切割，首先选择"host"立方体，然后选择要切除的立方体。我们有了四个 Cut 对象。


</div>

![](images/Exercise_table_03.jpg )


<div class="mw-translate-fuzzy">

你可能一直在想，可以将完整的脚重复三次，而不必复制基础立方体六次。完全正确，在 FreeCAD 中，有很多方法可以实现相同的结果。这是一个宝贵的经验，值得记住。因为随着我们接触到更复杂的对象，某些操作可能无法提供正确的结果，经常需要尝试其他方法。


</div>


<div class="mw-translate-fuzzy">

-   现在我们将使用相同的 Cut 方法为螺钉制作孔。由于我们需要 8 个孔，每个桌脚需要两个，我们可以制作 8 个要减去的对象。相反，让我们探索其他方法，并制作 4 个管道，这些管道将由两个脚重复使用。因此，让我们使用 <img alt="" src=images/Part_Cylinder.svg  style="width:16px;"> **圆柱体** 工具创建四个管道。您可以再次只制作一个圆柱体，然后将其复制。给所有圆柱体一个半径为 6 毫米。这次，我们需要旋转它们，这也是通过数据选项卡下的 **放置** 属性完成的 *（**注意：** 在设置角度之前更改轴属性，否则旋转将不会应用）*：
    -   Cylinder：高度：130cm，角度：90°，轴：x:0，y:1，z:0，位置：x：-10mm，y：40mm，z：72cm
    -   Cylinder001：高度：130cm，角度：90°，轴：x:0，y:1，z:0，位置：x：-10mm，y：84cm，z：72cm
    -   Cylinder002：高度：90cm，角度：90°，轴：x:-1，y:0，z:0，位置：x：40mm，y：-10mm，z：70cm
    -   Cylinder003：高度：90cm，角度：90°，轴：x:-1，y:0，z:0，位置：x：124cm，y：-10mm，z：70cm


</div>

![](images/Exercise_table_04.jpg )

您会注意到圆柱体比需要的稍长一点。这是因为，就像所有基于实体的3D应用程序一样，FreeCAD中的布尔运算有时对面对面的情况过于敏感，可能会失败。通过这样做，我们可以保险一些。


<div class="mw-translate-fuzzy">

-   现在让我们进行减法。选择第一个桌脚，然后按住 CTRL 键，选择穿过它的一个管道，按下 **剪切** 按钮。孔将被制作，管道将被隐藏。通过展开穿过的脚，在树视图中找到它。
-   选择另一个受到此隐藏管道穿透的桌脚，然后重复此操作，这次使用 Ctrl+ 在树视图中选择管道，因为它在 3D 视图中被隐藏了（您也可以使其再次可见并在 3D 视图中选择它）。对其他脚重复此操作，直到每个脚都有两个孔：


</div>

![](images/Exercise_table_05.jpg )

正如您所看到的，每个桌脚已经变成了一系列相当长的操作。所有这些操作都是参数化的，您可以随时更改任何早期操作的任何参数。在 FreeCAD 中，我们经常将这个堆栈称为"建模历史"，因为它实际上记载了您执行的所有操作的历史记录。

FreeCAD 的另一个特点是，3D 对象的概念和 3D 操作的概念往往融为一体。剪切既是一种操作，也是由此操作产生的 3D 对象。在 FreeCAD 中，这被称为"特征"（feature），而不是对象或操作。


<div class="mw-translate-fuzzy">

-   现在让我们制作桌面，它将是一个简单的木块，让我们使用另一个 **Box** 工具，长度：126cm，宽度：86cm，高度：8cm，位置：x：10mm，y：10mm，z：67cm。在 **视图** 选项卡中，您可以通过更改其 **形状颜色** 属性，使其具有漂亮的棕色木材质感：


</div>

现在我们的五个零件都完成了，是一个好时机给它们取比"Cut015"更恰当的名称。通过在树形视图中右键单击对象（或按下"F2"键），您可以将它们重命名为对您自己或稍后打开文件的其他人更有意义的名称。人们常说，为对象命名比建模的方式还重要。

-   我们现在将安装一些螺丝。FreeCAD 社区的一位成员开发了一个非常有用的插件，名为"Fasteners"，您可以在[FreeCAD 插件](https://github.com/FreeCAD/FreeCAD-addons)仓库中找到它。它能够使螺丝的插入变得非常容易。安装附加的工作台很容易，可以在[插件页面](Std_AddonMgr.md)上找到说明。

-   安装完"Fasteners"工作台并重新启动 FreeCAD 后，它将出现在工作台列表中，我们可以切换到它。将螺丝添加到我们的孔中是通过首先选择我们孔的圆形边缘来完成的：


<div class="mw-translate-fuzzy">

![](images/Exercise_table_07.jpg )


</div>


<div class="mw-translate-fuzzy">

-   然后，我们可以按下"Fasteners"工作台中的一个螺丝按钮，例如**EN 1665 Hexagon bolt with flanges, heavy series**。螺丝将被放置并与我们的孔对齐，直径将自动选择以匹配我们孔的大小。有时螺丝会被倒置放置，我们可以通过翻转其"invert"属性来进行更正。我们也可以将其偏移设置为2毫米，以遵循我们在桌面和脚之间使用的相同规则：


</div>


<div class="mw-translate-fuzzy">

![](images/Exercise_table_08.jpg )


</div>

-   对所有孔重复此操作，桌子就完成了。


<div class="mw-translate-fuzzy">

**Part对象的内部结构**


</div>


<div class="mw-translate-fuzzy">

正如我们之前看到的，FreeCAD 中不仅可以选择整个对象，还可以选择它们的一部分，例如我们的螺丝孔的圆形边界。现在是一个快速了解 Part 对象如何在内部构建的好时机。每个生成 Part 几何体的工作台都将基于这些内容：


</div>

![](images/Tabble_alternative_complete.png )

**The internal structure of Part objects**

As we saw above, it is possible in FreeCAD to select not only whole objects but parts of them, such as the circular border of our screw hole. This is a good time to have a quick look at how Part objects are constructed internally. Every workbench that produces Part geometry will be based on these:

-   **Vertices**: These are points (usually endpoints) on which all the rest is built. For example, a line has two vertices.
-   **Edges**: the edges are linear geometry like lines, arcs, ellipses or [NURBS](https://en.wikipedia.org/wiki/Non-uniform_rational_B-spline) curves. They usually have two vertices, but some special cases have only one (a closed circle for example).
-   **Wires**: A wire is a sequence of edges connected by their endpoints. It can contain edges of any type, and it can be closed or not.
-   **Faces**: Faces can be planar or curved, and can be formed by one closed wire, which forms the border of the face, or more than one, in case the face has holes.
-   **Shells**: Shells are simply a group of faces connected by their edges. It can be open or closed.
-   **Solids**: When a shell is tightly closed, that is, it has no \"leak\", it becomes a solid. Solids carry the notion of inside and outside. Many workbenches rely on this to make sure the objects they produce can be built in the real world.
-   **Compounds**: Compounds are simply aggregates of other shapes, no matter their type, into a single shape.

In the 3D view, you can select individual **vertices**, **edges** or **faces**. Selecting one of these also selects the whole object.

**关于共享设计的说明**


<div class="mw-translate-fuzzy">

看到上面的桌子，您可能会认为它的设计不太好。桌面与脚的紧固可能太弱了。您可能想要添加加固件，或者您有其他想法使其更好。这就是共享变得有趣的地方。您可以从下面的链接下载本次练习中制作的文件，并修改它使其更好。然后，如果您分享这个改进的文件，其他人可能能够使它变得更好，或者在他们的项目中使用您精心设计的桌子。您的设计可能会给其他人带来新的想法，也许这将有助于让世界变得更好\...\...


</div>

**下载**

-   本练习中生成的文件：https://github.com/yorikvanhavre/FreeCAD-manual/blob/master/files/table.FCStd

**延伸阅读**

-   [Part 工作台](Part_Workbench.md)
-   [FreeCAD 插件库](https://github.com/FreeCAD/FreeCAD-addons)
-   [Fasteners 工作台](https://github.com/shaise/FreeCAD_FastenersWB)



---
⏵ [documentation index](../README.md) > [Tutorials](Category_Tutorials.md) > Manual:Traditional modeling, the CSG way/zh-cn
