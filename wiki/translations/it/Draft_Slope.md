---
- GuiCommand:/it
   Name:Draft Slope
   Name/it:Draft Slope
   MenuLocation:Draft → Utilità → Imposta la pendenza
   Workbenches:[Draft](Draft_Workbench/it.md), [Arch](Arch_Workbench/it.md)
   Version:0.17
   SeeAlso:[Linea](Draft_Line/it.md), [Polilinea](Draft_Wire/it.md)
---

# Draft Slope/it

## Descrizione


<div class="mw-translate-fuzzy">

Per una [Linea](Draft_Line/it.md) o una [Polilinea](Draft_Wire/it.md) selezionata e disegnata sul piano XY, lo strumento Pendenza aumenta la coordinata Z di tutti i vertici dopo il primo, in modo che la linea o la polilinea abbia la pendenza definita.


</div>

<img alt="" src=images/Draft_Slope_example.png  style="width:400px;">


<div class="mw-translate-fuzzy">



*Linea orizzontale; linea con la pendenza modificata di 45°*


</div>

## Utilizzo


<div class="mw-translate-fuzzy">

1.  Selezionare uno o più oggetti [Wire](Draft_Wire/it.md) o [Linea](Draft_Line/it.md)
2.  Andare nel menu **Draft → Utilità → <img src="images/Draft_Slope.png" width=16px> [Imposta la pendenza](Draft_Slope/it.md)**.
3.  Impostare il valore di pendenza desiderato e premere il pulsante **OK**.


</div>

## Scripting

See also: _.

There is no Python method to slope objects. To emulate the results of the Draft Slope command the `Points` property of wire objects has to be modified.

---
[documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Slope/it
