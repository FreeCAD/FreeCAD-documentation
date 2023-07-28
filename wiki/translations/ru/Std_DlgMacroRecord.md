---
- GuiCommand:/ru
   Name:Std_MacroStopRecord
   Name/ru:Запись макроса...
   MenuLocation:Макросы → Запись макроса...
   Workbenches:Все
   SeeAlso:[Остановить запись макроса](Std_MacroStopRecord/ru.md)
---

# Std DlgMacroRecord/ru



## Описание

The **Std DlgMacroRecord** command starts a [macro](Macros.md) recording session during which user actions are stored in a FreeCAD macro, a file with the **.FCMacro** extension. A macro can later be replayed, executed, to repeat the recorded actions.

![](images/Std_DlgMacroRecord_dialog.png ) 
*The Macro recording dialog box*



## Применение

1.  There are several ways to invoke the command:
    -   Press the **<img src="images/Std_DlgMacroRecord.svg" width=16px> [Std DlgMacroRecord](Std_DlgMacroRecord.md)** button.
    -   Select the **Macro → <img src="images/Std_DlgMacroRecord.svg" width=16px> Macro recording...** option from the menu.
2.  The Macro recording dialog box opens.
3.  Enter a name for the macro in the **Macro name** input box.
4.  Optionally change the **Macro path** by pressing the **...** button.
5.  The **Stop** button does not work at this time.
6.  Press the **Record** button to close the dialog box and start the recording session.
7.  Perform the actions you want to record.
8.  To end the recording session do one of the following:
    -   Press the **<img src="images/Std_MacroStopRecord.svg" width=16px> [Std MacroStopRecord](Std_MacroStopRecord.md)** button.
    -   Select the **Macro → <img src="images/Std_MacroStopRecord.svg" width=16px> Stop macro recording** option from the menu.



## Опции


<div class="mw-translate-fuzzy">

-   При отображении диалогового окна записи макросов: нажмите **Esc** или кнопку **Отмена**, чтобы прервать выполнение команды.


</div>



## Примечания

-   To execute the recorded macro use the [Std DlgMacroExecute](Std_DlgMacroExecute.md) command.
-   To learn more about macros see the [Macros](Macros.md) page.



## Настройки

-   The macro path can also be changed in the preferences: **Edit → Preferences... → Python → Macro → Macro path**. See [Preferences Editor](Preferences_Editor#Macro.md).
-   In most cases it is undesirable to record actions that do not change the model: under **Edit → Preferences... → Python → Macro → GUI commands** do one of the following:
    -   To exclude these actions uncheck the {{CheckBox|FALSE|Record GUI commands}} checkbox.
    -   To include them as comments only check both the {{CheckBox|TRUE|Record GUI commands}} and {{CheckBox|TRUE|Record as comment}} checkboxes.





{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std DlgMacroRecord/ru
