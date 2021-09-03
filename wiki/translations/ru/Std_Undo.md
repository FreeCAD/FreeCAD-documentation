---
- GuiCommand:/ru
   Name:Std_Undo
   Name/ru:Отменить
   MenuLocation:Правка → Отменить
   Workbenches:Все
   Shortcut:**Ctrl**+**Z**
   SeeAlso:[Вернуть](Std_Redo/ru.md)
---

## Описание

Команда \"Отменить\", отменяет последнее действие.

## Применение

1.  Существует несколько способов вызова данной команды:
    -   Нажатием кнопки **<img src="images/Std_Undo.svg" width=16px> [Отменить](Std_Undo/ru.md)** на панели инструментов.
    -   Вызовом через меню {{MenuCommand|Правка → <img src="images/Std_Undo.svg" width=16px> Отменить}}.
    -   Используя комбинацию клавиш клавиатуры: **Ctrl**+**Z**.

## Опции

-   Чтобы отменить несколько действий, нажмите на маленькую черную стрелку указывающую вниз с правой стороны от кнопки **<img src="images/Std_Undo.svg" width=16px> [Отмена](Std_Undo/ru.md)** и выберите шаг к которому нужно вернуться из списка.

## Настройки

-   Функцию Отмены/Повтора можно отключить, установив {{MenuCommand|Инструменты → Редактор параметров... → Base App → Preferences → Document → UsingUndo}} в состяние `False`, но это не рекомендуется. Этот параметр также можно изменить через [Настройки](Preferences_Editor/ru#Документ.md).
-   Максимальное количество шагов Отмены/Повтора steps можно установить в {{MenuCommand|Инструменты → Редактор параметров... → BaseApp → Preferences → Document → MaxUndoSize}}. Этот параметр также можно изменить через [Настройки](Preferences_Editor/ru#Документ.md).

## Программирование


**Смотрите так же:**

[Основы составления скриптов в FreeCAD](FreeCAD_Scripting_Basics/ru.md).

Чтобы отменить последнее действие используйте метод `undo` объекта document.


```python
import FreeCAD

FreeCAD.ActiveDocument.undo()
```





{{Std Base navi

}}  
