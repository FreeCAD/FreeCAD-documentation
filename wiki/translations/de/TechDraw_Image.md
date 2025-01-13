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


{{Version/de|1.0}}

: Auch das Werkzeug [TechDraw Ansicht](TechDraw_View/de.md) kann eine Bildansicht erstellen.

![](images/TechDraw_Image_example.png ) 
*Ein auf dem Zeichnungsblatt eingefügtes Bild*



## Anwendung

1.  Wenn mehrere Zeichnungsblätter im Dokument vorhanden sind: Wahlweise das gewünschte Zeichnungsblatt durch Auswahl in der [Baumansicht](Tree_view/de.md) aktivieren.
2.  Den Menüeintrag **TechDraw → TechDraw Ansichten → <img src="images/TechDraw_Image.svg" width=16px> Bitmap-Grafik einfügen** auswählen.
3.  Wenn mehrere Zeichnungsblätter im Dokument vorhanden sind und noch kein Blatt aktiviert wurde, wird das Dialogfeld **Blattauswahl** geöffnet:
    1.  Das gewünschte Blatt auswählen.
    2.  Die Schaltfläche **OK** drücken.
4.  Ein Datei-Browser wird geöffnet.
5.  Eine Bilddatei auswählen.
6.  Eine Bildansicht wird eingefügt.
7.  Wahlweise ihre {{PropertyData/de|Scale}} Anpassen, um ihre Größe einzustellen.



## Eigenschaften

Siehe auch: [Eigenschafteneditor](Property_editor/de.md).

Eine Bildansicht, oder formal ein {{Incode|TechDraw::DrawViewImage}}-Objekt, besitzt die gemeinsamen [Eigenschaften](TechDraw_View/de#Eigenschaften_der_Bauteilansicht.md) aller Ansichtsarten. Sie enthält außerdem die folgenden Eigenschaften:



### Daten


{{TitleProperty|Image}}

-    {{PropertyData/de|Image File|File}}(Bilddatei): Die Datei, die dieses Bitmap-Bild enthält.

-    {{PropertyData/de|Image Included|FileIncluded}}(Enthaltenes Bild): Eingebettete Bilddatei. Nur systeminterne Verwendung.

-    {{PropertyData/de|Width|Float}}: Die Breite des zugeschnittenen Bildes in mm.

-    {{PropertyData/de|Height|Float}}: Die Höhe des zugeschnittenen Bildes in mm.

:   Die beiden letzten Eigenschaften werden nur verwendet, wenn der Wert der {{PropertyView/de|Crop}} `True` ist.



### Ansicht


{{TitleProperty|Image}}

-    {{PropertyView/de|Crop|Bool}}: Beschneidet das Bild entsprechen der {{PropertyData/de|Width}} und der {{PropertyData/de|Height}}.



## Skripten

Siehe auch: [Autogenerierte API-Dokumentation](https://freecad.github.io/SourceDoc/) und [Grundlagen der Skripterstellung in FreeCAD](FreeCAD_Scripting_Basics/de.md).

Das Werkzeug Bild kann in [Makros](Macros/de.md) und von der [Python](Python/de.md)-Konsole aus mit den folgenden Funktionen verwendet werden:


```python
dvi = FreeCAD.ActiveDocument.addObject('TechDraw::DrawViewImage','TestImage')
rc = page.addView(dvi)
dvi.ImageFile = "pathToMy/imageFile.png"
dvi.Height = 200
dvi.Width  = 200
```





{{TechDraw_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw Image/de
