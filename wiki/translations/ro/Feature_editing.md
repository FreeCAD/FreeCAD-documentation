# Feature editing/ro
{{TOCright}}

## Introducere

This page explains the way the <img alt="" src=images/Workbench_PartDesign.svg  style="width:32px;"> [PartDesign Workbench](PartDesign_Workbench.md) is intended to be used starting with FreeCAD 0.17.


<div class="mw-translate-fuzzy">

În timp ce [Part Workbench](Part_Workbench/ro.md) și alte ateliere FreeCAD construiesc modele prin combinarea formelor împreună, atelierul PartDesign folosește **caracteristicile**. Funcția [1](https://en.wikipedia.org/wiki/Feature_recognition) este o operațiune care modifică forma unui model.


</div>

## Metodologia de editare a funcțiilor 

Prima caracteristică este în mod obișnuit numită **caracteristică de bază**. La adăugarea mai multor caracteristici la model, fiecare caracteristică ia forma celei anterioare și adaugă sau înlătură materialul, creând dependențe liniare de la o caracteristică la alta. De fapt, această metodologie imită un proces de fabricație obișnuit: un bloc este tăiat pe o parte, apoi pe altă parte, se adaugă găuri, apoi arce de cerc etc.

Toate funcțiile sunt listate secvențial în arborele Model și pot fi editate în orice moment, ultima caracteristică din partea de jos reprezentând partea finală.

Caracteristicile pot fi sortate în diferite categorii:

-   **Bazat pe profil**: aceste caracteristici pornesc de la un profil pentru a defini forma materiei care urmează să fie adăugată sau eliminată. Profilul poate fi o schiță, o față plană pe geometria existentă (un profil va fi extras din marginile sale), un ShapeBinder sau un obiect Draft care a fost inclus în corpul activ.

-   *\'Additiv*: adaugă material modelului existent. Funcțiile adiționale prezintă iconițele galbene.

-   **Subtractive**: elimină materialul din modelul existent. Funcțiile subtitrate prezintă icoanițele roșii și albastre.

-   **Bazate pe Primitive**: bazate pe primitive geometrice (cub, cilindru, con, torus \...). Acestea pot fi aditive sau subtractive.

-   **Caracteristicile transformării**: aplică o transformare la caracteristicile existente (simetrică, model liniar, model polar, multitransformare).

-   **Dress-up**: caracteristici care aplică un tratament pe margini sau fețe, cum ar fi teșire/ rotunjire, șanfren și trasare.

-   **Procedural**: se poate spune despre caracteristici care nu se bazează pe schițe, cum ar fi trăsăturile de transformare și traiectoria adițională.

## Corp


<div class="mw-translate-fuzzy">

Lucrul în PartDesign necesită mai întâi crearea unui <img alt="" src=images/PartDesign_Body.png  style="width:24px;"> **Corp**. Corpul este un container care grupează o secvență de caracteristici care formează un singur solid contiguu.


</div>

![](images/PartDesign_Body_tree.png )


<div class="mw-translate-fuzzy">

Ce este un solid solid contiguu? Este un obiect ca o piesă turnată sau ceva prelucrat dintr-un singur bloc de metal. Dacă obiectul implică cuie, șuruburi, lipici sau sudură, acesta nu este un singur solid contiguu. Ca un exemplu practic, un scaun din lemn ar fi făcut din mai multe corpuri, câte unul pentru fiecare subcomponentă (picioare, șipci, fundul scaunului etc.).


</div>

Corpurile multiple pot fi create într-un document FreeCAD; ele pot fi, de asemenea, combinate pentru a forma un singur solid contiguu.

Only one body can be active in a document. The active body gets the new created features. A body can be activated or deactivated by double clicking on it. An activated body is highlighted in light blue. The highlighting color can be set in the preferences under Display/Colors/Active container since version 0.18.


<div class="mw-translate-fuzzy">

Atunci când un model necesită mai multe corpuri, cum ar fi exemplul precedent de scaun din lemn, scopul general [container part](Std_Part/ro.md) poate fi utilizat pentru a le grupa și a muta întregul ca unitate.


</div>

### Managementul Vizibilității Corpului 

Un corp va prezenta implicit caracteristica cea mai recentă spre exterior. Această caracteristică este definită în mod prestabilit ca vârf. O bună analogie este expresia \"vârful aisbergului\": numai vârful este vizibil deasupra apei, cea mai mare parte a masei aisbergului (celelalte caracteristici) este ascunsă. Când o caracteristică nouă este adăugată corpului, vizibilitatea caracteristicii anterioare este dezactivată, iar noua caracteristică devine sfat.


<div class="mw-translate-fuzzy">

Nu poate exista decât o funcție vizibilă la un moment dat. Este posibil să comutați vizibilitatea oricărei caracteristici din corp, selectându-l în arborele Modelului și apăsând bara de spațiu, revenind în istoricul corpului.


</div>

### Originea corpului 

Corpul are o origine care constă din planuri de referință (XY, XZ, YZ) și axe (X, Y, Z) care pot fi folosite de către schițe și caracteristici. Schițele pot fi atașate la planurile de origine și nu mai trebuie să fie cartografiate pe fețe plane pentru ca elementele bazate pe ele să fie adăugate sau scăzute din model.

### Mișcarea și Reorientarea Obiectelor 

Este posibilă redefinirea temporară a vârfului la o caracteristică din mijlocul arborelui Corpului pentru a insera obiecte noi (caracteristici, schițe sau geometrie de origine). De asemenea, este posibilă reordonarea funcțiilor sub un Corp sau mutarea acestora într-un alt Corp. Selectați obiectul și faceți clic dreapta pentru a obține un meniu contextual care va oferi ambele opțiuni. Operația poate fi împiedicată dacă obiectul are dependențe în corpul sursă, cum ar fi atașarea la o față. Pentru a muta o schiță într-un alt corp, nu ar trebui să conțină legături către geometria exterioară.

### Difference with other CAD systems 

A fundamental difference between FreeCAD and other programs, like Catia, is that FreeCAD doesn\'t allow you to have many disconnected solids in the same <img alt="" src=images/PartDesign_Body.svg  style="width:24px;"> **[PartDesign Body](PartDesign_Body.md)**. That is, a new feature should always be built on top of the previous one. Or said in a different way, the newer feature should \"touch\" the previous feature, so that both features are fused together and become a single solid. You cannot have \"floating\" solids.

<img alt="" src=images/PartDesign_Body_non-contiguous.png  style="width:550px;">



*Difference between Catia and FreeCAD. Left: Catia allows disconnected bodies from the previous features of the body. In FreeCAD this causes an error; Right: the newer feature should always contact or intersect the previous feature so that it is fused to it, and becomes a single contiguous solid.*

## Geometria de referință 


<div class="mw-translate-fuzzy">

Geometria de referință constă din planuri personalizate, linii, puncte sau forme legate în exterior. Acestea pot fi create pentru a fi folosite ca referință prin schițe și caracteristici. Există o multitudine de posibilități de atașament pentru date.


</div>

In some CAD systems you can define a datum plane that is offset from the previous body and you can create a disconnected solid. So, placing a lot of datum planes, and building objects on them is okay and won\'t cause an error. Typically, you would eventually adjust the planes to their final positions, so that the individual objects are fused together.

In FreeCAD, as mentioned in the previous section, disconnected solids are **NOT** allowed, so a sketch on a datum plane that would create a non-contiguous solid will fail.

In FreeCAD, datum planes make sense if you are placing sketches (and padding, pocketing, etc.) in non-standard orientations, that is, in planes offset or rotated around the three main axes. Since sketches can also be placed in non-standard orientations in the same way as datum planes, often there is no need to use datum planes.

Datum planes also make sense if there will be more than one sketch in the same non-standard orientation. In this case a datum plane can be used and the orientation only needs to be adjusted for the datum plane to adjust all associated sketches and the features created from the sketches.

Both sketches and datum planes should be attached to base planes. Referencing generated geometry (geometry that is the result of a feature creating operation, for example a pad or pocket) should be avoided since faces and edges get renamed and renumbered and the references no longer refer to the same thing. This is called topological instability and is due the way FreeCAD uses some external geometric libraries. Hopefully this will be improved in the future. (See Advice for creating stable models below).

Even if not used for supporting sketches, datum objects are still helpful as visual indicators, to draw attention to important features or distances in the modelling process. (Though, simply adding geometry to a sketch also provides similar visual feedback.)

<img alt="" src=images/PartDesign_Body_non-contiguous_slanted.png  style="width:550px;">



*Difference between Catia and FreeCAD. Left: Catia allows disconnected bodies from the previous features of the body. In FreeCAD this causes an error; Right: the newer feature should always contact or intersect the previous feature, so that it is fused to it, and becomes a single contiguous solid. In this example, the new solid is based on a datum plane that is rotated around the Y axis.*

## Referințe încrușișate 


<div class="mw-translate-fuzzy">

Este posibilă trimiterea elementelor dintr-un corp în alt corp prin referințe. De exemplu, liantul de formă de origine permite copierea pe fețe dintr-un corp ca referință în altul. Acest lucru ar trebui să ușureze construirea unei cutii cu capac de montaj în două corpuri diferite. FreeCAD vă ajută să nu vă conectați în mod accidental la alte organisme și să vă întrebe care vă este intenția.


</div>

## Atașament

Obiectul atașat nu este un instrument specific PartDesign, ci mai degrabă un utilitar Partea introdus în v0.17 care poate fi găsit în meniul Part. Este foarte folosită în atelierul PartDesign pentru a atașa schițele și geometria de referință la planurile și axele standard ale Corpului. Sunt disponibile metode foarte extensive de a crea puncte de referință, linii și planuri. Parametrii offset de atașare opțional fac acest instrument foarte versatil.


<div class="mw-translate-fuzzy">

Informații suplimentare pot fi găsite la [Attachment](Part_EditAttachment/ro.md) page.


</div>

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

## Body building workflow 

There are several workflows that are possible with the [PartDesign Workbench](PartDesign_Workbench.md). What should always be noticed is that all the features created inside a [PartDesign Body](PartDesign_Body.md) will be fused together to obtain the final object.

### Different sketches 

Sketches need to be supported by a plane. This plane can be one of the main planes (XY, XZ, or YZ) defined by the Origin of the Body. A sketch is either extruded into a positive solid (additive), with a tool like <img alt="" src=images/PartDesign_Pad.svg  style="width:24px;"> [PartDesign Pad](PartDesign_Pad.md), or into a negative solid (subtractive), with a tool like <img alt="" src=images/PartDesign_Pocket.svg  style="width:24px;"> [PartDesign Pocket](PartDesign_Pocket.md). The first adds volume to the final shape of the body, while the latter cuts volume from the final shape. Any number of sketches and partial solids can be created in this way; the final shape (tip) is the result of fusing these operations together. Naturally, the Body can\'t consist of only subtractive operations, as the final shape should be a solid with a positive, non-zero volume.

<img alt="" src=images/PartDesign_workflow_1.svg  style="width:600px;">

### Sequential features 

Sketches can be supported by the faces of previous solid operations. This may be necessary if you need to access a face that is only available after a certain feature has been created. However, this workflow isn\'t recommended since, if the original feature is modified, the following features in the sequence may break. This is the [topological naming problem](Topological_naming_problem.md).

<img alt="" src=images/PartDesign_workflow_2.svg  style="width:600px;">

### Use of datum planes for support 

Datum planes are useful to support the sketches. These auxiliary planes should be attached to the base planes of the body.

*Note: In many cases, a sketch attached to a base plane with attachment offsets can accomplish the same function. Datums are particularly useful when multiple sketches or other constructs will use the datum. This means all changes to the datum will be apply to attached sketches, etc. Adding a single sketch to a datum, rather than using attachment offsets in the sketch properties, is an extra step and is essentially redundant.*

As with sketches, it is possible to attach Datum planes to generated geometry (edges, faces of previously created solids), ***but this is not recommended*** since it can cause the topological naming problem.

In addition, a <img alt="" src=images/PartDesign_ShapeBinder.svg  style="width:24px;"> [PartDesign ShapeBinder](PartDesign_ShapeBinder.md) can be used to import external geometry into the body to serve as reference; then sketches can be attached to this auxiliary body, either using datum planes or not.

*Again, the ShapeBinder should be based on Sketches from the previous body, not generated geometry.*

Using datum objects is often the best way to produce stable models, when used with base planes and attachment offsets, although it requires a bit more work from the user. For details about basic attachment see: [Basic Attachment Tutorial](Basic_Attachment_Tutorial.md) *Note: while this tutorial talks about sketches, datum attachment is done in similar fashion.*

## Tutorials

The [tutorials](Tutorials.md) page provides some examples of using the [feature editing](Feature_editing.md) method of the <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [PartDesign Workbench](PartDesign_Workbench.md).

-   [Creating a simple part with PartDesign](Creating_a_simple_part_with_PartDesign.md)
-   [Basic Part Design Tutorial](Basic_Part_Design_Tutorial.md)
-   [Basic Attachment Tutorial](Basic_Attachment_Tutorial.md)

## Related

-   [Constructive solid geometry](Constructive_solid_geometry.md)

<img alt="" src=images/PartDesign_workflow_3.svg  style="width:600px;">


{{PartDesign Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Common Questions](Category_Common Questions.md) > [PartDesign](Category_PartDesign.md) > Feature editing/ro
