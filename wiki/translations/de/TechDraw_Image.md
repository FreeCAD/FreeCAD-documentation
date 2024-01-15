---
 GuiCommand:
   Name: TechDraw Image
   Name/de: TechDraw Bild
   MenuLocation: TechDraw , TechDraw Ansichten , Bitmap-Grafik einfügen
   Workbenches: TechDraw_Workbench/de
   SeeAlso: TechDraw_Symbol/de
---

# TechDraw Image/de



## Beschreibung

Das Werkzeug **TechDraw Bild** fügt eine [Bitmap](Bitmap/de.md)-Grafik (PNG, JPEG, JPG, BMP usw.) aus einer Datei als Ansicht auf einem Zeichnungsblatt ein.

![](images/TechDraw_Image_example.png ) 
*Ein auf dem Zeichnungsblatt eingefügtes Bild*



## Anwendung

1.  Wenn mehrere Zeichnungsblätter im Dokument vorhanden sind: Wahlweise das gewünschte Zeichnungsblatt durch Auswahl in der [Baumansicht](Tree_view/de.md) aktivieren.
2.  Es gibt mehrere Möglichkeiten, das Werkzeug aufzurufen:
    -   Die Schaltfläche **<img src="images/TechDraw_Image.svg" width=16px> [Bitmap-Grafik einfügen](TechDraw_Image/de.md)** drücken.
    -   Den Menüeintrag **TechDraw → TechDraw Ansichten → <img src="images/TechDraw_Image.svg" width=16px> Bitmap-Grafik einfügen** auswählen.
3.  Wenn mehrere Zeichnungsblätter im Dokument vorhanden sind und noch kein Blatt aktiviert wurde, wird das Dialogfeld **Blattauswahl** geöffnet: {{Version/de|0.20}}
    1.  Das gewünschte Blatt auswählen.
    2.  Die Schaltfläche **OK** drücken.
4.  Ein Dateidialog wird geöffnet.
5.  Einen Speicherort und einen Dateinamen auswählen.
6.  Die Bitmap-Grafik wird eingefügt.
7.  Wahlweise ihre {{PropertyData/de|Scale}} ändern, um ihre Größe anzupassen.



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

Siehe auch: [Autogenerierte API-Dokumentation](https://freecad.github.io/SourceDoc/) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

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
