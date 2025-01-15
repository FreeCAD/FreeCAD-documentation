# Tree view/es
## Introducción


<div class="mw-translate-fuzzy">

La [vista de árbol](Tree_view/es.md) aparece en la pestaña **Modelo** de la [vista combo](Combo_view/es.md), uno de los paneles más importantes de la [interfaz](Interface/es.md); muestra todos los objetos definidos por el usuario que forman parte de un documento de FreeCAD. La vista de árbol es una representación de la [estructura del documento](document_structure/es.md), e indica qué información se guarda en el disco.


</div>

Estos objetos no tienen que ser necesariamente formas geométricas visibles en la [Vista 3D](3D_view/es.md), sino que también pueden ser objetos de datos de apoyo creados con cualquiera de los [Ambientes de trabajo](Workbenches/es.md).

![](images/FreeCAD_Tree_view.png )



*La vista de árbol que muestra varios elementos del documento.*



## Trabajando con la vista de árbol 

By default, whenever a new object is created, it is added to the end of the list in the Tree view. The Tree view allows managing the objects to keep them organized; it permits creating [groups](Std_Group.md), moving objects inside groups, moving groups inside other groups, relabeling objects, copying objects, deleting objects, and using options from its [context menu](#Context_menu.md).

Many operations create objects that are dependent on a previously existing object. In this case, the Tree view shows this relationship by absorbing the older object inside the new object. Expanding and collapsing the objects in the Tree view shows the parametric history of that object. Objects that are deeper inside others are older, while objects that are outside are newer, and are derived from the older objects. By modifying the interior objects, the parametric operations propagate all the way to the top, generating a new result.

<img alt="" src=images/FreeCAD_Tree_view_parametric_history.png  style="width:" height="300px;">



*The topmost object is created by doing parametric operations on objects which themselves were created by previous operations.<br>
Fully expanding the tree reveals the original elements that were used to create the partial solids.*

### Tree view columns 

The Tree view always displays a column with the icons and labels of objects. Two additional columns can optionally be displayed as well. To enable these columns right-click the Tree view and in the context menu select **Tree settings** and then **Show description** (<small>(v0.21)</small> ) and/or **Show internal name** (<small>(v1.0)</small> ). Column headings are added if more than one column is displayed. Note that the internal names of objects cannot be changed.

### Edit object label 

Select an object in the first column and press **F2** (on Windows and Linux), or **Enter** (on macOS), to edit its **Label** property. This property can also be edited via the context menu option **Rename** or in the [Property editor](Property_editor.md).

### Edit object description 

An object can optionally have a description. This information is stored in its **Label2** property. If the description column is displayed you can edit this property by selecting an object in that column and pressing **F2** (on Windows and Linux), or **Enter** (on macOS). The property can also be changed in the [Property editor](Property_editor.md).

### Context menu 

The options in the context menu of the Tree view depend on the selected object(s) and the currently active workbench. To display this menu right-click the background of the list, right-click an object in the list, or select multiple objects in the list and then right-click one of them.

### Keyboard modifiers 

The usual keyboard modifiers can be used in the Tree view. The modifiers can be combined as well.

-    **Ctrl**: hold down this key to select multiple objects.

-    **Shift**: hold down this key to select all objects between a previously selected object and the next selected object.

### Keyboard shortcuts 

The following keyboard shortcuts are available when the focus is on the Tree view:

-    **Ctrl**\+**F**: opens a search box at the bottom of the tree, allowing to search and reach objects using their internal names or labels.

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


<div class="mw-translate-fuzzy">

Se pueden mostrar uno o varios iconos superpuestos más pequeños sobre el icono por defecto de un objeto en la vista de árbol. Los iconos superpuestos disponibles y su significado se enumeran a continuación. {{Version/es|0.19}}


</div>



### ![](images/FreeCAD_Tree_view_recompute.png ) Marca de verificación blanca sobre fondo azul 

Esto indica que el objeto tiene que ser [recalculado](Std_Refresh/es.md), debido a los cambios realizados en el modelo o porque el usuario marcó el objeto en el menú contextual de la vista de árbol para ser recalculado. En la mayoría de los casos los recálculos se activan automáticamente, pero a veces se retrasan por razones de rendimiento.



### ![](images/FreeCAD_Tree_view_error.png ) Signo de exclamación blanco sobre fondo rojo 

Esto indica que el objeto tiene un error que debe ser corregido. Después de volver a calcular todo el documento, se muestra un punto herramienta que describe el error cuando se pasa el ratón por encima del objeto en la vista de árbol. Nota: Todos los demás objetos que dependan de un objeto en ese estado de error no se volverán a calcular correctamente, por lo que pueden seguir mostrando algún estado antiguo.




<div class="mw-translate-fuzzy">

### ![](images/FreeCAD_Tree_view_unattached.png ) Cadena de eslabones púrpura sobre fondo blanco 


</div>


<div class="mw-translate-fuzzy">

Se muestra normalmente para [bocetos](Sketch/es.md), primitivas geométricas, como caja, cilindro, etc. y geometría [Referencia](Datum/es.md). Indica que el objeto no está unido a nada. No tiene desplazamiento de fijación y obtiene su posición y alineación únicamente de su propiedad [Colocación](Placement/es.md).


</div>

Hay un [Tutorial Básico de Adjuntos](Basic_Attachment_Tutorial/es.md) que explica cómo manejar tales objetos.



### ![](images/FreeCAD_Tree_view_notfullyconstrained.png ) Amarillo X 


<div class="mw-translate-fuzzy">

Esto sólo se utiliza para [bocetos](Sketch/es.md) e indica que el sketch no está completamente restringido. Dentro de [Croquizador](Sketcher_Workbench/es.md) el número de grados de libertad restantes se muestra en los mensajes del solucionador.


</div>



### ![](images/FreeCAD_Tree_view_tip.png ) Flecha blanca sobre fondo verde 

Indica la llamada [Punta](PartDesign_Body/es#punta.md) de un cuerpo. Suele ser la última característica de un [DiseñoPieza Cuerpo](PartDesign_Body/es.md) y representa todo el cuerpo para el mundo exterior al cuerpo, por ejemplo, cuando el cuerpo se exporta o se utiliza en operaciones [Pieza booleano](Part_Boolean/es.md). La punta puede ser cambiada por el usuario.

### ![](images/FreeCAD_Tree_view_suppressed.png ) Red backslash 


<small>(v1.0)</small> 

This indicates a suppressed [PartDesign](PartDesign_Workbench.md) feature.

### ![](images/FreeCAD_Tree_view_link.png ) White upwards curved arrow 

This indicates a [linked](Std_LinkMake.md) object.

### ![](images/FreeCAD_Tree_view_link_external.png ) Two white upwards curved arrows 

This indicates a [linked](Std_LinkMake.md) object loaded from an external document.

### ![](images/FreeCAD_Tree_view_hidden.png ) Eye symbol 

This indicates that the object will be hidden in the Tree view if the **Show items hidden in Tree view** context menu option is unchecked.

### ![](images/FreeCAD_Tree_view_frozen.png ) Cyan ice crystal 


<small>(v1.0)</small> 

This indicates a [frozen](Std_ToggleFreeze.md) object that is not recomputed when its parents change.

## Preferences

See [Combo view](Combo_view#Preferences.md).



---
⏵ [documentation index](../README.md) > Tree view/es
