# Sketcher ConstrainRadius/cs
---
 GuiCommand:   Name: Constraint Radius   Name/cs: Constraint Radius   Workbenches: Sketcher Workbench/cs   Náčrt, PartDesign Workbench/cs, Sketcher ConstrainDistanceX/cs, Sketcher ConstrainDistanceY/cs---


</div>




<div class="mw-translate-fuzzy">

#### Popis

Tato vazba nastavuje hodnotu poloměru kružnice nebo oblouku na zadanou hodnotu. Najednou může být nastavena hodnota pouze pro jednu kružnici nebo jeden obklouk.


</div>

The <img alt="" src=images/Sketcher_ConstrainRadius.svg  style="width:24px;"> [Sketcher ConstrainRadius](Sketcher_ConstrainRadius.md) tool fixes the radius of circles, arcs and [B-spline weight circles](Sketcher_CreateBSpline#Notes.md).

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

See also: [Drawing aids](Sketcher_Workbench#Drawing_aids.md).

### [Continue mode](Sketcher_Workbench#Continue_modes.md) 

1.  Make sure there is no selection.
2.  There are several ways to invoke the tool:
    -   
        <small>(v1.0)</small> 
        
        : If the **Dimensioning constraints** [preference](Sketcher_Preferences#General.md) is set to {{Value|Single tool}} (default): press the down arrow to the right of the **<img src="images/Sketcher_Dimension.svg" width=|x16px><img src="images/Toolbar_flyout_arrow.svg" width=x16px>** button and select the **<img src="images/Sketcher_ConstrainRadius.svg" width=16px> Constrain radius** option from the dropdown.

    -   If this preference has a different value (and in {{VersionMinus|0.21}}): press the **<img src="images/Sketcher_ConstrainRadius.svg" width=16px> [Constrain radius](Sketcher_ConstrainRadius.md)** button.

    -   Select the **Sketch → Sketcher constraints → <img src="images/Sketcher_ConstrainRadius.svg" width=16px> Constrain radius** option from the menu.

    -   
        <small>(v1.0)</small> 
        
        : Right-click in the [3D view](3D_view.md) and select the **Dimension → <img src="images/Sketcher_ConstrainRadius.svg" width=16px> Constrain radius** option from the context menu.

    -   Use the keyboard shortcut: **K** then **R**.
3.  For further steps see [Sketcher ConstrainRadiam](Sketcher_ConstrainRadiam#Continue_mode.md).

### Run-once mode 

See [Sketcher ConstrainRadiam](Sketcher_ConstrainRadiam#Run-once_mode.md).

## Scripting


```pythonSketch.addConstraint(Sketcher.Constraint('Radius', ArcOrCircle, App.Units.Quantity('123.0 mm')))```

The [Sketcher scripting](Sketcher_scripting.md) page explains the values which can be used for `ArcOrCircle`, and contains further examples on how to create constraints from Python scripts.



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainRadius/cs
