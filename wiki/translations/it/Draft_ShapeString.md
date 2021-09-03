---
- GuiCommand:/it
   Name:Draft_ShapeString
   Name/it:ShapeString
   Workbenches:[Draft](Draft_Workbench/it.md), [Arch](Arch_Workbench/it.md)
   MenuLocation:Draft → Forma da testo...
   Shortcut:**S** **S**
   SeeAlso:[Testo Draft](Draft_Text/it.md), [Part Estrusione](Part_Extrude/it.md),<br /> [Macro Fonts Win10 PYMP](Macro_Fonts_Win10_PYMP/it.md) <img src="images/Macro_Fonts_Win10_PYMP.png" width=24px>
   Version:0.14---


</div>

## Descrizione


<div class="mw-translate-fuzzy">

Lo strumento ShapeString inserisce una forma composta che riproduce una stringa di testo in un dato punto del documento corrente. Si possono definire gli attributi del testo quali altezza, tipo di carattere, ecc.. La forma risultante può essere utilizzata con lo strumento [Estrusione](Part_Extrude/it.md) di Part per creare lettere 3D.


</div>


<div class="mw-translate-fuzzy">

Per inserire un elemento di testo più semplice senza una forma chiusa, utilizzare <img alt="" src=images/Draft_Text.svg  style="width:24px;"> [Testo](Draft_Text/it.md). Per creare un\'etichetta di testo con una linea guida e una freccia usare <img alt="" src=images/Draft_Label.svg  style="width:24px;"> [Etichetta](Draft_Label/it.md).


</div>

![](images/Draft_ShapeString_Example400.png )


<div class="mw-translate-fuzzy">


*Per posizionare una Shapestring basta un singolo punto*


</div>

## Utilizzo


<div class="mw-translate-fuzzy">

Se la modalità dell\'interfaccia di Draft è impostata su Vista azioni:

1.  Premere il pulsante **<img src="images/Draft_ShapeString.svg" width=16px> [Forma da testo](Draft_ShapeString/it.md)**, o premere i tasti **S** e poi **S**.
2.  Appare una finestra di dialogo in cui è possibile specificare i parametri.
3.  Premere **OK** per creare la forma dal testo.


</div>

## Opzioni


<div class="mw-translate-fuzzy">

-   Per inserire le coordinate manualmente, è sufficiente inserire i numeri, quindi premere **Invio** per ciascun componente X, Y e Z.. È possibile premere il pulsante **<img src="images/Draft_AddPoint.svg" width=16px> [Inserisci punto](Draft_AddPoint/it.md)** quando si hanno i valori desiderati per inserire il punto.
-   Premere il tasto **Esc** o il pulsante {{button|Chiudi}} per interrompere il comando corrente.


</div>

## Notes


<div class="mw-translate-fuzzy">

### Limitazioni

-   Altezze di testo molto ridotte possono causare deformazioni delle forme del carattere a causa della perdita di dettagli nel ridimensionamento.
-   La versione corrente mostra solo un testo scritto in orizzontale da sinistra a destra.
-   Per creare un testo curvo è possibile utilizzare la macro **<img src=images/FCCircularTextButtom.png style="width:24px"> [Testo circolare](Macro_FCCircularText/it.md)**.


</div>

## Tutorial

-   [Tutorial Forma da testo - ShapeString](Draft_ShapeString_tutorial/it.md): come estrudere un testo, posizionarlo nello spazio 3D e creare un\'incisione in un altro corpo.
-   [How to use ShapeStrings in PartDesign](https://forum.freecadweb.org/viewtopic.php?f=3&t=36623)

## Preferences

See also: [Preferences Editor](Preferences_Editor.md) and [Draft Preferences](Draft_Preferences.md).

-   The default font file can be changed in the preferences: {{MenuCommand|Edit → Preferences... → Draft → Texts and dimensions → Default ShapeString font file}}. See [Draft Preferences](Draft_Preferences.md).

## Proprietà

See also: [Property editor](Property_editor.md).

A Draft ShapeString object is derived from a [Part Part2DObject](Part_Part2DObject.md) and inherits all its properties. It also has the following additional properties:

### Data


{{TitleProperty|Draft}}


<div class="mw-translate-fuzzy">

-    **Position**: specifica la posizione del punto base della forma composta.

-    **Angle**: specifica la rotazione della linea di base della forma.

-    **Axis**: specifica l\'asse da utilizzare per la rotazione.

-    **String**: specifica la stringa di testo da visualizzare; a differenza dello strumento [Testo](Draft_Text/it.md), [Forma da testo](Draft_ShapeString/it.md) può visualizzare solo una singola riga.

-    **Size**: specifica l\'altezza generale delle lettere.

-    **Tracking**: specifica la spaziatura inter-carattere aggiuntiva nella stringa.

-    **Font File**: specifica il percorso completo del file di font utilizzato per disegnare la stringa.


</div>

### View


{{TitleProperty|Draft}}

-    **Pattern|Enumeration**: specifies the [Draft Pattern](Draft_Pattern.md) with which to fill the faces of the text. This property only works if **Display Mode** is {{value|Flat Lines}}.

-    **Pattern Size|Float**: specifies the size of the [Draft Pattern](Draft_Pattern.md).

## Scripting


<div class="mw-translate-fuzzy">

## Script


**Vedere anche:**

[API Draft](Draft_API/it.md) e [Nozioni di base sugli script di FreeCAD](FreeCAD_Scripting_Basics/it.md).


</div>


<div class="mw-translate-fuzzy">

Lo strumento ShapeString può essere utilizzato nelle [macro](macros/it.md) e dalla console [Python](Python/it.md) tramite la seguente funzione:


</div>


```python
shapestring = make_shapestring(String, FontFile, Size=100, Tracking=0)
```


<div class="mw-translate-fuzzy">

-   Crea una forma composta `ShapeString` usando la `String` specificata e il percorso completo di un `FontFile` supportato.

-    `Size`è l\'altezza in millimetri del testo risultante.

-    `Tracking`è la spaziatura aggiuntiva tra i caratteri, in millimetri.


</div>

Il posizionamento di `ShapeString` può essere cambiato sovrascrivendo il suo attributo `Placement`, o sovrascrivendo singolarmente i suoi attributi `Placement.Base` e `Placement.Rotation`.

Esempio:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

font1 = "/usr/share/fonts/truetype/msttcorefonts/Arial.ttf"
font2 = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
font3 = "/usr/share/fonts/truetype/freefont/FreeSerifItalic.ttf"

S1 = Draft.make_shapestring("This is a sample text", font1, 200)

S2 = Draft.make_shapestring("Inclined text", font2, 200, 10)

zaxis = App.Vector(0, 0, 1)
p2 = App.Vector(-1000, 500, 0)
place2 = App.Placement(p2, App.Rotation(zaxis, 45))
S2.Placement = place2

S3 = Draft.make_shapestring("Upside-down text", font3, 200, 10)
S3.Placement.Base = App.Vector(0, -1000, 0)
S3.Placement.Rotation = App.Rotation(zaxis, 180)

doc.recompute()
```


<div class="mw-translate-fuzzy">





</div>


 
