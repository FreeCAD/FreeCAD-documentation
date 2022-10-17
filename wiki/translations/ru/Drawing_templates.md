# Drawing templates/ru
**The [Drawing Workbench](Drawing_Workbench.md) became obsolete in v0.17. Consider using the [TechDraw Workbench](TechDraw_Workbench.md) instead.**


{{TOCright}}

## Создание SVG-шаблонов 


<div class="mw-translate-fuzzy">

Создавать шаблоны для модуля чертежей (Drawing) легко и приятно. Смотрите также [руководство по созданию шаблонов чертежей](Drawing_Template_HowTo/ru.md). Шаблон --- это файл в формате SVG, который можно создать в любой программе способной экспортировать SVG, например [Inkscape](http   *//www.inkscape.org). Необходимо соблюдать только два правила   *


</div>

### Base rules 


<div class="mw-translate-fuzzy">

### Базовые правила 

-   1 пиксель = 1 миллиметру. Размер страницы может быть указан внутри открывающего тега<svg>либо без единиц измерения, либо с \"мм\". Например, эти две формы действительны   *


</div>

 html
width="1067mm"
height="762mm"


или

 html
width="1067"
height = "762"


Хотя svg поддерживает дюймы (\"42 in\"), в настоящее время они не поддерживаются FreeCAD, поэтому всегда лучше указывать размер страницы svg в миллиметрах. Атрибут \"viewBox\" (видимая область) должен иметь то же значение, например   *

 html
viewBox="0 0 1067 762"


-   Вы должны вставить где-нибудь внутри вашего svg-кода, где вы хотите, чтобы отображалось содержимое чертежа (например, в конце файла, непосредственно перед последним тегом</svg>), следующую строку   *

 html



This text above (which is actually an XML comment) must be on a separate line, and not embedded in the middle of other pieces of text. Beware that if you reopen and resave your template in inkscape, after adding the above line, inkscape will keep the line, but will add other xml elements on the same line, causing the template to not work anymore. You will need to edit it with a text editor and isolate the comment above on its own line again.

### Namespace

-   Several objects (specifically those created with the [Draft Drawing](Draft_Drawing.md) command and if your template has editable texts) use a special [Svg Namespace](Svg_Namespace.md) specific to FreeCAD. This makes FreeCAD able to detect specific items inside svg files, that other applications will just ignore. If you plan to use any of these, you must add this line inside the opening<svg>tag, for example together with the other xmlns lines added by inkscape   *

xmlns   *freecad=\"<http   *//www.freecadweb.org/wiki/index.php?title=Svg_Namespace>\"

### Title block 


<div class="mw-translate-fuzzy">

### Блок Title 

В дополнение к этим правилам, начиная с FreeCAD 0.14, информация о границах блока Title может быть добавлена в шаблон для использования инструментом орфографической проекции. Эта область определяет, где FreeCAD может и не может размещать проекции.


</div>

Чтобы задать положение рамки, необходимо вставить следующую строку перед тегом  в svg файле   *

 html



Где X1, Y1, X2, Y2 определяются как   *

-   X1 - расстояние по оси X от левого края страницы до левой границы Рамки.
-   Y1 - расстояние по оси Y от верхнего края страницы до верхней границы Рамки.
-   X2 - расстояние по оси X от левого края страницы до правой границы Рамки.
-   Y2 - расстояние по оси Y от верхнего края страницы до нижней границы Рамки.

![](images/XY_Working_v2.svg )

Для определения блока Title необходимо вставить следующую строку после тега рабочего пространства и перед тегом .

 html




<div class="mw-translate-fuzzy">

Где   *

-   X1a --- расстояние по оси X между левой границей листа и левой стороной основной надписи.
-   Y1a --- расстояние по оси Y между верхней границей листа и верхней стороной основной надписи.
-   X2a --- расстояние по оси X между левой границей листа и правой стороной основной надписи.
-   Y2a --- расстояние по оси Y между верхней границей листа и нижней стороной основной надписи.
-   X1a \<= X1 или X2a \>= X2.
-   Y1a \<= Y1 или Y2a \>= Y2.


</div>

![](images/XY_Title_v2.svg )


<div class="mw-translate-fuzzy">

Положение основной надписи нужно задавать сразу после задания положения рамки   *


</div>

 html




Чтобы включить печать в масштабе, реальный размер текста должен быть указан в атрибутах ширины и высоты SVG-тега. Размер документа в пользовательских единицах (px) должен быть указан в атрибуте viewBox.

Это должно быть отформатировано, как в примере ниже, где   *

-   xxx = ширина в пикселях,
-   yyy = высота в пикселях.

 html
width="xxxmm"
height="yyymm"
viewBox="0 0 xxx yyy"



<div class="mw-translate-fuzzy">

В шаблоны можно добавлять пользовательские атрибуты. Список атрибутов смотрите в статье [Svg Namespace](Svg_Namespace.md).


</div>

## DXF шаблоны 

Since version 0.15, FreeCAD can reliably export a [Drawing](Drawing_Workbench.md) page to the DXF format. This system also uses templates. If a dxf file with the same name is found in the same folder as the SVG template used for a page, it will be used for export. If not, a default empty template is created on the fly.

Consequently, if you create your own SVG templates, and wish to be able to export the Drawing pages that you create with it to DXF, you just need to create a corresponding DXF template, and save it with the same name in the same folder.

DXF templates can be created with any application that produces DXF files, such as LibreCAD. You then need to edit them with a text editor, and add two additional lines, one at the beginning or end of the BLOCKS section, and another at the beginning or end of the ENTITIES section, which are where FreeCAD will add its own blocks and entities.

Самый простой шаблон выглядит так   *

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

## A3 templates 

### A3 Classic   * 

<img alt="" src=images/A3_Classic.svg  style="width   *800px;">

### A3 Clean   * 

<img alt="" src=images/A3_Clean.svg  style="width   *800px;">

### A3 Modern   * 

<img alt="" src=images/A3_Modern.svg  style="width   *800px;">

### A3 Showcase   * 

<img alt="" src=images/A3_Showcase.svg  style="width   *800px;">

### A3 Landscape english   * 

<img alt="" src=images/A3_Landscape_english.svg  style="width   *800px;">

## A4 Templates 

### A4 Landscape english   * 

<img alt="" src=images/A4_Landscape_english.svg  style="width   *800px;">

### A4 Portrait 1 english   * 

<img alt="" src=images/A4_Portrait_1_english.svg  style="width   *400px;">

## US Letter Templates 

### US Letter landscape   * 

<img alt="" src=images/US_Letter_landscape.svg  style="width   *800px;">

### US Letter portrait   * 

<img alt="" src=images/US_Letter_portrait.svg  style="width   *400px;">

### US Letter ds Landscape   * 

<img alt="" src=images/US_Letter_ds_Landscape.svg  style="width   *800px;">

### US Legal ds Landscape   * 

<img alt="" src=images/US_Legal_ds_Landscape.svg  style="width   *800px;">

### US Ledger ds Landscape   * 

<img alt="" src=images/US_Ledger_ds_Landscape.svg  style="width   *800px;">

## Other standards available 

-   [ANSI templates](ANSI_templates.md)   * according to American National Standards Institute [ANSI](http   *//en.wikipedia.org/wiki/American_National_Standards_Institute) standard
-   [Arch templates](Arch_templates.md)   * according to American National Standards Institute [Arch](http   *//en.wikipedia.org/wiki/American_National_Standards_Institute) standard
-   [Misc templates](Misc_templates.md)   * mixed templates


{{Drawing Tools navi

}} 

[Category   *Developer Documentation](Category_Developer_Documentation.md) [Category   *Documentation](Category_Documentation.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Documentation](Category_Documentation.md) > [Drawing](Category_Drawing.md) > Drawing templates/ru
