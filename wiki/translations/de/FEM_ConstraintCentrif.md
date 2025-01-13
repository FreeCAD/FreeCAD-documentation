---
 GuiCommand:Container|
{{GuiCommand/de
   Name: FEM ConstraintCentrif
   Name/de: FEM RandbedingungZentrif
   MenuLocation: Modell , Mechanische Randbedingungen und Lasten , Zentrifugale Last
   Workbenches: FEM_Workbench/de
   Shortcut: 
   Version: 0.20
   SeeAlso: 
}}
{{GuiCommandFemInfo/de
   Solvers: CalculiX
}}
---

# FEM ConstraintCentrif/de



## Beschreibung

Legt eine zentrifugale Last auf den Körper fest.



## Anwendung

1.  Es gibt mehrere Möglichkeiten den Befehl aufzurufen:
    -   Die Schaltfläche **<img src="images/FEM_ConstraintCentrif.svg" width=16px> [Zentrifugale Last](FEM_ConstraintCentrif/de.md)** drücken.
    -   Den Menüeintrag **Modell → Mechanische Randbedingungen und Belastungen → <img src="images/FEM_ConstraintCentrif.svg" width=16px> Zentrifugale Last** auswählen.
2.  Die Drehfrequenz in Hz eingeben.
3.  Die Schaltfläche **Hinzufügen** im Fenster **Geometriereferen-Auswahl für Solid** drücken und einen Festkörper auswählen, dem die Last in der [3D-Ansicht](3D_view/de.md) zugeordnet werden soll.
4.  Die Schaltfläche **Hinzufügen** im Fenster **Geometriereferen-Auswahl für Edge** klicken und eine Kante auswählen, um die die Drehung in der [3D-Ansicht](3D_view.md) erfolgen soll.



## Hinweise

-   Diese Funktion verwendet die [\* DLOAD-Karte in CalculiX](https://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node190.html).





{{FEM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > FEM ConstraintCentrif/de
