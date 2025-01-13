---
 GuiCommand:
   Name: Arch Pipe
   Name/ru: Труба
   MenuLocation: Arch , Инструменты для труб , Труба
   Workbenches: Arch_Workbench/ru
   Shortcut: **P** **I**
   SeeAlso: Arch PipeConnector/ru, Arch_Equipment/ru
   Version: 0.17
---

# Arch Pipe/ru


</div>



## Описание


<div class="mw-translate-fuzzy">

Этот инструмент позволяет создавать трубы с нуля или из выбранных объектов. Выбранные объекты должны быть основами деталей (Draft, Sketch, и дт..) и содержать одну и только одну незамкнутую линию.


</div>



## Применение


<div class="mw-translate-fuzzy">

1.  При необходимости выберите линейную фигуру в верстаке [Деталь](Part_Workbench/ru.md), например [Линия](Draft_Line/ru.md), [Кривая](Draft_Wire/ru.md) или [ Эскиз](Sketcher_NewSketch/ru.md).
2.  Нажмите кнопку {{Button | <img src="images/_Arch_Pipe.svg" width=16px> [Труба](Arch_Pipe/ru.md)}} или нажмите клавиши **P**, а затем **I**.


</div>



## Параметры


<div class="mw-translate-fuzzy">

-   Трубы обладают таким же общими свойствами и моделью поведения, как и все остальные [компоненты верстака Arch](Arch_Component/ru.md)


</div>



## Свойства

### Data


{{TitleProperty|Component}}

-    **Base|Link**: The base wire of this pipe, if any.

For the other properties in the group see [Arch Component](Arch_Component#Properties.md).


{{TitleProperty|Pipe}}


<div class="mw-translate-fuzzy">

-    **Length**: Задает длину данной трубы, когда она не основана на кривой

-    **Diameter**: Диаметр данной трубы, когда она основана не на профиле

-    **Base**: Базовая кривая данной трубы, если есть

-    **Profile**: Базовый профиль данной трубы. Если не задан, труба будет цилиндрическая.


</div>



## Процесс создания 


<div class="mw-translate-fuzzy">

-   Начните с размещения предметов сантехники/гидравлики (ниже указано пошагово). Вы переводите эти объекты в Оборудование, выбирая их и нажимая кнопку [Оборудование](Arch_Equipment/ru.md).


</div>

![](images/Arch_pipe_example_01.jpg )


<div class="mw-translate-fuzzy">

-   Теперь Оборудование имеет новое свойство **SnapPoints**, представляющее собой список трехмерных векторов. Это позволяет добавлять пользовательские точки привязки, к которым вы можете привязываться, когда включена кнопка привязки [Специальные](Draft_Snap_Special/ru.md). В настоящее время это свойство доступно только для Python. В приведенном выше примере я добавил новую точку привязки на выходе устройства wc. Внутренние векторы Точек Привязки отображаются на модели в виде белых точек:


</div>

FreeCAD.ActiveDocument.Equipment.SnapPoints=[FreeCAD.Vector(0,0,100)]

![](images/Arch_pipe_example_02.jpg )

-   Теперь к [\"Специальными\"](Draft_Snap_Special/ru.md) точками привязки вы можете привязаться:

![](images/Arch_pipe_example_03.jpg )

-   Теперь мы можем нарисовать наш трубопровод, используя Линии, Кривы, или Эскизы. Однако лучше всего использовать только Линии:

![](images/Arch_pipe_example_04.jpg )


<div class="mw-translate-fuzzy">

-   Теперь появился новый инструмент [Наклон](Draft_Slope/ru.md), который позволяет изменять наклон Линий, например, до 5% (0,05). Таким образом, мы можем быстро дать нашим линиям правильный уклон. Этот инструмент изменяет только координаты z, поэтому нам нужно только привязать их друг к другу, верхняя проекция останется неизменной.


</div>

![](images/Arch_pipe_example_05.jpg )


<div class="mw-translate-fuzzy">

-   Теперь нам нужно только выбрать все наши линии и нажать кнопку [Труба](Arch_Pipe/ru.md). Инструмент Труба работает с любыми основами Деталей, которые содержат одну и только одну незамкнутую линию (или кривую).


</div>

![](images/Arch_pipe_example_06.jpg )


<div class="mw-translate-fuzzy">

-   Теперь мы можем создавать соединения, выбирая 2 или 3 соединенные трубы и нажимая кнопку [Соединитель Труб](Arch_PipeConnector.md). Если выбраны 3 трубы, две из них должны быть выровнены, чтобы создать элемент тройника:


</div>

![](images/Arch_pipe_example_07.jpg )

-   Изменение радиуса соединений не меняет длину базовой линии, а только результирующую трубу (путем изменения их свойства OffsetStart или OffsetEnd). Таким образом, вы можете нарисовать макет вашей линии только с помощью прямых линий, не заботясь о кривых и радиусах.

Также возможно создать Трубы без базовой линии, в этом случае используйте свойство «Length» для задания длины.

## Scripting


<div class="mw-translate-fuzzy">

## Программирование


**Смотрите так же:**

[Arch API](Arch_API/ru.md) и [Основы составления скриптов в FreeCAD](FreeCAD_Scripting_Basics/ru.md).


</div>


<div class="mw-translate-fuzzy">

Инструмент Труба можно использовать в [макросах](macros/ru.md) и в консоли [Python](Python.md), используя следующую функцию:


</div>


```python
pipe = makePipe(baseobj=None, diameter=0, length=0, placement=None, name="Pipe")
```

-   Creates a `pipe` object from the given `baseobj` and `diameter`.
    -   
        `baseobj`
        
        is a [Draft Line](Draft_Line.md) or [Draft Wire](Draft_Wire.md).

    -   If `baseobj` is omitted, a straight pipe can be created with just the `diameter` and the `length` in the Z direction.
-   If a `placement` is given, it is used.


```python
import Draft, Arch

p1 = FreeCAD.Vector(1000, 0, 0)
p2 = FreeCAD.Vector(2500, 200, 0)
p3 = FreeCAD.Vector(3100, 1000, 0)
p4 = FreeCAD.Vector(3500, 500, 0)
line = Draft.make_wire([p1, p2, p3, p4])

pipe = Arch.makePipe(line, 200)
FreeCAD.ActiveDocument.recompute()

pipe2 = Arch.makePipe(diameter=120, length=3000)
FreeCAD.ActiveDocument.recompute()
```


<div class="mw-translate-fuzzy">





</div>


{{BIM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > Arch Pipe/ru
