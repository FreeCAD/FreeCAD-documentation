---
- GuiCommand   */de
   Name   *Std StoreWorkingView
   Name/de   *Std ArbeitsansichtSpeichern
   MenuLocation   *View → Standardansichten → Arbeitsansicht speichern
   Workbenches   *Alle
   Shortcut   ***Shift**+**End**
   Version   *1.0
   SeeAlso   *[Std ArbeitsansichtWiederherstellen](Std_RecallWorkingView/de.md), [Std AnsichtenEinfrieren](Std_FreezeViews/de.md)
---

# Std StoreWorkingView/de

## Beschreibung

The **Std StoreWorkingView** command stores the camera settings of the active [3D view](3D_view.md) in its temporary working view. This view can be recalled with the [Std RecallWorkingView](Std_RecallWorkingView.md) command.

Each 3D view has its own working view. Storing a new working view will overwrite the existing working view of the active 3D view. When a 3D view is closed its working view is lost.

## Anwendung

1.  Make sure a [3D view](3D_view.md) is active.
2.  There are several ways to invoke the command   *
    -   Select the **View → Standard views → Store working view** option from the menu.
    -   Use the keyboard shortcut   * **Shift**+**End**.

## Skripten


**Siehe auch   ***

[FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

To store the current camera settings of the active 3D view in a working view   *


```python
import FreeCADGui

FreeCADGui.runCommand("Std_StoreWorkingView", 0)
```





{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std StoreWorkingView/de
