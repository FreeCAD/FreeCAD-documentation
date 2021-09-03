---
- GuiCommand:/ro   Name:Part CreateSimpleCopy‏‎   Name/ro:Part CreateSimpleCopy‏‎   MenuLocation:Part → Create simple copy   Workbenches:[SeeAlso:[[Draft_Clone/ro   Clone](Part_Workbench/ro___Part]].md), [Copy](Std_Copy/ro.md), [Duplicate Selection](Std_DuplicateSelection/ro.md)|Icon:Tree_Part.svg---


</div>

## Introducere

Elimină istoricul piesei, astfel încât pașii diferiți pentru a crea piesa nu mai sunt accesibili / editabili de loc.


**![](images/)_[Part_SimpleCopy‎](Part_SimpleCopy‎.md)**

produces a copy that has no parametric history; the steps and operations needed to create it aren\'t accessible any more.


<div class="mw-translate-fuzzy">

With Simple copy only a non-parametric simple solid is produced, so if you want to change anything you have to go back to your creation file or history fix the issue then create a new simple solid.


</div>


<div class="mw-translate-fuzzy">

## Utilizare

Mark part of choice in the tree view and choose {{MenuCommand|Part → Create simple copy}}.


</div>

1.  Select an object for which you wish to make a copy.
2.  Go to the menu {{MenuCommand|Part → Create a copy → ![](images/)_[Create_simple_copy](Part_SimpleCopy.md)}}.

## Properties

### Data

The copy has a simple **Placement** property like any other [Part Feature](Part_Feature.md).

### View

The copy has simple view properties like any other [Part Feature](Part_Feature.md).

## Scripting

The **Part SimpleCopy**‎ command can be applied after selecting one or more objects in the [Tree view](Tree_view.md):


```python
FreeCADGui.runCommand('Part_SimpleCopy')
```

The selection can be manual (by using the mouse), or via the [Python console](Python_console.md).
To know more about selecting objects programmatically, refer to [Selection methods](Selection_methods.md).





  
