# Manual:Navigating in the 3D view/zh-cn
<div class="mw-translate-fuzzy">





</div>


{{Manual   *TOC/zh-cn}}

### 话说 3D 空间 

如果这是你第一次接触 3D 应用程序，则需要先熟悉一些概念。如果不是，你可以跳过这个部分，没有关系。

FreeCAD 的 3D 空间是[欧几里德空间](https   *//en.wikipedia.org/wiki/Euclidean_space)。它有一个原点和三个轴：X，Y 和 Z。如果从上面看你的场景，传统上，X 轴指向右边，Y 轴指向后面，Z 轴指向上方。在 FreeCAD 视图的右下角，您始终可以看到您正站在哪里查看场景。

![](images/Axes_orientation.png )

三轴相遇的点是原点。这是所有坐标的值为零的点。对于任何给定的轴，沿一个方向移动将增加坐标值，而沿相反方向移动将减小坐标值。3D 空间中存在的每个对象的每个点都可以通过其（x，y，z）坐标定位。例如，坐标为（2,3,1）的点将位于 X 轴上的 +2 个单位，Y 轴上的 +3 个单位和 Z 轴上的 +1 个单位。

![](images/3dspace_coordinates.jpg )

您可以从任何角度查看该场景，就像您拿着相机一样。相机可以左右移动，上下移动（平移），围绕它指向（旋转）的方向旋转，或使其更接近或远离场景（缩放）。

### FreeCAD 3D 视图 

#### 鼠标导航


<div class="mw-translate-fuzzy">

可以使用鼠标，Space Navigator 设备，键盘，触摸板或它们的组合在 FreeCAD 3D 视图中导航。 FreeCAD 实现了多种[导航模式](http   *//www.freecadweb.org/wiki/index.php?title=Mouse_Model)，这些模式决定了三种基本视图操作操作（平移，旋转和缩放）的完成方式，以及如何选中屏幕上的对象。你可以从"首选项"屏幕访问导航模式，也可以直接右键单击 3D 视图上的任意位置。


</div>

![](images/FreeCAD-v0-18-NavigationModePopup.png )

为这四个操作,这些模式中的每一个都分配了不同的鼠标按钮，或是鼠标+键盘组合，或是鼠标手势。下表显示了主要的可用模式。


<div class="mw-translate-fuzzy">

  模式             平移                                                                                                                            旋转                                                                                                                                               缩放                                                                                                                                              选中
      
  OpenInventor     ![按住鼠标中键](images/Pan-mouse.svg )                                                                                   ![按住鼠标左键](images/Select-mouse.svg )                                                                                                   ![滚动鼠标中键](images/Zoom-mouse.svg )                                                                                                    按住 CTRL + 拖动 ![按住鼠标左键](images/Select-mouse.svg )
  CAD **(默认)**   ![按住鼠标中键](images/Pan-mouse.svg ) 或 ![按住鼠标右键 + CTRL 键](images/Pan-mouse-CTRL.svg )         ![按住鼠标中键然后左键](images/Rotate-mouse.svg ) 或 ![按住鼠标右键 + SHIFT 键](images/Rotate-mouse-SHIFT.svg )   ![滚动鼠标中键](images/Zoom-mouse.svg ) 或 ![按住鼠标右键 + CTRL + SHIFT 键](images/Zoom-mouse-CTRL-SHIFT.svg )   ![点击鼠标左键](images/Select-mouse.svg )
  Blender          按住 SHIFT + ![按住鼠标中键](images/Pan-mouse.svg ) 或 ![按住鼠标左键和右键](images/Mouse_LMB%2BRMB.svg )   ![按住鼠标中键](images/Pan-mouse.svg )                                                                                                      ![滚动鼠标中键](images/Zoom-mouse.svg )                                                                                                    ![点击鼠标左键](images/Select-mouse.svg )
  触摸板           按住 SHIFT + 拖动![触摸板（鼠标）指针](images/Touchpad.png )                                                       按住 ALT + 拖动![触摸板（鼠标）指针](images/Touchpad.png )                                                                            向上翻页 / 向下翻页                                                                                                                               ![点击触摸板（鼠标）左键](images/Select-touchpad.png )
  手势             拖动 ![点击鼠标右键](images/Pan-mouse-Ctrl.svg )                                                                         拖动 ![点击鼠标左键](images/Select-mouse.svg )                                                                                              ![滚动鼠标中键](images/Zoom-mouse.svg )                                                                                                    ![点击鼠标左键](images/Select-mouse.svg )
  OpenCascade      ![按住鼠标中键](images/Pan-mouse.svg )                                                                                   ![按住鼠标中键然后右键](images/Rotate-mouse-MMB+RMB.svg )                                                                           ![滚动鼠标中键](images/Zoom-mouse.svg )                                                                                                    ![点击鼠标左键](images/Select-mouse.svg )


</div>

#### 键盘导航

作为替代，无论在什么导航模式下，一些键盘控件始终可用。


<div class="mw-translate-fuzzy">

-   **CTRL +** 和 **CTRL -** 放大和缩小
-   **箭头键**可左/右和上/下移动视图
-   **SHIFT +向左箭头**和 **SHIFT +向右箭头**将视图旋转90度
-   数字键0到6对应七个标准视图：轴测，前、上、右，后、下、左
-   '''O''' 会将相机设置为正交模式
-   而 '''P''' 将其设置为透视模式
-   按住 '''CTRL''' 将允许您选择多个对象或元素


</div>


<div class="mw-translate-fuzzy">

这些控制功能也可以通过"视图"菜单达成，某些功能可以从"视图"工具栏中达成。


</div>

#### 使用导航立方

=

在默认设置状态，3D 显示屏的右上角有一个[导航立方](Navigation_Cube.md)。用于将显示的对象旋转一个固定的角度，将视角重置为若干标准视图之一，还可以更改显示模式。

![](images/FreeCAD-v0-18-NavCube_SelectCorner.png )

使用导航立方，指针悬停在敏感区域上方时，控制点会变为浅蓝色。若指针下方的区域还没有改变颜色，点击它将没有任何效果。在撰写本文时（v0.18），存在一些注册问题，这些问题会阻止某些控制点的所有部分处于活动状态。


<div class="mw-translate-fuzzy">

单击一个面，视图会切换到让这个面面向你; 单击一个角，视图会切换到让这个角指向你。


</div>

单击四个三角形，会使视图在三角形指示的方向上旋转45度。 单击顶部两个弯曲箭头，会使视图围绕指向你的线，在弯曲箭头指示的方向上旋转45度。

拖动导航立方，可以将它移动到 3D 视窗的任何部位。必须在立方体内按下（左）鼠标按钮，才能启用拖动。只有指针拖到了立方体之外，导航立方才会开始移动。

群集右下方有一个较小的迷你立方体，点击它激活下拉菜单，可以切换查看模式。

### 选择对象

选择 3D 视图中的对象，可以使用相应的鼠标按钮单击，具体取决于导航模式（如上所述）。单击，会选择对象及其子组件之一（边、面、顶点）。双击，会选择对象及其所有子组件。按住 CTRL 键，可以选择多个子组件，甚至可以从不同对象中选择不同的子组件。单击 3D 视图的空白区域，会取消选定的所有内容。

还可以打开"视图"菜单中的"选择视图"面板，该面板显示当前选定的内容：

![](images/Selection_view.jpg )

还可以在"选择视图"中，搜索特定对象来选择。

**延伸阅读**


<div class="mw-translate-fuzzy">

-   [FreeCAD 的导航模式](Mouse_Model.md)
-   [导航集群](Navigation_Cube.md)


</div>


<div class="mw-translate-fuzzy">





</div>



---
![](images/Right_arrow.png) [documentation index](../README.md) > Manual:Navigating in the 3D view/zh-cn
