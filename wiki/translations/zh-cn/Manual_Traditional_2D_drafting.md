# Manual:Traditional 2D drafting/zh-cn
<div class="mw-translate-fuzzy">





</div>


{{Manual:TOC/zh-cn}}


<div class="mw-translate-fuzzy">

你对 FreeCAD 感兴趣，可能因为你有技术绘图经验，例如使用过 _，包含大多数 2D CAD 应用程序中都有的工具。


</div>


<div class="mw-translate-fuzzy">

Draft 工作台虽然继承了传统 2D CAD 的工作方式，但并不局限于 2D 领域。Draft 工作台的所有工具都可以在整个 3D 空间中工作。许多 Draft 工具，例如，<img alt="" src=images/Draft_Move.png  style="width:16px;"> _ FreeCAD 中使用广泛，因为比起手动更改位置参数，Move 和 Rotate 更直观。


</div>


<div class="mw-translate-fuzzy">

在 Draft 工作台提供的工具中，你会发现传统的绘图工具，像<img alt="" src=images/Draft_Line.png  style="width:16px;"> _, or <img alt="" src=images/Draft_Wire.png  style="width:16px;"> _, <img alt="" src=images/Draft_Rotate.png  style="width:16px;"> _, a _, <img alt="" src=images/Draft_Rotate.png  style="width:16px;"> _, a [working plane/grid system](Draft_SelectPlane/zh-cn.md)，让你精确定义正在工作的平面，以及一个完整的 [snapping system](Draft_Snap/zh-cn.md) ，使得相对于彼此绘制和定位元素非常容易。


</div>

为了展示 Draft 的工作流程和能力范围，我们做一个简单的练习，结果将是这个小图，一个只包含厨房顶部的小房子的平面图（一个非常荒谬的平面图，但我们可以在这里做我们想做的事，不是够了吗？）：

![](images/Exercise_cabin_01.jpg )

-   切换到 Draft 工作台
-   与所有技术绘图应用程序一样，正确设置环境是明智的，它将为你节省大量时间。在菜单 **Edit → Preferences → Draft** 根据自己的喜好配置[grid and working plane](Draft_SelectPlane/zh-cn.md), [Text](Draft_Text/zh-cn.md) 和 [Dimension](Draft_Dimension/zh-cn.md)。 但是，在本练习中，我们将这些设置保留默认值。

![](images/Freecad_draft_options_01.jpg )

-   你可能需要注意一个选项，它很霸道：\"**Fill objects with faces whenever possible**\" 选项。如果选中这个选项，默认情况下 FreeCAD 将用面来填充诸如矩形或圆形这类的闭合对象，这样可能就难以捕捉到底层对象了。你可以立即关闭此选项，或者稍后关闭每个单独对象的 \"**Make Face**\" 属性，以防止它们创建面。

-   Draft 工作台还有两个特殊的工具栏。一个具是 **visual settings**，可以更改当前工作平面，打开/关闭 [construction mode](Draft_ToggleConstructionMode/zh-cn.md)，设置要用于新对象的线条颜色、面的颜色、线宽和文本大小。另一个是**snap locations**，可以打开/关闭网格并设置/取消设置单个 [Snap locations](Draft_Snap/zh-cn.md)。

![](images/Draft_toolbars.jpg )

-   打开所有捕捉按钮是会带来方便，但也会使绘图变慢，因为移动鼠标光标时需要进行更多的计算。通常只保留实际使用的那些就好了。


<div class="mw-translate-fuzzy">

-   我们先打开 **construction mode**，这样可以绘制一些引导线，在其基础上绘制最终的几何图形。
-   愿意的话，将 **working plane** 设置为 **XY**。 这样无论当前视图如何，工作平面都不会改变。如果没有设置，工作平面将自动适应当前视图，只要想在 XY（地面）平面上绘图，都应该小心注意保持在顶视图。
-   然后，选择 <img alt="" src=images/Draft_Rectangle.png  style="width:16px;"> [Rectangle](Draft_Rectangle/zh-cn.md) 工具并绘制一个矩形，从点（0,0,0）开始，2 米乘 2 米（将 Z 保持为零）。请注意，大多数 Draft 命令都完全可以使用双字母快捷键从键盘执行，而无需鼠标。我们的第一个 2x2m 的矩形可以这样完成：re 0 **Enter** 0 **Enter** 0 **Enter** 2m **Enter** 2m **Enter** 0 **Enter**。
-   将矩形向内复制 15cm，使用 <img alt="" src=images/Draft_Offset.png  style="width:16px;"> [Offset](Draft_Offset/zh-cn.md) 工具，打开复制模式，并给出距离 15cm。


</div>

![](images/Exercise_cabin_02.jpg )


<div class="mw-translate-fuzzy">

-   接下来，绘制几条垂直的线来定义门窗的位置，使用 <img alt="" src=images/Draft_Line.png  style="width:16px;"> [Line](Draft_Line/zh-cn.md) 工具。 这些线与两个矩形的交叉点为我们提供帮助，来捕捉墙壁的位置。从点（15cm，1m，0）到点（15cm，3m，0）绘制第一条线。
-   使用 <img alt="" src=images/Draft_Move.png  style="width:16px;"> [Move](Draft_Move/zh-cn.md) 工具，打开 Copy 模式,将这条线复制 5 次。同时打开 **Relative** 模式，定义相对距离的移动，这比计算每条线的确切位置更容易。给每个新副本任意起始点，例如，可以保留在（0,0,0），指定相对终点如下：
    -   line001: x: 10cm
    -   line002: x: 120cm
    -   line003: x: -55cm, y: -2m
    -   line004: x: 80cm
    -   line005: x: 15cm


</div>

![](images/Exercise_cabin_03.jpg )


<div class="mw-translate-fuzzy">

-   这就是我们现在所需要的，所以我们可以关闭构造模式。检查一下所有构造几何体是否已放入 \"Construction\" 组中，这样可以轻松地将其全部隐藏起来，甚至可以在以后完全删除它。
-   现在用 <img alt="" src=images/Draft_Wire.svg  style="width:16px;"> _ 已打开，因为我们需要捕捉到线条和矩形的交叉点。绘制如下两条线，单击圈出轮廓的所有点。要使它们闭合，请再次单击第一个点，或触发 **Close** 按钮。


</div>

![](images/Exercise_cabin_04.jpg )

-   可以选择两个墙，将它们的 **Pattern** 属性设置为 **Simple**，并将它们的 **Pattern size** 设置为合适的值，比如 **0.005**，这样便将它们的默认灰色改为了漂亮的阴影图案。

![](images/Exercise_cabin_05.jpg )


<div class="mw-translate-fuzzy">

-   现在，可以右键单击 Construction 组并选择 **Hide Selection** 来隐藏构造几何体。
-   我们现在画窗户和门。 确保<img alt="" src=images/Draft_Snap_Midpoint.svg  style="width:16px;"> [midpoint snap](Draft_Snap/zh-cn.md) 已打开，如下所示，绘制六条线：


</div>

![](images/Exercise_cabin_06.jpg )


<div class="mw-translate-fuzzy">

-   现在将更改门线，创建一个打开的门的符号。首先使用 <img alt="" src=images/Draft_Rotate.png  style="width:16px;"> [Rotate](Draft_Rotate/zh-cn.md) 工具。单击线的端点作为旋转中心，将其起始角度设置为 *0*\' ，结束角度为 **-90**。
-   然后用 <img alt="" src=images/Draft_Arc.png  style="width:16px;"> [Arc](Draft_Arc/zh-cn.md) 工具创建开门的弧线。选中与上一步中使用的旋转中心相同的点作为中心，单击该线的另一个点以给出半径，然后选择起点和终点，如下所示。


</div>

![](images/Exercise_cabin_07.jpg )

-   现在开始摆放一些家具。首先，从左上角绘制一个矩形，放好一个厨房台面，给出 170cm 的宽度和 -60cm 的高度。在下图中，矩形的 **Transparency** 属性设置为 80％，让它看起来像个漂亮的家具。
-   然后，添加一个水槽和一个灶台。手工绘制这些符号可能非常繁琐，通常很容易在互联网上找到它们，例如在http://www.cad-blocks.net。在页面底部的 **Downloads**，为方便起见，我们从这个项目中提取了一个水槽和一个灶台，并将它们保存为 DXF 文件。你可以访问下面的链接来下载这两个文件，右键单击 **Raw** 按钮，然后 **另存为**。
-   将 DXF 文件插入打开的 FreeCAD 文档有两种方法，可以选择 **File → Import** 菜单选项，也可以将 DXF 文件从文件浏览器拖放到 FreeCAD 窗口中来完成。DXF 文件的内容可能不会出现在当前视图的中心，具体取决于它们在DXF 文件中的位置。可以使用菜单 **View → Standard views → Fit all** 适当缩放，看到导入的对象。插入两个 DXF 文件，将它们移动到厨房台面上的适当位置。

![](images/Exercise_cabin_08.jpg )


<div class="mw-translate-fuzzy">

-   现在使用<img alt="" src=images/Draft_Dimension.png  style="width:16px;"> [Dimension](Draft_Dimension/zh-cn.md) 工具来添加几个尺寸。 绘制尺寸要单击3个点：起点、终点和放置尺寸线的第三个点。即使起点、终点未对齐，在单击第二个点时按住 **Shift** 键，便可以制作水平或垂直尺寸。
-   可以通过双击树视图中的尺寸来更改标注文字的位置。通过控制点，可以用图形方式移动文本。在本练习中，\"0.15\" 文本被移到了尺寸线的外侧，这样更清晰。
-   可以通过编辑其 **Override** 属性来更改标注文本的内容。在本示例中，门和窗口尺寸的文本已经过编辑，指示出了其高度。


</div>

![](images/Exercise_cabin_09.jpg )


<div class="mw-translate-fuzzy">

-   使用 <img alt="" src=images/Draft_Text.png  style="width:16px;"> [Text](Draft_Text/zh-cn.md) 添加一些描述文本。单击一点来定位文本，然后输入文本行。在每行后按 Enter 键，按 Enter 键两次便完成了。
-   将文本链接到它们描述的项目的指示线（也称为 \"leaders\"），只需使用 **Wire** 工具完成。从文本位置开始绘制线到所描述的位置。完成后，可以通过将 **End Arrow** 属性设置为 **True** 来在指示线末尾添加圆点或箭头。


</div>

![](images/Exercise_cabin_10.jpg )

-   这张图纸完成了！由于那里的对象相当多，明智的做法是清理一下，将所有内容重新分到合适的组，以便其他人更容易理解这个文件。

![](images/Exercise_cabin_11.jpg )

-   现在将它放在制图图框里，便可以打印我们的工作成果了，这个我们将在本手册的后面部分介绍。或者，将绘图导出到 DXF 文件中，以便将绘图导入其他 CAD 应用程序。只需选中 \"Floor plan\" 组，选择菜单 **File → Export**，然后选中 Autodesk DXF 格式。该文件可以在任何其他 2D CAD 应用程序（如 [LibreCAD](http://www.librecad.org)）中打开。打开后可能会发现一些差异，取决于每个应用程序的配置。

![](images/Exercise_cabin_12.jpg )


<div class="mw-translate-fuzzy">

-   然而，使用 Draft 工作台最重要的是要知道，这里创建的几何体可以用作基础，或轻易地拉伸成 3D 对象。你可以使用 _ 工具。或者，留在 Draft 工作台中，用 <img alt="" src=images/Draft_Trimex.png  style="width:16px;"> [Trimex](Draft_Trimex/zh-cn.md) (Trim/Extend/Extrude) 工具。它在面具下执行的是 **Part Extrusion**，但是更符合 \"Draft 方式\"，也就是说，允许用图形的方式指示和捕捉拉伸的长度。尝试一下拉伸本例中做过的墙壁，如下所示。
-   选中对象的一个面后，按下 <img alt="" src=images/Draft_SelectPlane.png  style="width:16px;"> [working plane](Draft_SelectPlane/zh-cn.md) 按钮，可以将工作平面放置在任何位置。因此可以在不同的平面上绘制 Draft 对象，例如在墙面上，之后便可以将它们拉伸成 3D 固体。尝试一下将工作平面设置在墙壁的顶面上，然后就地绘制几个矩形。


</div>

![](images/Exercise_cabin_13.jpg )

-   在墙面上绘制 Draft 对象，拉伸成实体，然后使用 Part 工作台中的布尔工具从另一个实体中减去它们，便可以轻松完成所有类型的开口，如前一章所述。

从根本上说，Draft 工作台所做的，是提供一种图形的方式，来创建基本的 Part 操作。在 Part 工作台中，通常会通过设置其放置参数来定位对象，而在 Draft 工作台中，可以在视窗里执行此操作。有时候这个方式好，有时候另一个方式好。不要忘记，可以在其中一个工作台中创建 [自定义工具栏](Interface_Customization.md)，从另一个工作台中调取工具，充分利用这两个世界的优势资源。


<div class="mw-translate-fuzzy">

**下载**


</div>

-   本练习中创建的文件：https://github.com/yorikvanhavre/FreeCAD-manual/blob/master/files/cabin.FCStd
-   水槽的 DXF 文件：https://github.com/yorikvanhavre/FreeCAD-manual/blob/master/files/sink.dxf
-   台面的 DXF 文件：https://github.com/yorikvanhavre/FreeCAD-manual/blob/master/files/cooktop.dxf
-   本练习中生成的最终DXF文件：https://github.com/yorikvanhavre/FreeCAD-manual/blob/master/files/cabin.dxf


<div class="mw-translate-fuzzy">

**延伸阅读**


</div>


<div class="mw-translate-fuzzy">

-   [Draft 工作台](Draft_Workbench/zh-cn.md)
-   [捕捉](Draft_Snap/zh-cn.md)
-   [Draft 工作平面](Draft_SelectPlane/zh-cn.md)


</div>


<div class="mw-translate-fuzzy">





</div>

_ _

---
[documentation index](../README.md) > [Tutorials](Category_Tutorials.md) > Manual:Traditional 2D drafting/zh-cn
