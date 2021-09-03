---
- GuiCommand:/ru
   Name:Std Quit
   Name/ru:Std Quit
   MenuLocation:Файл → Выход
   Workbenches:All
   Shortcut:**Alt**+**F4**
   SeeAlso:[Std Open](Std_Open/ru.md)
---


</div>

## Описание

The **Std Quit** command closes the FreeCAD application and optionally saves unsaved documents.

## Применение

1.  Есть несколько способов вызвать команду:
    -   Выберите в меню параметр {{MenuCommand|Файл → <img src="images/Std_Quit.svg" width=16px>Выход}}.
    -   Используйте сочетание клавиш: **Alt** + **F4**.
2.  Если есть несохранённые документы, диалоговое окно предложит вам сохранить их:
    -   Нажмите кнопку **Сохранить**, чтобы сохранить активный документ. При необходимости сначала введите имя файла.
    -   Нажмите кнопку **Закрыть без сохранения**, чтобы сбросить активный документ и потерять все изменения.

## Опции

-   If there are multiple unsaved documents: check the {{CheckBox|TRUE|Apply answer to all}} checkbox to avoid being prompted for each unsaved document separately.
-   If there are unsaved documents: press **Esc** or the **Cancel** button to abort the command.

## Настройки

-   The last used file location is stored: {{MenuCommand|Tools → Edit parameters... → BaseApp → Preferences → General → FileOpenSavePath}}.





{{Std Base navi

}}  
