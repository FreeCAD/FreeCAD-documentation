# OpenSCAD AddOpenSCADElement/ro
---
- GuiCommand:   Nume:OpenSCAD_AddOpenSCADElement   Name/ro:OpenSCAD_AddOpenSCADElement   Workbenches:[[OpenSCAD Workbench/ro   OpenSCAD]]|MenuLocation:OpenSCAD - Add OpenSCAD Element---


</div>

## Description


<div class="mw-translate-fuzzy">

#### Descriere

Adăugați un element OpenSCAD introducând cod OpenSCAD în panoul de activități și executând binarul OpenSCAD (necesită OpenSCAD).


</div>

Atunci când o plasă \'as mesh\' este selectată OpenSCAD randează o Mesh.

De fiecare dată când se execută codul openSCAD și se importă elemente.


<div class="mw-translate-fuzzy">

Dacă OpenSCAD revine cu succes, mesajele sale sunt afișate ca avertismente în fereastra raportului. Acesta va fi cazul în cazul în care calea către fișierele importate, incluse și utilizate nu este corectată. În cazul unor rezultate nedorite, este recomandat să consultați ferestrele de raport, deoarece ar putea exista multe alte rezultate create pe durata importului. Dacă OpenSCAD eșuează, mesajele sale vor fi înregistrate ca erori. Bibliotecile trebuie să fie accesibile ca de obicei, în timp ce exemplul poate fi atins după cum se arată mai jos


</div>

Libraries should be accessible as usual, whereas example can be reached as stated below.


```python
include <../examples/example001.scad>;
```


<div class="mw-translate-fuzzy">

ar include primele exemple cunoscute și sub numele de iconița/pictograma OpenSCAD


</div>

## Setup OpenSCAD within FreeCAD 


<div class="mw-translate-fuzzy">

#### Setarea inițială din cadrul FreeCAD 

-   OpenSCAD trebuie să fie instalat pe computer înainte ca FreeCAD să aibă această funcționalitate
    -   instalați OpenSCAD în modul corespunzător pentru sistemul dvs. de operare. Consultați [site-ul web OpenSCAD](http://www.openscad.org/) pentru mai multe informații
-   FreeCAD trebuie să-i spună unde să găsească executabilul OpenSCAD
    -   Comutați la meniul OpenBSD Workbench -\> View Workbench -\> OpenSCAD
    -   Deschideți meniul dialogului Preferințe -\> Editare -\> Preferințe
    -   Faceți clic pe \"OpenSCAD\" în planul din stânga
    -   Faceți clic pe butonul lasat \"\...\" în Setări generale -\> Setări generale OpenSCAD -\> OpenSCAD executabil pentru a naviga în director sau introduceți calea (de ex. Distribuții Linux / usr / bin / openscad pe bază de Ubuntu) dreapta la buton
    -   închideți și reporniți FreeCAD, o nouă pictogramă OpenSCAD va apărea pe bara de unelte și în meniul OpenSCAD în bara de lucru FreeCAD OpenSCAD
-   Este, de asemenea, posibil să adăugați un alt parametru opțional care controlează laturile maxime ale unui poligon înainte de a fi considerat un cerc (fn).


</div>

FreeCAD needs to be told where to find the OpenSCAD executable:

-   Switch to the <img alt="" src=images/Workbench_OpenSCAD.svg  style="width:24px;"> [OpenSCAD Workbench](OpenSCAD_Workbench.md) via 
**View → Workbench → OpenSCAD**
-   Open the preferences dialog **Edit → Preferences**
-   Click on \"OpenSCAD\" on the left plane
-   Click on the button labled **...** in **General Settings → General OpenSCAD Settings → OpenSCAD executable** to browse the directory or enter the path (e.g. Ubuntu based Linux distributions `/usr/bin/openscad`) directly into the line input right to the button
-   Close and restart FreeCAD

:   **Result:** A new OpenSCAD icon will appear on the tool bar, and in the OpenSCAD menu, in the FreeCAD OpenSCAD workbench.

Note: It is also possible to add another optional Parameter which controls the maximum sides of a polygon before it is considered a circle (fn).


<div class="mw-translate-fuzzy">

Pornind de la FreeCAD Version 0.14, FreeCAD va căuta executabilul OpenSCAD dacă setarea menționată mai sus este goală.


</div>





{{OpenSCAD_Tools_navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [OpenSCAD](OpenSCAD_Workbench.md) > OpenSCAD AddOpenSCADElement/ro
