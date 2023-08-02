---
- GuiCommand:
   Name: PartDesign Plane
   Name/ro: PartDesign Plane
   Workbenches: PartDesign Workbench/ro
   MenuLocation: PartDesign -> Create a datum plane
   Version: 0.17
   SeeAlso: PartDesign Point/ro, PartDesign Line/ro
---

# PartDesign Plane/ro


</div>

## Descriere

Creați un plan de referință **datum plane** care poate fi folosit ca referință pentru schițe sau alte forme geometrice de referințe. Schițele pot fi atașate la planele de referință . ![](images/Datum_plane.png ) \"Planul de referință care traversează cele trei colțuri ale cubului cu partea de sus a unui Cilindru folosind planul de referință X-Y\".


<div class="mw-translate-fuzzy">

## Cum se folosește 


</div>

A datum plane, as of FreeCAD 0.18, can only be created inside of a <img alt="" src=images/PartDesign_Body.svg  style="width:16px;"> [Body](PartDesign_Body.md). Every body has an origin, which is hidden by default. To be able to refer to the origin base planes, make the the origin visible. You can do this before creating a datum plane.


<div class="mw-translate-fuzzy">

1.  Apăsați butonul **<img src="images/PartDesign_Plane.png" width=24px> '''Create a datum plane'''**.
2.  Define Plane parameters. Select a first reference in the 3D view to filter the available [attachment](Part_EditAttachment.md) modes.
3.  Depending on the selected reference, there may be one or more attachment modes available in the the list. The most likely one will automatically be selected and shown in bold in the list. The text *Attached with mode* along with the attachment mode name will appear in green at the top of the Parameters panel.
4.  To add an additional reference, press the next **Reference** button. Once pressed its label changes to *Selecting\...* until a selection is made.
5.  Select an attachment mode in the list.
6.  Define Attachment Offset values.
7.  Apăsați tasta **OK**.


</div>


<div class="mw-translate-fuzzy">

## Opţiuni


</div>


<div class="mw-translate-fuzzy">

Faceți dublu clic pe eticheta DatumPlane din arborescența Model sau faceți clic cu butonul din dreapta și selectați **Editați datum** din meniul contextual pentru a edita parametrii. Pentru mai multe detalii despre modul referențiere și offset (decalajul referinței), consultați [Attachment](Part_EditAttachment.md).


</div>


<div class="mw-translate-fuzzy">

## Proprietăți


</div>


<div class="mw-translate-fuzzy">

-    **MapMode**: listează modul de atașare utilizat.

-    **Attachment Offset**: applies a transformation (translation and rotation) in reference to the attachment placement.

-    **Label**: numele dat obiectului, acest nume poate fi modificat dacă vă este mai comod.


</div>

-    **MapMode**: lists the attachment mode used.

-    **Attachment Offset**: applies a transformation (translation and rotation) in reference to the attachment placement.

-    **Label**: name given to the object, this name can be changed at convenience.





{{PartDesign Tools navi

}}



---
⏵ [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Plane/ro
