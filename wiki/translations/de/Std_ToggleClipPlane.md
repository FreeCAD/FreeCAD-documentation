---
- GuiCommand:/de
   Name:Std ToggleClipPlane
   Name/de:Std ToggleClipPlane
   MenuLocation:Ansicht → Schnittebene
   Workbenches:Alle
   Shortcut:
   SeeAlso:
---

# Std ToggleClipPlane/de


</div>

## Description


<div class="mw-translate-fuzzy">

Eine **Schnittebene** ist eine Ebene, die den Objektraum in zwei Halbräume teilt. Alle Objektteile in einem Halbraum sind sichtbar, Teile des anderen Halbraums sind unsichtbar. Die Objekte sehen aufgeschnitten aus und interne Details werden sichtbar. Die Schnittebene wird durch das [Ansicht](Std_View_Menu/de.md) → **Schnittebene**-Menü aktiviert.


</div>

![](images/Std_ToggleClipPlane_example.png ) 
*A clipped hollow object*

![](images/Std_ToggleClipPlane_taskpanel.png ) 
*The Clipping task panel*

## Usage

1.  Select the **View → <img src="images/Std_ToggleClipPlane.svg" width=16px> Clipping plane** option from the menu.
2.  In the Clipping task panel do one of the following:
    -   Check one or more of the {{CheckBox|TRUE|Clipping X}} to {{CheckBox|TRUE|Clipping Z}} checkboxes.
        -   Optionally change the offset distance(s).
        -   Optionally press the **Flip** button(s) to change the side of the clipping plane objects are hidden on.
    -   Check the {{CheckBox|TRUE|Clipping custom direction}} checkbox.
        -   Optionally change the offset distance.
        -   Do one of the following:
            -   Press the **View** button to use the direction of the current view.
            -   Check the {{CheckBox|TRUE|Adjust to view direction}} checkbox for a direction that dynamically adepts to view changes.
            -   Specify the direction by entering the X, Y and Z coordinates of a normal vector.
3.  Optionally change the view to inspect the model.
4.  Press the **Close** button to close the task panel and finish the command.

## Notes

-   To clearly distinguish the interior of partially clipped objects change their **Lighting** property to \'One side\'. The color of the interior side of their faces will then depend on the backlight settings: **Edit → Preferences... → Display → 3D View → Backlight color - Intensity**. See [Preferences Editor](Preferences_Editor#3D_View.md).





{{Std_Base_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std ToggleClipPlane/de
