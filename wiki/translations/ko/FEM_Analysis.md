---
 GuiCommand:
   Name: FEM Analysis
   MenuLocation: Model , Analysis container‏‎
   Workbenches: FEM_Workbench
   Shortcut: **S** **A**
   SeeAlso: FEM_tutorial
---

# FEM Analysis/ko

## Description

The FEM Analysis could be seen as a Container that holds all objects of a Finite Element Analysis. It is mandatory to have an analysis container which holds all the needed objects. At least one of the following objects is necessary for a mechanical analysis:

-   [solid material](FEM_MaterialSolid.md)
-   [fixed boundary condition](FEM_ConstraintFixed.md) or [displacement boundary condition](FEM_ConstraintDisplacement.md)

## Usage

1.  There are several ways to invoke the command:
    -   Press the **<img src="images/FEM_Analysis.svg" width=16px> [Analysis container](FEM_Analysis.md)** button.
    -   Select the **Model → <img src="images/FEM_Analysis.svg" width=16px> Analysis container‏‎** option from the menu.
    -   Use the keyboard shortcut: **S** then **A**.
2.  A new Analysis is created and set to active.
3.  Other objects could be added or removed to the analysis container by drag and drop.
4.  To add new FEM Objects to the document the analysis has to be active. Double click on the analysis does activate the analysis.

## Options

-   Up to date there is no option to choose.

## Properties

-    **OutpuDir**: Specifies the working directory of the analysis

## Scripting

most code here is deprecated in 0.17.

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
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM Analysis/ko
