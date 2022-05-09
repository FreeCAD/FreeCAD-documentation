---
- GuiCommand   */de
   Name   *PartDesign SubShapeBinder
   Name/de   *PartDesign UnterFormBinder
   Workbenches   *[PartDesign Arbeitsbereich](PartDesign_Workbench/de.md)
   MenuLocation   *Part Design → Erstellen eines Unterobjekt-Formbinders
   Version   *0.19
   SeeAlso   *[PartDesign FormBinder](PartDesign_ShapeBinder/de.md), [PartDesign Klon](PartDesign_Clone/de.md)
---

# PartDesign SubShapeBinder/de


</div>

## Beschreibung


<div class="mw-translate-fuzzy">

Ein [PartDesign UnterFormBinder](PartDesign_SubShapeBinder/de.md) importiert ein Element aus einem anderen Körper in den aktiven [Körper](PartDesign_Body/de.md). Es kann die [Form](Shape/de.md) eines anderen Objekts übernehmen oder an ein oder mehrere Objekte oder Unterelemente (Kanten oder Flächen) eines anderen Objekts \"gebunden\" werden.


</div>


<div class="mw-translate-fuzzy">

Es kann auch an Objekte binden, die innerhalb von [Std Parts](Std_Part/de.md) verschachtelt sind, und es verfolgt die relative Platzierung dieser Merkmale. Dies ist im Zusammenhang mit der Erstellung von [Baugruppen](Assembly/de.md) nützlich, da der Anwender oft auf [Formelemente](PartDesign_Feature/de.md) verweisen muss, die bereits korrekt in einer anderen Unterbaugruppe platziert sind.


</div>

The referenced geometry can consist of one or multiple elements. Each element can be an individual object (for example a [PartDesign Body](PartDesign_Body.md)), a subobject (for example a [Part Box](Part_Box.md) inside a [Std Part](Std_Part.md), or a [sketch](PartDesign_NewSketch.md) or [Feature](PartDesign_Feature.md) inside a Body), or a subelement (a face, edge or vertex). Which geometry should be selected depends on the intended purpose of the SubShapeBinder. For a Boolean operation you would need to select a solid. For a [Pad operation](PartDesign_Pad.md) a face, a sketch or a planar wire can be used. And for the [external geometry](Sketcher_External.md) in a sketch, or to attach a sketch, any combination of subelements may be appropriate. Elements can belong to different parent objects, and can even belong to the Body the SubShapeBinder is nested in. Because a SubShapeBinder is [Link-based](Std_LinkMake.md) the referenced geometry can also belong to an external document.

<img alt="" src=images/PartDesign_SubShapeBinder_example_1.png  style="width   *" height="300px;"> <img alt="" src=images/PartDesign_SubShapeBinder_example_2.png  style="width   *" height="300px;">


<div class="mw-translate-fuzzy">



*Links   * zwei Körper, die in zwei separaten [Körpern](PartDesign_Body/de.md) erzeugt wurden. Rechts   * zwei UnterFormBinder, die aus dem ersten Körper extrahiert, in den zweiten Körper importiert und an eine andere Position verschoben wurden.*


</div>

<img alt="" src=images/PartDesign_SubShapeBinder_example_3.png  style="width   *" height="300px;">


<div class="mw-translate-fuzzy">



*Die beiden UnterFormBinder werden verwendet, um einen [booleschen Schnitt](PartDesign_Boolean/de.md) und ein [Polster](PartDesign_Pad/de.md), mit dem zweiten Körper, zu erstellen.*


</div>

## Anwendung

### Same document 

1.  If there are multiple Bodies in the document   * optionally [activate the Body](PartDesign_Body#Active_status.md) the SubShapeBinder should be nested in.
2.  Select the required geometry. Subelements can only be selected in the [3D view](3D_view.md).
3.  There are several ways to invoke the tool   *
    -   Press the **<img src="images/PartDesign_SubShapeBinder.svg" width=16px> [PartDesign SubShapeBinder](PartDesign_SubShapeBinder.md)** button.
    -   Select the **Part Design → <img src="images/PartDesign_SubShapeBinder.svg" width=16px> Create a sub-object(s) shape binder** option from the menu.
4.  The SubShapeBinder is created.
5.  If there is only one Body in the document the SubShapeBinder is automatically added to it and the Body is activated. If this is the case and the SubShapeBinder should not be nested, it can be dragged out of the Body and dropped onto the <img alt="" src=images/Document.svg  style="width   *16px;"> document node in the [Tree view](Tree_view.md).

### External document 

1.  If required open the source document (the external document) and the target document. Both documents must have been saved at least once.
2.  If there are multiple Bodies in the target document   * optionally activate the Body the SubShapeBinder should be nested in.
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

The main differences are   *

-   Editing a PartDesign ShapeBinder is easier. Double-clicking the object in the [Tree view](Tree_view.md) will open a task panel.
-   A PartDesign ShapeBinder can either reference a single whole object, or subelements belong to a single parent object. A PartDesign SubShapeBinder does not have these restrictions.
-   Only PartDesign SubShapeBinders can reference geometry from an external file.
-   A PartDesign SubShapeBinder always tracks the relative placement of the referenced geometry. For a PartDesign ShapeBinder this behavior is optional through its **Trace Support** property.
-   Only PartDesign SubShapeBinders support 2D offsetting.

## Eigenschaften


<div class="mw-translate-fuzzy">

Der [UnterFormBinder](PartDesign_SubShapeBinder/de.md) ist abgeleitet von [Part Formelement](Part_Feature/de.md) (`Part   *   *Feature` Klasse). Zusätzlich zu den in [Part Formelement](Part_Feature/de.md) aufgelisteten Eigenschaften sind die folgenden Eigenschaften im [Eigenschaftseditor](property_editor/de.md) verfügbar.


</div>

### Daten


{{TitleProperty|Base}}


<div class="mw-translate-fuzzy">

-    **Unterstützung|XVerknüpfungUnterListe|ausgeblendet**   * Unterstützung für die Geometrie.

-    **Verschmelzen|Bool**   * wenn es `True` ist, werden die verknüpften Volumenkörperformen verschmolzen.

-    **Flächen erstellen|Bool**   * Wenn der Wert `True` ist, wird eine Fläche für die verknüpften Drahtobjekte erstellt.

-    **Kindobjekte beanspruchen|EigenschaftBool**   * Wenn der Wert `True` ist, werden die verknüpften Objekte in der [Baumansicht](Tree_view/de.md) als Kindobjekte beansprucht.

-    **Relativ|Bool**   * wenn es`True` ist, ermöglicht es die relative Verknüpfung von Unterobjekten.

-    **Bindungsmodus|Aufzählung**   * Bindungsmodus, {{value|Synchronisiert}}, {{value|Eingefroren}}, {{value|Abgehängt}}.

-    **Teilweise laden|Bool**}   * wenn es `True` ist, ermöglicht es Objekte teilweise zu Laden.

-    **Kontext|XVerknüpfung|ausgeblendet**   * Containerobjekt dieses Binderobjekts.

-    **_Version|Integer|ausgeblendet**   * Version dieses Objekttyps.

-    **Form|PartForm|ausgeblendet**   * [Part TopoForm](Part_TopoShape/de.md) dieses Objekttyps.


</div>


{{TitleProperty|Cache}}

-    {{PropertyData/de|Körper|Matrix|ausgeblendet}}   * Einheitenmatrix dieses Objekts.


{{TitleProperty|Offsetting}}

-    **Offset**   * 2D offset to apply. If Offset = 0, then no offset is applied. If Offset \< 0, then the offset is applied inward. <small>(v0.20)</small> 

-    **Offset Join Type**   * Join method of offsetting non-tangent joints. The method can be {{Value|Arcs}}, {{Value|Tangent}} or {{Value|Intersection}}. <small>(v0.20)</small> 

-    **Offset Fill|Bool**   * If `True`, a face is made between the new wire and the original wire. See also the **Make Face** property. <small>(v0.20)</small> 

-    **Offset Open Result|Bool**   * Affects the way open wires are processed. If `False`, an open wire is made. If `True`, a closed wire is made from a double-sided offset, with rounds around open vertices. <small>(v0.20)</small> 

-    **Offset Intersection|Bool**   * Affects the way compounds are processed. If `False`, all children are processed independently. If `True`, and children are edges and wires, the children are offset in a collective manner. <small>(v0.20)</small> 

## Verweise

-   [New Sublink Link Feature](https   *//forum.freecadweb.org/viewtopic.php?t=41450), Gebrauchserklärung mit Video.


<div class="mw-translate-fuzzy">





</div>


{{PartDesign_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign SubShapeBinder/de
