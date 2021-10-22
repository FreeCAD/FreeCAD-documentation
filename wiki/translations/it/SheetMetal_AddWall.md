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

# SheetMetal AddWall/it


</div>

## Descrizione


<div class="mw-translate-fuzzy">

Lo strumento di piegatura di SheetMetal <img alt="" src=images/SheetMetal_Bend.svg  style="width:24px;"> crea una piega sul bordo selezionato.

<img alt="" src=images/PostBend.png  style="width:320px;">


</div>

A **flange** consists of a 90° cylindrical bend and a planar strip (wall).

<img alt="" src=images/SheetMetal_AddWall-12.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_AddWall-13.png  style="width:200px;"> 
*Two selected edges -> two flanges*

Resetting the **angle** property to about 180° in a second step will create a **hem** instead.

<img alt="" src=images/SheetMetal_AddWall-14.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_AddWall-15.png  style="width:200px;"> 
*Two selected edges -> two hems*

## Utilizzo


<div class="mw-translate-fuzzy">

Per aggiungere una piega:

1.  Passare nell\'ambiente <img alt="" src=images/Sheetmetal_workbench_icon.svg  style="width:22px;"> SheetMetal.
2.  Iniziare con una lastra di base o un foglio, selezionare uno o più bordi che devono ricevere una piega.
3.  Cliccare sullo strumento <img alt="" src=images/SheetMetal_Bend.svg  style="width:24px;"> **Bend** per aggiungere una piega.


</div>

## Notes


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

::\* <img alt="" src=images/PartDesign_Pad.svg  style="width:24px;"> _.

::\* Usare <img alt="" src=images/Part_Thickness.svg  style="width:24px;"> [Spessore di Part](Part_Thickness/it.md) per creare un solido (**Tipicamente con il valore dello spessore della lamiera.**)


</div>

Alternatively a base plate (blank) can be created with commands from the <img alt="" src=images/Workbench_Part.svg  style="width:16px;"> _.

To create a blank with the [Part Workbench](Part_Workbench.md):

1.  Create a solid using either:
    -   <img alt="" src=images/Part_Box.svg  style="width:16px;"> [Part Box](Part_Box.md).
    -   <img alt="" src=images/Part_Extrude.svg  style="width:16px;"> [Part Extrude](Part_Extrude.md) from:
        -   A <img alt="" src=images/Draft_Rectangle.svg  style="width:16px;"> [Draft Rectangle](Draft_Rectangle.md).
        -   A <img alt="" src=images/Draft_Wire.svg  style="width:16px;"> [Draft Wire](Draft_Wire.md).
        -   A <img alt="" src=images/Sketcher_NewSketch.svg  style="width:16px;"> [Sketch](Sketcher_NewSketch.md).
2.  Make sure one the dimensions of the Box or the extrusion distance equals the sheet metal thickness.

To create a blank with the [PartDesign Workbench](PartDesign_Workbench.md):

1.  Create a solid using either:
    -   <img alt="" src=images/PartDesign_AdditiveBox.svg  style="width:16px;"> [Additive Box](PartDesign_AdditiveBox.md).
    -   <img alt="" src=images/PartDesign_Pad.svg  style="width:16px;"> _.
2.  Make sure one the dimensions of the Box or the **Length** property of the Pad equals the sheet metal thickness.


<div class="mw-translate-fuzzy">


:   

    :   Se si inizia con un <img alt="" src=images/PartDesign_Body.svg  style="width:24px;"> Corpo di PartDesign, è possibile combinare funzioni di Sheet Metal con funzioni di PartDesign come <img alt="" src=images/PartDesign_Pocket.svg  style="width:24px;"> _.


</div>

## Proprietà

See also: [Property editor](Property_editor.md).

A SheetMetal Bend object is derived from a [Part Feature](Part_Feature.md) object and inherits all its properties. It also has the following additional properties and its label has a default value:

### Dati


{{Properties_Title|Base}}


<div class="mw-translate-fuzzy">

-    **Label**: Nome assegnato dall\'utente all\'oggetto nella [vista ad albero](Tree_view/it.md).


</div>


{{Properties_Title|Parameters}}


<div class="mw-translate-fuzzy">

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


</div>


{{Properties_Title|Parameters Ex}}

-    **Auto Miter|Bool**: \"Enable Auto Miter\". Default: `True`.

-    **extend1|Distance**: \"Extend from Left Side\". Default: {{value|0,00 mm}}.

-    **extend2|Distance**: \"Extend from Right Side\". Default: {{value|0,00 mm}}.

-    **kfactor|FloatConstraint**: \"Location of Neutral Line. Caution: Using ANSI standards, not DIN.\".  Default: {{value|0,50}}. K factor (also known as neutral factor) for the bend. Used to calculate bend allowance when unfolding.

-    **max Extend Dist|Length**: \"Auto Miter maximum Extend Distance\". Default: {{value|5,00 mm}}.

-    **min Gap|Length**: \"Auto Miter Minimum Gap\". Default: {{value|5,00 mm}}.

-    **miterangle1|Angle**: \"Bend Miter Angle from Left Side\". Default angle: {{value|0,00°}}.

-    **miterangle2|Angle**: \"Bend Miter Angle from Right Side\". Default angle: {{value|0,00°}}.

-    **offset|Distance**: \"Offset Bend\". Default: {{value|0,00 mm}}.

-    **unfold|Bool**: \"Shows Unfold View of Current Bend\". Default:  `True` unfolds the bend.


{{Properties_Title|Parameters Ex2}}

-    **Sketch|Link**: \"Sketch Object\".

-    **sketchflip|Bool**: \"Flip Sketch Direction\". Default: `False`.

-    **sketchinvert|Bool**: \"Invert Sketch Start\". Default: `False`.


{{Properties_Title|Parameters Ex3}}

-    **Length List|FloatList**: \"Length of Wall List\". Default: {{value|[10,00]}}.

-    **bend AList|FloatList**: \"Bend Angle List\". Default: {{value|[90,00]}}.


{{Properties_Title|Parameters Relief}}

-    **Relief Factor|Float**: \"Relief Factor\". Default: {{value|0,70}}.

-    **Use Relief Factor|Bool**: \"Use Relief Factor\". Default: `False`.

-    **min Relief Gap|Length**: \"Minimum Gap to Relief Cut\". Default: {{value|1,00 mm}}.

-    **relief Type|Enumeration**: \"Relief Type\". {{value|Rectangle}} (default), {{value|Round}}. Enabled only when a gap value is set.

-    **reliefd|Length**: \"Relief Depth\". Default: {{value|1,00 mm}}. Enabled only when a gap value is set.

-    **reliefw|Length**: \"Relief Width\". Default: {{value|0,80 mm}}. Enabled only when a gap value is set.

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

_ _ _

---
[documentation index](../README.md) > [SheetMetal](Category_SheetMetal.md) > SheetMetal AddWall/it
