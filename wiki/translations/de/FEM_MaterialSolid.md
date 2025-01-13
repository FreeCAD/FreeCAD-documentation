---
 GuiCommand:Container|
{{GuiCommand/de
   Name: FEM MaterialSolid
   Name/de: FEM MaterialFeststoff
   MenuLocation: Modell , Materiallien , Material für Feststoffe
   Workbenches: FEM_Workbench/de
   Shortcut: **M** **S**
   SeeAlso: FEM_tutorial/de
}}
{{GuiCommandFemInfo/de
   Solvers: Alle
}}
---

# FEM MaterialSolid/de



## Beschreibung

Erstellt ein Material für Festkörper.

![](images/FEMMaterialSolidProperties.png ) 
*Der Aufgabenbereich FEM-Material*



## Anwendung

1.  Zum Erstellen eines neuen MaterialSolid-Objekts hat man folgende Möglichkeiten:
    -   Die Schaltfläche **<img src="images/FEM_MaterialSolid.svg" width=16px> [Material für Festkörper](FEM_MaterialSolid/de.md)** drücken.
    -   Den Menüeintrag **Modell → Materialien → <img src="images/FEM_MaterialSolid.svg" width=16px> Material für Festkörper** auswählen.
2.  Ein existierendes MaterialSolid-Objekt ändern:
    -   Doppelklick auf das Objekt in der [Baumansicht](Tree_view/de.md).
3.  Das Aufgaben-Fenster FEM-Material wird geöffnet.
4.  Ein Material in der Ausklappliste auswählen. Für eine mechanische Analyse ist **CalculiX-Steel** eine passende Auswahl.
5.  Wahlweise die Checkbox **Diesen Aufgabenbereich benutzen** aktivieren, um Materialeigenschaften, wie Dichte, Elastizitätsmodul, Poissonzahl, usw. anzupassen.
6.  Soll der Werkstoff dem gesamten Objekt zugeordnet werden, dürfen keine geometrischen Elemente ausgewählt werden (die Referenzliste bleibt leer). Das Material wird dem gesamten Modell zugeordnet. Andernfalls weist man ausgewählten Bereichen manuell das Material zu, indem für jeden eingesetzten Werkstoff einige davon auswählt werden; es sollte am Ende aber kein Teil des Modells ohne zugewiesenes Material bleiben.
7.  Aut die Schaltfläche **OK** klicken, um das Aufgaben-Fenster zu schließen.



## Hinweise

-   Der mechanische Werkstoff verwendet die [\*MATERIAL-Karte in CalculiX](http://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node216.html).





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM MaterialSolid/de
