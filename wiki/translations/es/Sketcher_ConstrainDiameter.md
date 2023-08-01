---
- GuiCommand:
   Name:Sketcher ConstrainDiameter
   Name/es:Croquizador RestringirDiámetro
   Workbenches:[Sketcher](Sketcher_Workbench/es.md)
   MenuLocation:Boceto → Croquizador restricciónes → RestringirDiámetro
   SeeAlso:[Restringir la distancia](Sketcher_ConstrainDistance/es.md), [Restringir distancia horizontal](Sketcher_ConstrainDistanceX/es.md), [Restringir distancia vertical](Sketcher_ConstrainDistanceY/es.md)
---

# Sketcher ConstrainDiameter/es


</div>



## Descripción

This constraint constrains the value of the diameter of a circle or arc to have a specific value. If more than one circle or arc is selected before launching the command :

-   If the constrain is applied in \'Reference\' mode, a new reference constrain is added to each object separately according above rules
-   If the constrain is applied in \'Normal\' (driving) mode, following rules are applied
    -   A reference constrain is applied separately on each object which is an external geometry

    -   
        **[<img src=images/Sketcher_ConstrainEqual.svg style="width:16px"> [Equal constrains](Sketcher_ConstrainEqual.md)**
        
        are applied sequentially between all real/construction geometry objects and a dimensional constrain is applied to the first selected object according above rules

NB : B-spline poles can\'t be mixed with other object type in the selection




<div class="mw-translate-fuzzy">

## Como utilizar 


</div>

1.  Pick one or more circles or arcs.
2.  Press the **[<img src=images/Sketcher_ConstrainDiameter.svg style="width:16px"> [Constrain diameter](Sketcher_ConstrainDiameter.md)** button.
3.  A pop up dialog opens to edit or confirm the value. Press **OK** to validate. In case multiple circles/arcs were selected, all constraints will adopt this value. Edit their separate values by double-clicking on the dimension label in the 3D view; or in the Constraints list, double-click on the constraint or right-click and select **Change value**.
4.  Optionally the dimension label and line can be moved and rotated in the 3D view by clicking on the value and dragging while keeping the left mouse button pressed.

**Note:** the constraint tool can also be started with no prior selection. By default the command will be in continue mode to create new constraints; press the right mouse button or **Esc** once to quit the command.

## Scripting


```pythonSketch.addConstraint(Sketcher.Constraint('Diameter', ArcOrCircle, App.Units.Quantity('123.0 mm')))```

The [Sketcher scripting](Sketcher_scripting.md) page explains the values which can be used for `ArcOrCircle`, and contains further examples on how to create constraints from Python scripts.


<div class="mw-translate-fuzzy">





</div>


{{Sketcher_Tools_navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainDiameter/es
