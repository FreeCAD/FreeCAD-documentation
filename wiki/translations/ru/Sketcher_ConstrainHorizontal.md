---
 GuiCommand:
   Name/ru: Ограничение горизонтальности
   Name: Sketcher_ConstrainHorizontal
   MenuLocation: Sketch , Ограничения эскиза , Ограничение горизонтальности
   Workbenches: Sketcher_Workbench/ru
   Shortcut: **H**
   SeeAlso: Sketcher_ConstrainVertical/ru
---

# Sketcher ConstrainHorizontal/ru


</div>



## Описание


<div class="mw-translate-fuzzy">

Горизонтальное ограничение заставляет выбранную линию или линии в эскизе быть параллельными горизонтальной оси эскиза.


</div>


<small>(v1.0)</small> 

: In most cases it is advisable to use the combined [Sketcher ConstrainHorVer](Sketcher_ConstrainHorVer.md) tool instead.



## Применение

See also: [Drawing aids](Sketcher_Workbench#Drawing_aids.md).

### [Continue mode](Sketcher_Workbench#Continue_modes.md) 


<div class="mw-translate-fuzzy">

<img alt="" src=images/HorizontalConstraint1.png  style="width:500px;"> 
*Выберите отрезок на эскизе, кликнув по нему.*


</div>

### Run-once mode 

1.  Do one of the following:
    -   Select two or more points.
    -   Select one or more lines. Points can be included in the selection, but will be ignored.
2.  Invoke the tool as explained above, or with the following additional option:
    -   
        <small>(v1.0)</small> 
        
        : Right-click in the [3D view](3D_view.md) and select the **<img src="images/Sketcher_ConstrainHorizontal.svg" width=16px> Constrain horizontal** option from the context menu.
3.  Depending on the selection one or more constraints are added.



## Программирование


```pythonSketch.addConstraint(Sketcher.Constraint('Horizontal', Line))```

The [Sketcher scripting](Sketcher_scripting.md) page explains the values which can be used for `Line` and contains further examples on how to create constraints from Python scripts.


<div class="mw-translate-fuzzy">





</div>



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainHorizontal/ru
