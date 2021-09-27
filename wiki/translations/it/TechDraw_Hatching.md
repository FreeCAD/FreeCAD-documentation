# TechDraw Hatching/it
<div class="mw-translate-fuzzy">





</div>


{{TOCright}}

## Descrizione

TechDraw ha due strumenti per il tratteggio:

-   <img alt="" src=images/TechDraw_Hatch.svg  style="width:32px;"> [Tratteggio da modello](TechDraw_Hatch/it.md) (basato su tasselli)
-   <img alt="" src=images/TechDraw_GeometricHatch.svg  style="width:32px;"> [Tratteggio geometrico](TechDraw_GeometricHatch/it.md) (basato su linee).

## Utilizzo

1.  Selezionare una faccia

    :   <img alt="" src=images/SelectFace.png  style="width:150px;">
2.  A seconda dell\'esigenza, premere le icone <img alt="" src=images/TechDraw_Hatch.svg  style="width:24px;"> _.

**Risultato:** La faccia verrà tratteggiata inizialmente usando i valori predefiniti. **Nota**: modificare le proprietà del tratteggio per ottenere il tratteggio desiderato.

### Tratteggio da modello 

Il <img alt="" src=images/TechDraw_Hatch.svg  style="width:24px;"> [Tratteggio da modello](TechDraw_Hatch/it.md) utilizza delle tessere di base [SVG](SVG/it.md) o [bitmap](bitmap/it.md) per coprire la faccia selezionata.

Di solito le tessere SVG sono delle immagini di **64x64** pixel. Tutti i file di pattern forniti con FreeCAD sono disponibili su [GitHub](https://github.com/FreeCAD/FreeCAD/tree/master/src/Mod/TechDraw/Patterns).

Come riempimento è possibile utilizzare qualsiasi file bitmap (png, jpeg, ecc\...). **Nota:** I risultati migliori si ottengono con molte piccole immagini ripetute piuttosto che poche immagini grandi.


<div class="mw-translate-fuzzy">

I riempimenti di tratteggio predefiniti possono essere specificati nelle [Preferenze](TechDraw_Preferences/it.md).


</div>

### Tratteggio geometrico 

Il <img alt="" src=images/TechDraw_GeometricHatch.svg  style="width:24px;"> [Tratteggio geometrico](TechDraw_GeometricHatch/it.md) genera un modello di linee basato su una specifica letta da un file. Questo file è generalmente **compatibile con il formato PAT di AutoDesk® ampiamente utilizzato**. Una piccola selezione di modelli è inclusa nel file FCPAT.pat:


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

Il file `FCPAT.pat` può essere trovato nel seguente percorso:

-   **Windows**: `C:\Program Files\FreeCAD\data\Mod\TechDraw\PAT\`
-   **Mac**: `/Applications/FreeCAD.app/Contents/Mod/TechDraw/PAT/`
-   **Linux**: `/usr/share/freecad/Mod/TechDraw/PAT/`
    -   *freecad-daily PPA*: `/usr/share/freecad-daily/Mod/TechDraw/PAT/`


<div class="mw-translate-fuzzy">





</div>


{{TechDraw Tools navi

}}

---
[documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw Hatching/it
