# PartDesign Scaled/de
{{GuiCommand/de
|Name=PartDesign Scaled
|Name/de=PartDesign Skalieren
|Workbenches=[PartDesign](PartDesign_Workbench/de.md), Complete
|MenuLocation=PartDesign → MultiTransform
}}

## Einführung

\'Skalieren\' - dieser Werkzeug nimmt ein oder mehrere Features als Eingabe (die \"Originale\") und skaliert sie mit einem gegebenen Faktor. Weil um den Schwerpunkt der gewählten Features skaliert wird, verschwinden sie üblicherweise in den skalierten Versionen. Darum ist es normalerweise nur innerhalb einer Mehrfachtransformation sinnvoll zu skalieren.

Seit FreeCAD 0.15 ist diese Funktion nicht mehr direkt verfügbar, aber als Komponente [ MultiTransform](PartDesign_MultiTransform/de.md) enthalten

## Options

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




## Limitations

-   Scaling always happens with the centre of gravity of the feature as the base point.
-   A scaled transformation should not be the first in the list
-   The scaled transformation must have the same number of occurrences as the transformation immediately preceding it in the list
-   See [linear pattern feature](PartDesign_LinearPattern.md) for other limitations
-   See [MultiTransform](PartDesign_MultiTransform.md) for more details

## Examples

![c\|center\|800px](images/mt_example2.png ) The smallest pad was first patterned three times in X direction and then scaled to factor two (so the three occurrences have scaling factor 1.0, 1.5 and 2.0). Then a polar pattern was applied with 8 occurrences.

Since the scaling is done with respect to the center of gravity, in the case of a pad, it is necessary that the pad penetrate also in the main body, otherwise the scaled objects are floating, detached from the body. To have a pad that intersects the main body can be used \"two dimensions\" type or \"simmetric to plane\" option.

---
[documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Scaled/de
