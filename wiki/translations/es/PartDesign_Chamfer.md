---
- GuiCommand:
   Name: PartDesign Chamfer
   Name/es: DiseñoPieza Chaflán
   Workbenches: PartDesign Workbench/es
   MenuLocation: DiseñoPieza -> Chaflán
   SeeAlso: PartDesign_Fillet/es, Part Chamfer/es
---

# PartDesign Chamfer/es


</div>



## Descripción


<div class="mw-translate-fuzzy">

Esta herramienta crea chaflanes en los bordes seleccionados de un objeto. Se crea una nueva entrada separada de chaflanes (seguida de un número consecutivo si ya existen chaflanes en el documento) en el árbol del proyecto.


</div>



## Utilización

### Add a chamfer 

1.  Optionally [activate](PartDesign_Body#Active_status.md) the Body to chamfer.
2.  There are several ways to select edges to chamfer:
    -   Select one or more edges of the Body individually.
    -   Select one or more faces of the Body to select all their edges.
    -   Select a feature (usually the last feature) of the Body to select all its edges. <small>(v0.20)</small> 
3.  For a chain of tangentially connected edges only a single edge needs to be selected, the chamfer will propagate along the chain.
4.  There are several ways to invoke the tool:
    -   Press the **<img src="images/PartDesign_Chamfer.svg" width=16px> [Chamfer](PartDesign_Chamfer.md)** button.
    -   Select the **Part Design → Apply a dress-up feature → <img src="images/PartDesign_Chamfer.svg" width=16px> Chamfer** option from the menu.
5.  If there is no active Body, and there are two or more Bodies in the document, the **Active Body Required** dialog will open and prompt you to activate one. If there is a single Body it will be activated automatically.
6.  The **Chamfer parameters** [task panel](Task_panel.md) opens. See [Options](#Options.md) for more information.
7.  Press the **OK** button to finish.

### Edit a chamfer 

1.  Do one of the following:
    -   Double-click the Chamfer object in the [Tree view](Tree_view.md)
    -   Right-click the Chamfer object in the [Tree view](Tree_view.md) and select **Edit Chamfer** from the context menu.
2.  The **Chamfer parameters** [task panel](Task_panel.md) opens. See [Options](#Options.md) for more information.
3.  Press the **OK** button to finish.

## Options

-   To add edges do one of the following:
    -   Press the **Add** button to start selecting edges and/or faces in the [3D view](3D_view.md).
    -   To select all remaining edges do the following:
        1.  If required press the **Add** button.
        2.  Use the **Ctrl**+**Shift**+**A** keyboard shortcut, or right-click the list and select **Add all edges** from the context menu. <small>(v0.20)</small> 
-   To remove edges do one of the following:
    -   Press the **Remove** button to start deselecting edges and/or faces in the [3D view](3D_view.md). Selected elements are highlighted in purple.
    -   Select one or more elements in the list and press the **Del** key, or right-click the list and select **Remove** from the context menu.
-   Specify a chamfer **Type**:
    -   
        **Equal distance**
        
        : One distance is used to place both chamfer edges.

    -   
        **Two distances**
        
        : Two distances are used to place the chamfer edges.

    -   
        **Distance and angle**
        
        : A distance is used to place one chamfer edge, the placement of the other chamfer edge is defined by the angle of the chamfer.
-   Press the **<img src="images/PartDesign_Flip_Direction.svg" width=16px> Flip direction** button to flip the direction of the chamfer (deactivated for **Equal distance**).
-   Set the **Size** of the chamfer.
-   Set the **Size2** of the chamfer (only available if **Two distances** is selected).
-   Set the **Angle** of the chamfer (only available if **Distance and angle** is selected).
-   Check the **Use all edges** checkbox to select all edges of the previous feature. This deactivates the selection list and the related buttons. <small>(v0.20)</small> 

## Notes


<div class="mw-translate-fuzzy">

## DiseñoPieza Chaflán VS. Pieza Chaflán 

\"El DiseñoPiezas chaflán no debe confundirse con su [Ambiente de trabajo piezas contraparte](Part_Chamfer/de.md)\". Aunque comparten el mismo icono, no son lo mismo, y no se usan de la misma manera. La principal diferencia es que DiseñoPiezas Chaflán crea una entrada de chaflán separada (seguida de un número secuencial si ya existen chaflanes) en el árbol de proyecto para el cuerpo actual. El Piezas chaflán se convierte en el padre del objeto al que se aplicó.


</div>

## Properties

See also: [Property editor](Property_editor.md).

A PartDesign Chamfer object is derived from a [Part Feature](Part_Feature.md) object and inherits all its properties. It also has the following additional properties:

### Data


{{Properties_Title|Base}}

-    **Base|LinkSub**: Link to the selected edges and faces of the parent feature. Can be a link to only the parent feature if **Use All Edges** is `True`.

-    **Support Transform|Bool**: If `True` the chamfered shape of the additive/subtractive parent feature will be used when the chamfer object is included in a [pattern](PartDesign_Workbench#Transformation_tools.md), else only the shape of the chamfer itself will be used. The default is `False`.

-    **Add Sub Shape|PartShape|hidden**
    

-    **Base Feature|Link|hidden**: Link to the parent feature.

-    **_ Body|LinkHidden|hidden**: Link to the parent body.


{{Properties_Title|Chamfer}}

-    **Chamfer Type|Enumeration**: The chamfer type: {{value|Equal distance}} (default), {{value|Two distances}} or {{value|Distance and Angle}}.

-    **Size|QuantityConstraint**: The first chamfer distance. The default is {{value|1 mm}}.

-    **Size2|QuantityConstraint**: The second chamfer distance. Only used if **Chamfer Type** is {{Value|Two distances}}. The default is {{value|1 mm}}.

-    **Angle|Angle**: The chamfer angle. Only used if **Chamfer Type** is {{Value|Distance and Angle}}. The default is {{value|45 °}}.

-    **Flip Direction|Bool**: If `True` the direction of the chamfer is flipped. Not used if **Chamfer Type** is {{Value|Equal distance}}. The default is `False`.

-    **Use All Edges|Bool**: If `True` all edges of the feature are chamfered, and the edges specified by **Base** are ignored. The default is `False`.


{{Properties_Title|Part Design}}

-    **Refine|Bool**: If `True` redundant edges are removed from the result of the operation. The default value is determined by the **Automatically refine model after sketch-based operation** preference. See [PartDesign Preferences](PartDesign_Preferences#General.md).

## Known issues 

See [PartDesign Fillet](PartDesign_Fillet#Known_issues.md).


<div class="mw-translate-fuzzy">





</div>


{{PartDesign Tools navi

}}



---
⏵ [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Chamfer/es
