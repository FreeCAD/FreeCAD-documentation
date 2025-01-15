---
 GuiCommand:
   Name/ru: Перевернуть крепёж
   Name: FSFlip
   MenuLocation: Стандартные изделия , Перевернуть крепёж
   Workbenches: Fasteners_Workbench/ru
---

# Fasteners Flip/ru



## Описание

The <img alt="" src=images/Fasteners_Flip.svg  style="width:24px;"> **Fasteners Flip** command inverts the orientation of [attached fasteners](Fasteners_Workbench#Usage.md) by changing their **Invert** property.



## Применение

1.  Выберите одно или несколько прикрепленных к чему-либо изделий. Можно так же выбрать изделия которые ни к чему не прикреплены, они просто не будут перевернуты. См. [Примечания](#Примечания.md).
2.  Команду можно вызвать несколькими способами:
    -   Нажатием на кнопку **<img src="images/Fasteners_Flip.svg" width=16px> [Перевернуть крепёж](Fasteners_Flip.md)**.
    -   Выбрав пункт главного меню **Стандартные изделия → <img src="images/Fasteners_Flip.svg" width=16px> Перевернуть крепёж**.
3.  Ориентация выбранного крепежа будет изменена на противоположную.



## Примечания

-   The **Invert** property is ignored for unattached fasteners and they cannot be flipped with this command. To flip them their **Placement** should be changed, for example with the <img alt="" src=images/Std_TransformManip.svg  style="width:16px;"> [Std TransformManip](Std_TransformManip.md) command.




{{Fasteners_Tools_navi}}



---
⏵ [documentation index](../README.md) > [External_Command_Reference](Category_External_Command_Reference.md) > [Fasteners](Category_Fasteners.md) > Fasteners Flip/ru
