---
- GuiCommand:
   Name:PartDesign WizardShaft
   Name/ru:PartDesign WizardShaft
   MenuLocation:Part Design → Shaft design wizard...
   Workbenches:[PartDesign](PartDesign_Workbench/ru.md), Complete
---

# PartDesign WizardShaft/ru


</div>



## Описание


<div class="mw-translate-fuzzy">

Данный инструмент позволяет создать вал на основе значений таблицы, также проводить анализ силы и моментов. Мастер можно запустить через меню **Part Design → [<img src=images/PartDesign_WizardShaft.svg style="width:20px"> Мастер проектирования вала...**.


</div>

## Usage

You can start the wizard from the Part Design menu **Part Design → [<img src=images/PartDesign_WizardShaft.svg style="width:20px"> Shaft design wizard...**.

Запущенный Мастер отобразит таблицу с значениями по умолчанию, соответствующую деталь вала и графики сил/моментов.

<img alt="" src=images/WizardShaft_Part.jpg  style="width:780px;">

The top of the window is taken up by the table. It is organized into numbered columns which correspond to segments of the shaft. A shaft segment is characterized by having certain length and diameter. The main window shows two tabs. One is the shaft part itself (a revolution feature), shown in the image above. The second tab shows graphs of the shear forces and moments created by the loads defined in the table.

<img alt="" src=images/shaftwizard1.jpg  style="width:1024px;">

## Prerequisites

The shaft design wizard depends on the [matplotlib](http://matplotlib.org/) library to create and display the graphs of shear force and bending moment. On Debian/Ubuntu-based systems, it is available through the python-matplotlib package.



## Параметры

For each shaft segment, the following parameters can be defined

-   Length of the segment
-   Diameter of the segment
-   Load type. Note that you have to click on the desired entry in the menu after scrolling to it, otherwise it will not be selected!
    -   None: No load
    -   Fixed: The end of the shaft is fixed (e.g. welded to another part). This load type can only be defined for the first or last segment.
    -   Static: There is a static load on this shaft segment
-   Load on the shaft segment
-   Location where the load is applied to the segment. The location is counted from the left-hand edge of the segment

(Other rows and load types exist but no functionality has been implemented yet)



## Меню

Чтобы добавить новый сегмент вала, щелкните правой кнопкой мыши на пустом месте справа от таблицы и выберите \"Добавить столбец\".



## Ограничения

-   Невозможно создавать соседние сегменты вала с одинаковым диаметром.



## Планируемая функциональность 

-   Table-driven chamfers and rounds on the shaft edges
-   Recognize a previously created shaft wizard part and initialize the table values from it
-   Shaft stress calculation
-   Visualization of loads on the shaft (can use the same functionality as for FEM module)
-   Definition of loads as a Document Object (can use the same functionality as for FEM module)
-   Material database
-   Allow loads in the Z-direction as well as in Y-direction (requires definition of loads as a Document Object, otherwise the table will become very long)





{{PartDesign Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign WizardShaft/ru
