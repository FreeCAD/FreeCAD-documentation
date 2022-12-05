# TechDraw Image/it
---
- GuiCommand:/it   Name:TechDraw Image   Name/it:Immagine bitmap   Workbenches:[MenuLocation:TechDraw → Immagine bitmap   Shortcut:   SeeAlso:[[TechDraw Symbol/it|Simbolo SVG](TechDraw_Workbench/it___TechDraw]].md)---


</div>

## Descrizione

Lo strumento Immagine inserisce un\'immagine [bitmap](bitmap/it.md) (PNG, TIFF, JPEG, ecc.) da un file nella pagina come una vista

![](images/TechDraw_Image_example.png ) 
*Immagine inserita nella pagina di disegno*

## Uso


<div class="mw-translate-fuzzy">

1.  Premere il pulsante **<img src="images/TechDraw_Image.svg" width=16px> [Immagine bitmap](TechDraw_Image/it.md)**.
2.  Si apre una finestra di dialogo. Selezionare un percorso e il nome file.


</div>

## Proprietà

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

## Script


<div class="mw-translate-fuzzy">


**Vedere anche:**

[TechDraw API](TechDraw_API/it.md) e [Nozioni di base sugli script di FreeCAD](FreeCAD_Scripting_Basics/it.md).


</div>


<div class="mw-translate-fuzzy">

Lo strumento Image può essere utilizzato nelle [macro](macros/it.md) e dalla [console di Python](FreeCAD_Scripting_Basics/it.md) tramite la seguente funzione:


</div>


```python
dvi = FreeCAD.ActiveDocument.addObject('TechDraw::DrawViewImage','TestImage')
rc = page.addView(dvi)
dvi.ImageFile = "pathToMy/imageFile.png"
dvi.Height = 200
dvi.Width  = 200
```


<div class="mw-translate-fuzzy">





</div>


{{TechDraw Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw Image/it
