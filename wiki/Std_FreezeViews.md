---
- GuiCommand:
   Name:Std FreezeViews
   Empty:1
   MenuLocation:View → Freeze display → ...
   Workbenches:All
   SeeAlso:[Std ViewIvIssueCamPos](Std_ViewIvIssueCamPos.md)
---

## Introduction

FreeCAD can store camera settings in up to 50 \'frozen views\'. The menu options that deal with frozen views can be found in the {{MenuCommand|View → Freeze display}} submenu. Frozen views are not stored in the document and, if not saved with the **[Save views\...](#Save_views.md)** menu option, will be lost when the FreeCAD application closes.

## Save views {#save_views}

### Description

The **Save views\...** menu option saves all existing frozen views in a file with the \*.cam extension.

### Usage

1.  To use this option one or more frozen views must exist. A frozen view is created with the **[Freeze view](#Freeze_view.md)** menu option.
2.  Select the {{MenuCommand|View → Freeze display → Save views...}} option from the menu.
3.  Enter a filename in the dialog box.
4.  Press the **Save** button.

### Options

-   Press **Esc** or the **Cancel** button to abort the command.

## Load views {#load_views}

### Description {#description_1}

The **Load views\...** menu option loads frozen views from a file with the \*.cam extension. All existing frozen views will be deleted.

### Usage {#usage_1}

1.  Select the {{MenuCommand|View → Freeze display → Load views...}} option from the menu.
2.  Press the **Yes** button in the Restore views dialog box to confirm you want to lose all existing frozen views.
3.  Select a file.
4.  Press the **Open** button.

### Options {#options_1}

-   If the Restore views dialog box is displayed: press **Esc** or the **No** button to abort the command.
-   If the file dialog box is displayed: press **Esc** or the **Cancel** button to abort the command.

## Freeze view {#freeze_view}

### Description {#description_2}

The **Freeze view** menu option saves the current camera settings (direction, zoom, etc.) of the [3D view](3D_view.md) in a new entry in the frozen view list. The frozen view list can contain up to 50 frozen views.

### Usage {#usage_2}

1.  There are several ways to invoke this option:
    -   Select the {{MenuCommand|View → Freeze display → Freeze view}} option from the menu.
    -   Use the keyboard shortcut: **Shift**+**F**.
2.  The new frozen view can be selected in the {{MenuCommand|View → Freeze display}} submenu.

## Clear views {#clear_views}

### Description {#description_3}

The **Clear views** menu option deletes all existing frozen views.

### Usage {#usage_3}

1.  Select the {{MenuCommand|View → Freeze display → Clear views}} option from the menu.

## Restore view {#restore_view}

### Description {#description_4}

For each frozen view a **Restore view** option is added with which it can be restored. The options are numbered: **Restore view 1** - **Restore view 50**.

### Usage {#usage_4}

1.  There are several ways to invoke this option:
    -   Select the correct {{MenuCommand|View → Freeze display → Restore view}} option from the menu.
    -   For the first 9 frozen views: use the keyboard shortcut: **Ctrl**+**1** - **Ctrl**+**9**.




 {{Std Base navi}}  
