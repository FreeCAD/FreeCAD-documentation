# Std DlgMacroExecute/ro
---
 GuiCommand:   Name: Std DlgMacroExecute   MenuLocation: Macros   Macros , Execute macro---


</div>




<div class="mw-translate-fuzzy">

## Descriere


</div>


<div class="mw-translate-fuzzy">

Această funcție execută macroul selectat sau activ în editor. Este accesibil pe calea **Macro → Execute macro**, sau via butonul **[<img src=images/Std_DlgMacroExecute.png style="width:16px"> Execute macro** în bara de instrumente macro <img alt="" src=images/Macros_toolbar.jpg  style="width:96px;">.


</div>

<img alt="" src=images/Std_DlgMacroExecute_dialog.png  style="width:300px;"> 
*The Execute macro dialog box*




<div class="mw-translate-fuzzy">

## Utilizare


</div>


<div class="mw-translate-fuzzy">

Când tastați în **[<img src=images/Std_DlgMacroExecuteDirect.png style="width:16px"> [Macros...](Std_DlgMacroExecuteDirect.md)**, butonul **[<img src=images/Std_DlgMacroExecute.png style="width:16px"> Execute macro** își schimbă cularea în verde <img alt="" src=images/Menu_Std_DlgMacroExecute_fr_02.png  style="width:20px;">. Click pe acest buton pentru a rula macrocomanda.


</div>

## Options

### Find file / Find in files 

:   
    <small>(v0.22)</small> 
    





:   These two input boxes can be used to filter macros from the file list on the **User macros** tab or the **System macros** tab. You may use regular expressions or simply enter text. All matches are case-insensitive.





:   **Find file** filters the list by filename. Only filenames that match the entered text will appear in the list. **Find in files** filters the list by file content. Only files whose text content matches the entered text will appear in the list.





:   Remove all text from a filter\'s input box to disable it. If both input boxes contain text, both filters are applied. Filtering may result in an empty list.

### User macros 

:   The **User macros** tab lists the macros available in the **User macros location**.

1.  Click a macro in the list to select it.
2.  The name of the selected macro will appear in the **Macro name** box.

### System macros 

:   To make use of the **System macros** tab you must create a folder named **Macro** as a sibling folder of the **bin** folder where FreeCAD is installed and put some macros there.





:   To find the **bin** folder enter this in the [Python console](Python_console.md):





:   
    
```python
    App.getHomePath()
    
```
    

1.  Click a macro in the list to select it.
2.  The name of the selected macro will appear in the **Macro name** box.

### User macros location 

1.  Press the **...** button to change the user macros location.
2.  Browse to a different folder and select it.

### Execute

1.  To execute a macro do one of the following:
    -   Select the macro in the list and press the **Execute** button.
    -   Double-click the macro in the list.
2.  The dialog box closes.
3.  The macro is executed.

### Close

1.  Press **Esc** or the **Close** button to close the dialog box.

### Create

1.  Press the **Create** button to create a new macro file.
2.  Enter a name in the dialog box that pops up. You do not have to include the **.FCMacro** extension.
3.  Press **Enter** or the **OK** button.
4.  Both dialog boxes close.
5.  The new file is opened in the Macro editor.

### Delete

1.  Select the macro you want to delete in the list.
2.  Press the **Delete** button.
3.  Press the **Yes** button in the confirmation dialog box that pops up.

### Edit

1.  Select the macro you want to edit in the list.
2.  Press the **Edit** button.
3.  The dialog box closes.
4.  The selected file is opened in the Macro editor.

### Rename

1.  Select the macro you want to rename in the list.
2.  Press the **Rename** button.
3.  Enter a new name in the dialog box that pops up. You do not have to include the **.FCMacro** extension.
4.  Press **Enter** or the **OK** button.

### Duplicate

1.  Select the macro you want to duplicate in the list.
2.  Press the **Duplicate** button.
3.  Enter a new name in the dialog box that pops up. You do not have to include the **.FCMacro** extension.
4.  Press **Enter** or the **OK** button.

### Toolbar

1.  Select the macro you want to add to a custom toolbar in the list.
2.  Press the **Toolbar** button.
3.  Two \'walkthrough\' dialogs will guide you through the required steps. See [Interface Customization](Interface_Customization.md) for more information.

### Download

1.  Press the **Download** button to start the [Addon manager](Std_AddonMgr.md).

## Notes

-   To learn more about macros see the [Macros](Macros.md) page.

## Preferences

-   The user macros location can also be changed in the preferences: **Edit → Preferences... → Python → Macro → Macro path**. See [Preferences Editor](Preferences_Editor#Macro.md).





{{Std Base navi

}}



---
⏵ [documentation index](../README.md) > Std DlgMacroExecute/ro
