---
- GuiCommand   *
   Name   *Std FreezeViews
   Empty   *1
   MenuLocation   *View → Freeze display → ...
   Workbenches   *All
   SeeAlso   *[Std ViewIvIssueCamPos](Std_ViewIvIssueCamPos.md)
---

# Std FreezeViews/en

## Introduction

FreeCAD can store camera settings in up to 50 \'frozen views\'. The menu options that deal with frozen views can be found in the **View → Freeze display** submenu. Frozen views are not stored in the document and, if not saved with the **[Save views\...](#Save_views.md)** menu option, will be lost when the FreeCAD application closes.

## Save views 

### Description

The **Save views\...** menu option saves all existing frozen views in a file with the \*.cam extension.

### Usage

1.  To use this option one or more frozen views must exist. A frozen view is created with the **[Freeze view](#Freeze_view.md)** menu option.
2.  Select the **View → Freeze display → Save views...** option from the menu.
3.  Enter a filename in the dialog box.
4.  Press the **Save** button.

### Options

-   Press **Esc** or the **Cancel** button to abort the command.

## Load views 

### Description 

The **Load views\...** menu option loads frozen views from a file with the \*.cam extension. All existing frozen views will be deleted.

### Usage 

1.  Select the **View → Freeze display → Load views...** option from the menu.
2.  Press the **Yes** button in the Restore views dialog box to confirm you want to lose all existing frozen views.
3.  Select a file.
4.  Press the **Open** button.

### Options 

-   If the Restore views dialog box is displayed   * press **Esc** or the **No** button to abort the command.
-   If the file dialog box is displayed   * press **Esc** or the **Cancel** button to abort the command.

## Freeze view 

### Description 

The **Freeze view** menu option saves the current camera settings (direction, zoom, etc.) of the [3D view](3D_view.md) in a new entry in the frozen view list. The frozen view list can contain up to 50 frozen views.

### Usage 

1.  There are several ways to invoke this option   *
    -   Select the **View → Freeze display → Freeze view** option from the menu.
    -   Use the keyboard shortcut   * **Shift**+**F**.
2.  The new frozen view can be selected in the **View → Freeze display** submenu.

## Clear views 

### Description 

The **Clear views** menu option deletes all existing frozen views.

### Usage 

1.  Select the **View → Freeze display → Clear views** option from the menu.

## Restore view 

### Description 

For each frozen view a **Restore view** option is added with which it can be restored. The options are numbered   * **Restore view 1** - **Restore view 50**.

### Usage 

1.  There are several ways to invoke this option   *
    -   Select the correct **View → Freeze display → Restore view** option from the menu.
    -   For the first 9 frozen views   * use the keyboard shortcut   * **Ctrl**+**1** - **Ctrl**+**9**.





{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std FreezeViews/en
