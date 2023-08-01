# App FeaturePython/ru
## Введение


<div class="mw-translate-fuzzy">

Объект <img alt="" src=images/Feature.svg  style="width:32px;"> [App FeaturePython](App_FeaturePython/ru.md), или формально `Приложение::FeaturePython`, является простым экземпляром [App DocumentObject](App_DocumentObject/ru.md) в [Python](Python/ru.md).


</div>


<div class="mw-translate-fuzzy">

Это простой объект, который по умолчанию не имеет многих свойств, например таких как [разположение](Placement/ru.md) и [топологическая форма](Part_TopoShape/ru.md). Этот объект предназначен для общего использования; в зависимости от назначенных ему свойств его можно использовать для управления различными типами данных.


</div>

<img alt="" src=images/FreeCAD_core_objects.svg  style="width:800px;">


<div class="mw-translate-fuzzy">



*Упрощенная схема взаимосвязей между основными объектами в программе. Класс `App::FeaturePython* является простой реализацией {{incode|App::DocumentObject`, который можно использовать для любых целей, так как по умолчанию в нем нет [TopoShape](Part_TopoShape/ru.md).}}


</div>

## Применение

[App FeaturePython](App_FeaturePython/ru.md) является внутренним объектом, поэтому его нельзя создать с помощью графического интерфейса. Он предназначен для подклассов классов, которые будут обрабатывать различные типы данных.

For example, the [Draft Text](Draft_Text.md), [Draft Dimension](Draft_Dimension.md), and [Draft WorkingPlaneProxy](Draft_WorkingPlaneProxy.md) objects of the [Draft Workbench](Draft_Workbench.md) are `App::FeaturePython` objects with a custom icon and additional properties. They hold data but not an actual [Part TopoShape](Part_TopoShape.md).

If the desired object should have a placement, a shape, an attachment or other complex properties, it is better to create one of the more complex classes, for example, [App GeoFeature](App_GeoFeature.md), [Part Feature](Part_Feature.md), or [Part Part2DObject](Part_Part2DObject.md).

## Свойства

See [Property](Property.md) for all property types that scripted objects can have.


<div class="mw-translate-fuzzy">

[App FeaturePython](App_FeaturePython/ru.md) (`App::FeaturePython` класс) является производным от базового [App DocumentObject](App_DocumentObject/ru.md) (`App::DocumentObject` класса), поэтому он разделяет все свойства последнего.


</div>

These are the properties available in the [property editor](Property_editor.md). Hidden properties can be shown by using the **Show all** command in the context menu of the [property editor](Property_editor.md).

### Свойства объекта 


{{TitleProperty|Основные}}

-    **Proxy|PythonObject|Hidden**: a custom class associated with this object.

-    **Label|String**: the user editable name of this object, it is an arbitrary UTF8 string.

-    **Label2|String|Hidden**: a longer, user editable description of this object, it is an arbitrary UTF8 string that may include newlines. By default, it is an empty string {{value|""}}.

-    **Expression Engine|ExpressionEngine|Hidden**: a list of expressions. By default, it is empty {{value|[]}}.

-    **Visibility|Bool|Hidden**: whether to display the object or not.

### Свойства отображения 


{{TitleProperty|Основные}}

-    **Proxy|PythonObject|Hidden**: a custom [viewprovider](Viewprovider.md) class associated with this object.


{{TitleProperty|Display Options}}

-    **Display Mode|Enumeration**: it is empty by default.

-    **Show In Tree|Bool**: it defaults to `True`, in which case the object will appear in the [Tree view](Tree_view.md); otherwise, the object will be hidden in the tree view. Once an object in the tree is invisible, you can see it again by opening the context menu over the name of the document (right-click), and selecting {{CheckBox|TRUE|Show hidden items}}. Then the hidden item can be chosen and **Show In Tree** can be switched back to `True`.

-    **Visibility|Bool**: it defaults to `True`, in which case the object will be visible in the [3D view](3D_view.md) if it has a [Shape](Part_TopoShape.md), otherwise it will be invisible. By default this property can be toggled on and off by selecting the object, and pressing the **Space** bar.


{{TitleProperty|Selection}}

-    **On Top When Selected|Enumeration**: it controls the way in which the selection occurs in the [3D view](3D_view.md) if the object has a [Shape](Part_TopoShape.md), and there are many objects partially covered by others. It defaults to {{value|Disabled}}, meaning that no special highlighting will occur; {{value|Enabled}} means that the object will appear on top of any other object when selected; {{value|Object}} means that the object will appear on top only if the entire object is selected in the [Tree view](Tree_view.md); {{value|Element}} means that the object will appear on top only if a subelement (vertex, edge, face) is selected in the [3D view](3D_view.md).

-    **Selection Style|Enumeration**: it controls the way the object is highlighted if it has a [Shape](Part_TopoShape.md). If it is {{value|Shape}}, the entire shape (vertices, edges, and faces) will be highlighted in the [3D view](3D_view.md); if it is {{value|BoundBox}} a bounding box will appear surrounding the object and will be highlighted.

## Составление скриптов 


<div class="mw-translate-fuzzy">


**Смотрите так же:**

[Основы составления скриптов в FreeCAD](FreeCAD_Scripting_Basics/ru.md), и [скриптовые объекты](scripted_objects/ru.md).


</div>


<div class="mw-translate-fuzzy">

Общие сведения о добавлении объектов в программу смотрите в разделе [Объект \"Part::Feature\"](Part_Feature/ru.md).


</div>

App FeaturePython создается с помощью метода `AddObject()` документа.


```python
import FreeCAD as App

doc = App.newDocument()
obj = App.ActiveDocument.addObject("App::FeaturePython", "Name")
obj.Label = "Custom label"
```


{{Document_objects_navi

}}



---
⏵ [documentation index](../README.md) > App FeaturePython/ru
