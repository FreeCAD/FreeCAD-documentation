---
 GuiCommand:
   Name: Mesh RemeshGmsh
   Name/de: Mesh NeuVernetzenGmsh
   MenuLocation: Netze , Aufbereitung...
   Workbenches: Mesh_Workbench/de
   Version: 0.19
   SeeAlso: Mesh_FromPartShape/de
---

# Mesh RemeshGmsh/de



## Beschreibung

Der Befehl **Mesh NeuVernetzenGmsh** vernetzt ein Netzobjekt erneut unter Verwendung des Vernetzers [Gmsh](https://gmsh.info/). Das neue Netz kann feiner oder gröber sein.



## Anwendung

1.  Ein einzelnes Netzobjekt auswählen.
2.  Es gibt mehrere Möglichkeiten, den Befehl aufzurufen:
    -   Die Schaltfläche **<img src="images/Mesh_RemeshGmsh.svg" width=16px> [Aufbereitung...](Mesh_RemeshGmsh/de.md)** drücken.
    -   Den Menüeintrag **Netze → <img src="images/Mesh_RemeshGmsh.svg" width=16px> Aufbereitung...** auswählen.
3.  Der Aufgaben-Bereich **Neuvernetzung durch Gmsh** wird geöffnet.
4.  Die erforderlichen Einstellungen festlegen. Siehe die [Gmsh-Vernetzer-Einstellungen](Mesh_FromPartShape/de#Netzgenerator_Gmsh.md) des Befehls [Mesh NetzAusPartForm](Mesh_FromPartShape.md).
5.  Die Schaltfläche **Anwenden** drücken, um das Netzobjekt neu zu vernetzen.
6.  Wahlweise eine oder Mehrere Einstellungen anpassen und erneut die Schaltfläche **Anwenden** drücken, bis das Netz gefällt.
7.  Die Schaltfläche **Schließen** drücken, um den Aufgaben-Bereich zu schließen und den Befehl zu beenden.



## Hinweise

-   In einigen Fällen erzeugt dieser Befehl Netze mit umgekehrten Normalen. Der Befehl [Mesh NormalenUmkehren](Mesh_FlipNormals/de.md) kann verwendet werden, um dies zu korrigieren.



## Eigenschaften

Siehe: [Mesh Formelement](Mesh_Feature/de.md).





{{Mesh Tools navi

}}



---
⏵ [documentation index](../README.md) > [Mesh](Mesh_Workbench.md) > Mesh RemeshGmsh/de
