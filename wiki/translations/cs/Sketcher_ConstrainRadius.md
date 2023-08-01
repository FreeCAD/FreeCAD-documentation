# Sketcher ConstrainRadius/cs
---
- GuiCommand:   Name: Constraint Radius   Name/cs: Constraint Radius   Workbenches: [Návrh dílu](Sketcher_Workbench/cs___Náčrt]],_[[PartDesign_Workbench/cs.md)|MenuLocation: Sketch - Sketcher constraints - Constrain radius   SeeAlso: [Vazba délky](Sketcher_ConstrainDistance/cs.md), [Vazba vodorovnosti](Sketcher_ConstrainDistanceX/cs.md), [Vazba svislosti](Sketcher_ConstrainDistanceY/cs.md)---


</div>




<div class="mw-translate-fuzzy">

#### Popis

Tato vazba nastavuje hodnotu poloměru kružnice nebo oblouku na zadanou hodnotu. Najednou může být nastavena hodnota pouze pro jednu kružnici nebo jeden obklouk.


</div>

This constraint constrains the value of the radius of a circle or arc to have a specific value. If more than one circle or arc is selected before launching the command :

-   If the constrain is applied in \'Reference\' mode, a new reference constrain is added to each object separately according above rules
-   If the constrain is applied in \'Normal\' (driving) mode, following rules are applied
    -   A reference constrain is applied separately on each object which is an external geometry

    -   
        **[<img src=images/Sketcher_ConstrainEqual.svg style="width:16px"> [Equal constrains](Sketcher_ConstrainEqual.md)**
        
        are applied sequentially between all real/construction geometry objects and a dimensional constrain is applied to the first selected object according above rules

NB : B-spline poles can\'t be mixed with other object type in the selection

![](images/Sketcher_ConstrainRadius_example.png )




<div class="mw-translate-fuzzy">

#### Postup

<img alt="" src=images/ConstrainRadius1.png  style="width:256px;">
Kliknutím vyberte oblouk nebo kružnici v náčrtu ( vybraná položka bude mít tmavězelenou barvu).
<img alt="" src=images/ConstrainRadius2.png  style="width:256px;">
Aplikujte vazbu kliknutím na ikonu vazby poloměru <img alt="" src=images/Constraint_Radius.png  style="width:16px;"> v nástrojovém pruhu Náčrtu nebo výběrem položky Vazba poloměru v submenu Vazby náčrtu v menu Náčrtu (nebo Návrhu dílu, závisí ve které pracovní ploše jste - Náčrt nebo Navrh dílu).
<img alt="" src=images/ConstrainRadius3.png  style="width:256px;">
Poloměr je zafixován na aktuální hodnotu poloměru.
Hodnotu nastavení změníte buď dvojklikem na vazbu ve 3D zobrazení (změna barvy na červenou indikuje, že vazba je vybrána) nebo dvojklikem na vazbu v panelu vazeb záložky Nástroje v rozbalovacím pohledu.
Tím zobrazíte vyskakovací dialogové okno.
<img alt="" src=images/ConstrainRadius4.png  style="width:256px;">
Zadáte požadovanou hodnotu poloměru do dialogového okna a kliknete na OK a tak nastavíte hodnotu vazby.
<img alt="" src=images/ConstrainRadius5.png  style="width:256px;">
Vazba je nastavena na hodnotu zadanou v dialogovém okně.
D zobrazení


</div>

1.  Pick one or more circles or arcs.
2.  Press the **[<img src=images/Sketcher_ConstrainRadius.svg style="width:16px"> [Constrain radius](Sketcher_ConstrainRadius.md)** button.
3.  A pop up dialog opens to edit or confirm the value. Press **OK** to validate. In case multiple circles/arcs were selected, all constraints will adopt this value. Edit their separate values by double-clicking on the dimension label in the 3D view; or in the Constraints list, double-click on the constraint or right-click and select **Change value**.
4.  Optionally the dimension label and line can be moved and rotated in the 3D view by clicking on the value and dragging while keeping the left mouse button pressed.

**Note:** the constraint tool can also be started with no prior selection. By default the command will be in continue mode to create new constraints; press the right mouse button or **Esc** once to quit the command.

## Scripting


```pythonSketch.addConstraint(Sketcher.Constraint('Radius', ArcOrCircle, App.Units.Quantity('123.0 mm')))```

The [Sketcher scripting](Sketcher_scripting.md) page explains the values which can be used for `ArcOrCircle`, and contains further examples on how to create constraints from Python scripts.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainRadius/cs
