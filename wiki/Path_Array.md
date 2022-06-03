---
- GuiCommand   *
   Name   *Path Array
   MenuLocation   *Path → Path Modification → Array
   Workbenches   *[Path](Path_Workbench.md)
---

# Path Array

## Description

This tool creates a new path by duplicating another path several times at a certain interval distance.

## Usage

1.  Select the operation you want to repeat
2.  Press the **<img src="images/Path_Array.svg" width=24px> [Array](Path_Array.md)** button
3.  Press **Apply**
4.  Adjust the desired properties at the data box

## Properties

-    **Type**   * The type array (polar, linear one ore two directions)

-    **Offset**   * The spacing between the array copies for each direction

-    **Copies**   * The number of copies (not counting the original) for each direction

## Limitations

This feature only works on actual path operations, not on derivative paths produced by Path Dressups. In that case the Array icon is disabled.

## Scripting


**See also   ***

[FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

Example   *

 
```python
#Place code example here.
```




 {{Path_Tools_navi}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Path](Path_Workbench.md) > Path Array
