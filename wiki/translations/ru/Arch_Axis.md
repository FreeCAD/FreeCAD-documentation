---
- GuiCommand:/ru
   Name:Arch Axis
   Name/ru:Arch Axis
   MenuLocation:Arch → Axis
   Workbenches:[Arch](Arch_Module/ru.md)
   Shortcut:**A** **X**
   SeeAlso:[Axis System](Arch_AxisSystem/ru.md), [Arch Grid](Arch_Grid/ru.md)
---


</div>

## Описание

Инструмент **<img src="images/Arch_Axis.svg" width=16px> [Arch Axis](Arch_Axis.md)** позволяет разместить набор осей в текущем документе. Расстояние и угол между осями настраиваются, так же как и стиль нумерации. Главным образом Оси служат как объекты привязки, но так же могут использоваться совместно с инструментом **<img src="images/Arch_Axis_System.svg" width=16px> [Arch AxesSystems](Arch_AxisSystem/ru.md)** и могут ссылаться на другие объекты Архитектуры для создания параметрических массивов, например балок или столбов. Вместо осей могут так же использоваться **<img src="images/Arch_Grid.svg" width=16px> [Arch Grids](Arch_Grid/ru.md)**.

<img alt="" src=images/Arch_Axis_example.jpg  style="width:600px;"> 
*Два разных объекта осей расположены перпендикулярно друг другу для создания сетки*

## Использование

1.  Нажмите кнопку **<img src="images/Arch_Axis.svg" width=16px> [Arch Axis](Arch_Axis/ru.md)
**, или сочетание клавиш **A**, затем **X**
2.  [Передвиньте](Draft_Move/ru.md)/[Поверните](Draft_Rotate/ru.md) систему осей в нужное положение.
3.  Войдите в режим редактирования, дважды кликнув по системе осей в дереве объектов, что бы настроить их параметры, такие как количество осей, расстояние и углы между осями.

## Опции

-   Каждая ось в ряду имеет свое собственное расстояние и угол наклона относительно предыдущей оси. Это позволяет создавать очень сложные системы, такие как неортогональные системы, полярные системы или любые неравномерные системы
-   Двойной клик по системе осей в дереве объектов позволяет редактировать расстояния, углы и метки каждой оси
-   Длина осей, размер кружков и стиль нумерации настраиваются непосредственно через свойства системы осей
-   Каждая ось может отображать метку, которая так же настраивается в диалоговом окне панели задач

## Свойства


<div class="mw-translate-fuzzy">

-    **Length**: Длина осей

-    **Bubble Size**: Размер кружков осей

-    **Numeration style**: Как оси будут пронумерованы: 1,2,3, A,B,C, etc\...

-    **Bubble Position**: В каком месте оси кружек будет располагаться: В начальной точке, в конечной, обоих или нигде.

-    **Font Name**: Шрифт отображающий номер в кружочке или/и метки

-    **Font Size**: Размер текстовых меток (размер текста в кружечках контролирует размер кружечков осей)

-    **Show Labels**: Включает/отключает отображение текстовых меток


</div>

## Use as section mark 

By setting the **Bubble Position** property to **Arrow left/right** or **Bar left/right**, the axis will display a filled arrow or bar instead of the bubble, so it can be used as a section mark. <small>(v0.20)</small> 

## Скрипты


**См. так же:**

[Arch API](Arch_API/ru.md) и [Основы скриптов FreeCAD](FreeCAD_Scripting_Basics/ru.md)

The Axis tool can be used in [macros](macros.md) and from the [Python](Python.md) console by using the following function: 
```python
Axes = makeAxis(num=5, size=1000, name="Axes")
```

-   Creates an `Axes` object from the given number (`num`) of axes, and `size`, the interval between each axis.

Example:


```python
import Draft, Arch

Axes = Arch.makeAxis(5, 1000)

Axes.ViewObject.LineWidth = 3
Axes.ViewObject.BubbleSize = 200
Axes.ViewObject.FontSize = 150

Axes2 = Arch.makeAxis(6, 500)

Axes2.ViewObject.LineWidth = 2
Axes2.ViewObject.BubbleSize = 200
Axes2.ViewObject.FontSize = 150
Axes2.ViewObject.NumberingStyle = "A,B,C"
FreeCAD.ActiveDocument.recompute()

Axes2.Length = 6000
Draft.rotate(Axes2, -90)
Draft.move(Axes2, FreeCAD.Vector(-1000, 2500, 0))
FreeCAD.ActiveDocument.recompute()
```


<div class="mw-translate-fuzzy">





</div>


 
