---
- GuiCommand:/de
   Name:Assembly3 AddPlacement
   Name/de:Assembly3 BezugssystemHinzufügen
   Icon:Assembly_Add_Placement.svg‎‎
   MenuLocation:Assembly3 → Workplane and origin → Add placement
   Workbenches:[Assembly3](Assembly3_Workbench/de.md)
---

# Assembly3 AddPlacement/de

## Beschreibung

Der Befehl <img alt="" src=images/Assembly_Add_Placement.svg  style="width:24px;"> [Bezugssystem hinzufügen](Assembly3_AddPlacement/de.md) fügt einer aktiven Baugruppe ein Bezugssystem (Placement-Objekt) hinzu.

Ein Placement-Objekt wird innerhalb des Parts-Containers des Baugruppenbaumes angelegt und das zugehörige Bezugssystem in der 3D-Ansicht erstellt. Es wird am Ursprung der Baugruppe platziert und übernimmt die Ausrichtung des lokalen Koordinatensystems der Baugruppe, wenn die Baugruppe (das Assembly-Objekt) direkt ausgewählt wurde.

<img alt="" src=images/Assembly3_AddPlacement-01.png  style="width:250px;"> <img alt="" src=images/Assembly3_AddPlacement-02.png  style="width:350px;"> 
*Links: Baumansicht. Rechts: Ein Bezugssystem nahe dem Baugruppenursprung (hier als Dateiursprung dargestellt)*

Die Baugruppe kann auch indirekt ausgewählt werden durch ein Bestandteil der Baugruppe. Dann wird das Bezugssystem am Ursprung dieses Bestandteiles platziert und übernimmt die Ausrichtung seines lokalen Koordinatensystems.

Mögliche Bestandteile sind z. B. Elemente, Körper, Knoten, Kanten, Flächen, Ursprünge und Arbeitsebenen, entweder aus der [Baumansicht](Tree_view/de.md) oder aus der [3D-Ansicht](3D_view/de.md).

## Anwendung

1.  Den Befehl <img alt="" src=images/Assembly_Add_Placement.svg  style="width:16px;"> **Bezugssystem hinzufügen** aktivieren durch:
    -   Die Schaltfläche**<img src="images/Assembly_Add_Placement.svg_" width=16px> [ Bezugssystem hinzufügen](Assembly3_AddPlacement/de.md)**.
    -   Den Menüeintrag **Assembly3 → Workplane and origin → <img src="images/Assembly_Add_Placement.svg_" width=16px> Bezugssystem hinzufügen**.



---
![](images/Right_arrow.png) [documentation index](../README.md) > Assembly3 AddPlacement/de
