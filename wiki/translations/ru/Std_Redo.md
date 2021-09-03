---
- GuiCommand:/ru
   Name:Std_Redo
   Name/ru:Вернуть
   MenuLocation:Правка → Вернуть
   Workbenches:Все
   Shortcut:**Ctrl**+**Y**
   SeeAlso:[Отмена](Std_Undo/ru.md)
---

## Описание

Команда **Вернуть** отменяет действие команды [Отменить](Std_Undo/ru.md).

## Применение

1.  Существует несколько способов для вызова данной команды:
    -   Нажатием кнопки **<img src="images/Std_Redo.svg" width=16px> [Вернуть](Std_Redo/ru.md)** на панели инструментов.
    -   Вызовом через меню {{MenuCommand|Правка → <img src="images/Std_Redo.svg" width=16px> Вернуть}}
    -   Используя комбинацию клавиш клавиатуры: **Ctrl**+**Y**.

## Опции

-   Чтобы вернуть сразу несколько действий, нажмите на маленькую черную стрелку указывающую вниз справой стороны от кнопки **<img src="images/Std_Redo.svg" width=16px> [Вернуть](Std_Redo/ru.md)** и выберите шаг к которому нужно вернуться из списка.

## Настройки

-   Функцию Отмены/Повтора можно отключить, установив {{MenuCommand|Инструменты → Редактор параметров... → Base App → Preferences → Document → UsingUndo}} в состяние `False`, но это не рекомендуется. Этот параметр также можно изменить через [Настройки](Preferences_Editor/ru#Документ.md).
-   Максимальное количество шагов Отмены/Повтора steps можно установить в {{MenuCommand|Инструменты → Редактор параметров... → BaseApp → Preferences → Document → MaxUndoSize}}. Этот параметр также можно изменить через [Настройки](Preferences_Editor/ru#Документ.md).

## Программирование


**Смотрите так же:**

[Основы составления скриптов в FreeCAD](FreeCAD_Scripting_Basics/ru.md).

Чтобы вернуть действие, которое только что было отменено, используйте метод `redo` объекта document.


```python
import FreeCAD

FreeCAD.ActiveDocument.redo()
```





{{Std Base navi

}}  
