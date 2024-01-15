---
 GuiCommand:
   Name: FEM ConstraintFlowVelocity
   Name/ru: FEM ConstraintFlowVelocity
   Icon: Fem-constraint-flow-velocity.svg
   MenuLocation:  Model , Fluid constraints , Constraint flow velocity
   Workbenches: FEM_Workbench/ru
   Shortcut: 
   SeeAlso: FEM_tutorial/ru
---

# FEM ConstraintFlowVelocity/ru


</div>



## Описание

Устанавливает скорость потока в качестве граничного условия к ребру в 2D или к грани в 3D.



## Применение

1.  Press the **<img src="images/FEM_ConstraintFlowVelocity.svg" width=16px> [Flow velocity boundary condition](FEM_ConstraintFlowVelocity.md)** button or select the menu **Model → Fluid boundary conditions → <img src="images/FEM_ConstraintFlowVelocity.svg" width=16px> Flow velocity boundary condition**.
2.  Select the target Edges or Faces.
3.  Press the **Add** button.
4.  Uncheck *Unspecified* to activate the necessary fields for edition.
5.  Set the velocity values or (<small>(v0.21)</small> ) specify a formula.

## Formulas


<small>(v0.21)</small> 

It is possible to define a velocity by specifying the velocity profile as formula. In this case the solver sets the velocities at the different positions according to the profile.

To specify for example the velocity profile

$\quad
v_{x} (y)=6\left(y-1\right)\left(2-y\right)$

for $y\in[1;2]$ (assuming that e.g. a pipe has the wall at y = 1 m and y = 2 m)

enter this to the *Formula* field: ` Variable Coordinate 2; Real MATC "6*(tx-1)*(2-tx)"`

This code has the following syntax:

-   the prefix *Variable* specifies that the velocity is not a constant but a variable
-   the variable to calculate the velocity is *Coordinate 2*, meaning y
-   the velocity values are returned as *Real* (floating point value)
-   *MATC* is the prefix for the Elmer solver that the following code is a formula
-   *tx* is always the name of the variable in *MATC* formulas, no matter that *tx* in our case is actually *y*

That *y* will only be in the range $y\in[1;2]$ is set because *MATC* only evaluates the *tx* range where the result is positive. This behavior is a bit special but has the advantage that one does not need to specify the range manually.

It is also possible to use more than one variable. See as example the definition of rotations in the [displacement constraint](FEM_ConstraintDisplacement#Rotations.md).



## Примечания


<div class="mw-translate-fuzzy">

-   Компоненты вектора, отмеченные как *не указана*, будут интерполированы выбранным решателем.

    :   Любой вектор, который должен быть результатом решателя, должен быть помечен как *не указана*.
-   Если целевая грань или ребро не выровнены с основной декартовой системой координат, можно поставить галочку *нормаль к границе*.

    :   Если установлен флажок *нормаль к границе*, вектор нормали к выбранному ребру или грани равен X, и он будет ориентирован от области сетки.
    :   Например, если в домен должен поступать поток воздуха со скоростью 20 мм/с, то после отметки *нормаль к границе* пользователь должен будет ввести -20 мм/с в поле *скорость X*.


</div>

-   For a wall with non-slip condition, set all velocity components to 0.
-   For a symmetry condition, set the the flow to (0, Unspecified, Unspecified) if **Normal to boundary** is checked.


<div class="mw-translate-fuzzy">





</div>


{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ConstraintFlowVelocity/ru
