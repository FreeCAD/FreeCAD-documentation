# Copying Objects/de
{{TOCright}}

## Übersicht

Wie viele andere Computerprogramme hat auch FreeCAD die Möglichkeit, Objekte auszuschneiden, zu kopieren und einzufügen.[Dokument](Document_structure/de.md)-Objekte können innerhalb eines Dokuments oder zwischen Dokumenten frei kopiert werden, durch verwenden der Befehle <img alt="" src=images/Std_Copy.svg  style="width:24px;"> [Std Kopieren](Std_Copy.md), <img alt="" src=images/Std_Paste.svg  style="width:24px;"> [Std Einfügen](Std_Paste.md) und [Std AuswahlDuplizieren](Std_DuplicateSelection.md).

![](images/Copy_past_duplicate.png )

Bitte beachten, dass die kopiert und eingefügten Objekte nicht vom Original abhängig sind. Werden abhängige Klone gebraucht, sollte <img alt="" src=images/Draft_Clone.svg  style="width:24px;"> [Draft Klon](Draft_Clone/de.md) oder <img alt="" src=images/PartDesign_Clone.svg  style="width:24px;"> [PartDesign Klon](PartDesign_Clone/de.md) verwendet werden. Wird weder einen abhängiger Klon noch ein parametrisches Abbild gebraucht, kann auch <img alt="" src=images/Part_SimpleCopy.svg  style="width:24px;"> [Part Einfache Kopie](Part_SimpleCopy/de.md) verwendet werden. Für in Mustern angeordnete Klone siehe Abschnitt [Andere Methoden](Copying_Objects/de#Andere_Methoden.md) auf dieser Seite.

## Verknüpfte Objekte kopieren 

Wenn ein zu kopierendes Objekt Verweise auf Objekte besitzt, die nicht in der Auswahl sind, fragt FreeCAD, ob die nicht ausgewählten Objekte in den Kopiervorgang einbezogen werden sollen.

## Eingefügte Objekte finden und positionieren 

Nach einem Kopier- und Einfügevorgang ist es möglicherweise nicht offensichtlich, wo sich die neuen Objekte inder [3D-Ansicht](3D_view/de.md) befinden. Das liegt daran, dass die neuen Objekte die gleiche Eigenschaft [Placement](Placement/de.md) besitzen, wie ihre Originale. Die Eigenschaft Sichtbarkeit umgeschaltet (**Leertaste**), um die Originale auszublenden und dann die Kopien auf ihre richtige Position zu bewegen, z.B. mit <img alt="" src=images/Std_TransformManip.svg  style="width:24px;"> [Std Bewegen](Std_TransformManip/de.md) oder <img alt="" src=images/Std_Placement.svg  style="width:24px;"> [Std Positionierung](Std_Placement/de.md).

## Andere Methoden 

Wie bei den meisten Dingen in FreeCAD gibt es viele Möglichkeiten, eine Kopie zu erstellen. Für weitere Ideen siehe unter:

-   PartDesign: [Spiegeln](PartDesign_Mirrored/de.md), [Lineares Muster](PartDesign_LinearPattern/de.md), [Radiales Muster](PartDesign_PolarPattern/de.md), [Mehrfach-Transformation erstellen](PartDesign_MultiTransform/de.md)
-   Part: [Spiegelung](Part_Mirror/de.md), [Einfache Kopie erstellen](Part_SimpleCopy/de.md)
-   Draft: [Versetzen](Draft_Offset/de.md), [Skalieren](Draft_Scale/de.md), [AnordnungRechtwinklig](Draft_OrthoArray/de.md), [PfadAnordnen](Draft_PathArray/de.md), [Klonen](Draft_Clone/de.md), [Spiegeln](Draft_Mirror/de.md)



---
![](images/Button_right.svg) [documentation index](../README.md) > Copying Objects/de
