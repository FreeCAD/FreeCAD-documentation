---
- GuiCommand:
   Name: TechDraw Image
   Name/de: TechDraw Bild
   MenuLocation: TechDraw - Bitmap Bild einfügen
   Workbenches: [TechDraw](TechDraw_Workbench/de.md)
   SeeAlso: [TechDraw SVG Symbol](TechDraw_Symbol/de.md)
---

# TechDraw Image/de


</div>



## Beschreibung

Das Werkzeug **TechDraw Bild** fügt eine [Bitmap](Bitmap/de.md)-Grafik (PNG, JPEG, JPG, BMP usw.) aus einer Datei als Ansicht auf einem Zeichnungsblatt ein.

![](images/TechDraw_Image_example.png ) 
*In die Zeichnungsseite eingefügtes Bild*



## Anwendung


<div class="mw-translate-fuzzy">

1.  Die Schaltfläche **<img src="images/TechDraw_Image.svg" width=16px> [Bitmap-Grafik einfügen](TechDraw_Image/de.md)** drücken.
2.  Ein Dateidialog wird geöffnet. Einen Speicherort und einen Dateinamen auswählen.


</div>



## Eigenschaften

Siehe auch [TechDraw Ansicht](TechDraw_View/de#Eigenschaften.md)



### Daten


{{TitleProperty|Image}}

-    {{PropertyData/de|Image File|File}}(Bilddatei): Die Datei, die dieses Bitmap-Bild enthält.

-    {{PropertyData/de|Image Included|FileIncluded}}(Enthaltenes Bild): Eingebettete Bilddatei. Nur systeminterne Verwendung.

-    {{PropertyData/de|Width|Float}}: Die Breite des zugeschnittenen Bildes in mm.

-    {{PropertyData/de|Height|Float}}: Die Höhe des zugeschnittenen Bildes in mm.

:   Die beiden letzten Eigenschaften werden nur verwendet, wenn der Wert der {{PropertyView/de|Crop}} `True` ist.



### Ansicht


{{TitleProperty|Image}}

-    {{PropertyView/de|Crop|Bool}}: Schneidet das Bild auf {{PropertyData/de|Width}} x {{PropertyData/de|Height}} zu.



## Skripten

Siehe auch: [Autogenerierte API Dokumentation](https://freecad.github.io/SourceDoc/) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Das Werkzeug Bild kann in [Makros](Macros/de.md) und von der [Python](Python/de.md)-Konsole aus mit den folgenden Funktionen verwendet werden:


```python
dvi = FreeCAD.ActiveDocument.addObject('TechDraw::DrawViewImage','TestImage')
rc = page.addView(dvi)
dvi.ImageFile = "pathToMy/imageFile.png"
dvi.Height = 200
dvi.Width  = 200
```





{{TechDraw Tools navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw Image/de
