---
 GuiCommand:
   Name: Std VarSet
   Workbenches: All
   Version: 1.0
   SeeAlso: Spreadsheet_Workbench, DynamicData_Workbench
---

# Std VarSet/en

## Description

The **Std VarSet** command creates a VarSet. A VarSet is a set of properties that can be used as variables in [expressions](Expressions.md).

![](images/Std_VarSet_Dialog.png ) 
*The Add a property dialog box*

## Usage

1.  Do one of the following:
    -   To create a new VarSet: press the **<img src="images/Std_VarSet.svg" width=16px> [Create a variable set](Std_VarSet.md)** button.
    -   To edit an existing VarSet: double-click the set in the [Tree view](Tree_view.md).
2.  The **Add a property** dialog box opens.
3.  Enter a **Name** for the property.
    -   The name must be unique for the VarSet.
    -   Only alphanumeric characters and underscores (`A` to `Z`, `a` to `z`, `0` to `9` and `_`) are allowed.
    -   The first character may not be a digit.
    -   FreeCAD uses the [UpperCamelCase](https://en.wikipedia.org/wiki/Camel_case) convention for its property names, meaning each word starts with a capital letter, and there are no spaces or underscores. When the [Property editor](Property_editor.md) displays such a name, spaces are inserted between the words, making the name easier to read. It is advisable to follow this convention.
4.  Enter a **Group** name for the property or select a group from the list. Group names have the same restrictions as property names.
5.  Select the property **Type** from the list. See below for the most [common types](#Common_property_types.md).
6.  Enter a **Value** for the property. This input accepts units for properties that have units.
7.  Optionally check the **Add another** checkbox if you want to add more properties.
8.  Optionally enter a **Tooltip** for the property.
9.  Press the **OK** button.
10. If the **Add another** checkbox has been checked, the dialog box reopens and a new property can be added.
11. Press the **Cancel** button when done.

## Common property types 

FreeCAD supports many property types. The table below lists some of the most common types. See [FeaturePython Custom Properties](FeaturePython_Custom_Properties.md) for more information.

++++
| Property type                    | Default unit (if any) | Remark                                                                                                               |
+==================================+=======================+======================================================================================================================+
|                   | ° (or deg)            |                                                                                                                      |
| {{Incode|App::PropertyAngle}}    |                       |                                                                                                                      |
|                               |                       |                                                                                                                      |
++++
|                   |                       |                                                                                                       |
| {{Incode|App::PropertyBool}}     |                       | `True`                                                                                                             |
|                               |                       |                                                                                                                   |
|                                  |                       | or `False`, can be used in [conditional expressions](Expressions#Conditional_expressions.md) |
++++
|                   | mm                    |                                                                                                                      |
| {{Incode|App::PropertyDistance}} |                       |                                                                                                                      |
|                               |                       |                                                                                                                      |
++++
|                   |                       | Decimal number                                                                                                       |
| {{Incode|App::PropertyFloat}}    |                       |                                                                                                                      |
|                               |                       |                                                                                                                      |
++++
|                   |                       | Whole number                                                                                                         |
| {{Incode|App::PropertyInteger}}  |                       |                                                                                                                      |
|                               |                       |                                                                                                                      |
++++
|                   | mm                    | Similar to {{Incode|App::PropertyDistance}} but cannot be negative                                     |
| {{Incode|App::PropertyLength}}   |                       |                                                                                                                      |
|                               |                       |                                                                                                                      |
++++
|                   |                       | Text string                                                                                                          |
| {{Incode|App::PropertyString}}   |                       |                                                                                                                      |
|                               |                       |                                                                                                                      |
++++

## Notes

-   Properties can also be added to existing VarSets in the [Expression editor](Expressions.md) by checking the **Show variable sets** checkbox.
-   A property can be removed from a VarSet via the [context menu](Property_editor#Context_menu.md) of the [Property editor](Property_editor.md).
-   A group name can be changed via the same menu.
-   The command currently cannot set the list of allowed items of an {{Incode|App::PropertyEnumeration}} property. This can be done via [Python code](FeaturePython_Custom_Properties#App:_PropertyEnumeration.md) or in the Property editor. The steps for the latter option are:
    1.  Select **Show hidden** in the context menu of the Property editor.
    2.  Expand the node of the property.
    3.  Click in the **Enum** field.
    4.  Press the **...** button that appears.
    5.  Enter values in the **List** dialog box that opens.
    6.  Press the **OK** button.

## Scripting


```python
import FreeCAD as App

doc = App.ActiveDocument

var_set = doc.addObject("App::VarSet", "VarSetName")
var_set.addProperty("App::PropertyInteger", "MyNumber")  # Property is added to the Base group.
var_set.MyNumber = 123
var_set.addProperty("App::PropertyString", "MyText", group="SomeGroup", doc="Some tooltip information")
var_set.MyText = "Abc"

doc.recompute()
```



---
⏵ [documentation index](../README.md) > Std VarSet/en
