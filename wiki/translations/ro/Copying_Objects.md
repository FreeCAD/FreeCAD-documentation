# Copying Objects/ro
{{TOCright}}

## Overview


<div class="mw-translate-fuzzy">

## Descriere

Este o aplicație de duplicare a obiectelor (paragrafe, celule de calcul tabelar, imagini etc.) fiind prezentă în majoritatea aplicațiilor. FreeCAD nu este o excepție. [Document](Document_structure.md) pot fi copiate în mod liber într-un document sau între documente folosind comenzile [Copy](Std_Copy.md), [Paste](Std_Paste.md) și comenzile [Duplicate Selection](Std_DuplicateSelection.md) .

## Copierea Obiectelor legate între ele 

Obiectele [Document](Document_structure.md) pot fi legate de alte obiecte (de exemplu, o funcție Pad este legată de Sketch-ul său și o funcționalitate Fusion este legată de obiectele componente ale acestuia). Aceasta înseamnă că trebuie să fii atent atunci când alegi obiecte de copiat.


</div>

![](images/Copy_past_duplicate.png )

Please consider that the copy-pasted objects are not dependent on the original. If you want dependent clones please use <img alt="" src=images/Draft_Clone.svg  style="width:24px;"> [Draft Workbench\'s Clone](Draft_Clone.md) or <img alt="" src=images/PartDesign_Clone.svg  style="width:24px;"> [Part Design Workbench\'s Clone](PartDesign_Clone.md). If you need neither a dependent clone nor a parametric replica, you may also use <img alt="" src=images/Part_SimpleCopy.svg  style="width:24px;"> [ Part Workbench\'s Simple Copy](Part_SimpleCopy.md). For patterned clones, please look into the [ Other Methods section](Copying_Objects#Other_Methods.md) of this page.

## Copying Linked Objects 

If an object to be copied has links to object(s) not in the selection, FreeCAD will ask if the unselected objects should be included in the copy operation.

## Finding and Positioning Pasted Object(s) 


<div class="mw-translate-fuzzy">

În general, practica recomandată este selectarea tuturor obiectelor dependente/copii atunci când se copiază un obiect părinte.

## Găsirea și Poziționarea Obiect(ului)elor Pasted 

After the Copy/Paste operation, it may not be obvious where the new object(s) are located in the Document window. That is because the new object has the same [Placement](Placement.md) property as the original. comutați proprietatea Vizibilitate (bara de spațiu) pentru a ascunde originalul. Apoi utilizați dialogul de plasare pentru a muta copia în poziția corectă.


</div>

## Other Methods 


<div class="mw-translate-fuzzy">

## Alte Metode 

Ca multe lucruri în FreeCAD, există multe modalități de a face o copie. Pentru mai multe idei, uitați-vă la:

-   PartDesign: [Mirror](PartDesign_Mirrored.md), [Linear Pattern](PartDesign_LinearPattern.md), [Polar Pattern](PartDesign_PolarPattern.md), [MultiTransform](PartDesign_MultiTransform.md)
-   Part: [Mirror](Part_Mirror.md), [Simple copy](Part_SimpleCopy.md)
-   Draft: [Offset](Draft_Offset.md), [Scale](Draft_Scale.md), [Array](Draft_Array.md), [PathArray](Draft_PathArray.md), [Clone](Draft_Clone.md), [Mirror](Draft_Mirror.md)

## Notă

-   În vesiunile ulterioare lui v0.14+, dacă un obiect care urmează să fie copiat are legături către obiecte care nu sunt în selecție, FreeCAD va întreba dacă obiectele neselectate ar trebui să fie incluse în operația de copiere.


</div>



---
![](images/Button_right.svg) [documentation index](../README.md) > Copying Objects/ro
