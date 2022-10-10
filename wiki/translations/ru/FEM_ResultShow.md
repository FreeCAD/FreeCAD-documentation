---
- GuiCommand   */ru
   Name   *FEM ResultShow
   Name/ru   *FEM ShowResult
   MenuLocation   *Results → Показать результаты
   Workbenches   *[FEM](FEM_Workbench/ru.md)
   Shortcut   ***S** **R**
   SeeAlso   *[FEM tutorial](FEM_tutorial/ru.md)
---

# FEM ResultShow/ru


</div>

## Описание

FEM ResultShow opens the dialog for a FEM results object. A result object is automatically created when a FEM analysis was performed using either the solver [Calculix](FEM_SolverCalculixCxxtools.md) or [Z88](FEM_SolverZ88.md).

A result objects holds the resulting mesh and allows to visualize results. It is designed and therefore limited to thermomechanical results. For these result types the result object can be used as alternative to a [result pipeline](FEM_PostPipelineFromResult.md). A result pipeline can be used to visualize any kind of results (also electrical etc.).

The units used for the result object are those of the set [unit system](Preferences_Editor#Units.md) while for a result pipelines the units are [SI](https   *//en.wikipedia.org/wiki/International_System_of_Units).

The visualization of the results is only active when the dialog is open. However, the dialog settings are stored in the FreeCAD model file.

## Применение

To show the result dialog, select the result object in the [Tree view](Tree_view.md), then either press the toolbar button **<img src="images/FEM_ResultShow.svg" width=16px> '''Show result'''** or use the menu **Results → <img src="images/FEM_ResultShow.svg" width=16px> Show result** (sortcut **R** then **S**). Alternatively you can also double-click on the result object in the tree view.

When the dialog is open, the result mesh will automatically be shown.

[left\|framed](File   *FEM_Result-Object-Dialog.png.md)

The dialog is shown at the left and offers the following features   *

-   Select a result type and the minimum and maximum will be displayed in the dialog. The result mesh will be colored accordingly.

-   Click on the button **'''Histogram'''** to get a histogram what amount of result mesh nodes have a certain result. The histogram plot can be modified by the buttons in its toolbar. it is also possible to save the histogram as image using the save button from its toolbar.

-   Check the option **Show** to enables the slider and to visualize the result mesh deformation. The slider value is a factor with which the result *Displacement Magnitude* is multiplied.**Note**   * The slider only affects the Displacement Magnitude, not its X, Y, Z components.

-   With the button After you input an equation press the button and the result will be shown in the fields displaying the minimum and maximum. The result mesh will be colored accordingly.**Note**   * The calculation results always have the unit MPa, mm or T, no matter what [unit system](Preferences_Editor#Units.md) you use.





{{FEM Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ResultShow/ru
