---
 GuiCommand:
   Name: Draft Array
   Name/it: Serie
   Workbenches: Draft_Workbench/it, Arch_Workbench/it
   SeeAlso: Draft_OrthoArray/it, Draft_PolarArray/it, Draft_CircularArray/it
---

# Draft Array/it



## Descrizione

Il comando <img alt="" src=images/Draft_Array.svg  style="width:24px;"> **Draft Array** crea una serie ortogonale (3 assi) da un oggetto selezionato. La serie creata può essere trasformata in un [array polare](Draft_PolarArray/it.md) o in un [array circolare](Draft_CircularArray/it.md) modificando la sua proprietà **Array Type**.

Il comando può essere utilizzato su oggetti 2D creati con [Draft](Draft_Workbench/it.md) o [Sketcher](Sketcher_Workbench/it.md), ma anche su molti oggetti 3D come quelli creati con [Part](Part_Workbench/it.md), [PartDesign](PartDesign_Workbench/it.md) o [Arch](Arch_Workbench/it.md).

Questo comando è ormai obsoleto. Utilizzare invece il comando [Serie ortogonale](Draft_OrthoArray/it.md), [Serie polare](Draft_PolarArray/it.md) o [Serie circolare](Draft_CircularArray/it.md).



## Utilizzo

1.  Per utilizzare questo comando in FreeCAD versione 0.19 e successive è necessario aggiungere un pulsante ad una barra degli strumenti personalizzata. Vedere [Personalizzazione dell\'interfaccia](Interface_Customization/it.md).
2.  Facoltativamente seleziona un oggetto.
3.  Premere il pulsante **<img src="images/Draft_Array.svg" width=16px> [Serie](Draft_Array/it.md)**.
4.  Se non si è ancora selezionato un oggetto: selezionare un oggetto.
5.  La serie viene creata.
6.  Eventualmente modificarne le [proprietà](Draft_OrthoArray/it#Proprietà.md).



## Proprietà

Vedere [Serie ortogonale](Draft_OrthoArray/it#Proprietà.md).



## Script

Vedere [Serie Ortogonale](Draft_OrthoArray/it#Script.md).



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Array/it
