---
- GuiCommand   */de
   Name   *TechDraw Image
   Name/de   *TechDraw Bild
   MenuLocation   *TechDraw → Bitmap Bild einfügen
   Workbenches   *[TechDraw](TechDraw_Workbench/de.md)
   SeeAlso   *[TechDraw SVG Symbol](TechDraw_Symbol/de.md)
---

# TechDraw Image/de

## Beschreibung

Das Bild Werkzeug fügt ein [Bitmap](bitmap/de.md) Bild (PNG, JPEG, JPG, BMP usw.) aus einer Datei als Ansicht in die Seite ein.

![](images/TechDraw_Image_example.png ) 
*In die Zeichnungsseite eingefügtes Bild*

## Anwendung

1.  Drücke die **<img src="images/TechDraw_Image.svg" width=16px> [Bitmap Bild einfügen](TechDraw_Image/de.md)** Schaltfläche
2.  Ein Dateidialog wird geöffnet. Wähle einen Speicherort und einen Dateinamen.

## Eigenschaften

Siehe auch [TechDraw Ansicht](TechDraw_View/de#Eigenschaften.md)

### Daten


{{TitleProperty|Image}}

-    **Image File|File**   * The file containing this bitmap.

-    **Image Included|FileIncluded**   * Embedded image file. System use only.

-    **Width|Float**   * The width of the cropped image in mm. Only used if **Crop** is `True`.

-    **Height|Float**   * The height of the cropped image in mm. Idem.

### Ansicht


{{TitleProperty|Image}}

-    **Crop|Bool**   * Schneidet das Bild auf **Width** x **Height** zu.

## Skripten


**Siehe auch   ***

[TechDraw Anwendungsschnittstelle](TechDraw_API/de.md) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Das Bildwerkzeug kann in [Makros](Macros/de.md) und aus der [Python](Python/de.md) Konsole aus mit den folgenden Funktionen verwendet werden   *


```python
dvi = FreeCAD.ActiveDocument.addObject('TechDraw   *   *DrawViewImage','TestImage')
rc = page.addView(dvi)
dvi.ImageFile = "pathToMy/imageFile.png"
dvi.Height = 200
dvi.Width  = 200
```





{{TechDraw Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw Image/de
