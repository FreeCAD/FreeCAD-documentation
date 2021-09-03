---
- GuiCommand:   Name:PartDesign Scaled   Workbenches:[[PartDesign Workbench   PartDesign]], Complete|MenuLocation:PartDesign → MultiTransform---


</div>


<div class="mw-translate-fuzzy">

## Introducere

\'Scale features\' - This tool takes a set of one or more selected features as its input (the \'originals\'), and scales them by a given factor. Since the scaling takes place around the centre of gravity of the selected features, they usually disappear inside the scaled versions. Therefore, normally it is only useful to use scaling as part of the MultiTransform feature.


</div>

\'Scale features\' - This tool takes a set of one or more selected features as its input (the \'originals\'), and scales them by a given factor. Since the scaling takes place around the centre of gravity of the selected features, they usually disappear inside the scaled versions. Therefore, normally it is only useful to use scaling as part of the MultiTransform feature.


<div class="mw-translate-fuzzy">

## Notă

De la FreeCAD 0.15, această funcție nu este valabilă direct, dar este inclusă ca o componentă [MultiTransform](PartDesign_MultiTransform.md).


</div>

## Opțiuni

+----------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
| ![](images/Scaled_parameters.png ) | When creating a scaled feature, the \'scaled parameters\' dialogue offers the following options:                                             |
|                                                    |                                                                                                                                              |
|                                                    | ### Select originals                                                                                                      |
|                                                    |                                                                                                                                              |
|                                                    | The list view shows the \'originals\', the features that are to be scaled. Clicking on any feature will add it to the list.                  |
|                                                    |                                                                                                                                              |
|                                                    | ### Factor and Occurrences                                                                                          |
|                                                    |                                                                                                                                              |
|                                                    | Specifies the maximum factor which the features are to be scaled to, and the total number of scaled shapes (including the original feature). |
+----------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+




## Limitări

-   Scaling always happens with the centre of gravity of the feature as the base point.
-   A scaled transformation should not be the first in the list
-   The scaled transformation must have the same number of occurrences as the transformation immediately preceding it in the list
-   See [linear pattern feature](PartDesign_LinearPattern.md) for other limitations
-   See [MultiTransform](PartDesign_MultiTransform.md) for more details

## Exemple

![c\|center\|800px](images/mt_example2.png ) The smallest pad was first patterned three times in X direction and then scaled to factor two (so the three occurrences have scaling factor 1.0, 1.5 and 2.0). Then a polar pattern was applied with 8 occurrences.

Deoarece scalarea se face în raport cu centrul de greutate, în cazul unui bosaj, este necesar ca bosajul să pătrundă și în corpul principal, în caz contrar obiectele scalate sunt plutitoare, detașate de corp. Pentru a avea un bosaj care intersectează corpul principal, se poate utiliza opțiunea \"două dimensiuni\" sau opțiunea \"simetric la plan\". 
