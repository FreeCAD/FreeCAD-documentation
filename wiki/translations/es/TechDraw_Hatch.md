---
- GuiCommand:
   Name: TechDraw Hatch
   Name/es: DibujoTécnico Achurado
   MenuLocation: DibujoTécnico - Achurar un plano usando un archivo de imagen
   Workbenches: [DibujoTécnico](TechDraw_Workbench/es.md)
   SeeAlso: [DibujoTécnico Aplicar la achurado geométrica a la plano](TechDraw_GeometricHatch/es.md), [DibujoTécnico Achurado](TechDraw_Hatching/es.md)
---

# TechDraw Hatch/es


</div>



## Descripción


<div class="mw-translate-fuzzy">

La herramienta Achurado rellena una región cerrada en una Vista con un patrón de achurado, que pueden ser archivos [SVG](SVG/es.md) o [bitmap](bitmap/es.md). Por el contrario el <img alt="" src=images/TechDraw_GeometricHatch.svg  style="width:24px;"> [Achurado geométrico](TechDraw_GeometricHatch/es.md) utiliza un archivo de patrones PAT específico, vea [Achurado](TechDraw_Hatching/es.md) para más detalles.


</div>

<img alt="" src=images/TechDraw_Hatch_example.png  style="width:300px;">



*SVG achurado patrón en una cara*



## Utilización


<div class="mw-translate-fuzzy">

1.  Seleccione una región cerrada en una Vista.
2.  Pulse el **<img src="images/TechDraw_Hatch.svg" width=16px> [Achurar un plano usando un archivo de imagen](TechDraw_Hatch/es.md)
**
3.  Se abrirá un diálogo en el que podrá seleccionar el archivo de patrón, la escala y el color.


</div>



## Notas

-   Hatching objects are vulnerable to the \"[topological naming problem](Topological_naming_problem.md)\". See [TechDraw LengthDimension](TechDraw_LengthDimension.md) for more information. It is recommended that hatching be one of the last steps in your drawing process.
-   Sample [SVG](SVG.md) patterns are available locally in:

:   
    
```python
    $INSTALL_DIR/data/Mod/TechDraw/Patterns
    
```
    

:   Where `$INSTALL_DIR` is the directory where FreeCAD was installed, for example:

:   
    
```python
    /usr/share/freecad/data/Mod/TechDraw/Patterns
    
```
    


<div class="mw-translate-fuzzy">

y también en [GitHub](https://github.com/FreeCAD/FreeCAD/tree/master/src/Mod/TechDraw/Patterns).


</div>



## Propiedades

-    **Source**: The View and Face to receive the hatch pattern.

-    **Hatch Pattern**: Full path and filename to an SVG pattern file.

-    **Hatch Color**: Hatch pattern will be displayed in this color.

-    **Hatch Scale**: Hatch pattern size modifier.



## Guión


**Ver también:**

[DibujoTécnico API](TechDraw_API/es.md) y [FreeCAD Fundamentos de Guión](FreeCAD_Scripting_Basics/es.md).


<div class="mw-translate-fuzzy">

La herramienta Achurado se puede utilizar en [macros](Macros/es.md) y desde la consola de [Python](Python/es.md) utilizando las siguientes funciones:


</div>


```python
hatch = FreeCAD.ActiveDocument.addObject("TechDraw::DrawHatch", "Hatch")
hatch.Source = (view1, ["Face0"])
hatch.HatchPattern = hatchFileSpec
page.addView(hatch)
```


<div class="mw-translate-fuzzy">





</div>


{{TechDraw Tools navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw Hatch/es
