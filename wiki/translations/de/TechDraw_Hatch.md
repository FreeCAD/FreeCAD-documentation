---
- GuiCommand:/de
   Name:TechDraw Hatch
   Name/de:TechDraw Schraffur
   MenuLocation:TechDraw → Hatching → Fläche mit Muster aus einer Bilddatei schraffieren
   Workbenches:[TechDraw](TechDraw_Workbench/de.md)
   SeeAlso:[TechDraw Geometrische Schraffur](TechDraw_GeometricHatch/de.md), [TechDraw Schraffieren](TechDraw_Hatching/de.md)
---

# TechDraw Hatch/de



## Beschreibung

Das Werkzeug **TechDraw Schraffur** füllt einen geschlossenen Bereich in einer Ansicht mit einem gekachelten [SVG](SVG/de.md)- oder bitmap-basierten ({{Version/de|0.21}}) Schraffurmuster. Alternativ dazu verwendet das Werkzeug <img alt="" src=images/TechDraw_GeometricHatch.svg  style="width:16px;"> [TechDraw GeometrischeSchraffur](TechDraw_GeometricHatch/de.md) ein PAT-basiertes Schraffurmuster. Siehe [Schraffieren](TechDraw_Hatching/de.md) für Einzelheiten.

<img alt="" src=images/TechDraw_Hatch_example.png  style="width:300px;">



*SVG Schraffurmuster auf einer Fläche*



## Anwendung

1.  Einen geschlossenen Bereich in einer Ansicht auswählen.
2.  Es gibt mehrere Möglichkeiten das Werkzeug aufzurufen:
    -   Die Schaltfläche **<img src="images/TechDraw_Hatch.svg" width=16px> [Fläche mit Muster aus einer Bilddatei schraffieren](TechDraw_Hatch/de.md)** drücken.
    -   Den Menüeintrag **TechDraw → Hatching → <img src="images/TechDraw_Hatch.svg" width=16px> Fläche mit Muster aus einer Bilddatei schraffieren** auswählen.
3.  Der Aufgabenbereich zu **Fläche mit Muster aus einer Bilddatei schraffieren** öffnet sich.
4.  Wahlweise kann **Pattern File** geändert werden (wechselt die Schraffurdatei) .
5.  Wahlweise können **Pattern Scale** (Schraffurskalierung) und **Line Color** (Linienfarbe) verändert werden. Diese Einstellungen werden für Bitmap-Muster ignoriert.
6.  Schaltfläche **OK** drücken.



## Hinweise

-   Schraffierte Objekte sind anfällig für das \"[Problem der topologischen Benennung](Topological_naming_problem/de.md)\". Siehe [TechDraw Längenmaß](TechDraw_LengthDimension/de.md) für weitere Information. Es wird empfohlen, dass das Schraffieren einer der letzten Schritte im Zeichenprozess ist.
-   [SVG](SVG/de.md)-Beispielmuster sind lokal verfügbar unter:

:   
    
```python
    $INSTALL_DIR/data/Mod/TechDraw/Patterns
    
```
    

:   Dabei ist `$INSTALL_DIR` das Verzeichnis, in dem FreeCAD installiert wurde, z.B.:

:   
    
```python
    /usr/share/freecad/data/Mod/TechDraw/Patterns
    
```
    

:   Sie stehen auch auf [GitHub](https://github.com/FreeCAD/FreeCAD/tree/master/src/Mod/TechDraw/Patterns) zur Verfügung.



## Eigenschaften

-    **Quelle**: Ansicht und Fläche, die das Schraffurmuster enthalten.

-    **Schraffurmuster**: Vollständiger Pfad und Dateiname zu einer SVG Musterdatei.

-    **Schraffurfarbe**: Das Schraffurmuster wird mit dieser Farbe angezeigt.

-    **Schraffurmaßstab**: Faktor zur Modifizierung der Schraffurmuster.



## Skripten

Siehe auch: [Autogenerierte API Dokumentation](https://freecad.github.io/SourceDoc/) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Eine Schraffur kann mit [Makros](Macros/de.md) und von der [Python](Python/de.md)-Konsole aus mit den folgenden Funktionen erstellt werden:


```python
hatch = FreeCAD.ActiveDocument.addObject("TechDraw::DrawHatch", "Hatch")
hatch.Source = (view1, ["Face0"])
hatch.HatchPattern = hatchFileSpec
page.addView(hatch)
```





{{TechDraw Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw Hatch/de
