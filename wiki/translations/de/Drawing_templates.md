# Drawing templates/de



**The [Drawing Workbench](Drawing_Workbench.md) became obsolete in v0.17. Consider using the [TechDraw Workbench](TechDraw_Workbench.md) instead.**


{{TOCright}}


**Die Entwicklung des Drawing-Moduls wurde gestoppt und ein neuer in v0.17 eingeführter TechDraw-Arbeitsbereich zielt darauf, es zu setzen. Beide Module stehen in v0.17 zur Verfügung, aber das Drawing-Modul könnte in zukünftigen Ausgaben entfernt werden.**

## SVG-Vorlagenerstellung 


<div class="mw-translate-fuzzy">

Das Anlegen von Vorlagen für den Zeichnungs-Arbeitsbereich ist sehr einfach (siehe auch das Tutorial [Drawing\_Template\_HowTo/de](Drawing_Template_HowTo/de.md)). Vorlagen sind svg-Dateien, die mit jeder Anwendung erstellt werden können, die svg-Dateien exportieren kann, wie z.B. [Inkscape](http://www.inkscape.org). Trotzdem musst Du oftmals später die Datei mit einem Texteditor öffnen, um die folgenden Regeln zu erfüllen. Es geht nur um zwei Regeln:


</div>

### Base rules 


<div class="mw-translate-fuzzy">

### Basisregeln

-   Ein Pixel = ein Millimeter. Die Seitengröße kann innerhalb des öffnenden<svg>-Tags angegeben werden, entweder ohne Einheit oder mit \"mm\". Beispielsweise sind diese beiden Formen gültig:


</div>

 {.html}
width="1067mm"
height="762mm"


oder

 {.html}
width="1067"
height = "762"


Obwohl svg Inches (\"42 in\") unterstützt, ist das bei FreeCAD bisher nicht der Fall, so dass es immer besser ist, die svg-Seitengröße in Millimeter anzugeben. Das \"viewBox\"-Attribut muss den gleichen Wert haben, z.B.:

 {.html}
viewBox="0 0 1067 762"


-   Du musst irgendwo innerhalb Deines svg-Codes angeben, wo der Inhalt der Zeichnung auftauchen soll (z.B. am Ende der Datei, direkt vor dem letzten</svg>-Tag). Dazu dient die folgende Zeile:

 {.html}



Der Text oben (bei dem es sich eigentlich um einen XML-Kommentar handelt) muss auf einer eigenen Zeile stehen und darf nicht Teil eines anderen Textes sein. Achte darauf, dass Inkscape bei erneutem öffnen und speichern die Zeile zwar beibehält, aber andere XML-Elemente in der gleichen Zeile hinzufügt, so dass diese Vorlagen nicht mehr funktioniert. Du musst die Datei daher mit einem Texteditor öffnen und dafür sorgen, dass diese Zeile einzeln steht.

### Namespace


<div class="mw-translate-fuzzy">

### Namensraum

-   Verschiedene Objekte (besonders die mit dem [Draft\_Drawing](Draft_Drawing/de.md)-Befehl erstellten und wenn Deine Vorlage editierbaren Text enthält) benutzen einen speziellen [Namensraum](Svg_Namespace/de.md), der spezifisch für FreeCAD ist. Dies erlaubt FreeCAD, diese Elemente in svg-Dateien zu erkennen, die andere Anwendungen einfach ignorieren. Wenn Du beabsichtigst, diese Elemente zu nutzen, musst Du diese Zeile nach dem öffnenden<svg>-Tag einfügen, z.B. zusammen mit den anderen xmlns-Zeilen, die durch Inkscape hinzugefügt werden.


</div>

xmlns:freecad=\"<http://www.freecadweb.org/wiki/index.php?title=Svg_Namespace>\"

### Title block 


<div class="mw-translate-fuzzy">

### Titelblock

Zusätzlich zu diesen Regeln können der Vorlage (seit FreeCAD v0.14) Informationen zu der Umrandung (border) und dem Titelblock hinzugefügt werden, die vom orthographischen Projektionswerkzeug benutzt werden. Diese Information definiert, wo FreeCAD diese Projektionen platzieren kann (und wo nicht).


</div>

Um die Umrandung zu definieren, muss die folgende Zeile vor dem -Tag der svg-Datei stehen.

 {.html}



wo X1, Y1, X2, Y2 definiert sind als:

-   X1 ist der horizontale Abstand von der linken Kante der Seite zur linken Seite der Umrandung.
-   Y1 ist der vertikale Abstand von der oberen Kante der Seite zur oberen Umrandung.
-   X2 ist der horizontale Abstand von der linken Kante der Seite zur rechten Seite der Umrandung.
-   Y2 ist der vertikale Abstand von der oberen Kante der Seite zur unteren Umrandung.

![](images/XY_Working_v2.svg )

Um den Titelblock zu definieren, muss die folgende Zeile vor dem -Tag und nach dem \"Working space\"-Tag der svg-Datei stehen.

 {.html}



wo X1a, Y1a, X2a, Y2a definiert sind als:

-   X1a ist der horizontale Abstand von der linken Kante der Seite zur linken Seite des Titelblocks.
-   Y1a ist der vertikale Abstand von der oberen Kante der Seite zur oberen Kante des Titelblocks.
-   X2a ist der horizontale Abstand von der linken Kante der Seite zur rechten Seite des Titelblocks.
-   Y2a ist der vertikale Abstand von der oberen Kante der Seite zur unteren Kante des Titelblocks.
-   X1a \<= X1 or X2a \>= X2
-   Y1a \<= Y1 or Y2a \>= Y2

![](images/XY_Title_v2.svg )

Das Folgende ist ein Beispiel für den Code, der die \"Working space\"- und \"Title block\"-Bereiche definiert, die vor dem -Tag einzufügen ist. Du musst keinen Titelblock definieren, aber wenn Du es tust, muss es in der Zeile direkt nach \"Working space\" sein.

 {.html}




In order to enable up to scale printing, the real word size has to be given in the width and height attributes of the SVG-Tag. The size of the document in user units, (px), has to be given in the viewBox attribute.

Das Folgende muss wie im nachfolgenden Beispiel formattiert werden:

-   xxx = Pixel-Breite
-   yyy = Pixel-Höhe

 {.html}
width="xxxmm"
height="yyymm"
viewBox="0 0 xxx yyy"


-   Several custom attributes can be placed in templates. The list of currently supported attributes is available on the [Svg Namespace](Svg_Namespace.md) page.

## DXF-Vorlagen 


<div class="mw-translate-fuzzy">

Seit v0.15 kann FreeCAD zuverlässig eine [Zeichnungsseite](Drawing_Workbench/de.md) ins DXF-Format exportieren. Dieses System benutzt ebenfalls Vorlagen. Wenn eine dxf-Datei mit dem gleichen Namen im gleichen Verzeichnis wie die für eine Seite genutzte svg-Vorlage gefunden wird, wird sie für den Export verwendet. Falls nicht, wird eine leere Vorlage erstellt.


</div>

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

## A3 Vorlagen 


<div class="mw-translate-fuzzy">

### A3 Klassisch: 

<img alt="" src=images/A3_Classic.svg  style="width:800px;">


</div>

<img alt="" src=images/A3_Classic.svg  style="width:800px;">

### A3 Clean: 

<img alt="" src=images/A3_Clean.svg  style="width:800px;">

### A3 Modern: 

<img alt="" src=images/A3_Modern.svg  style="width:800px;">

### A3 Showcase: 

<img alt="" src=images/A3_Showcase.svg  style="width:800px;">


<div class="mw-translate-fuzzy">

### A3 Querformat englisch: 

<img alt="" src=images/A3_Landscape_english.svg  style="width:800px;">


</div>

<img alt="" src=images/A3_Landscape_english.svg  style="width:800px;">

## A4 Vorlagen 

### A4 Querformat englisch: 

<img alt="" src=images/A4_Landscape_english.svg  style="width:800px;">

### A4 Hochformat 1 englisch: 

<img alt="" src=images/A4_Portrait_1_english.svg  style="width:400px;">

## US Letter Vorlagen 

### US Letter Querformat: 

<img alt="" src=images/US_Letter_landscape.svg  style="width:800px;">

### US Letter Hochformat: 

<img alt="" src=images/US_Letter_portrait.svg  style="width:400px;">

### US Letter ds Querformat: 

<img alt="" src=images/US_Letter_ds_Landscape.svg  style="width:800px;">

### US Legal ds Querformat: 

<img alt="" src=images/US_Legal_ds_Landscape.svg  style="width:800px;">

### US Ledger ds Querformat: 

<img alt="" src=images/US_Ledger_ds_Landscape.svg  style="width:800px;">

## Andere verfügbare Standards 

-   [ANSI-Vorlagen](ANSI_templates/de.md): entsprechend dem American National Standards Institute [ANSI](https://de.wikipedia.org/wiki/American_National_Standards_Institute)-Standard\* [Architektur-Vorlagen](Arch_templates/de.md): entsprechend dem American National Standards Institute [Architektur](https://de.wikipedia.org/wiki/American_National_Standards_Institute)-Standard
-   [Verschiedene Vorlagen](Misc_templates/de.md): Verschiedene Vorlagen


{{Drawing Tools navi

}} 

[Category:Developer Documentation](Category:Developer_Documentation.md) [Category:Documentation](Category:Documentation.md)
