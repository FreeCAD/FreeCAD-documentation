---
- GuiCommand   *
   Name   *Std UserEditMode
   MenuLocation   *Edit → Edit mode → ...
   Workbenches   *All
   Version   *0.20
   SeeAlso   *[Std Edit](Std_Edit.md)
---

# Std UserEditMode/en

## Description

The **Std UserEditMode** command defines the edit mode to be used when an object is double-clicked in the [Tree view](Tree_view.md).

## Usage

1.  In the menu go to **Edit → Edit mode** and select an edit mode.

## Available edit modes 

### <img alt="" src=images/Std_UserEditModeDefault.svg  style="width   *24px;"> Default 

The object will be edited using its default mode. This edit mode is defined internally to be the most appropriate for the object type. For example, it will be shape properties edition for [Part primitives](Part_Primitives.md) and [PartDesign features](PartDesign_Feature.md), placement edition for [Part booleans](Part_Boolean.md), etc.

### <img alt="" src=images/Std_UserEditModeTransform.svg  style="width   *24px;"> Transform 

The object will have its placement editable with the [Std TransformManip](Std_TransformManip.md) command.

### <img alt="" src=images/Std_UserEditModeCutting.svg  style="width   *24px;"> Cutting 

This edit mode is implemented as available but currently does not seem to be used by any object.

### <img alt="" src=images/Std_UserEditModeColor.svg  style="width   *24px;"> Color 

The object will have the color of its individual faces editable with the [Part FaceColors](Part_FaceColors.md) command.

## Notes

-   Not all objects support all edit modes. If the selected mode isn\'t supported by the object, its default edit mode will be used instead.

## Preferences

-   The last edit mode is stored   * **Tools → Edit parameters... → BaseApp → Preferences → General → UserEditMode**. It is an integer value. Possible values are {{Incode|0}} (Default), {{Incode|1}} (Transform), {{Incode|2}} (Cutting) or {{Incode|3}} (Color). The default is {{Incode|0}}.

## Scripting


**See also   ***

[FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

To list the available edit modes   *


```python
import FreeCADGui
FreeCADGui.listUserEditModes()
```

To get the active edit mode   *


```python
import FreeCADGui
FreeCADGui.getUserEditMode()
```

To set the active edit mode   *


```python
import FreeCADGui
FreeCADGui.setUserEditMode(MODENAME) # Where MODENAME is a string available in the list of edit modes
```





{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std UserEditMode/en
