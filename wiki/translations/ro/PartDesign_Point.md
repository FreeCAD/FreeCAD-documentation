---
- GuiCommand:/ro
   Name:PartDesign Point
   Name/ro:PartDesign Point
   Workbenches:[PartDesign](PartDesign_Workbench/ro.md)
   MenuLocation:Part Design → Create a datum point
   Version:0.17
   SeeAlso:[[PartDesign Line/ro]], [[PartDesign Plane/ro]]
---

# PartDesign Point/ro


</div>

## Descriere

Crearea unui punct de referință **datum point** care poate fi utilizat ca referință pentru schițe sau alte forme geometrice de referință.

![](images/DatumPoint.png )


<div class="mw-translate-fuzzy">

Un punct de referință atașat la o sferă care are un decalaj al atașamentului în Z = 2


</div>


<div class="mw-translate-fuzzy">

## Cum se folosește 


</div>


<div class="mw-translate-fuzzy">

1.  Apăsați pe butonul **<img src="images/PartDesign_Point.png" width=24px> '''Create a datum point'''** .
2.  Definiți parametrii punctului. Selectați o primă referință în vizualizarea 3D pentru a filtra modurile de atașare disponibile.
3.  În funcție de referința selectată, este posibil să existe unul sau mai multe moduri de atașare în listă. Cel mai probabil va fi selectată automat și afișată cu caractere aldine din listă. Textul *Attached with mode* iar numele modului de atașare apare verde în partea de sus a panoului Setări.
4.  Pentru a adăuga o referință suplimentară, apăsați butonul următor **Référence**. Odată butonul apăsat, eticheta sa va deveni *Sélection \...* până ce o selecție va fi făcută.
5.  Selecționați un mode atașare în listă.
6.  Definiți valorile decalajului de atașament.
7.  Apăsați pe **OK**.


</div>

## Opţiuni


<div class="mw-translate-fuzzy">

Faceți dublu clic pe eticheta DatumPoint din arborescența Model sau faceți clic cu butonul din dreapta și selectați **Editați datum** din meniul contextual pentru a edita parametrii. Pentru mai multe detalii despre modul referențiere și offset (decalajul referinței), consultați [Attachment](Part_EditAttachment.md).


</div>

## Proprietăți

-    **MapMode**: listează modurile de atașament folosite

-    **Attachment Offset**: applică o transformare (translație și rotație) în referință la plasamentul atașamentului.

-    **Label**: nume dat obiectului, acest nume poate fi schimbat dacă este necesar.

## Limite

-   Punctul de referință nu poate fi folosit ca secțiune pentru funcții(onalități)le Pipe, Sweep și Loft(funcțiile de baleiere și lisaj)





{{PartDesign Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Point/ro
