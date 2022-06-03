# Draft Pattern/cs
{{TOCright}}

## Description


<div class="mw-translate-fuzzy">

## Popis

Všechny objekty Kreslení, které mohou být uzavřené, jako je [obdélník](Draft_Rectangle/cs.md), [kružnice](Draft_Circle/cs.md), [elipsa](Draft_Ellipse/cs.md), [drát](Draft_Wire/cs.md) nebo [mnohoúhelník](Draft_Polygon/cs.md), jsou-li uzavřeny a je nastaven zobrazovací mód na \"Flat Lines\", mohou zobrazovat šrafovací vzor, místo barevné plochy, pomocí nastavení vlastnosti \"Vzor\".


</div>

![](images/DraftPatternSample.png )


<div class="mw-translate-fuzzy">

![](images/DraftPatternSample.png )


</div>

## Usage


<div class="mw-translate-fuzzy">

## Použití

1.  Vyberte objekt
2.  V rozbalovacím pohledu → Data   * nastavte Vytvořit pochu na true abyste zajistili, že objekt bude mít plochy, kde bude vzor
3.  V rozbalovacím pohledu → Pohled → Vzor   * specifikujte šrafovací vzor pro vyplnění drátů
4.  V rozbalovacím pohledu → Pohled → Velikost vzoru   * specifikujte rozměr šrafovacího vzoru


</div>

## Available patterns 

Image   *Aluminium.svg\|aluminium Image   *Brick01.svg\|brick01 Image   *Concrete.svg\|concrete Image   *Cross.svg\|cross Image   *Cuprous.svg\|cuprous Image   *Diagonal1.svg\|diagonal1 Image   *Diagonal2.svg\|diagonal2 Image   *Earth.svg\|earth Image   *General\_steel.svg\|general\_steel Image   *Glass.svg\|glass Image   *Hatch45L.svg\|hatch45L Image   *Hatch45R.svg\|hatch45R Image   *Hbone.svg\|hbone Image   *Line.svg\|line Image   *Plastic.svg\|plastic Image   *Plus.svg\|plus Image   *Simple.svg\|simple Image   *Solid.svg\|solid Image   *Square.svg\|square Image   *Steel.svg\|steel Image   *Titanium.svg\|titanium Image   *Wood.svg\|wood Image   *Woodgrain.svg\|woodgrain Image   *Zinc.svg\|zinc

## Notes

-   SVG patterns are stored in **.SVG** files. It is possible to use your own custom patterns. See [Preferences](#Preferences.md).
-   The patterns themselves are not saved in the FreeCAD document. Objects whose **Pattern** cannot be found are displayed with a solid face color instead.

## Preferences

See also   * [Preferences Editor](Preferences_Editor.md) and [Draft Preferences](Draft_Preferences.md).

-   To specify a directory with addition SVG patterns   * **Edit → Preferences... → Draft → Visual settings → Alternate SVG patterns location**. Select a file in the directory and then remove the filename in the preferences input box, leaving only the path. After changing this preference you must restart FreeCAD.
-   The **Edit → Preferences... → Draft → Visual settings → SVG pattern resolution** preference is not used.
-   To change the **Pattern Size** used for new objects   * **Edit → Preferences... → Draft → Visual settings → SVG pattern default size**.



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Pattern/cs
