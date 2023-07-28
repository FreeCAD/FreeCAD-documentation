---
- GuiCommand:/de
   Name:OpenSCAD ExplodeGroup
   Name/de:OpenSCAD GruppeSprengen
   MenuLocation:OpenSCAD → Sprenge Gruppe‏‎
   Workbenches:[OpenSCAD](OpenSCAD_Workbench/de.md)
---

# OpenSCAD ExplodeGroup/de



## Beschreibung

Diese Funktion sprengt eine Vereinigung oder einen Verbund zurück in einzelne Teile, wobei diesen Teilen zufällige Farben zugeordnet werden.



## Anwendung

1.  Zu sprengende(n) Vereinigung/Verbund auswählen.
2.  Auf <img alt="" src=images/OpenSCAD_ExplodeGroup.svg  style="width:32px;"> klicken oder den Menüeintrag ** OpenSCAD** → **<img src="images/OpenSCAD_ExplodeGroup.svg" width=32px> GruppeSprengen** auswählen.



## Begrenzungen

Die Funktion arbeitet nur mit Vereinigungen/Verbunden bestehend aus

-   Part-Grundelementen des Arbeitsbereichs Part
-   Extrudierten Teilen des Arbeitsbereichs Part
-   Gedrehten Teilen des Arbeitsbereichs Part

Die Funktion funktioniert **NICHT** bei

-   Aufpolsterungen/gedrehten Teilen des Arbeitsbereichs PartDesign
-   Anordnungen des Arbeitsbereichs Draft



## Hinweise

Um Anordnungen des Arbeitsbereichs Draft aufzulösen, wird das das Werkzeug [Draft Herabstufen](Draft_Downgrade/de.md) des Arbeitsbereichs Draft verwendet.





{{OpenSCAD_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [OpenSCAD](OpenSCAD_Workbench.md) > OpenSCAD ExplodeGroup/de
