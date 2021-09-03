---
- GuiCommand:   Name:TechDraw  Image   Workbenches:[[TechDraw_Workbench   TechDraw]]|MenuLocation:TechDraw → Image   Shortcut:   SeeAlso:---


</div>


<div class="mw-translate-fuzzy">

## Descriere

Instrumentul Image inserează o imagina tip bitmap (png,jpeg,jpg,bmp,etc) dintr-un fișier în pagină ca vedere


</div>

The Image tool inserts a [bitmap](bitmap.md) image (PNG, TIFF, JPEG, etc.) from a file into the page as a view.

![](images/TechDraw_Image_example.png ) *Image inserted in the drawing page*


<div class="mw-translate-fuzzy">

## Cum se folosește {#cum_se_folosește}

1.  Apăsați butonul **<img src="images/Techdraw-image.png" width=24px> [Image](TechDraw_Image.md)
**
2.  Se va deschide un dialog. Selectați o locație și un nume de fișier.


</div>

1.  Press the **<img src="images/TechDraw_Image.svg" width=16px> [Insert Bitmap Image](TechDraw_Image.md)** button
2.  A file dialog will open. Select a location and file name.


<div class="mw-translate-fuzzy">

## Proprietăți

-   n/a


</div>

-   Use the Scale property to adjust the size of the image.
-   Use the Width and Height properties to clip the image.


<div class="mw-translate-fuzzy">

## Script

Fișiere Bitmap Images pot fi inserate într-o pagină de desen folosind Python.


</div>


**See also:**

[TechDraw API](TechDraw_API.md) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

The Image tool can be used in [macros](Macros.md) and from the [Python](Python.md) console by using the following functions:


```python
dvi = FreeCAD.ActiveDocument.addObject('TechDraw::DrawViewImage','TestImage')
rc = page.addView(dvi)
dvi.ImageFile = "pathToMy/imageFile.png"
dvi.Height = 200
dvi.Width  = 200
```





{{TechDraw Tools navi

}}  
