# Svg Namespace/it
**Lo sviluppo del modulo Drawing è stato interrotto in FreeCAD 0.16 con il proposito di sostituirlo con il nuovo modulo [TechDraw](TechDraw_Workbench/it.md) che sarà introdotto nella versione 0.17. Nella versione 0.17 sono forniti entrambi i moduli, ma il modulo Drawing potrebbe essere rimosso nelle versioni future.**


{{TOCright}}

Nei documenti [SVG](http://it.wikipedia.org/wiki/Scalable_Vector_Graphics) esportati dal [Modulo Disegno](Drawing_Workbench/it.md) di FreeCAD e utilizzati come [modelli di pagina](Drawing_templates/it.md) (squadrature), si possono utilizzare diversi [attributi](http://www.w3schools.com/xml/xml_attributes.asp) personalizzati, originariamente per uso interno di FreeCAD, ma che, in futuro, potrebbero essere utilizzati anche da altre applicazioni oltre a FreeCAD . Tutti questi attributi utilizzano il prefisso **freecad:** per il [namespace](http://www.w3schools.com/xml/xml_namespaces.asp). L\'URL del namespace definito in tali documenti SVG fa riferimento a questa pagina.

## Utilizzo

Un pixel = un millimetro

È necessario inserire, da qualche parte dentro il codice svg, dove si desidera che appaia il contenuto del disegno (per esempio alla fine del file, appena prima dell\'ultimo tag \'\'\'


</svg>

\'\'\'), la riga seguente :

 xml



 xml
<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<svg
    xmlns:freecad="http://www.freecadweb.org/wiki/index.php?title=Svg_Namespace"


Per scalare la stampa, la dimensione effettiva deve essere data negli attributi width e height del tag SVG. Le dimensioni del documento, nelle unità utilizzate (px), deve essere fornita nell\'attributo Viewbox.

In questo caso deve essere formattato come nell\'esempio sottostante dove:

-   xxx = pixel width (larghezza)
-   yyy = pixel height (altezza)

 xml
width="xxxmm"
height="yyymm"
viewBox="0 0 xxx yyy"


Possono essere aggiunte informazioni supplementari per lo spazio di lavoro e il blocco del titolo e esse sono definite nella pagina [Modelli di squadrature](Drawing_templates/it.md).

## Attributi

### [freecad:EditableText](#Example_of_code_freecad_EditableText.md)

Per utilizzare uno degli attributi **freecad:** nei documenti SVG, si deve prima definire il namespace freecad come attributo del tag di apertura


<svg>

Definisce un testo in un modello che può essere modificato da FreeCAD.

Esempio:

 xml
<text freecad:EditableText="MyTitleText">
    <tspan>This is a title</tspan>
</text>


### freecad:basepoint1

Definisce il primo punto di un oggetto di [Quotatura](Draft_Dimension/it.md) (rappresentato come un gruppo in un documento SVG). Questo attributo viene utilizzato durante l\'importazione del frammento di SVG in FreeCAD, per ricreare l\'oggetto Quotatura. Il gruppo contiene i percorsi e altri elementi grafici per rappresentare correttamente l\'oggetto Quotatura in altre applicazioni SVG.

Esempio:

 xml
<g freecad:basepoint1="0.5 4.34" freecad:basepoint2="2.4 5.8" dimpoint="3.2 7.76">
    <path d="...">
</g>


### freecad:basepoint2

Definisce il secondo punto di un oggetto di [Quotatura](Draft_Dimension/it.md) (rappresentato come un gruppo in un documento SVG). Questo attributo viene utilizzato durante l\'importazione del frammento di SVG in FreeCAD, per ricreare l\'oggetto Quotatura. Il gruppo contiene i percorsi e altri elementi grafici per rappresentare correttamente l\'oggetto Quotatura in altre applicazioni SVG.

Esempio: vedere [freecad:basepoint1](#freecad_basepoint1.md)

### freecad:dimpoint

Definisce il punto di un oggetto di [Quotatura](Draft_Dimension/it.md) attraverso il quale passa la linea di quota. Questo attributo viene utilizzato durante l\'importazione del frammento di SVG in FreeCAD, per ricreare l\'oggetto Quotatura. Il gruppo contiene i percorsi e altri elementi grafici per rappresentare correttamente l\'oggetto Quotatura in altre applicazioni SVG.

Esempio: vedere [freecad:basepoint1](#freecad_basepoint1.md)

### Esempio di codice freecad:EditableText 

Questo esempio è tratto dalla tabella del modello di squadratura [A3_Landscape](Misc_templates#A3_Landscape_US_Text_Complet_With_Convention_US.md)

#### 1 : Title without textedit 

<img alt="" src=images/Svg_Namespace_01.png  style="width:300px;">

 xml
  <g
     id="g3587">
    <text
       sodipodi:linespacing="119.00001%"
       id="text3482"
       y="229.10912"
       x="220.8476"
       style="font-size:1.97555566px;font-style:normal;font-weight:normal;line-height:119.00000572%;letter-spacing:0.01975556px;word-spacing:0.00846667px;writing-mode:lr-tb;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans;-inkscape-font-specification:Sans"
       xml:space="preserve"><tspan
         y="229.10912"
         x="220.8476"
         id="tspan3484"
         sodipodi:role="line">AUTHOR NAME :</tspan></text>


#### 2 : Title with textedit 

<img alt="" src=images/Svg_Namespace_02.png  style="width:300px;">

 xml
  <g
     style="fill:none;stroke:#000000;stroke-width:0.13;stroke-linecap:butt;stroke-linejoin:miter"
     id="g578-7"
     transform="translate(0,4)">
    <text
       xml:space="preserve"
       style="font-size:4px;font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;line-height:125%;letter-spacing:0px;word-spacing:0px;fill:#000000;fill-opacity:1;stroke:none;font-family:sans;-inkscape-font-specification:sans"
       x="220.9935"
       y="228.95425"
       id="text3331"
       sodipodi:linespacing="125%"
       freecad:editable="AuthorName"><tspan
         sodipodi:role="line"
         id="tspan3333"
         x="220.9935"
         y="228.95425">AUTHOR NAME</tspan></text>
    <text
    ...
    ...
    ...
    ... </text>
  
  </g>


#### Spiegazioni

 xml
  <g


Inizio del riquadro

 xml
     style="fill:none;stroke:#000000;stroke-width:0.13;stroke-linecap:butt;stroke-linejoin:miter"
     id="g578-7"
     transform="translate(0,4)">


I dati relativi al riquadro

 xml
    <text


Inizio del blocco di testo

 xml
       xml:space="preserve"
       style="font-size:4px;font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;line-height:125%;letter-spacing:0px;word-spacing:0px;fill:#000000;fill-opacity:1;stroke:none;font-family:sans;-inkscape-font-specification:sans"


Tutte le informazioni sul testo che verrà visualizzato

 xml
       x="220.9935"
       y="228.95425"
       id="text3331"
       sodipodi:linespacing="125%"


Coordinate e l\'identità in cui verrà visualizzato il testo

 xml
       freecad:editable="AuthorName"><tspan


Qui **AuthorName** è la var gestita da **freecad:editable** che salva la stringa per cambiare ciò che verrà visualizzato

 xml
         sodipodi:role="line"
         id="tspan3333"
         x="220.9935"
         y="228.95425">AUTHOR NAME</tspan></text>


Coordinate e l\'identità del testo che viene visualizzato per impostazione predefinita e **** significa la fine del blocco di testo

 xml
    <text
    ...
    ...
    ...
    ... </text>
  </g>


Altri blocchi di testo e fine **** blocca il raggruppamento del blocco di testo

È possibile che dopo aver lavorato il file SVG con Inkscape non funzioni più, è possibile che l\'informazione sia scomparsa.

Quindi controllare che il testo non sia stato modificato

Esempio :

-   **editable** = \"AuthorName\"
-   replace by **freecad:editable** = \"AuthorName\"

## Altri attributi disponibili 

Vedere la pagina dei [Modelli di squadrature](Drawing_templates/it.md)


{{Drawing Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Poweruser_Documentation](Category_Poweruser_Documentation.md) > [Developer](Category_Developer.md) > [Python_Code](Category_Python_Code.md) > [Macros](Category_Macros.md) > [Drawing](Category_Drawing.md) > Svg Namespace/it
