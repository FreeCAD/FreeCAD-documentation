---
- GuiCommand:/fr
   Name:TechDraw Image
   Name/fr:TechDraw Image
   MenuLocation:TechDraw → Insérer une image Bitmap
   Workbenches:[TechDraw](TechDraw_Workbench/fr.md)
   SeeAlso:[TechDraw Symbole SVG](TechDraw_Symbol/fr.md)
---

## Description

L\'outil Image insère une image [bitmap](bitmap/fr.md) (png, jpeg, jpg, bmp, etc.) à partir d\'un fichier dans la page en tant que vue.

![](images/TechDraw_Image_example.png ) *Image insérée dans la page de dessin*

## Comment faire 

1.  Appuyez sur le bouton**<img src="images/TechDraw_Image.svg" width=16px> [Insérer une image Bitmap](TechDraw_Image/fr.md)
**
2.  Une boîte de dialogue de fichier s\'ouvrira. Sélectionnez un emplacement et un nom de fichier.

## Propriétés

-   Utilisez la propriété Scale (échelle) pour ajuster la taille de l\'image.
-   Utilisez les propriétés Width (largeur) et Height (hauteur) pour découper l\'image.

## Script


**Voir aussi:**

[TechDraw API](TechDraw_API/fr.md) et [Débuter avec les scripts](FreeCAD_Scripting_Basics/fr.md).

L\'outil Image peut être utilisé dans des [macros](Macros/fr.md) et à partir de la console [Python](Python/fr.md) à l\'aide des fonctions suivantes :


```python
dvi = FreeCAD.ActiveDocument.addObject('TechDraw::DrawViewImage','TestImage')
rc = page.addView(dvi)
dvi.ImageFile = "pathToMy/imageFile.png"
dvi.Height = 200
dvi.Width  = 200
```





{{TechDraw Tools navi

}}  
