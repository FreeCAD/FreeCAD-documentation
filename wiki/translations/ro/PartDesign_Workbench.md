# <img alt="PartDesign workbench icon" src=images/Workbench_PartDesign.svg  style="width:64px;"> PartDesign Workbench/ro


{{TOCright}}

## Introduction


<div class="mw-translate-fuzzy">

## Introducere

\"Atelierul Part Design\" oferă instrumente avansate pentru modelarea componentelor solide complexe și se bazează pe o metodă de [feature-editing methodology](#Feature_Editing_Methodology.md). Se concentrează în cea mai mare parte pe, dar nu se limitează la, crearea de piese mecanice. Este strâns legată de [Sketcher Workbench](Sketcher_Workbench.md).


</div>


<div class="mw-translate-fuzzy">

Baza de lucru PartDesign este în mod intrinsec legată de [Sketcher Workbench](Sketcher_Workbench.md). În mod normal, utilizatorul creează o schiță, apoi utilizează instrumentul [PartDesign Pad](PartDesign_Pad.md) pentru a-l extruda și a crea un solid de bază, iar acest solid este modificat ulterior.


</div>


<div class="mw-translate-fuzzy">

În timp ce _ pentru o explicație mai completă a acestui proces și apoi a se vedea [Creating a simple part with PartDesign](Creating_a_simple_part_with_PartDesign.md) pentru a începe să creați solide.


</div>

A more detailed discussion of Part workbench versus Part Design workbench can be found here: [Part and Part Design](Part_and_PartDesign.md).

The bodies created with PartDesign are often subject to the [topological naming problem](Topological_naming_problem.md) which causes internal features to be renamed when the parametric operations are modified. This problem can be minimized by following the best practices described in the [feature editing](feature_editing.md) page, and by taking advantage of datum objects as support for sketches and features.

<img alt="" src=images/PartDesign_Example.png  style="width:500px;">

## Instrumente


<div class="mw-translate-fuzzy">

Instrumentele de proiectare a componentelor sunt amplasate în meniul *\' Design Part*\' și în bara de instrumente PartDesign care apare atunci când încărcați atelierul Part Design.


</div>

### Structure tools 


<div class="mw-translate-fuzzy">

These are tools to organize the Model tree.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Std_Part.png  style="width:32px;"> [Part](Std_Part.md): adds a new Part container in the active document and makes it active.
-   <img alt="" src=images/Group.svg  style="width:32px;"> [Group](Std_Group.md): adds a Group in the active document\'s Model tree.


</div>

-   <img alt="" src=images/Std_Group.svg  style="width:32px;"> _.

### Instrumente Help pentru Part Design 


<div class="mw-translate-fuzzy">

-   ![ 32px](images/_PartDesign_Body.png ) [ Create body](PartDesign_Body/ro.md): Creează un corp în documentul activ și îl activează.


</div>


<div class="mw-translate-fuzzy">

-   !_ în modul de editare a schițelor.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_EditSketch.png  style="width:32px;"> [Edit sketch](Sketcher_EditSketch.md): Editează Sketch selectat.


</div>


<div class="mw-translate-fuzzy">

-   ![ 32px](images/_Sketcher_MapSketch.png ) [Mapează o schiță pe o fațetă ](Sketcher_MapSketch.md): Mapează o schiță pe un plan selectat anterior sau o fațetă a corpului activ.


</div>

### Part Design Modeling tools 

#### Instrumente de referință 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/PartDesign_Point.png  style="width:32px;"> [Create a datum point](PartDesign_Point.md): creează un punct de referință în corpul activ.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/PartDesign_Line.png  style="width:32px;"> [Create a datum line](PartDesign_Line.md): creează o linie de referință în corpul activ.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/PartDesign_Plane.png  style="width:32px;"> [Create a datum plane](PartDesign_Plane.md): creează un plan de referință în corpul activ.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/PartDesign_CoordinateSystem.png  style="width:32px;"> [Create a local coordinate system](PartDesign_CoordinateSystem.md): creează un sistem de coordonate local atașat la referința geometrică în corpul activ.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/PartDesign_ShapeBinder.png  style="width:32px;"> [Create a shape binder](PartDesign_ShapeBinder.md): creează un liant de formă corpul activ.


</div>

-   <img alt="" src=images/PartDesign_SubShapeBinder.svg  style="width:32px;"> [Create a sub-object shape binder](PartDesign_SubShapeBinder.md): creates a shape binder to a subelement, like edge or face from another body, while retaining the relative position of that element. <small>(v0.19)</small> 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/PartDesign_Clone.png  style="width:32px;"> [Create a clone](PartDesign_Clone.md): creează o clonă a corpului selectat.


</div>

#### Instrumente Aditive 

Acestea sunt instrumente pentru crearea de caracteristici de bază sau adăugarea de materiale unui corp solid existent.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/PartDesign_Pad.png  style="width:32px;"> [Pad](PartDesign_Pad.md): extrudează un solid dintr-o schiță selectată.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/PartDesign_Revolution.png  style="width:32px;"> [Revolution](PartDesign_Revolution.md): creează un solid prin rotirea unei schițe în jurul unei axe. Schița trebuie să formeze un profil închis.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/PartDesign_AdditiveLoft.png  style="width:32px;"> [Additive loft](PartDesign_AdditiveLoft.md): creează un solid prin efectuarea unei tranziții între două sau mai multe schițe.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/PartDesign_AdditivePipe.png  style="width:32px;"> [Additive pipe](PartDesign_AdditivePipe.md):creează un solid baleind una sau mai multe schițe de-a lungul unei traiectorii deschise sau închise.


</div>

-   <img alt="" src=images/PartDesign_AdditiveHelix.svg  style="width:32px;"> [Additive helix](PartDesign_AdditiveHelix.md): creates a solid by sweeping a sketch along a helix. <small>(v0.19)</small> 


<div class="mw-translate-fuzzy">

-   _: adaugă o primitivă geometrică aditivă la corpul activ.


</div>


<div class="mw-translate-fuzzy">

:\*<img alt="" src=images/PartDesign_AdditiveBox.png  style="width:32px;"> [Additive box](PartDesign_AdditiveBox.md): creează un paralelipiped aditiv.


</div>


<div class="mw-translate-fuzzy">

:\*<img alt="" src=images/PartDesign_AdditiveCone.png  style="width:32px;"> [Additive cone](PartDesign_AdditiveCone.md): creează un con aditiv.


</div>


<div class="mw-translate-fuzzy">

:\*<img alt="" src=images/PartDesign_AdditiveCylinder.png  style="width:32px;"> [Additive cylinder](PartDesign_AdditiveCylinder.md): creează un cilindru aditiv.


</div>


<div class="mw-translate-fuzzy">

:\*<img alt="" src=images/PartDesign_AdditiveEllipsoid.png  style="width:32px;"> [Additive ellipsoid](PartDesign_AdditiveEllipsoid.md): creează un elipsoid aditiv.


</div>


<div class="mw-translate-fuzzy">

:\*<img alt="" src=images/PartDesign_AdditivePrism.png  style="width:32px;"> [Additive prism](PartDesign_AdditivePrism.md): creează o prismă aditivă.


</div>


<div class="mw-translate-fuzzy">

:\*<img alt="" src=images/PartDesign_AdditiveSphere.png  style="width:32px;"> [Additive sphere](PartDesign_AdditiveSphere.md): creează o sferă aditivă.


</div>


<div class="mw-translate-fuzzy">

:\*<img alt="" src=images/PartDesign_AdditiveTorus.png  style="width:32px;"> [Additive torus](PartDesign_AdditiveTorus.md): creează un tor aditiv.


</div>


<div class="mw-translate-fuzzy">

:\*<img alt="" src=images/PartDesign_AdditiveWedge.png  style="width:32px;"> [Additive wedge](PartDesign_AdditiveWedge.md): creează o pană aditivă.


</div>

#### Instrumente substractive 

Acestea sunt instrumente pentru îndepărtarea materialului dintr-un corp existent.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/PartDesign_Pocket.png  style="width:32px;"> [Pocket](PartDesign_Pocket.md): creează o gaură dreptunghiulară/un buzunar din schița selectată.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/PartDesign_Hole.png  style="width:32px;"> [Hole](PartDesign_Hole.md): creează o funcționalitate tip gaură din schița selectată. Schița trebuie să conțină unul sau mai multe cercuri.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/PartDesign_Groove.png  style="width:32px;"> [Groove](PartDesign_Groove.md): creează o canelură prin rotirea schiței în jurul unei axe.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/PartDesign_SubtractiveLoft.png  style="width:32px;"> [Subtractive loft](PartDesign_SubtractiveLoft.md):

creează o formă solidă făcând o tranziție/extrudere între două sau mai multe schițe și o scade din corpul activ.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/PartDesign_SubtractivePipe.png  style="width:32px;"> [Subtractive pipe](PartDesign_SubtractivePipe.md): creează o formă solidă prin baleierea uneia sau a mai multor schițe de-a lungul unei traiectorii deschise sau închise și o scade din corpul activ.


</div>

-   <img alt="" src=images/PartDesign_SubtractiveHelix.svg  style="width:32px;"> [Subtractive helix](PartDesign_SubtractiveHelix.md): creates a solid shape by sweeping a sketch along a helix and subtracts it from the active body. <small>(v0.19)</small> 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/PartDesign_CompPrimitiveSubtractive.png  style="width:48px;"> [Create a subtractive primitive](PartDesign_CompPrimitiveSubtractive.md): adaugă o primitivă geometrică substractivă la corpul activ.


</div>


<div class="mw-translate-fuzzy">

:\*<img alt="" src=images/PartDesign_SubtractiveBox.png  style="width:32px;"> [Subtractive box](PartDesign_SubtractiveBox.md): adaugă un paralelipiped substractiv la corpul activ.


</div>


<div class="mw-translate-fuzzy">

:\*<img alt="" src=images/PartDesign_SubtractiveCone.png  style="width:32px;"> [Subtractive cone](PartDesign_SubtractiveCone.md): adaugă un con subtractiv la corpul activ.


</div>


<div class="mw-translate-fuzzy">

:\*<img alt="" src=images/PartDesign_SubtractiveCylinder.png  style="width:32px;"> [Subtractive cylinder](PartDesign_SubtractiveCylinder.md): adaugă un cilindru substractiv la corpul activ.


</div>


<div class="mw-translate-fuzzy">

:\*<img alt="" src=images/PartDesign_SubtractiveEllipsoid.png  style="width:32px;"> [Subtractive ellipsoid](PartDesign_SubtractiveEllipsoid.md): adaugă un elipsoid substractiv la corpul activ.


</div>


<div class="mw-translate-fuzzy">

:\*<img alt="" src=images/PartDesign_SubtractivePrism.png  style="width:32px;"> [Subtractive prism](PartDesign_SubtractivePrism.md): adaugă o prismă substractivă la corpul activ.


</div>


<div class="mw-translate-fuzzy">

:\*<img alt="" src=images/PartDesign_SubtractiveSphere.png  style="width:32px;"> [Subtractive sphere](PartDesign_SubtractiveSphere.md): adaugă o sferă substractivă la corpul activ.


</div>


<div class="mw-translate-fuzzy">

:\*<img alt="" src=images/PartDesign_SubtractiveTorus.png  style="width:32px;"> [Subtractive torus](PartDesign_SubtractiveTorus.md): adaugă un tor substractiv la corpul activ.


</div>


<div class="mw-translate-fuzzy">

:\*<img alt="" src=images/PartDesign_SubtractiveWedge.png  style="width:32px;"> ‎[Subtractive wedge](PartDesign_SubtractiveWedge.md): adaugă o pană substractivă la corpul activ.


</div>

#### instrumente de Transformare 

Acestea sunt instrumente pentru transformarea caracteristicilor existente. Acestea vă vor permite să alegeți caracteristicile care trebuie transformate.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/PartDesign_Mirrored.png  style="width:32px;"> [Mirrored](PartDesign_Mirrored.md): simetrizați una sau mai multe caracteristici față de un plan sau o fațetă.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/PartDesign_LinearPattern.png  style="width:32px;"> [Linear Pattern](PartDesign_LinearPattern.md): creează un model liniar bazat pe una sau mai multe caracteristici.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/PartDesign_PolarPattern.png  style="width:32px;"> [Polar Pattern](PartDesign_PolarPattern.md): creează un model circular/polar bazat pe una sau mai multe caracteristici.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/PartDesign_MultiTransform.png  style="width:32px;"> [Create MultiTransform](PartDesign_MultiTransform.md): creează un model bazat pe orice combinație a altor transformări.


</div>

#### Instrumente pentru traiectorie suplimentară 

Aceste instrumente se aplică tratării marginilor sau fațetelor selectate.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/PartDesign_Fillet.png  style="width:32px;"> [Fillet](PartDesign_Fillet.md): rotunjirea marginilor/colțurilor corpului activ


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/PartDesign_Chamfer.png  style="width:32px;"> [Chamfer](PartDesign_Chamfer.md): șanfrenarea marginilor corpului activ.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/PartDesign_Draft.png  style="width:32px;"> [Draft](PartDesign_Draft.md): se aplică conicitate la fațetele corpului activ.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/PartDesign_Thickness.png  style="width:32px;"> [Thickness](PartDesign_Thickness.md):

creează o cochilie/coajă groasă din corpul activ și deschide fațeta(ele) selectate.


</div>

#### Boolean


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/PartDesign_Boolean.png  style="width:32px;"> [Boolean operation](PartDesign_Boolean.md): importă unul sau mai multe Corpuri sau Clone PartDesign în corpul activ și le aplică o operație booleană.


</div>

#### Suplimentar

Unele funcționalități suplimentare găsite în meniul PartDesign:


<div class="mw-translate-fuzzy">

-   [Migrează](PartDesign_Migrate.md): migrează fișierele create cu versiuni mai vechi din FreeCAD. Dacă fișierul este o componentă pură pe bază de elemente, migrarea ar trebui să aibă succes. În cazul în care fișierul conține amestec de obiecte Part/Part Design/Draft, conversia va eșua, cel mai probabil.


</div>

-   <img alt="" src=images/PartDesign_Sprocket.svg  style="width:32px;"> [Sprocket design wizard](PartDesign_Sprocket.md): creates a sprocket profile that can be padded. <small>(v0.19)</small> 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/PartDesign_InternalExternalGear.png  style="width:32px;"> [Involute gear](PartDesign_InvoluteGear.md):creează un profil de angrenaj cu profil în evolventă care poate fi utilizat de un PAD.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/PartDesign_WizardShaft.png  style="width:32px;"> [Shaft design wizard](PartDesign_WizardShaft.md): Generă un arbore dintr-o tabelă de valori și permite analizarea forțelor și momentelor. Arborele este realizat cu o schiță de revoluție care poate fi editată.


</div>


<div class="mw-translate-fuzzy">

### Meniu Contextual de Instrumente 


</div>

-   <img alt="" src=images/PartDesign_MoveTip.svg  style="width:32px;"> [Set tip](PartDesign_MoveTip.md): redefines the tip, which is the feature exposed outside of the Body.

-   <img alt="" src=images/PartDesign_MoveFeature.svg  style="width:32px;"> [Move object to other body](PartDesign_MoveFeature.md): moves the selected sketch, datum geometry or feature to another Body.

-   <img alt="" src=images/PartDesign_MoveFeatureInTree.svg  style="width:32px;"> [Move object after other object](PartDesign_MoveFeatureInTree.md): allows reordering of the Body tree by moving the selected sketch, datum geometry or feature to another position in the list of features.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/PartDesign_MoveTip.png  style="width:32px;"> [Set tip](PartDesign_MoveTip.md): redefinește vârful, care este caracteristica expusă în afara corpului.


</div>

-   <img alt="" src=images/Std_SetAppearance.svg  style="width:32px;"> [Appearance](Std_SetAppearance.md): determines appearance of the whole part (color transparency etc.).

-   <img alt="" src=images/Part_FaceColors.svg  style="width:32px;"> [Set colors](Part_FaceColors.md): assigns colors to part faces.

### Preferințe


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Std_DlgParameter.png  style="width:32px;"> [Preferences\...](PartDesign_Preferences.md): Preferințele sunt disponibile în Instrumente partDesign.


</div>

## Tutoriale


<div class="mw-translate-fuzzy">

-   [How to use FreeCAD](http://help-freecad-jpg87.fr/), a website describing the workflow for mechanical design.
-   [Creating a simple part with PartDesign v0.17](Creating_a_simple_part_with_PartDesign.md)
-   [Tutorial de proiectare a pieselor de baza 017](Basic_Part_Design_Tutorial_017.md)
-   [Tutorial PartDesign de Rulmenți I](PartDesign_Bearingholder_Tutorial_I.md) (are nevoie de actualizare)
-   [Tutorial PartDesign de Rulmenți II](PartDesign_Bearingholder_Tutorial_II.md) (are nevoie de actualizare)


</div>


<div class="mw-translate-fuzzy">





</div>


 {{PartDesign Tools navi}}

_

---
[documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > PartDesign Workbench/ro
