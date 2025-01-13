# Feature editing/ro
## Introducere

This page explains the feature editing workflow of the <img alt="" src=images/Workbench_PartDesign.svg  style="width:32px;"> [PartDesign Workbench](PartDesign_Workbench.md).



## Corp


<div class="mw-translate-fuzzy">

Lucrul în PartDesign necesită mai întâi crearea unui <img alt="" src=images/PartDesign_Body.png  style="width:24px;"> **Corp**. Corpul este un container care grupează o secvență de caracteristici care formează un singur solid contiguu.


</div>

<img alt="" src=images/PartDesign_Feature_example.png  style="width:400px;">



*Feature editing in practice. From left to right:<br>
Body with a [box](PartDesign_AdditiveBox.md) feature.<br>
Body with a box and a [chamfer](PartDesign_Chamfer.md) feature.<br>
Body with a box, a chamfer and a [pocket](PartDesign_Pocket.md) feature.*

A document can contain multiple Bodies, but only one Body can be active. New features are added to the active Body. A Body can be activated or deactivated by double clicking it in the [Tree view](Tree_view.md). The activate Body is highlighted in the Tree view.

![](images/PartDesign_Body_tree.png )

### What is a contiguous solid? 


<div class="mw-translate-fuzzy">

Ce este un solid solid contiguu? Este un obiect ca o piesă turnată sau ceva prelucrat dintr-un singur bloc de metal. Dacă obiectul implică cuie, șuruburi, lipici sau sudură, acesta nu este un singur solid contiguu. Ca un exemplu practic, un scaun din lemn ar fi făcut din mai multe corpuri, câte unul pentru fiecare subcomponentă (picioare, șipci, fundul scaunului etc.).


</div>

In FreeCAD version 1.0 an experimental property was introduced that allows the Body to have non-contiguous solids. This can also be set in the [Preferences](PartDesign_Preferences#General.md) as default for newly created Bodies. This is not intended to be used to build, as in the example, a chair in one Body. It is meant to allow features that may produce disconnected solids that will be made contiguous by later features.


<div class="mw-translate-fuzzy">

Atunci când un model necesită mai multe corpuri, cum ar fi exemplul precedent de scaun din lemn, scopul general [container part](Std_Part/ro.md) poate fi utilizat pentru a le grupa și a muta întregul ca unitate.


</div>



### Managementul Vizibilității Corpului 


<div class="mw-translate-fuzzy">

Un corp va prezenta implicit caracteristica cea mai recentă spre exterior. Această caracteristică este definită în mod prestabilit ca vârf. O bună analogie este expresia \"vârful aisbergului\": numai vârful este vizibil deasupra apei, cea mai mare parte a masei aisbergului (celelalte caracteristici) este ascunsă. Când o caracteristică nouă este adăugată corpului, vizibilitatea caracteristicii anterioare este dezactivată, iar noua caracteristică devine sfat.


</div>


<div class="mw-translate-fuzzy">

Nu poate exista decât o funcție vizibilă la un moment dat. Este posibil să comutați vizibilitatea oricărei caracteristici din corp, selectându-l în arborele Modelului și apăsând bara de spațiu, revenind în istoricul corpului.


</div>



### Mișcarea și Reorientarea Obiectelor 


<div class="mw-translate-fuzzy">

Este posibilă redefinirea temporară a vârfului la o caracteristică din mijlocul arborelui Corpului pentru a insera obiecte noi (caracteristici, schițe sau geometrie de origine). De asemenea, este posibilă reordonarea funcțiilor sub un Corp sau mutarea acestora într-un alt Corp. Selectați obiectul și faceți clic dreapta pentru a obține un meniu contextual care va oferi ambele opțiuni. Operația poate fi împiedicată dacă obiectul are dependențe în corpul sursă, cum ar fi atașarea la o față. Pentru a muta o schiță într-un alt corp, nu ar trebui să conțină legături către geometria exterioară.


</div>

<img alt="" src=images/PartDesign_workflow.svg  style="width:400px;">



*Schematic representation of the PartDesign workflow.*



## Geometria de referință 


<div class="mw-translate-fuzzy">

Geometria de referință constă din planuri personalizate, linii, puncte sau forme legate în exterior. Acestea pot fi create pentru a fi folosite ca referință prin schițe și caracteristici. Există o multitudine de posibilități de atașament pentru date.


</div>

In FreeCAD, datum planes make sense if you are placing sketches in non-standard orientations, that is, on planes offset or rotated around the three main axes. But since sketches can also be placed in non-standard orientations and have the same attachment options as datum planes, there is often no need to use them. Datum planes make the most sense if there is more than one sketch with the same non-standard orientation. Adjusting the orientation of the datum plane will then adjust all associated sketches and the features created from those sketches.

Although FreeCAD version 1.0 already has code to mitigate the [topological naming problem](Topological_naming_problem.md), it is still best practice to attach both sketches and datum planes to the base planes of the Body\'s Origin whenever possible. Referencing generated geometry (geometry that is the result of a feature operation, for example a pad or pocket) may yet result in less stable models. See [Advice for creating stable models](#Advice_for_creating_stable_models.md) below.



## Sfat pentru crearea de modele stabile 


<div class="mw-translate-fuzzy">

Ideea de modelare parametrică implică faptul că puteți modifica valorile anumitor parametri, iar pașii ulteriori sunt modificați în funcție de noile valori. Cu toate acestea, atunci când se fac modificări ample, modelul se poate rupe. Comparativ cu versiunile anterioare ale FreeCAD, ruperea poate fi redusă la minimum atunci când respectați următoarele principii de proiectare:


</div>


<div class="mw-translate-fuzzy">

-   Practic, trebuie să opriți cartografierea schițelor în fațete - în întregime! Plasați schițele pe planurile standard sau pe planurile de referință personalizate.
-   Atunci când creați geometria de origine, nu o bazați pe topologia piesei, bazați-o pe planuri standard / axe și / sau schițe.
-   Utilizați o \"schiță master\". Aceasta este o schiță de preferință nu prea complicată care conține elemente geometrice de bază ale modelului dvs. Aceste elemente pot fi menționate la modelarea caracteristicilor ulterioare. O astfel de schiță principală va fi de multe ori prima schiță din Corp, dar nu trebuie să fie; de fapt, nici măcar nu trebuie să-l folosiți deloc pentru altceva decât pentru a fi referit.
-   Dacă trebuie să menționați în mod inevitabil o caracteristică intermediară, de ex. rezultatul unei operațiuni de grosime, utilizați prima referință posibilă în lista caracteristicilor ulterioare în care are loc elementul geometric referit. Din FreeCAD 0.17 nu trebuie să utilizați cea mai recentă caracteristică. Dacă luați o caracteristică timpurie ca referință, toate modificările aduse pașilor intermediari nu vă vor sparge modelul. Și din nou, este mai bine să faceți referire la o schiță decât la marginile și vârfurile unui solid.


</div>

## Tutorials

The [tutorials](Tutorials.md) page provides some examples of using the feature editing method of the [PartDesign Workbench](PartDesign_Workbench.md).

-   [Creating a simple part with PartDesign](Creating_a_simple_part_with_PartDesign.md)
-   [Basic Part Design Tutorial 019](Basic_Part_Design_Tutorial_019.md)
-   [Basic Attachment Tutorial](Basic_Attachment_Tutorial.md)

## Related

-   [Constructive solid geometry](Constructive_solid_geometry.md)


{{PartDesign Tools navi

}}



---
⏵ [documentation index](../README.md) > [Common Questions](Category_Common Questions.md) > [PartDesign](Category_PartDesign.md) > Feature editing/ro
