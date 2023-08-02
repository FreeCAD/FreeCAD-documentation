---
- GuiCommand:
   Name: Draft_Array
   Name/it: Serie
   MenuLocation: Draft -> Serie
   Workbenches: Draft_Workbench/it
   SeeAlso: Draft_PolarArray/it, Draft_CircularArray/it,Draft PathArray/it, Draft PointArray/it, Draft Clone/it
---

# Draft Array/it


</div>



## Descrizione


<div class="mw-translate-fuzzy">

Lo strumento **<img src="images/Draft_Array.svg" width=16px> [Serie](Draft_Array/it.md)** crea una schiera (array) ortogonale (3 assi) o polare utilizzando gli oggetti selezionati.


</div>


<div class="mw-translate-fuzzy">

Questo strumento può essere utilizzato su forme 2D create con [Draft](Draft_Workbench/it.md) ma può anche essere utilizzato su molti tipi di oggetti 3D come quelli creati con [Part](Part_Workbench/it.md) o [PartDesign](PartDesign_Workbench/it.md).


</div>

This command is now obsolete. Use the [Draft OrthoArray](Draft_OrthoArray.md), [Draft PolarArray](Draft_PolarArray.md) or [Draft CircularArray](Draft_CircularArray.md) command instead.

## Usage


<div class="mw-translate-fuzzy">

## Utilizzo

1.  Selezionare un oggetto con cui si desidera creare una serie.
2.  Premere il pulsante **<img src="images/Draft_Array.svg" width=16px> [Serie](Draft_Array/it.md)**. Se nessun oggetto è selezionato, si viene invitati a selezionarne uno.
3.  L\'oggetto Array viene creato immediatamente. È necessario modificare le proprietà della serie per modificare il numero e la direzione delle copie create.


</div>

## Properties


<div class="mw-translate-fuzzy">

## Proprietà

-    {{PropertyData/it|Base}}: specifica l\'oggetto da duplicare nella schiera.

-    {{PropertyData/it|Array Type}}: specifica il tipo di schiera da creare, {{value|"ortho"}}, {{value|"polar"}}, o {{value|"circular"}}.

-    {{PropertyData/it|Fuse}}: se è `True`, e le copie si intersecano tra loro, esse vengono fuse insieme in un\'unica forma.


</div>

## Scripting


<div class="mw-translate-fuzzy">

## Script


**Vedere anche:**

[API Arch](Arch_API/it.md) e [Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md).


</div>


<div class="mw-translate-fuzzy">





</div>



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Array/it
