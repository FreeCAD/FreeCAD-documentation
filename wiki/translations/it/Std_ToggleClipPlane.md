---
- GuiCommand:/it
   Name:Std ToggleClipPlane
   Name/it:Piano di taglio
   Empty:1
   MenuLocation:Visualizza → Piano di taglio
   Workbenches:Tutti
---


</div>

## Descrizione


<div class="mw-translate-fuzzy">

Un **piano di taglio** divide lo spazio dell\'oggetto in due metà. Tutte le parti dell\'oggetto che si trovano in un semispazio sono visibili, mentre le parti nell\'altra metà sono invisibili. Gli oggetti sembrano affettati e diventano visibili i dettagli interni. Il piano si attiva nel menu {{MenuCommand|Visualizza → Piano di taglio}}.


</div>

![](images/Std_ToggleClipPlane_example.png ) *A clipped hollow object*

![](images/Std_ToggleClipPlane_taskpanel.png ) *The Clipping task panel*

## Utilizzo

1.  Select the {{MenuCommand|View → <img src="images/Std_ToggleClipPlane.svg" width=16px> Clipping plane}} option from the menu.
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

## Note

-   To clearly distinguish the interior of partially clipped objects change their **Lighting** property to \'One side\'. The color of the interior side of their faces will then depend on the backlight settings: {{MenuCommand|Edit → Preferences... → Display → 3D View → Backlight color - Intensity}}. See [Preferences Editor](Preferences_Editor#3D_View.md).


<div class="mw-translate-fuzzy">





</div>


{{Std Base navi

}}  
