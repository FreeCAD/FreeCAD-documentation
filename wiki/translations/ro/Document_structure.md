# Document structure/ro
{{TOCright}}

![](images/Screenshot_treeview.jpg ) Un document FreeCAD conține toate obiectele din scenă. Poate conține grupuri și obiecte realizate cu oricare atelier.Ca urmare atelierele pot fi schimbate fără a părăsi documentul. Conținutul documentului este cel salvat pe disc. Mai multe documente pot fi deschise în acelasi timp și mai multe vizualizări al aceluiași document pot fi deschise în același timp.


<div class="mw-translate-fuzzy">

In ineriorul documentului obiectele pot fi mutate in grupuri si au un nume unic. Administrarea obiectelor, a grupurilor de obiecte si a numelor obiectelor se face in primul rand dn vizualizarea arborescenta. Toate acestea pot fi realizate ca orice altceva in FreeCAD, folosind script-uri [Python](Python/ro.md). In vizualizarea arborescenta se pot crea grupuri, muta obiecte in grupuri, sterge obiecte sau grupuri folosind meniul contextual (click dreapta cu mouse-ul). Redenumirea obiectelor se face cu dublu-click pe obiect. Este posibil sa existe si alte actiuni permise in functie de tipul obiectului si paleta curenta.


</div>


<div class="mw-translate-fuzzy">

Obiectele din documentul FreeCAD pot avea diferite tipuri. Fiecare atelier poate crea propriile tipuri de obiecte, de exemplu [Atelierul Plase](Mesh_Workbench/ro.md) creează obiecte plasă, atelierul [\|atelierul Piese](Part_Workbench/ro.md) poate crea piese, [Atelierul desen2D](Draft_Workbench/ro.md) poate crea și el piese, etc.


</div>

Daca este cel putin un document deschis in FreeCAD, atunci exact un document este activ. Acesta este documentul care apare in vizualizarea 3D curenta, documentul cu care lucrati in mod curent.

## Aplicatia si Interfata cu Utilizatorul 

Ca orice altceva in FreeCAD, partea de interfața grafică a utilizatorului (GUI) este separată de partea de aplicație (App). Acest lucru este adevărat și pentru documente. Acestea sunt și ele alcătuite din două părți   * partea de aplicație, ce conține obiecte, și partea de vizualizare, ce conține reprezentarea grafica a obiectelor.

Gândiți-vă la aceasta arhitectură ca la două spații unde obiectele sunt definite. Parametrii constructivi (este un cub? un con? ce dimensiuni are?) sunt stocați in partea de App, pe când reprezentarea grafică (liniile au culoarea neagră? fațetele sunt albastre?) este stocată în partea GUI. De ce aceasta separare? Pentru că FreeCAD poate fi folosit și {{emphasis|without}}

fără interfața grafică, de exemplu în interiorul altor programe, și trebuie să putem manipula obiectele chiar dacă nimic nu este desenat pe ecran.

O alta parte ce este stocată în partea de grafică sunt vizualizările 3D. Un document poate avea mai multe vizualizări deschise în același timp astfel ca să puteți examina conținutul documentului din mai multe puncte de vedere în același timp. Poate doriți să vedeți în același timp imaginea de sus și din față în același timp? In acest caz trebuie să folosiți două vizualizări stocate în partea grafică ce pot fi create în meniul Vizualizare sau prin click-dreapta pe un tab de vizualizare.

## Scripturi


<div class="mw-translate-fuzzy">

Documentele pot fi ușor create, accesate și modificate de la interpretorul [Python](Python.md) . De exemplu   *


</div>


```python
FreeCAD.ActiveDocument
```

O sa dea documentul curent 
```python
FreeCAD.ActiveDocument.Blob
``` O sa acceseze un document numit \"Blob\" inauntrul documentului activ 
```python
FreeCADGui.ActiveDocument
``` O sa dea partea grafica asociata cu documentul activ 
```python
FreeCADGui.ActiveDocument.Blob
``` O sa acceseze partea grafica a obiectului \"Blob\" 
```python
FreeCADGui.ActiveDocument.ActiveView
``` O sa dea vizualizarea activa


<div class="mw-translate-fuzzy">


{{docnav/ro|[Mouse Model](Mouse_Model/ro.md)|[Preferences Editor](Preferences_Editor/ro.md)}}


</div>



---
![](images/Right_arrow.png) [documentation index](../README.md) > Document structure/ro
