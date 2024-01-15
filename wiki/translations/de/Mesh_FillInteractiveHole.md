---
 GuiCommand:
   Name: Mesh FillInteractiveHole
   Name/de: Mesh LochInteraktivSchließen
   MenuLocation: Netze , Loch schließen
   Workbenches: Mesh_Workbench/de
   SeeAlso: Mesh_FillupHoles/de, Mesh_AddFacet/de
---

# Mesh FillInteractiveHole/de



## Beschreibung

Der Befehl **Mesh LochInteraktivFüllen** füllt ausgewählte Löcher in Netzobjekten.



## Anwendung

1.  Es gibt mehrere Möglichkeiten, den Befehl aufzurufen:
    -   Die Schaltfläche **<img src="images/Mesh_FillInteractiveHole.svg" width=16px>.[Loch schließen](Mesh_FillInteractiveHole/de.md)** drücken.
    -   Den Menüeintrag **Netze → <img src="images/Mesh_FillInteractiveHole.svg" width=16px> Loch schließen** auswählen.
2.  Der Mauszeiger ändert sich in ein Dreieckssymbol.
3.  Eine Fläche auswählen, die eine Kante mit dem Loch teilt, das geschlossen werden soll.
4.  Das Loch wird geschlossen.
5.  Wahlweise wiederholen, um weitere Löcher zu schließen.
6.  Bei Bedarf [Std Rückgängig](Std_Undo/de.md) verwenden, um die letzte Aktion des Befehls rückgängig zu machen.
7.  Die Option **Löcher-Schließen-Modus verlassen** aus dem Kontextmenü der [3D-Ansicht](3D_view/de.md) auswählen, um den Befehl zu beenden.



## Hinweise

-   Wenn die Kanten eines Lochs nicht in der gleichen Ebene liegen, kann das Ergebnis des Befehls von der ausgewählten Fläche abhängen.





{{Mesh Tools navi

}}



---
⏵ [documentation index](../README.md) > [Mesh](Mesh_Workbench.md) > Mesh FillInteractiveHole/de
