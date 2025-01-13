# Macro Compound Plus/it
<div class="mw-translate-fuzzy">


{{Macro/it
|Name=Macro Compound Plus
|Description=Utilità che combina diversi comandi di Draft.
|Author=Mario52
|Version=00.02
|Date=2018-01-24
|FCVersion=<= 0.17
|Download=[https://www.freecadweb.org/wiki/images/f/fd/Macro_Compound_Plus.png ToolBar Icon]
}}


</div>



## Descrizione


<div class="mw-translate-fuzzy">

Macro utility che riunisce numerosi comandi di Draft per lavorare con gli oggetti 2D. Ad esempio, lavorare con gli oggetti dei file DXF.


</div>


{{Codeextralink|https://gist.githubusercontent.com/mario52a/7be361a8c489deec918f664fdcfc4394/raw/2d12268123cbd38a3fba10fff1c7f35837cd3325/Macro_Compound_Plus.FCMacro}}




<div class="mw-translate-fuzzy">

## Uso


</div>

![Macro_Compound_Plus_00](images/Macro_Compound_Plus_00.png )


<div class="mw-translate-fuzzy">

-    **Compound I**Type I \[1 + 1 = 1\] : Crea un composto unico di tutti gli oggetti selezionati, senza lo storico.

-    **Compound II**Type II \[1 + 1 = A (1 + 1)\] : Crea un composto di tutti gli oggetti selezionati con lo storico di tutti gli oggetti. Stessa funzione di \"**Menu \> Part \> Crea composto**\".

-   Opzioni per le linee:
    -   Line colour : Assegna un colore agli oggetti.
    -   Width line : Assegna uno spessore di linea.

-    ** Convert (A)**= Converte i testi ![](images/Draft_Text.png ) in forme ![](images/Draft_ShapeString.png ) (Lo spessore del testo convertito è rispettato, ma il risultato visivo può non essere rispettato, vedere le proprietà della Vista Combinata per conferma)

-    ** 8.00 **: Gives a thickness of the character and font Family.

-    **Convert Edge**: Questo comando converte una polilinea in una linea con le coordinate. (Es: un composto declassato non ha le coordinate, questa funzione crea una linea con le coordinate)


</div>

### {{CheckBox}} Option color 

If it {{CheckBox}} checked the colour to object to work are coloured (edge, vertex)

-    **{{ColoredText|#ff0000|<img src="images/Workbench_Image.svg" width=16px> Color** }}: Gives a colour to object. (Default Red 255, 0, 0)

### Tools

-   LineEdit : display (Iindex of Font / Number of font) the path and name of the font.

-    **[<img src=images/Draft_Text.svg style="width:16px"> Convert Text (A)**: convert the text <img alt="" src=images/Draft_Text.svg  style="width:16px;"> in a shape string <img alt="" src=images/Draft_ShapeString.svg  style="width:16px;"> (The height of the text converted is respected but the visual result may not be respected, see the Combo view property for confirm). (A) is Automatic value height of text.

    -   
        {{SpinBox|0,00 Auto}}
        
        : If the spinbox is egual 0.0 the heigth of the VALUE of the text is respected, if other of 0.0 the **[<img src=images/Draft_Text.svg style="width:16px"> Convert Text (A)** change to **[<img src=images/Draft_Text.svg style="width:16px"> Convert Text (M)** manual.

-    **[<img src=images/Draft_Line.svg style="width:16px"> Convert Wire (A)**: This command convert the wire in one line with coordinates. (ex: one compound downgraded does not have coordinates, this function create a line with the coordinate as Draft line and reproduce the DXF wire in a Draft object are detected: Line, Arc, Circle, Ellipse, BSplineCurve.

    -   
        {{SpinBox|0,00 Auto}}
        
        : Gives a thickness of the wire. If the spinbox is egual 0.0 the heigth of the VALUE of the text is respected, if other of 0.0 the **<img src="images/Draft_Line.svg" width=16px> Convert Wire (A)** change to **Convert Wire (M)** manual.

-    {{CheckBox|<img src="images/Draft_BezCurve.svg" width=16px> BezierCurve}}: By default the BezierCurve detected is <img alt="" src=images/Draft_BezCurve.svg  style="width:24px;">, if it is checked the BezierCurve is Cubic <img alt="" src=images/Draft_CubicBezCurve.svg  style="width:24px;"> and the button change {{CheckBox|TRUE|<img src="images/Draft_CubicBezCurve.svg" width=16px> Cubic BezierCurve}}

-    {{RadioButton|TRUE|<img src="images/Std_DrawStyleFlatLines.svg" width=16px> FlatLines}}: The objects created is FlatLines.

-    {{RadioButton|<img src="images/Std_DrawStyleWireFrame.svg" width=16px> Wireframe}}: The objects created is Wireframe.

-    {{RadioButton|<img src="images/Std_DrawStylePoints.svg" width=16px> Points}}: The objects created is Points.

-    **[<img src=images/Draft_Upgrade.svg style="width:16px"> UpGrade**: UpGrade

-    **[<img src=images/Draft_Downgrade.svg style="width:16px"> DownGrade**: DownGrade


<div class="mw-translate-fuzzy">

-   Per Compound I e Convert Edge

Questa sezione lavora solo con i menu **Compound I**, **Convert (A)** e **Convert Edge**

-    **None**: Tutti gli oggetti originali restano così come sono.

-    **Hidden original line(s)**: Nasconde le linee originali.

-    **Delete original line(s)**: Elimina le linee originali.

-    **Reset**: Reset della macro

-    **DownGrade**: Declassa gli oggetti, allo stesso modo di ![](images/Draft_Downgrade.png ).

-    **Quit**: Esce dalla macro


</div>

### Force on a form : Line 

If the object line, arc or circle is not reconized (as form in a volume 3D object), this section force the creation of Line, Arc or Circle.

no verification is done, this section tray to create a requested shape 2D (Draft) based on the data provided

-    {{RadioButton|TRUE|<img src="images/Draft_Line.svg" width=16px> Lines}}: Tray to create a Line.

-    {{RadioButton|<img src="images/Draft_Arc.svg" width=16px> Arc}}: Tray to create a Arc.

-    {{RadioButton|<img src="images/Draft_Circle.svg" width=16px> Circle}}: Tray to create a Circle.

-    **<img src="images/Draft_Line.svg" width=16px> Force on : Line**: Button Force

### Command

-   ProgressBar

-    **Reset**: Reset the macro

-    **Quit**: Quit the macro, bye

-    **Help**: Display the wiki page in the FreeCAD browser

## Script

L\'icona per la barra degli strumenti ![](images/Macro_Compound_Plus.png ) da copiare nella stessa cartella della macro

[Come personalizzare la barra degli strumenti](Customize_Toolbars/it.md), [Come installare le macro](How_to_install_macros/it.md)

Lo script in github [Macro_Compound_Plus.FCMacro](https://gist.github.com/mario52a/7be361a8c489deec918f664fdcfc4394)

## Link

Le mie macro su [Github](https://gist.github.com/mario52a)


<div class="mw-translate-fuzzy">

## Versioni

-   24/01/2018 ver 00.02 : sup \"import PyQt4\"
-   21/11/2016 ver 00.01 :


</div>



---
⏵ [documentation index](../README.md) > Macro Compound Plus/it
