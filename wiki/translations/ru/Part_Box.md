---
- GuiCommand:/ru
   Name:Part_Box
   Name/ru:Куб
   MenuLocation:Деталь → Примитивы → Куб
   Workbenches:[Part](Part_Workbench/ru.md)
   SeeAlso:[Создать примитивы](Part_CreatePrimitives/ru.md)
---

## Описание

Команда Куб из [верстака Part](Part_Workbench.md) добавляет параметрический геометрический примитив [1](https://ru.wikipedia.org/wiki/Прямоугольный_параллелепипед) в текущий документ. По умолчанию, команда добавляет куб с ярлыком \"Куб\" со сторонами 10х10х10 мм и располагает его в центре системы координат. Эти параметры могут быть изменены после добавления объекта.

<img alt="Part\_Box" src=images/Part_Box.jpg  style="width:400px;">


<div class="mw-translate-fuzzy">

## Использование

1.  Переключитесь на <img alt="" src=images/Workbench_Part.svg  style="width:16px;"> [верстак Part](Part_Workbench.md)
2.  Существует несколько способов вызова команды:
    -   Нажмите на иконку куба **<img src="images/Part_Box.svg" width=16px>** на панели инструментов.
    -   Выберите из меню **Деталь → Примитивы → <img src="images/Part_Box.svg" width=16px> Куб**.


</div>

**Result:** The default result is a box with an equal length, width and height of 10 mm. It is attached to the global xy-plane and one edge is coincident with the global z-axis.

The box properties can later be edited, either in the property editor or by double-clicking on the box in the model tree.

## Properties


{{Properties_Title|Base}}

-    **Placement**: Specifies the orientation and position of the Box in the 3D space. See [Placement](Placement.md). The reference point is the left front lower corner of the box.

-    **Label**: Label given to the Box object. Change to suit your needs.


{{Properties_Title|Box}}

-    **Length**: The length parameter is the Box\'s dimension in the x-direction.

-    **Width**: The width parameter is the Box\'s dimension in the y-direction.

-    **Height**: The height parameter is the Box\'s dimension in the z-direction.

![Part\_Box-Properties](images/Part_Box-Properties.jpg )

## Scripting

The Box command can by used in [macros](Macros.md) and from the python console using the following function: 
```python
FreeCAD.ActiveDocument.addObject("Part::Box", "myBox")
```

-   Where \"myBox\" is the label for the Box object.
-   Returns newly created object of type Box.

You can access and modify attributes of the Box object. For example, you may wish to modify the length, width and height parameters. 
```python
FreeCAD.ActiveDocument.myBox.Length = 25
FreeCAD.ActiveDocument.myBox.Width = 15
FreeCAD.ActiveDocument.myBox.Height = 30
```

You can change its placement with: 
```python
FreeCAD.ActiveDocument.myBox.Placement = FreeCAD.Placement(FreeCAD.Vector(4, 6, 3), FreeCAD.Rotation(30, 45, 10))
```





 
