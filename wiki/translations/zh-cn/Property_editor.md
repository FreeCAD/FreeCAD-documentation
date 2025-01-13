# Property editor/zh-cn
<div class="mw-translate-fuzzy">

## 概述

属性编辑器是FreeCAD最重要的工具之一，也是FreeCAD使用的主要元素。 属性编辑器允许管理文档中对象的属性。


</div>

The [Property editor](Property_editor.md) appears in the lower section of the **Model** panel (if the [Combo view](Combo_view.md) is active) or as a stand-alone panel called **Property view**.


<div class="mw-translate-fuzzy">

通常，属性编辑器一次只处理一个对象。属性编辑器中显示的值属于活动文档的活动对象（如果您处理多个文档，请注意哪个文档是真正活动文档）。如果您没有选择任何元素（或没有元素），则属性编辑器将为空。


</div>


<div class="mw-translate-fuzzy">

并不是所有的属性都可以随时修改。根据具体状态，某些属性将显示为只读。


</div>

<img alt="" src=images/FreeCAD_Property_editor_Data.png  style="width:300px;"> 
*The Data properties of a [Part Box](Part_Box.md)*




<div class="mw-translate-fuzzy">

## 属性定义

一个**属性**是一条信息，如一个数字或文本字符串，附加到一个FreeCAD文档或文档中的一个对象。可以使用属性编辑器修改属性，如果允许的话。


</div>

A property is a piece of information like a number or a text string that is attached to a FreeCAD document or an object in the document. Many property types are available. Some of the most common types are:


{{Code|lang=text|code=
App::PropertyAngle
App::PropertyBool
App::PropertyDistance
App::PropertyFloat
App::PropertyInteger
App::PropertyLength
App::PropertyPlacement
App::PropertyString
App::PropertyVector
}}

## View and Data properties 


<div class="mw-translate-fuzzy">

有两种功能属性类型，可通过属性编辑器下方的选项卡来访问：

:   
    **View**: 关于对象"视觉"显示方面上的各种属性。

:   
    **Data**: 关于对象"物理"参数的各种属性。


</div>

## Basic properties 

Different objects may have different properties. However, many objects have the same properties because they are derived from the same internal class.

Most geometrical objects that can be created and displayed in the [3D view](3D_view.md) are derived from a `Part::Feature`. See [Part Feature](Part_Feature.md) for the basic properties these objects have.

For 2D geometry, most objects are derived from a `Part::Part2DObject` (itself derived from a `Part::Feature`) which is the base of [Sketches](Sketch.md), and most [Draft objects](Draft_Workbench.md). See [Part Part2DObject](Part_Part2DObject.md) for the basic properties these objects have.

## Context menu 

To display the context menu of the Property editor right-click the background of the editor, or right-click a property.

Right-clicking the background shows three options:

-    **Add property**: adds a dynamic property to the object.

-    **Show hidden**: if active, hidden Data and View properties are shown in the editor.

-    **Auto expand**: if active, all nodes in the editor are expanded when an object is selected.

When right-clicking a property the following additional options are available:

-    **Rename property group**: renames the property group of selected properties. Only available for dynamic properties. Dynamic properties are those added by the user, as well as those added through Python code.

-    **Remove property**: removes selected properties. Only available for dynamic properties.

-    **Expression...**: brings up the Expression editor, which allows using [expressions](Expressions.md) in the property value.

-    **Status**:

:   If a status value is followed by an asterisk (*****) it is static and cannot be changed.

  - **Hidden**: if active, sets the property as hidden, meaning that it will only be displayed in the Property editor if **Show hidden** is active.

  - **Output**: if active, sets the property as output.

  - **NoRecompute**: if active, modifying the property doesn\'t touch its container for recompute.

  - **ReadOnly**: if active, sets the property as read-only. The property won\'t be editable in the Property editor and the **Expression...** option no longer available. It may however still be possible to change the property via a dialog.

  - **Transient**: if active, sets the property as transient. The value of a transient property is not saved to file. When opening a file, it is instantiated with its default value.

  - **Touched**: if active, the object becomes touched, and ready for recompute.

  - **EvalOnRestore**: if active, the property is evaluated when the document is restored.

  - **CopyOnChange**: if active, the property is copied when changed in a Link. The Link\'s **Link Copy on Change** property must be set to {{Value|Tracking}} or {{Value|Enabled}} for this to work. This is related to [Variant Links](https://forum.freecad.org/viewtopic.php?p=738833#p738833).

## Scripting

See [FeaturePython Custom Properties](FeaturePython_Custom_Properties.md).

## Preferences

See [Combo view](Combo_view#Preferences.md).


<div class="mw-translate-fuzzy">


{{docnav|Interface Customization/zh-cn|Workbenches/zh-cn}}


</div>


{{Interface_navi

}} {{Std_Base_navi}}



---
⏵ [documentation index](../README.md) > Property editor/zh-cn
