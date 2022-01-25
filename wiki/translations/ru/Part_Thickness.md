---
- GuiCommand:/ru
   Name:Part_Thickness
   Name/ru:Толщина
   MenuLocation:Деталь → Толщина
   Workbenches:[Верстак Part](Part_Workbench/ru.md)
   SeeAlso:[Смещение](Part_Offset/ru.md)
---

# Part Thickness/ru

## Description


<div class="mw-translate-fuzzy">

## Описание

Инструмент **Полость** обрабатывает твёрдые тела и трансформирует их в полые объекты, задавая каждой из имеющихся граней заданную толщину. В некоторых случаях это сильно ускоряет работу и позволяет избежать выдавливания и создания вырезов.


</div>

## Usage

1.  Create a solid
2.  Select one or more faces
3.  Click on the **<img src="images/Part_Thickness.svg" width=16px> '''Part Thickness'''** tool
4.  Set the parameters (see [Options](#Options.md))
5.  Click **OK** to confirm, create the operation and exit the function
6.  In the Properties table adjust the parameters if necessary

## Options

-   Thickness: Wall thickness of the resulting object, set the desired value
    -   A positive value will offset the faces outward
    -   A negative value will offset the faces inward
-   Mode
    -   Skin: Select this option if you want to get an item like a vase, headless but with the bottom
    -   Pipe: Select this option if you want to get an object like a pipe, headless and bottomless. In this case it may be convenient to select the faces to be deleted before you start the tool. Helping with predefined views buttons or use the numeric keys.
    -   RectoVerso:
-   Join Type
    -   Arc: removes the outer edges and create a fillet with a radius equal to the thickness defined
    -   Tangent:
    -   Intersection:
-   Intersection:
-   Self-intersection: Enables self-intersection
-   Face / Done: Select the faces to be removed, then click Done
-   Update view: Automatically updates the view in real time

## Limitations

Complex shapes may produce bizarre, hard to predict results. Carefully inspect the resulting shape and save your work before applying the operation.

## Links

A good example on how to use this tool on the forum: [Re: Help designing a simple enclosure](http://forum.freecadweb.org/viewtopic.php?f=3&t=3766&p=29741&hilit=enclosure#p29547)

## Примеры

**Hollow cylinder**

1.  Create **<img src="images/Part_Cylinder.svg" width=16px> [Cylinder](Part_Cylinder.md)** with radius 10mm and height 20mm
2.  Select the top and bottom surface of the cylinder
3.  Click on the **<img src="images/Part_Thickness.svg" width=16px> Thickness
** button (no need to change default settings) and press **OK**

Notes:

-   For this shape, consider using **<img src="images/Part_Tube.svg" width=16px> [Tube](Part_Tube.md)** instead <small>(v0.19)</small> 
-   Select the cylinder\'s top surface only to create a receptacle

![](images/ThicknessEsempio1.png )

![](images/ThicknessEsempio2.png )

**Box-Enclosure**

![](images/ThicknessEsempio3.png )

![](images/ThicknessEsempio4.png )



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Thickness/ru
