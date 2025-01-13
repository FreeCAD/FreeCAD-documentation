---
 GuiCommand:
   Name/ru: Ограничение перемещения
   Name: Sketcher_ConstrainBlock
   MenuLocation: Sketch , Ограничения эскиза , Constrain Block
   Workbenches: Sketcher_Workbench/ru
   Version: 0.17
   SeeAlso: Sketcher_ConstrainLock/ru
---

# Sketcher ConstrainBlock/ru


</div>



## Описание


<div class="mw-translate-fuzzy">

**Блокирующее ограничение** фиксирует геометрический элемент в указанном месте, одним нажатием.


</div>

The block constraint only affects the freely movable parts of an edge. Blocked edges can have other constraints, and applying additional constraints to a blocked edge can modify it.



## Применение

See also: [Drawing aids](Sketcher_Workbench#Drawing_aids.md).

### [Continue mode](Sketcher_Workbench#Continue_modes.md) 


<div class="mw-translate-fuzzy">

1.  Выберите элемент, степень свободы которого вы хотите ограничить.
2.  Нажмите на кнопку **[<img src=images/Sketcher_ConstrainBlock.svg style="width:16px"> [Ограничение (Привязка)](Sketcher_ConstrainBlock/ru.md)**.


</div>

### Run-once mode 

1.  Select one or more edges.
2.  Invoke the tool as explained above, or with the following additional option:
    -   
        <small>(v1.0)</small> 
        
        : Right-click in the [3D view](3D_view.md) and select the **<img src="images/Sketcher_ConstrainBlock.svg" width=16px> Constrain block** option from the context menu.
3.  Depending on the selection one or more constraints are added.



## Программирование


```pythonSketch.addConstraint(Sketcher.Constraint('Block', Edge))```

The [Sketcher scripting](Sketcher_scripting.md) page explains the values which can be used for `Edge` and contains further examples on how to create constraints from Python scripts.


<div class="mw-translate-fuzzy">





</div>


{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainBlock/ru
