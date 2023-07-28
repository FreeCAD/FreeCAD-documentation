---
- GuiCommand:/de
   Name:Mesh HarmonizeNormals
   Name/de:Mesh Normalen ausrichten
   MenuLocation:Netze → Normalen ausrichten
   Workbenches:[Mesh](Mesh_Workbench/de.md)
   SeeAlso:[Mesh Normalen umkehren](Mesh_FlipNormals/de.md)
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

-   This command can produce a mesh with flipped normals. The [Mesh FlipNormals](Mesh_FlipNormals.md) command can be used to correct this.
-   For a clear indication of the orientation of the faces of mesh objects make sure the **Lighting** property of the mesh objects is set to {{Value|One side}}. The color of the back side of their faces will then depend on the backlight settings: **Edit → Preferences... → Display → 3D View → Backlight color - Intensity**. See: [Preferences Editor](Preferences_Editor#3D_View.md).





{{Mesh Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Mesh](Mesh_Workbench.md) > Mesh HarmonizeNormals/de
