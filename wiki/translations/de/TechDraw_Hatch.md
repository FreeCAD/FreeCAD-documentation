---
- GuiCommand:/de
   Name:TechDraw Hatch
   Name/de:TechDraw Schraffur
   MenuLocation:TechDraw → Schraffieren einer Fläche unter Verwendung einer Bilddatei 
   Workbenches:[TechDraw](TechDraw_Workbench/de.md)
   SeeAlso:[TechDraw Geometrische Schraffur](TechDraw_GeometricHatch/de.md), [TechDraw Schraffieren](TechDraw_Hatching/de.md)
---

# TechDraw Hatch/de

## Beschreibung

Das Schraffur Werkzeug füllt einen geschlossenen Bereich in einer Ansicht mit einem Schraffurmuster, das [SVG](SVG/de.md) oder [bitmap](bitmap/de.md) Dateien sein können. Im Gegenteil, das <img alt="" src=images/TechDraw_GeometricHatch.svg  style="width:24px;"> [Geometrische Schraffur](TechDraw_GeometricHatch/de.md) Werkzeug verwendet eine bestimmte PAT Musterdatei, siehe [Schraffur](TechDraw_Hatching/de.md) für Einzelheiten.

<img alt="" src=images/TechDraw_Hatch_example.png  style="width:300px;">


*SVG Schraffurmuster auf einer Fläche*

## Anwendung

1.  Wähle einen geschlossenen Bereich in einer Ansicht.
2.  Drücke die **<img src="images/TechDraw_Hatch.svg" width=16px> [Fläche schraffieren unter Verwendung einer Bilddatei](TechDraw_Hatch/de.md)** Schaltfläche
3.  Ein Dialog öffnet sich, in demdu die Musterdatei, den Maßstab und die Farbe auswählen kannst.

## Hinweise

-   Schraffierte Objekte sind anfällig für das \"[topologische Benennungsproblem](Topological_naming_problem/de.md)\". Siehe [TechDraw LängenBemaßung](TechDraw_LengthDimension/de.md) für weitere Information. Es wird empfohlen, dass das Schraffieren einer der letzten Schritte in deinem Zeichenprozess ist.
-   Beispielmuster [SVG](SVG/de.md) sind lokal verfügbar in


```python
$INSTALL_DIR/data/Mod/TechDraw/Patterns
```

wobei `$INSTALL_DIR` das Verzeichnis ist, wo FreeCAD installiert wurde, z.B. 
```python
/usr/share/freecad/data/Mod/TechDraw/Patterns
``` und auch auf [GitHub](https://github.com/FreeCAD/FreeCAD/tree/master/src/Mod/TechDraw/Patterns).

## Eigenschaften

-    **Quelle**: Ansicht und Fläche, die das Schraffurmuster enthalten.

-    **Schraffurmuster**: Vollständiger Pfad und Dateiname zu einer SVG Musterdatei.

-    **Schraffurfarbe**: Das Schraffurmuster wird mit dieser Farbe angezeigt.

-    **Schraffurmaßstab**: Faktor zur Modifizierung der Schraffurmuster.

## Skripten


**Siehe auch:**

[TechDraw Anwendungsschnittstelle](TechDraw_API/de.md) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Das Schraffur Werkzeug kann mit [Makros](Macros/de.md) und aus der [Python](Python/de.md) Konsole mit den folgenden Funktionen verwendet werden:


```python
hatch = FreeCAD.ActiveDocument.addObject('TechDraw::DrawHatch','Hatch')
hatch.Source = (view1,["Face0"])
hatch.HatchPattern = hatchFileSpec
rc = page.addView(hatch)
```





{{TechDraw Tools navi

}}

---
[documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw Hatch/de
