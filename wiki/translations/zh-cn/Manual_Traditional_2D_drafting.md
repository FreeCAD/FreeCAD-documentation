# Manual:Traditional 2D drafting/zh-cn
{{Manual:TOC/zh-cn}}

你会对 FreeCAD 感兴趣，因为你已经有一些技术绘图经验，例如使用 [AutoCAD](https://en.wikipedia.org/wiki/AutoCAD) 等软件。或者你已经了解一些关于设计的知识，或者你更喜欢在建造之前绘制物品。无论哪种情况，FreeCAD 都具有更传统的工作台，其中包含在大多数 2D CAD 应用程序中能找到的工具：[草图工作台](Draft_Workbench.md)。

Draft 工作台虽然继承了传统 2D CAD 的工作方式，但并不局限于 2D 领域。Draft 工作台的所有工具都可以在整个 3D 空间中工作。许多 Draft 工具，例如，<img alt="" src=images/Draft_Move.svg  style="width:16px;"> [Move](Draft_Move/zh-cn.md) 和 <img alt="" src=images/Draft_Rotate.svg  style="width:16px;"> [Rotate在](Draft_Rotate/zh-cn.md) FreeCAD 中使用广泛，因为比起手动更改位置参数，Move 和 Rotate 更直观。

在 Draft 工作台提供的工具中，你会发现传统的绘图工具，例如<img alt="" src=images/Draft_Line.svg  style="width:16px;"> [线](Draft_Line.md)，<img alt="" src=images/Draft_Circle.svg  style="width:16px;"> [圆或](Draft_Circle.md)<img alt="" src=images/Draft_Wire.svg  style="width:16px;"> [线段](Draft_Wire.md)，修改工具，例如<img alt="" src=images/Draft_Move.svg  style="width:16px;"> [移动](Draft_Move.md)，<img alt="" src=images/Draft_Rotate.svg  style="width:16px;"> [旋转或](Draft_Rotate.md)<img alt="" src=images/Draft_Offset.svg  style="width:16px;"> [偏移](Draft_Offset.md)，一个[工作平面/网格系统](Draft_SelectPlane.md)，它允许你精确定义你正在工作的平面，并且完整的[捕捉系统使得在元素之间精确定位和绘制非常容易](Draft_Snap.md)。

为了展示 Draft 工作台的工作流程和可能性，我们将通过一个简单的练习来演示，其结果将是这个小图纸，显示一个只包含厨房的小房子的平面图（这是一个相当荒谬的平面图，但是我们在这里可以做我们想做的事情，不是吗？）：

![](images/Exercise_cabin_01.jpg )

-   切换到 Draft 工作台
-   与所有技术绘图应用程序一样，正确设置环境是明智的，它将为你节省大量时间。在菜单 **Edit → Preferences → Draft** 根据自己的喜好配置[grid and working plane](Draft_SelectPlane/zh-cn.md), [Text](Draft_Text/zh-cn.md) 和 [Dimension](Draft_Dimension/zh-cn.md)。 但是，在本练习中，我们将这些设置保留默认值。

![](images/Freecad_draft_options_01.jpg )

-   不过，有一个选项可能需要你的注意："**尽可能使用面填充对象**\"选项。如果选择了这个选项，默认情况下，像矩形或圆形这样的封闭对象将被填充为面，这可能会使对底层对象的捕捉变得困难。你现在可以关闭此选项，或者稍后关闭每个单独对象的"**创建面**\"属性，以防止它们创建面。

-   Draft 工作台还有两个特殊的工具栏：一个是**可视化设置**工具栏，你可以在其中更改当前工作平面，打开/关闭 [构造模式](Draft_ToggleConstructionMode.md)，设置用于新对象的线条颜色、面颜色、线条粗细和文本大小，另一个是**捕捉位置**工具栏。在那里，你可以打开/关闭网格并设置/取消单个[捕捉位置](Draft_Snap.md)：

![](images/Draft_toolbars.jpg )

-   打开所有捕捉按钮虽然方便，但同时也会使绘图速度变慢，因为移动鼠标时需要进行更多的计算。通常最好只保留你实际使用的捕捉。

-   让我们首先打开**构造模式**，这将允许我们绘制一些指导线，我们将在这些指导线上绘制最终的几何图形。
-   如果你想的话，把**工作平面**设置为**XY**。如果这样做，无论当前视图如何，工作平面都不会改变。如果没有这样做，工作平面将自动适应当前视图，你应该确保在想要在XY（地面）平面上绘制时保持在俯视视图。
-   然后，选择<img alt="" src=images/Draft_Rectangle.svg  style="width:16px;"> [矩形工具](Draft_Rectangle.md)，并绘制一个 2 米乘 2 米（将 Z 保持为零）的矩形，从点 (0,0,0) 开始。注意，大多数草图命令可以完全使用键盘执行，不需要触摸鼠标，只需使用它们的两个字母的快捷键。我们的第一个 2x2 m 矩形可以这样做：re 0 **Enter** 0 **Enter** 0 **Enter** 2m **Enter** 2m **Enter** 0 **Enter**。
-   使用<img alt="" src=images/Draft_Offset.svg  style="width:16px;"> [偏移](Draft_Offset.md) 工具，在内部 15cm 处复制该矩形。打开其复制模式，并给它一个距离为 15cm：

![](images/Exercise_cabin_02.jpg )

-   接下来，绘制几条垂直的线来定义门窗的位置，使用 <img alt="" src=images/Draft_Line.png  style="width:16px;"> [Line](Draft_Line/zh-cn.md) 工具。 这些线与两个矩形的交叉点为我们提供帮助，来捕捉墙壁的位置。从点（15cm，1m，0）到点（15cm，3m，0）绘制第一条线。
-   使用 <img alt="" src=images/Draft_Move.png  style="width:16px;"> [Move](Draft_Move/zh-cn.md) 工具，打开 Copy 模式,将这条线复制 5 次。同时打开 **Relative** 模式，定义相对距离的移动，这比计算每条线的确切位置更容易。给每个新副本任意起始点，例如，可以保留在（0,0,0），指定相对终点如下：
    -   line001: x: 10cm
    -   line002: x: 120cm
    -   line003: x: -55cm, y: -2m
    -   line004: x: 80cm
    -   line005: x: 15cm

-   接下来，我们可以使用<img alt="" src=images/Draft_Line.svg  style="width:16px;"> [线条](Draft_Line.md) 工具绘制一些垂直线，来定义我们的门和窗户的位置（注意，此步骤应取消勾选\"相对\"模式）。这些线与我们的两个矩形的交点将为我们提供有用的交点，以便将我们的墙壁对齐。从点 (15cm, 1m, 0) 到点 (15cm, 3m, 0) 绘制第一条线。
-   使用<img alt="" src=images/Draft_Move.svg  style="width:16px;"> [移动](Draft_Move.md) 工具复制该线 5 次，并打开复制模式。同时，打开相对模式，这将使我们能够以相对距离定义移动，比计算每条线的确切位置更容易。按顺序在刚刚创建的线上执行每个移动操作。给每个新副本任何起始点，例如可以将其保留为 (0,0,0)，然后设置以下相对终点：
    -   line001: x: 10cm
    -   line002: x: 120cm
    -   line003: x: -55cm, y: -2m
    -   line004: x: 80cm
    -   line005: x: 15cm

![](images/Exercise_cabin_03.jpg )

-   现在我们已经完成了这一步，所以可以关闭构造模式。检查所有构造几何体是否已经被放置在"Construction"组中，这使得一次性隐藏或甚至完全删除它们变得容易。
-   现在让我们使用<img alt="" src=images/Draft_Wire.svg  style="width:16px;"> [线段工](Draft_Wire.md) 具绘制我们的两个墙壁。确保<img alt="" src=images/Draft_Snap_Intersection.svg  style="width:16px;"> [交点捕捉](Draft_Snap.md) 已打开，因为我们需要对线和矩形的交点进行捕捉。按如下方式绘制两条线段，通过单击它们的轮廓的所有点进行绘制。要关闭它们，可以再次单击第一个点，或者按**Close**按钮：

![](images/Exercise_cabin_04.jpg )

-   我们可以将它们的默认灰色更改为漂亮的阴影图案，方法是选择两个墙壁，然后将它们的**Pattern**属性设置为**Simple**，将它们的**Pattern size**设置为你喜欢的大小，例如**0.005**。

![](images/Exercise_cabin_05.jpg )

-   现在我们可以通过右键单击构造组并选择**隐藏选定项**来隐藏构造几何体。
-   现在让我们绘制窗户和门。确保 <img alt="" src=images/Draft_Snap_Midpoint.svg  style="width:16px;"> [中点捕捉](Draft_Snap.md) 已打开，并按照以下方式绘制六条线：

![](images/Exercise_cabin_06.jpg )

-   现在我们将更改门的线来创建一个开着的门的符号。首先使用 <img alt="" src=images/Draft_Rotate.svg  style="width:16px;"> [旋转](Draft_Rotate.md) 工具旋转该线。以该线的端点为旋转中心，将起始角度设置为**0**，结束角度设置为**-90**。
-   然后使用 <img alt="" src=images/Draft_Arc.svg  style="width:16px;"> [弧线](Draft_Arc.md) 工具创建开口弧线。将旋转中心设置为我们在上一步中使用的相同点，单击线的另一个点以设置半径，然后按如下设置起始点和结束点：

![](images/Exercise_cabin_07.jpg )

-   现在我们可以开始放置一些家具。首先，让我们通过从内部左上角绘制一个矩形，给它一个宽度为 170cm 和高度为 -60cm 的尺寸来放置一个柜台。在下面的图像中，该矩形的**透明度**属性设置为 80％，以使其具有漂亮的家具外观。
-   然后让我们添加一个水槽和一个炉灶。手工绘制这些符号可能非常繁琐，通常可以在互联网上轻松找到它们，例如在 [http://www.cad-blocks.net。为方便起见，在下面的](http://www.cad-blocks.net。为方便起见，在下面的)**下载**部分中，我们将从该项目中提取出一个水槽和一个炉灶来，并将它们保存为 DXF 文件。您可以通过访问下面的链接，右键单击**Raw**按钮，然后选择**另存为**来下载这两个文件。
-   将 DXF 文件插入到已打开的 FreeCAD文 档中可以通过选择**文件→导入**菜单选项或从文件浏览器中将 DXF 文件拖放到 FreeCAD 窗口中来完成。DXF 文件的内容可能不会出现在当前视图的中心，这取决于它们在 DXF 文件中的位置。您可以使用菜单**视图→标准视图→全部适合**来缩放并查找导入的对象。插入这两个 DXF 文件，并将它们移动到桌面上的适当位置：

![](images/Exercise_cabin_08.jpg )

-   现在我们可以使用 <img alt="" src=images/Draft_Dimension.svg  style="width:16px;"> [标注](Draft_Dimension.md) 工具放置一些尺寸标注。标注通过单击 3 个点绘制：起始点、终点和第三个点来放置标注线。即使前两个点没有对齐，也可以按住 **Shift** 键绘制水平或垂直标注。
-   您可以通过在树视图中双击标注来更改标注文字的位置。控制点将使您可以以图形方式移动文本。在我们的练习中，"0.15" 文字已移开以获得更好的清晰度。
-   您可以通过编辑它们的 **Override** 属性来更改标注文字的内容。在我们的示例中，已编辑门和窗的标注文字以指示它们的高度：

![](images/Exercise_cabin_09.jpg )

-   让我们使用 <img alt="" src=images/Draft_Text.svg  style="width:16px;"> [文本](Draft_Text.md) 工具添加一些描述性文本。单击一个点来定位文本，然后输入每行文本，每行结束时按 Enter 键。要结束，请按两次 Enter 键。
-   将文本与它们描述的项目连接起来的标记线（也称为"引线"）可以使用 Wire 工具完成。从文本位置开始绘制线，到所描述的地方。完成后，您可以通过将它们的 **End Arrow** 属性设置为 **`True`** 来在线的末端添加一个小圆点或箭头。

![](images/Exercise_cabin_10.jpg )

-   我们的绘图现在已经完成！由于有相当多的对象，因此一个明智的选择是对它们进行一些清理，并将其重新组织成清爽的分组，使文件更易于其他人理解：

![](images/Exercise_cabin_11.jpg )

-   我们现在可以将我们的工作打印到制图图框里，这将稍后在本手册中展示，或通过将其导出为 DXF 文件直接将我们的绘图导出到其他 CAD 应用程序中。只需选择我们的"平面图"组，选择菜单**文件→导出**，并选择 Autodesk DXF 格式。然后可以在任何其他 2D CAD 应用程序（如[LibreCAD](http://www.librecad.org)）中打开该文件。您可能会注意到一些差异，这取决于每个应用程序的配置。

![](images/Exercise_cabin_12.jpg )

-   然而，Draft工作台最重要的是，您使用它创建的几何图形可以用作基础或轻松地从其中提取 3D 对象，只需使用 [Part 工作台](Part_Workbench.md) 中的 <img alt="" src=images/Part_Extrude.svg  style="width:16px;"> [拉伸](Part_Extrude.md) 工具，或者要来保持在 Draft 工作台中，就使用 <img alt="" src=images/Draft_Trimex.svg  style="width:16px;"> [Trimex](Draft_Trimex.md)（修剪/延伸/拉伸）工具，这会在幕后执行 Part Extrusion，但使用"Draft 方法"执行它，即允许您以图形方式指示并捕捉拉伸长度。尝试按照下面所示的方式拉伸我们的墙壁。
-   在选择对象的面后，按下 <img alt="" src=images/Draft_SelectPlane.svg  style="width:16px;"> [工作平面](Draft_SelectPlane.md) 按钮，您也可以将工作平面放置在任何位置，并因此在不同的平面上绘制 Draft 对象，例如在墙壁上方。然后可以将它们拉伸以形成其他 3D 实体。尝试将工作平面设置在墙壁顶部面之一上，然后在那里绘制一些矩形。

![](images/Exercise_cabin_13.jpg )

-   同样地，通过在墙壁的面上绘制 Draft 对象，然后将它们拉伸，再使用 Part 工作台中的布尔运算工具从另一个实体中减去它们，可以轻松地完成各种类型的开口，就像我们在前一章中看到的一样。

从根本上说，Draft 工作台所做的就是提供以图形方式创建基本Part操作的方法。在 Part 中，通常会通过设置它们的放置参数来定位对象，而在 Draft 中，您可以在屏幕上完成。有时候一个更好，其他时候另一个更可取。不要忘记，您可以在其中一个工作台中创建 [自定义工具栏](Interface_Customization.md)，添加另一个中的工具，得到两者的优势资源。



## 下载

-   本练习中创建的文件：https://github.com/yorikvanhavre/FreeCAD-manual/blob/master/files/cabin.FCStd
-   水槽的 DXF 文件：https://github.com/yorikvanhavre/FreeCAD-manual/blob/master/files/sink.dxf
-   台面的 DXF 文件：https://github.com/yorikvanhavre/FreeCAD-manual/blob/master/files/cooktop.dxf
-   本练习中生成的最终DXF文件：https://github.com/yorikvanhavre/FreeCAD-manual/blob/master/files/cabin.dxf



## 延伸阅读

-   [Draft 工作台](Draft_Workbench/zh-cn.md)
-   [捕捉](Draft_Snap/zh-cn.md)
-   [Draft 工作平面](Draft_SelectPlane/zh-cn.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Tutorials](Category_Tutorials.md) > [Draft](Category_Draft.md) > Manual:Traditional 2D drafting/zh-cn
