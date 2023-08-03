---
 GuiCommand:
   Name: PartDesign Fillet
   Name/es: DiseñoPiezas Redondeo
   Workbenches: PartDesign Workbench/es
   MenuLocation: DiseñoPiezas , Redondeo
   SeeAlso: PartDesign_Chamfer,Part Fillet/es
---

# PartDesign Fillet/es


</div>

## Descripción


<div class="mw-translate-fuzzy">

Esta herramienta crea redondeos en las aristas seleccionadas de un objeto. Se crea una nueva entrada de Redondeo, (seguida por un número de secuencia si ya existen redondeos en el documento) en el árbol del proyecto.


</div>

## Utilización

### Add a fillet 


<div class="mw-translate-fuzzy">

-   Selecciona una o varias aristas o una cara en un objeto, y luego inicia la herramienta haciendo clic en su icono o entrando en el menú. En caso de que hayas seleccionado una cara, todos sus bordes se respetan para el fileteado.
-   En el [Panel de tareas](Task_panel/es.md) que aparece, establezca el radio de fileteado ya sea ingresando el valor, o haciendo clic en las flechas arriba/abajo.
-   Si desea agregar más aristas o caras, haga clic en el botón **Agregar** y seleccione las aristas y/o las caras.
-   Si desea eliminar aristas o caras
    -   o bien seleccione el borde/cara en la lista del diálogo y pulse la tecla **DEL**. *Nota*: Como debe haber al menos un borde para la característica, el último borde o cara restante en la lista no puede ser eliminado.
    -   o pulse el botón **Eliminar**. Todos los bordes y caras que se hayan seleccionado previamente se resaltarán en color púrpura. Seleccione el borde o la cara que desea eliminar.
-   Pulsa **OK** para validar.
-   Para una cadena de aristas tangentes entre sí, se puede seleccionar una única arista; el redondeo se propagará a lo largo de la cadena.
-   Para editar el redondeo después de que la función ha sido validada, haz doble clic en la etiqueta del redondeo en el árbol del proyecto o pulsa con el botón derecho sobre ella y selecciona **Editar Redondeo**.


</div>

### Edit a fillet 

1.  Do one of the following:
    -   Double-click the Fillet object in the [Tree view](Tree_view.md)
    -   Right-click the Fillet object in the [Tree view](Tree_view.md) and select **Edit Fillet** from the context menu.
2.  The **Fillet parameters** [task panel](Task_panel.md) opens.See [Options](#Options.md) for more information.
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
-   Set the **Radius** of the fillet.
-   Check the **Use all edges** checkbox to select all edges of the previous feature. This deactivates the selection list and the related buttons. <small>(v0.20)</small> 

## Notes

-   PartDesign Fillet should not be confused with [Part Fillet](Part_Fillet.md). Unless you know what you are doing, [Part Fillet](Part_Fillet.md) should not be used on a PartDesign Body. See [Part and PartDesign](Part_and_PartDesign.md).
-   Fillets cannot completely consume the adjacent faces.

## Properties

See also: [Property editor](Property_editor.md).

A PartDesign Fillet object is derived from a [Part Feature](Part_Feature.md) object and inherits all its properties. It also has the following additional properties:

### Data


{{Properties_Title|Base}}

-    **Base|LinkSub**: Link to the selected edges and faces of the parent feature. Can be a link to only the parent feature if **Use All Edges** is `True`.

-    **Support Transform|Bool**: If `True` the filleted shape of the additive/subtractive parent feature will be used when the fillet object is included in a [pattern](PartDesign_Workbench#Transformation_tools.md), else only the shape of the fillet itself will be used. The default is `False`.

-    **Add Sub Shape|PartShape|hidden**
    

-    **Base Feature|Link|hidden**: Link to the parent feature.

-    **_ Body|LinkHidden|hidden**: Link to the parent body.


{{Properties_Title|Fillet}}

-    **Radius|QuantityConstraint**: The fillet radius. The default is {{value|1 mm}}.

-    **Use All Edges|Bool**: If `True` all edges of the feature are filleted, and the edges specified by **Base** are ignored. The default is `False`.


{{Properties_Title|Part Design}}

-    **Refine|Bool**: If `True` redundant edges are removed from the result of the operation. The default value is determined by the **Automatically refine model after sketch-based operation** preference. See [PartDesign Preferences](PartDesign_Preferences#General.md).


<div class="mw-translate-fuzzy">

## Temas conocidos 


</div>

Fillets, chamfers, and other features that operate on solid bodies depend on the underlying [OpenCASCADE](OpenCASCADE.md) Technology (OCCT) kernel that FreeCAD uses. The OCCT kernel occasionally has difficulty handling coincident sharp edges, where two faces meet. If this is the case FreeCAD may crash without an explanation.

If run from the terminal, FreeCAD may output a log like this after a crash:


{{code|lang=text|code=
#1  0x7fff63d660ba in BRep_Tool::Curve(TopoDS_Edge const&, TopLoc_Location&, double&, double&) from /usr/lib/x86_64-linux-gnu/libTKBRep.so.7+0x2a
#2  0x7fff63d69546 in BRep_Tool::Curve(TopoDS_Edge const&, double&, double&) from /usr/lib/x86_64-linux-gnu/libTKBRep.so.7+0x46
#3  0x7fff71f4fef5 in ChFi3d_Builder::PerformIntersectionAtEnd(int) from /usr/lib/x86_64-linux-gnu/libTKFillet.so.7+0x3b05
#4  0x7fff71f58307 in ChFi3d_Builder::PerformOneCorner(int, bool) from /usr/lib/x86_64-linux-gnu/libTKFillet.so.7+0x1097
#5  0x7fff71ef6218 in ChFi3d_Builder::PerformFilletOnVertex(int) from /usr/lib/x86_64-linux-gnu/libTKFillet.so.7+0x4e8
#6  0x7fff71ef71d1 in ChFi3d_Builder::Compute() from /usr/lib/x86_64-linux-gnu/libTKFillet.so.7+0xe31
#7  0x7fff720ad7c3 in BRepFilletAPI_MakeChamfer::Build() from /usr/lib/x86_64-linux-gnu/libTKFillet.so.7+0x33
#8  0x7fff723be48e in PartDesign::Chamfer::execute() from /usr/lib/freecad-daily/lib/_PartDesign.so+0x60e
...
}}

This output references functions from OCCT libraries. If this type of crash occurs, the problem may need to be reported and solved in OCCT rather than in FreeCAD.

See the forum threads for more information:

-   [Bug Chamfer bigger than 2mm crashes freecad](https://forum.freecadweb.org/viewtopic.php?p=263818#p263818)
-   [Segfault when using part design fillet](https://forum.freecadweb.org/viewtopic.php?p=264827#p264827)

### Topological naming 


<div class="mw-translate-fuzzy">

### Denominación topológica 

Los números de los bordes no son completamente estables, por lo tanto es aconsejable que termine el trabajo de diseño principal de su cuerpo sólido antes de aplicar características como filetes y chaflanes, de lo contrario los bordes podrían cambiar de nombre y los bordes fileteados probablemente quedarían inválidos.


</div>


<div class="mw-translate-fuzzy">

Lea más en [problema de denominación topológica](topological_naming_problem/es.md).


</div>


<div class="mw-translate-fuzzy">





</div>


{{PartDesign Tools navi

}}



---
⏵ [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Fillet/es
