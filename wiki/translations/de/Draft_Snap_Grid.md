---
 GuiCommand:
   Name: Draft Snap Grid
   Name/de: Draft EinrastenAufRaster
   MenuLocation: Einrasten , Einrasten auf Raster
   Workbenches: Draft_Workbench/de, BIM_Workbench/de
   SeeAlso: Draft_Snap/de, Draft_Snap_Lock, Draft_ToggleGrid/de, Draft_SelectPlane/de
---

# Draft Snap Grid/de



## Beschreibung

Die Option <img alt="" src=images/Draft_Snap_Grid.svg  style="width:24px;"> **Draft EinrastenAufRaster** rastet auf den Schnittstellen von Rasterlinien ein.

![](images/Draft_Snap_Grid_example.png ) 
*Einrasten des zweiten Punktes einer Linie am Raster*



## Anwendung

Für allgemeine Informationen zum Einrasten (Fangen) siehe [Draft Fangen](Draft_Snap/de.md).

1.  Wahlweise [Arbeitsebene und/oder Raster](Draft_SelectPlane/de.md) auswählen.
2.  Vergewissern, dass Einrasten aktiviert ist. Siehe <img alt="" src=images/Draft_Snap_Lock.svg  style="width:16px;"> [Draft EinrastenSperren](Draft_Snap_Lock/de.md).
3.  Ist **Draft EinrastenSperren** nicht aktiv, gibt es folgende Möglichkeiten:
    -   Die Schaltfläche **<img src="images/Draft_Snap_Grid.svg" width=16px> [Einrasten auf Raster](Draft_Snap_Grid/de.md)** in der Symbolleiste Draft-Einrasten drücken.
    -   [Draft](Draft_Workbench/de.md): Die Schaltfläche **<img src="images/Draft_Snap_Lock.svg" width=x16px><img src="images/Toolbar_flyout_arrow.svg" width=x16px>** im [Draft-Widget Einrasten](Draft_snap_widget/de.md) gedrückt halten und im Ausklappmenü die Option **<img src="images/Draft_Snap_Grid.svg" width=16px> Einrasten auf Raster** auswählen.
    -   [BIM](BIM_Workbench/de.md): Den Menüeintrag **Einrasten → <img src="images/Draft_Snap_Grid.svg" width=16px> Einrasten auf Raster** auswählen oder die Menüoption im Kontextmenü der [3D-Ansicht](3D_view/de.md) auswählen.
4.  Einen Draft- oder BIM-Befehl auswählen, um die gewünschte Geometrie zu erstellen.
5.  Man beachte, dass sich die Einrast-Optionen auch ändern lassen, während ein Befehl aktiv ist.
6.  Falls erforderlich [Draft RasterUmschalten](Draft_ToggleGrid/de.md) verwenden, um das Raster anzuzeigen. Das Raster muss sichtbar sein, damit diese Einrastoption funktioniert.
7.  Den Mauszeiger in die Nähe einer Schnittstelle zweier Rasterlinien bewegen.
8.  Wird eine Schnittstelle gefunden, wird der Schnittpunkt markiert und das Symbol <img alt="" src=images/Draft_Snap_Grid.svg  style="width:16px;"> neben dem Mauszeiger angezeigt.
9.  Klicken, um den Punkt zu bestätigen.



## Einstellungen

Siehe [Draft-Einrasten](Draft_Snap/de#Einstellungen.md).

-   Es gibt mehrere Raster-Voreinstellungen unter: **Bearbeiten → Einstellungen... → Draft → Raster und Einrasten**.



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Snap Grid/de
