---
- GuiCommand:
   Name:Std DrawStyle
   Name/ru:Std DrawStyle
   MenuLocation:Вид - Стиль представления - ...
   Workbenches:All
   Shortcut:**V** **1** - **V** **7**
   SeeAlso:[Std SelBoundingBox](Std_SelBoundingBox/ru.md)
---

# Std DrawStyle/ru



## Описание

The **Std DrawStyle** command can override the effect of the **Display Mode** [property](Property_editor.md) of objects in a [3D view](3D_view.md).



## Применение

1.  There are several ways to invoke the command:
    -   Click on the black down arrow to the right of the **<img src="images/Std_DrawStyleAsIs.svg" width=16px> [Std DrawStyle](Std_DrawStyle.md)** button and select a style from the flyout.
    -   In the menu go to **View → Draw style** and select a style.
    -   In the [3D view](3D_view.md) context menu go to **Draw style** and select a style.
    -   Use one of the keyboard shortcut: **V** then **1**, **2**, **3**, **4**, **5**, **6** or **7**.

## Available draw styles 



### <img alt="" src=images/Std_DrawStyleAsIs.svg  style="width:24px;"> Как есть 

The **As is** style does not override the **Display Mode** of objects.

![](images/Std_DrawStyleAsIs_example.png ) 
*4 одинаковых объекта, с разными значениями переменной Display Mode (слева направо: 'Points', 'Wireframe', 'Shaded' и 'Flat lines') в режиме отображения 'Как есть'*



### <img alt="" src=images/Std_DrawStylePoints.svg  style="width:24px;"> Точки 

The **Points** style overrides the **Display Mode** of objects. This style matches the \'Points\' Display Mode. Vertices are displayed in solid colors. Edges and faces are not displayed.

![](images/Std_DrawStylePoints_example.png ) 
*Внешний вид тех же самых объектов в режиме отображения 'Точки'*



### <img alt="" src=images/Std_DrawStyleWireFrame.svg  style="width:24px;"> Каркас 

The **Wireframe** style overrides the **Display Mode** of objects. This style matches the \'Wireframe\' Display Mode. Vertices and edges are displayed in solid colors. Faces are not displayed.

![](images/Std_DrawStyleWireframe_example.png ) 
*Внешний вид тех же самых объектов в режиме отображения 'Каркас'*



### <img alt="" src=images/Std_DrawStyleHiddenLine.svg  style="width:24px;"> Скрытые линии 

The **Hidden line** style overrides the **Display Mode** of objects. Objects are displayed as if converted to triangular meshes.

![](images/Std_DrawStyleHiddenLine_example.png ) 
*Внешний вид тех же самых объектов в режиме отображения 'Скрытые линии'*



### <img alt="" src=images/Std_DrawStyleNoShading.svg  style="width:24px;"> Без затенения 

The **No shading** style overrides the **Display Mode** of objects. Vertices, edges and faces are displayed in solid colors.

![](images/Std_DrawStyleNoShading_example.png ) 
*Внешний вид тех же самых объектов в режиме отображения 'Без затенения'*



### <img alt="" src=images/Std_DrawStyleShaded.svg  style="width:24px;"> Только грани 

The **Shaded** style overrides the **Display Mode** of objects. This style matches the \'Shaded\' Display Mode. Vertices and edges are not displayed. Faces are illuminated depending on their orientation.

![](images/Std_DrawStyleShaded_example.png ) 
*Внешний вид тех же самых объектов в режиме отображения 'Только грани'*



### <img alt="" src=images/Std_DrawStyleFlatLines.svg  style="width:24px;"> Плоские линии 

The **Flat lines** style overrides the **Display Mode** of objects. This style matches the \'Flat lines\' Display Mode. Vertices and edges are displayed in solid colors. Faces are illuminated depending on their orientation.

![](images/Std_DrawStyleFlatLines_example.png ) 
*Внешний вид тех же самых объектов в режиме отображения 'Плоские линии'*



## Примечания

-   Objects in a [3D view](3D_view.md) also have a **Draw Style** property. This property controls the linetype used for the edges. The Std DrawStyle command does not override this property.
-   For a macro to toggle between two draw styles see: [Macro Toggle Drawstyle](Macro_Toggle_Drawstyle.md).





{{Std Base navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > Std DrawStyle/ru
