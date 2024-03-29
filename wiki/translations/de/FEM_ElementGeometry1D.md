---
 GuiCommand:
   Name: FEM ElementGeometry1D
   Name/de: FEM ElementGeometrie1D
   MenuLocation: Modell , Element-Geometrie , Stabquerschnitt
   Workbenches: FEM_Workbench/de
   Shortcut: **C** **B**
   SeeAlso: FEM_tutorial/de
---

# FEM ElementGeometry1D/de



## Beschreibung

**ElementGeometrie1D** wird zur Festlegung der Querschnitte (BeamCrossSection-Objekte) von Stabelementen (Träger, Balken, Säulen usw.) verwendet. Derzeit sind folgende drei Querschnittformen vorhanden: Rechteck, Kreis und Ring.



## Anwendung

1.  Es gibt mehrere Möglichkeiten, den Befehl aufzurufen:
    -   Die Schaltfläche **<img src="images/FEM_ElementGeometry1D.svg" width=16px> [Stabquerschnitt](FEM_ElementGeometry1D/de.md)** drücken.
    -   Den Menüeintrag **Modell → Element-Geometrie → <img src="images/FEM_ElementGeometry1D.svg" width=16px> Stabquerschnitt** auswählen.
2.  Die Art des Querschnitts auswählen und die erforderlichen Abmaße eingeben:
    -   Rectangular (Rechteck): Breite und Höhe.
    -   Circular (Kreis): Durchmesser.
    -   Pipe (Ring): Durchmesser und Wandstärke.
3.  Wahlweise die Schaltfläche **Hinzufügen** im Aufgabenbereich drücken und anschließend die Kante anklicken, die einen festgelegten Querschnitt erhalten soll. Ist die Auswahl leer, werden alle verbleibenden Kanten (deren Querschnitte nicht durch andere [ElementGeometrie1D](FEM_ElementGeometry1D/de.md)-Objekte festgelegt sind) automatisch zugeordnet.



## Optionen



## Eigenschaften



## Einschränkungen



## Hinweise

-   Um die Ergebnisse sehen zu können, die der CalculiX-Löser aus dem Netz ableitet, das auf dem vorgegebenen Querschnitt basiert, muss die Eigenschaft `Beam Shell Result Output 3D` des [SolverCcxTools](FEM_SolverCalculixCxxtools/de.md)-Objekts auf `True` gesetzt werden.



## Skripten





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ElementGeometry1D/de
