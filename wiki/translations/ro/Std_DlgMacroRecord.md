---
 GuiCommand:
   Name: Std DlgMacroRecord
   Name/ro: Std DlgMacroRecord
   MenuLocation: Macros/ro , Macro recording ...
   Workbenches: All
   SeeAlso: Std_DlgMacroExecuteDirect/ro
---

# Std DlgMacroRecord/ro




<div class="mw-translate-fuzzy">

## Descriere


</div>


<div class="mw-translate-fuzzy">

Această funcție înregistrează la macro, toate operațiile efectuate în spațiul 3D.


</div>

![](images/Std_DlgMacroRecord_dialog.png ) 
*The Macro recording dialog box*




<div class="mw-translate-fuzzy">

## Utilizare


</div>


<div class="mw-translate-fuzzy">

Este accesibil via **Macro → Macro recording ...**, sau pe calea apăsării butonului **[<img src=images/Std_DlgMacroRecord.png style="width:16px"> Macro recording** în bara de instrumente Macros <img alt="" src=images/Macros_toolbar.jpg  style="width:96px;">.


</div>

## Options

-   When the Macro recording dialog box is displayed: press **Esc** or the **Close** button to abort the command.

## Notes

-   To execute the recorded macro use the [Std DlgMacroExecute](Std_DlgMacroExecute.md) command.
-   To learn more about macros see the [Macros](Macros.md) page.

## Preferences

See also: [Preferences Editor](Preferences_Editor.md).

-   The macro path can also be changed in the preferences: **Edit → Preferences... → Python → Macro → Macro path**.
-   In most cases it is undesirable to record actions that do not change the model: under **Edit → Preferences... → Python → Macro → GUI commands** do one of the following:
    -   To exclude these actions uncheck the **Record GUI commands** checkbox.
    -   To include them as comments only, check both the **Record GUI commands** and **Record as comment** checkboxes.





{{Std_Base_navi

}}



---
⏵ [documentation index](../README.md) > Std DlgMacroRecord/ro
