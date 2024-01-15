---
 GuiCommand:
   Name: FEM ConstraintFixed
   Name/de: FEM RandbedingungFestsetzen
   MenuLocation: Modell , Mechanische Randbedingungen und Belastungen , Randbedingung Festsetzen
   Workbenches: FEM_Workbench/de
   SeeAlso: FEM_ConstraintContact/de
---

# FEM ConstraintFixed/de



## Beschreibung

Erstellt eine FEM-Randbedingung zum Festsetzen einer geometrischen Einheit, die alle vorhandenen Freiheitsgrade der Knoten sperrt, die der ausgewählten geometrischen Einheit zugrunde liegen (6 Freiheitsgrade für Balken- und Schalenelemente, 3 für Festkörper-Elemente).



## Anwendung

1.  Es gibt mehrere Möglichkeiten den Befehl aufzurufen:
    -   Die Schaltfläche **<img src="images/FEM_ConstraintFixed.svg" width=16px> [Randbedingung Festsetzen](FEM_ConstraintFixed/de.md)** drücken.
    -   Den Menüeintrag **Modell → Mechanische Randbedingungen und Belastungen → <img src="images/FEM_ConstraintFixed.svg" width=16px> Randbedingung Festsetzen** auswählen.
2.  In der [3D-Ansicht](3D_view/de.md) das Objekt auswählen, dem die Randbedingung zugeordnet werden soll; dies kann ein Knoten (Ecke), eine Kante oder eine Fläche sein.



## Begrenzungen

Objektarten können innerhalb derselben Randbedingung nicht gemischt werden. Für jede Objektart sollte eine eigene Randbedingung Festsetzen verwendet werden.





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ConstraintFixed/de
