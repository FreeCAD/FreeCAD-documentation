---
 GuiCommand:
   Name: Draft ToggleGrid
   Name/de: Draft RasterUmschalten
   Workbenches: Draft_Workbench/de, Arch_Workbench/de
   Shortcut: **G** **R**
   SeeAlso: Draft_Snap_Grid/de, Draft_SelectPlane/de
---

# Draft ToggleGrid/de



## Beschreibung

Der Befehl <img alt="" src=images/Draft_ToggleGrid.svg  style="width:24px;"> **Draft RasterUmschalten** schaltet die Sichtbarkeit des Rasters ein bzw. aus.


{{Version/de|0.22}}

: Jede [3D-Ansicht](3D_view.md) hat ihr eigenes Raster, das jeweils ständig sichtbar, nur sichtbar während der Ausführung eines Befehls oder unsichtbar ist. Die Ausgangseinstellung der Sichtbarkeit hängt von den [Einstellungen](#Einstellungen.md) ab.



## Anwendung

1.  Der Befehl kann verwendet werden, während ein anderer Befehl aktiv ist.
2.  Es gibt mehrere Möglichkeiten den Befehl aufzurufen:
    -   Die Schaltfläche **<img src="images/Draft_ToggleGrid.svg" width=16px> [Raster umschalten](Draft_ToggleGrid/de.md)** in der Symbolleiste Draft-Einrasten drücken.
    -   Die Schaltfläche **<img src="images/Draft_ToggleGrid.svg" width=16px> [Raster umschalten](Draft_ToggleGrid/de.md)** im [Draft-Widget Einrasten](Draft_snap_widget/de.md) drücken.
    -   Das Tastaturkürzel **G** then **R**. Dieses Tastaturkürzel kann nur verwendet werden, wenn ein anderer Befehl aktiv ist.
3.  Die Sichtbarkeit des Rasters, das zur aktuellen 3D-Ansicht gehört, wurde geändert:
    -   Wenn kein anderer Befehl aktiv ist:
        -   War das Raster unsichtbar, ist es jetzt ständig sichtbar.
        -   War das Raster sichtbar, ist es jetzt nicht mehr ständig sichtbar, aber die Sichtbarkeit des Raster während der Ausführung eines Befehls bleibt unverändert.
    -   Wenn eine anderer Befehl aktiv ist:
        -   War das Raster unsichtbar, ist es jetzt nur während der Ausführung eines Befehls sichtbar.
        -   War das Raster unsichtbar, ist es jetzt nicht mehr während der Ausführung eines Befehls sichtbar und auch nicht mehr ständig sichtbar.



## Einstellungen

Siehe auch: [Voreinstellungseditor](Preferences_Editor/de.md) und [Draft Einstellungen](Draft_Preferences/de.md).

-   Es stehen mehrere Rastereigenschaften zur Verfügung: **Bearbeiten → Einstellungen... → Draft → Raster und Einrasten**.
-   Um das Raster zu behalten, wenn man zu anderen Arbeitsbereichen wechselt, siehe [Fine-Tuning](Fine-tuning/de#Draft_Workbench.md).



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft ToggleGrid/de
