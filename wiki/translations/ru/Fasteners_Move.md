---
- GuiCommand:
   Name:Fasteners Move
   MenuLocation:Fasteners → Move fastener
   Workbenches:[Fasteners](Fasteners_Workbench.md)
---

# Fasteners Move/ru

## Описание

Команда <img alt="" src=images/Fasteners_Move.svg  style="width:24px;"> **Переместить крепёж** перемещает и устанавливает крепёж в указанную грань круглой формы. Данная команда может быть также применена для отсоединения крепежа. Крепеж который не присоединен к какой-либо грани, можно свободно перемещать. В свою очередь установленный крепёж привязан к объекту к которому он прикреплён и может перемещаться только совместно с этим объектом. Установленный крепеж имеет базовый объект в свойствах **base Object** и положение **Placement** такого крепежа динамический привязано к данному объекту.

## Применение

### Установка

<img alt="" src=images/Fasteners_Move_Selected.png  style="width:200px;"> <img alt="" src=images/Fasteners_Move_Result.png  style="width:200px;"> 
*On the left a fastener and a circular edge are selected. On the right the fastener has been moved and attached to the selected edge.*

1.  Выберите одно крепёжное изделие и одно ребро круглой формы, для этого при выборе зажмите клавишу **Ctrl**.
2.  Существует несколько способов вызова команды:
    -   Нажатием кнопки **<img src="images/Fasteners_Move.svg" width=16px> [Move fastener](Fasteners_Move/ru.md)**.
    -   Или через пункт меню **Fasteners → <img src="images/Fasteners_Move.svg" width=16px> Move fastener**.
3.  Крепёжное изделие будет перемещено к выбранному ребру круглой формы и будет установлено рядом с ним.

### Отсоединение

1.  Select a single fastener.
2.  There are several ways to invoke the command:
    -   Press the **<img src="images/Fasteners_Move.svg" width=16px> [Move fastener](Fasteners_Move.md)** button.
    -   Select the **Fasteners → <img src="images/Fasteners_Move.svg" width=16px> Move fastener** option from the menu.
3.  The fastener is detached.





{{Fasteners Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [External Command Reference](Category_External Command Reference.md) > [Fasteners](Category_Fasteners.md) > Fasteners Move/ru
