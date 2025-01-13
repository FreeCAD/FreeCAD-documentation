# TechDraw Hatching/it
## Descrizione

TechDraw include due strumenti per il tratteggio:

-   <img alt="" src=images/TechDraw_Hatch.svg  style="width:32px;"> [TechDraw Tratteggio da modello](TechDraw_Hatch/it.md) (basato su tasselli SVG o immagini bitmap)
-   <img alt="" src=images/TechDraw_GeometricHatch.svg  style="width:32px;"> [TechDraw Tratteggio geometrico](TechDraw_GeometricHatch/it.md) (basato su linee).



## Tratteggio basato su immagine 

<img alt="" src=images/TechDraw_Hatch.svg  style="width:16px;"> [TechDraw Tratteggio](TechDraw_Hatch/it.md) utilizza immagini affiancate [SVG](SVG/it.md) o bitmap ({{Version/it|0.21}}) per coprire la faccia selezionata. L\'origine della griglia di piastrellatura corrisponderà al centro geometrico della faccia.

Di solito le tessere SVG sono delle immagini di **64x64** pixel. Tutti i file di pattern forniti con FreeCAD sono disponibili su [GitHub](https://github.com/FreeCAD/FreeCAD/tree/master/src/Mod/TechDraw/Patterns).

I modelli basati su bitmap vengono visualizzati con una risoluzione fissa di 10 px/mm rispetto alla pagina.

I modelli di tratteggio predefiniti possono essere specificati nelle [Preferenze](TechDraw_Preferences/it.md).



### Modelli SVG disponibili 

Image:Aluminium.svg\|aluminium Image:Brick01.svg\|brick01 Image:Concrete.svg\|concrete Image:Cross.svg\|cross Image:Cuprous.svg\|cuprous Image:Diagonal1.svg\|diagonal1 Image:Diagonal2.svg\|diagonal2 Image:Earth.svg\|earth Image:General_steel.svg\|general_steel Image:Glass.svg\|glass Image:Hatch45L.svg\|hatch45L Image:Hatch45R.svg\|hatch45R Image:Hbone.svg\|hbone Image:Line.svg\|line Image:Plastic.svg\|plastic Image:Plus.svg\|plus Image:Simple.svg\|simple Image:Solid.svg\|solid Image:Square.svg\|square Image:Steel.svg\|steel Image:Titanium.svg\|titanium Image:Wood.svg\|wood Image:Woodgrain.svg\|woodgrain Image:Zinc.svg\|zinc



## Tratteggio geometrico 

Il <img alt="" src=images/TechDraw_GeometricHatch.svg  style="width:16px;"> [Tratteggio geometrico](TechDraw_GeometricHatch/it.md) genera un modello di linee basato su una specifica letta da un file. Questo file è generalmente compatibile con il formato PAT di AutoDesk® ampiamente utilizzato. Una piccola selezione di modelli è inclusa nel file FCPAT.pat:


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

Se si dispone dell\'autorizzazione alla scrittura è possibile aggiungere i propri schemi in FCPAT.pat, oppure è possibile creare il proprio file \*.pat e indicarlo nelle [Preferenze](TechDraw_Preferences/it.md).



### Percorso del file PAT 

Il file `FCPAT.pat` può essere trovato nel seguente percorso:

-   **Windows**: `C:\Program Files\FreeCAD\data\Mod\TechDraw\PAT\`
-   **Mac**: `/Applications/FreeCAD.app/Contents/Mod/TechDraw/PAT/`
-   **Linux**: `/usr/share/freecad/Mod/TechDraw/PAT/`
    -   *freecad-daily PPA*: `/usr/share/freecad-daily/Mod/TechDraw/PAT/`





{{TechDraw_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw Hatching/it
