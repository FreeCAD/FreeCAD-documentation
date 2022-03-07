# TechDraw Hatching/en
{{TOCright}}

## Description

The TechDraw workbench has two hatching tools:

-   <img alt="" src=images/TechDraw_Hatch.svg  style="width:32px;"> [Hatch Face using Image File](TechDraw_Hatch.md) (tile based)
-   <img alt="" src=images/TechDraw_GeometricHatch.svg  style="width:32px;"> [Apply Geometric Hatch to Face](TechDraw_GeometricHatch.md) (line based)

## Usage

1.  Select a Face

    :   <img alt="" src=images/SelectFace.png  style="width:150px;">
2.  Depending on the need, press either <img alt="" src=images/TechDraw_Hatch.svg  style="width:24px;"> [Hatch Face using Image File](TechDraw_Hatch.md) or <img alt="" src=images/TechDraw_GeometricHatch.svg  style="width:24px;"> [Apply Geometric Hatch to Face](TechDraw_GeometricHatch.md) icons.

**Result:** The face will be hatched initially using default values. **Note**: Edit the hatch properties to get the desired pattern.

<img alt="" src=images/TechDraw_Hatch.svg  style="width:24px;"> [Hatch Face using Image File](TechDraw_Hatch.md) uses [SVG](SVG.md) or [bitmap](bitmap.md) based tiles to cover the selected Face.

[SVG](SVG.md) tiles are typically **64x64** pixel images. All pattern files that come with FreeCAD are available on [GitHub](https://github.com/FreeCAD/FreeCAD/tree/master/src/Mod/TechDraw/Patterns).

Any [bitmap](bitmap.md) file can be used (PNG, JPG, etc.) as a fill. **Note:** Results are best with many small repeated images rather than fewer larger images.

The default hatch pattern file can be specified in the [TechDraw Preferences](TechDraw_Preferences.md).

<img alt="" src=images/TechDraw_GeometricHatch.svg  style="width:24px;"> [Apply Geometric Hatch to Face](TechDraw_GeometricHatch.md) forms a pattern of lines based on a specification read from a file. This file is generally **compatible with the widely used AutoDesk® PAT format**. A small selection of patterns is included in the FCPAT.pat file:


```python
; standard PAT patterns

*Diamond, 45 diagonals L & R, Solid, 1.0 mm separation
45,0,0,0,1.0
-45,0,0,0,1.0
*Diamond2, 45 diagonals L & R, Solid, 2.0 mm separation
45,0,0,0,2.0
-45,0,0,0,2.0
*Diamond4, 45 diagonals L & R, Solid, 4.0 mm separation
45,0,0,0,4.0
-45,0,0,0,4.0
*Diagonal4, 45 diagonal R, Solid, 4.0 mm separation
45,0,0,0,4.0
*Diagonal5, 45 diagonal L, Solid, 4.0 mm separation
-45,0,0,0,4.0
*Square, square grid, Solid, 5.0 mm separation 
90,1,1,0,5.0
0,0,0,1,5.0
*Horizontal5, horizontal lines, Solid 5.0 separation
0,0,0,0,5.0
*Vertical5, vertical lines, Solid, 5.0 separation
90,0,0,0,5.0
```

You can add your own patterns if you have write permission to FCPAT.pat, or you can create your own \*.pat file and point to it in [TechDraw Preferences](TechDraw_Preferences.md).

### PAT File Path 

The `FCPAT.pat` file can be found in the following location.

-   **Windows**: `C:\Program Files\FreeCAD\data\Mod\TechDraw\PAT\`
-   **Mac**: `/Applications/FreeCAD.app/Contents/Mod/TechDraw/PAT/`
-   **Linux**: `/usr/share/freecad/Mod/TechDraw/PAT/`
    -   *freecad-daily PPA*: `/usr/share/freecad-daily/Mod/TechDraw/PAT/`





{{TechDraw Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw Hatching/en
