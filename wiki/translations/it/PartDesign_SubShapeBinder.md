---
- GuiCommand:
   Name:PartDesign SubShapeBinder
   Name/it:Lega forme secondarie
   Workbenches:[PartDesign](PartDesign_Workbench/it.md)
   MenuLocation:Part Design → Forme legate secondarie
   Version:0.19
   SeeAlso:[PartDesign Forme legate](PartDesign_ShapeBinder/it.md), [PartDesign Clona](PartDesign_Clone/it.md)
---

# PartDesign SubShapeBinder/it


</div>

## Descrizione


<div class="mw-translate-fuzzy">

[PartDesign SubShapeBinder](PartDesign_SubShapeBinder/it.md) importa un elemento da un altro corpo nel [Corpo](PartDesign_Body/it.md) attivo. Può prendere delle [Forme](Shape/it.md) o essere \"associato\" a uno o più oggetti o sottoelementi (bordi o facce) di un altro oggetto.


</div>


<div class="mw-translate-fuzzy">

Può anche legare oggetti nidificati all\'interno di [Parti](Std_Part/it.md) e seguirà il posizionamento relativo di queste funzioni. Ciò è utile nel contesto della creazione di [assemblaggi](Assembly/it.md), poiché spesso si deve fare riferimento a [funzioni](PartDesign_Feature/it.md) che sono già correttamente posizionate in un altro sottoassieme.


</div>

The referenced geometry can consist of one or multiple elements. Each element can be an individual object (for example a [PartDesign Body](PartDesign_Body.md)), a subobject (for example a [Part Box](Part_Box.md) inside a [Std Part](Std_Part.md), or a [sketch](PartDesign_NewSketch.md) or [Feature](PartDesign_Feature.md) inside a Body), or a subelement (a face, edge or vertex). Which geometry should be selected depends on the intended purpose of the SubShapeBinder. For a Boolean operation you would need to select a solid. For a [Pad operation](PartDesign_Pad.md) a face, a sketch or a planar wire can be used. And for the [external geometry](Sketcher_External.md) in a sketch, or to attach a sketch, any combination of subelements may be appropriate. Elements can belong to different parent objects, and can even belong to the Body the SubShapeBinder is nested in. Because a SubShapeBinder is [Link-based](Std_LinkMake.md) the referenced geometry can also belong to an external document.

<img alt="" src=images/PartDesign_SubShapeBinder_example_1.png  style="width:" height="300px;"> <img alt="" src=images/PartDesign_SubShapeBinder_example_2.png  style="width:" height="300px;">


<div class="mw-translate-fuzzy">



*A sinistra: due solidi creati in due [corpi](PartDesign_Body/it.md) separati. A destra: due SubShapeBinders estratti dal primo corpo, importati nel secondo corpo e spostati in una posizione diversa.*


</div>

<img alt="" src=images/PartDesign_SubShapeBinder_example_3.png  style="width:" height="300px;">


<div class="mw-translate-fuzzy">



*I due SubShapeBinders vengono utilizzati per creare un [taglio booleano](PartDesign_Boolean/it.md) e un [pad](PartDesign_Pad/it.md), con il secondo corpo.*


</div>

## Utilizzo

### Same document 

1.  If there are multiple Bodies in the document: optionally [activate the Body](PartDesign_Body#Active_status.md) the SubShapeBinder should be nested in.
2.  Select the required geometry. Subelements can only be selected in the [3D view](3D_view.md).
3.  There are several ways to invoke the tool:
    -   Press the **<img src="images/PartDesign_SubShapeBinder.svg" width=16px> [PartDesign SubShapeBinder](PartDesign_SubShapeBinder.md)** button.
    -   Select the **Part Design → <img src="images/PartDesign_SubShapeBinder.svg" width=16px> Create a sub-object(s) shape binder** option from the menu.
4.  The SubShapeBinder is created.
5.  If there is only one Body in the document the SubShapeBinder is automatically added to it and the Body is activated. If this is the case and the SubShapeBinder should not be nested, it can be dragged out of the Body and dropped onto the <img alt="" src=images/Document.svg  style="width:16px;"> document node in the [Tree view](Tree_view.md).

### External document 

1.  If required open the source document (the external document) and the target document. Both documents must have been saved at least once.
2.  If there are multiple Bodies in the target document: optionally activate the Body the SubShapeBinder should be nested in.
3.  Select the required geometry in the source document. Subelements can only be selected in the [3D view](3D_view.md).
4.  Switch to the target document by clicking its tab in the [Main view area](Main_view_area.md).
5.  Invoke the tool as described above.

### Start with empty SubShapeBinder 

1.  Follow the instructions described under [Same document](#Same_document.md) above but without selecting geometry.
2.  An empty SubShapeBinder is created.
3.  Select the required geometry. Subelements can only be selected in the [3D view](3D_view.md).
4.  In the [Tree view](Tree_view.md) drag and drop the selection onto the SubShapeBinder. If you have selected subelements their parent objects are highlighted in the [Tree view](Tree_view.md), indicating the objects to be dragged.
5.  Optionally add more geometry in the same manner.
6.  To replace already referenced geometry hold down **Ctrl** during the drag and drop operation.

## Notes

-   2D offsetting is supported for some shape types, included planar faces, edges and wires. Because offsetting is a difficult operation for the software it does not always succeed. <small>(v0.20)</small> 
-   A SubShapeBinder that is not nested in a Body can be used as the [Base Feature](PartDesign_Body#Base_Feature.md) for a new Body.
-   The **Support** property contains the links to the referenced geometry. The property is read only by default, but can be changed by following the instructions described under [Start with empty SubShapeBinder](#Start_with_empty_SubShapeBinder.md).
-   A SubShapeBinder created from a sketch can have an opposite \"tool direction\". For example a [Pad](PartDesign_Pad.md) created from the sketch may extend in the +Y direction, while a [Pad](PartDesign_Pad.md), with the same properties, created from the SubShapeBinder extends in the -Y direction. Toggling the **Reversed** property (or checkbox) will solve this.

## PartDesign SubShapeBinder vs. PartDesign ShapeBinder 

The PartDesign SubShapeBinder tool and the [PartDesign ShapeBinder](PartDesign_ShapeBinder.md) tool are quite similar. Their names are somewhat confusing as both can reference whole objects and subelements.

The main differences are:

-   Editing a PartDesign ShapeBinder is easier. Double-clicking the object in the [Tree view](Tree_view.md) will open a task panel.
-   A PartDesign ShapeBinder can either reference a single whole object, or subelements belong to a single parent object. A PartDesign SubShapeBinder does not have these restrictions.
-   Only PartDesign SubShapeBinders can reference geometry from an external file.
-   A PartDesign SubShapeBinder always tracks the relative placement of the referenced geometry. For a PartDesign ShapeBinder this behavior is optional through its **Trace Support** property.
-   Only PartDesign SubShapeBinders support 2D offsetting.

## Proprietà


<div class="mw-translate-fuzzy">

[SubShapeBinder](PartDesign_SubShapeBinder/it.md) deriva da una [Funzione Part](Part_Feature/it.md) (classe `Part::Feature`). Oltre alle proprietà elencate in [Funzione Part](Part_Feature/it.md), nell\'[editor delle proprietà](property_editor/it.md) sono disponibili le seguenti proprietà.


</div>

### Dati


{{TitleProperty|Base}}


<div class="mw-translate-fuzzy">

-    **Support|XLinkSubList|hidden**: supporto per la geometria.

-    **Fuse|Bool**: se è `True` fonde le forme solide legate.

-    **Make Face|Bool**: se è `True` crea una faccia dalle polilinee connesse.

-    **Claim Children|PropertyBool**: se è `True` richiama gli oggetti collegati come figli nella [vista ad albero](tree_view/it.md).

-    **Relative|Bool**: se è `True` abiliterà il collegamento relativo degli oggetti secondari.

-    **Bind Mode|Enumeration**: modalità di legame, {{value|Synchronized}}, {{Value|Frozen}}, {{Value|Detached}}.

-    **Partial Load|Bool**: se è `True` abiliterà il caricamento parziale degli oggetti.

-    **Context|XLink|hidden**: oggetto contenitore di questo oggetto raccoglitore.

-    **_Version|Integer|hidden**: versione di questo tipo di oggetto.

-    **Shape|PartShape|hidden**: [Part TopoShape](Part_TopoShape.md) di questo oggetto.


</div>


{{TitleProperty|Cache}}

-    **Body|Matrix|hidden**: matrice di unità di questo oggetto.


{{TitleProperty|Offsetting}}

-    **Offset**: 2D offset to apply. If Offset = 0, then no offset is applied. If Offset \< 0, then the offset is applied inward. <small>(v0.20)</small> 

-    **Offset Join Type**: Join method of offsetting non-tangent joints. The method can be {{Value|Arcs}}, {{Value|Tangent}} or {{Value|Intersection}}. <small>(v0.20)</small> 

-    **Offset Fill|Bool**: If `True`, a face is made between the new wire and the original wire. See also the **Make Face** property. <small>(v0.20)</small> 

-    **Offset Open Result|Bool**: Affects the way open wires are processed. If `False`, an open wire is made. If `True`, a closed wire is made from a double-sided offset, with rounds around open vertices. <small>(v0.20)</small> 

-    **Offset Intersection|Bool**: Affects the way compounds are processed. If `False`, all children are processed independently. If `True`, and children are edges and wires, the children are offset in a collective manner. <small>(v0.20)</small> 

## Link

-   [New Sublink Link Feature](https://forum.freecadweb.org/viewtopic.php?t=41450), spiegazione sull\'uso con video.


<div class="mw-translate-fuzzy">





</div>


{{PartDesign_Tools_navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign SubShapeBinder/it
