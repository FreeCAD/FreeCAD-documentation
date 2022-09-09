---
- GuiCommand   */de
   Name   *TechDraw  ActiveView
   Name/de   *TechDraw AktiveAnsicht
   MenuLocation   *TechDraw → Aktive (3D-)Ansicht einfügen
   Workbenches   *[TechDraw](TechDraw_Workbench/de.md)
   Version   *0.19
   SeeAlso   *[TechDraw Symbol](TechDraw_Symbol/de.md)
---

# TechDraw ActiveView/de

## Beschreibung

Das Werkzeug AktiveAnsicht fügt eine Kopie eines 3D-Fensters in ein Zeichnungsblatt ein.

![](images/TechDraw_ActiveView_example.png ) 
*Eine einfache Ansicht aus dem 3D-Modell, die keine komplexen Berechnungen ausführt.*

## Anwendung

1.  Zur richtigen [3D-Ansicht](3D_view/de.md) wechseln.
2.  Wenn sich mehrere Zeichnungsblätter im Dokument befinden, kann man das gewünschte Blatt in der [Baumansicht](Tree_view/de.md) auswählen. Für {{VersionMinus/de|0.19}} muss hier ein Blatt ausgewählt werden.
3.  Es gibt mehrere Möglichkeiten das Werkzeug aufzurufen   *
    -   Die Schaltfläche **<img src="images/TechDraw_ActiveView.svg" width=16px> [Aktive (3D-)Ansicht einfügen](TechDraw_ActiveView/de.md)** drücken.
    -   Den Menüeintrag **TechDraw → <img src="images/TechDraw_ActiveView.svg" width=16px> Aktive (3D-)Ansicht einfügen** auswählen.
4.  Wenn sich mehrere Zeichnungsblätter im Dokument befinden und noch kein Blatt ausgewählt wurde, öffnet sich der Dialog {{MenuCommand/de|Blattauswahl}} {{Version/de|0.20}}   *
    1.  Das gewünschte Zeichnungsblatt auswählen.
    2.  Die Schaltfläche **OK** drücken.
5.  Der Aufgabenbereich {{MenuCommand/de|Aktive Ansicht wird TD-Ansicht}} wird geöffnet. Siehe [Optionen](#Optionen.md) für weitere Informationen.
6.  Die Schaltfläche **OK** drücken.

## Optionen

Folgendes kann eingestellt werden   *

-    **Width**   * Die Breite der erstellten Ansicht.

-    **Height**   * Die Höhe der erstellten Ansicht.

-    **Border**   * Der leere Randbereich um die Ansicht herum (aber innerhalb von Breite x Höhe).

-    **Background**   * Wenn aktiviert, wird ein Hintergrund in der eingestellten Farbe hinzugefügt.

-    **Line Width**   * Die Strichstärke in der Ansicht.

-    **Render Mode**   * Die verfügbaren Modi   *

    -   
        {{Value|As is}}
        
           * Rendert Grundkörper wie sie sind.

    -   
        {{Value|Wireframe}}
        
           * Rendert Vielecke als Drahtgeometrie

    -   
        {{Value|Points}}
        
           * Rendert nur die Knotenpunkte der Vielecke und linien.

    -   
        {{Value|Wireframe overlay}}
        
           * Rendert ein Drahtgitter zusätzlich zum {{Value|As is}} -Modus.

    -   
        {{Value|Hidden Line}}
        
           * Wie {{Value|Wireframe}}, blendet aber Linien aus, die sonst geometrisch verdeckt sein würden.

    -   
        {{Value|Bounding box}}
        
           * Zeigt nur die Hüllquader (BoundingBox) der jeweiligen Objekte an.

## Hinweise

-   Aktive Ansichten sind statisch; nach der Erzeugung werden sie nicht mehr aktualisiert, wenn sich das 3D-Modell ändert.
-   Eine aktive Ansicht ist im Grunde ein <img alt="" src=images/TechDraw_Symbol.svg  style="width   *24px;"> [Symbol](TechDraw_Symbol/de.md). Seine {{PropertyData/de|Scale Type}} wird daher immer als {{Value|Custom}} (benutzerdefiniert) voreingestellt.

* Dieses Werkzeug ist noch etwas **experimentell**.

## Eigenschaften

Siehe [TechDraw Symbol](TechDraw_Symbol/de.md).

## Skripten


**Siehe auch   ***

[TechDraw API](TechDraw_API/de.md) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Das Werkzeug AktiveAnsicht kann in [Makros](Macros/de.md) und aus der [Python](Python/de.md)-Konsole heraus mittels folgender Funktionen verwendet werden   *


```python
import TechDrawGui
TechDrawGui.copyActiveViewToSvgFile(Gui.ActiveDocument.ActiveView,"myFile.svg")
```





{{TechDraw Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw ActiveView/de
