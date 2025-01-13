---
 GuiCommand:
   Name/ru: Фигура вращения
   Name: PartDesign_Revolution
   MenuLocation: PartDesign , Create an additive feature , Фигура вращения
   Workbenches: PartDesign_Workbench/ru
---

# PartDesign Revolution/ru


</div>



## Описание

Инструмент \"Вращения\" создает тело из эскиза или 2D объекта вращая его вокруг выбранной оси.

![](images/PartDesign_Revolution_example.svg )



*Выше: эскиз (A) вращается на 270 градусов против часовой стрелки вокруг оси (B); полученно тело (C) .*



## Применение


<div class="mw-translate-fuzzy">

1.  Выберете эскиз, который хотите вращать. Грань существующего тела тоже может быть использована.
2.  Нажмите на кнопку **<img src="images/PartDesign_Revolution.svg" width=24px> '''Вращение'''**.
3.  Установите параметры вращения (разобраны в следующей секции).
4.  Нажмите **OK**.


</div>



## Опции


<div class="mw-translate-fuzzy">

Когда производится вращение , появляется диалоговое окно **Параметры вращения** оно позволяет настроить как именно эскиз будет изогну.


</div>


<div class="mw-translate-fuzzy">

+++
| ![](images/partdesign_revolution_parameters.png ) |                                                                                                                                                                                                                                                                                                    |
|                                                                                  | </div>                                                                                                                                                                                                                                                                                                       |
|                                                                                  |                                                                                                                                                                                                                                                                                                           |
|                                                                                  | ### Type                                                                                                                                                                                                                                                                                                     |
|                                                                                  |                                                                                                                                                                                                                                                                                                              |
|                                                                                  |                                                                                                                                                                                                                                                                                               |
|                                                                                  | <small>(v1.0)</small>                                                                                                                                                                                                                                                                                               |
|                                                                                  |                                                                                                                                                                                                                                                                                                           |
|                                                                                  | Type offers five different ways of specifying the angle of the revolution:                                                                                                                                                                                                                                   |
|                                                                                  |                                                                                                                                                                                                                                                                                                              |
|                                                                                  | #### Dimension                                                                                                                                                                                                                                                                                               |
|                                                                                  |                                                                                                                                                                                                                                                                                                              |
|                                                                                  | Enter a numeric value for the **Angle** of the revolution. With the option **Symmetric to plane** the revolution will extend half the given angle to either side of the sketch or face.                                                                                                                      |
|                                                                                  |                                                                                                                                                                                                                                                                                                              |
|                                                                                  | #### To last                                                                                                                                                                                                                                                                                       |
|                                                                                  |                                                                                                                                                                                                                                                                                                              |
|                                                                                  | The revolution will extend up to the last face of the support it encounters in its direction. If there is no support, an error message will appear.                                                                                                                                                          |
|                                                                                  |                                                                                                                                                                                                                                                                                                              |
|                                                                                  | #### To first                                                                                                                                                                                                                                                                                     |
|                                                                                  |                                                                                                                                                                                                                                                                                                              |
|                                                                                  | The revolution will extend up to the first face of the support it encounters in its direction. If there is no support, an error message will appear.                                                                                                                                                         |
|                                                                                  |                                                                                                                                                                                                                                                                                                              |
|                                                                                  | #### Up to face                                                                                                                                                                                                                                                                                 |
|                                                                                  |                                                                                                                                                                                                                                                                                                              |
|                                                                                  | The revolution will extend up to a face. Press the **Face** button and select a face or a [datum plane](PartDesign_Plane.md) from the Body.                                                                                                                                     |
|                                                                                  |                                                                                                                                                                                                                                                                                                              |
|                                                                                  | #### Two dimensions                                                                                                                                                                                                                                                                         |
|                                                                                  |                                                                                                                                                                                                                                                                                                              |
|                                                                                  | This allows to enter a second angle in which the revolution should extend in the opposite direction. The directions can be switched by checking the **Reversed** option.                                                                                                                                     |
|                                                                                  |                                                                                                                                                                                                                                                                                                              |
|                                                                                  |                                                                                                                                                                                                                                                                     |
|                                                                                  |                                                                                                                                                                                                                                                                                                              |
|                                                                                  | ### Оси                                                                                                                                                                                                                                                                                                      |
|                                                                                  |                                                                                                                                                                                                                                                                                                              |
|                                                                                  | Specifies the axis of the revolution:                                                                                                                                                                                                                                                                        |
|                                                                                  |                                                                                                                                                                                                                                                                                                              |
|                                                                                  |                                                                                                                                                                                                                                                                                                    |
|                                                                                  | <div class="mw-translate-fuzzy">                                                                                                                                                                                                                                                                             |
|                                                                                  |                                                                                                                                                                                                                                                                                                           |
|                                                                                  | Это параметр определяет, вокруг каких осей эскиз будет изогнут.                                                                                                                                                                                                                                              |
|                                                                                  |                                                                                                                                                                                                                                                                                                              |
|                                                                                  | -   **Вертикальная ось эскиза**: выбирает вертикальную ось эскиза.                                                                                                                                                                                                                                           |
|                                                                                  | -   **Горизонтальная ось эскиза**: выбирает горизонтальную ось эскиза.                                                                                                                                                                                                                                       |
|                                                                                  | -   **Вспомогательные линии**: выбирает вспомогательную линию, содержимую в эскизе. выпадающий список содержит каждую вспомогательную линию. Первая вспомогательная линия будет названа *Вспомогательная линя 1*.                                                                                            |
|                                                                                  | -   **Основные оси (X/Y/Z)**: выбирает ось X, Y или Z.                                                                                                                                                                                                                                                       |
|                                                                                  | -   **Выбрать ориентир\...**: позволяет выбрать в 3D режиме грань тела, или [Создать опорный отрезок](PartDesign_Line/ru.md).                                                                                                                                                                        |
|                                                                                  |                                                                                                                                                                                                                                                                                                              |
|                                                                                  |                                                                                                                                                                                                                                                                                                    |
|                                                                                  | </div>                                                                                                                                                                                                                                                                                                       |
|                                                                                  |                                                                                                                                                                                                                                                                                                           |
|                                                                                  | Note that when changing the axis, the **Reversed** option may be (un)checked automatically.                                                                                                                                                                                                                  |
|                                                                                  |                                                                                                                                                                                                                                                                                                              |
|                                                                                  |                                                                                                                                                                                                                                                                    |
|                                                                                  |                                                                                                                                                                                                                                                                                                              |
|                                                                                  | ### Угол                                                                                                                                                                                                                                                                                                     |
|                                                                                  |                                                                                                                                                                                                                                                                                                              |
|                                                                                  |                                                                                                                                                                                                                                                                                                    |
|                                                                                  | <div class="mw-translate-fuzzy">                                                                                                                                                                                                                                                                             |
|                                                                                  |                                                                                                                                                                                                                                                                                                           |
|                                                                                  | Этот параметр задает угол, на который будет вращаться эскиз, к примеру 360 создаст смыкающееся тело. Тело в секции [Примеров](#Examples.md) демонстрирует чего можно добиться с помощью углов. Невозможно задать негативные углы (используйте параметр **В обратную сторону**) или углы больше 360°. |
|                                                                                  |                                                                                                                                                                                                                                                                                                              |
|                                                                                  |                                                                                                                                                                                                                                                                                                    |
|                                                                                  | </div>                                                                                                                                                                                                                                                                                                       |
|                                                                                  |                                                                                                                                                                                                                                                                                                           |
|                                                                                  |                                                                                                                                                                                                                                                       |
|                                                                                  |                                                                                                                                                                                                                                                                                                              |
|                                                                                  | ### Симметрично плоскости                                                                                                                                                                                                                                                            |
|                                                                                  |                                                                                                                                                                                                                                                                                                              |
|                                                                                  |                                                                                                                                                                                                                                                                                                    |
|                                                                                  | <div class="mw-translate-fuzzy">                                                                                                                                                                                                                                                                             |
|                                                                                  |                                                                                                                                                                                                                                                                                                           |
|                                                                                  | Если выбрано, вращение будет происходить в обе стороны от плоскости эскиза на половину заданного угла.                                                                                                                                                                                                       |
|                                                                                  |                                                                                                                                                                                                                                                                                                              |
|                                                                                  |                                                                                                                                                                                                                                                                                                    |
|                                                                                  | </div>                                                                                                                                                                                                                                                                                                       |
|                                                                                  |                                                                                                                                                                                                                                                                                                           |
|                                                                                  |                                                                                                                                                                                                                                                                 |
|                                                                                  |                                                                                                                                                                                                                                                                                                              |
|                                                                                  | ### В обратную сторону                                                                                                                                                                                                                                                                  |
|                                                                                  |                                                                                                                                                                                                                                                                                                              |
|                                                                                  |                                                                                                                                                                                                                                                                                                    |
|                                                                                  | <div class="mw-translate-fuzzy">                                                                                                                                                                                                                                                                             |
|                                                                                  |                                                                                                                                                                                                                                                                                                           |
|                                                                                  | Если выбрано, направление вращения будет изменено со стандартного (по часовой стрелки) на противоположенное                                                                                                                                                                                                  |
+++


</div>

### 2nd angle 


<small>(v1.0)</small> 

Defines the angle of the revolution in the opposite direction. This option is only available if **Type** is **Two dimensions** and **Angle** is smaller than 360°.




<div class="mw-translate-fuzzy">

## Свойства


</div>

### Data


{{TitleProperty|Part Design}}

-    **Refine|Bool**
    


{{TitleProperty|Revolution}}

-    **Type|Enumeration**
    

-    **Base|Vector**: (read-only)

-    **Axis|Vector**: (read-only)

-    **Angle|Angle**
    

-    **Up To Face|LinkSub**
    

-    **Angle2|Angle**
    

-    **Reference Axis|LinkSub**
    


{{TitleProperty|Sketch Based}}

-    **Profile|LinkSub**
    

-    **Midplane|Bool**
    

-    **Reversed|Bool**
    

-    **Allow Multi Face|Bool**
    

## Notes

-   A <img alt="" src=images/PartDesign_ShapeBinder.svg  style="width:16px;"> [ShapeBinder](PartDesign_ShapeBinder.md) cannot be used for the profile.
-   When using a <img alt="" src=images/PartDesign_SubShapeBinder.svg  style="width:16px;"> [SubShapeBinder](PartDesign_SubShapeBinder.md) for the profile, selecting the binder in the [Tree view](Tree_view.md) will fail, instead the binder\'s face has to be selected in the [3D view](3D_view.md).





{{PartDesign Tools navi

}}



---
⏵ [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Revolution/ru
