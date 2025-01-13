---
 GuiCommand:
   Name: Std_Undo
   Name/ru: Отменить
   MenuLocation: Правка , Отменить
   Workbenches: Все
   Shortcut: **Ctrl**+**Z**
   SeeAlso: Std_Redo/ru
---

# Std Undo/ru



## Описание

Команда \"Отменить\", отменяет последнее действие.



## Применение


<div class="mw-translate-fuzzy">

1.  Существует несколько способов вызова данной команды:
    -   Нажатием кнопки **<img src="images/Std_Undo.svg" width=16px> [Отменить](Std_Undo/ru.md)** на панели инструментов.
    -   Вызовом через меню **Правка → <img src="images/Std_Undo.svg" width=16px> Отменить**.
    -   Используя комбинацию клавиш клавиатуры: **Ctrl**+**Z**.


</div>



## Опции


<div class="mw-translate-fuzzy">

-   Чтобы отменить несколько действий, нажмите на маленькую черную стрелку указывающую вниз с правой стороны от кнопки **<img src="images/Std_Undo.svg" width=16px> [Отмена](Std_Undo/ru.md)** и выберите шаг к которому нужно вернуться из списка.


</div>



## Настройки

See also: [Preferences Editor](Preferences_Editor.md).


<div class="mw-translate-fuzzy">

-   Функцию Отмены/Повтора можно отключить, установив **Инструменты → Редактор параметров... → Base App → Preferences → Document → UsingUndo** в состяние `False`, но это не рекомендуется. Этот параметр также можно изменить через [Настройки](Preferences_Editor/ru#Документ.md).
-   Максимальное количество шагов Отмены/Повтора steps можно установить в **Инструменты → Редактор параметров... → BaseApp → Preferences → Document → MaxUndoSize**. Этот параметр также можно изменить через [Настройки](Preferences_Editor/ru#Документ.md).


</div>



## Программирование


<div class="mw-translate-fuzzy">


**Смотрите так же:**

[Основы составления скриптов в FreeCAD](FreeCAD_Scripting_Basics/ru.md).


</div>


<div class="mw-translate-fuzzy">

Чтобы отменить последнее действие используйте метод `undo` объекта document.


</div>


```python
import FreeCAD

FreeCAD.ActiveDocument.undo()
```

При запуске FreeCAD в консольном режиме (CLI) механизм отмены/повтора по умолчанию выключен. Его нужно активировать для каждого документа следующим кодом:


```python
import FreeCAD

FreeCAD.ActiveDocument.UndoMode = 1
```





{{Std_Base_navi

}}



---
⏵ [documentation index](../README.md) > Std Undo/ru
