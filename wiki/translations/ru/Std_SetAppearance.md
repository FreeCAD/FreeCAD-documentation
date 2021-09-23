---
- GuiCommand:/ru
   Name:Std SetAppearance
   Name/ru:Внешний вид
   MenuLocation:Вид → Внешний вид...
   Workbenches:All
   Shortcut:**Ctrl**+**D**
   SeeAlso:[Part FaceColors](Part_FaceColors/ru.md)
---

## Описание

The **Std SetAppearance** command shows the Display properties [task panel](Task_panel.md) for selected objects.

## Применение

1.  Select one or more objects.
2.  There are several ways to invoke the command:
    -   Select the **View → <img src="images/Std_SetAppearance.svg" width=16px> Appearance...** option from the menu.
    -   Select the **<img src="images/Std_SetAppearance.svg" width=16px> Appearance...** option from the [Tree view](Tree_view.md) context menu or [3D view](3D_view.md) context menu.
    -   Use the keyboard shortcut: **Ctrl**+**D**.
3.  Change one or more display properties. See [Options](#Options.md). The objects will update immediately.
4.  Optionally select one or more new objects whose display properties you want to change.
5.  Press the **Close** button to close the task panel and finish the command.

## Опции

### Viewing mode 

-   Select a **Display Mode** from the dropdown list. The available options are: \'Flat lines\', \'Shaded\' (not for [Draft](Draft_Workbench.md) objects), \'Wireframe\' and \'Points\'. See the [Std DrawStyle](Std_DrawStyle.md) command for more information.

### Material

-   Select a predefined material from the dropdown list (\'Default\', \'Aluminum\', \'Brass\', \'Bronze\', etc.).
-   Press the **...** button to open the Material properties dialog box and edit the ambient, diffuse, emissive and specular colors, as well as the shininess.
-   **Color plot:** unsupported at this time.
-   **Shape color:** sets the **Shape Color** property. Press the button to open the Select color dialog box.
-   **Line color:** sets the **Line Color** property. Press the button to open the Select color dialog box.

### Display

-   **Point size:** sets the **Point Size** property (in pixels).
-   **Line width:** sets the **Line Width** property (in pixels).
-   **Transparency:** sets the **Transparency** property (in percentage). 0% is opaque, 100% is fully transparent.
-   **Line transparency:** unsupported at this time.

## Примечания

-   The mentioned view properties can also be changed in the [Property editor](Property_editor.md) or the [Combo view](Combo_view.md).





{{Std Base navi

}}  
