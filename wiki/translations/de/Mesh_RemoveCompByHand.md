---
 GuiCommand:
   Name: Mesh RemoveCompByHand
   Name/de: Mesh KomponenteVonHandEntfernen‏‎
   MenuLocation: Netze , Komponente von Hand entfernen...
   Workbenches: Mesh_Workbench/de
   SeeAlso: Mesh_RemoveComponents/de, Arch_SplitMesh/de
---

# Mesh RemoveCompByHand/de



## Beschreibung

Der Befehl \"Mesh KomponentenVonHandEntfernen\" entfernt Komponenten aus Netzobjekten.



## Anwendung

1.  Als eine Komponente wird eine komplette Gruppe von verbundenen Flächen bezeichnet. Normalerweise besteht ein Netzobjekt aus einer einzigen Komponente. Nach der Anwendung des Befehls [Mesh Zusammenführen](Mesh_Merge/de.md) kann aber ein Netzobjekt mehrere Komponenten enthalten.
2.  Der Befehl verwendet die Farbe Rot, um ausgwählte Komponenten zu markieren. Damit diese korrekt dargestellt werden:
    -   Die {{PropertyView/de|Display Mode}} (Anzeigemodus) des Netzobjekts sollte Flächen darstellen. Wenn nötig, den Befehl [Std Darstellungsart](Std_DrawStyle/de.md) anwenden, um diese Eigenschaft anzupassen.
    -   Die {{PropertyView/de|Shape Color}} (Formfarbe) des Netzobjekts sollte nicht Rot sein.
3.  Den Menüeintrag **Netze → <img src="images/Mesh_RemoveCompByHand.svg" width=16px> Komponente von Hand entfernen...** auswählen.
4.  Der Mauszeiger wandelt sich in ein Hand-Symbol.
5.  Die Komponenten in der [3D-Ansicht](3D_view/de.md) auswählen, die gelöscht werden sollen.
6.  Wahlweise die Menüoption **Auswahl aufheben** im Kontextmenü der 3D-Ansicht auswählen, um alle Komponenten abzuwählen.
7.  Die Menüoption **Selektierte Dreiecke löschen** im Kontextmenü der 3D-Ansicht auswählen, um die ausgewählten Komponenten zu löschen.
8.  Die Menüoption **Entfernen-Modus verlassen** im Kontextmenü der 3D-Ansicht auswählen, um den Befehl fertigzustellen.





{{Mesh Tools navi

}}



---
⏵ [documentation index](../README.md) > [Mesh](Mesh_Workbench.md) > Mesh RemoveCompByHand/de
