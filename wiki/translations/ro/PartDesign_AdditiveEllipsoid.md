# PartDesign AdditiveEllipsoid/ro
---
- GuiCommand:   Name: PartDesign AdditiveEllipsoid   Workbenches: PartDesign Workbench   PartDesign---


</div>

## Descriere

Introduceți un elipsoid primitiv în Corpul activ ca o funcție de bază sau îmbinați-l cu o funcție(onalitate) existentă.

<img alt="" src=images/PartDesign_AdditiveEllipsoid_example.png  style="width:200px;">


<div class="mw-translate-fuzzy">

## Cum se folosește 


</div>


<div class="mw-translate-fuzzy">

1.  Apăsați mai întâi butonul **<img src="images/PartDesign_AdditiveEllipsoid.png" width=24px> '''Additive Ellipsoid'''**. **Notă**: Elipsoidul Aditiv parte dintr-un meniu cu pictograme etichetat *Create an additive primitive*. După lansarea FreeCAD, Additive Box este printe cele afișate în toolbar. Pentru a obține butonul Ellipsoid, click pe săgeata în jos alături de iconița vizibilă și selectați Ellipsoid in meniu.
2.  Definiți parametrii Primitivei geometrice și [Attachment](Part_EditAttachment.md).
3.  Click pe **OK**.
4.  O funcție(onalitate) Ellipsoid apare sub Copul activ.


</div>

## Opţiuni


<div class="mw-translate-fuzzy">

Elipsoidul poate fi editat după crearea sa în două moduri:

-   Double-clicking pe el în arborescența Model, sau right-clicking și selectați **Edit primitive** in meniul contextual; acest lucru deschide parametrii Primitivei geometrice.
-   Via [Property editor](Property_editor.md).


</div>

## Proprietăți


<div class="mw-translate-fuzzy">

-    **Attachment**: definește modul de atașare, precum și decalajul atașamentului. Vedeți [Part EditAttachment](Part_EditAttachment.md).

-    **Label**: numele/eticheta dată obiectului Ellipsoid. Poate fi schimba funcție de nevoile dvs.

-    **Radius1**: valoarea razei de-a lungul axei verticale a elipsoidului; în mod prestabilit, paralel cu axa Z.

-    **Radius2**: valoarea razei de-a lungul lungimii elipsoidului; în mod prestabilit, paralel cu axa X.

-    **Radius3**: valoarea razei de-a lungul lățimii elipsoidului; în mod prestabilit, paralel cu axa Y. La valoarea implicită de zero, elipsoidul formează un [oblate spheroid](http://en.wikipedia.org/wiki/Oblate_spheroid). Aceasta are aceeași formă ca și când Radius3 este identic cu Radius2.

-    **Angle1**: (etichetat cu parametrul \"V\" din parametrii Primitive) trunchierea inferioară a elipsoidului, paralelă cu secțiunea transversală circulară (-90 grade într-un sferoid complet)

-    **Angle2**:(neetichetat printre parametrii Primitive) trunchierea superioară a elipsoidului, paralelă cu secțiunea transversală circulară (90 de grade într-un sferoid complet).

-    **Angle3**: (numit *U parameter* în parametrii Primitivei) unghiul de rotație a secțiunii eliptice (360 de grade într-un sferoid complet).


</div>





{{PartDesign_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign AdditiveEllipsoid/ro
