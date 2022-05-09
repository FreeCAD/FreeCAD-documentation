# TechDraw Hatching/it
{{TOCright}}

## Descrizione


<div class="mw-translate-fuzzy">

TechDraw ha due strumenti per il tratteggio   *

-   <img alt="" src=images/TechDraw_Hatch.svg  style="width   *32px;"> [Tratteggio da modello](TechDraw_Hatch/it.md) (basato su tasselli)
-   <img alt="" src=images/TechDraw_GeometricHatch.svg  style="width   *32px;"> [Tratteggio geometrico](TechDraw_GeometricHatch/it.md) (basato su linee).


</div>

## Image based hatch 


<div class="mw-translate-fuzzy">

### Tratteggio da modello 

Il <img alt="" src=images/TechDraw_Hatch.svg  style="width   *24px;"> [Tratteggio da modello](TechDraw_Hatch/it.md) utilizza delle tessere di base [SVG](SVG/it.md) o [bitmap](bitmap/it.md) per coprire la faccia selezionata.


</div>

Di solito le tessere SVG sono delle immagini di **64x64** pixel. Tutti i file di pattern forniti con FreeCAD sono disponibili su [GitHub](https   *//github.com/FreeCAD/FreeCAD/tree/master/src/Mod/TechDraw/Patterns).


<div class="mw-translate-fuzzy">

I riempimenti di tratteggio predefiniti possono essere specificati nelle [Preferenze](TechDraw_Preferences/it.md).


</div>

### Available patterns 

Image   *Aluminium.svg\|aluminium Image   *Brick01.svg\|brick01 Image   *Concrete.svg\|concrete Image   *Cross.svg\|cross Image   *Cuprous.svg\|cuprous Image   *Diagonal1.svg\|diagonal1 Image   *Diagonal2.svg\|diagonal2 Image   *Earth.svg\|earth Image   *General\_steel.svg\|general\_steel Image   *Glass.svg\|glass Image   *Hatch45L.svg\|hatch45L Image   *Hatch45R.svg\|hatch45R Image   *Hbone.svg\|hbone Image   *Line.svg\|line Image   *Plastic.svg\|plastic Image   *Plus.svg\|plus Image   *Simple.svg\|simple Image   *Solid.svg\|solid Image   *Square.svg\|square Image   *Steel.svg\|steel Image   *Titanium.svg\|titanium Image   *Wood.svg\|wood Image   *Woodgrain.svg\|woodgrain Image   *Zinc.svg\|zinc

## Geometric hatch 


<div class="mw-translate-fuzzy">

### Tratteggio geometrico 

Il <img alt="" src=images/TechDraw_GeometricHatch.svg  style="width   *24px;"> [Tratteggio geometrico](TechDraw_GeometricHatch/it.md) genera un modello di linee basato su una specifica letta da un file. Questo file è generalmente **compatibile con il formato PAT di AutoDesk® ampiamente utilizzato**. Una piccola selezione di modelli è inclusa nel file FCPAT.pat   *


</div>


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


<div class="mw-translate-fuzzy">

Se si dispone dell\'autorizzazione alla scrittura è possibile aggiungere i propri schemi in FCPAT.pat, oppure è possibile creare il proprio file \*.pat e indicarlo nelle [Preferenze](TechDraw_Preferences/it.md).


</div>

### Percorso del file PAT 

Il file `FCPAT.pat` può essere trovato nel seguente percorso   *

-   **Windows**   * `C   *Program Files\FreeCAD\data\Mod\TechDraw\PAT\`
-   **Mac**   * `/Applications/FreeCAD.app/Contents/Mod/TechDraw/PAT/`
-   **Linux**   * `/usr/share/freecad/Mod/TechDraw/PAT/`
    -   *freecad-daily PPA*   * `/usr/share/freecad-daily/Mod/TechDraw/PAT/`





{{TechDraw_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw Hatching/it
