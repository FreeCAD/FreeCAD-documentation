# Drawing templates/es



**The [Drawing Workbench](Drawing_Workbench.md) became obsolete in v0.17. Consider using the [TechDraw Workbench](TechDraw_Workbench.md) instead.**


{{TOCright}}

## SVG templates creation 

Creating templates for the Drawing module is very easy. See also the tutorial [Drawing Template HowTo](Drawing_Template_HowTo.md). Templates are svg files, created with any application capable of exporting svg files, such as [Inkscape](http://www.inkscape.org). However, you will often need to open the svg file in a text editor afterwards, to comply with the following rules. Only two rules must be followed:

### Base rules 


<div class="mw-translate-fuzzy">

La creación de plantillas para el módulo de dibujo es muy sencilla. Son archivos SVG, creados con cualquier aplicación capaz de exportar archivos SVG, como [inkscape](http://www.inkscape.org). Sólo se deben seguir dos reglas:

-   Un pixel = Un milímetro
-   Tienes que insertar, en alguna parte dentro del código SVG, donde quieras que aparezca el contenido del dibujo (por ejemplo al final del archivo, simplemente antes del tag</svg>), la siguiente línea:


</div>

 {.html}
width="1067mm"
height="762mm"


or

 {.html}
width="1067"
height = "762"


Although svg supports inches (\"42 in\"), these are currently not supported by FreeCAD, so it\'s always better to have your svg page size specified in millimeters. The \"viewBox\" attribute must have the same value, for example:

 {.html}
viewBox="0 0 1067 762"


-   You must insert, somewhere inside your svg code, where you want the contents of the drawing to appear (for example at the end of the file, just before the last</svg>tag), the following line:

 {.html}



This text above (which is actually an XML comment) must be on a separate line, and not embedded in the middle of other pieces of text. Beware that if you reopen and resave your template in inkscape, after adding the above line, inkscape will keep the line, but will add other xml elements on the same line, causing the template to not work anymore. You will need to edit it with a text editor and isolate the comment above on its own line again.

### Namespace

-   Several objects (specifically those created with the [Draft Drawing](Draft_Drawing.md) command and if your template has editable texts) use a special [Svg Namespace](Svg_Namespace.md) specific to FreeCAD. This makes FreeCAD able to detect specific items inside svg files, that other applications will just ignore. If you plan to use any of these, you must add this line inside the opening<svg>tag, for example together with the other xmlns lines added by inkscape:

xmlns:freecad=\"<http://www.freecadweb.org/wiki/index.php?title=Svg_Namespace>\"

### Title block 

In addition to these rules, since FreeCAD 0.14, information about the Border and Title block can be added to the template for use by the orthographic projection tool. This information defines where FreeCAD can, and can not place the projections.

To define the Border, the following line must appear before the  tag in the svg file.

 {.html}



Where X1, Y1, X2, Y2 are defined as:

-   X1 is the X axis distance from the left edge of the page to the left side of the Border.
-   Y1 is the Y axis distance from the top edge of the page to the top of the Border.
-   X2 is the X axis distance from the left edge of the page to the right side of the Border.
-   Y2 is the Y axis distance from the top edge of the page to the bottom of the Border.

![](images/XY_Working_v2.svg )

To define the Title block the following line must be inserted before the  tag and after the Working space tag.

 {.html}



Where X1a, Y1a, X2a, Y2a are defined as:

-   X1a is the X axis distance from the left edge of the page to the left side of the Title block
-   Y1a is the Y axis distance from the top edge of the page to the top of the Title block
-   X2a is the X Axis distance from the left edge of the page to the right side of the Title block
-   Y2a is the Y axis distance from the top edge of the page to the bottom of the Title block
-   X1a \<= X1 or X2a \>= X2
-   Y1a \<= Y1 or Y2a \>= Y2

![](images/XY_Title_v2.svg )

The following is an example of the code that defines the Working space and Title block areas that are to be inserted before the  tag. You needn\'t specify a title block, but if you do it must be defined on the next line immediately following the Working space:

 {.html}




In order to enable up to scale printing, the real word size has to be given in the width and height attributes of the SVG-Tag. The size of the document in user units, (px), has to be given in the viewBox attribute.

The following is to be formatted like the example below where:

-   xxx = pixel width
-   yyy = pixel height

 {.html}
width="xxxmm"
height="yyymm"
viewBox="0 0 xxx yyy"



<div class="mw-translate-fuzzy">

-   Diversos atributos personalizables se pueden incluir en las plantillas. La lista de atributos soportados actualmente está disponible en la página [Svg Namespace](Svg_Namespace/es.md).


</div>

## DXF templates 

Since version 0.15, FreeCAD can reliably export a [Drawing](Drawing_Workbench.md) page to the DXF format. This system also uses templates. If a dxf file with the same name is found in the same folder as the SVG template used for a page, it will be used for export. If not, a default empty template is created on the fly.

Consequently, if you create your own SVG templates, and wish to be able to export the Drawing pages that you create with it to DXF, you just need to create a corresponding DXF template, and save it with the same name in the same folder.

DXF templates can be created with any application that produces DXF files, such as LibreCAD. You then need to edit them with a text editor, and add two additional lines, one at the beginning or end of the BLOCKS section, and another at the beginning or end of the ENTITIES section, which are where FreeCAD will add its own blocks and entities.

A very simple template looks like this:

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


<div class="mw-translate-fuzzy">

## A3 templates 


</div>


<div class="mw-translate-fuzzy">

<img alt="" src=images/A3_Classic.svg  style="width:800px;">


</div>

<img alt="" src=images/A3_Classic.svg  style="width:800px;">


<div class="mw-translate-fuzzy">

<img alt="" src=images/A3_Clean.svg  style="width:800px;">


</div>

<img alt="" src=images/A3_Clean.svg  style="width:800px;">


<div class="mw-translate-fuzzy">

<img alt="" src=images/A3_Modern.svg  style="width:800px;">


</div>

<img alt="" src=images/A3_Modern.svg  style="width:800px;">


<div class="mw-translate-fuzzy">

<img alt="" src=images/A3_Showcase.svg  style="width:800px;">


</div>

<img alt="" src=images/A3_Showcase.svg  style="width:800px;">


<div class="mw-translate-fuzzy">

<img alt="" src=images/A3_Landscape_english.svg  style="width:800px;">


</div>

<img alt="" src=images/A3_Landscape_english.svg  style="width:800px;">


<div class="mw-translate-fuzzy">

## Plantillas A4 


</div>


<div class="mw-translate-fuzzy">

### Apaisadas:


</div>

<img alt="" src=images/A4_Landscape_english.svg  style="width:800px;">


<div class="mw-translate-fuzzy">

### Vertical:


</div>

<img alt="" src=images/A4_Portrait_1_english.svg  style="width:400px;">


<div class="mw-translate-fuzzy">

## Plantillas US Letter 


</div>


<div class="mw-translate-fuzzy">

### Apaisadas: 


</div>

<img alt="" src=images/US_Letter_landscape.svg  style="width:800px;">


<div class="mw-translate-fuzzy">

### Vertical: 


</div>

<img alt="" src=images/US_Letter_portrait.svg  style="width:400px;">

### US Letter ds Landscape: 

<img alt="" src=images/US_Letter_ds_Landscape.svg  style="width:800px;">

### US Legal ds Landscape: 

<img alt="" src=images/US_Legal_ds_Landscape.svg  style="width:800px;">

### US Ledger ds Landscape: 

<img alt="" src=images/US_Ledger_ds_Landscape.svg  style="width:800px;">

## Other standards available 

-   [ANSI templates](ANSI_templates.md): according to American National Standards Institute [ANSI](http://en.wikipedia.org/wiki/American_National_Standards_Institute) standard
-   [Arch templates](Arch_templates.md): according to American National Standards Institute [Arch](http://en.wikipedia.org/wiki/American_National_Standards_Institute) standard
-   [Misc templates](Misc_templates.md): mixed templates


{{Drawing Tools navi

}} 

[Category:Developer Documentation](Category:Developer_Documentation.md) [Category:Documentation](Category:Documentation.md)
