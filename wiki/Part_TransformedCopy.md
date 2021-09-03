---
- GuiCommand:
   Name:Part TransformedCopy
   MenuLocation:Part → Create a copy → Create transformed copy
   Workbenches:[Part](Part_Workbench.md)
   Version:0.19
   SeeAlso:[Part SimpleCopy](Part_SimpleCopy.md), [Part ElementCopy](Part_ElementCopy.md), [Part RefineShape](Part_RefineShape.md)
---

## Description

[Part TransformedCopy](Part_TransformedCopy.md) produces a non-parametric copy of an object that has been displaced from its original position.

To produce other non-parametric copies use **<img src="images/Part_SimpleCopy.svg" width=16px> [Simple Copy](Part_SimpleCopy.md)
**, **<img src="images/Part_ElementCopy.svg" width=16px>[ElementCopy](Part_ElementCopy.md)**, or **<img src="images/Part_RefineShape.svg" width=16px> [RefineShape](Part_RefineShape.md)**

## Usage

1.  Select an object that you wish to copy.
2.  Go to the menu {{MenuCommand|Part → Create a copy → <img src=images/Part_TransformedCopy.svg style="width:16px"> [Create transformed copy](Part_TransformedCopy.md)}}.

## Properties

### Data

The copy has a simple **Placement** property like any other [Part Feature](Part_Feature.md).

### View

The copy has simple view properties like any other [Part Feature](Part_Feature.md).

## Scripting

The **Part TransformedCopy** command can be applied after selecting one or more objects in the [Tree view](Tree_view.md):

 
```python
FreeCADGui.runCommand('Part_TransformedCopy')
```

The selection can be manual (by using the mouse), or via the [Python console](Python_console.md).
To know more about selecting objects programmatically, refer to [Selection methods](Selection_methods.md).




  
