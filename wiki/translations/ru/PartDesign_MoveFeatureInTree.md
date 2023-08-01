---
- GuiCommand:/ru
   Name:PartDesign MoveFeatureInTree
   Name/ru:PartDesign MoveFeatureInTree
   Empty:1
   MenuLocation:Контекстное меню → Поместить объект позади другого объекта
   Workbenches:[PartDesign](PartDesign_Workbench/ru.md)
   Version:0.17
   SeeAlso:[Set tip](PartDesign_MoveTip/ru.md), [Перемещение объекта в другое тело](PartDesign_MoveFeature/ru.md)
---

# PartDesign MoveFeatureInTree/ru


</div>

## Описание

<img alt="" src=images/PartDesign_MoveFeatureInTree.svg  style="width:24px;"> [Переместить объект за другой объект](PartDesign_MoveFeatureInTree/ru.md), при выделении этой команды в контекстном меню, позволяет переупорядочивать объекты в Теле. Перемещать можно эскизы, геометрию построения и конструктивные элементы.

## Применение

1.  In the Model tree, select the object(s) to be moved then right-click to open the context menu.
2.  Select **Move object after other object**.
3.  In the **Select feature** dialog, select the object under which to move the object(s).
4.  Press **OK**.

## Пример

На следующих трех рисунках показана та же модель с вырезом, определенным на эскизе, прикрепленном к базовой плоскости. Функции переупорядочиваются от одного изображения к другому. Это приводит к тому, что вырез либо не создает отверстия, либо создает отверстия в разных контактных площадках, в зависимости от порядка элементов в дереве модели.

![](images/PD_move_feature0.png ) ![](images/Hole_Pad002.png ) ![](images/PD_move_feature2.png )





{{PartDesign Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign MoveFeatureInTree/ru
