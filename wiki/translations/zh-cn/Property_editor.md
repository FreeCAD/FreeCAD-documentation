# Property editor/zh-cn
{{TOCright}}




<div class="mw-translate-fuzzy">

## 概述

属性编辑器是FreeCAD最重要的工具之一，也是FreeCAD使用的主要元素。 属性编辑器允许管理文档中对象的属性。


</div>

The [property editor](Property_editor.md) appears when the **Model** tab of the [combo view](Combo_view.md) is active in the [interface](interface.md); it allows managing the publicly exposed properties of the objects in the document.


<div class="mw-translate-fuzzy">

通常，属性编辑器一次只处理一个对象。属性编辑器中显示的值属于活动文档的活动对象（如果您处理多个文档，请注意哪个文档是真正活动文档）。如果您没有选择任何元素（或没有元素），则属性编辑器将为空。


</div>


<div class="mw-translate-fuzzy">

并不是所有的属性都可以随时修改。根据具体状态，某些属性将显示为只读。


</div>


{{TOCright}}

![](images/FreeCAD_Property_editor_empty.png )



*Empty property editor, when no object is selected.*




<div class="mw-translate-fuzzy">

## 属性定义

一个**属性**是一条信息，如一个数字或文本字符串，附加到一个FreeCAD文档或文档中的一个对象。可以使用属性编辑器修改属性，如果允许的话。


</div>

A property is a piece of information like a number or a text string that is attached to a FreeCAD document or an object in the document.


<div class="mw-translate-fuzzy">

FreeCAD中的自定义[脚本对象可以具有以下类型的属性](Scripted_objects/zh-cn.md)：


</div>

Some of the most commonly used property types are:


```python
App::PropertyBool
App::PropertyFloat
App::PropertyAngle
App::PropertyDistance
App::PropertyInteger
App::PropertyString
App::PropertyMatrix
App::PropertyVector
App::PropertyPlacement
```


<div class="mw-translate-fuzzy">

不同的对象可能有不同的属性。然而，一些属性在所有对象中是常见的，例如对象的位置和旋转是可以被操纵的数据属性。


</div>

## View and Data properties 


<div class="mw-translate-fuzzy">

有两种功能属性类型，可通过属性编辑器下方的选项卡来访问：

:   
    **View**: 关于对象"视觉"显示方面上的各种属性。

:   
    **Data**: 关于对象"物理"参数的各种属性。


</div>

For this reason, **Data** properties are considered to be more \"real\", as they truly define the geometry of a shape. On the other hand, **View** properties are less important because they only affect the superficial appearance of the geometry. For example, a circle of 10 mm radius is different from a circle of 5 mm radius; the color of the circle (view property) doesn\'t affect its shape, but the radius does (data property). In many instances in this documentation, the word \"property\" is understood to refer to a \"Data property\" and not to a \"View property\".

### Basic properties 


**See also: [Object name](Object_name.md)**

The most basic [scripted object](Scripted_objects.md) won\'t show any **Data** property in the property editor, except for its `Label` attribute. The `Label` is a user editable string that identifies the object in the [tree view](Tree_view.md). On the other hand, the `Name` attribute of an object is assigned at the moment of its creation and cannot be changed; this attribute is read-only, and is not displayed in the property editor either.

A basic parametric object is created as follow


```python
obj = App.ActiveDocument.addObject("App::FeaturePython", "App__FeaturePython")
obj.Label = "Plain_object"
print(obj.Name)
print(obj.Label)
```

<img alt="" src=images/FreeCAD_Property_editor_View_basic.png  style="width:" height="264px;"> <img alt="" src=images/FreeCAD_Property_editor_Data_basic.png  style="width:" height="264px;">



*View and Data tabs of the property editor, for a basic "App::FeaturePython" scripted object.*

Most geometrical objects that can be created and displayed in the [3D view](3D_view.md) are derived from a `Part::Feature`. See [Part Feature](Part_Feature.md) for the most basic properties that these objects have.

For 2D geometry, most objects are derived from `Part::Part2DObject` (itself derived from `Part::Feature`) which is the base of [Sketches](Sketch.md), and most [Draft elements](Draft_Workbench.md). See [Part Part2DObject](Part_Part2DObject.md) for the most basic properties that these objects have.

## Actions


<small>(v0.19)</small> 

Right clicking in an empty space of the view, or with a property selected, shows only one command:

-    **Show all**: if active, in addition to the standard properties that appear already, it shows all the hidden Data and View properties in their respective tabs.

    -   Data: \"Proxy\", \"Label2\", \"Expression Engine\", and \"Visibility\".
    -   View: \"Proxy\".

When the **Show all** option is active, and one property is selected, more actions are available with a second right click:

-    **Show all**: deactivates the **Show all** command, hiding the additional Data and View properties.

-    **Add Property**: adds a dynamic property to the object; this works with both C++ defined objects, and Python [scripted objects](Scripted_objects.md).

-    **Expression...**: brings up the formula editor, which allows using [expressions](Expressions.md) in the property value.

-    **Hidden**: if active, sets the property as hidden, meaning that it will only be displayed in the property editor if **Show all** is active.

-    **Output**: if active, sets the property as output.

-    **NoRecompute**: if active, sets the property as not recomputed when the document is recomputed; this is useful when a property should be kept unaffected by other updates.

-    **ReadOnly**: if active, sets the property to be read-only; it won\'t be editable in the property editor any more until this switch is turned off. The **Expression...** menu entry is no longer available. **Note:** It may be still possible to change the property via a dialog that updates the property.

-    **Transient**: if active, sets the property as transient. The value of a transient property is not saved to file. When opening a file, it is instantiated with its default value.

-    **Touched**: if active, it becomes touched, and ready for recompute.

-    **EvalOnRestore**: if active, it is evaluated when the document is restored.




<div class="mw-translate-fuzzy">

## 零件对象属性的相关示例

### 属性


</div>

In this section we show some common properties that are visible for a [PartDesign Body](PartDesign_Body.md), and one [PartDesign Feature](PartDesign_Feature.md). The specific properties of an object can found in the specific documentation page of that object.



### 视图

Most of these properties are inherited from the [Part Feature](Part_Feature.md) basic object.


<div class="mw-translate-fuzzy">

<img alt="" src=images/FreeCAD_Properties_View.png  style="width:490px;"> {{TitleProperty|基本信息}}


</div>


{{TitleProperty|Base}}


<div class="mw-translate-fuzzy">

-    **包围盒（Bounding Box）**: 指示是否显示对象的最小外接立方体值可为False, 或True (默认值为False)。

-    **控制点（Control Point）**: 指示是否显示特征控制点。值可为False, 或True (默认值为False)。

-    **偏差（Deviation）**: 设置3D视图中模型多边形表示法（polygonal representation）的精准度（曲面细分）。较小的数值 = 更高的渲染质量。此值按对象大小的百分比来计算(以mm表示的偏差 = (w+h+d)/3\*valueInPercent/100, 其中w,h,d分别为包围盒的维度)。

-    **显示模式（Display Mode）**:对象的显示模式，**平直线（Flat lines）, 着色（Shaded）, 线框（Wireframe）, 点（Points）** [96px](IMAGE:Vue_DisplayModePartDesign_fr_00.png.md)。 （默认值, **平直线**）。

-    **光照（Lighting）**: 光照**单侧（One side）, 两侧（Two side）** [96px](IMAGE:Vue_Lighting_fr_00.png.md). (默认值，**两侧**)。

-    **线段颜色（Line Color）**: 指定线段（边）的颜色（默认值, **25, 25, 25**）。

-    **线段宽度（Line Width）**: 指定线段（边）的粗细（默认值, **2**）。

-    **点的颜色（Point Color）**: 指定点（端点）的颜色（默认值, **25, 25, 25**）。

-    **点的大小（Point Size）**: 指定点的大小（默认值, **2**）。

-    **可选择性（Selectable）**: 对象是否可以被选中。值为False或True （默认值, True）。

-    **几何形状的颜色（Shape Color）**: 指定带有颜色的几何形状（默认值, **204, 204, 204**）。

-    **透明度（Transparency）**: 设置对象的透明度，取值范围为**0** to **100** （默认值, **0**）。

-    **可见性（Visibility）**: 确定对象的可见性(如同**SPACE**键的效果)。取值为False或True （默认值, True）。





</div>






### 数据

In this case we observe the properties of the [PartDesign Revolution](PartDesign_Revolution.md) feature.


<div class="mw-translate-fuzzy">

<img alt="" src=images/FreeCAD_Properties_Data.png  style="width:490px;"> {{TitleProperty|基本信息}}


</div>


{{TitleProperty|Base}}


<div class="mw-translate-fuzzy">


**标签（Label）**

: 此标签是为目标对象（特征）指定的名称，此名可按需更改。


</div>


{{TitleProperty|Part Design}}

-    **Refine**: whether to refine the fusion done with other objects.


{{TitleProperty|Revolution}}

-    **Base**: the point in space that specifies where the revolution takes place. It cannot be modified directly, only when editing the feature.

-    **Axis**: the axis around which the revolution will be performed. It cannot be modified directly, only when editing the feature.

-    **Angle**: the angle that specifies how much of the base element is rotated. By default it is {{value|360 deg}}, but it can be any fraction of that.


{{TitleProperty|Sketch Based}}


<div class="mw-translate-fuzzy">


**位置（Position）**

: 本属性指定了与目标对象所有维度有关的基点。此属性取3个参数，通过工具中的x、y、z输入框来传递对应数值。为一个以上的输入框设置同一值，将导致零件在对应坐标轴上按设置的数值移动相应数量的单位。


</div>




## Scripting


**See also:**

[FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

See [scripted objects](scripted_objects.md) for the full information on adding properties to objects defined through [Python](Python.md).

Most properties that are visible in the property editor can be accessed from the [Python console](Python_console.md). These properties are just attributes of the class that defines the selected object. For example, if the property editor shows the **Group** property, this means that the object has the `Group` attribute.


```python
print(obj.Group)
```

These attributes (properties) are added with the `addProperty` method of the base object. At least it is necessary to specify the type of [property](property.md), and its name.


```python
obj.addProperty("App::PropertyFloat", "Custom")
print(obj.Custom)
```

Properties follow the `CapitalCamelCase` or `PascalCase` convention, meaning that each word starts with a capital letter, and there are no underscores. When the property editor displays such names, it leaves a space between each capital letter, making it easier to read.


```python
obj.addProperty("App::PropertyDistance", "CustomCamelProperty")
obj.CustomCamelProperty = 1000
print(obj.CustomCamelProperty)
```

![](images/FreeCAD_Property_editor_Custom.png ) 
*Property editor showing the Data properties of a [PartDesign Body](PartDesign_Body.md), with two additional properties, "Custom" and "Custom Camel Property".*

In similar way the **View** properties are added, not to the base object, but to its `ViewObject`. Then, it follows that properties like **Angular Deflection**, **Bounding Box**, **Display Mode**, **Display Mode Body**, **Line Color**, and others, can be examined and changed from the [Python console](Python_console.md).


```python
print(obj.ViewObject.AngularDeflection)
print(obj.ViewObject.BoundingBox)
print(obj.ViewObject.DisplayMode)
print(obj.ViewObject.DisplayModeBody)
print(obj.ViewObject.LineColor)
```

All public properties of the object, and of its view provider, are contained in the corresponding `PropertiesList` attribute.


```python
print(obj.PropertiesList)
print(obj.ViewObject.PropertiesList)
```


<div class="mw-translate-fuzzy">


{{docnav|Interface Customization/zh-cn|Workbenches/zh-cn}}


</div>


{{Interface navi

}} {{Std Base navi}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Property editor/zh-cn
