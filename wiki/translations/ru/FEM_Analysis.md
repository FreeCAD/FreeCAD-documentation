---
 GuiCommand:
   Name: FEM Analysis
   Name/ru: FEM Analysis
   MenuLocation: Model , Блок анализа
   Workbenches: FEM_Workbench/ru
   Shortcut: **N** **A**
   SeeAlso: FEM_tutorial/ru
---

# FEM Analysis/ru


</div>



## Описание

The FEM Analysis could be seen as a container that holds all objects of a Finite Element Analysis. It is mandatory to have an analysis container that holds all the needed objects. At least one of the following objects (apart from the mesh) is necessary for a mechanical analysis:

-   [solid material](FEM_MaterialSolid.md),
-   [fixed boundary condition](FEM_ConstraintFixed.md) or [displacement boundary condition](FEM_ConstraintDisplacement.md) or [rigid body constraint](FEM_ConstraintRigidBody.md).



## Применение

1.  There are several ways to invoke the command:
    -   Press the **<img src="images/FEM_Analysis.svg" width=16px> [Analysis container](FEM_Analysis.md)** button.
    -   Select the **Model → <img src="images/FEM_Analysis.svg" width=16px> Analysis container‏‎** option from the menu.
    -   Use the keyboard shortcut: **S** then **A**.
2.  A new Analysis is created and set to active.
3.  Other objects could be added or removed from the analysis container by drag and drop.
4.  To add new FEM objects to the document the analysis has to be active. Double-clicking on the analysis container activates the analysis.



## Опции

-   Up to date there is no option to choose.



## Свойства

-    **OutpuDir**: Specifies the working directory of the analysis



## Программирование

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

Примеры: 
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
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM Analysis/ru
