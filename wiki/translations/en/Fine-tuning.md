


{{TOCright}}

This page holds different settings and parameters that you can use to fine-tune your FreeCAD installation or overcome problems.

## Option parameters {#option_parameters}

The FreeCAD [Preferences Editor](Preferences_Editor.md) under menu {{MenuCommand|Edit → Preferences}} is commonly used to set and manipulate the FreeCAD parameters table.

However, it is also possible to access, modify and create parameters manually, using the [Parameter Editor](Std_DlgParameter.md) found under menu {{MenuCommand|Tools → Edit parameters}}.

The list below shows parameters that are not accessible via the preferences editor, but that you can set manually (located in **BaseApp/Preferences**)

-   **Bitmaps/Theme/ThemeSearchPaths** (boolean): Set to `False` so FreeCAD uses it\'s included icons instead of the system icon theme on Linux.
-   **DockWindows/DAGView/Enabled** (boolean): Set to `True` to enable a beta [DAG view](DAG_view.md) dockable widget. After changing the parameter value, a FreeCAD restart is needed so the widget is available in the View/Panels list.
-   **DockWindows/PropertyView/Enabled** (boolean): Set to `True` to enable a [Property View](Property_editor.md) dockable widget independent from the Combo View. After changing the parameter value, a FreeCAD restart is needed so the widget is available in the View/Panels list.
-   **DockWindows/TreeView/Enabled** (boolean): Set to `True` to enable a [Tree View](Document_structure.md) dockable widget independent from the Combo View. After changing the parameter value, a FreeCAD restart is needed so the widget is available in the View/Panels list.
-   **Document/ChangeViewProviderTouchDocument** (boolean) : Set to `False` so items visibility changes won\'t mark the document as changed.
-   **Document/SaveThumbnailFix** (boolean): Set to `True` to fix a problem with Qt5 that prevents the generation of `.FCStd` file thumbnails.
-   **General/RecentIncludesExported** (boolean): Set to `True` to include exported files in the Recent Files list. Defaults to `False`.
-   **General/RecentIncludesImported** (boolean): Set to `False` to exclude imported files from the Recent Files list. Defaults to `True`.
-   **Mod/Draft/defaultCameraHeight** (int) : Sets the height of the camera when Draft starts in an empty document. 0 disables, FreeCAD default is 5, good when working in millimeters, a good height for arch work is 4500.
-   **Mod/Part/ParametricRefine** (boolean) : Set to `False` so [Part RefineShape](Part_RefineShape.md) creates an independent copy rather than a linked one. Defaults to `True`.
-   **Mod/PartDesign/AdditiveHelixPreview** (boolean): Set to `True` to ensure an additive helix that does not intersect the body is visible in the preview. Defaults to `False`.
-   **Mod/PartDesign/SubtractiveHelixPreview** (boolean): Set to `True` to ensure a subtractive helix that does not intersect the body is visible in the preview. Defaults to `True`.
-   **Mod/PartDesign/SwitchToTask** (boolean): Set to `False` to prevent the [PartDesign Workbench](PartDesign_Workbench.md) from switching to the Task panel when starting. Defaults to `True`.
-   **Mod/PartDesign/SwitchToWB** (boolean): Set to `False` to prevent the [PartDesign Workbench](PartDesign_Workbench.md) to be automatically called when a [PartDesign Body](PartDesign_Body.md) is activated. Defaults to `True`.
-   **PropertyView/AutoTransactionView** (boolean) : Set to `True` so changes of View tab properties are added to the undo stack (hence are undoable). Defaults to `False`.
-   **View/NavigationDebug** (boolean) : enables debug output of navigation styles (as of v0.19, only Gesture navigation style has something to say).
-   **View/SavePicture** (string): Set to **FramebufferObject**, **PixelBuffer** or **CoinOffscreenRenderer** for different methods to produce images from the 3D view.

### Export Default Filename {#export_default_filename}

-   **General/ExportDefaultFilenameMultiple** (string): Set the default filename to use when exporting multiple objects. Defaults to \"%F\".
-   **General/ExportDefaultFilenameSingle** (string): Set the default filename to use when exporting a single object. Defaults to \"%F-%P-\".

Both of these options support the automatic insertion of various pieces of information into the filename, using the following format characters:

-   %F - the name of the .FCStd file (or the label, if it is not saved yet)
-   %Lx - the label of the selected object(s), separated by character \'x\'
-   %Px - the label of the selected object(s) and their first parent, separated by character \'x\'
-   %U - the date and time, in UTC, [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)
-   %D - the date and time, in local timezone, [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)

Any other characters are treated literally. If the resulting filename is illegal it will be changed on saving, with illegal characters replaced by the underscore (\_).

## Mouse related {#mouse_related}

-   **General/ComboBoxWheelEventFilter** (boolean) : Set to `True` so widgets do not catch mouse wheel event and prevent scrollable areas to be scrolled.
-   **View/GestureMoveThreshold** (integer) : the distance (px) mouse cursor has to move to enter rotation or pan modes of Gesture navigation style. Default is 5.
-   **View/GestureRollFwdCommand**, **View/GestureRollBackCommand** (string) : commands to be executed by mouse button roll gestures of Gesture navigation style.
-   **View/GestureTapHoldTimeout** (integer) : sets for how long to wait (in milliseconds) to enter pan mode in Gesture navigation style. It can be helpful to increase it if dragging geometry in sketcher is difficult. Default is 700.

## Keyboard Shortcuts {#keyboard_shortcuts}

### Escape Key {#escape_key}

-   **General/TasksKeyEsc** (boolean) : Create and set to `False` to disable the **ESC** key exiting the [Task panel](Task_panel.md) in all workbenches (that is if the task panel has focus). **Note:** Superceded by [Sketcher Preferences](Sketcher_Preferences#General.md).
-   **Mod/Sketcher/ViewKeyEsc** (boolean) : Create and set to `False` to disable **ESC** key issues with pressing one to many times, when escaping sketcher geometry/constraints creation continue mode (see [forum thread](https://forum.freecadweb.org/viewtopic.php?f=3&t=42207&start=60#p367584))

## Specific Workbenches {#specific_workbenches}

-   <img alt="" src=images/Workbench_TechDraw.svg  style="width:16px;"> [TechDraw Workbench](TechDraw_Workbench.md) has several hidden switches documented in [TechDraw Preferences](TechDraw_Preferences#Hidden_Settings.md).
-   <img alt="" src=images/Workbench_Path.svg  style="width:16px;"> [Path Workbench](Path_Workbench.md) has a switch to enable experimental features documented in [Path experimental](Path_experimental.md).
-   <img alt="" src=images/Workbench_BIM.svg  style="width:16px;"> [BIM Workbench](BIM_Workbench.md):
    -   **Mod/BIM/DefaultPageScale** (float): Default scaling for new TechDraw pages created from the BIM Workbench, in case the template doesn\'t contain any \"Scale\" or \"Scaling\" (text insensitive) editable text field.

## Related

-   [Parameter editor](Std_DlgParameter.md)
-   [Preferences editor](Preferences_editor.md)




[Category:Developer Documentation{{\#translation:}}](Category:Developer_Documentation.md)
