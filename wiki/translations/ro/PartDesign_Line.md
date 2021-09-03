---
- GuiCommand:/ro
   Name:PartDesign Line
   Name/ro:PartDesign Line
   Workbenches:[PartDesign](PartDesign_Workbench/ro.md)
   MenuLocation:Part Design → Create a datum line
   Version:0.17
   SeeAlso:[[PartDesign Point/ro]], [[PartDesign Plane/ro]]
---


</div>

## Descriere

Creează o linie de referință **datum line** care poate fi folosită ca referință pentru schițe, alte forme geometrice sau funcții(onalități). De exemplu, poate fi folosit ca axă de Rotație sau creare Caneluri.

<img alt="" src=images/datum_line.png  style="width:600px;">


<div class="mw-translate-fuzzy">

*Two Datum lines through opposite corners of the cube meet at the center of mass.*


</div>

## Cum se folosește {#cum_se_folosește}


<div class="mw-translate-fuzzy">

1.  apăsați butonul **<img src="images/PartDesign_Line.png" width=24px> '''Create a datum line'''**.
2.  Definiți parametrii liniei. Selectați o primă referință în vizualizarea 3D pentru filtrarea modurilor de atașare disponibile.
3.  În funcție de referința selectată, pot fi disponibile unul sau mai multe moduri de atașare în listă. Cel mai probabil va fi selectat automat și arătat cu caractere aldine în listă. Textul \"Atașat cu modul\" împreună cu numele modului de atașare va apărea cu verde în partea superioară a panoului Parametri.
4.  To add an additional reference, press the next **Reference** button. Once pressed its label changes to *Selecting\...* until a selection is made.
5.  Selectați un mod de attachment din listă.
6.  Definește valaorea Attachment Offset.
7.  Apăsați pe **OK**.


</div>

## Opţiuni


<div class="mw-translate-fuzzy">

Faceți dublu clic pe eticheta DatumLine din arborescența Model sau faceți clic cu butonul din dreapta și selectați **Editați datum** din meniul contextual pentru a edita parametrii. Pentru mai multe detalii despre modul referențiere și Attachment offset (decalajul referinței), consultați [Attachment](Part_Attachment.md).


</div>

## Proprietăți

-    **MapMode**: listează modul de tașamentu utilizat.

-    **Attachment Offset**: applies a transformation (translation and rotation) in reference to the attachment placement.

-    **Label**: nume dat obiectului, acest nume poate fi modificat la nevoie.





{{PartDesign Tools navi

}} 
