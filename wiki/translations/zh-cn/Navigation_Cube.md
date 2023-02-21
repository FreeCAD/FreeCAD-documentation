# Navigation Cube/zh-cn
<div class="mw-translate-fuzzy">


{{docnav/zh-cn|[Mouse Model](Mouse_Model/zh-cn.md)|[Document structure](Document_structure/zh-cn.md)}}


</div>


{{TOCright}}

## Introduction


<div class="mw-translate-fuzzy">

导航立方控制，或称**导航立方**是一种用于重新定位的图形用户界面。在默认情况下，它位于3D显示界面的右上角。如果您在标准的3D视图下查看，会发现它长相如下：


</div>

![](images/Navigation_Cube_Example.png )


<div class="mw-translate-fuzzy">

导航立方由以下几部分组成：

-   指向箭头
-   主导航立方
-   微型立方菜单


</div>

All parts, except the axis indicators, can be clicked.

## Usage

### Main cube 

The main cube has 26 faces: 6 main faces, 12 rectangular edge faces (<small>(v0.20)</small> ), and 8 corner faces. Clicking any of them will reorient the camera so that its direction is perpendicular to the selected face.




<div class="mw-translate-fuzzy">

## 指向箭头


</div>


<div class="mw-translate-fuzzy">

导航立方有6个指向箭头：4个三角箭头，位列上、下、左、右；以及2个弯曲箭头，分列上箭头的两侧。


</div>

### Reverse view button 

Clicking the round button in the top right corner of the Navigation Cube will rotate the [3D view](3D_view.md) 180 degrees around the vertical axis of the view.




<div class="mw-translate-fuzzy">

## 微型立方菜单


</div>


<div class="mw-translate-fuzzy">

在导航立方的右下方有一个小立方体。点击此立方体将弹出一个菜单，借此来改变视图类型（正交视图（orthographic），透视视图（perspective），等角视图（isometric））或执行"缩放至适当视图（zoom to fit）"。


</div>

## Customization

### Move the Navigation Cube 


<div class="mw-translate-fuzzy">

## 移动导航立方

通过在主导上按住鼠标左键并进行拖拽，即可将整个导航立方控制结构移动到另一个地方。撰写本文时（v0.18版），直到鼠标指针越过主导的边界时，此结构才会开始移动。


</div>

### Preferences

The Navigation Cube is controlled by several preferences: **Edit → Preferences... → Display → Navigation → Navigation cube**. See [Preferences Editor](Preferences_Editor#Navigation.md).

### Advanced parameters 

Some advanced Navigation Cube parameters cannot be changed in the [Preferences Editor](Preferences_Editor#Navigation.md). These parameters can be set manually in the [Parameter editor](Std_DlgParameter.md) or via the [CubeMenu external workbench](Interface_Customization#CubeMenu.md). Changes will become visible when a new 3D view is created (with [Std New](Std_New.md), [Std Open](Std_Open.md) or [Std ViewCreate](Std_ViewCreate.md)).

To manually set colors:

1.  Start the <img alt="" src=images/Std_DlgParameter.svg  style="width:16px;"> [Parameter editor](Std_DlgParameter.md).
2.  In the panel on the left browse to **BaseApp → Preferences → NaviCube**.
3.  Right-click the panel on the right and select **New unsigned item** from the context menu.
4.  Enter the name of one of these colors:
    -   
        **BorderColor**
        
        : the lines separating the cube faces, default is {{Value|4281479730}} (hex: {{Value|ff323232}}).

    -   
        **ButtonColor**
        
        : all elements around the cube, default is {{Value|2162354671}} (hex: {{Value|80e2e9ef}}).

    -   
        **FrontColor**
        
        : all cube faces, default is {{Value|3236096495}} (hex: {{Value|c0e2e9ef}}).

    -   
        **HiliteColor**
        
        : the cube or arrow face that is currently highlighted, default is {{Value|4289389311}} (hex: {{Value|ffaae2ff}}).

    -   
        **TextColor**
        
        : the text on the cube faces, default is {{Value|4278190080}} (hex: {{Value|ff000000}}).
5.  The color value must be entered as a 32-bit unsigned integer. Translated to the hexadecimal format this integer has the form {{Value|AARRGGBB}}. Where {{Value|AA}} stands for the alpha channel (a measure for the transparency), and the other three digit pairs stand for red, green and blue. To convert a hexadecimal value to an unsigned integer you can use the [Python console](Python_console.md), enter for example {{Incode|int("ff323232", 16)}}, or an online service such as [this one](https://cryptii.com/pipes/integer-encoder).
6.  Optionally set more colors.
7.  Press the **Close** button.

To manually set the border width:

1.  Start the <img alt="" src=images/Std_DlgParameter.svg  style="width:16px;"> [Parameter editor](Std_DlgParameter.md).
2.  In the panel on the left browse to **BaseApp → Preferences → NaviCube**.
3.  Right-click the panel on the right and select **New float item** from the context menu.
4.  Enter the name **BorderWidth**, {{Value|default is 1.1}}.
5.  Enter the width.
6.  Press the **Close** button.


<div class="mw-translate-fuzzy">


{{docnav/zh-cn|[Mouse Model](Mouse_Model/zh-cn.md)|[Document structure](Document_structure/zh-cn.md)}}


</div>



---
![](images/Right_arrow.png) [documentation index](../README.md) > [User Documentation](Category_User Documentation.md) > Navigation Cube/zh-cn
