---
- GuiCommand:
   Name:Arch Space
   Name/ru:Arch Space
   MenuLocation:Архитектура → Пространство
   Workbenches:[Arch](Arch_Workbench/ru.md)
   Shortcut:**S** **P**
   Version:0.14
   SeeAlso:[[Arch Wall/ru]], [[Arch Structure/ru]]
---

# Arch Space/ru


</div>


<div class="mw-translate-fuzzy">

## Определение

Инструмент Пространство позволяет определить пустое пространство, базируясь на твердой оболочке, или определив границы, или и тем, и другим. Если он базируется только на границах, объем вычисляется, исходя из ограничительного блока всех заданных границ, и вычитая пространство за каждой границей. Пространственный объект всегда определяет твердотельный объём. Площадь пола пустого пространства вычисляемая пересечением горизонтальной плоскости через центр масс пустого пространства, так же может показываться установкой режима показа пространственного объекта в \"detailed\".


</div>

<img alt="" src=images/Arch_Space_example.jpg  style="width:640px;">


<div class="mw-translate-fuzzy">

*На рисунке выше пространственный объект создан из существующего твердотельного объекта, затем две стены добавлены как границы, и режим показа установлен в \"detailed\" для показа занимаемой площади.*


</div>



## Применение


<div class="mw-translate-fuzzy">

1.  Выберите существующий твердый объект или грани на граничных объектах
2.  Нажмите кнопку {{KEY | <img src="images/_Arch_Space.png_" width= 16px> [[Arch Space]]}} или нажмите клавиши {{KEY | S}}, {{KEY | P}}


</div>



### Ограничения

-   The boundaries properties is currently not editable via GUI.
-   See the [forum announcement](http://forum.freecadweb.org/viewtopic.php?f=9&t=4275).



## Свойства


<div class="mw-translate-fuzzy">

-    **Base**: Базовый объект, если он есть (должен быть твердым)

-    {{PropertyData | Boundaries}}: список необязательных граничных элементов


</div>

-    **Text**: The text to show. Use \$area, \$label, \$tag, \$floor, \$walls, \$ceiling to insert the respective data

-    **FontName**: The name of the font

-    **TextColor**: The color of the text

-    **FontSize**: The size of the text

-    **FirstLine**: The size of the first line of text (multiplies the font size. 1 = same size, 2 = double size, etc..)

-    **LineSpacing**: The space between the lines of text

-    **TextPosition**: The position of the text. Leave (0,0,0) for automatic position

-    **TextAlign**: The justification of the text

-    **Decimals**: The number of decimals to use for calculated texts

-    **ShowUnit**: Show the unit suffix or not



## Опции

-   To create zones that group several spaces, use a [Arch BuildingPart](Arch_BuildingPart.md) and set its IFC type to \"Spatial Zone\"
-   The space object has the same display modes as other Arch and Part objects, with one more, called **Footprint**, that displays only the bottom face of the space.

## Программирование


**Смотрите так же:**

[Основы составления скриптов в FreeCAD](FreeCAD_Scripting_Basics/ru.md).


<div class="mw-translate-fuzzy">

Инструмент Пространства можно использовать в сценариях python и [макросы](макросы.md), используя следующую функцию:


</div>


```python
Space = makeSpace(objects=None, baseobj=None, name="Space")
```

-   Creates a `Space` object from the given `objects` or `baseobj`, which can be
    -   one document object, in which case it becomes the base shape of the space object, or
    -   a list of selection objects as returned by `FreeCADGui.Selection.getSelectionEx()`, or
    -   a list of tuples `(object, subobjectname)`

Пример: 
```python
import FreeCAD, Arch

Box = FreeCAD.ActiveDocument.addObject("Part::Box", "Box")
Box.Length = 1000
Box.Width = 1000
Box.Height = 1000

Space = Arch.makeSpace(Box)
Space.ViewObject.LineWidth = 2
FreeCAD.ActiveDocument.recompute()
```

After a space object is created, selected faces can be added to it with the following code: 
```python
import FreeCAD, FreeCADGui, Draft, Arch

points = [FreeCAD.Vector(-500, 0, 0), FreeCAD.Vector(1000, 1000, 0)]
Line = Draft.makeWire(points)
Wall = Arch.makeWall(Line, width=150, height=2000)
FreeCAD.ActiveDocument.recompute()

# Select a face of the wall
selection = FreeCADGui.Selection.getSelectionEx()
Arch.addSpaceBoundaries(Space, selection)
```

Boundaries can also be removed, again by selecting the indicated faces: 
```python
selection = FreeCADGui.Selection.getSelectionEx()
Arch.removeSpaceBoundaries(Space, selection)
```



---
![](images/Button_right.svg) [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch Space/ru
