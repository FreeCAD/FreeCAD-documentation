---
- GuiCommand:/ro
   Name:Draft Array   Name/ro:Matrice repetabilitate
   MenuLocation:Draft → Array
   Workbenches:[Draft](Draft_Workbench/ro.md), [Arch](Arch_Workbench/ro.md)
   SeeAlso:[PolarArray](Draft_PolarArray.md), [CircularArray](Draft_CircularArray.md), [PathArray](Draft_PathArray.md), [PointArray](Draft_PointArray.md), [Clone](Draft_Clone.md)
---

# Draft Array/ro


</div>




<div class="mw-translate-fuzzy">

## Descriere

Instrumentul Array creează o matrice ortogonală (3-axe) sau polară dintr-un obiect selectat. Dacă nu este selectat niciun obiect, veți fi invitat să selectați unul.


</div>

The <img alt="" src=images/Draft_Array.svg  style="width:24px;"> **Draft Array** command creates an orthogonal (3-axes) array from a selected object. The created array can be turned into a [polar array](Draft_PolarArray.md) or a [circular array](Draft_CircularArray.md) by changing its **Array Type** property.

The command can be used on 2D objects created with the [Draft Workbench](Draft_Workbench.md) or [Sketcher Workbench](Sketcher_Workbench.md), but also on many 3D objects such as those created with the [Part Workbench](Part_Workbench.md), [PartDesign Workbench](PartDesign_Workbench.md) or [Arch Workbench](Arch_Workbench.md).

This command is now obsolete. Use the [Draft OrthoArray](Draft_OrthoArray.md), [Draft PolarArray](Draft_PolarArray.md) or [Draft CircularArray](Draft_CircularArray.md) command instead.

## Usage


<div class="mw-translate-fuzzy">

## Cum se utilizează 

1.  Selectați un obiect cu care doriți să faceți o matrice

2.  Apăsați tasta {{KEY | <img src="images/Draft_Array.svg" width=16px> [Array de Proiect](Draft_Array.md)}}

3.  Selectați {{PropertyData | Array Type}}: Specifică tipul matricei, orto sau polar

4.  Pentru matrice ortogonale:
    1.  
        {{PropertyData | Interval X}}
        
        : Intervalul dintre fiecare copie pe prima axă

    2.  
        {{PropertyData | Interval Y}}
        
        : Intervalul dintre fiecare copie pe a doua axă

    3.  
        {{PropertyData | Interval Z}}
        
        : Intervalul dintre fiecare copie pe a treia axă

    4.  
        {{PropertyData | Număr X}}
        
        : Numărul de copii pe prima axă

    5.  
        {{PropertyData | Număr Y}}
        
        : numărul de copii pe a doua axă

    6.  
        {{PropertyData | Număr Z}}
        
        : Numărul de copii pe a treia axă

5.  Pentru tablouri polare:
    1.  
        {{PropertyData | Axis}}
        
        : Direcția normală a cercului matricei

6.  
    {{PropertyData | Center}}: Punctul central al matricei

7.  
    {{PropertyData | Angle}}: Unghiul de acoperire cu copii

8.  
    {{PropertyData | Număr Polar}}: Numărul de copii


</div>

## Properties

See [Draft OrthoArray](Draft_OrthoArray#Properties.md).

## Scripting


<div class="mw-translate-fuzzy">

## Script-Programre 

Instrumentul Array poate fi utilizat în [macros](macros.md) și din consola Python utilizând una dintre următoarele funcții, în funcție de situația în care doriți să obțineți copii simple, independente ale obiectului de bază sau un obiect parametric, care rămâne legat de obiectul original.


</div>


<div class="mw-translate-fuzzy">





</div>



---
![](images/Button_right.svg) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Array/ro
