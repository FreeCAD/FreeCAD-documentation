---
- GuiCommand:/ru
   Name/ru:Управление решателем
   Name:FEM_SolverControl
   MenuLocation:Решить → Управление решателем
   Workbenches:[FEM](FEM_Workbench/ru.md)
   Shortcut:**S** **T**
   SeeAlso:[Запустить решатель](FEM_SolverRun/ru.md)
---

# FEM SolverControl/ru

## Описание

This command is used to control the FEM solver (write the input file, edit it, and trigger the solver).

## Применение

1.  Select the Solver object in the [Tree view](Tree_view.md), e.g., for CalcuilX solver <img alt="" src=images/FEM_SolverCalculixCxxtools.svg  style="width:24px;"> **SolverCcxTools**.
2.  There are several ways to invoke the command:
    -   Press the **<img src="images/FEM_SolverControl.svg" width=16px> [Solver job control](FEM_SolverControl.md)** button.
    -   Select the **Solve → <img src="images/FEM_SolverControl.svg" width=16px> Solver job control** option from the menu.
    -   Use the keyboard shortcut: **S** then **T**.
3.  Optionally, edit working directory.
4.  Optionally, select analysis type.
5.  Click **Write .inp file** to write the input file.
6.  Optionally, click **Edit .inp file**.
    -   Input file will open so you can edit it and save by **Ctrl**+**S**.
7.  Click **Run CalculiX** to trigger the solver.
    -   The solution may take considerable time for large models.

## Notes

-   Default working directory can be changed in **Edit → Preferences → FEM**
-   Controls for other solvers may differ.
-   The simplified version of the command is <img alt="" src=images/FEM_SolverRun.svg  style="width:24px;"> [Run solver calculation](FEM_SolverRun.md).





{{FEM Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM SolverControl/ru
