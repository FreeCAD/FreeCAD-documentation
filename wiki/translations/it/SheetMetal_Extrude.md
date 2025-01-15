---
 GuiCommand:
   Name: SheetMetal_Extrude
   Name/it: Estendi
   MenuLocation: SheetMetal , Extrude
   Workbenches: SheetMetal Workbench/it
   Shortcut: None
   Version: 
   SeeAlso: 
---

# SheetMetal Extrude/it


</div>



## Descrizione


<div class="mw-translate-fuzzy">

Lo strumento <img alt="" src=images/SheetMetal_Extrude.svg  style="width:24px;"> Extrude estende una faccia del foglio di lamiera.


</div>

It creates a **simple extension** along the face normal of the selected edge face:

<img alt="" src=images/SheetMetal_Extrude-01.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_Extrude-02.png  style="width:200px;">

If an outline sketch is added it creates **interlocking geometry** to close a profile:

<img alt="" src=images/SheetMetal_Extrude-05.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_Extrude-04.png  style="width:200px;">



*Three profiles with outline sketches to add → three results*



## Utilizzo

### Simple Extension 


<div class="mw-translate-fuzzy">

Per estendere la faccia:

1.  Iniziare con una piastra di base o un foglio, selezionare una faccia sottile che rappresenta lo spessore della lamiera
2.  Cliccare sullo strumento <img alt="" src=images/SheetMetal_Extrude.svg  style="width:24px;"> **Extrude** per estendere la faccia.


</div>

### Interlocking Extension 

:   (Prepare a <img alt="" src=images/Workbench_Sketcher.svg  style="width:16px;"> [sketch](Sketcher_Workbench.md) for interlocking tabs)

1.  Select the edge face to be extended.
2.  Invoke the command as described above.
3.  Press the **OK** button to finish the command and close the Task panel.
4.  In the [Property editor](Property_editor.md) press the **...** button of the **Sketch** property.
5.  The Link dialog window opens.
    -   Select the prepared sketch from the list
    -   Press the **OK** button to close the dialog.
6.  Set the property **Use Subtraction** to `True` to create cut-outs to make room for the extensions.
7.  Set the property **Offset** to adjust the clearance around the extension.

<img alt="" src=images/SheetMetal_Extrude-03.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_Extrude-05.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_Extrude-06.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_Extrude-04.png  style="width:200px;">



*Three profiles → position of the sketches → results without cut-outs → final results*

### Notes


<div class="mw-translate-fuzzy">


**Nota**

: questo ambiente non dispone di uno strumento per creare una piastra di base, quindi è necessario avviare il modello con uno dei seguenti metodi:

  - Metodo 1: <img alt="" src=images/Part_Box.svg  style="width:24px;"> [Cubo di Part](Part_Box/it.md)

  - Metodo 2: Un solido estruso realizzato con <img alt="" src=images/Part_Extrude.svg  style="width:24px;"> [Estrudi di Part](Part_Extrude/it.md) da un:

:  - <img alt="" src=images/Draft_Rectangle.svg  style="width:24px;"> [Rettangolo di Draft](Draft_Rectangle/it.md) o una

:  - <img alt="" src=images/Draft_Wire.svg  style="width:24px;"> [Polilinea di Draft](Draft_Wire/it.md) o uno

:  - <img alt="" src=images/Sketcher_NewSketch.svg  style="width:24px;"> [Schizzo](Sketcher_NewSketch/it.md)

  - Metodo 3: <img alt="" src=images/PartDesign_Body.svg  style="width:24px;"> [Corpo di PartDesign](PartDesign_Body/it.md) contenente un

:  - <img alt="" src=images/PartDesign_AdditiveBox.svg  style="width:24px;"> [cubo additivo](PartDesign_AdditiveBox/it.md) o un

:  - <img alt="" src=images/PartDesign_Pad.svg  style="width:24px;"> [pad](PartDesign_Pad/it.md) prodotto da uno <img alt="" src=images/Sketcher_NewSketch.svg  style="width:24px;"> [schizzo](Sketcher_NewSketch/it.md).


</div>


:   After inserting a sketch, at least one of its outlines must at least touch one opposite face or the tool will fail to create any extension or cut-out.





:   Just one outline touching an opposite face is enough to create extension geometry from all outlines of the sketch.

-   Each cut-out will have a cuboid shape, no matter what shape the corresponding outline sketch is.

-   Shapes other than rectangles may behave little bit strange and even though the object can be unfolded, the result will not turn out as expected.

<img alt="" src=images/SheetMetal_Extrude-07.png  style="width:250px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_Extrude-08.png  style="width:250px;">



*Three outline sketches and their resulting extensions: separate triangle plate with a rectangular cut-out, circle without clearance → unfold solid is split at an unexpected position *


<div class="mw-translate-fuzzy">


**Nota**

: In un\'operazione di estensione, impostare `Refine {{:=` true}}.


</div>

-   The extension operation with a linked sketch may fail due to coplanar issues if the face on the sketch side and the face on the opposite side are coplanar, but with opposite orientations. A small offset may help in such a case.



## Proprietà

See also: [Property editor](Property_editor.md).

A SheetMetal Extend object is derived from a [Part Feature](Part_Feature.md) object or, if it is inside a [PartDesign Body](PartDesign_Body.md), from a [PartDesign Feature](PartDesign_Feature.md) object, and inherits all its properties. It also has the following additional properties:



### Dati


{{Properties_Title|Parameters}}


<div class="mw-translate-fuzzy">

-    **gap1**: Distanza dal lato sinistro.

-    **gap2**: Distanza dal lato destro.

-    **length**: Lunghezza.


</div>


{{Properties_Title|Parameters Ext.}}

-    **Offset|Distance**: \"Offset for subtraction\". Default: {{value|20,00 µm}}.

-    **Refine|Bool**: \"Use Refine\". Default: `True`.

-    **Sketch|Link**: \"Wall Sketch\".

-    **Use Subtraction|Bool**: \"Use Subtraction\". Default: `False`


<div class="mw-translate-fuzzy">





</div>



---
⏵ [documentation index](../README.md) > [SheetMetal](Category_SheetMetal.md) > [Addons](Category_Addons.md) > [External Command Reference](Category_External%20Command%20Reference.md) > SheetMetal Extrude/it
