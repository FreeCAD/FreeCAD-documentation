---
- GuiCommand:/ru
   Name:Part_Sweep
   Name/ru:Развёртка
   MenuLocation:Деталь → Развёртка
   Workbenches:[Верстак Part](Part_Workbench/ru.md)
   SeeAlso:[Лофт](Part_Loft/ru.md)
---

# Part Sweep/ru

## Описание

Инструмент развертки верстака Part используется для создания лица, оболочки или твердой формы из одного или нескольких профилей, проецируемого вдоль заданной трассы.


<div class="mw-translate-fuzzy">

Инструмент Сдвиг похож на [Лофт](Part_Loft/ru.md), где добавлена трасса для определения проекций между профилями


</div>


<div class="mw-translate-fuzzy">

![](images/Part_Sweep_simple.png ) *A solid sweep generated from a single profile (A) projected along a path (B).*


</div>

## Применение

1.  Press the **<img src="images/Part_Sweep.svg" width=16px> '''Sweep'''** button. This opens the Sweep parameters in the [Task panel](Task_panel.md).
2.  In the *Available Profiles* left column (previously *Vertex/Edge/Wire/Face* in v0.16), click on the element to be used as sweep profile, then click on the right arrow to place it in the *Selected profiles* right column (previously *Sweep* in v0.16). Repeat if more than one profile is desired. Use the up and down arrows to reorder the selected profiles.
3.  Click on the **Sweep Path** button, then choose either mode of selection:
    -   *Single segment selection*: select one or more contiguous edges in the [3D view](3D_view.md) (press **CTRL** for multiple selection) and click **Done**. The sweep will only be generated along the selected edges.
    -   *Complete path selection*: switch to the Model tab, select the 2D object to be used as path in the tree, switch back to the [Task panel](Task_panel.md) and click **Done**. The sweep will be generated along all the contiguous edges found in the 2D object.
4.  Define options [Solid](#Solid.md) and [Frenet](#Frenet.md).
5.  Click **OK**

### Accepted geometry 


<div class="mw-translate-fuzzy">

Профили могут быть точками (вершинами), линиями (рёбрами), полилиниями или гранями. Рёбра и полилинии могут быть открытыми или замкнутыми. Есть различные [ограничения и сложности с профилями](Part_Sweep#Profile_limitations_and_complications.md), указанные ниже, тем не менее профили могут браться из примитивов модуля Part, форма модуля Draft и элементы модуля Sketch.


</div>


<div class="mw-translate-fuzzy">

Путь может быть линией (гранью) или серией соединённых линий, полилинией или различными примитивами модуля Part, формами модуля Draft или элементами модуля Sketch. Путь обычно выбирается прямо из окна модели, тем не менее он так же может выбираться из древа проекта. Путь может быть либо подходящая форма полностью, или подходящий суб-компонент более сложной формы (например, в качестве пути может быть выбрана грань Куба). Путь может быть открыт или замкнут, и соответственно будет создана открытая или замкнутая фигура. Замкнутый путь, вроде круга, создаёт замкнутую фигуру. Например, сдвиг по отношению маленького круга вокруг пути большой окружности создаёт тор.


</div>

## Свойства

### Solid

Если параметр \"Solid\" установлен в \"true\" (отмечен бокс \"Создать твёрдое тело\"), FreeCAD создаёт твёрдое тело если профиль замкнутой геометрии, если \"false\", FreeCAD создаёт грань или (если несколько граней) оболочку для открытых или закрытых профилей.

### Frenet

<img alt="" src=images/Sweep-frenet-comp.png  style="width:500px;">

Параметр \"Frenet\" (устанавливается, если отметить бокс \"Френе\") управляет тем, как ориентация профиля изменяется по пути следования. Если \"Frenet\" равен \"false\", ориентация профиля остаётся неизменной от точки к точке. Итоговый профиль имеет минимально возможное кручение. Упрощённо, когда профиль идёт вдоль винтовой линии, это приводит к тому, что ориентация профиля медленно сползает (поворачивается) вслед за спиралью. Установка \"Frenet\" в \"true\" предотвращает это сползание.

Если \"Frenet\" равен \"true\", ориентация профиля вычисляется на базе местной кривизны и касательной к пути. Это сохраняет ориентацию профиля постоянной при кручении вдоль винтовой линии (поскольку вектор кривизны прямой спирали всегда указывает на их оси). Тем не менее, если путь не винтовой, результирующая форма в некоторых случаях будет содержать странные кручения. Дальнейшую информацию смотрите в [Frenet Serret formulas](http://ru.wikipedia.org/wiki/Трёхгранник_Френе).

### Transition

\"Transition\" sets the transition style of the Sweep at a joint in the path, if the path does not define the corner transition (for example where the path is a wire). The property is not exposed in the [Task panel](Task_panel.md) and can be found in properties after the Sweep has been created.

## Profile limitations and complications 

-   A vertex or point
    -   vertex or point may only be used as the first and/or last profile in the list of profiles.
        -   For example
            -   you can not Sweep from a circle to a point, to a ellipse.
            -   However you could Sweep from a point to a circle to an ellipse to another point.
-   Open or closed geometry profiles can not be mixed in one single Sweep
    -   In one Sweep, all profiles (lines wires etc.) must be either open or closed.
        -   For example
            -   FreeCAD can not Sweep between one Part Circle and one default Part Line.
-   Draft Workbench features
    -   Draft Workbench features can be directly used as a profile in FreeCAD 0.14 or later.
        -   For example the following Draft features can be used as profiles in a Part Sweep
            -   Draft Polygon.
            -   Draft Point, Line, wire,
            -   Draft B-spline, Bezier Curve
            -   Draft Circle, Ellipse, Rectangle
-   PartDesign Sketches
    -   The profile may be created with a sketch. However only a valid sketch will be shown in the list to be available for selection.
    -   The sketch must contain only one open or closed wire or line (can be multiple lines, if those lines are all connected as they are then a single wire)
-   Part Workbench
    -   the profile can be a valid Part geometric primitive which can be created with the [Part Primitives tool](Part_Primitives.md)
        -   For example the following Part geometric primitives can be a valid profile
            -   Point (Vertex), Line (Edge)
            -   Helix, Spiral
            -   Circle, Ellipse
            -   Regular Polygon
            -   Plane (Face)

## Ссылки

-   Since Sweep is often used to create threads for screws, you should see [Thread for Screw Tutorial](Thread_for_Screw_Tutorial.md).

---
[documentation index](../README.md) > [Part](Part_Workbench.md) > Part Sweep/ru
