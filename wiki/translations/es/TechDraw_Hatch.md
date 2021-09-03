---
- GuiCommand:/es
   Name:TechDraw Hatch
   Name/es:DibujoTécnico Achurado
   MenuLocation:DibujoTécnico → Achurar un plano usando un archivo de imagen
   Workbenches:[DibujoTécnico](TechDraw_Workbench/es.md)
   SeeAlso:[DibujoTécnico Aplicar la achurado geométrica a la plano](TechDraw_GeometricHatch/es.md), [DibujoTécnico Achurado](TechDraw_Hatching/es.md)
---


</div>

## Descripción

La herramienta Achurado rellena una región cerrada en una Vista con un patrón de achurado, que pueden ser archivos [SVG](SVG/es.md) o [bitmap](bitmap/es.md). Por el contrario el <img alt="" src=images/TechDraw_GeometricHatch.svg  style="width:24px;"> [Achurado geométrico](TechDraw_GeometricHatch/es.md) utiliza un archivo de patrones PAT específico, vea [Achurado](TechDraw_Hatching/es.md) para más detalles.

<img alt="" src=images/TechDraw_Hatch_example.png  style="width:300px;">


*SVG achurado patrón en una cara*

## Utilización

1.  Select an closed region in a View.
2.  Press the **<img src="images/TechDraw_Hatch.svg" width=16px> [Hatch a Face using Image File](TechDraw_Hatch.md)** button
3.  A dialog will open where you can select the pattern file, the scale and color.

## Notas

-   Hatching objects are vulnerable to \"[topological naming](Topological_naming_problem.md)\" issues. See the information in the [TechDraw Dimension Length](TechDraw_Dimension_Length.md) tool for more information. It is recommended that hatching be one of the last steps in your drawing process.
-   Sample [SVG](SVG.md) patterns are available locally in


```python
$INSTALL_DIR/data/Mod/TechDraw/Patterns
```

where `$INSTALL_DIR` is the directory where FreeCAD was installed, for example 
```python
/usr/share/freecad/data/Mod/TechDraw/Patterns
``` and also on [GitHub](https://github.com/FreeCAD/FreeCAD/tree/master/src/Mod/TechDraw/Patterns).

## Propiedades

-    **Source**: The View and Face to receive the hatch pattern.

-    **Hatch Pattern**: Full path and filename to an SVG pattern file.

-    **Hatch Color**: Hatch pattern will be displayed in this color.

-    **Hatch Scale**: Hatch pattern size modifier.

## Guión


**See also:**

[TechDraw API](TechDraw_API.md) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

The Hatch tool can be used in [macros](Macros.md) and from the [Python](Python.md) console by using the following functions:


```python
hatch = FreeCAD.ActiveDocument.addObject('TechDraw::DrawHatch','Hatch')
hatch.Source = (view1,["Face0"])
hatch.HatchPattern = hatchFileSpec
rc = page.addView(hatch)
```


<div class="mw-translate-fuzzy">





</div>


{{TechDraw Tools navi

}}  
