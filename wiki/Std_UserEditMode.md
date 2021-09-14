---
- GuiCommand:
   Name:Std UserEditMode
   MenuLocation:Edit → Edit mode
   Workbenches:All
   Version:0.20
   SeeAlso:[Std Edit](Std_Edit.md)
---

## Description

The **Std UserEditMode** command defines the edit mode to be used when an object is double-clicked in the [Tree view](Tree_view.md).

## Usage

Choose an edit mode among available ones:

1.  <img alt="" src=images/EditModeDefault.svg  style="width:24px;"> **Default**: the object will be edited with its default mode. The edit mode is defined internally to be the most appropriate according the object type: for example, it will be shape properties edition for Part primitives and PartDesign features, placement edition with transform tool for boolean operations, \...
2.  <img alt="" src=images/EditModeTransform.svg  style="width:24px;"> **Transform**: the object will have its placement editable with the [Transform manipulator](Std_TransformManip.md)
3.  <img alt="" src=images/EditModeCutting.svg  style="width:24px;"> **Cutting**: ??? this mode is implemented as available but seems to be currently not used by any object in FreeCAD
4.  <img alt="" src=images/EditModeColor.svg  style="width:24px;"> **Color**: the object will have its individual faces color editable with the [face color editor](Part_FaceColors.md)

## Notes

-   Not all objects support all edit modes. In case the selected edit mode isn\'t supported by the edited object, it will fall back to its default mode

## Scripting


**See also:**

[FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

To list the available edit modes:

 
```python
import FreeCADGui
FreeCADGui.listUserEditModes()
```

To get the active edit mode:

 
```python
import FreeCADGui
FreeCADGui.getUserEditMode()
```

To set the active edit mode:

 
```python
import FreeCADGui
FreeCADGui.setUserEditMode(MODENAME) # Where MODENAME is a string available in the list of edit modes
```




 {{Std Base navi}} 
