---
 GuiCommand:
   Name: PartDesign SubShapeBinder
   Name/de: PartDesign Teilformbinder
   Workbenches: PartDesign_Workbench/de
   MenuLocation: Part Design , Teilformbinder erstellen
   Version: 0.19
   SeeAlso: PartDesign_Clone/de
---

# PartDesign SubShapeBinder/de



## Beschreibung

Das Werkzeug **PartDesign Teilformbinder** erstellt einen Teilformbinder (Binder-Objekt), der Geometrien eines oder mehrerer übergeordneter Objekte referenziert. Ein Teilformbinder. Ein Teilformbinder wird üblicherweise in einem [PartDesign Körper](PartDesign_Body/de.md) (Body) verwendet, um auf Geometrie außerhalb des Körpers zuzugreifen.Externe Geometrie direkt in einem Körper zu verwenden, ist nicht erlaubt und wird zu \"out of scope\"-Fehlern führen. Ein Teilformbinder kann aber auch verwendet werden, ohne dass er in einem Körper eingebunden ist.

Ein Teilformbinder ermittelt die relative Positionierung der referenzierten Geometrien, was im Zusammenhang mit der Erstellung von [Baugruppen](Assembly/de.md) nützlich ist, aber darüber hinaus besitzt er auch eine eigene Positionierung.

Die referenzierte Geometrie kann aus einem oder mehreren Elementen bestehen. Jedes Element kann ein einzelnes Objekt sein (z.B. ein [PartDesign Körper](PartDesign_Body/de.md)), ein Unterobjekt (z.B. ein [Part Würfel](Part_Box/de.md) innerhalb eines [Std Teiles](Std_Part/de.md) oder eine [Skizze](PartDesign_NewSketch/de.md) oder ein [Formelement](PartDesign_Feature/de.md) innerhalb eines Körpers) oder ein Unterelement (eine Fläche, eine Kante oder ein Knotenpunkt). Welche Geometrie verwendet wird, hängt von der geplanten Verwendung des Teilformbinders ab. Für eine boolesche Operation muss ein Festkörper ausgewählt werden. Für eine Extrusion mit [Aufpolsterung](PartDesign_Pad.md) kann eine Fläche, eine Skizze oder ein ebener Draht verwendet werden. Und für eine [externe Geometrie](Sketcher_External/de.md) in einer Skizze oder um eine Skizze zu befestigen kann jede Kombination von Unterelementen geeignet sein. Die Elemente können zu unterschiedlichen übergeordneten Objekten gehören und sogar zu dem Körper, der den Teilformbinder enthält. Da ein Teilformbinder [link-basiert](Std_LinkMake.md) ist, kann die referenzierte Geometrie auch zu einem externen Dokument gehören.

<img alt="" src=images/PartDesign_SubShapeBinder_example_1.png  style="width:" height="300px;"> <img alt="" src=images/PartDesign_SubShapeBinder_example_2.png  style="width:" height="300px;"> 
*Links: zwei Festkörper, die in zwei separaten [Körpern](PartDesign_Body/de.md) erstellt wurden.<br> 
Rechts: zwei Teilformbinder, die Geometrien des ersten Körpers referenzieren, innerhalb des zweiten Körpers und an eine andere Position verschoben.*

<img alt="" src=images/PartDesign_SubShapeBinder_example_3.png  style="width:" height="300px;"> 
*Die beiden Teilfornbinder werden verwendet, um im zweiten Körper mit der [booleschen Operation](PartDesign_Boolean/de.md) Differenz einen Ausschnitt zu erstellen und mit [Aufpolsterung](PartDesign_Pad/de.md) einen Block hinzuzufügen.*



## Anwendung

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



### Mit leerem Teilformbinder starten 

1.  Follow the instructions described under [Same document](#Same_document.md) above but without selecting geometry.
2.  An empty SubShapeBinder is created.
3.  Select the required geometry. Subelements can only be selected in the [3D view](3D_view.md).
4.  In the [Tree view](Tree_view.md) drag and drop the selection onto the SubShapeBinder. If you have selected subelements their parent objects are highlighted in the [Tree view](Tree_view.md), indicating the objects to be dragged.
5.  Optionally add more geometry in the same manner.
6.  To replace already referenced geometry hold down **Ctrl** during the drag and drop operation.



## Hinweise

-   2D-Versatz wird für einige Formarten unterstützt, eingeschlossen ebene Flächen, Kanten und Kantenzüge. Da Versetzen für die Software eine schwierige Aufgabe ist, ist diese nicht immer erfolgreich.
-   Ein Teilformbinder der sich nicht innerhalb eines Körpers befindet, kann als [Basis-Formelement](PartDesign_Body/de#Basis_Formelement.md) eines neuen Körpers dienen.
-   Die {{PropertyData/de|Support}} enthält die Verknüpfungen zu den referenzierten Geometrien. Die Eigenschaft ist schreibgeschützt, kann aber durch das unter [Mit leerem Teilformbinder starten](#Mit_leerem_Teilformbinder_starten.md) beschriebenen Vorgehen geändert werden.
-   Ein aus einer Skizze erstellter Teilformbinder kann eine umgekehrte \"Werkzeugausrichtung\" besitzen. Beispielsweise kann sich ein aus einer Skizze extrudierter [Block](PartDesign_Pad/de.md) in die positive Y-Richtung ausdehnen, während sich ein aus einem Teilformbinder extrudierter [Block](PartDesign_Pad/de.md) mit den gleichen Eigenschaften in die negative Y-Richtung ausdehnt. Durch umschalten der {{PropertyData/de|Reversed}} (oder der Checkbox) kann dies angeglichen werden.



## Vergleich von PartDesign Teilformbinder und PartDesign Formbinder 

Siehe [Vergleich von PartDesign-Teilformbinder und PartDesign-Formbinder](PartDesign_ShapeBinder/de#Vergleich_von_PartDesign_Teilformbinder_und_PartDesign_Formbinder.md).



## Eigenschaften

Ein PartDesign-Teilformbinder (Binder-Objekt) ist von einem [Part-Formelement](Part_Feature/de.md) abgeleitet und erbt alle seine Eigenschaften. Außerdem hat es die folgenden zusätzlichen Eigenschaften:



### Daten


{{TitleProperty|Base}}

-    {{PropertyData/de|Support|XLinkSubList}}: Aufnahme/Träger der Geometrie.

-    {{PropertyData/de|Fuse|Bool}}: wenn auf `True` gesetzt, werden die verknüpften Festkörperformen vereinigt.

-    {{PropertyData/de|Make Face|Bool}}: wenn auf `True` gesetzt, wird eine Fläche aus den verknüpften Drähten erstellt.

-    {{PropertyData/de|Claim Children|PropertyBool}}: wenn auf `True` gesetzt, werden die verknüpften Objekte in der [Baumannsicht](Tree_view/de.md) als untergeordnete Elemente beansprucht.

-    {{PropertyData/de|Relative|Bool}}: wenn auf `True` gesetzt, ermöglicht es die relative Verknüpfung von Unterobjekten.

-    {{PropertyData/de|Bind Mode|Enumeration}}: Bindungsmodus, {{value|Synchronized}}, {{Value|Frozen}}, {{Value|Detached}}.

-    {{PropertyData/de|Partial Load|Bool}}: wenn auf `True` gesetzt, ermöglicht es Objekte teilweise zu Laden.

-    {{PropertyData/de|Context|XLink|hidden}}: Containerobjekt dieses Binderobjekts.

-    {{PropertyData/de|Bind Copy On Change|Enumeration}}
    

-    {{PropertyData/de|Refine|Bool}}: wenn auf `True` gesetzt, werden überzählige Kanten entfernt (z.B. nach einer booleschen Operation).

-    {{PropertyData/de|_ Version|Integer|hidden}}: Version dieses Objekttyps.

-    {{PropertyData/de|_ Copied Link|XLinkSub|hidden}}.


{{TitleProperty|Cache}}

-    {{PropertyData/de|Cache_*|Matrix|hidden}}: Einheitsmatrix (eine separate Eigenschaft für jedes Objekt in {{PropertyData/de|Support}}).


{{TitleProperty|Offsetting}}

-    **Offset**: 2D offset to apply. If Offset = 0, then no offset is applied. If Offset \< 0, then the offset is applied inward.

-    **Offset Join Type**: Join method of offsetting non-tangent joints. The method can be {{Value|Arcs}}, {{Value|Tangent}} or {{Value|Intersection}}.

-    **Offset Fill|Bool**: If `True`, a face is made between the new wire and the original wire. See also the **Make Face** property.

-    **Offset Open Result|Bool**: Affects the way open wires are processed. If `False`, an open wire is made. If `True`, a closed wire is made from a double-sided offset, with rounds around open vertices.

-    **Offset Intersection|Bool**: Affects the way compounds are processed. If `False`, all children are processed independently. If `True`, and children are edges and wires, the children are offset in a collective manner.

### View


{{TitleProperty|Base}}

-    **Use Binder Style|Bool**: If `True` the colors of the binder object depend on the [fine-tuning](Fine-tuning#PartDesign_Workbench.md) parameter **DefaultDatumColor**. If `False`, normal shape colors are applied.



## Verweise

-   [New Sublink Link Feature](https://forum.freecadweb.org/viewtopic.php?t=41450), Gebrauchserklärung mit Video.



---
⏵ [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign SubShapeBinder/de
