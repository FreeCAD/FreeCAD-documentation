# <img alt="PartDesign workbench icon" src=images/Workbench_PartDesign.svg  style="width:64px;"> PartDesign Workbench/ro




## Introduction


<div class="mw-translate-fuzzy">

## Introducere

\"Atelierul Part Design\" oferă instrumente avansate pentru modelarea componentelor solide complexe și se bazează pe o metodă de [feature-editing methodology](#Feature_Editing_Methodology.md). Se concentrează în cea mai mare parte pe, dar nu se limitează la, crearea de piese mecanice. Este strâns legată de [Sketcher Workbench](Sketcher_Workbench.md).


</div>


<div class="mw-translate-fuzzy">

În timp ce [Part Workbench](Part_Workbench.md) se bazează pe o metodologie [constructive solid geometry](https://en.wikipedia.org/wiki/Constructive_solid_geometry) (CSG) pentru forme de construcție, Atelierul de lucru PartDesign utilizează o editare parametrică, ceea ce înseamnă că un solid de bază este transformat secvențial prin adăugarea de caracteristici deasupra până la obținerea formei finale. Consultați pagina [feature editing](feature_editing.md) pentru o explicație mai completă a acestui proces și apoi a se vedea [Creating a simple part with PartDesign](Creating_a_simple_part_with_PartDesign.md) pentru a începe să creați solide.


</div>

See the [feature editing](Feature_editing.md) page for a more complete explanation of this process, and then see [Creating a simple component with PartDesign](Creating_a_simple_part_with_PartDesign.md) to get started with creating solids.

The <img alt="" src=images/Workbench_Part.svg  style="width:16px;"> [Part Workbench](Part_Workbench.md) provides an alternative [constructive solid geometry](constructive_solid_geometry.md) (CSG) methodology for building shapes. For a detailed discussion of the Part Workbench versus the Part Design Workbench see [Part and Part Design](Part_and_PartDesign.md).

![](images/PartDesign_Workbench_Example.jpg )



## Instrumente


<div class="mw-translate-fuzzy">

Instrumentele de proiectare a componentelor sunt amplasate în meniul **Design Part** și în bara de instrumente PartDesign care apare atunci când încărcați atelierul Part Design.


</div>



### Instrumente Help pentru Part Design 


<div class="mw-translate-fuzzy">

-   ![ 32px](images/_PartDesign_Body.png ) [ Create body](PartDesign_Body/ro.md): Creează un corp în documentul activ și îl activează.


</div>

-   <img alt="" src=images/PartDesign_NewSketch.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Create Sketch:


<div class="mw-translate-fuzzy">

-   ![ 32px](images/_PartDesign_NewSketch.png ) [ Creare schiță](PartDesign_NewSketch.md): creează o schiță nouă pe o față sau pe un plane selectat. Dacă nu este selectată nicio față în timp ce această unealtă este executată, utilizatorul este chemat să selecteze un plan din panoul Activități. Interfața trece apoi în modul [ Sketcher_Workbench](Sketcher_Workbench.md) în modul de editare a schițelor.


</div>


<div class="mw-translate-fuzzy">

-   ![ 32px](images/_Sketcher_MapSketch.png ) [Mapează o schiță pe o fațetă ](Sketcher_MapSketch.md): Mapează o schiță pe un plan selectat anterior sau o fațetă a corpului activ.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_EditSketch.png  style="width:32px;"> [Edit sketch](Sketcher_EditSketch.md): Editează Sketch selectat.


</div>

-   <img alt="" src=images/Sketcher_ValidateSketch.svg  style="width:32px;"> [Validate sketch](Sketcher_ValidateSketch.md): verifies the tolerance of different points and adjusts them.

-   <img alt="" src=images/Part_CheckGeometry.svg  style="width:32px;"> [Check geometry](Part_CheckGeometry.md): Checks the geometry of selected objects for errors.

-   <img alt="" src=images/PartDesign_ShapeBinder.svg  style="width:32px;"> [Create a shape binder](PartDesign_ShapeBinder.md): creates a shape binder referencing geometry from a single parent object.

-   <img alt="" src=images/PartDesign_SubShapeBinder.svg  style="width:32px;"> [Create a sub-object(s) shape binder](PartDesign_SubShapeBinder.md): creates a shape binder referencing geometry from one or more parent objects.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/PartDesign_Clone.png  style="width:32px;"> [Create a clone](PartDesign_Clone.md): creează o clonă a corpului selectat.


</div>

-   <img alt="" src=images/PartDesign_Plane.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Create a datum (


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/PartDesign_Plane.png  style="width:32px;"> [Create a datum plane](PartDesign_Plane.md): creează un plan de referință în corpul activ.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/PartDesign_Line.png  style="width:32px;"> [Create a datum line](PartDesign_Line.md): creează o linie de referință în corpul activ.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/PartDesign_Point.png  style="width:32px;"> [Create a datum point](PartDesign_Point.md): creează un punct de referință în corpul activ.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/PartDesign_CoordinateSystem.png  style="width:32px;"> [Create a local coordinate system](PartDesign_CoordinateSystem.md): creează un sistem de coordonate local atașat la referința geometrică în corpul activ.


</div>


:   
    <small>(v1.1)</small> : these tools have been replaced by new [datum tools](Std_Base#Part_Datums.md).

### Part Design Modeling tools 



#### Instrumente Aditive 


<div class="mw-translate-fuzzy">

Acestea sunt instrumente pentru crearea de caracteristici de bază sau adăugarea de materiale unui corp solid existent.


</div>


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

-   <img alt="" src=images/PartDesign_AdditiveHelix.svg  style="width:32px;"> [Additive helix](PartDesign_AdditiveHelix.md): creates a solid by sweeping a sketch along a helix.

-   <img alt="" src=images/PartDesign_AdditiveBox.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Create an additive primitive:


<div class="mw-translate-fuzzy">

  -<img alt="" src=images/PartDesign_AdditiveBox.png  style="width:32px;"> [Additive box](PartDesign_AdditiveBox.md): creează un paralelipiped aditiv.


</div>


<div class="mw-translate-fuzzy">

  -<img alt="" src=images/PartDesign_AdditiveCylinder.png  style="width:32px;"> [Additive cylinder](PartDesign_AdditiveCylinder.md): creează un cilindru aditiv.


</div>


<div class="mw-translate-fuzzy">

  -<img alt="" src=images/PartDesign_AdditiveSphere.png  style="width:32px;"> [Additive sphere](PartDesign_AdditiveSphere.md): creează o sferă aditivă.


</div>


<div class="mw-translate-fuzzy">

  -<img alt="" src=images/PartDesign_AdditiveCone.png  style="width:32px;"> [Additive cone](PartDesign_AdditiveCone.md): creează un con aditiv.


</div>


<div class="mw-translate-fuzzy">

  -<img alt="" src=images/PartDesign_AdditiveEllipsoid.png  style="width:32px;"> [Additive ellipsoid](PartDesign_AdditiveEllipsoid.md): creează un elipsoid aditiv.


</div>


<div class="mw-translate-fuzzy">

  -<img alt="" src=images/PartDesign_AdditiveTorus.png  style="width:32px;"> [Additive torus](PartDesign_AdditiveTorus.md): creează un tor aditiv.


</div>


<div class="mw-translate-fuzzy">

  -<img alt="" src=images/PartDesign_AdditivePrism.png  style="width:32px;"> [Additive prism](PartDesign_AdditivePrism.md): creează o prismă aditivă.


</div>


<div class="mw-translate-fuzzy">

  -<img alt="" src=images/PartDesign_AdditiveWedge.png  style="width:32px;"> [Additive wedge](PartDesign_AdditiveWedge.md): creează o pană aditivă.


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

-   <img alt="" src=images/PartDesign_SubtractiveHelix.svg  style="width:32px;"> [Subtractive helix](PartDesign_SubtractiveHelix.md): creates a solid shape by sweeping a sketch along a helix and subtracts it from the active body.

-   <img alt="" src=images/PartDesign_SubtractiveBox.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Create a subtractive primitive:


<div class="mw-translate-fuzzy">

  -<img alt="" src=images/PartDesign_SubtractiveBox.png  style="width:32px;"> [Subtractive box](PartDesign_SubtractiveBox.md): adaugă un paralelipiped substractiv la corpul activ.


</div>


<div class="mw-translate-fuzzy">

  -<img alt="" src=images/PartDesign_SubtractiveCylinder.png  style="width:32px;"> [Subtractive cylinder](PartDesign_SubtractiveCylinder.md): adaugă un cilindru substractiv la corpul activ.


</div>


<div class="mw-translate-fuzzy">

  -<img alt="" src=images/PartDesign_SubtractiveSphere.png  style="width:32px;"> [Subtractive sphere](PartDesign_SubtractiveSphere.md): adaugă o sferă substractivă la corpul activ.


</div>


<div class="mw-translate-fuzzy">

  -<img alt="" src=images/PartDesign_SubtractiveCone.png  style="width:32px;"> [Subtractive cone](PartDesign_SubtractiveCone.md): adaugă un con subtractiv la corpul activ.


</div>


<div class="mw-translate-fuzzy">

  -<img alt="" src=images/PartDesign_SubtractiveEllipsoid.png  style="width:32px;"> [Subtractive ellipsoid](PartDesign_SubtractiveEllipsoid.md): adaugă un elipsoid substractiv la corpul activ.


</div>


<div class="mw-translate-fuzzy">

  -<img alt="" src=images/PartDesign_SubtractiveTorus.png  style="width:32px;"> [Subtractive torus](PartDesign_SubtractiveTorus.md): adaugă un tor substractiv la corpul activ.


</div>


<div class="mw-translate-fuzzy">

  -<img alt="" src=images/PartDesign_SubtractivePrism.png  style="width:32px;"> [Subtractive prism](PartDesign_SubtractivePrism.md): adaugă o prismă substractivă la corpul activ.


</div>


<div class="mw-translate-fuzzy">

  -<img alt="" src=images/PartDesign_SubtractiveWedge.png  style="width:32px;"> ‎[Subtractive wedge](PartDesign_SubtractiveWedge.md): adaugă o pană substractivă la corpul activ.


</div>

#### Boolean


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/PartDesign_Boolean.png  style="width:32px;"> [Boolean operation](PartDesign_Boolean.md): importă unul sau mai multe Corpuri sau Clone PartDesign în corpul activ și le aplică o operație booleană.


</div>




<div class="mw-translate-fuzzy">

#### Instrumente pentru traiectorie suplimentară 


</div>


<div class="mw-translate-fuzzy">

Aceste instrumente se aplică tratării marginilor sau fațetelor selectate.


</div>


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




<div class="mw-translate-fuzzy">

#### instrumente de Transformare 


</div>


<div class="mw-translate-fuzzy">

Acestea sunt instrumente pentru transformarea caracteristicilor existente. Acestea vă vor permite să alegeți caracteristicile care trebuie transformate.


</div>


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



#### Suplimentar

Unele funcționalități suplimentare găsite în meniul PartDesign:

-   <img alt="" src=images/PartDesign_Sprocket.svg  style="width:32px;"> [Sprocket](PartDesign_Sprocket.md): creates a sprocket profile that can be padded.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/PartDesign_InternalExternalGear.png  style="width:32px;"> [Involute gear](PartDesign_InvoluteGear.md):creează un profil de angrenaj cu profil în evolventă care poate fi utilizat de un PAD.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/PartDesign_WizardShaft.png  style="width:32px;"> [Shaft design wizard](PartDesign_WizardShaft.md): Generă un arbore dintr-o tabelă de valori și permite analizarea forțelor și momentelor. Arborele este realizat cu o schiță de revoluție care poate fi editată.


</div>




<div class="mw-translate-fuzzy">

### Meniu Contextual de Instrumente 


</div>

-   [Suppressed](PartDesign_Suppressed.md): checkbox to disable a specific feature without deleting it. <small>(v1.0)</small> 

-   <img alt="" src=images/PartDesign_MoveTip.svg  style="width:32px;"> [Set tip](PartDesign_MoveTip.md): redefines the tip, which is the feature exposed outside of the Body.

-   <img alt="" src=images/PartDesign_MoveFeature.svg  style="width:32px;"> [Move object to other body](PartDesign_MoveFeature.md): moves the selected sketch, datum geometry or feature to another Body.

-   <img alt="" src=images/PartDesign_MoveFeatureInTree.svg  style="width:32px;"> [Move object after other object](PartDesign_MoveFeatureInTree.md): allows reordering of the Body tree by moving the selected sketch, datum geometry or feature to another position in the list of features.




<div class="mw-translate-fuzzy">

-   <img alt="" src=images/PartDesign_MoveTip.png  style="width:32px;"> [Set tip](PartDesign_MoveTip.md): redefinește vârful, care este caracteristica expusă în afara corpului.


</div>

-   <img alt="" src=images/Std_SetAppearance.svg  style="width:32px;"> [Appearance](Std_SetAppearance.md): determines appearance of the whole part (color transparency etc.).

-   <img alt="" src=images/Part_ColorPerFace.svg  style="width:32px;"> [Color per face](Part_ColorPerFace.md): Assigns colors to individual faces of objects.

### Obsolete tools 

-   <img alt="" src=images/PartDesign_Migrate.svg  style="width:32px;"> [Migrate](PartDesign_Migrate.md): migrates files from FreeCAD versions below 0.17 to version 0.17. This tool is not available in <small>(v1.0)</small> .




<div class="mw-translate-fuzzy">

### Preferințe


</div>


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

## Examples

For some ideas of what can be achieved with Part Design tools, have a look at: [PartDesign examples](PartDesign_Examples.md).

<img alt="" src=images/PartDesign_ExampleSphere-02.png  style="width:80px;"> <img alt="" src=images/PartDesign_ExampleTorus-01.png  style="width:80px;"> <img alt="" src=images/PartDesign_ExamplePad-09.png  style="width:80px;"> <img alt="" src=images/PartDesign_ExampleSweep-02.png  style="width:80px;"> <img alt="" src=images/PartDesign_ExampleSweep-05.png  style="width:80px;"> <img alt="" src=images/PartDesign_ExampleSpring-04.png  style="width:80px;">


<div class="mw-translate-fuzzy">





</div>


 {{PartDesign_Tools_navi}}



---
⏵ [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > [PartDesign](Category_PartDesign.md) > PartDesign Workbench/ro
