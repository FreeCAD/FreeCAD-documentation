---
- GuiCommand:/it
   Name:SheetMetal_Junction
   Name/it:Giunzione
   MenuLocation:SheetMetal → Junction
   Workbenches:[SheetMetal](SheetMetal_Workbench/it.md)
   Shortcut:None
   Version:
   SeeAlso:
---


</div>

## Descrizione


<div class="mw-translate-fuzzy">

Lo strumento <img alt="" src=images/SheetMetal_Junction.svg  style="width:24px;"> SheetMetal Junction.


</div>

<img alt="" src=images/PostGap.png  style="width:320px;">


<div class="mw-translate-fuzzy">


:   <img alt="" src=images/PostGap.png  style="width:320px;">
:   
    *Giunzione applicata all'angolo.
    *
    


</div>

## Utilizzo

Per aggiungere la giunzione nel vertice di un angolo:

1.  Iniziare con una piastra di base o un foglio, selezionare un vertice d\'angolo a cui applicare lo scarico
2.  Fare clic sullo strumento <img alt="" src=images/SheetMetal_Junction.svg  style="width:24px;"> **Junction** per aggiungere un taglio di giunzione all\'angolo.


<div class="mw-translate-fuzzy">


**Nota**

: questo ambiente non dispone di uno strumento per creare una piastra di base, quindi è necessario avviare il modello con uno dei seguenti metodi:

:\* Metodo 1: <img alt="" src=images/Part_Box.svg  style="width:24px;"> [Cubo di Part](Part_Box/it.md)

:\* Metodo 2: Un solido estruso realizzato con <img alt="" src=images/Part_Extrude.svg  style="width:24px;"> [Estrudi di Part](Part_Extrude/it.md) da un:

::\* <img alt="" src=images/Draft_Rectangle.svg  style="width:24px;"> [Rettangolo di Draft](Draft_Rectangle/it.md) o una

::\* <img alt="" src=images/Draft_Wire.svg  style="width:24px;"> [Polilinea di Draft](Draft_Wire/it.md) o uno

::\* <img alt="" src=images/Sketcher_NewSketch.svg  style="width:24px;"> [Schizzo](Sketcher_NewSketch/it.md)

::\* Usare <img alt="" src=images/Part_Thickness.svg  style="width:24px;"> [Spessore di Part](Part_Thickness/it.md) per creare un solido (**Tipicamente con il valore dello spessore della lamiera.**)

:\* Metodo 3: <img alt="" src=images/PartDesign_Body.svg  style="width:24px;"> [Corpo di PartDesign](PartDesign_Body/it.md) contenente un

::\* <img alt="" src=images/PartDesign_AdditiveBox.svg  style="width:24px;"> [cubo additivo](PartDesign_AdditiveBox/it.md) o un

::\* <img alt="" src=images/PartDesign_Pad.svg  style="width:24px;"> [pad](PartDesign_Pad/it.md) prodotto da uno <img alt="" src=images/Sketcher_NewSketch.svg  style="width:24px;"> [schizzo](Sketcher_NewSketch/it.md).

::\* Usare <img alt="" src=images/Part_Thickness.svg  style="width:24px;"> [Spessore di Part](Part_Thickness/it.md) per creare un solido (**Tipicamente con il valore dello spessore della lamiera**).


</div>


:   

    :   Se si inizia con un <img alt="" src=images/PartDesign_Body.svg  style="width:24px;"> Corpo di PartDesign, è possibile combinare funzioni di Sheet Metal con funzioni di PartDesign come <img alt="" src=images/PartDesign_Pocket.svg  style="width:24px;"> [tasche](PartDesign_Pocket/it.md) o <img alt="" src=images/PartDesign_Hole.svg  style="width:24px;"> [fori](PartDesign_Hole/it.md).

## Proprietà

See also: [Property editor](Property_editor.md).

A SheetMetal Junction object is derived from a [Part Feature](Part_Feature.md) object and inherits all its properties. It also has the following additional properties and its label has a default value:

### Dati


{{Properties_Title|Base}}


<div class="mw-translate-fuzzy">

-    **Label**: Nome assegnato dall\'utente all\'oggetto nella [vista ad albero](Tree_view/it.md).


</div>


{{Properties_Title|Parameters}}


<div class="mw-translate-fuzzy">

-    **gap**: Dimensione della fessura di giunzione da aggiungere.


</div>


<div class="mw-translate-fuzzy">





</div>

[Category:SheetMetal](Category:SheetMetal.md) [Category:Addons](Category:Addons.md) [Category:External Command Reference](Category:External_Command_Reference.md)
