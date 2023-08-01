# Fine-tuning/en
## Introduction

The FreeCAD [Preferences Editor](Preferences_Editor.md) under menu **Edit → Preferences** is commonly used to set and manipulate the FreeCAD parameters table.

However, it is also possible to access, modify and create parameters manually, using the [Parameter Editor](Std_DlgParameter.md) found under menu **Tools → Edit parameters**.

This page lists parameters that are not accessible via the preferences editor, but that you can set manually to fine-tune your FreeCAD installation or overcome problems. All parameters are located in **BaseApp/Preferences/**.

## General

-   **Addons/developerMode** (boolean): Set to `True` to enable the developer mode of the [Addon Manager](Std_AddonMgr.md). See [Package Metadata](Package_Metadata#Validation.md).

-   **Bitmaps/Theme/ThemeSearchPaths** (boolean): Set to `False` so FreeCAD uses its included icons instead of the system icon theme on Linux.

-   **Dialog/DontUseNativeColorDialog** (boolean): Color picker dialog setting. Set to `False` if you want FreeCAD to use the native color dialog on your system rather than the Qt Color Dialog. Defaults to `True`.

-   **Dialog/DontUseNativeDialog** (boolean): File dialog setting. Set to `False` if you want to use the native File dialog when opening files or to `True` to use the Qt File Picker Dialog. Default depends on a compile time setting: #define (USE_QT_FILEDIALOG).

-   **Dialog/DontUseNativeFontDialog** (boolean): Used by the [Draft ShapeString](Draft_ShapeString.md) command. Set to `False` to use the native Font dialog. Defaults to `True`.

-   **DockWindows/DAGView/Enabled** (boolean): Set to `True` to enable a beta [DAG view](DAG_view.md) dockable widget. After changing the parameter value, a FreeCAD restart is needed so the widget is available in the View/Panels list.

-   **DockWindows/PropertyView/Enabled** (boolean): Set to `True` to enable a [Property View](Property_editor.md) dockable widget independent from the Combo View. After changing the parameter value, a FreeCAD restart is needed so the widget is available in the View/Panels list.

-   **DockWindows/TreeView/Enabled** (boolean): Set to `True` to enable a [Tree View](Document_structure.md) dockable widget independent from the Combo View. After changing the parameter value, a FreeCAD restart is needed so the widget is available in the View/Panels list.

-   **Document/AutoNameDynamicProperty** (boolean): Set to `True` to make FreeCAD automatically rename dynamic properties with an invalid specified name instead of throwing an exception. Note that Python code will not have access to the new name.

-   **Document/ChangeViewProviderTouchDocument** (boolean): Set to `False` so items visibility changes won\'t mark the document as changed.

-   **Document/SaveThumbnailFix** (boolean): Set to `True` to fix a problem with Qt5 that prevents the generation of `.FCStd` file thumbnails.

-   **General/LockToolBars** (boolean): Set to `True` to prevent toolbars from being draggable, and to hide the small drag handles. Mostly used in conjunction with stylesheets that make the toolbars vertical.

-   **General/RecentIncludesExported** (boolean): Set to `True` to include exported files in the Recent Files list. Defaults to `False`.

-   **General/RecentIncludesImported** (boolean): Set to `False` to exclude imported files from the Recent Files list. Defaults to `True`.

-   **Macro/DuplicateFrom001** (boolean): Set to `True` to always begin searching for suggested duplicate macro filename with \@001 instead of current \@NNN, if applicable. Defaults to `False`.

-   **Macro/DuplicateIgnoreExtraNote** (boolean): Set to `True` to ignore extra note when suggesting duplicate macro filename. Extra note is text in the filename following \"@NNN\" and before \".FCMacro\". Example: \"my_macro@005.my_note.FCMacro\". If `True` the next suggested filename is \"my_macro@006.FCMacro\". If set to `False` the next suggested filename is \"my_macro@006.my_note.FCMacro\". To be recognized as an extra note the text should begin with a dot (\".\") following the \"@NNN\". Otherwise, for example \"my_macro@006_my_note.FCMacro\" gets \"my_macro@006_my_note@001.FCMacro\" as suggested new filename, which might be desirable in some cases. Defaults to `False`.

-   **Macro/ReplaceSpaces** (boolean): Set to `False` if you do not want spaces in your filenames automatically converted to underscores when creating, renaming, or duplicating a macro. Does not affect existing files, only matters when creating new file or renaming or duplicating existing file. Defaults to `True`.

-   **MainWindow/ClearMenuBar** (boolean): Set to `True` to clear the menu bar on workbench change, useful when using a global menu as they may fail to update on workbench change and quickly get cluttered with each workbench\'s menu entries. Defaults to `False`. On macOS it is cleared either way to workaround a Qt bug.

-   **MainWindow/ToolBarNameAsToolTip** (boolean): Set to `False` to not get the toolbar name as a tooltip. Defaults to `True`.

-   **PropertyView/AutoTransactionView** (boolean): Set to `True` so changes of View tab properties are added to the undo stack (hence are undoable). Defaults to `False`.

-   **Selection/AutoShowSelectionView** (boolean): Set to `True` to make the Selection View pane show automatically when selecting something. Defaults to `False`.

-   **Selection/singleClickFeatureSelect** (boolean): Set to `False` to disable single click selection of a feature in PartDesign. Defaults to `True`.

-   **TreeView/HideColumn** (boolean): Set to {{True}} to hide the \'Description\' column in the [Tree view](Tree_view.md). Defaults to `False`.

-   **TreeView/TreeViewStretchDescription** (boolean): Set to `True` to stretch the \'Description\' column in the [Tree view](Tree_view.md) to the right edge of the pane. Defaults to `False`.

-    {{VersionMinus|0.20}}**View/Dimensions3dColor** (string): Set to a hex color value in the format `#RRGGBB` to change the direct dimension display color in [Part Measure Linear](Part_Measure_Linear.md). For <small>(v0.21)</small>  see [PartDesign Preferences](PartDesign_Preferences#Measure.md).

-    {{VersionMinus|0.20}}**View/DimensionsAngularColor** (string): Set to a hex color value in the format `#RRGGBB` to change the angular dimension display color in [Part Measure Angular](Part_Measure_Angular.md). For <small>(v0.21)</small>  see [PartDesign Preferences](PartDesign_Preferences#Measure.md).

-    {{VersionMinus|0.20}}**View/DimensionsDeltaColor** (string): Set to a hex color value in the format `#RRGGBB` to change the orthogonal dimensions display color in [Part Measure Linear](Part_Measure_Linear.md). For <small>(v0.21)</small>  see [PartDesign Preferences](PartDesign_Preferences#Measure.md).

-   **View/NavigationDebug** (boolean): Enables debug output of navigation styles (as of v0.19, only Gesture navigation style has something to say).

-   **View/SavePicture** (string): Set to **FramebufferObject**, **PixelBuffer** or **CoinOffscreenRenderer** for different methods to produce images from the 3D view.

## Default export filename 

-   **General/ExportDefaultFilenameMultiple** (string): Set the default filename to use when exporting multiple objects. Defaults to \"%F\".
-   **General/ExportDefaultFilenameSingle** (string): Set the default filename to use when exporting a single object. Defaults to \"%F-%P-\".

Both of these options support the automatic insertion of various pieces of information into the filename, using the following format characters:

-   %F - the name of the .FCStd file (or the label, if it is not saved yet)
-   %Lx - the label of the selected object(s), separated by character \'x\'
-   %Px - the label of the selected object(s) and their first parent, separated by character \'x\'
-   %U - the date and time, in UTC, [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)
-   %D - the date and time, in local timezone, [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)

Any other characters are treated literally. If the resulting filename is illegal it will be changed on saving, with illegal characters replaced by the underscore (\_).

## Mouse related 

-   **General/ComboBoxWheelEventFilter** (boolean): Set to `True` so widgets do not catch mouse wheel event and prevent scrollable areas to be scrolled. Needs FreeCAD restart to be taken into account.
-   **View/GestureMoveThreshold** (integer): the distance (px) mouse cursor has to move to enter rotation or pan modes of Gesture navigation style. Default is 5.
-   **View/GestureRollFwdCommand**, **View/GestureRollBackCommand** (string): commands to be executed by mouse button roll gestures of Gesture navigation style.
-   **View/GestureTapHoldTimeout** (integer): sets for how long to wait (in milliseconds) to enter pan mode in Gesture navigation style. It can be helpful to increase it if dragging geometry in sketcher is difficult. Default is 700.

## Keyboard shortcuts 

### Escape key 

-   **General/TasksKeyEsc** (boolean): Create and set to `False` to disable the **ESC** key exiting the [Task panel](Task_panel.md) in all workbenches (that is if the task panel has focus).

## Navigation Cube 

See [Navigation Cube](Navigation_Cube#Advanced_parameters.md).

## Specific workbenches 

### <img alt="" src=images/Workbench_BIM.svg  style="width:24px;"> [BIM Workbench](BIM_Workbench.md) 

-   **Mod/BIM/DefaultPageScale** (float): Default scaling for new TechDraw pages created from the BIM Workbench, in case the template doesn\'t contain any \"Scale\" or \"Scaling\" (case insensitive) editable text field.

### <img alt="" src=images/Workbench_Draft.svg  style="width:24px;"> [Draft Workbench](Draft_Workbench.md) 

-   **Mod/Draft/defaultCameraHeight** (int): Sets the height of the camera when Draft starts in an empty document. 0 disables, FreeCAD default is 5, good when working in millimeters, a good height for arch work is 4500.

### <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Part Workbench](Part_Workbench.md) 

-   **Mod/Part/ParametricRefine** (boolean): Set to `False` so [Part RefineShape](Part_RefineShape.md) creates an independent copy rather than a linked one. Defaults to `True`.

### <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [PartDesign Workbench](PartDesign_Workbench.md) 

-   **Mod/PartDesign/AdditiveHelixPreview** (boolean): Set to `True` to ensure an additive helix that does not intersect the body is visible in the preview. Defaults to `False`.
-   **Mod/PartDesign/SubtractiveHelixPreview** (boolean): Set to `True` to ensure a subtractive helix that does not intersect the body is visible in the preview. Defaults to `True`.
-   **Mod/PartDesign/SwitchToTask** (boolean): Set to `False` to prevent the [PartDesign Workbench](PartDesign_Workbench.md) from switching to the Task panel when starting. Defaults to `True`.
-   **Mod/PartDesign/SwitchToWB** (boolean): Set to `False` to prevent the [PartDesign Workbench](PartDesign_Workbench.md) to be automatically called when a [PartDesign Body](PartDesign_Body.md) is activated. Defaults to `True`.

### <img alt="" src=images/Workbench_Path.svg  style="width:24px;"> [Path Workbench](Path_Workbench.md) 

-   The [Path Workbench](Path_Workbench.md) has two switches to enable experimental features documented on the [Path experimental](Path_experimental.md) page.

### <img alt="" src=images/Workbench_Sketcher.svg  style="width:24px;"> [Sketcher Workbench](Sketcher_Workbench.md) 

-   **Mod/Sketcher/RadiusDiameterConstraintDisplayAngleRandomness** (float): Set an angle randomness on the above value. Value is the range of the random angle, centered on base angle. Default is 0 degree.
-   **Mod/Sketcher/RadiusDiameterConstraintDisplayBaseAngle** (float): Set the angle (from horizontal) used to display radius/diameter constraints in Sketcher at creation time. Default is 15 degrees (if no value set).
-   **Mod/Sketcher/RoundRectangleSuggConstraints** (boolean): Set to `False` to disable the addition of two extra construction points when creating a rounded rectangle. <small>(v0.21)</small> 

#### Constraint label colors 

The label in Sketcher that displays the current status of the constraints (e.g. \"Underconstrained,\" \"Fully Constrained,\" etc.) is styleable on a per-state basis either using the Qt stylesheet, or via user preferences. User preferences take precedence if they have been set (in **Mod/Sketcher/General**):

-   **EmptySketchMessageColor** - Defaults to 50% opacity black
-   **UnderconstrainedMessageColor** - Defaults to black
-   **MalformedConstraintMessageColor** - Defaults to red
-   **ConflictingConstraintMessageColor** - Defaults to red
-   **RedundantConstraintMessageColor** - Defaults to orange red
-   **PartiallyRedundantConstraintMessageColor** - Defaults to royal blue
-   **SolverFailedMessageColor** - Defaults to red
-   **FullyConstrainedMessageColor** - Defaults to green

### <img alt="" src=images/Workbench_Start.svg  style="width:24px;"> [Start Workbench](Start_Workbench.md) 

-   **Mod/Start/DefaultImportXXX** (string): Where XXX is a lowercase file extension. For example DefaultImportifc for .IFC files. Allows to set a default import module to be used when clicking an icon on the start page, when several importers are available. For example, setting DefaultImportifc = ifc_import will use the NativeIFC importer if available. <small>(v0.21)</small>



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > Fine-tuning/en
