# Drawing templates/cs
**The [Drawing Workbench](Drawing_Workbench.md) became obsolete in v0.17. Consider using the [TechDraw Workbench](TechDraw_Workbench.md) instead.**


{{TOCright}}

## SVG templates creation 

Creating templates for the Drawing module is very easy. See also the tutorial [Drawing Template HowTo](Drawing_Template_HowTo.md). Templates are svg files, created with any application capable of exporting svg files, such as [Inkscape](http   *//www.inkscape.org). However, you will often need to open the svg file in a text editor afterwards, to comply with the following rules. Only two rules must be followed   *

### Base rules 


<div class="mw-translate-fuzzy">

Vytváření šablon pro modul Výkresy je velmi snadné. Koukněte na výukový program [Výkres Šablona Jak](Drawing_Template_HowTo/cs.md). Šablony jsou SVG soubory, které jsou vytvořené nějakou aplikací schopnou vyexportovat SVG soubory, jako je třeba [Inkscape](http   *//www.inkscape.org). Musí být dodrženy pouze násleující 2 pravidla   *

-   Jeden pixel = jeden millimeter
-   Ve vytvořeném SVG kódu musíte do místa kde chcete aby se zobrazoval Váš výkres (například na konec souboru před značku</svg>) vložit následující řádek   *


</div>

 html
width="1067mm"
height="762mm"


or

 html
width="1067"
height = "762"


Although svg supports inches (\"42 in\"), these are currently not supported by FreeCAD, so it\'s always better to have your svg page size specified in millimeters. The \"viewBox\" attribute must have the same value, for example   *

 html
viewBox="0 0 1067 762"


-   You must insert, somewhere inside your svg code, where you want the contents of the drawing to appear (for example at the end of the file, just before the last</svg>tag), the following line   *

 html



This text above (which is actually an XML comment) must be on a separate line, and not embedded in the middle of other pieces of text. Beware that if you reopen and resave your template in inkscape, after adding the above line, inkscape will keep the line, but will add other xml elements on the same line, causing the template to not work anymore. You will need to edit it with a text editor and isolate the comment above on its own line again.

### Namespace

-   Several objects (specifically those created with the [Draft Drawing](Draft_Drawing.md) command and if your template has editable texts) use a special [Svg Namespace](Svg_Namespace.md) specific to FreeCAD. This makes FreeCAD able to detect specific items inside svg files, that other applications will just ignore. If you plan to use any of these, you must add this line inside the opening<svg>tag, for example together with the other xmlns lines added by inkscape   *

xmlns   *freecad=\"<http   *//www.freecadweb.org/wiki/index.php?title=Svg_Namespace>\"

### Title block 


<div class="mw-translate-fuzzy">

Navíc k těmto dvěma pravidlům mohou být pro verze FreeCADu 0.14, revize 2995 do šablony přidány ještě informace o Pracovním prostoru a Popisovém poli pro nástroj ortografického zobrazení. tyto informace definují kam může a nemůže FreeCAD umístit zobrazení.


</div>


<div class="mw-translate-fuzzy">

Pro definování rámečku výkresu se musí před značku \<metadata v souboru SVG objevit následující řádek.


</div>

 html




<div class="mw-translate-fuzzy">

Kde X1, Y1, X2, Y2 jsou definovány jako   *

-   X1 je vzdálenost od levého okraje stránky k levé straně rámečku v ose X.
-   Y1 je vzdálenost od horního okraje stránky k horní straně rámečku v ose Y.
-   X2 je vzdálenost od levého okraje stránky k pravé straně rámečku v ose X.
-   Y2 je vzdálenost od horního okraje stránky ke spodní straně rámečku v ose Y.


</div>

![](images/XY_Working_v2.svg )


<div class="mw-translate-fuzzy">

Pro definování Popisového pole musí být před značku \<metadata, ale za značku Working space (Pracovná prostor), přidán i následující řádek.


</div>

 html




<div class="mw-translate-fuzzy">

Kde X1a, Y1a, X2a, Y2a jsou definovány jako   *

-   X1a je vzdálenost od levého okraje stránky k levé straně popisového pole v ose X.
-   Y1a je vzdálenost od horního okraje stránky k horní straně popisového pole v ose Y.
-   X2a je vzdálenost od levého okraje stránky k pravé straně popisového pole v ose X.
-   Y2a je vzdálenost od horního okraje stránky ke spodní straně popisového pole v ose Y.


</div>

![](images/XY_Title_v2.svg )


<div class="mw-translate-fuzzy">

Následuje příklad kódu, který definuje Pracovní prostor (Working space) a Popisové pole (Title block) a který musí být vložen před značku \<metadata. Popisové pole není nutné specifikovat, ale když to uděláte, musí být ihned za definicí Pracovního prostoru (Working space)   *


</div>

 html




In order to enable up to scale printing, the real word size has to be given in the width and height attributes of the SVG-Tag. The size of the document in user units, (px), has to be given in the viewBox attribute.

The following is to be formatted like the example below where   *

-   xxx = pixel width
-   yyy = pixel height

 html
width="xxxmm"
height="yyymm"
viewBox="0 0 xxx yyy"



<div class="mw-translate-fuzzy">

-   V šabloně může být umístěno několik uživatelských atributů. Seznam aktuálně dostupných atributů je na stránce [Svg Namespace](Svg_Namespace.md).


</div>

## DXF templates 

Since version 0.15, FreeCAD can reliably export a [Drawing](Drawing_Workbench.md) page to the DXF format. This system also uses templates. If a dxf file with the same name is found in the same folder as the SVG template used for a page, it will be used for export. If not, a default empty template is created on the fly.

Consequently, if you create your own SVG templates, and wish to be able to export the Drawing pages that you create with it to DXF, you just need to create a corresponding DXF template, and save it with the same name in the same folder.

DXF templates can be created with any application that produces DXF files, such as LibreCAD. You then need to edit them with a text editor, and add two additional lines, one at the beginning or end of the BLOCKS section, and another at the beginning or end of the ENTITIES section, which are where FreeCAD will add its own blocks and entities.

A very simple template looks like this   *

    999
    FreeCAD DXF exporter v0.15
    0
    SECTION
    2
    HEADER
    9
    $ACADVER
    1
    AC1009
    0
    ENDSEC
    0
    SECTION
    2
    BLOCKS
    $blocks
    0
    ENDSEC
    0
    SECTION
    2
    ENTITIES
    $entities
    0
    ENDSEC
    0
    EOF

The above template doesn\'t contain any entity. If you create your DXF file with a CAD application, there will likely be much more content inside the HEADER, BLOCKS and ENTITIES sections.

The two lines that FreeCAD will be looking for are \"\$blocks\" and \"\$entities\". They must exist in the template, and they must be placed on their own line. You can choose to place them right after the BLOCKS or ENTITIES line, which is easier (just use the \"search\" function of your text editor to find them), or at the end, just before the \"0 ENDSEC\" lines (beware that there is one for each SECTION, make sure to use the ones relative to BLOCKS and ENTITIES). The latter method will place the FreeCAD objects after the objects defined in the template, which might be more logical.

## Šablony A3 


<div class="mw-translate-fuzzy">

### Klasická A3   * 

<img alt="" src=images/A3_Classic.svg  style="width   *800px;">


</div>

<img alt="" src=images/A3_Classic.svg  style="width   *800px;">


<div class="mw-translate-fuzzy">

### Čistá A3   * 

<img alt="" src=images/A3_Clean.svg  style="width   *800px;">


</div>

<img alt="" src=images/A3_Clean.svg  style="width   *800px;">


<div class="mw-translate-fuzzy">

### Moderní A3   * 

<img alt="" src=images/A3_Modern.svg  style="width   *800px;">


</div>

<img alt="" src=images/A3_Modern.svg  style="width   *800px;">


<div class="mw-translate-fuzzy">

### Ukázková A3   * 

<img alt="" src=images/A3_Showcase.svg  style="width   *800px;">


</div>

<img alt="" src=images/A3_Showcase.svg  style="width   *800px;">


<div class="mw-translate-fuzzy">

### A3 na šířku anglicky   * 

<img alt="" src=images/A3_Landscape_english.svg  style="width   *800px;">


</div>

<img alt="" src=images/A3_Landscape_english.svg  style="width   *800px;">

## Šablona A4 

### A4 na šířku anglicky   * 

<img alt="" src=images/A4_Landscape_english.svg  style="width   *800px;">

### A4 na výšku 1 anglicky   * 

<img alt="" src=images/A4_Portrait_1_english.svg  style="width   *400px;">

## Šablona US Letter 

### US Letter na šířku   * 

<img alt="" src=images/US_Letter_landscape.svg  style="width   *800px;">

### US Letter na výšku   * 

<img alt="" src=images/US_Letter_portrait.svg  style="width   *400px;">

### US Letter ds na šířku   * 

<img alt="" src=images/US_Letter_ds_Landscape.svg  style="width   *800px;">

### US Legal ds na šířku   * 

<img alt="" src=images/US_Legal_ds_Landscape.svg  style="width   *800px;">

### US Ledger ds na šířku   * 

<img alt="" src=images/US_Ledger_ds_Landscape.svg  style="width   *800px;">

## Další dostupné standardy 

-   [ANSI šablony](ANSI_templates/cs.md)   * podle standardů American National Standards Institute [ANSI](http   *//en.wikipedia.org/wiki/American_National_Standards_Institute)
-   [Architektonické šablony](Arch_templates/cs.md)   * podle standardů American National Standards Institute [Arch](http   *//en.wikipedia.org/wiki/American_National_Standards_Institute)
-   [Ostatní šablony](Misc_templates/cs.md)   * další šablony


{{Drawing Tools navi

}} 

[Category   *Developer Documentation](Category_Developer_Documentation.md) [Category   *Documentation](Category_Documentation.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Documentation](Category_Documentation.md) > [Drawing](Category_Drawing.md) > Drawing templates/cs
