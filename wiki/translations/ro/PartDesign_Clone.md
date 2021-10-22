---
- GuiCommand:/ro
   Name:PartDesign Clone
   Name/ro:PartDesign Clone
   Workbenches:[PartDesign](PartDesign_Workbench/ro.md)
   MenuLocation:Part Design → Create a clone
   Version:0.17
   SeeAlso:[Draft Clone](Draft_Clone/ro.md)
---

# PartDesign Clone/ro


</div>

## Descriere


<div class="mw-translate-fuzzy">

**PartDesign Clone** creează o copie legată a unui obiect selectat. Cele mai multe tipuri de obiecte sunt acceptate, atâta timp cât sunt solide singulare. Utilizarea principală a Clonei PartDesign este de a folosi un obiect creat într-un alt Atelier de lucru pentru o funcție [PartDesign Boolean](PartDesign_Boolean.md) . Poate fi pur și simplu utilizat pentru a crea copii corelate.


</div>

![*Clone of the inner gear while being translated in 3D space as an independent object*](images/clone.png ) 
*Clone of the inner gear while being translated in 3D space as an independent object*

## Cum se folosește 


<div class="mw-translate-fuzzy">

1.  In arborescența Model, selectați obiectul de clonat.
2.  Apăsați butonul **<img src=images/PartDesign_Clone.png style="width:24px"> '''Create a clone'''**.


</div>

## Proprietăți


<div class="mw-translate-fuzzy">

-    **Base Feature**: definește obiectul origina pe care se bazează clona. Pentru a în locuit, apăsați butonul **...** pentru a obține o listă a obiectelor disponibile.

-    **Placement**: definește orientarea și poziția clonei ăn spașiul 3D. A se vedea[Placement](Placement.md).

-    **Label**: numele/eticheta dată obiectului Clonă. Poate fi schimbat dacă vă este necesar.


</div>

## Limite


<div class="mw-translate-fuzzy">

-   Numai un singur obiect poate fi folosit pentru o clona PartDesign.
-   Sunt acceptate numai obiectele care constau dintr-un singur solid. Prin urmare, [compounds](Glossary#Compound.md) like [Part container](Std_Part.md), [Part Compound](Part_Compound/ro.md) or [Draft Array](Draft_Array.md) are not supported.


</div>





{{PartDesign Tools navi

}}

---
[documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Clone/ro
