---
 GuiCommand:
   Name: Part_Sweep
   Name/ru: Развёртка
   MenuLocation: Деталь , Развёртка
   Workbenches: Part_Workbench/ru
   SeeAlso: Part_Loft/ru
---

# Part Sweep/ru



## Описание


<div class="mw-translate-fuzzy">

Инструмент <img alt="" src=images/Part_Sweep.svg  style="width:24px;"> [построения профиля по траектории](Part_Sweep/ru.md) позволяет создать: грань, оболочку или твёрдое тело из одного или последовательности нескольких контуров, путем смещения их вдоль заданной траектории.


</div>


<div class="mw-translate-fuzzy">

В отличии от похожего инструмента <img alt="" src=images/Part_Loft.svg  style="width:24px;"> [Лофт](Part_Loft/ru.md), в данный инструмент добавлена траектория для определения направления смещения контуров.


</div>

<img alt="" src=images/Part_Sweep_simple.png  style="width:400px;"> 
*A solid sweep generated from a single profile (A) distributed along a spine (B)*



## Применение

1.  There are several ways to invoke the command:
    -   Press the **<img src="images/Part_Sweep.svg" width=16px> [Sweep...](Part_Sweep.md)** button.
    -   Select the **Part → <img src="images/Part_Sweep.svg" width=16px> Sweep...** option from the menu.
2.  The Sweep [task panel](Task_panel.md) opens.
3.  In the *Available Profiles* list on the left select a profile and click on the right arrow to place it in the *Selected profiles* list on the right.
4.  Repeat if more than one profile is desired.
5.  The up and down arrows will reorder the list on the right. But this has no impact on the result. The position of the profiles along the spine determines in which order they are used.
6.  Click on the **Sweep Path** button, then choose either mode of selection:
    -   *Segment selection*: select one or more contiguous edges in the [3D view](3D_view.md) (press **CTRL** for multiple selection) and click **Done**. The sweep will only be generated along the selected edges.
    -   *Complete path selection*: switch to the [Tree view](Tree_view.md), select the object to be used as spine, switch back to the task panel and click **Done**. The sweep will be generated along all the contiguous edges found in the object.
7.  Define options [Solid](#Solid.md) and [Frenet](#Frenet.md).
8.  Click **OK**.



### Допустимые типы геометрических примитивов 


<div class="mw-translate-fuzzy">

Профили могут быть точками (вершинами), линиями (рёбрами), полилиниями или гранями. Рёбра и полилинии могут быть открытыми или замкнутыми. Есть различные [ограничения и сложности с профилями](Part_Sweep#Profile_limitations_and_complications.md), указанные ниже, тем не менее профили могут браться из примитивов модуля Part, форма модуля Draft и элементы модуля Sketch.


</div>


<div class="mw-translate-fuzzy">

Путь может быть линией (гранью) или серией соединённых линий, полилинией или различными примитивами модуля Part, формами модуля Draft или элементами модуля Sketch. Путь обычно выбирается прямо из окна модели, тем не менее он так же может выбираться из древа проекта. Путь может быть либо подходящая форма полностью, или подходящий суб-компонент более сложной формы (например, в качестве пути может быть выбрана грань Куба). Путь может быть открыт или замкнут, и соответственно будет создана открытая или замкнутая фигура. Замкнутый путь, вроде круга, создаёт замкнутую фигуру. Например, сдвиг по отношению маленького круга вокруг пути большой окружности создаёт тор.


</div>

-   [App Link](App_Link.md) objects linked to the appropriate object types and [App Part](App_Part.md) containers with the appropriate visible objects inside can also be used as profiles and paths. <small>(v0.20)</small> 

## Options




<div class="mw-translate-fuzzy">

### Solid


</div>


<div class="mw-translate-fuzzy">

Если параметр \"Solid\" установлен в \"true\" (отмечен бокс \"Создать твёрдое тело\"), FreeCAD создаёт твёрдое тело если профиль замкнутой геометрии, если \"false\", FreeCAD создаёт грань или (если несколько граней) оболочку для открытых или закрытых профилей.


</div>




<div class="mw-translate-fuzzy">

### Frenet


</div>

<img alt="" src=images/Sweep-frenet-comp.png  style="width:500px;">


<div class="mw-translate-fuzzy">

Параметр \"Frenet\" (устанавливается, если отметить бокс \"Френе\") управляет тем, как ориентация профиля изменяется по пути следования. Если \"Frenet\" равен \"false\", ориентация профиля остаётся неизменной от точки к точке. Итоговый профиль имеет минимально возможное кручение. Упрощённо, когда профиль идёт вдоль винтовой линии, это приводит к тому, что ориентация профиля медленно сползает (поворачивается) вслед за спиралью. Установка \"Frenet\" в \"true\" предотвращает это сползание.


</div>


<div class="mw-translate-fuzzy">

Если \"Frenet\" равен \"true\", ориентация профиля вычисляется на базе местной кривизны и касательной к пути. Это сохраняет ориентацию профиля постоянной при кручении вдоль винтовой линии (поскольку вектор кривизны прямой спирали всегда указывает на их оси). Тем не менее, если путь не винтовой, результирующая форма в некоторых случаях будет содержать странные кручения. Дальнейшую информацию смотрите в [Frenet Serret formulas](http://ru.wikipedia.org/wiki/Трёхгранник_Френе).


</div>

#### Transition

\"Transition\" sets the transition style of the Sweep at non-tangential joints in the path. The property is not exposed in the task panel and can be found in the [properties](Property_editor.md) after the Sweep has been created.



## Свойства

See also: [Property editor](Property_editor.md).

A Part Sweep object is derived from a [Part Feature](Part_Feature.md) object and inherits all its properties. It also has the following additional properties:

### Data


{{TitleProperty|Sweep}}

-    **Sections|LinkList**: lists the sections used.

-    **Spine|LinkSub**: spine (path) to sweep along.

-    **Solid|Bool**: true or false (default). True creates a Solid.

-    **Frenet|Bool**: true or false (default). True uses Frenet algorithm.

-    **Transition|Enumeration**: transition mode. Options are *Transformed*, *Right corner* or *Round corner*.

## Limitations

### Vertex or point 

A vertex or point may only be used as the first and/or last profile.
For example:

-   You cannot Sweep from a circle to a point, to an ellipse.
-   You can however Sweep from a point to a circle to an ellipse to another point.

### Profiles

In one Sweep, all profiles (lines wires etc.) must be either open or closed.
For example:

-   FreeCAD cannot Sweep between a Part Circle and a Part Line.

### Sketches

-   The profile may be created with a sketch. However only valid sketches will be available for selection in the task panel.
-   The sketch must contain only one open or closed wire or line (can be multiple lines, if those lines are all connected as they are then a single wire).

### Draft Workbench objects 

A profile can be a [Draft Workbench](Draft_Workbench.md) object.
The following objects can be valid profiles:

-   Point
-   Line, Wire
-   B-spline, Bézier Curve
-   Circle, Ellipse
-   Rectangle, Polygon

### Part Workbench objects 

A profile can be a Part object created with the [Part Primitives](Part_Primitives.md) command.
The following objects can be valid profiles:

-   Point (Vertex)
-   Line (Edge)
-   Helix, Spiral
-   Circle, Ellipse
-   Regular Polygon
-   Plane (Face)



## Ссылки

-   A Sweep is often used to create threads for screws, see the [Thread for Screw Tutorial](Thread_for_Screw_Tutorial.md) for more information.



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Sweep/ru
