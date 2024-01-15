---
 GuiCommand:
   Name: FEM ElementGeometry2D
   Name/de: FEM ElementGeometrie2D
   MenuLocation: Modell , Element-Geometrie , Schalendicke
   Workbenches: FEM_Workbench/de
   Shortcut: **C** **S**
   SeeAlso: FEM_tutorial/de
---

# FEM ElementGeometry2D/de



## Beschreibung

Ein **ElementGeometry2D**-Objekt wird zum Festlegen der Wandstärke von FEM-Schalenelementen verwendet; für alle oder nur diejenigen, die auf der ausgewählten Oberfläche liegen.



## Anwendung

1.  Es gibt mehrereMöglichkeiten den Befehl aufzurufen:
    -   Die Schaltfläche **<img src="images/FEM_ElementGeometry2D.svg" width=16px> [Schalendicke](FEM_ElementGeometry2D/de.md)** drücken.
    -   Den Menüeintrag **Modell → Element-Geometrie → <img src="images/FEM_ElementGeometry2D.svg" width=16px> Schalendicke** auswählen.
2.  Die Schalendicke festlegen.
3.  Wahlweise die Schaltfläche **Hinzufügen** im Aufgabenbereich drücken und danach auf die Fläche klicken, die eine voreingestellte Wandstärke erhalten soll. Wenn die Flächenauswahl leer ist, werden automatisch alle übrigen Flächen zugeordnet (deren Wandstärke nicht durch andere [ElementGeometry2D](FEM_ElementGeometry2D/de.md)-Objekte festgelegt ist).



## Einschränkungen

-   Zurzeit werden Analysen, die Schalenelemente mit Festkörper- oder Kantenelementen kombinieren, nicht unterstützt.



## Eigenschaften


**Thickness**

: Legt die Wandstärke der Schale (Hülle) fest.



## Skripten



## Hinweise

-   Um die Ergebnisse sehen zu können, die der CalculiX-Löser aus dem Netz ableitet, das auf der vorgegebenen Wandstärke basiert, muss die Eigenschaft `Beam Shell Result Output 3D` des [SolverCcxTools](FEM_SolverCalculixCxxtools/de.md)-Objekts auf `True` gesetzt werden.





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ElementGeometry2D/de
