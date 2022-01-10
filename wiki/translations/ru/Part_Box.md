---
- GuiCommand:/ru
   Name:Part_Box
   Name/ru:Куб
   MenuLocation:Деталь → Примитивы → Куб
   Workbenches:[Part](Part_Workbench/ru.md)
   SeeAlso:[Создать примитивы](Part_CreatePrimitives/ru.md)
---

# Part Box/ru

## Description


<div class="mw-translate-fuzzy">

## Описание

Команда Куб из [верстака Part](Part_Workbench.md) добавляет параметрический геометрический примитив [1](https://ru.wikipedia.org/wiki/Прямоугольный_параллелепипед) в текущий документ. По умолчанию, команда добавляет куб с ярлыком \"Куб\" со сторонами 10х10х10 мм и располагает его в центре системы координат. Эти параметры могут быть изменены после добавления объекта.


</div>

<img alt="Part\_Box" src=images/Part_Box.jpg  style="width:400px;">

## Usage


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


{{Properties_Title|Box}}

-    **Length**: The length parameter is the Box\'s dimension in the x-direction.

-    **Width**: The width parameter is the Box\'s dimension in the y-direction.

-    **Height**: The height parameter is the Box\'s dimension in the z-direction.

## Scripting

A Part Box can be created using the following function:


```python
box = FreeCAD.ActiveDocument.addObject("Part::Box", "myBox")
```

-   Where {{Incode|"myBox"}} is the name for the object.
-   The function returns the newly created object.

You can access and modify attributes of the {{Incode|box}} object. For example, you may wish to modify the length, width and height parameters.


```python
box.Length = 25
box.Width = 15
box.Height = 30
```

You can change its placement with:


```python
box.Placement = FreeCAD.Placement(FreeCAD.Vector(4, 6, 3), FreeCAD.Rotation(30, 45, 10))
```

---
[documentation index](../README.md) > [Part](Part_Workbench.md) > Part Box/ru
