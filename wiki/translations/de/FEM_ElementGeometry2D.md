---
 GuiCommand:Container|
{{GuiCommand/de
   Name: FEM ElementGeometry2D
   Name/de: FEM ElementGeometrie2D
   MenuLocation: Modell , Element-Geometrie , Schalendicke
   Workbenches: FEM_Workbench/de
   Shortcut: **C** **S**
   SeeAlso: FEM_tutorial/de
}}
{{GuiCommandFemInfo/de
   Solvers: Alle
}}
---

# FEM ElementGeometry2D/de



## Beschreibung

Ein **ElementGeometry2D**-Objekt wird zum Festlegen der Wandstärke von 2D-FEM-Elementen (Schalenelemente und {{Version/de|1.0}}: ebene Spannungs-/Belastungselemente) verwendet; für alle oder nur diejenigen, die auf der ausgewählten Oberfläche liegen.



## Anwendung

1.  Es gibt mehrere Möglichkeiten, den Befehl aufzurufen:
    -   Die Schaltfläche **<img src="images/FEM_ElementGeometry2D.svg" width=16px> [Schalendicke](FEM_ElementGeometry2D/de.md)** drücken.
    -   Den Menüeintrag **Modell → Element-Geometrie → <img src="images/FEM_ElementGeometry2D.svg" width=16px> Schalendicke** auswählen.
2.  Die Schalendicke festlegen.
3.  Wahlweise die Schaltfläche **Hinzufügen** im Aufgabenbereich drücken und danach auf die Fläche klicken, die eine voreingestellte Wandstärke erhalten soll. Wenn die Flächenauswahl leer ist, werden automatisch alle übrigen Flächen zugeordnet (deren Wandstärke nicht durch andere [ElementGeometry2D](FEM_ElementGeometry2D/de.md)-Objekte festgelegt ist).



## Einschränkungen

-   Zurzeit werden Analysen, die Schalenelemente mit Festkörper- oder Kantenelementen kombinieren, nicht unterstützt.



## Eigenschaften


**Thickness**

: Legt die Wandstärke der 2D-Elemente fest.



## Hinweise

-   Zum Betrachten der Ergebnisse des Lösers CalculiX aus dem auf die vorgegebene Wandstärke erweiterten Netz muss die Eigenschaft `Beam Shell Result Output 3D` des [FEM LöserCalculixCxxtools](FEM_SolverCalculixCxxtools/de.md)-Objekts auf `True` gesetzt werden.
-   Diese Funktion verwendet die [\*SHELL SECTION-Karte in CalculiX](https://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node238.html) für Schalenelemente und die [\*SOLID SECTION-Karte](https://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node239.html) für ebene Spannungs-/Belastungselemente.





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ElementGeometry2D/de
