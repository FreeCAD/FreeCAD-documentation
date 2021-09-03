---
- GuiCommand:/de
   Name:TechDraw  ActiveView
   Name/de:TechDraw AktiveAnsicht
   MenuLocation:TechDraw → Aktive Ansicht einfügen (3D Ansicht)
   Workbenches:[TechDraw](TechDraw_Workbench/de.md)
   Version:0.19
   SeeAlso:[TechDraw Symbol](TechDraw_Symbol/de.md)
---

## Beschreibung

Das Werkzeug AktiveAnsicht fügt eine Kopie eines 3D Fensters in eine Zeichnungsseite ein.

![](images/TechDraw_ActiveView_example.png )


*Eine einfache Ansicht aus dem 3D Modell, die keine komplexen Berechnungen ausführt.*

## Anwendung

1.  Gehe zu dem 3D Fenster, das du kopieren möchtest.
2.  Wenn du mehrere Zeichnungsseiten in deinem Dokument hast, musst du auch die gewünschte Seite im Baum auswählen.
3.  Drücke die **<img src="images/TechDraw_ActiveView.svg" width=16px> [Aktive Ansicht einfügen](TechDraw_ActiveView/de.md)** Schaltfläche
4.  Ein Dialogfeld wird geöffnet, in dem du die Größe, den Rahmen und die Hintergrundfarbe der Kopie festlegen kannst.

## Hinweise

-   Aktive Ansichten sind nach der Erzeugung statisch, sie werden nie mit Änderungen am 3D Modell aktualisiert.
-   AktiveAnsicht hinter den Kulissen ist ein <img alt="" src=images/TechDraw_Symbol.svg  style="width:24px;"> [Symbolansicht](TechDraw_Symbol/de.md). Sein **Maßstabstyp** wird daher immer als *Angepasst* gekennzeichnet.

* Dieses Werkzeug ist noch etwas **experimentell**.

## Eigenschaften

See <img alt="" src=images/TechDraw_Symbol.svg  style="width:16px;"> [Symbol](TechDraw_Symbol/de.md)

### Dialog Felder 

-    {{PropertyData/de|Breite}}: Die Breite der Ansicht.

-    **Höhe**: Die Höhe der Ansicht.

-    **Grenze**: Der Wert von leerem Raum am linken Rand, der dann auch umlaufend angezeigt wird (aber innerhalb der Werte von Breite x Höhe).

-    {{PropertyData/de|Hintergrund}}: Zeigt oder verbirgt den Hintergrund.

-    **Hintergrundfarbe**: Hintergrundfarbe, wenn Hintergrund angezeigt werden soll.

-    {{PropertyData/de|Linienbreite}}: Strichstärke individueller Linien in der Ansicht.

-    {{PropertyData/de|Render Modus}}: Für das Rendering / Wiedergabe [render mode](https://grey.colorado.edu/coin3d/classSoRenderManager.html#a4b8d99cff0fd91e31bc2c5d33610f6eb) wird die Bibliothek verwendet [Coin3d](https://en.wikipedia.org/wiki/Coin3D). Mögliche einstellbare Modi sind:

    -   **AS\_IS** = Rendering / Wiedergabe so einfach wie möglich.
    -   **WIREFRAME** = Rendering / Wiedergabe als vieleckiges Drahtgestell
    -   **POINTS** = Rendering / Wiedergabe nur der Punkte auf dem Drahtgestell
    -   **WIREFRAME\_OVERLAY** = Rendering / Wiedergabe der Drahtansicht in Verbindung mit dem Modus **AS\_IS**.
    -   **HIDDEN\_LINE / verdeckte Linien** als **WIREFRAME / Drahtgestell**, zeigt Linien, die sonst nicht angezeigt würden.
    -   **BOUNDING\_BOX** Zeigt den Begrenzungsrahmen jedes Objekts.

## Skripten


**Siehe auch:**

[TechDraw API](TechDraw_API/de.md) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Das Werkzeug AktiveAnsicht kann in [Makros](Macros/de.md) und aus der [Python](Python/de.md) Konsole heraus mittels folgender Funktionen verwendet werden:


```python
import TechDrawGui
TechDrawGui.copyActiveViewToSvgFile(Gui.ActiveDocument.ActiveView,"myFile.svg")
```





{{TechDraw Tools navi

}}  
