---
 GuiCommand:
   Name: Robot_RestoreHomePos
   Name/ru: Вернуть в исходное положение
   MenuLocation: Робот , Вернуть в исходное положение
   Workbenches: Robot_Workbench/ru
---

# Robot RestoreHomePos/ru

## Описание

Приводит указанного робота в исходное положение.

## Применение

1.  Выберите робота в [древе документа](Tree_view/ru.md) или в [окне трехмерного вида](3D_view/ru.md)
2.  Нажмите кнопку <img alt="" src=images/Robot_RestoreHomePos.svg  style="width:32px;"> или выберите пункт главного меню **Робот** → **<img src="images/Robot_RestoreHomePos.svg" width=32px> Вернуть в исходное положение**.

## Примечания

-   Команда может привести в исходное положение только одного робота.
-   Если выбрано несколько роботов или вообще ни одного, пользователю будет предложено выбрать только одного робота.
-   Если исходная позиция не была указана с помощью команды <img alt="" src=images/Robot_SetHomePos.svg  style="width:32px;"> [установки исходной позиции](Robot_SetHomePos/ru.md), тогда в качестве исходной позиции будет использоваться позиция в которой робот находился сразу после его установки в сцену.





{{Robot_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Robot](Robot_Workbench.md) > Robot RestoreHomePos/ru
