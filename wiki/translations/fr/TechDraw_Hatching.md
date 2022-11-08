# TechDraw Hatching/fr
{{TOCright}}

## Description

L\'atelier TechDraw dispose de deux outils de hachurage    *

-   <img alt="" src=images/TechDraw_Hatch.svg  style="width   *32px;"> [TechDraw Hachures par motif](TechDraw_Hatch/fr.md) (sur la base d\'images en mosaïque SVG ou bitmap)
-   <img alt="" src=images/TechDraw_GeometricHatch.svg  style="width   *32px;"> [TechDraw Hachures géométriques](TechDraw_GeometricHatch/fr.md) (sur la base de lignes)

## Hachure basée sur une image 

<img alt="" src=images/TechDraw_Hatch.svg  style="width   *16px;"> [TechDraw Hachures par motif](TechDraw_Hatch/fr.md) utilise des tuiles au format [SVG](SVG/fr.md) ou bitmap ({{Version/fr|1.0}}) pour couvrir la face sélectionnée. L\'origine de la grille de tuiles correspondra au centre géométrique de la face.

Les tuiles [SVG](SVG/fr.md) sont typiquement des images de **64x64** pixels. Tous les fichiers de modèles fournis avec FreeCAD sont disponibles sur [GitHub](https   *//github.com/FreeCAD/FreeCAD/tree/master/src/Mod/TechDraw/Patterns).

Les motifs basés sur des images bitmap sont affichés avec une résolution fixe de 10 px/mm par rapport à la page.

Le fichier de motif de hachures par défaut peut être spécifié dans les [TechDraw Préférences](TechDraw_Preferences/fr.md).

### Motifs SVG disponibles 

Image   *Aluminium.svg\|aluminium Image   *Brick01.svg\|brick01 Image   *Concrete.svg\|concrete Image   *Cross.svg\|cross Image   *Cuprous.svg\|cuprous Image   *Diagonal1.svg\|diagonal1 Image   *Diagonal2.svg\|diagonal2 Image   *Earth.svg\|earth Image   *General_steel.svg\|general_steel Image   *Glass.svg\|glass Image   *Hatch45L.svg\|hatch45L Image   *Hatch45R.svg\|hatch45R Image   *Hbone.svg\|hbone Image   *Line.svg\|line Image   *Plastic.svg\|plastic Image   *Plus.svg\|plus Image   *Simple.svg\|simple Image   *Solid.svg\|solid Image   *Square.svg\|square Image   *Steel.svg\|steel Image   *Titanium.svg\|titanium Image   *Wood.svg\|wood Image   *Woodgrain.svg\|woodgrain Image   *Zinc.svg\|zinc

### Hachures géométriques 

<img alt="" src=images/TechDraw_GeometricHatch.svg  style="width   *16px;"> [TechDraw Hachures géométriques](TechDraw_GeometricHatch/fr.md) forme un motif de lignes basé sur une spécification lue dans un fichier. Ce fichier est généralement compatible avec le format AutoDesk® PAT, largement utilisé. Une petite sélection de motifs est incluse dans le fichier FCPAT.pat    *


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

Vous pouvez ajouter vos propres modèles si vous avez l\'autorisation d\'écriture sur FCPAT.pat, ou vous pouvez créer votre propre fichier \*.pat et le pointer dans [TechDraw Préférences](TechDraw_Preferences/fr.md).

### Chemin du fichier PAT 

Le fichier `FCPAT.pat` peut être trouvé à l\'emplacement suivant    *

-   **Windows**    * `C   *Program Files\FreeCAD\data\Mod\TechDraw\PAT\`
-   **Mac**    * `/Applications/FreeCAD.app/Contents/Mod/TechDraw/PAT/`
-   **Linux**    * `/usr/share/freecad/Mod/TechDraw/PAT/`
    -   *freecad-daily PPA*    * `/usr/share/freecad-daily/Mod/TechDraw/PAT/`





{{TechDraw_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw Hatching/fr
