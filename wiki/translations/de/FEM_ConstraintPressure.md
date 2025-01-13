---
 GuiCommand:Container|
{{GuiCommand/de
   Name: FEM ConstraintPressure
   Name/de: FEM RandbedingungDruck
   MenuLocation: Modell , Mechanische Randbedingungen und Belastungen , Druckbelastung
   Workbenches: FEM_Workbench/de
   SeeAlso: FEM_ConstraintForce/de
}}
{{GuiCommandFemInfo/de
   Solvers: CalculiX, Elmer
}}
---

# FEM ConstraintPressure/de



## Beschreibung

Wendet eine Drucklast (Flächenpressung) auf eine Fläche an.



## Anwendung

1.  Es gibt mehrere Möglichkeiten, den Befehl aufzurufen:
    -   Die Schaltfläche **<img src="images/FEM_ConstraintPressure.svg" width=16px> [Druckbelastung](FEM_ConstraintPressure/de.md)** drücken.
    -   Den Menüeintrag **Modell → Mechanische Randbedingungen und Belastungen → <img src="images/FEM_ConstraintPressure.svg" width=16px> Druckbelastung** auswählen.
2.  Die Schaltfläche **Hinzufügen** drücken und Flächen in der [3D-Ansicht](3D_view/de.md) auswählen. Wahlweise die Schaltfläche **Entfernen** drücken und die Flächen anklicken, die aus der Auswahl entfernt werden sollen.
3.  Die Druckbelastung in MPa im entsprechenden Fenster eingeben.
4.  Falls erforderlich, die Checkbox Richtung umkehren aktivieren, um die Wirkrichtung umzukehren.



## Hinweise

-   Die Verteilung des Drucks auf eine Fläche ist immer gleichmäßig und immer rechtwinklig zur Fläche.

-    {{VersionMinus/de|0.21}}: Eine Druckbelastung kann auf Hüllen (shells) angewendet werden, aber nur wenn [Gmsh](FEM_MeshGmshFromShape/de.md) zum Vernetzen verwendet wird und group meshing auf true gesetzt ist. Es ist dauerhaft als true codiert, so dass der Benutzer sich nicht darum kümmern muss. Aber aufgrund eines Fehlers kann Druckbelastung ein erneutes Vernetzen erfordern, um auf Hüllen zu funktionieren.

-   Diese Funktion verwendet die [\*DLOAD-Karte in CalculiX](https://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node190.html).





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ConstraintPressure/de
