---
- GuiCommand:/de
   Name:Assembly3 AddZYWorkplane
   Name/de:Assembly3 ZYArbeitsebeneHinzufügen
   Icon:Assembly_Add_WorkplaneZY.svg‎‎
   MenuLocation:Assembly3 → Workplane and origin → Add ZY workplane
   Workbenches:[Assembly3](Assembly3_Workbench/de.md)
---

# Assembly3 AddZYWorkplane/de

## Beschreibung

Der Befehl <img alt="" src=images/Assembly_Add_WorkplaneZY.svg  style="width:24px;"> [ZY-Arbeitsebene hinzufügen](Assembly3_AddZYWorkplane/de.md) fügt einer aktiven Baugruppe eine ZY-Arbeitsebene hinzu.

Ein Workplane-Objekt wird innerhalb des Parts-Containers des Baugruppenbaumes angelegt und die zugehörige Arbeitsebene in der 3D-Ansicht erstellt. Sie wird am Ursprung der Baugruppe platziert und entsprechend der YZ-Ebene der Baugruppe ausgerichtet, wenn die Baugruppe (das Assembly-Objekt) direkt ausgewählt wurde.

<img alt="" src=images/Assembly_Add_Workplane-01.png  style="width:250px;"> <img alt="" src=images/Assembly_AddZYWorkplane-04.png  style="width:350px;">

Die Baugruppe kann auch indirekt ausgewählt werden durch ein Bestandteil der Baugruppe. Dann wird die Arbeitsebene am Ursprung dieses Bestandteiles platziert wird aber noch immer entsprechend der YZ-Ebene der Baugruppe ausgerichtet.

Mögliche Bestandteile sind z. B. Elemente, Körper, Knoten, Kanten, Flächen, Ursprünge und andere Arbeitsebenen, entweder aus der [Baumansicht](Tree_view/de.md) oder aus der [3D-Ansicht](3D_view/de.md).

## Anwendung

1.  Den Befehl <img alt="" src=images/Assembly_Add_WorkplaneZY.svg  style="width:16px;"> **ZY-Arbeitsebene hinzufügen** aktivieren durch:
    -   Die Schaltfläche **<img src="images/Assembly_Add_WorkplaneZY.svg_" width=16px> [ZY-Arbeitsebene hinzufügen](Assembly3_AddZYWorkplane/de.md)**.
    -   Den Menüeintrag **Assembly3 → Workplane and origin → <img src="images/Assembly_Add_WorkplaneZY.svg_" width=16px> ZY-Arbeitsebene hinzufügen**.



---
![](images/Right_arrow.png) [documentation index](../README.md) > Assembly3 AddZYWorkplane/de
