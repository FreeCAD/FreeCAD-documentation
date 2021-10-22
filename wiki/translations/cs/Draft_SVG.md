# Draft SVG/cs
{{TOCright}}

## Description

Draft SVG is a software module used by the <img alt="" src=images/Std_Open.svg  style="width:24px;"> _ and <img alt="" src=images/Std_Export.svg  style="width:24px;"> [Std Export](Std_Export.md) commands to handle the [SVG](SVG.md) file format.

![](images/Screenshot_inkscape.jpg ) 
*Inkscape drawing exported to SVG, which is subsequently opened in FreeCAD*


<div class="mw-translate-fuzzy">

### Otevření

Tato funkce importuje SVG soubory jako zpracovatelné 2D objekty, jako protějšek zabudovaného kreslicího modulu, který importuje SVG soubory jako výkresy. V současnosti jsou importovány následující SVG objekty:

-   objekty PATH
-   objekty PŘÍMKA
-   objekty OBDÉLNÍK
-   objekty KRUŽNICE
-   objekty ELIPSA
-   objekty MNOHOÚHELNÍK
-   objekty LOMENÁ ČÁRA


</div>

The following SVG objects can be imported:

-   PATH objects
-   LINE objects
-   RECT objects
-   CIRCLE objects
-   ELLIPSE objects
-   POLYGON objects
-   POLYLINE objects

### Limitations

FreeCAD will not import path objects that have only one point ([forum discussion](https://forum.freecadweb.org/viewtopic.php?f=3&t=43856)).


<div class="mw-translate-fuzzy">

### Export

V SVG souboru mohou být exportovány následující objekty:

-   Přímky a dráty (lomené čáry)
-   Oblouky a kružnice
-   Plochy
-   Texty
-   Kóty


</div>

The following FreeCAD objects can be exported:

-   Lines and wires (polylines)
-   Arcs and circles
-   Faces
-   Texts
-   Dimensions


<div class="mw-translate-fuzzy">

Mějte na mysli, že SVG je 2D formát, takže všechny Z informace budou ignorovány (všechny objekty budou ploché).


</div>

SVG is a 2D format, so all Z information will be disregarded (all objects will be flattened).


<div class="mw-translate-fuzzy">

### Práce s jednotkami 

Při exportu se jedna User Unit (px) rovná jednomu milimetru.


</div>

When exporting, a User Unit (px) equals one millimeter.


<div class="mw-translate-fuzzy">

Při importu jsou respektovány atributy šířky, výšky a viewBoxu. Všechny prvky jsou převedeny na jejich rozměry v milimetrech, což je interní jednotka FreeCADu. Pokud SVG neobsahuje informace o fyzickém rozměru, předpokládá se rozlišení 90 DPI. Doporučuje se vyhýbat se použití absolutních jednotek v atributech uvnitř SVG . Relativní jednotky jako jsou em,ex a % nejsou aktuálně ve FreeCADu podporovány.


</div>


<div class="mw-translate-fuzzy">

SVG editor Inkscapu aktuálně pracuje s dokumenty s rozlišením 90 DPI. Nezáleží na tom jaké jsou v Inkscapu vybrány jednotky. Je třeba počítat s tím, že všechny výstupy jsou konvertovány do rozlišení 90 DPI a zaokrouhleny na 6 desetinných míst. Protože FreeCAD (a SVG standard) nedůvěřuje přesnosti zaokrouhlování v Inkscpau, nebudou tyto hodnoty zaoukrouhlovány na vstupu. Přebytečné informace v milimetrech zbudou. Jestliže potřebujete aby SVG import nebyl zaokrouhlován, pracujte v Inkscapu s User Units(px). Přepočet může být dodatečně proveden po importu do FreeCADu nebo změnou atributů šířky, výšky a viewBoxu.


</div>


<div class="mw-translate-fuzzy">

### Předvolby

V záložce [Kreslení Předvolby](Draft_Preferences/cs.md) (menu Úpravy -\> Předvolby -\> Kreslení) mohou být specifikovány následující parametry:

-   Import/Export -\> Styl Importu: Dává na výběr způsob jakým budou objekty z SVG souboru kresleny ve FreeCADu. Vyběr je mezi:
    -   Žádný: to je nejrychlejší způsob, nedělají se žádné konverze, všechny objekty jsou černé s defaultní (FreeCAD) tloušťkou čáry 2px
    -   Použít defaultní barvu a tloušťku čáry: Všechny importované objekty přebírají aktuálně nastavenou barvy a tloušťku čáry z příkazového pruhu kreslení
    -   Originální barvu a tloušťku čáry: Objekty si podrží barvu a tloušťku čáry (pokud je specifikovaná) takovou jakou mají v SVG souboru
-   Import/Export -\> Styl Exportu:
    -   Překlad: Všechny elementy jsou přeloženy tak, že mají kladné souřadnice. To by mělo pomoci při zobrazování a tisku. Výstupní souřadnicový systém NENÍ konzistentní mezi individuálně exportovanými prvky.
    -   Neupravený: Pozice všech prvků jsou zachovány. Je to zamýšleno pro použití v CAM, např. v PyCAM. Vrstvy nebo řezy, které jsou exportované samostatně budou spolu lícovat.
-   Základní nastavení -\> Interní úroveň přesnosti:
    -   Tato hodnota je využita pro kontrolu, zda segment Bezierovy křivky musí mít vazbu na přímou čáru. If you import detailed paths, like rendered text, you may want to increase this setting up to 6. Pracujete-li s Inscapem, uvažujte prosím o zvýšení přesnosti v SVG souboru. (Inkscape Menu -\> File -\> Inkscape Preferences -\> SVG Output -\> Numeric Precision)


</div>

See [Import Export Preferences](Import_Export_Preferences.md).

## Scripting

See also: _.

To export objects to SVG use the `export` method of the importSVG module.


```python
importSVG.export(exportList, filename)
```

-   For the Windows OS: use a {{FileName|/}} (forward slash) as the path separator in {{Incode|filename}}.

Example:


```python
import FreeCAD as App
import Draft
import importSVG

doc = App.newDocument()

polygon1 = Draft.make_polygon(3, radius=500)
polygon2 = Draft.make_polygon(5, radius=1500)

doc.recompute()

objects = [polygon1, polygon2]
importSVG.export(objects, "/home/user/Pictures/myfile.svg")
```


<div class="mw-translate-fuzzy">


</div>


 

_ _

---
[documentation index](../README.md) > [File Formats](Category_File Formats.md) > [Draft](Draft_Workbench.md) > Draft SVG/cs
