---
 GuiCommand:
   Name: Sketcher ConstrainRadius
   Name/ru: Sketcher ConstrainRadius
   MenuLocation: Sketch , Ограничения эскиза , Ограничения радиуса
   Workbenches: Sketcher_Workbench
   SeeAlso: Sketcher_ConstrainDistance/ru, Sketcher_ConstrainDistanceX/ru, Sketcher_ConstrainDistanceY/ru
---

# Sketcher ConstrainRadius/ru


</div>



## Описание

The <img alt="" src=images/Sketcher_ConstrainRadius.svg  style="width:24px;"> [Sketcher ConstrainRadius](Sketcher_ConstrainRadius.md) tool fixes the radius of circles, arcs and [B-spline weight circles](Sketcher_CreateBSpline#Notes.md).

![](images/Sketcher_ConstrainRadius_example.png )



## Применение

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



## Программирование


```pythonSketch.addConstraint(Sketcher.Constraint('Radius', ArcOrCircle, App.Units.Quantity('123.0 mm')))```

The [Sketcher scripting](Sketcher_scripting.md) page explains the values which can be used for `ArcOrCircle`, and contains further examples on how to create constraints from Python scripts.


<div class="mw-translate-fuzzy">





</div>


{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainRadius/ru
