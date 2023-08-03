---
 GuiCommand:
   Name: Std_CloseAllWindows
   Name/ru: Закрыть всё
   MenuLocation: Файл , Закрыть всё
   Workbenches: Все
   SeeAlso: Std_CloseActiveWindow/ru
---

# Std CloseAllWindows/ru

## Описание

Команда **Закрыть всё** закрывает все окна, тем самым закрывая все документы.

## Применение

1.  Select the **File → <img src="images/Std_CloseAllWindows.svg" width=16px> Close All** option from the menu.
2.  If there are unsaved documents a dialog box will prompt you to save them:
    -   Press the **Save** button to save the active document. If required enter a filename first.
    -   Press the **Discard** button to discard the active document and lose all changes.

## Опции

-   When the dialog box is displayed: press **Esc** or the **Cancel** button to abort the command.
-   If there are multiple unsaved documents: check the {{CheckBox|TRUE|Apply answer to all}} checkbox to avoid being prompted for each unsaved document separately.

## Примечания

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
⏵ [documentation index](../README.md) > Std CloseAllWindows/ru
