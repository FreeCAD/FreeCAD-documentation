---
- GuiCommand:
   Name:Part ElementCopy
   MenuLocation:Part → Create a copy → Create shape element copy
   Workbenches:[Part](Part_Workbench.md)
   Version:0.19
   SeeAlso:[Part SimpleCopy](Part_SimpleCopy.md), [Part TransformedCopy](Part_TransformedCopy.md), [Part RefineShape](Part_RefineShape.md)
---

## Description

[Part ElementCopy](Part_ElementCopy.md) produces a non-parametric copy of a sub-element of a particular object, that is, of a vertex, edge, or face.

To produce complete non-parametric copies of the objects use **<img src="images/Part_SimpleCopy.svg" width=16px> [Simple Copy](Part_SimpleCopy.md)
**, **<img src="images/Part_TransformedCopy.svg" width=16px>[Transformed Copy](Part_TransformedCopy.md)**, or **<img src="images/Part_RefineShape.svg" width=16px> [RefineShape](Part_RefineShape.md)**

## Usage

1.  Select a vertex, edge, or face of an object for which you wish to make a copy.
2.  Go to the menu {{MenuCommand|Part → Create a copy → <img src=images/Part_ElementCopy.svg style="width:16px"> [Create shape element copy](Part_ElementCopy.md)}}.

## Properties

### Data

The copy has a simple **Placement** property like any other [Part Feature](Part_Feature.md).

### View

The copy has simple view properties like any other [Part Feature](Part_Feature.md).

## Scripting

The **Part ElementCopy** command can be applied after selecting one or more objects in the [Tree view](Tree_view.md):


```python
FreeCADGui.runCommand('Part_ElementCopy')
```

The selection can be manual (by using the mouse), or via the [Python console](Python_console.md).
To know more about selecting objects programmatically, refer to [Selection methods](Selection_methods.md).





 
