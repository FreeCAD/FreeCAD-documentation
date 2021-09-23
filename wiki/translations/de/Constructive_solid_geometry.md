# Constructive solid geometry/de
 {{TOCright}}

## Einführung

[Konstruktive Festkörpergeometrie](https://de.wikipedia.org/wiki/Constructive_Solid_Geometry) (engl.: Constructive Solid Geometry) (**CSG**) ist ein Modellierungsparadigma, das in vielen herkömmlichen CAD Systemen verwendet wird. Es besteht im Wesentlichen darin, primitive Festkörperobjekte zu verwenden und mit ihnen boolesche Operationen wie Verschmelzung, Subtraktion und Verschneidung durchzuführen, um eine endgültige Form zu erzeugen.

In FreeCAD wird diese Methode hauptsächlich mit dem <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Arbeitsbereich Part](Part_Workbench/de.md) verwendet, der die Möglichkeit hat, Grundelementobjekte wie <img alt="" src=images/Part_Box.svg  style="width:24px;">[Kasten](Part_Box/de.md), <img alt="" src=images/Part_Cylinder.svg  style="width:24px;">[Zylinder](Part_Cylinder/de.md) und <img alt="" src=images/Part_Sphere.svg  style="width:24px;">[Kugel](Part_Sphere/de.md) zu erstellen und miteinander zu verschmelzen, oder sie zum Schneiden anderer Objekte mit Werkzeugen wie **<img src="images/Part_Cut.svg" width=24px> [Part Schneiden](Part_Cut/de.md)** zu verwenden.

<img alt="" src=images/Part_Constructive_Solid_Geometry_workflow.svg  style="width:800px;">


*Konstruktive Festkörpergeometrie (CSG) Arbeitsablauf; eine beliebige Anzahl von Operationen kann mit Volumenelementen durchgeführt werden, um andere Volumenobjekte zu erzeugen, und diese dann zu verschmelzen oder zu schneiden, bis die endgültige Form erzeugt wird.*

Der [PartDesign Arbeitsbereich](PartDesign_Workbench/de.md) verwendet einen moderneren Ansatz als einfaches CSG; diese Methode heißt [Formmerkmale bearbeiten](feature_editing/de.md), was bedeutet, dass ein Basisfestkörper erstellt und dann aufeinanderfolgende parametrische Umwandlungen hinzugefügt werden, um einen endgültigen Körper zu erhalten.


**Anmerkung:**

Ein [PartDesign Körper](PartDesign_Body/de.md), der mit dem [PartDesign Arbeitsbereich](PartDesign_Workbench/de.md) erstellt wurde, kann auch in einer boolschen Operation mit anderen Objekten verwendet werden.

## Beispiel

<img alt="" src=images/Part_CGS_workflow_example.svg  style="width:600px;">


* Beispiel für den Arbeitsablauf der konstruktiven Festkörpergeometrie (CSG): Basisteile werden verschmolzen (Vereinigung); der Schnittpunkt zweier anderer Basisteile wird berechnet (gemeinsam); die Differenz (Schnitt) der beiden vorherigen Formen wird erhalten.*

## Tutorien

Die [Tutorien](tutorials/de.md) Seite stellt einige Beispiele zur Erstellung von Festkörpern mit der <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Part Arbeitsbereich](Part_Workbench/de.md) bereit, die die **CSG** Methode verwenden.

-   [Herkömmliche Modellierung, die CSG Methode](Manual:Traditional_modeling,_the_CSG_way/de.md)
-   [Whiffleball Tutorium](Whiffle_Ball_tutorial/de.md)
-   [Grundlegendes Modellierungstutorial](Basic_modeling_tutorial/de.md)

 

[Category:Common Questions](Category:Common_Questions.md)
