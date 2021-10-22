# Constructive solid geometry/de
{{TOCright}}

## Einführung

[Konstruktive Festkörpergeometrie](https://de.wikipedia.org/wiki/Constructive_Solid_Geometry) (engl.: Constructive Solid Geometry) (**CSG**) ist ein Modellierungsparadigma, das in vielen herkömmlichen CAD Systemen verwendet wird. Es besteht im Wesentlichen darin, primitive Festkörperobjekte zu verwenden und mit ihnen boolesche Operationen wie Verschmelzung, Subtraktion und Verschneidung durchzuführen, um eine endgültige Form zu erzeugen.

In FreeCAD wird diese Methode hauptsächlich mit dem <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> _, <img alt="" src=images/Part_Cylinder.svg  style="width:24px;">_ zu erstellen und miteinander zu verschmelzen, oder sie zum Schneiden anderer Objekte mit Werkzeugen wie **<img src="images/Part_Cut.svg" width=24px> [Part Schneiden](Part_Cut/de.md)** zu verwenden.

<img alt="" src=images/Part_Constructive_Solid_Geometry_workflow.svg  style="width:800px;">



*Konstruktive Festkörpergeometrie (CSG) Arbeitsablauf; eine beliebige Anzahl von Operationen kann mit Volumenelementen durchgeführt werden, um andere Volumenobjekte zu erzeugen, und diese dann zu verschmelzen oder zu schneiden, bis die endgültige Form erzeugt wird.*

Der [PartDesign Arbeitsbereich](PartDesign_Workbench/de.md) verwendet einen moderneren Ansatz als einfaches CSG; diese Methode heißt [Formmerkmale bearbeiten](feature_editing/de.md), was bedeutet, dass ein Basisfestkörper erstellt und dann aufeinanderfolgende parametrische Umwandlungen hinzugefügt werden, um einen endgültigen Körper zu erhalten.


**Anmerkung:**

Ein [PartDesign Körper](PartDesign_Body/de.md), der mit dem [PartDesign Arbeitsbereich](PartDesign_Workbench/de.md) erstellt wurde, kann auch in einer boolschen Operation mit anderen Objekten verwendet werden.

## Beispiel

<img alt="" src=images/Part_CGS_workflow_example.svg  style="width:600px;">



* Beispiel für den Arbeitsablauf der konstruktiven Festkörpergeometrie (CSG): Basisteile werden verschmolzen (Vereinigung); der Schnittpunkt zweier anderer Basisteile wird berechnet (gemeinsam); die Differenz (Schnitt) der beiden vorherigen Formen wird erhalten.*

## Tutorien

Die _ bereit, die die **CSG** Methode verwenden.

-   _
-   [Whiffleball Tutorium](Whiffle_Ball_tutorial/de.md)
-   [Grundlegendes Modellierungstutorial](Basic_modeling_tutorial/de.md)

 

_

---
[documentation index](../README.md) > [Common Questions](Category_Common Questions.md) > Constructive solid geometry/de
