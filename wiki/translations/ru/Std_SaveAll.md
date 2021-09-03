---
- GuiCommand:/ru
   Name:Std SaveAll
   Name/ru:Std SaveAll
   MenuLocation:Файл → Save All
   Workbenches:All
   SeeAlso:[Std Save](Std_Save/ru.md)
---


</div>

## Описание

Команда **Сохранить всё** сохраняет все открытые документы.

## Применение

1.  Select the **File → <img src="images/Std_SaveAll.svg" width=16px> Save All** option from the menu.
2.  For new documents: enter a filename in the dialog box and press the **Save** button.

## Опции

-   Нажмите **Esc** или кнопку **Отмена**, чтобы прервать выполнение команды.

## Настройки

-   Путь к последнему файлу к которому была применена данная команда сохраняется в параметр: **Инструменты → Редактор параметров... → BaseApp → Preferences → General → FileOpenSavePath**.

## Scripting


**Смотрите так же:**

[Основы составления скриптов в FreeCAD](FreeCAD_Scripting_Basics/ru.md).

To save a document use the `save` method of the document object. A new document must first be saved with the `saveAs` method of the document object. For a scripting example see [Std New](Std_New.md).





{{Std Base navi

}}  
