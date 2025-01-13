---
 GuiCommand:
   Name: Sketcher ConstrainLock
   Name/cs: Sketcher ConstrainLock
   Workbenches: Sketcher Workbench/cs, PartDesign Workbench/cs
   MenuLocation: Sketch , Sketcher constraints , Constrain lock
   SeeAlso: Sketcher_ConstrainBlock/cs
---

# Sketcher ConstrainLock/cs


</div>




<div class="mw-translate-fuzzy">

\"Vytvoření zámku na vybrané položce\"

## Popis

Tento nástroj se pokusí plně ustavit jakoukoliv vybranou položku.


</div>

The <img alt="" src=images/Sketcher_ConstrainLock.svg  style="width:24px;"> [Sketcher ConstrainLock](Sketcher_ConstrainLock.md) tool applies [Horizontal distance](Sketcher_ConstrainDistanceX.md) and [Vertical distance](Sketcher_ConstrainDistanceY.md) constraints to points. If a single point is selected the constraints reference the origin of the sketch. If two or more points are selected the constraints reference the last point in the selection.




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

See also: [Drawing aids](Sketcher_Workbench#Drawing_aids.md).

### [Continue mode](Sketcher_Workbench#Continue_modes.md) 

1.  Make sure there is no selection.
2.  There are several ways to invoke the tool:
    -   
        <small>(v1.0)</small> 
        
        : If the **Dimensioning constraints** [preference](Sketcher_Preferences#General.md) is set to {{Value|Single tool}} (default): press the down arrow to the right of the **<img src="images/Sketcher_Dimension.svg" width=|x16px><img src="images/Toolbar_flyout_arrow.svg" width=x16px>** button and select the **<img src="images/Sketcher_ConstrainLock.svg" width=16px> Constrain lock** option from the dropdown.

    -   If this preference has a different value (and in {{VersionMinus|0.21}}): press the **<img src="images/Sketcher_ConstrainLock.svg" width=16px> [Constrain lock](Sketcher_ConstrainLock.md)** button.

    -   Select the **Sketch → Sketcher constraints → <img src="images/Sketcher_ConstrainLock.svg" width=16px> Constrain lock** option from the menu.

    -   
        <small>(v1.0)</small> 
        
        : Right-click in the [3D view](3D_view.md) and select the **Dimension → <img src="images/Sketcher_ConstrainLock.svg" width=16px> Constrain lock** option from the context menu.

    -   Use the keyboard shortcut: **K** then **L**.
3.  The cursor changes to a cross with the tool icon.
4.  Select a single point.
5.  Two constraints are added.
6.  Optionally keep creating constraints.
7.  To finish, right-click or press **Esc**, or start another geometry or constraint creation tool.

### Run-once mode 

1.  Select one or more points.
2.  Invoke the tool as explained above.
3.  Depending on the selection two or more constraints are added.

## Notes

-   There is no automatic prompt to edit the constraint values. If required values can be [edited manually](Sketcher_Workbench#Edit_constraints.md).





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainLock/cs
