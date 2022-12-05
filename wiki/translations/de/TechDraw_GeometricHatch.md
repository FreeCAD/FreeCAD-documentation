---
- GuiCommand:/de
   Name:TechDraw GeometricHatch
   Name/de:TechDraw GeometrischeSchraffur
   MenuLocation:TechDraw → Geometrische Schraffur auf Fläche anwenden
   Workbenches:[TechDraw](TechDraw_Workbench/de.md)
   SeeAlso:[TechDraw Schraffur](TechDraw_Hatch/de.md), [TechDraw Schraffieren](TechDraw_Hatching/de.md)
---

# TechDraw GeometricHatch/de

## Beschreibung

Das Werkzeug <img alt="" src=images/TechDraw_GeometricHatch.svg  style="width:24px;"> **TechDraw GeometrischeSchraffur** füllt einen geschlossenen Bereich in einer Ansicht mit einem Muster, das auf einer AutoDesk PAT Schraffur Spezifikation basiert. Alternativ dazu verwendet das Werkzeug <img alt="" src=images/TechDraw_Hatch.svg  style="width:16px;"> [TechDraw Schraffur](TechDraw_Hatch.md) SVG-basierte Schraffurmuster. Siehe [Schraffieren](TechDraw_Hatching/de.md) für Einzelheiten.

<img alt="" src=images/TechDraw_GeomHatch_example.png  style="width:300px;"> 
*Geometrisches Schraffurmuster auf einer Fläche*

## Anwendung

1.  Wähle eine geschlossenen Bereich in einer Ansicht aus.
2.  Es gibt mehrere Möglichkeiten das Werkzeug aufzurufen:
    -   Die Schaltfläche**<img src="images/TechDraw_GeometricHatch.svg" width=16px>[Geometrische Schraffur auf Fläche anwenden](TechDraw_GeometricHatch/de.md)** drücken.
    -   Den Menüeintrag **TechDraw → Extensions: Attributes/Modifications → <img src="images/TechDraw_GeometricHatch.svg" width=16px> Geometrische Schraffur auf Fläche anwenden** auswählen.
3.  Der Aufgabenbereich zu **Geometrische Schraffur auf Fläche anwenden** öffnet sich.
4.  Optional können **Pattern File** (Schraffurdatei), **Pattern Name** (Schraffurname), **Pattern Scale** (Schraffurskalierung), **Line Weight** (Linienbreite) und **Line Color** (Linienfarbe) verändert werden.
5.  Schaltfläche **OK** drücken.

## Hinweise

-   Schraffierte Objekte sind anfällig für das \"[topologische Benennungsproblem](Topological_naming_problem/de.md)\". Siehe <img alt="" src=images/TechDraw_LengthDimension.svg  style="width:16px;"> [TechDraw Längenmaß einfügen](TechDraw_LengthDimension/de.md) für weitere Informationen. Es wird empfohlen, das Schraffieren als einen der letzten Schritte der Zeichnungserstellung auszuführen.

Ein kleiner Satz von Beispielmustern ist verfügbar in:


```python
$INSTALL_DIR/data/Mod/TechDraw/PAT/FCPAT.pat
```


`$INSTALL_DIR`

ist das Verzeichnis, in dem FreeCAD installiert wurde, zum Beispiel


```python
/usr/share/freecad/data/Mod/TechDraw/PAT/FCPAT.pat
```

## Eigenschaften

-    **Quelle**: Die Ansicht und die Fläche, die das Schraffurmuster erhält.

-    **Musterdatei**: Der Speicherort der zu verwendenden PAT Datei.

-    **Mustername**: Der Name der PAT Spezifikation innerhalb der Musterdatei.

-    **Mustermaßstab**: Der Maßstab, der auf das Muster angewendet werden soll (muss \> 0,0 sein).

-    **Musterstärke**: Die Dicke der Musterlinien.

-    **Musterfarbe**: Die Farbe für die Musterlinien.

## Skripten

Siehe auch: [Autogenerierte API Dokumentation](https://freecad.github.io/SourceDoc/) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Das GeometrischeSchraffur Werkzeug kann in [Makros](Macros/de.md) und aus der [Python](Python/de.md) Konsole mit den folgenden Funktionen verwendet werden:


```python
hatch = FreeCAD.ActiveDocument.addObject('TechDraw::DrawGeomHatch','GeomHatch')
hatch.Source = (view1,["Face0"])
hatch.FilePattern = "path/to/myPATfile.pat"
hatch.NamePattern = "Diamond"
rc = page.addView(hatch)
```

Es ist auch möglich, mit der TechDraw-Grafische Schraffur-Funktion ein Verbund-Objekt im 3D-Raum zu erstellen. Dabei muss man darauf achten, dass die Basis-Fläche auf der XY-Ebene liegt, weil der Algorithmus bisher nicht für andere Fälle geeignet ist.


```python
import TechDraw
face = Part.makePlane(10,10)
patfile = "path/to/myPATfile.pat"
pattern = "Diamond"
scale = 10
hatch = TechDraw.makeGeomHatch(face, scale, pattern, patfile)
Part.show(hatch)
```





{{TechDraw Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw GeometricHatch/de
