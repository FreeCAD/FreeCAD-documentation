---
- GuiCommand:/ru
   Name/ru:Вставить растровое изображение
   Name:TechDraw_Image
   MenuLocation:TechDraw → Вставить растровое изображение
   Workbenches:[TechDraw](TechDraw_Workbench/ru.md)
   SeeAlso:[Вставить SVG знак](TechDraw_Symbol/ru.md)
---

# TechDraw Image/ru

## Описание

The Image tool inserts a [bitmap](bitmap.md) image (PNG, TIFF, JPEG, etc.) from a file into the page as a view.

![](images/TechDraw_Image_example.png ) 
*Image inserted in the drawing page*

## Применение

1.  Press the **<img src="images/TechDraw_Image.svg" width=16px> [Insert Bitmap Image](TechDraw_Image.md)** button
2.  A file dialog will open. Select a location and file name.

## Свойства

-   Use the Scale property to adjust the size of the image.
-   Use the Width and Height properties to clip the image.

## Программирование


**См. так же:**

[TechDraw API](TechDraw_API/ru.md) и [Основы составления скриптов FreeCAD](FreeCAD_Scripting_Basics/ru.md).

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
[documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw Image/ru
