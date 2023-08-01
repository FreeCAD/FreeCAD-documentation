---
- GuiCommand:
   Name:FEM ElementGeometry2D
   Name/de:FEM ElementGeometrie2D
   MenuLocation:Model - Element-Geometrie - Shell plate thickness
   Workbenches:[FEM](FEM_Workbench/de.md)
   Shortcut:**C** **S**
   SeeAlso:[FEM Anleitungl](FEM_tutorial/de.md)
---

# FEM ElementGeometry2D/de



## Beschreibung

Ein **ElementGeometry2D**-Objekt wird zum Festlegen der Wandstärke von 2D-FEM-Elementen verwendet; alle oder nur die auf einer ausgewählten Oberfläche liegen.



## Anwendung

1.  Es gibt mehrereMöglichkeiten den Befehl aufzurufen:
    -   Die Schaltfläche **<img src="images/FEM_ElementGeometry2D.svg" width=16px> [Shell plate thickness](FEM_ElementGeometry2D/de.md)** drücken.
    -   Den Menüeintrag **Modell → Element-Geometrie → <img src="images/FEM_ElementGeometry2D.svg" width=16px> Shell plate thickness** auswählen.
2.  Den Parameter der Wandstärke festlegen.
3.  Wahlweise die Schaltfläche **Hinzufügen** im Aufgabenbereich drücken und danach auf die Fläche klicken, die eine voreingestellte Wandstärke erhalten soll. Wenn die Flächenauswahl leer ist, werden ihr automatisch alle übrigen Flächen (deren Wandstärke nicht durch andere [ElementGeometry2D](FEM_ElementGeometry2D/de.md)-Objekte festgelegt ist) zugeordnet.



## Einschränkungen

-   Eine Analyse, die Schalenelemente und Festkörper- oder Kantenelementen kombiniert, wird in der aktuellen Version (FreeCAD 0.18) nicht unterstützt.



## Eigenschaften


**Thickness**

: Legt die Wandstärke der Schale (Hülle) fest.



## Skripten



## Hinweise

-   Um die Ergebnisse sehen zu können, die der CalculiX-Löser aus dem Netz ableitet, das auf der vorgegebenen Wandstärke basiert, muss die Eigenschaft `Beam Shell Result Output 3D` des [SolverCcxTools](FEM_SolverCalculixCxxtools/de.md)-Objekts auf `True` gesetzt werden.





{{FEM Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ElementGeometry2D/de
