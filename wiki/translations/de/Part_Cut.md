---
 GuiCommand:
   Name: Part Cut
   Name/de: Part Differenz
   MenuLocation: Part , Boolesche Verknüpfungen , Differenz
   Workbenches: Part_Workbench/de
   SeeAlso: Part_Boolean/de, Part_Fuse/de, Part_Common/de
---

# Part Cut/de



## Beschreibung

Das Werkzeug <img alt="" src=images/Part_Cut.svg  style="width:24px;"> **Part Differenz** beschneidet ausgewählte Part-Objekte, wobei das zuletzt ausgewählte vom ersten abgezogen (subtrahiert) wird. Diese Operation ist voll parametrisch und die Komponenten können modifiziert und das Ergebnis neu berechnet werden.

Dieses Werkzeug ist eine automatisierte Form der <img alt="" src=images/Part_Booleans.svg  style="width:24px;"> [Booleschen Verknüpfung](Part_Boolean/de.md).

<img alt="" src=images/Part_Cut_01.png  style="width:480px;">



## Anwendung

1.  Zwei Formen auswählen
2.  Es gibt mehrere Möglichkeiten, den Befehl aufzurufen:
    -   Die Schaltfläche **<img src="images/Part_Cut.svg" width=16px> [Differenz](Part_Cut/de.md)** drücken
    -   Den Menüeintrag **Part → Boolesche Verknüpfung → <img src="images/Part_Cut.svg" width=16px> Differenz** auswählen.



## Unterstützte Eingaben 

Eingabeobjekte müssen [OpenCASCADE](OpenCASCADE/de.md)-Formen sein. Zum Beispiel Objekte die mit den Arbeitsbereichen Part, PartDesign oder Sketcher erstellt wurden. Für Polygonnetze gibt es eigene boolesche Werkzeuge im Arbeitsbereich [Mesh](Mesh_Workbench/de.md).





{{Part_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Cut/de
