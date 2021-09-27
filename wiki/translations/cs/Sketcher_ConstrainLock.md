# Sketcher ConstrainLock/cs
---
- GuiCommand:/cs   Name:Sketcher ConstrainLock   Name/cs:Sketcher ConstrainLock   Workbenches:_---


</div>


<div class="mw-translate-fuzzy">

\"Vytvoření zámku na vybrané položce\"

## Popis

Tento nástroj se pokusí plně ustavit jakoukoliv vybranou položku.


</div>

**Constraint Lock** applies **<img src=images/Sketcher_ConstrainDistanceX.svg style="width:16px"> <img src=images/Sketcher_ConstrainDistanceY.svg style="width:Horizontal distance](Sketcher_ConstrainDistanceX.md)** and **[16px"> [Vertical distance](Sketcher_ConstrainDistanceY.md)** constraints to selected vertices (points) in the sketch. If a single vertex is selected, the horizontal and vertical distance constraints will refer to the sketch origin point. If two or more points are selected, horizontal and vertical distance constraints will be added for each pair of points. There is no automatic prompt to edit the constraints\' values, they must be edited manually.


<div class="mw-translate-fuzzy">

Díky tomu, že FreeCAD je stále ještě ve vývoji - tento nástroj předvádí podivné chování, když se pokouší \'zamknout\' cokoliv jiného než bod. Například (jako ve V0.12 R4802), když uzamknete kružnici její obvodovou čárou a ne jejím středovým bodem, zobrazí se v dialogovém okně horizontální i vertikální vazební hodnoty, ale jsou nastaveny na nulu a nezobrazí se v grafickém okně.

## Postup

1.  Nejdříve je nutné vysvítit položku, kterou chcete uzamknout. Z důvodů uvedených výše je rozumné vysvítit pouze bod.
    <img alt="" src=images/LockConstraint1.png  style="width:256px;">
2.  Vysvícení nakreselené položky je dosaženo posunutím myši nad položku a kliknutím na levé tlačítko myši. Vysvícená položka změní barvu na zelenou.
    <img alt="" src=images/LockConstraint2.png  style="width:256px;">
3.  Jakmile je položka vysvícena, kliknutím levým tlačítkem myši na vazbu uzamknout uzamčete položku na jejím místě. Obyčejně je to představováno jako dvě vazby: horizontální vzdálenost od počátku a vertikální vzdálenost od počátku. Tyto vzdálenosti jsou obecně nastaveny na aktuální koordináty bodu.
    <img alt="" src=images/LockConstraint3.png  style="width:256px;">
4.  Vertikální a horizontální vazba, které určují zámek mohou být editovány buď dvojklikem na příslušnou vazbu v náčrtu nebo v záložce vazeb rozbalovacího panelu pohledu. To otevře dialogové okno pro editaci vazeb. Kliknutí na horizontální vazbu vyvolá:
    <img alt="" src=images/LockConstraint4.png  style="width:256px;">.
5.  Zadejte požadovanou hodnotu v dialogovém okně a klikněte na OK.
    <img alt="" src=images/LockConstraint5.png  style="width:256px;">
6.  Nová hodnota vazby je ihned aplikována výkres.
    <img alt="" src=images/LockConstraint6.png  style="width:256px;">
7.  Podobně může být editována i vertikální vazba pro ustavení bodu na požadovaném místě.
    <img alt="" src=images/LockConstraint7.png  style="width:256px;">


</div>

1.  Select one or more vertices (points) in the sketch.
2.  Press the **<img src=images/Sketcher_ConstrainLock.svg style="width:16px"> [Constrain lock](Sketcher_ConstrainLock.md)** button.
3.  To edit the constraints values, double-click on a constraint value in the 3D view, or double-click on the constraint or right-click and select **Edit value** in the Constraint list in the Tasks tab.

**Note:** the constraint tool can also be started with no prior selection, but it will then only work on a single vertex, and reference the constraints to the sketch origin point. By default the command will be in continue mode to create new constraints; press the right mouse button or **ESC** once to quit the command.

## Scripting

The <img alt="" src=images/Sketcher_ConstrainLock.svg  style="width:24px;"> _ and a <img alt="" src=images/Sketcher_ConstrainDistanceY.svg  style="width:24px;"> [Vertical distance](Sketcher_ConstrainDistanceY.md) constraint, it is not a constraint of its own. See the [Sketcher scripting](Sketcher_scripting.md) page for details and examples on how to create these constraints from Python scripts.





{{Sketcher Tools navi

}}

---
[documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainLock/cs
