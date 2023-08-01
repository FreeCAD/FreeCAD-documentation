---
- GuiCommand:
   Name:Std CloseActiveWindow
   Name/ru:Закрыть
   MenuLocation:Файл → Закрыть
   Workbenches:Все
   Shortcut:**Ctrl**+**F4**
   SeeAlso:[Закрыть всё](Std_CloseAllWindows/ru.md)
---

# Std CloseActiveWindow/ru

## Описание

Команда **Закрыть** закрывает активное окно. Чтобы закрыть документ полностью, нужно чтобы все его окна были закрыты.

## Применение

1.  There are several ways to invoke the command:
    -   Select the **File → <img src="images/Std_CloseActiveWindow.svg" width=16px> Close** option from the menu.
    -   Use the keyboard shortcut: **Ctrl**+**F4**.
2.  To close a document: repeat this for all windows belonging to it.
3.  When closing the last window of a document that has not been saved, a dialog box will prompt you to save it:
    -   Press the **Save** button to save the document. If required enter a filename first.
    -   Press the **Discard** button to discard the document and lose all changes.

## Опции

-   Когда диалоговое окно отображается: нажмите **Esc** или кнопку **Отмена**, чтобы прервать выполнение команды.

## Примечания

-   The command can only close [docked](Std_ViewDockUndockFullscreen.md) windows.
-   A document can also be closed by right-clicking it in the [Tree view](Tree_view.md) and selecting **Close document** from the context menu.

## Настройки

-   Путь к последнему файлу к которому была применена данная команда сохраняется в параметр: **Инструменты → Редактор параметров... → BaseApp → Preferences → General → FileOpenSavePath**.

## Программирование


**Смотрите так же:**

[Основы составления скриптов в FreeCAD](FreeCAD_Scripting_Basics/ru.md).

Чтобы закрыть документ используйте метод `closeDocument` приложения FreeCAD. Пример скрипта можно посмотреть на странице команды [\"Создать\"](Std_New/ru.md).





{{Std Base navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > Std CloseActiveWindow/ru
