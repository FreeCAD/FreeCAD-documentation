---
 GuiCommand:
   Name: Mesh HarmonizeNormals
   Name/de: Mesh NormalenAusrichten
   MenuLocation: Netze , Normalen ausrichten
   Workbenches: Mesh_Workbench/de
   SeeAlso: Mesh_FlipNormals/de
---

# Mesh HarmonizeNormals/de



## Beschreibung

Der Befehl **Mesh Normalen ausrichten** richtet die Normalen eines Netzobjektes einheitlich aus.



## Anwendung

1.  Ein oder mehrere Netzobjekte auswählen.
2.  Es gibt mehrere Möglichkeiten den Befehl aufzurufen:
    -   Die Schaltfläche **<img src="images/Mesh_HarmonizeNormals.svg" width=16px> [Mesh Normalen ausrichten](Mesh_HarmonizeNormals/de.md)** drücken.
    -   Den Menüeintrag **Netze → <img src="images/Mesh_HarmonizeNormals.svg" width=16px> Normalen ausrichten** auswählen.



## Hinweise

-   Dieser Befehl kann Netze mit umgekehrten Normalen erstellen. Der Befehl [Mesh NormalenUmkehren](Mesh_FlipNormals/de.md) kann verwendet werden, um dies zu korrigieren.
-   Für eine deutliche Aussage zur Ausrichtung der Flächen von Netzobjekten sollte die {{PropertyView/de|Lighting}} des Netzobjekts auf {{Value|One side}} gesetzt sein, dann hängt die Farbe der Rückseite ihrer Flächen von den Einstellungen der Hintergrundbeleuchtung ab: **Bearbeiten → Einstellungen... → Anzeige → 3D-Viewer → Farbe der Hintergrundbeleuchtung - Intensität**. Siehe: [Voreinstellungseditor](Preferences_Editor/de#3D-Viewer.md).





{{Mesh Tools navi

}}



---
⏵ [documentation index](../README.md) > [Mesh](Mesh_Workbench.md) > Mesh HarmonizeNormals/de
