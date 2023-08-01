# Constructive solid geometry/de
## Einführung

[Konstruktive Festkörpergeometrie](https://de.wikipedia.org/wiki/Constructive_Solid_Geometry) (engl.: Constructive Solid Geometry) (**CSG**) ist ein Modellierungskonzept, das in vielen herkömmlichen CAD-Systemen verwendet wird. Es besteht im Wesentlichen darin, einfache Festkörperobjekte zu verwenden und mit ihnen boolesche Operationen wie Vereinigung (Verschmelzen), Differenz (Abziehen) und Schnitt (gemeinsamen Inhalt (Schnittmenge) ermitteln) durchzuführen, um eine endgültige Form zu erstellen.

In FreeCAD wird diese Methode hauptsächlich mit dem <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Arbeitsbereich Part](Part_Workbench/de.md) verwendet, der die Möglichkeit hat, einfache Grundkörper (Primitive) wie <img alt="" src=images/Part_Box.svg  style="width:24px;">[Würfel](Part_Box/de.md), <img alt="" src=images/Part_Cylinder.svg  style="width:24px;">[Zylinder](Part_Cylinder/de.md) und <img alt="" src=images/Part_Sphere.svg  style="width:24px;">[Kugel](Part_Sphere/de.md) zu erstellen und miteinander zu vereinigen, oder sie von anderen Objekten abzuziehen, mit Werkzeugen wie **<img src="images/Part_Cut.svg" width=24px> [Part Differenz](Part_Cut/de.md)**.

<img alt="" src=images/Part_Constructive_Solid_Geometry_workflow.svg  style="width:800px;">



* Arbeitsablauf zur konstruktiven Festkörpergeometrie (CSG); eine beliebige Anzahl von Operationen kann mit Grundkörpern (Festkörper-Primitive) durchgeführt werden, um andere Festkörperobjekte zu erzeugen und diese dann zu vereinigen oder abzuziehen, bis die endgültige Form erstellt ist.*

Der Arbeitsbereich [PartDesign](PartDesign_Workbench/de.md) verwendet einen moderneren Ansatz als einfaches CSG; diese Methode heißt [Bearbeitung mit Formelementen](feature_editing/de.md), was bedeutet, dass ein Basisfestkörper erstellt wird und dann aufeinanderfolgende parametrische Umwandlungen hinzugefügt werden, um den endgültigen Körper zu erhalten.


**Anmerkung:**

Ein [PartDesign Körper](PartDesign_Body/de.md), der mit dem Arbeitsbereich [PartDesign](PartDesign_Workbench/de.md) erstellt wurde, kann auch in einer boolschen Operation mit anderen Objekten verwendet werden.



## Beispiel

<img alt="" src=images/Part_CGS_workflow_example.svg  style="width:600px;">



* Beispiel für den Arbeitsablauf zur konstruktiven Festkörpergeometrie (CSG): Einfache Teile werden zusammengefügt (Vereinigung); das Schnittobjekt (das gemeinsame Volumen) zweier anderer einfacher Teile wird berechnet (Schnitt); die Differenz der beiden vorherigen Formen wird gebildet.*



## Tutorien

Die Seite [Tutorien](tutorials/de.md) stellt einige Beispiele zur Erstellung von Festkörpern mit dem Arbeitsbereich <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Part](Part_Workbench/de.md) bereit, die die **CSG**-Methode verwenden.

-   [Herkömmliche Modellierung, die CSG-Methode](Manual:Traditional_modeling,_the_CSG_way/de.md)
-   [Whiffleball Tutorium](Whiffle_Ball_tutorial/de.md)
-   [Grundlegendes Modellierungstutorial](Basic_modeling_tutorial/de.md)



---
![](images/Button_right.svg) [documentation index](../README.md) > [Common Questions](Category_Common Questions.md) > [Part](Category_Part.md) > Constructive solid geometry/de
