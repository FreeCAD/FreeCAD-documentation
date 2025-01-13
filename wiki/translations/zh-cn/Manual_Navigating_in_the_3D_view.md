# Manual:Navigating in the 3D view/zh-cn
{{Manual:TOC}}



### 话说 3D 空间 


<div class="mw-translate-fuzzy">

如果这是您第一次接触 3D 应用程序，您首先需要了解一些概念。如果不是，您可以安全地跳过本节。


</div>


<div class="mw-translate-fuzzy">

FreeCAD 的 3D 空间是一个 [欧几里德空间](https://en.wikipedia.org/wiki/Euclidean_space)。它具有一个原点和三个轴：X、Y 和 Z。如果您从上方观察场景，按照惯例，X 轴指向右侧，Y 轴指向后方，Z 轴指向上方。在 FreeCAD 视图的右下角，您始终可以看到您观察场景的位置：


</div>


<div class="mw-translate-fuzzy">

三个轴相交的点是原点。它是所有坐标值为零的点。对于任意给定的轴，向一个方向移动将增加坐标值，向相反方向移动将减小坐标值。在 3D 空间中存在的每个对象的每个点都可以通过其 (x, y, z) 坐标来确定位置。例如，具有坐标 (2, 3, 1) 的点将位于 X 轴上 +2 个单位，Y 轴上 +3 个单位，Z 轴上 +1 个单位：


</div>

![](images/3dspace_coordinates.jpg )



### FreeCAD 3D 视图 




<div class="mw-translate-fuzzy">

#### 鼠标导航


</div>


<div class="mw-translate-fuzzy">

在 FreeCAD 的 3D 视图中进行导航可以使用鼠标、Space Navigator 设备、键盘、触摸板或它们的组合。FreeCAD 实现了几种导航模式，决定了如何执行三种基本的视图操作（平移、旋转和缩放），以及如何在屏幕上进行对象选择。导航模式可以从首选项界面访问，或直接通过在 3D 视图的任意位置右键单击来访问：


</div>

![](images/FreeCAD_022_NavigationMethod.png )


<div class="mw-translate-fuzzy">

每个模式将不同的鼠标按钮、鼠标+键盘组合或鼠标手势分配给这四种操作。下表显示了主要可用的模式：


</div>


<div class="mw-translate-fuzzy">

++++++
| 模式           | 平移                                                                                                                                                                       | 旋转                                                                                                                                                               | 缩放                                                                                                                                                      | 选择                                                                                    |
+================+============================================================================================================================================================================+====================================================================================================================================================================+===========================================================================================================================================================+=========================================================================================+
| OpenInventor   | ![点击鼠标中键](images/Pan-mouse.svg )                                                                                                                              | ![点击鼠标左键](images/Select-mouse.svg )                                                                                                                   | ![滚动鼠标中键](images/Zoom-mouse.svg )                                                                                                            | 按住 **Ctrl** + 拖动 ![点击鼠标左键](images/Select-mouse.svg ) |
++++++
| CAD **(默认)** | ![点击鼠标中键](images/Pan-mouse.svg ) 或 ![点击鼠标右键 + 按住 CTRL 键](images/Pan-mouse-CTRL.svg )                                          | ![按住鼠标中键然后按下左键](images/Rotate-mouse.svg ) 或 ![点击鼠标右键 + 按住 SHIFT 键](images/Rotate-mouse-SHIFT.svg ) | ![滚动鼠标中键](images/Zoom-mouse.svg ) 或 ![点击鼠标右键 + 按住 CTRL + SHIFT 键](images/Zoom-mouse-CTRL-SHIFT.svg ) | ![点击鼠标左键](images/Select-mouse.svg )                                        |
++++++
| Blender        | 按住 **Shift** + 拖动 ![点击鼠标中键](images/Pan-mouse.svg ) 或拖动 ![点击鼠标左键 + 右键并拖动](images/Mouse_LMB%2BRMB.svg ) | ![点击鼠标中键](images/Pan-mouse.svg )                                                                                                                      | ![滚动鼠标中键](images/Zoom-mouse.svg )                                                                                                            | ![点击鼠标左键](images/Select-mouse.svg )                                        |
++++++
| 触摸板         | 按住 **Shift** + 拖动 ![触摸板（鼠标）指针](images/Touchpad.png )                                                                           |                                                                                                                                                     |                                                                                                                                            | ![点击触摸板（鼠标）左键](images/Select-touchpad.png )                 |
|                |                                                                                                                                                                            | **Alt**                                                                                                                                                        | **PgUp**                                                                                                                                              |                                                                                         |
|                |                                                                                                                                                                            |                                                                                                                                                                 |                                                                                                                                                        |                                                                                         |
|                |                                                                                                                                                                            | \+ ![触摸板（鼠标）指针](images/Touchpad.png )                                                                                                        | / **PgDn**                                                                                                                              |                                                                                         |
++++++
| 手势           | 拖动 ![点击鼠标右键](images/Pan-mouse-Ctrl.svg )                                                                                                                    | 拖动 ![点击鼠标左键](images/Select-mouse.svg )                                                                                                              | ![滚动鼠标中键](images/Zoom-mouse.svg )                                                                                                            | ![点击鼠标左键](images/Select-mouse.svg )                                        |
++++++
| OpenCascade    | ![点击鼠标中键](images/Pan-mouse.svg )                                                                                                                              | ![按住鼠标中键然后按下右键](images/Rotate-mouse-MMB+RMB.svg )                                                                                   | ![滚动鼠标中键](images/Zoom-mouse.svg )                                                                                                            | ![点击鼠标左键](images/Select-mouse.svg )                                        |
++++++


</div>

It\'s worth noting that when a user hovers over the navigation styles menu located at the bottom right of the screen, a tooltip will appear. This tooltip provides a brief description of the highlighted navigation style, offering immediate guidance on its use.

![](images/FreeCAD_022_NavigationHover.png )




<div class="mw-translate-fuzzy">

#### 键盘导航


</div>


<div class="mw-translate-fuzzy">

另外，一些键盘控制在任何导航模式下始终可用：


</div>


<div class="mw-translate-fuzzy">

-    **Ctrl**\+ {{ASCII|43}} 和 **Ctrl** + {{ASCII|22}} 分别用于放大和缩小视图。

-   箭头键 {{ASCII|17}}{{ASCII|16}}{{ASCII|30}}{{ASCII|31}} 用于左右和上下平移视图。

-    **Shift**\+ {{ASCII|17}} 和 **Shift** + {{ASCII|16}} 用于将视图旋转90度。

-   数字键 {{ASCII|48}}{{ASCII|49}}{{ASCII|50}}{{ASCII|51}}{{ASCII|52}}{{ASCII|53}}{{ASCII|54}} 分别对应七个标准视图：<img alt="" src=images/Std_ViewIsometric.svg  style="width:24px;"> [等轴视图](Std_ViewIsometric.md), <img alt="" src=images/Std_ViewFront.svg  style="width:24px;"> [前视图](Std_ViewFront.md), <img alt="" src=images/Std_ViewTop.svg  style="width:24px;"> [顶视图](Std_ViewTop.md), <img alt="" src=images/Std_ViewRight.svg  style="width:24px;"> [右视图](Std_ViewRight.md), <img alt="" src=images/Std_ViewRear.svg  style="width:24px;"> [后视图](Std_ViewRear.md), <img alt="" src=images/Std_ViewBottom.svg  style="width:24px;"> [底视图](Std_ViewBottom.md) 和 <img alt="" src=images/Std_ViewLeft.svg  style="width:24px;"> [左视图](Std_ViewLeft.md)。

-    **V**
    **O**将视图设置为<img alt="" src=images/View-isometric.svg  style="width:24px;"> [正交视图](Std_OrthographicCamera.md)。

-   而 **V****P** 将视图设置为<img alt="" src=images/View-perspective.svg  style="width:24px;"> [透视视图](Std_PerspectiveCamera.md)。

-    **Ctrl**允许你选择多个对象或元素。


</div>

这些控制项也可以通过[视图菜单](Std_View_Menu.md)和一些通过视图工具栏访问。

#### Using the Navigation Cube 


<div class="mw-translate-fuzzy">

#### 使用导航聚焦区

在默认设置中，3D 视图的右上角有一个[导航聚焦区](Navigation_Cube.md)。 可以使用它以固定的角度旋转显示的对象， 将显示重置为几种标准视图之一， 以及更改显示模式。


</div>

![](images/FreeCAD_022_Cube.png )


<div class="mw-translate-fuzzy">

单击一个面将切换到该面的视图； 单击一个角将切换到以该角朝向您的视图。


</div>


<div class="mw-translate-fuzzy">

导航集群的右下方有一个较小的迷你立方体，点击它会弹出一个下拉菜单，允许您切换视图模式。


</div>



### 选择对象


<div class="mw-translate-fuzzy">

在 3D 视图中，可以通过使用相应的鼠标按钮（根据上面描述的导航模式）来选择对象。单击将选择对象及其子组件（边、面、顶点）之一。双击将选择对象及其所有子组件。您可以通过按住 CTRL 键来选择多个子组件，甚至可以从不同对象中选择不同的子组件。在 3D 视图的空白部分上点击选择按钮将取消选择所有内容。


</div>

一个名为"选择视图"的面板，可以在"视图"菜单中找到，也可以打开，它会显示当前选择的内容：

![](images/Selection_view.jpg )

您还可以使用选择视图通过搜索特定对象来进行选择。

**延伸阅读**


<div class="mw-translate-fuzzy">

-   [FreeCAD导航模式](Mouse_navigation.md)
-   [导航立方体](Navigation_Cube.md)


</div>



---
⏵ [documentation index](../README.md) > Manual:Navigating in the 3D view/zh-cn
