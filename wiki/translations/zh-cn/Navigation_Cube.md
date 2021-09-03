


<div class="mw-translate-fuzzy">


{{docnav/zh-cn|[Mouse Model](Mouse_Model/zh-cn.md)|[Document structure](Document_structure/zh-cn.md)}}


</div>


{{TOCright}}

导航立方控制，或称**导航立方**是一种用于重新定位的图形用户界面。在默认情况下，它位于3D显示界面的右上角。如果您在标准的3D视图下查看，会发现它长相如下：

![](images/FreeCAD-v0-18-NavCube_Axonometric.png )

导航立方由以下几部分组成：

-   指向箭头
-   主导航立方
-   微型立方菜单

鼠标在导航立方上经过时，它会呈淡蓝色；点击时，会根据上面标明的视角对3D视图进行重新定位。在下面的示例中，已经通过[鼠标手势将](Mouse_Model.md)3D视图旋转到一个"非标准"的方位。现在，鼠标指针正停留在导航立方的一个角上（根据淡蓝色可以判断出）；若点击此角，便会令3D视图重新定位至此角正对您的标准轴测图。

![](images/FreeCAD-v0-18-NavCube_SelectCorner.png )

## 指向箭头

导航立方有6个指向箭头：4个三角箭头，位列上、下、左、右；以及2个弯曲箭头，分列上箭头的两侧。

单击三角箭头，将令3D视图绕正交于此箭头方向的直线旋转45度。单击弯曲箭头，将令3D视图绕指向坐在显示器前的您的直线旋转45度。

## 主导航立方

主导航立方(本节后面简作"主导")记录着实际对象在3D主视图部分中的方位。任意对3D主视图重新定位的操作都将导致主导随之重新定位。

主导实质上是一种由3种主要组件（面、边与角）构成的立方体所实现的增强3D视图，所以可以用鼠标指针轻松的点击来进行导航。点击特定的组件将令3D视图切换至组件正对您的视角。主导看起来有点儿"走形"，仿佛离您较远的组件比直接面对您的组件更大。借此即可看到并选择与正对着您的组件相邻的组件。例如，在一个普通立方体的"标准"视角下，当一个面正对着您，您也能够看到此面的4条边与4个角。在"走形"的主导中，您依然能看到正（对）面的每个邻接面、连接正反面角上的4条边。这将令您可以选择任意标准视图（除了背面及其面上的边，26个组件中有21个可见）:

-   正对您的立方体面（其实选也无用，因为当前采用的即此面）
-   当前立方体面上的4条边
-   当前立方体面上的4个角
-   四个相邻的立方体面
-   与背面相连的4条边
-   背面上的4个角

不可选的组件:

-   当前立方体的背面
-   背面上的边

请注意：撰写本文时（v0.18版），主导仍存在一些问题；当前，并非所有组件都可选。特别是不能选择边，也不能选择正（对）面上的4个角。

### 选择面

选择一个面将令3D视图定位至此面正对您的视角。根据一个面的视图，即可从上文推断出其他的可选点。正（对）面的侧边有4个细"条"表示其相邻面；点击它们即选中邻接面的对应视图。正（对）面的4个角可用于设置对应的轴测图。（正（对）面内其实还有一组边与角，但目前尚未完工）

### 选择边

可惜的是，选择边功能尚未完成。当前，若企图选择一个边，将会选中其侧的面。按道理来讲，若单击了这个边，它应切换至正对于您的视角。

### 选择角

单击一个角将给出以此角为视角的轴测图。但正如上文所述，当前正（对）面上的角不可选。

## 微型立方菜单

在导航立方的右下方有一个小立方体。点击此立方体将弹出一个菜单，借此来改变视图类型（正交视图（orthographic），透视视图（perspective），等角视图（isometric））或执行"缩放至适当视图（zoom to fit）"。


<div class="mw-translate-fuzzy">

## 移动导航立方

通过在主导上按住鼠标左键并进行拖拽，即可将整个导航立方控制结构移动到另一个地方。撰写本文时（v0.18版），直到鼠标指针越过主导的边界时，此结构才会开始移动。


</div>

## Configuration

The navigation cube is configurable, including adjusting its size: {{MenuCommand|Edit → Preferences... → Display → Navigation → Navigation cube}} <small>(v0.19)</small> .

For more advanced configuration, refer to the [CubeMenu](Interface_Customization#CubeMenu.md) [external workbench](External_workbenches.md).


<div class="mw-translate-fuzzy">


{{docnav/zh-cn|[Mouse Model](Mouse_Model/zh-cn.md)|[Document structure](Document_structure/zh-cn.md)}}


</div>




[Category:User Documentation{{\#translation:}}](Category:User_Documentation.md)
