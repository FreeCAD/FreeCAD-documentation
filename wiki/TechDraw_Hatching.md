# TechDraw Hatching
## Description

The TechDraw workbench includes two hatching tools   *

-   <img alt="" src=images/TechDraw_Hatch.svg  style="width   *32px;"> [TechDraw Hatch](TechDraw_Hatch.md) (based on tiled SVG images)
-   <img alt="" src=images/TechDraw_GeometricHatch.svg  style="width   *32px;"> [TechDraw GeometricHatch](TechDraw_GeometricHatch.md) (line based)

## Image based hatch 

<img alt="" src=images/TechDraw_Hatch.svg  style="width   *16px;"> [TechDraw Hatch](TechDraw_Hatch.md) uses tiled [SVG](SVG.md) images to cover the selected Face.

[SVG](SVG.md) tiles are typically **64x64** pixel images. All pattern files that come with FreeCAD are available on [GitHub](https   *//github.com/FreeCAD/FreeCAD/tree/master/src/Mod/TechDraw/Patterns).

The default hatch pattern file can be specified in the [TechDraw Preferences](TechDraw_Preferences.md).

### Available patterns 



Image   *Aluminium.svg\|aluminium Image   *Brick01.svg\|brick01 Image   *Concrete.svg\|concrete Image   *Cross.svg\|cross Image   *Cuprous.svg\|cuprous Image   *Diagonal1.svg\|diagonal1 Image   *Diagonal2.svg\|diagonal2 Image   *Earth.svg\|earth Image   *General\_steel.svg\|general\_steel Image   *Glass.svg\|glass Image   *Hatch45L.svg\|hatch45L Image   *Hatch45R.svg\|hatch45R Image   *Hbone.svg\|hbone Image   *Line.svg\|line Image   *Plastic.svg\|plastic Image   *Plus.svg\|plus Image   *Simple.svg\|simple Image   *Solid.svg\|solid Image   *Square.svg\|square Image   *Steel.svg\|steel Image   *Titanium.svg\|titanium Image   *Wood.svg\|wood Image   *Woodgrain.svg\|woodgrain Image   *Zinc.svg\|zinc



## Geometric hatch 

<img alt="" src=images/TechDraw_GeometricHatch.svg  style="width   *16px;"> [TechDraw GeometricHatch](TechDraw_GeometricHatch.md) forms a pattern of lines based on a specification read from a file. This file is generally **compatible with the widely used AutoDesk® PAT format**. A small selection of patterns is included in the FCPAT.pat file   *

 
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

-   **Windows**   * `C   *Program Files\FreeCAD\data\Mod\TechDraw\PAT\`
-   **Mac**   * `/Applications/FreeCAD.app/Contents/Mod/TechDraw/PAT/`
-   **Linux**   * `/usr/share/freecad/Mod/TechDraw/PAT/`
    -   *freecad-daily PPA*   * `/usr/share/freecad-daily/Mod/TechDraw/PAT/`




 {{TechDraw_Tools_navi}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw Hatching
