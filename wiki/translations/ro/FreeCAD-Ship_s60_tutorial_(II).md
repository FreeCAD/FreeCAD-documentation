# FreeCAD-Ship s60 tutorial (II)/ro
{{TutorialInfo/ro
|Topic=Ship Workbench
|Level= Beginner
|Time=
|Author=
|FCVersion=
|Files=
}}

## Overview

Înainte de a începe acest tutorial, vă rugăm să vă asigurați că ați parcurs deja [prima parte](FreeCAD-Ship_s60_tutorial.md).


<div class="mw-translate-fuzzy">

Puteți învăța mai mult despre vapoare [FreeCAD-Ship here](Ship_Workbench.md)


</div>

## Introducere

În acest tutorial vom lucra cu încărcări și compartimente pentru a calcula curba GZ (brațul cuplului de redresare), cel mai important parametru de stabilitate hidrostatică. GZ este momentul static generat atunci când nava ia un unghi de rotire, desigur, deoarece brațul GZ este pozitiv, nava are un moment pozitiv și va încerca să recupereze poziția verticală, dar când GZ se aprinde pe numerele negative nava nu mai are stabilitate , atingând o situație critică.

OMI (Organizația Maritimă Internațională) stabilește următoarele criterii:

-   \"GM\"\> = 0,15 m. \'GM\' \'(înălțimea metacentrică) este tangenta inițială a curbei\' \'GZ\' \'.
-   Valoarea maximă \'\' GZ \'\' trebuie plasată peste 30 de grade de unghi de rulare.
-   Cu un unghi de rotire de 30 de grade, valoarea \'\' GZ \'\' trebuie să fie de cel puțin 0,2 m.
-   Zona implicată de curba \"GZ\" până la 40 de grade de unghi de rulare trebuie să fie de cel puțin 0,090 m.
-   Zona implicată de curba \"GZ\" până la 30 de grade de unghi de rulare trebuie să fie de cel puțin 0,055 m.
-   Zona implicată de curba \"GZ\" de la 30 la 40 de grade de unghi de rulare trebuie să fie de cel puțin 0,030 m · rad.


<div class="mw-translate-fuzzy">

În acest tutorial vom stabili greutăți și rezervoare pentru nava seriei 60, într-o situație ipotetică.


</div>

## Încărcarea navei 

Pentru a putea calcula curba GZ trebuie să cunoaștem greutățile navei și poziția lor la fiecare unghi de rotire, astfel încât greutățile vor fi împărțite în două categorii:

-   Greutăți fixe, care sunt pe deplin legate de mișcările navei.
-   Rezervoare, în cazul în care forma fluide se schimbă cu unghiul, necesitând un centru de greutate calcul în fiecare poziție.


<div class="mw-translate-fuzzy">

FreeCAD-Ship provides two different tools to generate each instance.


</div>

![Weights definition tool icon.](images/FreeCAD-Ship-WeightIco.png )


<center>

Weights definition tool icon.


</center>


<div class="mw-translate-fuzzy">

Instrumentul de definire a greutății poate fi utilizat pentru a stabili prima categorie de greutăți. Atunci când lansați instrumentul pentru prima dată (cu selectarea navei), FreeCAD-Ship inițializează greutățile navei cu nava ușoară (egală cu deplasarea navei) plasată pe coordonata X a centrului de greutate al geometriei navei și la înălțimea proiectată. De obicei, aveți cel puțin 2 ponderi relevante:

-   Structura.
-   Motorul principal (sau mai multe dintre ele).


</div>


<div class="mw-translate-fuzzy">

Așa că o vom schimba. Dacă faceți dublu clic pe fiecare celulă, putem edita valoarea, setând aceste greutăți:

-   Structura, 15000 kg, (-0,1, 0, 1,25) m
-   Motor de tribord, 5000 kg, (-6,5, -0,65, 0,5) m
-   Motor babord, 5000 kg, (-6,5, 0,65, 0,5) m
-   Motor de urgență, 2500 kg, (0,2, 0, 2,5) m


</div>

![Weights definition 3D preview.](images/FreeCAD-Ship-S60WeightsPreview.png )


<center>

Weights definition 3D preview.


</center>


<div class="mw-translate-fuzzy">

Pozițiile greutăților sunt afișate în ecranul 3D. Aceste adnotări vor fi eliminate atunci când veți termina cu instrumentul, deci nu vă ocupați de acest lucru. Când apăsați pe **Accept**, greutățile vor fi stocate în exemplul dvs. de navă.


</div>


<div class="mw-translate-fuzzy">

## Cisterne

Cisternele/rezervoarele trebuie să fie create pe partea de sus a geometriei solide, așa cum este cazul navei, astfel încât primul pas este să creați două rezervoare de arc (câte una pe o parte a navei) geometrii solide pe care le vom lua în considerare (de obicei navele au o mulțime de rezervoare pentru combustibil, apă dulce, sare apă, încărcătură etc.).


</div>

### Generarea geometriei 

Pentru a genera rezervoare, încărcăm [Part module](Part_Workbench.md) și creăm o cutie solidă.


<div class="mw-translate-fuzzy">

Trebuie să editați caseta, așa că o selectăm pe arborele **Atribute și etichete**și schimbăm din fila vizualizare în fișierul de date. Deblocați Plasarea și plasați-o în Poziție și setați \"x\" la 1.5 și z la -1. Vrem să schimbăm lungimea casetei schimbând-o prea mult pentru 5.0 (rețineți că unitățile pot fi în mm, nu aveți grijă de asta).


</div>

Geometria rezervoarelor va fi o parte comună a cadrului creat și a geometriei navei, astfel încât să putem ascunde exemplul**Ship** și să arătăm geometria \'\'\'s60\_IowaUniversity \'\'\'. Selectând caseta și **s60\_IowaUniversity** putem folosi operațiunea comună generând geometria rezervorului nostru la tribord.

![Generated tank geometry.](images/FreeCAD-Ship-S60TankGeometry.png )


<center>

Generated tank geometry.


</center>

We can perform port side tank selecting our starboard geometry and executing mirror tool, selecting XZ as mirror plane.

In order to convert geometry into a ussual solid shape our tanks, and recover our **s60\_IowaUniversity** geometry, we can load [Draft module](Draft_Workbench.md), and with starboard tank geometry selected execute Upgrade, and repeat with port side tank geometry. We can rename geometries as:

-   StarboardTankGeom
-   PortTankGeom

We can delete created Box, that we don\'t need anymore.

### Generarea exemplelor de rezervoare 

Dacă reîncărcați [ FreeCAD-Ship module](Ship_Workbench.md) încă o dată, putem găsi unealtă generator de variante de rezervor.

![Tank instance generation tool icon.](images/FreeCAD-Ship-TankIco.png )


<center>

Tank instance generation tool icon.


</center>


<div class="mw-translate-fuzzy">

Now we can select **StarboardTankGeom** and execute tank instnace generation tool, where some data must be provided. We will set 40% of filling level, and 925 kg/m$\mathrm{m}^{3}$ (fuel approach). When **Accept** is clicked a new tank instance called **Tank** is generated. We can rename it as **StarboardTank**, and hide **StarboardTankGeom**.


</div>

We can repeat the same process in order to generate **PortTank**.

![View of generated weights.](images/FreeCAD-Ship-S60WeightsTanksPreview.png )


<center>

View of generated weights.


</center>

Figure shown our ship result that we will compute.


<div class="mw-translate-fuzzy">

### Calculul curbei GZ 

FreeCAD-Ship furnizează un instrument pentru a calcula cu ușurință o curbă \"GZ\".


</div>

<img alt="GZ curve computation tool icon." src=images/Ship_GZ.svg  style="width:128px;">


<center>

GZ curve computation tool icon.


</center>


<div class="mw-translate-fuzzy">

Cu instanța **Ship** selectată, putem folosi instrumentul. Primul lucru pe care îl putem vedea în caseta de dialog deschis este o listă a tuturor instanțelor de cisterne găsite în documentul activ.. Vrem să le folosim pe amândouă, așa că faceți clic pe rezervoarele care sunt remarcate cu un fundal diferit .


</div>

Pentru a cunoaște deplasarea și schița rezultată a navei, putem apăsa **Actualizați deplasarea și schița**, luând un timp pentru calcul. Primim următoarele date:

-   Deplasament = 37505,5 kg
-   Pescaj = 0.818664 m


<div class="mw-translate-fuzzy">

So we are in a unloaded situation, where draft are sightly lower than design draft. Ussually lower drafts imply lower ship stability, the draft depends on loading condition, so if we really expect than ship can be operated in this loading condition we can consider implement ballast tanks.


</div>

De asemenea, putem calcula automat pescajul de-a lungul navei, operație care poate dura aproximativ un minut, recuperând faptul că nava noastră are un unghi de înclinare de 0,95 grade (pozitiv de pupă). În acest exemplu vom lucra fără unghi de tăiere (0 grade).

Unele unghiuri de ruliu sunt luate în considerate de asemenea În acest caz vrem să cunoaștem toate comportamentele navei, astfel încât să putem seta:

-   Unghi de ruliu de 0 grade.
-   Unghi de ruliu la 180 de grade.
-   46 de puncte. Unul pentru fiecare 2 grade. Calculul GZ poate dura ceva timp, deci aveți grijă de numărul de puncte solicitate.


<div class="mw-translate-fuzzy">

Când apăsăm butonul \'\'\'Accept \'\'\', instrumentul începe calculul. Dacă rulați FreeCAD din terminal, puteți vedea progresul lucrului. În câteva secunde vom primi curba GZ.


</div>

This tool use [pyxplot](http://www.pyxplot.org.uk/) and [ghostscript](http://www.ghostscript.com/) too. You can see where **gz.dat** output file has been placed at the report view (View/Views/Report view), and load it with datasheet software (for example [libreOffice](http://www.libreoffice.org)). Nearby data file several auxiliary files has been created too:

-   **gz.dat**: Computed GZ curve data.
-   **gz.pyxplot**: pyxplot layout in order to plot the curve.
-   **gz.eps**: EPS image version.
-   **gz.png**: PNG image version.

This files will be overwritten if you executes the tool another time.

### Resultate

<img alt="Resultant GZ curve." src=images/FreeCAD-Ship-s60GZ.png  style="width:800px;">


<center>

Resultant GZ curve.


</center>


<div class="mw-translate-fuzzy">

*GZ* maximum value is placed over 30 degrees (45 degrees), getting 0.25 m at 30 degrees (0.2 m is the minimum). Up to 30 degrees the area below *GZ* curve is 0.065 m·rad, up to 40 degrees we have 0.092 m·rad, being the area between 30 and 40 degrees of 0.027 m·rad. So our ship don\'t meets the IMO requeriments. The solution is place ballast tanks.


</div>


<div class="mw-translate-fuzzy">

Pe de altă parte, nava, în această stare proastă, are valori pozitive ale \"GZ\" până la un unghi de rotație de 95 de grade, dar nu a fost suficient pentru cerințele de stabilitate ale OMI, arătând cerințele grele impuse acestui element.


</div>


<div class="mw-translate-fuzzy">

Desigur, acest exemplu nu este real (mai întâi pentru toate cisternele de combustibil nu pot fi plasate în structura dublă a fundului, sau folosind structura cocăi), dar este un bun exemplu pentru a învăța să folosești [FreeCAD-Ship](Ship_Workbench.md).


</div>


{{Ship Tools navi

}}

---
[documentation index](../README.md) > FreeCAD-Ship s60 tutorial (II)/ro
