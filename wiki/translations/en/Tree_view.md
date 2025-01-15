# Tree view/en
## Introduction

The [Tree view](Tree_view.md) appears in the upper section of the **Model** panel (if the [Combo view](Combo_view.md) is active) or as a stand-alone panel. It shows all user defined objects that are part of a FreeCAD document. The Tree view is a representation of the [document\'s structure](Document_structure.md), and indicates what information is saved to disk.

These objects don\'t necessarily have to be geometrical shapes visible in the [3D view](3D_view.md), but can also be supporting data objects created with any of the [workbenches](Workbenches.md).

![](images/FreeCAD_Tree_view.png )



*The Tree view showing various elements in the document.*

## Working with the Tree view 

By default, whenever a new object is created, it is added to the end of the list in the Tree view. The Tree view allows managing the objects to keep them organized; it permits creating [groups](Std_Group.md), moving objects inside groups, moving groups inside other groups, relabeling objects, copying objects, deleting objects, and using options from its [context menu](#Context_menu.md).

Many operations create objects that are dependent on a previously existing object. In this case, the Tree view shows this relationship by absorbing the older object inside the new object. Expanding and collapsing the objects in the Tree view shows the parametric history of that object. Objects that are deeper inside others are older, while objects that are outside are newer, and are derived from the older objects. By modifying the interior objects, the parametric operations propagate all the way to the top, generating a new result.

<img alt="" src=images/FreeCAD_Tree_view_parametric_history.png  style="width:" height="300px;">



*The topmost object is created by doing parametric operations on objects which themselves were created by previous operations.<br>
Fully expanding the tree reveals the original elements that were used to create the partial solids.*

### Tree view columns 

The Tree view always displays a column with the icons and labels of objects. Two additional columns can optionally be displayed as well. To enable these columns right-click the Tree view and in the context menu select **Tree settings** and then **Show description** (<small>(v0.21)</small> ) and/or **Show internal name** (<small>(v1.0)</small> ). Column headings are added if more than one column is displayed. Note that the internal names of objects cannot be changed.

### Edit object label 

Select an object in the first column and press **F2** (on Windows and Linux), or **Enter** (on macOS), to edit its **Label** property. This property can also be edited via the context menu option **Rename** or in the [Property editor](Property_editor.md).

### Edit object description 

An object can optionally have a description. This information is stored in its **Label2** property. If the description column is displayed you can edit this property by selecting an object in that column and pressing **F2** (on Windows and Linux), or **Enter** (on macOS). The property can also be changed in the [Property editor](Property_editor.md).

### Context menu 

The options in the context menu of the Tree view depend on the selected object(s) and the currently active workbench. To display this menu right-click the background of the list, right-click an object in the list, or select multiple objects in the list and then right-click one of them.

### Keyboard modifiers 

The usual keyboard modifiers can be used in the Tree view. The modifiers can be combined as well.

-    **Ctrl**: hold down this key to select multiple objects.

-    **Shift**: hold down this key to select all objects between a previously selected object and the next selected object.

### Keyboard shortcuts 

The following keyboard shortcuts are available when the focus is on the Tree view:

-    **Ctrl**\+**F**: opens a search box at the bottom of the tree, allowing to search and reach objects using their internal names or labels.

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

One or more overlay icons can be displayed on top of an object\'s default icon in the Tree view. The available overlay icons and their meaning are listed below.

### ![](images/FreeCAD_Tree_view_recompute.png ) White check mark on blue background 

This indicates that the object has to be [recomputed](Std_Refresh.md), due to changes made to the model or because the user marked the object in the Tree view context menu to be recomputed. In most cases recomputes are triggered automatically, but sometimes they are delayed for performance reasons.

### ![](images/FreeCAD_Tree_view_error.png ) White exclamation mark on red background 

This indicates that the object has an error that needs to be fixed. After recomputing the whole document a tooltip describing the error is shown when you hover the mouse over the object in the Tree view. Note: All other objects depending on an object in such an error state will not be properly recomputed, thus they may still show some old state.

### ![](images/FreeCAD_Tree_view_unattached.png ) Purple chain link 

This is typically shown for [sketches](Sketch.md), [PartDesign](PartDesign_Workbench.md) primitives, such as box, cylinder, etc. and [Datum](Datum.md) geometry. It indicates that the object is not attached to anything. It has no Attachment Offset and gets its position and alignment solely from its [Placement](Placement.md) property.

There is a [Basic Attachment Tutorial](Basic_Attachment_Tutorial.md) explaining how to handle such objects.

### ![](images/FreeCAD_Tree_view_notfullyconstrained.png ) Yellow X 

This is only used for [sketches](Sketch.md) and indicates that the sketch is not fully constrained. If the sketch is in [edit mode](Sketcher_EditSketch.md) the number of remaining degrees of freedom is shown in the [solver messages](Sketcher_Dialog#Solver_messages.md).

### ![](images/FreeCAD_Tree_view_tip.png ) White arrow on green background 

This indicates the so called [Tip](PartDesign_Body#Tip.md) of a [PartDesign Body](PartDesign_Body.md). It is usually the last feature in a body and represents the whole body to the world outside of the body, e.g. when the body is exported or used in [Part boolean](Part_Boolean.md) operations. The tip can be changed by the user.

### ![](images/FreeCAD_Tree_view_suppressed.png ) Red backslash 


<small>(v1.0)</small> 

This indicates a suppressed [PartDesign](PartDesign_Workbench.md) feature.

### ![](images/FreeCAD_Tree_view_link.png ) White upwards curved arrow 

This indicates a [linked](Std_LinkMake.md) object.

### ![](images/FreeCAD_Tree_view_link_external.png ) Two white upwards curved arrows 

This indicates a [linked](Std_LinkMake.md) object loaded from an external document.

### ![](images/FreeCAD_Tree_view_hidden.png ) Eye symbol 

This indicates that the object will be hidden in the Tree view if the **Show items hidden in Tree view** context menu option is unchecked.

### ![](images/FreeCAD_Tree_view_frozen.png ) Cyan ice crystal 


<small>(v1.0)</small> 

This indicates a [frozen](Std_ToggleFreeze.md) object that is not recomputed when its parents change.

## Preferences

See [Combo view](Combo_view#Preferences.md).



---
⏵ [documentation index](../README.md) > Tree view/en
