---
- GuiCommand   */de
   Name   *FEM MaterialSolid
   Name/de   *FEM MaterialFeststoff
   MenuLocation   *Modell → Materiallien → Material für Feststoffe
   Workbenches   *[FEM](FEM_Workbench/de.md)
   Shortcut   ***M** **S**
   SeeAlso   *[FEM Tutorium](FEM_tutorial/de.md)
---

# FEM MaterialSolid/de

## Beschreibung

Fügt einem Teil Materialeigenschaften hinzu.

![](images/FEMMaterialSolidProperties.png ) 
*Der Aufgabenbereich FEM-Material*

## Anwendung

1.  Zur Erstellung eines neuen MaterialSolid-Objekts hat man folgende Möglichkeiten   *
    -   Die Schaltfläche **<img src="images/FEM_MaterialSolid.svg" width=16px> [FEM MaterialFeststoff](FEM_MaterialSolid/de.md)** drücken.
    -   Den Menüeintrag **Modell → Materialien → <img src="images/FEM_MaterialSolid.svg" width=16px> Material für Feststoffe** auswählen.
2.  Ein existierendes MaterialSolid-Objekt ändern   *
    -   Doppelklick auf das Objekt in der [Baumansicht](Tree_view/de.md).
3.  Der Aufgabenbereich FEM-Materialwird geöffnet.
4.  Ein Material auswählen. Für eine mechanische Analyse ist **CalculiX-Steel** eine passende Auswahl.
5.  Soll der Werkstoff dem gesamten Objekt zugeordnet werden, müssen keine geometrischen Elemente ausgewählt werden (die Referenzliste bleibt leer). Der Werkstoff wird dem gesamten Modell zugeordnet. Andernfalls weist man bestimmten Teilen des Modells manuell Werkstoffe zu, indem für jeden eingesetzten Werkstoff einige davon auswählt werden; es sollte am Ende aber kein Teil des Modells ohne zugewiesenen Werkstoff bleiben.
6.  Die Materialeigenschaften wie density (Dichte), young\'s modulus (Elastizitätsmodul), poisson ratio (Querkontraktionszahl) usw. können angepasst werden, dabei sind die gängigsten Werkstoffe schon in den Voreinstellungen vorhanden und brauchen keine Feinabstimmung.
7.  Wurden Einstellungen geändert, kann das angepasste Material gespeichert werden.
8.  Aut die Schaltfläche **OK** klicken, um den Aufgabenbereich zu schließen.

## Hinweise

1.  Der mechanische Werkstoff verwendet die \*MATERIAL Karte in CalculiX. Einzelheiten über den mechanischen Werkstoff werden unter <http   *//web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node216.html> erläutert.





{{FEM Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM MaterialSolid/de
