# Navigation Cube/ru
{{TOCright}}

## Introduction


<div class="mw-translate-fuzzy">

Кубический элемент управления навигацией, или «куб навигации», представляет собой графический интерфейс пользовательского интерфейса для переориентации трехмерного вида. Он виден по умолчанию и находится в верхнем правом углу дисплея.Если вы смотрите на стандартный трёхмерный вид, он выглядит следующим образом:


</div>

The Navigation Cube was updated in FreeCAD version 0.20 and the rest of this page describes that version. In FreeCAD version 0.19 the main behavior is the same but some features are missing.

![](images/Navigation_Cube_Example.png )


<div class="mw-translate-fuzzy">

Навигационный куб состоит из нескольких частей:

-   Стрелки направлений
-   Главный навигационный куб
-   Меню мини-куба


</div>

All parts, except the axis indicators, can be clicked.

## Usage

### Main cube 

The main cube has 26 faces: 6 main faces, 12 rectangular edge faces (<small>(v0.20)</small> ), and 8 corner faces. Clicking any of them will reorient the camera so that its direction is perpendicular to the selected face.


<div class="mw-translate-fuzzy">

## Стрелки направлений 


</div>


<div class="mw-translate-fuzzy">

Есть шесть стрелок-указателей: четыре треугольные стрелки, одна сверху, снизу, слева и справа; и две изогнутые стрелки, по одной с каждой стороны от верхней стрелки.


</div>

### Reverse view button 

Clicking the round button in the top right corner of the Navigation Cube will rotate the [3D view](3D_view.md) 180 degrees around the vertical axis of the view.


<div class="mw-translate-fuzzy">

## Меню мини-куба 


</div>


<div class="mw-translate-fuzzy">

В правом нижнем углу навигационного куба находится маленький кубик. Нажатие на этот куб вызовет меню, которое можно использовать для изменения типа вида (Ортогональный, Перспективный, Изометрический) и «Вписать в окно просмотра».


</div>

## Customization

### Move the Navigation Cube 


<div class="mw-translate-fuzzy">

## Перемещение куба навигации 

Вы можете переместить всю управляющую структуру куба навигации в другое место на 3D-дисплее, нажав мышью в любом месте основного куба навигации и перетащив. На момент написания (для v 0.18) структура не начнет двигаться, пока указатель мыши не переместится за край навигационного куба.


</div>

### Preferences

The Navigation Cube is controlled by several preferences: **Edit → Preferences... → Display → Navigation → Navigation cube**. See [Preferences Editor](Preferences_Editor#Navigation.md).

### Advanced options 

The [CubeMenu](Interface_Customization#CubeMenu.md) external workbench provides easier access to several more advanced customization options.



---
![](images/Right_arrow.png) [documentation index](../README.md) > [User Documentation](Category_User Documentation.md) > Navigation Cube/ru
