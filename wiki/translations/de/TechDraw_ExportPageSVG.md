---
- GuiCommand:/de
   Name:TechDraw ExportPageSVG
   Name/de:TechDraw ExportiereSeiteSVG
   MenuLocation:TechDraw → Exportiere Seite als SVG
   Workbenches:[TechDraw](TechDraw_Workbench/de.md)
   SeeAlso:[TechDraw Vorlagen](TechDraw_Templates/de.md), [Entwurf SVG](Draft_SVG/de.md)
---

# TechDraw ExportPageSVG/de

## Beschreibung

Das ExportSeiteSVG Werkzeug speichert das aktuelle Zeichnungsseite als [SVG](SVG/de.md) Datei.

## Anwendung

1.  Drücke die **<img src="images/TechDraw_ExportPageSVG.svg" width=16px> [Export Seite als SVG](TechDraw_ExportPageSVG/de.md)** Schaltfläche.
2.  Ein Dateispeicher Dialog wird geöffnet. Wähle einen Speicherort und einen Dateinamen.

## Hinweise

-   [TechDraw Schraffur](TechDraw_Hatch/de.md) Muster werden aufgrund einer Begrenzung in der SVG Unterstützung von Qt4 nicht nach [SVG](SVG/de.md) exportiert.
-   Textpositionen und -größen sind in der exportierten Datei nicht korrekt. Die Verwendung der \"System\" Standardschriftart in der Zeichnung verbessert das Größenproblem erheblich.

## Skripten


**Siehe auch:**

[TechDrawGui API](TechDrawGui_API/de.md) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Das SpeichereSVG Werkzeug kann in [Makros](Macros/de.md) und aus der [Python](Python/de.md) Konsole mit den folgenden Funktionen benutzt werden:


```python
TechDrawGui.exportPageAsSvg(DrawPageObject,FilePath)
```

Beachte, dass das FreeCADGui Modul aktiv sein muss, um diese Funktion nutzen zu können.


<div class="mw-translate-fuzzy">





</div>


{{TechDraw Tools navi

}}

---
[documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw ExportPageSVG/de
