# Tree view/en
{{TOCright}}

## Introduction

The [tree view](Tree_view.md) appears in the **Model** tab of the [combo view](Combo_view.md), one of the most important panels in the [interface](Interface.md); it shows all user defined objects that are part of a FreeCAD document. The tree view is a representation of the [document\'s structure](document_structure.md), and indicates what information is saved to disk.

These objects don\'t necessarily have to be geometrical shapes visible in the [3D view](3D_view.md), but can also be supporting data objects created with any of the [workbenches](Workbenches.md).

![](images/FreeCAD_Tree_view.png )



*The tree view showing various elements in the document.*

## Working with the tree view 

By default, whenever a new object is created, it is added to the end of the list in the tree view. The tree view allows managing the objects to keep them organized; it permits creating [groups](Std_Group.md), moving objects inside groups, moving groups inside other groups, renaming objects, copying objects, deleting objects, and other operations in the context menu (right click) which depend on the currently selected object and the currently active workbench.

Many operations create objects that are dependent on a previously existing object. In this case, the tree view shows this relationship by absorbing the older object inside the new object. Expanding and collapsing the objects in the tree view shows the parametric history of that object. Objects that are deeper inside others are older, while objects that are outside are newer, and are derived from the older objects. By modifying the interior objects, the parametric operations propagate all the way to the top, generating a new result.

<img alt="" src=images/FreeCAD_Tree_view_parametric_history_1.png  style="width:" height="304px;"> <img alt="" src=images/FreeCAD_Tree_view_parametric_history_2.png  style="width:" height="304px;">

<img alt="" src=images/FreeCAD_Tree_view_parametric_history_3.png  style="width:" height="304px;">



*The topmost object is created by doing parametric operations on objects which themselves were created by previous operations. Expanding the tree many levels reveals the original elements that were used to create the partial solids.*

### Labels & Attributes 

In the Labels & Attributes column the labels and icons of the objects are displayed.

Selecting an object in this column and pressing **F2** (on Windows and Linux), or **Enter** (on macOS), allows to edit the object\'s **Label** property in situ without detour via the context menu action described below or the [Property editor](Property_editor.md).

### Description

The Description column displays further information about objects, if available.

This information is stored in an object\'s **Label2** property which can be edited in situ by selecting the object in this column and pressing **F2** (on Windows and Linux), or **Enter** (on macOS), or via the [Property editor](Property_editor.md).

## Actions

Since the tree view lists objects that may be visible in the [3D view](3D_view.md), many of the actions are the same as those that can be executed from the [3D view](3D_view.md). The actions can be started from a **Context menu** that can be accessed by right clicking either the background or an object.

### Application start 

When the application starts, the default [Start Workbench](Start_Workbench.md) is active, and no document has been created, the context menu of the [tree view](Tree_view.md) has only one entry:

-    **Expression actions**. When the cursor is moved onto it, a sub-menu opens containing four commands:

    -   [Copy selected](Std_Expressions.md)
    -   [Copy active document](Std_Expressions.md)
    -   [Copy all documents](Std_Expressions.md)
    -   [Paste](Std_Paste.md)

These allow working with various documents, but are disabled if no document is present.

### New document 

Once a new document has been created right clicking the background opens the context menu now containing two entries:

-    **Expression actions**as above but with these two entries activated:

    -   [Copy active document](Std_Expressions.md)
    -   [Copy all documents](Std_Expressions.md)

-    **Link actions**\- a sub-menu with two entries:

    -   
        **Make Link group**
        
        \- another sub-menu containing three commands:

        -   [Simple group](Std_LinkMakeGroup.md)
        -   [Group with links](Std_LinkMakeGroup.md)
        -   [Group with transform links](Std_LinkMakeGroup.md)

    -   [Make Link](Std_LinkMake.md)

### Selecting the document 

If you select the document and right click, in addition to **Expression actions** and **Link actions**, the context menu contains the following commands:

-    **Show items hidden in tree view**: if active, the tree view will show hidden items.

-    **Search**: shows an input field to search objects inside the selected document.

-    **Close document**: closes the selected document.

-    **Add dependent objects to selection**: all dependent objects will be added to the selection. This way one can see the dependencies and e.g. delete all dependent objects at once. Only available for objects with links and for documents.

-    **Skip recomputes**: if active, the document\'s objects will not [recompute](Std_Refresh.md) automatically.

-    **Allow partial recomputes**: if active, the document will allow [recompute](Std_Refresh.md) of only some objects. Only available if **Skip recomputes** is activated.

-    **Mark to recompute**: marks all objects of the document as touched, and ready for [recompute](Std_Refresh.md).

-    **[Create group](Std_Group.md)**: creates a [group](Std_Group.md) in the selected document.

### Selecting objects 

Once objects are added to the document right clicking them will show additional commands. These depend on the number of selected objects, their type and also on the active workbench. In most cases and with most workbenches (except the [Start Workbench](Start_Workbench.md)) the following commands are then available:

-    **[Appearance](Std_SetAppearance.md)**: launches a dialog to change the visual properties of the whole object.

-    **[Random color](Std_RandomColor.md)**: assigns a random color to the object.

-    **[Cut](Std_Cut.md)**: disabled.

-    **[Copy](Std_Copy.md)**: copies an object into memory.

-    **[Paste](Std_Paste.md)**: pastes the copied object into the document; the copy is added to the end of the tree view.

-    **[Delete](Std_Delete.md)**: removes the object from the document.

-    **[Toggle visibility in tree view](#Eye_symbol.md)**: toggles the Tree view visibility of objects.

-    **Mark to recompute**: marks the selected object as touched, and ready for [recompute](Std_Refresh.md).

-    **Recompute object**: recomputes the selected object.

-    **Rename**: starts editing the label of the selected object, not the name which is read-only. This option is only available if a single object is selected.

As an example of context menu extension, if a [Part Box](Part_Box.md) is right clicked while the [Part Workbench](Part_Workbench.md) is active the following additional commands are available:

-    **[Edit](Std_Edit.md)**: activates the edit mode of the object.

-    **[Transform](Std_TransformManip.md)**: launches the transform widget to move or rotate the object.

-    **[Attachment editor](Part_EditAttachment.md)**: launches a dialog to attach the object to one or more other objects.

-    **[Set colors](Part_FaceColors.md)**: sets the color of selected faces of the object.

-    **[Toggle visibility](Std_ToggleVisibility.md)**: makes the object visible or invisible in the [3D view](3D_view.md).

-    **[Show selection](Std_ShowSelection.md)**: makes the selected object visible.

-    **[Hide selection](Std_HideSelection.md)**: makes the selected object invisible.

-    **[Toggle selectability](Std_ToggleSelectability.md)**: toggles the selectability of the object in the [3D view](3D_view.md).

-    **[Select all instances](Std_TreeSelectAllInstances.md)**: selects all instances of this object in the tree view.

-    **[Send to Python Console](Std_SendToPythonConsole.md)**: creates a variable in the [Python console](Python_console.md) referencing the object

### Keyboard actions 

The following keyboard actions are available when the focus is on the Tree view:

-    **Ctrl**\+**F**: opens a search box at the bottom of the tree, allowing to search and reach objects using their names or labels.

-   Expand and collapse actions using **Alt**+**Arrow** combinations: <small>(v0.20)</small> 
    -   
        **Alt**
        
        \+**Left**: collapses selected item(s).

    -   
        **Alt**
        
        \+**Right**: expands selected item(s).

    -   
        **Alt**
        
        \+**Up**: expands selected item(s) with all their tier-1 children collapsed (deeper children remain unchanged).

    -   
        **Alt**
        
        \+**Down**: expands selected item(s) with all their tier-1 children expanded as well (deeper children remain unchanged).

## Overlay icons 

One or more smaller overlay icons can be displayed on top of an object\'s default icon in the tree view. The available overlay icons and their meaning are listed below.

### ![](images/FreeCAD_Tree_view_recompute.png ) White check mark on blue background 

This indicates that the object has to be [recomputed](Std_Refresh.md), due to changes made to the model or because the user marked the object in the tree view context menu to be recomputed. In most cases recomputes are triggered automatically, but sometimes they are delayed for performance reasons.

### ![](images/FreeCAD_Tree_view_tip.png ) White arrow on green background 

This indicates the so called [Tip](PartDesign_Body#Tip.md) of a body. It is usually the last feature in a [PartDesign Body](PartDesign_Body.md) and represents the whole body to the world outside of the body, e.g. when the body is exported or used in [Part boolean](Part_Boolean.md) operations. The tip can be changed by the user.

### ![](images/FreeCAD_Tree_view_unattached.png ) Purple chain link on white background 

This is typically shown for [sketches](Sketch.md), geometric primitives, such as box, cylinder, etc. and [Datum](Datum.md) geometry. It indicates that the object is not attached to anything. It has no Attachment Offset and gets its position and alignment solely from its [Placement](Placement.md) property.

There is a [Basic Attachment Tutorial](Basic_Attachment_Tutorial.md) explaining how to handle such objects.

### ![](images/FreeCAD_Tree_view_notfullyconstrained.png ) Yellow X 

This is only used for [sketches](Sketch.md) and indicates that the sketch is not fully constrained. Inside of [Sketcher](Sketcher_Workbench.md) the number of remaining degrees of freedom is shown in the solver messages.

### ![](images/FreeCAD_Tree_view_error.png ) White exclamation mark on red background 

This indicates that the object has an error that needs to be fixed. After recomputing the whole document a tooltip describing the error is shown when you hover the mouse over the object in the tree view. Note: All other objects depending on an object in such an error state will not be properly recomputed, thus they may still show some old state.

### ![](images/FreeCAD_Tree_view_hidden.png ) Eye symbol 

This indicates that the object will be hidden in the Tree view if the **Show items hidden in tree view** context menu option is unchecked.


{{Interface navi

}} {{Std Base navi}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Tree view/en
