---
- GuiCommand:
   Name:Part Torus
   MenuLocation:Part → Primitives → Torus
   Workbenches:[Part](Part_Workbench.md)
   SeeAlso:[Part Primitives](Part_Primitives.md)
---

# Part Torus/zh-cn

## Description


<div class="mw-translate-fuzzy">

## 描述

根据position, angle1, angle2, angle3, radius1 与 radius2参数创建一个简单的参数化环面。


</div>

<img alt="" src=images/SimpleTorus.jpg  style="width:400px;">


<div class="mw-translate-fuzzy">

## 如何使用


</div>


<div class="mw-translate-fuzzy">

在[零件工作台中点击环面图标](Part_Workbench.md)<img alt="" src=images/Part_Torus.png  style="width:32px;">。这会在原点(point 0,0,0)处创建一个环面。 三个角度参数(angle1, angle2, angle3)与两个半径参数(radius1 , radius2)用于确定参数化环面，详情请看下段文字。


</div>

**Result:** The torus will be positioned at origin (point 0,0,0) on creation.
The angle parameters (angle1, angle2, angle3), as well as the radius parameters (radius1, radius2) permit to parametrize the torus, see next section.

## 选项

![](images/TorusExampleOverviewParameters.jpg )

**参数**

创建环面的过程就相当于令一个小圆盘沿一个幻想的环形轨道为轴进行圆周运动。这样，就可以通过下列参数来定义参数化环面：

-    {{Parameter|Radius1:}}小圆盘圆周运动所绕圆环的半径

-    {{Parameter|Radius2:}}定义环面形状的小圆盘的半径

-    {{Parameter|Angle1:}}用于切割/定义环面小圆盘的第1个角度参数

-    {{Parameter|Angle2:}}用于切割/定义环面小圆盘的第2个角度参数

-    {{Parameter|Angle3:}}用于定义环面运动圆周的第3个角度参数

以及一系列标准定位参数。下图以可视化方式展示了上述提及的诸参数：

![](images/TorusExampleRadius1.jpg )
将Radius1参数的值指定为20 mm。

![](images/TorusExampleRadius2.jpg )
将Radius2参数的值指定为2 mm。

![](images/TorusExampleAngle1.jpg )
将Angle1参数的值指定为-90°。不难发现，\"角度测量\"工具并不能显示负值角度。因此，请将图中所示的值想象（zixingnaobu）为\"-90°\"。

![](images/TorusExampleAngle2.jpg )
将Angle2参数的值指定为90°。


<div class="mw-translate-fuzzy">

![](images/TorusExampleAngle3.jpg )  将Angle3参数指定为90°。


</div>

## Scripting

A Part Torus can be created using the following function:


```python
torus = FreeCAD.ActiveDocument.addObject("Part::Torus", "myTorus")
```

-   Where {{Incode|"myTorus"}} is the name for the object.
-   The function returns the newly created object.

---
[documentation index](../README.md) > [Part](Part_Workbench.md) > Part Torus/zh-cn
