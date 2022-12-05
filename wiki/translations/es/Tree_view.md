# Tree view/es
{{TOCright}}

## Introducción

La [vista árbol](Tree_view/es.md) aparece en la pestaña **Modelo** de la [vista combo](Combo_view/es.md), uno de los paneles más importantes de la [interfaz](Interface/es.md); muestra todos los objetos definidos por el usuario que forman parte de un documento de FreeCAD. La vista árbol es una representación de la [estructura del documento](document_structure/es.md), e indica qué información se guarda en el disco.

Estos objetos no tienen que ser necesariamente formas geométricas visibles en la [Vista 3D](3D_view/es.md), sino que también pueden ser objetos de datos de apoyo creados con cualquiera de los [Ambientes de trabajo](Workbenches/es.md).

![](images/FreeCAD_Tree_view.png )



*La vista de árbol que muestra varios elementos del documento.*

## Trabajando con el vista arbol 

By default, whenever a new object is created, it is added to the end of the list in the tree view. The tree view allows managing the objects to keep them organized; it permits creating [groups](Std_Group.md), moving objects inside groups, moving groups inside other groups, renaming objects, copying objects, deleting objects, and other operations in the context menu (right click) which depend on the currently selected object and the currently active workbench.

Many operations create objects that are dependent on a previously existing object. In this case, the tree view shows this relationship by absorbing the older object inside the new object. Expanding and collapsing the objects in the tree view shows the parametric history of that object. Objects that are deeper inside others are older, while objects that are outside are newer, and are derived from the older objects. By modifying the interior objects, the parametric operations propagate all the way to the top, generating a new result.

<img alt="" src=images/FreeCAD_Tree_view_parametric_history_1.png  style="width:" height="304px;"> <img alt="" src=images/FreeCAD_Tree_view_parametric_history_2.png  style="width:" height="304px;">

<img alt="" src=images/FreeCAD_Tree_view_parametric_history_3.png  style="width:" height="304px;">



*The topmost object is created by doing parametric operations on objects which themselves were created by previous operations. Expanding the tree many levels reveals the original elements that were used to create the partial solids.*

## Acciones

Since the tree view lists objects that may be visible in the [3D view](3D_view.md), many of the actions are the same as those that can be executed from the [3D view](3D_view.md).

When the application starts, the default [Start Workbench](Start_Workbench.md) is active, and no document has been created, right clicking on the [tree view](Tree_view.md) shows one sub-menu with four commands:

-    **Expression actions**:

    -   [Copy selected](Std_Expressions.md)
    -   [Copy active document](Std_Expressions.md)
    -   [Copy all documents](Std_Expressions.md)
    -   [Paste](Std_Paste.md)

These allow working with various documents, but are disabled if no document is present.

Once a new document has been created the following become active:

-    **Expression actions**:

    -   [Copy active document](Std_Expressions.md)
    -   [Copy all documents](Std_Expressions.md)

In addition, [Link](Std_LinkMake.md) actions are available.

-    **Link actions**:

    -   
        **Make Link group**
        
        :

        -   [Simple group](Std_LinkMakeGroup.md)
        -   [Group with links](Std_LinkMakeGroup.md)
        -   [Group with transform links](Std_LinkMakeGroup.md)

    -   [Make Link](Std_LinkMake.md)

### Seleccionar el documento 

If you select the active document and right click, in addition to **Expression actions** and **Link actions**, the following commands appear:

-    **Show hidden items**: if active, the tree view will show hidden items.

-    **Search**: shows an input field to search objects inside the selected document.

-    **Close document**: closes the selected document.

-    **Skip recomputes**: if active, the document\'s objects will not [recompute](Std_Refresh.md) automatically.

    -   
        **Allow partial recomputes**
        
        : if active, the document will allow [recompute](Std_Refresh.md) of only some objects.

-    **Mark to recompute**: marks all objects of the document as touched, and ready for [recompute](Std_Refresh.md).

-    **[Create group](Std_Group.md)**: creates a [group](Std_Group.md) in the selected document.

### Seleccionar de objetos 

Once objects are added to the document right clicking them will show additional commands. These depend on the number of selected objects, their type and also on the active workbench. In most cases and with most workbenches (except the [Start Workbench](Start_Workbench.md)) the following commands are then available:

-    **[Appearance](Std_SetAppearance.md)**: launches a dialog to change the visual properties of the whole object.

-    **[Random color](Std_RandomColor.md)**: assigns a random color to the object.

-    **[Cut](Std_Cut.md)**: disabled.

-    **[Copy](Std_Copy.md)**: copies an object into memory.

-    **[Paste](Std_Paste.md)**: pastes the copied object into the document; the copy is added to the end of the tree view.

-    **[Delete](Std_Delete.md)**: removes the object from the document.

-    **Hide item**: if active, the selected object will be set as hidden.

-    **Add dependent objects to selection**: all dependent objects will be added to the selection. This way one can see the dependencies and e.g. delete all dependent objects at once. This option is only available if one of the selected objects has links. <small>(v0.20)</small> 

-    **Mark to recompute**: marks the selected object as touched, and ready for [recompute](Std_Refresh.md).

-    **Recompute object**: recomputes the selected object.

-    **Rename**: starts editing the label of the selected object, not the name which is read-only. This option is only available if a single object is selected.

As an example of context menu extension, if a [Part Box](Part_Box.md) is right clicked while the [Part Workbench](Part_Workbench.md) is active the following additional commands are available:

-    **[Edit](Std_Edit.md)**: activates the edit mode of the object.

-    **[Transform](Std_TransformManip.md)**: launches the transform widget to move or rotate the object.

-    **[Attachment editor](Part_EditAttachment.md)**: launches a dialog to attach the object to one or more other objects.

-    **[Set colors](Part_FaceColors.md)**: sets the color of selected faces of the object.

-    **[Toggle visibility](Std_ToggleVisibility.md)**: makes the object visible or invisible in the [3D view](3D_view.md).

-    **[Show selection](Std_ShowSelection.md)**: makes the selected object visible.

-    **[Hide selection](Std_HideSelection.md)**: makes the selected object invisible.

-    **[Toggle selectability](Std_ToggleSelectability.md)**: toggles the selectability of the object in the [3D view](3D_view.md).

-    **[Select all instances](Std_TreeSelectAllInstances.md)**: selects all instances of this object in the tree view.

-    **[Send to Python Console](Std_SendToPythonConsole.md)**: creates a variable in the [Python console](Python_console.md) referencing the object

### Keyboard actions 

The following keyboard actions are available when the focus is on the Tree view:

-    **Ctrl**\+**F**: opens a search box at the bottom of the tree, allowing to search and reach objects using their names or labels.

-   Expand and collapse actions using **Alt**+**Arrow** combinations: <small>(v0.20)</small> 
    -   
        **Alt**
        
        \+**Left**: collapses selected item(s).

    -   
        **Alt**
        
        \+**Right**: expands selected item(s).

    -   
        **Alt**
        
        \+**Up**: expands selected item(s) with all their tier-1 children collapsed (deeper children remain unchanged).

    -   
        **Alt**
        
        \+**Down**: expands selected item(s) with all their tier-1 children expanded as well (deeper children remain unchanged).

## Iconos superpuestos 

Se pueden mostrar uno o varios iconos superpuestos más pequeños sobre el icono por defecto de un objeto en la vista de árbol. Los iconos superpuestos disponibles y su significado se enumeran a continuación. {{Version/es|0.19}}

### ![](images/FreeCAD_Tree_view_recompute.png ) Marca de verificación blanca sobre fondo azul 

Esto indica que el objeto tiene que ser [recalculado](Std_Refresh/es.md), debido a los cambios realizados en el modelo o porque el usuario marcó el objeto en el menú contextual de la vista de árbol para ser recalculado. En la mayoría de los casos los recálculos se activan automáticamente, pero a veces se retrasan por razones de rendimiento.

### ![](images/FreeCAD_Tree_view_tip.png ) Flecha blanca sobre fondo verde 

Indica la llamada [Punta](PartDesign_Body/es#punta.md) de un cuerpo. Suele ser la última característica de un [DiseñoPieza Cuerpo](PartDesign_Body/es.md) y representa todo el cuerpo para el mundo exterior al cuerpo, por ejemplo, cuando el cuerpo se exporta o se utiliza en operaciones [Pieza booleano](Part_Boolean/es.md). La punta puede ser cambiada por el usuario.

### ![](images/FreeCAD_Tree_view_unattached.png ) Cadena de eslabones púrpura sobre fondo blanco 

Se muestra normalmente para [bocetos](Sketch/es.md), primitivas geométricas, como caja, cilindro, etc. y geometría [Referencia](Datum/es.md). Indica que el objeto no está unido a nada. No tiene desplazamiento de fijación y obtiene su posición y alineación únicamente de su propiedad [Colocación](Placement/es.md).

Hay un [Tutorial Básico de Adjuntos](Basic_Attachment_Tutorial/es.md) que explica cómo manejar tales objetos.

### ![](images/FreeCAD_Tree_view_notfullyconstrained.png ) Amarillo X 

Esto sólo se utiliza para [bocetos](Sketch/es.md) e indica que el sketch no está completamente restringido. Dentro de [Croquizador](Sketcher_Workbench/es.md) el número de grados de libertad restantes se muestra en los mensajes del solucionador.

### ![](images/FreeCAD_Tree_view_error.png ) Signo de exclamación blanco sobre fondo rojo 

Esto indica que el objeto tiene un error que debe ser corregido. Después de volver a calcular todo el documento, se muestra un punto herramienta que describe el error cuando se pasa el ratón por encima del objeto en la vista de árbol. Nota: Todos los demás objetos que dependan de un objeto en ese estado de error no se volverán a calcular correctamente, por lo que pueden seguir mostrando algún estado antiguo.


{{Interface navi

}} {{Std Base navi}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Tree view/es
