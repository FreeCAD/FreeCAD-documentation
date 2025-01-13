# Property editor/pt-br
## Introdução


<div class="mw-translate-fuzzy">

O [editor de propriedades](property_editor/pt-br.md) aparece quando a guia **Model** da [visão combinada](combo_view/pt-br.md) está ativa na [interface](interface/pt-br.md); ele permite gerenciar as propriedades publicamente expostas dos objetos de documento.


</div>


<div class="mw-translate-fuzzy">

Geralmente, o editor de propriedade é destinado a lidar com apenas um objeto de cada vez. Os valores mostrados no editor de propriedade pertencem ao objeto selecionado do documento ativo. Apesar disso, algumas propriedades como cores, podem ser definidas para vários objetos selecionados. Se não houver elementos selecionados, o editor de propriedades estará vazio.


</div>


<div class="mw-translate-fuzzy">

Nem todas as propriedades podem ser modificadas sempre; dependendo do status específico da propriedade, algumas delas serão invisíveis (não listadas), ou somente leitura (não editáveis).


</div>

<img alt="" src=images/FreeCAD_Property_editor_Data.png  style="width:300px;"> 
*The Data properties of a [Part Box](Part_Box.md)*



## Tipos de propriedade 


<div class="mw-translate-fuzzy">

Uma propriedade é uma informação como um número ou uma cadeia de texto que é anexada a um documento FreeCAD ou a um objeto no documento.


</div>


{{Code|lang=text|code=
App::PropertyAngle
App::PropertyBool
App::PropertyDistance
App::PropertyFloat
App::PropertyInteger
App::PropertyLength
App::PropertyPlacement
App::PropertyString
App::PropertyVector
}}



## Propriedades de visualização e dados 


<div class="mw-translate-fuzzy">

Há duas classes de propriedades funcionais acessíveis através de abas no editor de propriedades:

-   Propriedades da **Vista** as propriedades relacionadas à aparência \"visual\" do objeto. As propriedades de visualização estão ligadas ao atributo **ViewProvider**(`ViewObject`) do objeto e só são acessíveis quando a interface gráfica do usuário (GUI) é carregada. Eles não são acessíveis quando se usa o FreeCAD no modo de console ou como biblioteca sem cabeça.
-   Propriedades dos **dados** relativos aos parâmetros \"físicos\" do objeto. As propriedades dos **dados**definem as características essenciais do objeto; elas sempre existem, mesmo quando o FreeCAD é usado no modo console ou como uma biblioteca. Isto significa que se você carregar um documento em modo console, você pode alterar o raio de um círculo ou o comprimento de uma linha, mesmo que não consiga ver o resultado na tela.


</div>




<div class="mw-translate-fuzzy">

### Propriedades básicas 


</div>

Different objects may have different properties. However, many objects have the same properties because they are derived from the same internal class.


<div class="mw-translate-fuzzy">

A maioria dos objetos geométricos que podem ser criados e exibidos em [Vista 3D](3D_view/pt-br.md) são derivados de uma `Parte::Característica`. Veja a [Característica Part](Part_Feature/pt-br.md) para conhecer as propriedades mais básicas desses objetos.


</div>


<div class="mw-translate-fuzzy">

Para a geometria 2D, a maioria dos objetos são derivados de `Part::Part2DObject` (ela mesma derivada de `Part::Feature`) sendo a base dos [Sketche](Sketch/pt-br.md), e elementos do [Draft](Draft_Workbench/pt-br.md). Veja a [Part Part2DObject](Part_Part2DObject/pt-br.md) para as propriedades mais básicas destes objetos.


</div>

## Context menu 

To display the context menu of the Property editor right-click the background of the editor, or right-click a property.

Right-clicking the background shows three options:

-    **Add property**: adds a dynamic property to the object.

-    **Show hidden**: if active, hidden Data and View properties are shown in the editor.

-    **Auto expand**: if active, all nodes in the editor are expanded when an object is selected.

When right-clicking a property the following additional options are available:

-    **Rename property group**: renames the property group of selected properties. Only available for dynamic properties. Dynamic properties are those added by the user, as well as those added through Python code.

-    **Remove property**: removes selected properties. Only available for dynamic properties.

-    **Expression...**: brings up the Expression editor, which allows using [expressions](Expressions.md) in the property value.

-    **Status**:

:   If a status value is followed by an asterisk (*****) it is static and cannot be changed.

  - **Hidden**: if active, sets the property as hidden, meaning that it will only be displayed in the Property editor if **Show hidden** is active.

  - **Output**: if active, sets the property as output.

  - **NoRecompute**: if active, modifying the property doesn\'t touch its container for recompute.

  - **ReadOnly**: if active, sets the property as read-only. The property won\'t be editable in the Property editor and the **Expression...** option no longer available. It may however still be possible to change the property via a dialog.

  - **Transient**: if active, sets the property as transient. The value of a transient property is not saved to file. When opening a file, it is instantiated with its default value.

  - **Touched**: if active, the object becomes touched, and ready for recompute.

  - **EvalOnRestore**: if active, the property is evaluated when the document is restored.

  - **CopyOnChange**: if active, the property is copied when changed in a Link. The Link\'s **Link Copy on Change** property must be set to {{Value|Tracking}} or {{Value|Enabled}} for this to work. This is related to [Variant Links](https://forum.freecad.org/viewtopic.php?p=738833#p738833).

## Scripting

See [FeaturePython Custom Properties](FeaturePython_Custom_Properties.md).

## Preferences

See [Combo view](Combo_view#Preferences.md).





{{Interface_navi

}} {{Std_Base_navi}}



---
⏵ [documentation index](../README.md) > Property editor/pt-br
