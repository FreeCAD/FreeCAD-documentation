# Std Base/es
<div class="mw-translate-fuzzy">





</div>

<img alt="Std Base icono" src=images/Freecad.svg  style="width:128px;">






## Introducción

**Std Base** no es realmente un Ambiente de trabajo, sino más bien una categoría de comandos y herramientas \'estándar\' que pueden ser utilizados en todos los Ambiente de trabajo.



## Herramientas


<div class="mw-translate-fuzzy">

Se puede acceder a la mayoría de las herramientas de **Std Base** desde el [menú estándar](Standard_Menu/es.md). Las que sólo están disponibles a través de una barra de herramientas o de un menú contextual están listadas en [Herramientas adicionales](#Herramientas_adicionales.md).


</div>




<div class="mw-translate-fuzzy">

### Herramientas de menú estándar 


</div>

El menú estándar se compone de 7 submenús. Cada submenú tiene una página dedicada. Basta con hacer clic en cualquiera de los nombres que aparecen a continuación.


{{StdMenu
|
[Archivo](Std_File_Menu/es.md)
&nbsp;&nbsp;&nbsp;
[Editar](Std_Edit_Menu/es.md)
&nbsp;&nbsp;&nbsp;
[Ver](Std_View_Menu/es.md)
&nbsp;&nbsp;&nbsp;
[Herramientas](Std_Tools_Menu/es.md)
&nbsp;&nbsp;&nbsp;
[Macro](Std_Macro_Menu/es.md)
&nbsp;&nbsp;&nbsp;
[Ventanas](Std_Windows_Menu/es.md)
&nbsp;&nbsp;&nbsp;
[Ayuda](Std_Help_Menu/es.md)
}}

### Structure toolbar 

-   <img alt="" src=images/Std_Part.svg  style="width:32px;"> [Create part](Std_Part.md): Creates a new part and makes it active.

-   <img alt="" src=images/Part_CoordinateSystem.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Create datums: 

  - <img alt="" src=images/Part_CoordinateSystem.svg  style="width:32px;"> [Create coordinate system](Part_CoordinateSystem.md): Creates a coordinate system object that can be attached to other objects. <small>(v1.1)</small> 

  - <img alt="" src=images/Part_DatumPlane.svg  style="width:32px;"> [Create datum plane](Part_DatumPlane.md): Creates a datum plane object that can be attached to other objects. <small>(v1.1)</small> 

  - <img alt="" src=images/Part_DatumLine.svg  style="width:32px;"> [Create datum line](Part_DatumLine.md): Creates a datum line object that can be attached to other objects. <small>(v1.1)</small> 

  - <img alt="" src=images/Part_DatumPoint.svg  style="width:32px;"> [Create datum point](Part_DatumPoint.md): Creates a datum point object that can be attached to other objects. <small>(v1.1)</small> 

-   <img alt="" src=images/Std_Group.svg  style="width:32px;"> [Create group](Std_Group.md): Creates a new group.

-   <img alt="" src=images/Std_LinkMake.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Link tools:

  - <img alt="" src=images/Std_LinkMake.svg  style="width:32px;"> [Make link](Std_LinkMake.md): Creates a link.

  - <img alt="" src=images/Std_LinkMakeRelative.svg  style="width:32px;"> [Make sub-link](Std_LinkMakeRelative.md): Creates a sub-object or sub-element link.

  - <img alt="" src=images/Std_LinkReplace.svg  style="width:32px;"> [Replace with link](Std_LinkReplace.md): Replaces object(s) with new link(s).

  - <img alt="" src=images/Std_LinkUnlink.svg  style="width:32px;"> [Unlink](Std_LinkUnlink.md): Replaces link(s) with their linked object(s).

  - <img alt="" src=images/Std_LinkImport.svg  style="width:32px;"> [Import link](Std_LinkImport.md): Imports selected external link(s).

  - <img alt="" src=images/Std_LinkImportAll.svg  style="width:32px;"> [Import all links](Std_LinkImportAll.md): Imports all external link(s).

-   <img alt="" src=images/Std_VarSet.svg  style="width:32px;"> [Create a variable set](Std_VarSet.md): Creates a set of properties that can be used as variables in [expressions](Expressions.md). <small>(v1.0)</small> 



### Herramientas adicionales 

-   <img alt="" src=images/Std_LinkMakeGroup.svg  style="width:32px;"> [Make link group](Std_LinkMakeGroup.md): Creates a group of links.

-   [Expression actions](Std_Expressions.md):

  - [Copy selected](Std_Expressions#Copy_selected.md): Copies expression data from selected objects to the Clipboard.

  - [Copy active document](Std_Expressions#Copy_active_document.md): Copies expression data from the active document to the Clipboard.

  - [Copy all documents](Std_Expressions#Copy_all_documents.md): Copies expression data from all documents to the Clipboard.

  - [Paste](Std_Expressions#Paste.md): Pastes expression data from the Clipboard.

-   <img alt="" src=images/Part_SelectFilter.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> [Selection filter](Part_SelectFilter.md): <small>(v1.0)</small> 

  - <img alt="" src=images/Vertex-selection.svg  style="width:32px;"> [Vertex selection](Part_SelectFilter#Vertex_selection.md): Only allows the selection of vertices.

  - <img alt="" src=images/Edge-selection.svg  style="width:32px;"> [Edge selection](Part_SelectFilter#Edge_selection.md): Only allows the selection of edges.

  - <img alt="" src=images/Face-selection.svg  style="width:32px;"> [Face selection](Part_SelectFilter#Face_selection.md): Only allows the selection of faces.

  - <img alt="" src=images/Clear-selection.svg  style="width:32px;"> [All selection filters cleared](Part_SelectFilter#All_selection_filters_cleared.md): Allows the selection of all subelements.

-   <img alt="" src=images/Std_TreeSelectAllInstances.svg  style="width:32px;"> [Select all instances](Std_TreeSelectAllInstances.md): Selects all instances of an object in the [Tree view](Tree_view.md).

-   <img alt="" src=images/Std_ToggleFreeze.svg  style="width:32px;"> [Toggle freeze](Std_ToggleFreeze.md): Toggles the freeze state of objects. <small>(v1.0)</small> 

### Obsolete tools 

-   <img alt="" src=images/View_Measure_Clear_All.svg  style="width:32px;"> [Clear measurement](View_Measure_Clear_All.md): Clears [Part](Part_Workbench.md) measurements. Not available in <small>(v1.0)</small> . Use [Std Measure](Std_Measure.md) instead.

-   <img alt="" src=images/View_Measure_Toggle_All.svg  style="width:32px;"> [Toggle measurement](View_Measure_Toggle_All.md): Toggles the display of Part measurements. Not available in <small>(v1.0)</small> . Use [Std Measure](Std_Measure.md) instead.

-   <img alt="" src=images/Std_MeasureDistance.svg  style="width:32px;"> [Measure distance](Std_MeasureDistance.md): Creates an object to measure and display a distance. Not available in <small>(v1.0)</small> . Use [Std Measure](Std_Measure.md) instead.


<div class="mw-translate-fuzzy">





</div>



---
⏵ [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > Std Base/es
