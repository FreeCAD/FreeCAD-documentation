---
- GuiCommand:
   Name:Part XOR
   MenuLocation:Part → Split → Boolean XOR
   Workbenches:[Part](Part_Workbench.md)
   Version:0.17
   SeeAlso:[Part Boolean Fragments](Part_BooleanFragments.md), [Part Slice](Part_Slice.md), [Part Join features](Part_CompJoinFeatures.md), [Part Boolean](Part_Boolean.md)
---

# Part XOR

## Description

The command <img alt="" src=images/Part_XOR.svg  style="width:24px;"> **Part XOR** removes geometry shared by an even number of objects and leaves a void space between the involved objects. (For two objects it represents a symmetric version of <img alt="" src=images/Part_Cut.svg  style="width:24px;"> [Cut](Part_Cut.md)).

 <img alt="" src=images/Part_XOR-01.png  style="width:300px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Part_XOR-02.png  style="width:300px;"> 



*Three overlapping objects -> Result object*

Void spaces are hard to detect if the cover faces are not coplanar.

## Usage

1.  Select two or more objects.
2.  There are several ways to invoke the command:
    -   Select the **Part → Boolean → <img src="images/Part_XOR.svg" width=16px> Boolean XOR** option from the menu.
    -   Press the **<img src="images/Part_XOR.svg" width=16px> [Boolean XOR](part_XOR.md)** button.

## Properties

==<Example:==>

## Scripting



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part XOR
