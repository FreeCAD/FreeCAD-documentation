---
- GuiCommand:
   Name:FEM Analysis
   MenuLocation:Model → Analysis container‏‎
   Workbenches:[FEM](FEM_Workbench.md)
   Shortcut:**S** **A**
   SeeAlso:[FEM tutorial](FEM_tutorial.md)
---

# FEM Analysis/en

## Description

The FEM Analysis could be seen as a Container that holds all objects of a Finite Element Analysis. It is mandatory to have a analysis container which holds all the needed objects. At least one of the following objects is needed for a mechanical analysis:

-   [material](FEM_MaterialSolid.md)
-   [fixed constraint](FEM_ConstraintFixed.md)
-   [force constraint](FEM_ConstraintForce.md) or [pressure constraint](FEM_ConstraintPressure.md)

## Usage

1.  There are several ways to invoke the command:
    -   Press the **<img src="images/FEM_Analysis.svg" width=16px> [FEM Analysis](FEM_Analysis.md)** button.
    -   Select the **Model → <img src="images/FEM_Analysis.svg" width=16px> Analysis container‏‎** option from the menu.
    -   Use the keyboard shortcut: **S** then **A**.
2.  A new Analysis is created and set to active.
3.  Other objects could be added or removed to the analysis container by drag and drop.
4.  To add new FEM Objects to the document the analysis has to be active. Double click on the analysis does activate the analysis.

## Options

-   Up to date there is no option to choose.
-   A frequency analysis in in development. See [1](http://forum.freecadweb.org/viewtopic.php?f=18&t=12189) for more informations.

## Properties

-    **OutpuDir**: Specifies the working directory of the analysis

## Scripting

most code here is depreciated in 0.17.

-   new analysis


```python
MechanicalAnalysis.makeMechanicalAnalysis( name )
```

-   add object to the analysis


```python
App.ActiveDocument.MechanicalAnalysis.Member = App.ActiveDocument.MechanicalAnalysis.Member + [ (object) ]
```

-   remove object from the analysis


```python
member = App.ActiveDocument.MechanicalAnalysis.Member
member.remove( documentobject )
 App.ActiveDocument.MechanicalAnalysis.Member = member
```

Examples: 
```python
import MechanicalAnalysis
analysis = MechanicalAnalysis.makeMechanicalAnalysis("MechanicalAnalysis")
FemGui.setActiveAnalysis(analysis)

addobj = App.ActiveDocument.getObject("MechanicalMaterial")
App.ActiveDocument.MechanicalAnalysis.Member = App.ActiveDocument.MechanicalAnalysis.Member + [addobj]

removeobj = App.ActiveDocument.getObject("MechanicalMaterial")
member = App.ActiveDocument.MechanicalAnalysis.Member
member.remove(removeobj)
App.ActiveDocument.MechanicalAnalysis.Member = member
```





{{FEM Tools navi

}}

---
[documentation index](../README.md) > FEM Analysis/en
