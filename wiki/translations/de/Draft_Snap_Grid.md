---
- GuiCommand:/de
   Name:Draft Snap Grid
   Name/de:Draft EinrastenAufRaster
   Workbenches:[Draft](Draft_Workbench/de.md), [Arch](Arch_Workbench/de.md)
   SeeAlso:[Draft Einrasten](Draft_Snap/de.md), [Draft EinrastenSperren](Draft_Snap_Lock.md), [Draft RasterUmschalten](Draft_ToggleGrid/de.md), [Draft EbeneAuswählen](Draft_SelectPlane/de.md)
---

# Draft Snap Grid/de



## Beschreibung

Die Option <img alt="" src=images/Draft_Snap_Grid.svg  style="width:24px;"> **Draft EinrastenAufRaster** Rastet auf den Schnittstellen von Rasterlinien ein. Das Raster kann nur verwendet werden, wenn die Eigenschaft **Use grid** ausgewählt wurde. Siehe [Einstellungen](#Einstellungen.md).

![](images/Draft_Snap_Grid_example.png ) 
*Einrasten des zweiten Punktes einer Linie am Raster*



## Anwendung

Für allgemeine Informationen zum Einrasten (Fangen) siehe [Draft Fangen](Draft_Snap/de.md).

1.  Wahlweise [Arbeitsebene und/oder Raster](Draft_SelectPlane/de.md) auswählen.
2.  Vergewissern, dass Einrasten aktiviert ist. Siehe <img alt="" src=images/Draft_Snap_Lock.svg  style="width:16px;"> [Draft EinrastenSperren](Draft_Snap_Lock/de.md).
3.  Ist **Draft EinrastenSperren** nicht aktiv, gibt es folgende Möglichkeiten:
    -   Die Schaltfläche **<img src="images/Draft_Snap_Grid.svg" width=16px>** in der Symbolleiste Draft-Einrasten drücken.
    -   Die Schaltfläche **<img src="images/Draft_Snap_Lock.svg" width=x16px><img src="images/Toolbar_flyout_arrow.svg" width=x16px>** im [Draft-Widget Einrasten](Draft_snap_widget.md) gedrückt halten und im Ausklappmenü die Option **<img src="images/Draft_Snap_Grid.svg" width=16px> Raster fangen** auswählen.
4.  Einen [Draft](Draft_Workbench/de.md)- oder [Arch](Arch_Workbench.md)-Befehl zur Geometrieerstellung auswählen.
5.  Man beachte, dass sich die Einrast-Optionen auch ändern lassen, während ein Befehl aktiv ist.
6.  Das Raster wird jetzt angezeigt, wenn es vorher noch nicht sichtbar war.
7.  Den Mauszeiger in die Nähe einer Schnittstelle zweier Rasterlinien bewegen.
8.  Wird eine Schnittstelle gefunden, wird der Schnittpunkt markiert und das Symbol <img alt="" src=images/Draft_Snap_Grid.svg  style="width:16px;"> neben dem Mauszeiger angezeigt.
9.  Klicken, um den Punkt zu bestätigen.



## Einstellungen

Siehe [Draft-Einrasten](Draft_Snap/de#Einstellungen.md).

-   Um das Raster zu verwenden: **Bearbeiten → Einstellungen... → Draft → Raster und einrasten → Raster → Raster verwenden** auswählen. Das Ändern dieser Einstellung erfordert einen Neustart von FreeCAD.
-   Unter ** Bearbeiten → Einstellungen... → Draft → Raster und einrasten → Raster** sind auch noch andere Raster-Einstellungen vorhanden:.



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Snap Grid/de
