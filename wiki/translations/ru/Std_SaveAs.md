---
- GuiCommand:/ru
   Name:Std_SaveAs
   Name/ru:Сохранить как...
   MenuLocation:[Файл](Std_File_Menu/ru.md) → Сохранить как...
   Workbenches:Все
   SeeAlso:[Сохранить копию](Std_SaveCopy/ru.md),<br> [Cохранить](Std_Save/ru.md)
---

# Std SaveAs/ru

## Описание

Команда **Сохранить как\...** позволяет сохранить текущий активный документ под другим названием.

## Применение

1.  Выберите пункт главного меню **Файл → <img src="images/Std_SaveAs.svg" width=16px> Сохранить как...**.
2.  Введите имя файла в появившемся окне.
3.  Нажмите кнопку **Сохранить**.

## Опции

-   Нажмите **Esc** или кнопку **Отмена**, чтобы прервать выполнение команды.

## Примечания

-   This command can also be used to save dependency graphs. See [Std DependencyGraph](Std_DependencyGraph.md).

## Настройки

-   Путь к последнему файлу к которому была применена данная команда сохраняется в параметр: **Инструменты → Редактор параметров... → BaseApp → Preferences → General → FileOpenSavePath**.

## Программирование


**Смотрите так же:**

[Основы составления скриптов в FreeCAD](FreeCAD_Scripting_Basics/ru.md).

To save a document under a new name use the `saveAs` method of the document object. For a scripting example see [Std New](Std_New.md).





{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std SaveAs/ru
