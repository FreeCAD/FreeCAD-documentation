# Draft Pattern/it
{{TOCright}}

## Descrizione


<div class="mw-translate-fuzzy">

Tutti gli oggetti Draft chiudibili, come [rettangolo](Draft_Rectangle.md), [cerchio](Draft_Circle.md), [ellisse](Draft_Ellipse.md), [polilinee](Draft_Wire.md) o [poligoni](Draft_Polygon.md), quando sono chiusi e visualizzati in \"Flat Lines\", possono essere riempiti con un modello di tratteggio, al posto del colore della faccia, impostando la loro proprietà \"Pattern\".


</div>

![](images/DraftPatternSample.png )


<div class="mw-translate-fuzzy">

![](images/DraftPatternSample.png )


</div>

## Utilizzo


<div class="mw-translate-fuzzy">

1.  Selezionare l\'oggetto
2.  In Vista combinata → Dati: impostare true per Make Face in modo da dare all\'oggetto una faccia riempibile con il tratteggio
3.  In Vista combinata → Vista → Pattern: specificare un modello di tratteggio con cui riempire il contorno
4.  In Vista combinata → Vista → Pattern Size: specificare la dimensione del tratteggio


</div>

## Available patterns 

Image:Aluminium.svg\|aluminium Image:Brick01.svg\|brick01 Image:Concrete.svg\|concrete Image:Cross.svg\|cross Image:Cuprous.svg\|cuprous Image:Diagonal1.svg\|diagonal1 Image:Diagonal2.svg\|diagonal2 Image:Earth.svg\|earth Image:General\_steel.svg\|general\_steel Image:Glass.svg\|glass Image:Hatch45L.svg\|hatch45L Image:Hatch45R.svg\|hatch45R Image:Hbone.svg\|hbone Image:Line.svg\|line Image:Plastic.svg\|plastic Image:Plus.svg\|plus Image:Simple.svg\|simple Image:Solid.svg\|solid Image:Square.svg\|square Image:Steel.svg\|steel Image:Titanium.svg\|titanium Image:Wood.svg\|wood Image:Woodgrain.svg\|woodgrain Image:Zinc.svg\|zinc

## Notes

-   SVG patterns are stored in {{FileName|.SVG}} files. It is possible to use your own custom patterns. See [Preferences](#Preferences.md).
-   The patterns themselves are not saved in the FreeCAD document. Objects whose **Pattern** cannot be found are displayed with a solid face color instead.

## Preferences

See also: [Preferences Editor](Preferences_Editor.md) and [Draft Preferences](Draft_Preferences.md).

-   To specify a directory with addition SVG patterns: **Edit → Preferences... → Draft → Visual settings → Alternate SVG patterns location**. Select a file in the directory and then remove the filename in the preferences input box, leaving only the path. After changing this preference you must restart FreeCAD.
-   The **Edit → Preferences... → Draft → Visual settings → SVG pattern resolution** preference is not used.
-   To change the **Pattern Size** used for new objects: **Edit → Preferences... → Draft → Visual settings → SVG pattern default size**.



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Pattern/it
