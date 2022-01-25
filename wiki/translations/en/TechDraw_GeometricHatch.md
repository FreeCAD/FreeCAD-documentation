---
- GuiCommand:
   Name:TechDraw GeometricHatch
   MenuLocation:TechDraw → Apply Geometric Hatch to Face
   Workbenches:[TechDraw](TechDraw_Workbench.md)
   SeeAlso:[TechDraw Hatch](TechDraw_Hatch.md), [TechDraw Hatching](TechDraw_Hatching.md)
---

# TechDraw GeometricHatch/en

## Description

The GeometricHatch tool fills a closed region in a View with a pattern based on an AutoDesk PAT hatching specification. **Alternatively**, the [Hatch](TechDraw_Hatch.md) tool uses an [SVG](SVG.md) or [bitmap](bitmap.md) file as hatch pattern, see [Hatching](TechDraw_Hatching.md) for details.

<img alt="" src=images/TechDraw_GeomHatch_example.png  style="width:300px;"> 
*Geometric hatch pattern on a face*

## Usage

1.  Select an closed region in a View.
2.  Press the **<img src="images/TechDraw_GeometricHatch.svg" width=16px> [Apply Geometric Hatch to Face](TechDraw_GeometricHatch.md)** button
3.  A dialog will open where you can select your pattern, the scale, line weight and color.

## Notes

-   Hatching objects are vulnerable to the \"[topological naming problem](Topological_naming_problem.md)\". See [TechDraw LengthDimension](TechDraw_LengthDimension.md) for more information. It is recommended that hatching be one of the last steps in your drawing process.

A small set of sample patterns are available in:


```python
$INSTALL_DIR/data/Mod/TechDraw/PAT/FCPAT.pat
```


`$INSTALL_DIR`

is the directory where FreeCAD was installed, for example


```python
/usr/share/freecad/data/Mod/TechDraw/PAT/FCPAT.pat
```

## Properties

-    **Source**: The View and Face to receive the hatch pattern.

-    **File Pattern**: The location of the PAT file to use.

-    **Name Pattern**: The name of the PAT specification within File Pattern.

-    **Scale Pattern**: The scale to be applied to the pattern (must be \> 0.0).

-    **Weight Pattern**: The thickness of the pattern lines.

-    **Color Pattern**: The color for the pattern lines.

## Scripting


**See also:**

[TechDraw API](TechDraw_API.md) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

The GeometricHatch tool can be used in [macros](Macros.md) and from the [Python](Python.md) console by using the following functions:


```python
hatch = FreeCAD.ActiveDocument.addObject('TechDraw::DrawGeomHatch','GeomHatch')
hatch.Source = (view1,["Face0"])
hatch.FilePattern = "path/to/myPATfile.pat"
hatch.NamePattern = "Diamond"
rc = page.addView(hatch)
```

It is also possible to use TechDraw\'s geometric hatch engine to produce a compound object in the 3D space. One must take care that the base face lies on the XY plane, as the algorithm is not tailored yet for other cases:


```python
import TechDraw
face = Part.makePlane(10,10)
patfile = "path/to/myPATfile.pat"
pattern = "Diamond"
scale = 10
hatch = TechDraw.makeGeomHatch(face, scale, pattern, patfile)
Part.show(hatch)
```





{{TechDraw Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw GeometricHatch/en
