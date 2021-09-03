---
- GuiCommand:/de
   Name:TechDraw Image
   Name/de:TechDraw Bild
   MenuLocation:TechDraw → Bitmap Bild einfügen
   Workbenches:[TechDraw](TechDraw_Workbench/de.md)
   SeeAlso:[TechDraw SVG Symbol](TechDraw_Symbol/de.md)
---

## Beschreibung

Das Bild Werkzeug fügt ein [Bitmap](bitmap/de.md) Bild (PNG, JPEG, JPG, BMP usw.) aus einer Datei als Ansicht in die Seite ein.

![](images/TechDraw_Image_example.png ) *In die Zeichnungsseite eingefügtes Bild*

## Anwendung

1.  Drücke die **<img src="images/TechDraw_Image.svg" width=16px> [Bitmap Bild einfügen](TechDraw_Image/de.md)** Schaltfläche
2.  Ein Dateidialog wird geöffnet. Wähle einen Speicherort und einen Dateinamen.

## Eigenschaften

-   Verwende die Eigenschaft Skalieren, um die Größe des Bildes anzupassen.
-   Verwende die Eigenschaften Breite und Höhe, um das Bild auszuschneiden.

## Skripten


**Siehe auch:**

[TechDraw Anwendungsschnittstelle](TechDraw_API/de.md) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Das Bildwerkzeug kann in [Makros](Macros/de.md) und aus der [Python](Python/de.md) Konsole aus mit den folgenden Funktionen verwendet werden:


```python
dvi = FreeCAD.ActiveDocument.addObject('TechDraw::DrawViewImage','TestImage')
rc = page.addView(dvi)
dvi.ImageFile = "pathToMy/imageFile.png"
dvi.Height = 200
dvi.Width  = 200
```





{{TechDraw Tools navi

}}  
