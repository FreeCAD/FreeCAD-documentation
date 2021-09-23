---
- GuiCommand:/de
   Name:FEM WerkstoffVolumenkörper
   MenuLocation:Modell → FEM Werkstoff für Volumenkörper
   Workbenches:[FEM](FEM_Workbench/de.md)
   Shortcut:**M** **M**
   SeeAlso:[FEM Tutorium](FEM_tutorial/de.md)
---

# FEM MaterialSolid/de


</div>

## Beschreibung

Fügt Materialeigenschaften einem Teil hinzu.

![](images/FEMMaterialSolidProperties.png ) *The FEM material task panel*

## Anwendung


<div class="mw-translate-fuzzy">

-   Klicke auf <img alt="" src=images/FEM_MaterialSolid.png  style="width:32px;"> oder wähle **Model** → **<img src="images/FEM_MaterialSolid.png" width=32px> FEM Werkstoff für Volumenkörper** aus dem Hauptmenü.
-   Doppelklicke auf das erstellte **<img src="images/FEM_MaterialSolid.png" width=32px> VolumenkörperWerkstoff** Objekt

![](images/FEMMaterialSolidProperties.png )

-   -   Wähle einen Werkstoff aus. Für die ingenieurmechanische Analyse ist **CalculiX-Stahl** eine typische Option.
    -   Vorausgesetzt, dass du Werkstoffe auf das gesamte Objekt anwendest, wähle keine geometrischen Objekte aus (Referenzliste leer lassen). Der Werkstoff wird auf das gesamte Modell angewendet. Andernfalls weise bestimmten Modellteilen manuell Werkstoffe zu, indem du für jeden eingefügten Werkstoff einige davon auswählst, aber lasse keinen Teil des Modells ohne zugewiesenen Werkstoff.
    -   Du kannst Materialeigenschaften wie Dichte, Elastizitätsmodul, Poissonzahl usw. einstellen, jedoch sind die meisten der gebräuchlichen Materialien bereits in den Voreinstellungen verfügbar und müssen nicht angepasst werden.
    -   Wenn du Änderungen vornimmst, kannst du dein angepassten Werkstoff speichern.

-   Klicke **Close** um den Dialog zu schließen und erstelle**<img src="images/FEM_MaterialSolid.png" width=32px> VolumenkörperWerkstoff** Objekt


</div>

## Hinweise


<div class="mw-translate-fuzzy">

1.  Der mechanische Werkstoff verwendet die \*MATERIAL Karte in CalculiX. Einzelheiten über den mechanischen Werkstoff werden unter <http://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node216.html> erläutert.


</div>


<div class="mw-translate-fuzzy">





</div>


{{FEM Tools navi

}}

---
[documentation index](../README.md) > FEM MaterialSolid/de
