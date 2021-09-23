---
- GuiCommand:/ro
   Name:Std DlgMacroRecord
   Name:Std DlgMacroRecord
   MenuLocation:[Macro](Macros/ro.md) → Macro recording ...
   Workbenches:All
   SeeAlso:[Execute macro](Std_DlgMacroExecuteDirect/ro.md)
---

# Std DlgMacroRecord/ro


</div>


<div class="mw-translate-fuzzy">

## Descriere


</div>


<div class="mw-translate-fuzzy">

Această funcție înregistrează la macro, toate operațiile efectuate în spațiul 3D.


</div>

![](images/Std_DlgMacroRecord_dialog.png ) *The Macro recording dialog box*


<div class="mw-translate-fuzzy">

## Utilizare


</div>


<div class="mw-translate-fuzzy">

Este accesibil via **Macro → Macro recording ...**, sau pe calea apăsării butonului **<img src=images/Std_DlgMacroRecord.png style="width:16px"> Macro recording** în bara de instrumente Macros <img alt="" src=images/Macros_toolbar.jpg  style="width:96px;">.


</div>

## Options

-   When the Macro recording dialog box is displayed: press **Esc** or the **Cancel** button to abort the command.

## Notes

-   To execute the recorded macro use the [Std DlgMacroExecute](Std_DlgMacroExecute.md) command.
-   To learn more about macros see the [Macros](Macros.md) page.

## Preferences

-   The macro path can also be changed in the preferences: **Edit → Preferences... → General → Macro → Macro path**. See [Preferences Editor](Preferences_Editor#Macro.md).
-   In most cases it is undesirable to record actions that do not change the model: under **Edit → Preferences... → General → Macro → GUI commands** do one of the following:
    -   To exclude these actions uncheck the {{CheckBox|FALSE|Record GUI commands}} checkbox.
    -   To include them as comments only check both the {{CheckBox|TRUE|Record GUI commands}} and {{CheckBox|TRUE|Record as comment}} checkboxes.





{{Std Base navi

}}

---
[documentation index](../README.md) > Std DlgMacroRecord/ro
