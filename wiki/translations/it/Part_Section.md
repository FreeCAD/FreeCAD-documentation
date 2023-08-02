# Part Section/it
---
- GuiCommand:   Name: Part_Section   Name/it: Seziona   MenuLocation: Parte -> Seziona   Workbenches: Part_Workbench/it   Parte---


</div>

## Descrizione


<div class="mw-translate-fuzzy">

Crea una sezione attraverso l\'intersezione di due oggetti selezionati, l\'ultimo oggetto viene utilizzato come piano di sezione. Questa operazione è completamente parametrica: si possono modificare i componenti e il risultato viene ricalcolato.


</div>

-   An intersection of two solids/faces results in one or more section lines.
-   An intersection of two lines, or a line and a solid/face, results in one or more points.

![](images/PartSection1_it.png ) 
*A cube sectioned with a cylinder*

## Utilizzo


<div class="mw-translate-fuzzy">

1.  Selezionare l\'oggetto base
2.  Selezionare l\'oggetto strumento
3.  Cliccare su **Part** → **<img src="images/Part_Section.svg" width=24px>  Seziona** dal menu principale.


</div>

## Properties

See also: [Property editor](Property_editor.md).

A PartDesign Section object is derived from a [Part Feature](Part_Feature.md) object and inherits all its properties. It also has the following additional properties:

### Data


{{Properties_Title|Base}}

-    **Base|Link**: Link to the first object.

-    **Tool|Link**: Link to the second object.


{{Properties_Title|Boolean}}

-    **History|ShapeHistory|hidden**: \"Shape history\".

-    **Refine|Bool**: \"Refine shape (clean up redundant edges) after this boolean operation\". The default value is determined by the **Automatically refine model after sketch-based operation** preference. See [PartDesign Preferences](PartDesign_Preferences#General.md).


{{Properties_Title|Section}}

-    **Approximation|Bool**: Approximate the output edges.

## Link


<div class="mw-translate-fuzzy">

Per creare delle sezioni con un piano di sezione vedere la pagina **Part** → **<img src="images/Part_CrossSections.svg" width=24px>** [Sezioni](Part_SectionCross/it.md).


</div>


<div class="mw-translate-fuzzy">





</div>



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Section/it
