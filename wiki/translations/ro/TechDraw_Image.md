# TechDraw Image/ro
---
 GuiCommand:   Name: TechDraw  Image   Workbenches: TechDraw_Workbench   TechDraw|MenuLocation: TechDraw , Image   Shortcut:    SeeAlso: ---


</div>




<div class="mw-translate-fuzzy">

## Descriere

Instrumentul Image inserează o imagina tip bitmap (png,jpeg,jpg,bmp,etc) dintr-un fișier în pagină ca vedere


</div>

The **TechDraw Image** tool inserts a [bitmap](Bitmap.md) image (PNG, TIFF, JPEG, etc.) from a file into the page as a view.

![](images/TechDraw_Image_example.png ) 
*Image inserted in the drawing page*




<div class="mw-translate-fuzzy">

## Cum se folosește 


</div>

1.  If there are multiple drawing pages in the document: optionally activate the desired page by selecting it in the [Tree view](Tree_view.md).
2.  There are several ways to invoke the tool:
    -   Press the **<img src="images/TechDraw_Image.svg" width=16px> [Insert Bitmap Image](TechDraw_Image.md)** button.
    -   Select the **TechDraw → TechDraw Views → <img src="images/TechDraw_Image.svg" width=16px> Insert Bitmap Image** option from the menu.
3.  If there are multiple drawing pages in the document and you have not yet activated a page, the **Page Chooser** dialog box opens: <small>(v0.20)</small> 
    1.  Select the desired page.
    2.  Press the **OK** button.
4.  A file dialog opens.
5.  Select a location and file name.
6.  The image is inserted.
7.  Optionally change its **Scale** property to adjust its size.




<div class="mw-translate-fuzzy">

## Proprietăți

-   n/a


</div>

See also [TechDraw View](TechDraw_View#Properties.md).

### Data


{{TitleProperty|Image}}

-    **Image File|File**: The file containing this bitmap.

-    **Image Included|FileIncluded**: Embedded image file. System use only.

-    **Width|Float**: The width of the cropped image in mm. Only used if **Crop** is `True`.

-    **Height|Float**: The height of the cropped image in mm. Idem.

### View


{{TitleProperty|Image}}

-    **Crop|Bool**: Crop the image to **Width** x **Height**.




<div class="mw-translate-fuzzy">

## Script

Fișiere Bitmap Images pot fi inserate într-o pagină de desen folosind Python.


</div>

See also: [Autogenerated API documentation](https://freecad.github.io/SourceDoc/) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

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



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw Image/ro
