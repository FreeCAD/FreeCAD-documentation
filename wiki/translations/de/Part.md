

## Einleitung


{{TOCright}}

In FreeCAD wird das Wort \"[Part](Part/de.md)\" normalerweise verwendet, um auf eine <img alt="" src=images/Std_Part.svg  style="width:24px;"> [Std Teil](Std_Part/de.md)(`App::Part` Klasse) zu verweisen, ein Typ eines Containerobjekts, das durch das Basissystem definiert ist. Dieses Teil wird zur Verwaltung der Position von 3D Formen verwendet, um mechanische Baugruppen zu erstellen.

Siehe <img alt="" src=images/Std_Part.svg  style="width:24px;"> [Std Part](Std_Part/de.md) für weitere Informationen über diesen Objekttyp.

## Anwendung

Das Std Part Werkzeug wird nicht durch einen bestimmten Arbeitsbereich, sondern durch das Basissystem definiert, daher ist es in der {{MenuCommand/de|structure toolbar}} zu finden, die in allen [Arbeitsbereiche](Workbenches/de.md) verfügbar ist.

1.  Drücke die **<img src=images/Std_Part.svg style="width:16px"> [Std Part](Std_Part/de.md)** Taste. Ein leeres Part wird erzeugt und wird automatisch *[aktiv](Std_Part#Active_status/de.md)*.

## Hinweise

Im informellen Gebrauch kann ein *Part* jede geometrische Figur sein, die in der [3D Ansicht](3D_view/DE.md) sichtbar ist, und daher kann sein Konzept mit dem von \"[Körper](Body/DE.md)\" oder \"[Zusammenbau](Assembly/de.md)\" verwechselt werden.

Wenn jedoch mehr Präzision erforderlich ist, muss die Unterscheidung vorgenommen werden.

-   Ein \"[Körper](Body/de.md)\" wird für einzelne, aneinandergrenzende Elemente verwendet, die normalerweise mit den [Part](Part_Workbench/de.md) oder [PartDesign Arbeitsbereich](PartDesign_Workbench/de.md) erstellt werden.
    -   Ein \"Körper\" hat eine \"[Form](Shape/de.md)\".
-   Ein \"Teil\" wird verwendet, um einen einzelnen \"Körper\" oder mehrere von ihnen zu einer \"Baugruppe\" zu gruppieren.
    -   Ein \"Teil\" hat eine Sammlung von \"[Formen](Shape/de.md)\", aber keine eigene \"Form\".
-   Eine \"Baugruppe\" ist eine Sammlung von \"Teilen\", die auf irgendeine Weise, manuell oder unter Verwendung einer Montage-Arbeitsbereichs, angeordnet sind.


{{Std Base navi

}} {{Document objects navi}} 

[Category:Glossary{{\#translation:}}](Category:Glossary.md)
