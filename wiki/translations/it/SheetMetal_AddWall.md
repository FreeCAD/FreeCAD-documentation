---
- GuiCommand:/it
   Name:SheetMetal_Bend
   Name/it:Piega
   MenuLocation:SheetMetal → Add Bend
   Workbenches:[SheetMetal](SheetMetal_Workbench/it.md)
   Shortcut:None
   Version:
   SeeAlso:
---


</div>

## Descrizione


<div class="mw-translate-fuzzy">

Lo strumento di piegatura di SheetMetal <img alt="" src=images/SheetMetal_Bend.svg  style="width:24px;"> crea una piega sul bordo selezionato.

<img alt="" src=images/PostBend.png  style="width:320px;">


</div>

<img alt="" src=images/PostBend.png  style="width:320px;">

## Utilizzo

Per aggiungere una piega:

1.  Passare nell\'ambiente <img alt="" src=images/Sheetmetal_workbench_icon.svg  style="width:22px;"> SheetMetal.
2.  Iniziare con una lastra di base o un foglio, selezionare uno o più bordi che devono ricevere una piega.
3.  Cliccare sullo strumento <img alt="" src=images/SheetMetal_Bend.svg  style="width:24px;"> **Bend** per aggiungere una piega.


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

::\* Usare <img alt="" src=images/Part_Thickness.svg  style="width:24px;"> [Spessore di Part](Part_Thickness/it.md) per creare un solido (**Tipicamente con il valore dello spessore della lamiera.**)


</div>


:   

    :   Se si inizia con un <img alt="" src=images/PartDesign_Body.svg  style="width:24px;"> Corpo di PartDesign, è possibile combinare funzioni di Sheet Metal con funzioni di PartDesign come <img alt="" src=images/PartDesign_Pocket.svg  style="width:24px;"> [tasche](PartDesign_Pocket/it.md) o <img alt="" src=images/PartDesign_Hole.svg  style="width:24px;"> [fori](PartDesign_Hole/it.md).

## Proprietà

### Dati


{{Properties_Title|Base}}

-    **Label**: Nome assegnato dall\'utente all\'oggetto nella [vista ad albero](Tree_view/it.md).


{{Properties_Title|Parameters}}

-    **angle**: Angolo di piega.

-    **extend1**: Estende il lato sinistro.

-    **extend2**: Estende il lato destro.

-    **gap1**: Distanza sul lato sinistro del lembo piegato dall\'angolo della forma base.

-    **gap2**: Distanza dall\'angolo dal lato destro.

-    **invert**: Inverte la direzione della piega.

-    **length**: Lunghezza della parte piegata .

-    **miterangle1**: Piega con un angolo di mitra sul lato sinistro.

-    **miterangle2**: Piega con un angolo di mitra sul lato destro.

-    **radius**: Raggio di curvatura della piega.

-    **relief Type**: Gole di scarico Rettangolari o arrotondate. Abilitato solo quando è impostato un valore di gap.

-    **reliefd**: Profondità della gola di scarico. Abilitata solo quando è impostato un valore di gap.

-    **reliefw**: Larghezza della gola di scarico. Abilitata solo quando è impostato un valore di gap.

-    **kfactor**: Fattore K (noto anche come fattore neutro) per la curva. Utilizzato per calcolare la tolleranza di piegatura durante lo sviluppo.

-    **unfold**: False (predefinito) o True. Se è vero, dispiega la curva.

## Example

<img alt="" src=images/SheetMetal_AddWall-01.png  style="width:300px;"> 
*A simple tray*


<div class="mw-collapsible mw-collapsed">


<div class="mw-collapsible-content">

### Preparation

This tray is made of a rectangular blank with walls added to its outline edges. And so one outline sketch for the blank has to be prepared in advance.

<img alt="" src=images/SheetMetal_AddWall-02.png  style="width:200px;"> 
*Just a rectangular outline*

### Workflow

1.  Create a blank
    1.  Select the outline sketch  <img alt="" src=images/SheetMetal_AddWall-03.png  style="width:240px;">
    2.  Press the  or use the keyboard shortcut:  <img alt="" src=images/SheetMetal_AddWall-04.png  style="width:240px;">  (The blank is padded in z direction  
2.  Add walls to the outline edges
    1.  Select the blank\'s **outline edges**  <img alt="" src=images/SheetMetal_AddWall-05.png  style="width:240px;">
    2.  Press the  or use the keyboard shortcut:  <img alt="" src=images/SheetMetal_AddWall-06.png  style="width:240px;">
    3.  If the fold is 90° down set the value of **invert** property to true to reverse the direction (and **length** to a lower value for smaller walls)  <img alt="" src=images/SheetMetal_AddWall-01.png  style="width:240px;">  
3.  Add some more walls
    1.  Select the tray\'s **upper outside edges**  <img alt="" src=images/SheetMetal_AddWall-08.png  style="width:240px;">
    2.  Press the  or use the keyboard shortcut:  <img alt="" src=images/SheetMetal_AddWall-09.png  style="width:240px;"> 
    3.  The walls are a bit too long (but nicely trimmed) and so the **length** property has to be set to a lower value  <img alt="" src=images/SheetMetal_AddWall-10.png  style="width:240px;">
    4.  If you like the folds swing outward set the **invert** value to true  <img alt="" src=images/SheetMetal_AddWall-11.png  style="width:240px;">

Done!


</div>


</div>


<div class="mw-translate-fuzzy">





</div>

[Category:SheetMetal](Category:SheetMetal.md) [Category:Addons](Category:Addons.md) [Category:External Command Reference](Category:External_Command_Reference.md)
