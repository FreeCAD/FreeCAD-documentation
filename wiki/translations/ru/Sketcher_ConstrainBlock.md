---
- GuiCommand:/ru
   Name/ru:Ограничение перемещения
   Name:Sketcher_ConstrainBlock
   MenuLocation:Sketch → Ограничения эскиза → Constrain Block
   Workbenches:[Sketcher](Sketcher_Workbench/ru.md)
   Version:0.17
   SeeAlso:[Ограничение положения](Sketcher_ConstrainLock/ru.md)
---

# Sketcher ConstrainBlock/ru

## Описание

**Блокирующее ограничение** фиксирует геометрический элемент в указанном месте, одним нажатием.

It is mainly intended to be used with **[<img src=images/Sketcher_CreateBSpline.svg style="width:16px"> [B-Splines](Sketcher_CreateBSpline.md)**, which can be difficult to fully constrain otherwise.

## Применение

1.  Выберите элемент, степень свободы которого вы хотите ограничить.
2.  Нажмите на кнопку **[<img src=images/Sketcher_ConstrainBlock.svg style="width:16px"> [Ограничение (Привязка)](Sketcher_ConstrainBlock/ru.md)**.

Или наоборот в начале нажмите кнопку, а потом выберите элемент.

## Программирование


```pythonSketch.addConstraint(Sketcher.Constraint('Block', Edge))```

The [Sketcher scripting](Sketcher_scripting.md) page explains the values which can be used for `Edge` and contains further examples on how to create constraints from Python scripts.





{{Sketcher Tools navi

}}

---
[documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainBlock/ru
