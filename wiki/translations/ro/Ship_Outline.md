---
- GuiCommand:   Name:Ship Outline   MenuLocation:Ship design → Outline draw   |Workbenches:[[Ship Workbench   Ship]]|Shortcut:   SeeAlso:---


</div>


<div class="mw-translate-fuzzy">

## Introducere

De făcut


</div>

Plots the ship hull outline draw

## Desenarea Liniilor 

FreeCAD-Ship furnizează un instrument care facilitează obținerea unui Line Plan de la desenul liniilor navei


<div class="mw-translate-fuzzy">

![Outline draw tool.](images/FreeCAD-Ship-OutlineDrawIco.png )


<center>

Lines drawing tool icon


</center>


</div>

Linia de desen este un set de linii din secțiuni tăiate în toate cele trei axe, care va arăta în cele din urmă geometria corpului într-un plan de linii. Trebuie să furnizăm linii pentru următoarele 3 vizionări: Planul corporal (folosind tăieturile transversale)

-   Planul de Sheer (folosind Longitudinals Cuts)
-   Plan de jumătate de lățime (folosind tăieturile pe linia de plutire)


<div class="mw-translate-fuzzy">

### Secțiuni transversale 

De obicei, trebuie efectuate 21 de secțiuni transversale echidistante între perpendiculare. pentru a face acest lucru, FreeCAD oferă un instrument automat pentru a face acest lucru, pur și simplu selectați tipul de secțiune transversală, mergeți la caseta \"Creare automată\" și setați secțiunile \"21\" , apoi apăsați \'\' \'Creare secțiuni\' \'\'.


</div>

![Outline draw transversal sections preview.](images/S60OutlineTransversal.png )


<center>

Outline draw transversal sections preview


</center>

Tabelul secțiunilor este umplut, iar previzualizarea secțiunilor numit **OutlineDraw** este afișată. De obicei, mai multe secțiuni au fost adăugate la prova și la pupa, unde sunt înregistrate curburi complexe, pentru a face acest lucru la sfârșitul mesei și faceți dublu clic pe elementul gol pentru al edita, apăsând pe intro la a confirma. Adăugați următoarele secțiuni:

-   X~22~ = -12.1125 m
-   X~23~ = 12.1125 m

În funcție de complexitatea geometriei carenei, previzualizarea secțiunilor poate dura ceva timp. Pentru a elimina o secțiune, completați-o cu un text gol și apăsați pe Enter.


<div class="mw-translate-fuzzy">

### Secțiunile Longitudinale 

Două secțiuni longitudinale trebuie adăugate, așa că selectați **Longitudinal** ca tip de secțiune, mergeți la caseta *Auto create*\' și setați **2** secțiuni, apoi apăsăsați **Create sections**. Tabela secțiunii este completată și previzualizarea secțiunilor este actualizată.


</div>


<div class="mw-translate-fuzzy">

### Linii de plutire 

6 Linii de plutire Trebuie să adăugați între linia de bază și schița de proiectare, deci selectați tipul secțiunilor \"Waterlines\" \"\", mergeți la caseta \"Creare automată\" și setați \"5\" (Z = 0 m nu va fi luată în considerare, adăugați-o manual dacă aveți nevoie de ea), apoi apăsați \'\' \'Creare secțiuni\' \'\'. Tabelul secțiunilor este umplut și previzualizarea secțiunilor este actualizată.


</div>

Several additional waterlines must be added:

-   Z~6~ = 1.2 m
-   Z~7~ = 1.4 m
-   Z~8~ = 1.6 m
-   Z~9~ = 1.8 m
-   Z~10~ = 2.0 m


<div class="mw-translate-fuzzy">

### Perform plot 

Select **1:100** scale and press **Accept** to let the tool to generate the 3D sections in a new object.


</div>

![Resultant sections.](images/FreeCAD-Ship-S60Outline3DSections.png )


<center>

Resultant sections.


</center>

In order to plot these sections you can use the [Drawing workbench](Drawing_Workbench.md):

![Outline draw plot.](images/FreeCAD-Ship-S60OutlinePlot.png )


<center>

Outline draw plot.


</center>

## Tutoriale

-   [FreeCAD-Ship s60 tutorial ](FreeCAD-Ship_s60_tutorial.md)
-   [FreeCAD-Ship s60 tutorial (II)](FreeCAD-Ship_s60_tutorial_(II).md)





{{Ship_Tools_navi

}}  
