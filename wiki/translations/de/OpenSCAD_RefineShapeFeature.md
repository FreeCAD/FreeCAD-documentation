---
- GuiCommand:/de
   Name:OpenSCAD RefineShapeFeature
   Name/de:OpenSCAD FormelementAufbereiten
   MenuLocation:OpenSCAD → Formelement aufbereiten
   Workbenches:[OpenSCAD](OpenSCAD_Workbench/de.md)
---

# OpenSCAD RefineShapeFeature/de



## Beschreibung

Entfernt unnötige Linien. Nach einer Booleschen Operation bleiben einige Linien sichtbar, die zu den vorherigen Formen gehören. Dieses Werkzeug erstellt eine Kopie des Aufbereiteten Körpers.

![](images/PartRefineShape_it.png )



## Anwendung

1.  Die zu bereinigende Form auswählen.
2.  Den Menüeintrag **OpenSCAD → Formelement aufbereiten** auswählen.

-   Ein Eltern-Objekt wird erstellt und komplett aufbereitet, das Original-Objekt wird ausgeblendet gerendert.



## Einschränkungen

-   Der Aufbereitungsalgorithmus arbeitet nur mit Hüllflächen. Dazu iteriert er über die Hüllflächen der Eingangsform und erstellt für jede Hüllfläche eine neue Hüllfläche mit verbundenen Flächen, wo immer es möglich ist. Das bedeutet, wenn das ausgewählte Objekt nur eine Fläche, ein Kantenzug, eine Kante oder ein Punkt ist, macht der Algorithmus nichts.
-   Im Gegensatz zum <img alt="" src=images/Part_RefineShape.svg  style="width:24px;"> [Part FormAufbereiten](Part_RefineShape/de.md) im Arbeitsbereich <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Part](Part_Workbench/de.md) **wird** dieses Element aktualisiert, wenn sich die zugrundeliegenden Formen ändern.



## Hinweise

-   Die Funktion wird nicht die vorhandene Form verändern, sondern eine neue Form erstellen.
-   Die Funktion wird normalerweise als letzter Schritt im Modellierungsablauf verwendet.
-   Die Funktion kann helfen, schwierige Rundungen zu erstellen.
-   Die Funktion ist dafür gedacht, bei 3D-Druckern das Drucken unerwünschte Kanten zu vermeiden.





{{OpenSCAD_Tools_navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [OpenSCAD](OpenSCAD_Workbench.md) > OpenSCAD RefineShapeFeature/de
