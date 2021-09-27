---
- GuiCommand:/it
   Name:SheetMetal_Extrude
   Name/it:Estendi
   MenuLocation:SheetMetal → Extrude
   Workbenches:[SheetMetal](SheetMetal_Workbench/it.md)
   Shortcut:None
   Version:
   SeeAlso:
---

# SheetMetal Extrude/it


</div>

## Descrizione


<div class="mw-translate-fuzzy">

Lo strumento <img alt="" src=images/SheetMetal_Extrude.svg  style="width:24px;"> Extrude estende una faccia del foglio di lamiera.


</div>

## Utilizzo

Per estendere la faccia:

1.  Iniziare con una piastra di base o un foglio, selezionare una faccia sottile che rappresenta lo spessore della lamiera
2.  Cliccare sullo strumento <img alt="" src=images/SheetMetal_Extrude.svg  style="width:24px;"> **Extrude** per estendere la faccia.


<div class="mw-translate-fuzzy">


**Nota**

: questo ambiente non dispone di uno strumento per creare una piastra di base, quindi è necessario avviare il modello con uno dei seguenti metodi:

:\* Metodo 1: <img alt="" src=images/Part_Box.svg  style="width:24px;"> [Cubo di Part](Part_Box/it.md)

:\* Metodo 2: Un solido estruso realizzato con <img alt="" src=images/Part_Extrude.svg  style="width:24px;"> [Estrudi di Part](Part_Extrude/it.md) da un:

::\* <img alt="" src=images/Draft_Rectangle.svg  style="width:24px;"> [Rettangolo di Draft](Draft_Rectangle/it.md) o una

::\* <img alt="" src=images/Draft_Wire.svg  style="width:24px;"> [Polilinea di Draft](Draft_Wire/it.md) o uno

::\* <img alt="" src=images/Sketcher_NewSketch.svg  style="width:24px;"> [Schizzo](Sketcher_NewSketch/it.md)

:\* Metodo 3: <img alt="" src=images/PartDesign_Body.svg  style="width:24px;"> [Corpo di PartDesign](PartDesign_Body/it.md) contenente un

::\* <img alt="" src=images/PartDesign_AdditiveBox.svg  style="width:24px;"> [cubo additivo](PartDesign_AdditiveBox/it.md) o un

::\* <img alt="" src=images/PartDesign_Pad.svg  style="width:24px;"> _.


</div>


:   

    :   Se si inizia con un <img alt="" src=images/PartDesign_Body.svg  style="width:24px;"> Corpo di PartDesign, è possibile combinare funzioni di Sheet Metal con funzioni di PartDesign come <img alt="" src=images/PartDesign_Pocket.svg  style="width:24px;"> _.


**Nota**

: In un\'operazione di estensione, impostare `Refine {{:=` true}}.

## Proprietà

See also: [Property editor](Property_editor.md).

A SheetMetal Extend object is derived from a [Part Feature](Part_Feature.md) object and inherits all its properties. It also has the following additional properties:

### Dati


{{Properties_Title|Base}}

-    **Label|String**: Default value: The user editable name of this object, it may be any arbitrary UTF8 string.

-    **Base Feature|Link|hidden**: Base Feature. Link to the parent feature.

-    **_Body|LinkHidden|hidden**: Hidden link to the parent body.


{{Properties_Title|Parameters}}


<div class="mw-translate-fuzzy">

-    **gap1**: Distanza dal lato sinistro.

-    **gap2**: Distanza dal lato destro.

-    **length**: Lunghezza.


</div>


{{Properties_Title|Parameters Ext.}}

-    **Offset|Distance**: \"Offset for substraction\". Default: {{value|20,00 µm}}.

-    **Refine|Bool**: \"Use Refine\". Default: `True`.

-    **Sketch|Link**: \"Wall Sketch\".

-    **Use Substraction|Bool**: \"Use Substraction\". Default: `False`


<div class="mw-translate-fuzzy">





</div>

_ _ _

---
[documentation index](../README.md) > [SheetMetal](Category_SheetMetal.md) > SheetMetal Extrude/it
