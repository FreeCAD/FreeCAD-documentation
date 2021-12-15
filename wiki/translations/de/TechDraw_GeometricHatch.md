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

Das GeometrischeSchraffur Werkzeug füllt einen geschlossenen Bereich in einer Ansicht mit einem Muster, das auf einer AutoDesk PAT Schraffur Spezifikation basiert. *Alternativ* verwendet das [Schraffur](TechDraw_Hatch/de.md) Werkzeug eine [SVG](SVG/de.md) oder [Bitmap](bitmap/de.md) Datei als Schraffurmuster, siehe [Schraffierung](TechDraw_Hatching/de.md) für Einzelheiten.

<img alt="" src=images/TechDraw_GeomHatch_example.png  style="width:300px;"> 
*Geometrisches Schraffurmuster auf einer Fläche*

## Anwendung

1.  Wähle eine geschlossenen Bereich in einer Ansicht aus.
2.  Drücke die Taste **<img src="images/TechDraw_GeometricHatch.svg" width=16px>[Geometrische Schraffur auf Fläche anwenden](TechDraw_GeometricHatch/de.md)** Schaltfläche
3.  Ein Dialog öffnet sich , in dem du dein Muster, den Maßstab, Linienstärke und Farbe auswählen kannst.

## Hinweise


<div class="mw-translate-fuzzy">

-   Schraffierte Objekte sind anfällig für \"[topologische Benennungs](Topological_naming_problem/de.md)\" Probleme. Siehe die Informationen in der **<img src="images/TechDraw_LengthDimension.svg" width=16px> [TechDraw Bemaßungslänge](TechDraw_LengthDimension/de.md)** für weitere Informationen. Es wird empfohlen, dass das Schraffieren einer der letzten Schritte in Ihrem Zeichenprozess ist.


</div>

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


**Siehe auch:**

[TechDraw API](TechDraw_API/de.md) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

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
[documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw GeometricHatch/de
