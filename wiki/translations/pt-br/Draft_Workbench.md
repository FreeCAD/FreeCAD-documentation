
{{Page in progress}}

 

<img alt="Ícone da bancada de trabalho de draft" src=images/Workbench_Draft.svg  style="width:128px;">


{{TOCright}}

## Introdução

A <img alt="" src=images/Workbench_Draft.svg  style="width:32px;"> [bancada de trabalho Draft](Draft_Module/pt-br.md) permite desenhar objetos 2D simples, e oferece várias ferramentas para modificá-los posteriormente. Ele também fornece ferramentas para definir um plano de trabalho, uma grade e um sistema de disparo para controlar com precisão a posição de sua geometria.

Os objetos 2D criados podem ser usados para esboço geral de uma forma semelhante à do Inkscape ou do Autocad. Estas formas 2D também podem ser usadas como componentes base de objetos 3D criados com outras bancadas de trabalho, por exemplo, a <img alt="" src=images/Workbench_Part.svg  style="width:32px;"> [bancada de trabalho Part](Part_Workbench/pt-br.md) e [Arch](Arch_Workbench/pt-br.md). A conversão de objetos de Draft para <img alt="" src=images/Workbench_Sketcher.svg  style="width:32px;"> [Sketches](Sketcher_Workbench/pt-br.md) também é possível, o que significa que as formas também podem ser usadas com a <img alt="" src=images/Workbench_PartDesign.svg  style="width:32px;"> [bancada de trabalho PartDesign](PartDesign_Workbench/pt-br.md) para a criação de corpos sólidos.

O FreeCAD é principalmente uma aplicação de modelagem 3D, e assim suas ferramentas 2D não são tão avançadas como em outros programas de desenho. Se seu objetivo principal é a produção de desenhos 2D complexos e arquivos [DXF](DXF/pt-br.md), e você não precisa de modelagem 3D, talvez você queira considerar um programa de software dedicado ao desenho técnico, como o [LibreCAD](https://en.wikipedia.org/wiki/LibreCAD), [QCad](https://en.wikipedia.org/wiki/QCad), ou outros.

<img alt="Draft Workbench Example" src=images/Draft_Workbench_Example.png  style="width:400px;">

## Ferramentas para desenhar objetos {#ferramentas_para_desenhar_objetos}

Estas são ferramentas para criar objetos.

-   <img alt="" src=images/Draft_Line.svg  style="width:32px;"> [Linha](Draft_Line/pt-br.md): desenha um segmento de linha entre dois pontos.
-   <img alt="" src=images/Draft_Wire.svg  style="width:32px;"> [Polilinha](Draft_Wire/pt-br.md): desenha uma linha feita de segmentos de linhas múltiplas (polilinha).
-   <img alt="" src=images/Draft_Fillet.svg  style="width:32px;"> [Filé](Draft_Fillet/pt-br.md): desenha um filete (canto arredondado) ou um chanfro (linha reta) entre duas [linhas](Draft_Line/pt-br.md) simples. <small>(v0.19)</small> 
-   <img alt="" src=images/Draft_Arc.svg  style="width:32px;"> [Arco](Draft_Arc/pt-br.md): desenha um segmento de arco a partir do centro, raio, ângulo inicial e ângulo final.
-   <img alt="" src=images/Draft_Arc_3Points.svg  style="width:32px;"> [Arco 3Pontos](Draft_Arc_3Points/pt-br.md): desenha um segmento de arco circular a partir de três pontos que estão localizados na circunferência. <small>(v0.19)</small> 
-   <img alt="" src=images/Draft_Circle.svg  style="width:32px;"> [Círculo](Draft_Circle/pt-br.md): desenha um círculo a partir do centro e do raio.
-   <img alt="" src=images/Draft_Ellipse.svg  style="width:32px;"> [Elipse](Draft_Ellipse/pt-br.md): desenha uma elipse a partir de dois pontos de canto.
-   <img alt="" src=images/Draft_Rectangle.svg  style="width:32px;"> [Rectângulo](Draft_Rectangle/pt-br.md): desenha um retângulo a partir de dois pontos de canto.
-   <img alt="" src=images/Draft_Polygon.svg  style="width:32px;"> [Polígono](Draft_Polygon/pt-br.md): desenha um polígono regular a partir do centro, do raio e do número de lados.
-   <img alt="" src=images/Draft_BSpline.svg  style="width:32px;"> [BSpline](Draft_BSpline/pt-br.md): retira um B-Spline de uma série de pontos.
-   <img alt="" src=images/Draft_CubicBezCurve.svg  style="width:32px;"> [Curva de Bezier Cúbica](Draft_CubicBezCurve/pt-br.md): desenha uma curva Bezier de terceiro grau arrastando dois pontos. <small>(v0.19)</small> 
-   <img alt="" src=images/Draft_BezCurve.svg  style="width:32px;"> [Curva de Bezier](Draft_BezCurve/pt-br.md): desenha uma curva Bezier a partir de uma série de pontos.
-   <img alt="" src=images/Draft_Point.svg  style="width:32px;"> [Ponto](Draft_Point/pt-br.md): insere um objeto pontual.
-   <img alt="" src=images/Draft_Facebinder.svg  style="width:32px;"> [Ligar Faces](Draft_Facebinder/pt-br.md): cria um objeto a partir de faces selecionadas em objetos existentes.
-   <img alt="" src=images/Draft_ShapeString.svg  style="width:32px;"> [Formato de texto](Draft_ShapeString/pt-br.md): insere uma forma composta que representa uma cadeia de texto em um determinado ponto.

## Objetos de anotação {#objetos_de_anotação}

-   <img alt="" src=images/Draft_Text.svg  style="width:32px;"> [Texto](Draft_Text/pt-br.md): desenha uma anotação de texto com várias linhas.
-   <img alt="" src=images/Draft_Dimension.svg  style="width:32px;"> [Dimensão](Draft_Dimension/pt-br.md): desenha uma anotação dimensional.
-   <img alt="" src=images/Draft_Label.svg  style="width:32px;"> [Etiqueta](Draft_Label/pt-br.md): coloca uma etiqueta com uma seta apontando para um elemento selecionado. <small>(v0.17)</small> 
-   <img alt="" src=images/Draft_AnnotationStyleEditor.svg  style="width:32px;"> [Editor de estilo de anotação](Draft_AnnotationStyleEditor/pt-br.md): abre um editor para mudar o estilo de anotação desses objetos. <small>(v0.19)</small> 

## Modificador de objetos {#modificador_de_objetos}

Estas são ferramentas para modificar objetos existentes. Elas trabalham em objetos selecionados, mas se nenhum objeto for selecionado, você será convidado a selecionar um.

Muitas ferramentas de operação (mover, girar, matriz, etc.) também trabalham em objetos sólidos ([Part](Part_Workbench/pt-br.md), [PartDesign](PartDesign_Workbench/pt-br.md), [Arch](Arch_Workbench/pt-br.md), etc.).

-   <img alt="" src=images/Draft_Move.svg  style="width:32px;"> [Mover](Draft_Move/pt-br.md): move objetos de um local para outro.
-   <img alt="" src=images/Draft_Rotate.svg  style="width:32px;"> [Girar](Draft_Rotate/pt-br.md): gira os objetos de um ângulo inicial a um ângulo final.
-   <img alt="" src=images/Draft_Scale.svg  style="width:32px;"> [Escala](Draft_Scale/pt-br.md): escalas de objetos selecionados em torno de um ponto base.
-   <img alt="" src=images/Draft_Mirror.svg  style="width:32px;"> [Espelho](Draft_Mirror/pt-br.md): espelha os objetos selecionados.
-   <img alt="" src=images/Draft_Offset.svg  style="width:32px;"> [Deslocar](Draft_Offset/pt-br.md): segmentos de um objeto a uma certa distância.
-   <img alt="" src=images/Draft_Trimex.svg  style="width:32px;"> [Aparar/Alargar](Draft_Trimex/pt-br.md): apara ou estende um objeto.
-   <img alt="" src=images/Draft_Stretch.svg  style="width:32px;"> [Esticar](Draft_Stretch/pt-br.md): estica os objetos selecionados. <small>(v0.17)</small> 

-   <img alt="" src=images/Draft_Clone.svg  style="width:32px;"> [Clone](Draft_Clone/pt-br.md): clona os objetos selecionados.
-   <img alt="" src=images/Draft_Array.svg  style="width:32px;"> Ferramentas de séries.
    -   <img alt="" src=images/Draft_OrthoArray.svg  style="width:32px;"> [ Séries ortogonais](Draft_OrthoArray/pt-br.md): cria uma série ortogonal a partir do objeto selecionado. Ele também pode criar copias de [Link do aplicativo](App_Link/pt-br.md). <small>(v0.19)</small> 
    -   <img alt="" src=images/Draft_PolarArray.svg  style="width:32px;"> [Série Polar](Draft_PolarArray/pt-br.md): cria uma série em um padrão polar, ou seja, varrendo um ângulo. Também pode criar cópias [Link do aplicativo](App_Link/pt-br.md). <small>(v0.19)</small> 
    -   <img alt="" src=images/Draft_CircularArray.svg  style="width:32px;"> [Série circular](Draft_CircularArray/pt-br.md): cria uma série em um padrão circular, ou seja, partindo de um centro e avançando radialmente para fora. Também pode criar cópias [Link do aplicativo](App_Link/pt-br.md). <small>(v0.19)</small> 
    -   <img alt="" src=images/Draft_PathArray.svg  style="width:32px;"> [Série por caminho](Draft_PathArray/pt-br.md): cria um conjunto de objetos colocando as cópias ao longo de um caminho.
    -   <img alt="" src=images/Draft_PathLinkArray.svg  style="width:32px;"> [Série de links sobre trilhos](Draft_PathLinkArray/pt-br.md): como <img alt="" src=images/Draft_PathArray.svg  style="width:32px;"> [Série por caminho](Draft_PathArray/pt-br.md), mas cria [Link do aplicativo](App_Link/pt-br.md) em vez de cópias regulares. <small>(v0.19)</small> 
    -   <img alt="" src=images/Draft_PointArray.svg  style="width:32px;"> [Série em pontos](Draft_PointArray/pt-br.md): cria um conjunto de objetos colocando as cópias em certos pontos. <small>(v0.18)</small> 
    -   <img alt="" src=images/Draft_PointLinkArray.svg  style="width:32px;"> [Série de links sobre pontos](Draft_PointLinkArray/pt-br.md): como <img alt="" src=images/Draft_PointArray.svg  style="width:32px;"> [Série em pontos](Draft_PointArray/pt-br.md), mas cria [Link do aplicativo](App_Link/pt-br.md) em vez de cópias regulares. <small>(v0.19)</small> 

-   <img alt="" src=images/Draft_Edit.svg  style="width:32px;"> [Editar](Draft_Edit/pt-br.md): edita um objeto selecionado.
-   <img alt="" src=images/Draft_SubelementHighlight.svg  style="width:32px;"> [Destaque do subelemento](Draft_SubelementHighlight/pt-br.md): entra em um modo de edição que permite editar diferentes objetos. <small>(v0.19)</small> 

-   <img alt="" src=images/Draft_Join.svg  style="width:32px;"> [Conectar](Draft_Join/pt-br.md): une as linhas em um único fio. <small>(v0.18)</small> 
-   <img alt="" src=images/Draft_Split.svg  style="width:32px;"> [Separar](Draft_Split/pt-br.md): divide um fio em dois em um ponto. <small>(v0.18)</small> 
-   <img alt="" src=images/Draft_Upgrade.svg  style="width:32px;"> [Atualizar](Draft_Upgrade/pt-br.md): atualiza objetos em um objeto de nível superior.
-   <img alt="" src=images/Draft_Downgrade.svg  style="width:32px;"> [Regredir](Draft_Downgrade/pt-br.md): rebaixa os objetos para objetos de nível inferior.

-   <img alt="" src=images/Draft_WireToBSpline.svg  style="width:32px;"> [Da polilinha à BSpline](Draft_WireToBSpline/pt-br.md): converte uma linha B-Spline e vice-versa.
-   <img alt="" src=images/Draft_Draft2Sketch.svg  style="width:32px;"> [Draft para Sketch](Draft_Draft2Sketch/pt-br.md): converte um objeto Draft em um [Bancada de trabalho Sketch](Sketcher_Workbench/pt-br.md). Sketch e vice-versa.
-   <img alt="" src=images/Draft_Slope.svg  style="width:32px;"> [Declive](Draft_Slope/pt-br.md): altera a inclinação de elevação da [Linha](Draft_Line/pt-br.md) ou [Polilinha](Draft_Wire/pt-br.md) atualmente selecionada. <small>(v0.17)</small> 
-   <img alt="" src=images/Draft_FlipDimension.svg  style="width:32px;"> [ Reverter a direção das cotas](Draft_FlipDimension/pt-br.md): vira a orientação do texto de uma [cota](Draft_Dimension/pt-br.md).

-   <img alt="" src=images/Draft_Shape2DView.svg  style="width:32px;"> [Visão 2D de uma forma](Draft_Shape2DView/pt-br.md): cria um objeto 2D que é uma visão 2D achatada de um objeto 3D.

## Barra de ferramentas da bandeja de rascunho {#barra_de_ferramentas_da_bandeja_de_rascunho}

A barra de ferramentas [Bandeja de rascunho](Draft_Tray/pt-br.md) aparece quando a bancada de trabalho é iniciada, e permite selecionar o plano de trabalho, com algumas propriedades visuais como a cor da linha, cor da forma, largura da linha, tamanho do texto e grupo automático.

![](images/Draft_tray_default.png )

Its tools are also available in the {{MenuCommand|Draft → Utilities}} menu:

-   <img alt="" src=images/Draft_SelectPlane.svg  style="width:32px;"> [Plano de trabalho](Draft_SelectPlane/pt-br.md): define um plano de trabalho a partir de uma vista padrão ou de uma face selecionada.
-   <img alt="" src=images/Draft_SetStyle.svg  style="width:32px;"> [Estilo de conjunto](Draft_SetStyle/pt-br.md): define o estilo padrão para novos objetos, e opcionalmente aplica o estilo a objetos e grupos selecionados.
-   <img alt="" src=images/Draft_ToggleConstructionMode.svg  style="width:32px;">[Modo de construção](Draft_ToggleConstructionMode/pt-br.md): ativa ou desativa o modo de construção de rascunho.
-   <img alt="" src=images/Draft_AutoGroup.svg  style="width:32px;"> [Grupo automático](Draft_AutoGroup/pt-br.md): colocar automaticamente novos objetos em um determinado <img alt="" src=images/Std_Group.svg  style="width:32px;">[Grupo padrão](Std_Group/pt-br.md), <img alt="" src=images/Draft_Layer.svg  style="width:32px;">[Camada](Draft_Layer/pt-br.md), ou um dos objetos de grupo do [Bancada de trabalho Arch](Arch_Workbench/pt-br.md), como <img alt="" src=images/Arch_BuildingPart.svg  style="width:32px;">. [Parte de um edifício](Arch_BuildingPart/pt-br.md). <small>(v0.17)</small> 

-   <img alt="" src=images/Draft_SetStyle.svg  style="width:32px;"> [Set style](Draft_SetStyle.md): sets the default style for new objects. <small>(v0.19)</small> 

-   <img alt="" src=images/Draft_ToggleConstructionMode.svg  style="width:32px;"> [Toggle construction mode](Draft_ToggleConstructionMode.md): switches Draft construction mode on or off.

-   <img alt="" src=images/Draft_AutoGroup.svg  style="width:32px;"> [AutoGroup](Draft_AutoGroup.md): changes the active [Draft Layer](Draft_Layer.md) or, optionally, the active [Std Group](Std_Group.md) or group-like [Arch](Arch_Workbench.md) object.

## Draft annotation scale widget {#draft_annotation_scale_widget}

Com o [Widget de escala de anotação](Draft_annotation_scale_widget/pt-br.md) a escala de anotação Draft pode ser especificada. O widget está localizado na [Barra de status](Status_bar/pt-br.md).

![](images/Draft_annotation_scale_widget_button.png )

## Draft snap widget {#draft_snap_widget}

O [Widget de ancoragem](Draft_snap_widget/pt-br.md) pode ser usado como uma alternativa para a [Barra de ferramentas Rascunho de pressão](#Barra_de_ferramentas_Rascunho_de_pressão.md). O widget está localizado na [Barra de status](Status_bar/pt-br.md).

![](images/Draft_snap_widget_button.png )

## Barra de ferramentas Rascunho de pressão {#barra_de_ferramentas_rascunho_de_pressão}

A barra de ferramentas [Captura](Draft_Snap/pt-br.md) permite selecionar o modo de precisão atual. Seu botão se mantém pressionado quando um modo está ativo.

-   <img alt="" src=images/Draft_Snap_Lock.svg  style="width:32px;"> [Alternar tranca](Draft_Snap_Lock/pt-br.md): habilita ou desabilita a [ancoragem](Draft_Snap/pt-br.md) global de objetos.
-   <img alt="" src=images/Draft_Snap_Endpoint.svg  style="width:32px;"> [Ponto final](Draft_Snap_Endpoint/pt-br.md): é fixado nas extremidades dos segmentos de linha, arco e estriados.
-   <img alt="" src=images/Draft_Snap_Midpoint.svg  style="width:32px;"> [Ponto médio](Draft_Snap_Midpoint/pt-br.md): fica pendurado no ponto central da linha e nos segmentos de arco.
-   <img alt="" src=images/Draft_Snap_Center.svg  style="width:32px;"> [Centro](Draft_Snap_Center/pt-br.md): presilhas no centro dos círculos, arcos e faces, [objetos proxy para a bancada de trabalho](Draft_WorkingPlaneProxy/pt-br.md) e [peças de construção](Arch_BuildingPart/pt-br.md).
-   <img alt="" src=images/Draft_Snap_Angle.svg  style="width:32px;"> [Ângulo](Draft_Snap_Angle/pt-br.md): estala para os pontos cardinais especiais de círculos e arcos, a 45° e 90°.
-   <img alt="" src=images/Draft_Snap_Intersection.svg  style="width:32px;"> [Intersecção](Draft_Snap_Intersection/pt-br.md): encaixa na interseção de duas linhas ou segmentos de arco. Passe o mouse sobre os dois objetos desejados para ativar seus encaixes de interseção.
-   <img alt="" src=images/Draft_Snap_Perpendicular.svg  style="width:32px;"> [Perpendicular](Draft_Snap_Perpendicular/pt-br.md): em segmentos de linha e arco, encaixa perpendicularmente ao último ponto.
-   <img alt="" src=images/Draft_Snap_Extension.svg  style="width:32px;"> [Extensão](Draft_Snap_Extension/pt-br.md): se estende para além dos pontos finais dos segmentos de linha. Passe o mouse sobre o objeto desejado para ativar seu estalido de extensão.
-   <img alt="" src=images/Draft_Snap_Parallel.svg  style="width:32px;"> [Paralelo](Draft_Snap_Parallel/pt-br.md): se encaixa em uma linha imaginária paralela a um segmento de linha. Passe o mouse sobre o objeto desejado para ativar seu estalido paralelo.
-   <img alt="" src=images/Draft_Snap_Special.svg  style="width:32px;"> [Especial](Draft_Snap_Special/pt-br.md): instantâneos em pontos especiais definidos pelo objeto. <small>(v0.17)</small> 
-   <img alt="" src=images/Draft_Snap_Near.svg  style="width:32px;"> [Perto](Draft_Snap_Near/pt-br.md): encaixa no ponto ou borda mais próximo do objeto mais próximo.
-   <img alt="" src=images/Draft_Snap_Ortho.svg  style="width:32px;"> [Orto](Draft_Snap_Ortho/pt-br.md): encaixa em linhas imaginárias que cruzam o último ponto e se estendem a 0 °, 45 ° e 90 °.
-   <img alt="" src=images/Draft_Snap_Grid.svg  style="width:32px;"> [Grade](Draft_Snap_Grid/pt-br.md): encaixa nas interseções das linhas da grade, se a grade estiver visível.
-   <img alt="" src=images/Draft_Snap_WorkingPlane.svg  style="width:32px;"> [Plano de trabalho](Draft_Snap_WorkingPlane/pt-br.md): sempre coloca o ponto de destino no [plano de trabalho](Draft_SelectPlane/pt-br.md) atual, mesmo se você fizer snap de um ponto externo no plano de trabalho.
-   <img alt="" src=images/Draft_Snap_Dimensions.svg  style="width:32px;"> [Dimensões](Draft_Snap_Dimensions/pt-br.md): mostra as dimensões temporárias X e Y enquanto se encaixa.
-   <img alt="" src=images/Draft_ToggleGrid.svg  style="width:32px;"> [Grade de comutação](Draft_ToggleGrid/pt-br.md): ativa ou desativa a visibilidade da grade.

## Draft utility tools toolbar {#draft_utility_tools_toolbar}

-   <img alt="" src=images/Draft_Layer.svg  style="width:32px;"> [Camada](Draft_Layer/pt-br.md): cria uma camada no documento atual, à qual os objetos podem ser adicionados para controlar a visibilidade e a cor do objeto. Ele substitui o Draft VisGroup. <small>(v0.19)</small> 
-   <img alt="" src=images/Draft_WorkingPlaneProxy.svg  style="width:32px;"> [Proxy de plano de trabalho](Draft_WorkingPlaneProxy/pt-br.md): criar um objeto proxy para armazenar a posição atual no [Plano de trabalho](Draft_SelectPlane/pt-br.md). <small>(v0.17)</small> 
-   <img alt="" src=images/Draft_ToggleDisplayMode.svg  style="width:32px;"> [Modo de exibição comutável](Draft_ToggleDisplayMode/pt-br.md): alterna o modo de exibição dos objetos selecionados entre \"Flat Lines\" e \"Wireframe\".
-   <img alt="" src=images/Draft_AddToGroup.svg  style="width:32px;"> [Adicionar ao grupo](Draft_AddToGroup/pt-br.md): rapidamente adiciona objetos selecionados a um [Grupo Std](Std_Group/pt-br.md) existente.
-   <img alt="" src=images/Draft_SelectGroup.svg  style="width:32px;"> [Selecione o conteúdo do grupo](Draft_SelectGroup/pt-br.md): seleciona o conteúdo de um selecionado [Grupo Std](Std_Group/pt-br.md) ou [Draft Layer](Draft_Layer/pt-br.md).
-   <img alt="" src=images/Draft_AddConstruction.svg  style="width:32px;"> [Adicionar ao grupo Construção](Draft_AddConstruction/pt-br.md): adicionar objetos selecionados ao grupo Construção. <small>(v0.17)</small> 
-   <img alt="" src=images/Draft_Heal.svg  style="width:32px;"> [Curar](Draft_Heal/pt-br.md): cura objetos de rascunho problemáticos encontrados em arquivos muito antigos.

## Ferramentas adicionais {#ferramentas_adicionais}

The {{MenuCommand|Draft → Utilities}} menu contains several tools. Most of them can also be accessed from toolbars or the [Draft Tray](Draft_Tray.md) and have already been mentioned above. For the following tools this is not the case:

-   <img alt="" src=images/Draft_ToggleContinueMode.svg  style="width:32px;"> [Alternar modo continuar](Draft_ToggleContinueMode/pt-br.md): ativa ou desativa o modo de continuação do Draft.
-   <img alt="" src=images/Draft_ApplyStyle.svg  style="width:32px;"> [Aplicar o estilo atual](Draft_ApplyStyle/pt-br.md): aplica o estilo atual a objetos e grupos selecionados.
-   <img alt="" src=images/Draft_ShowSnapBar.svg  style="width:32px;"> [Mostrar barra de acoragem](Draft_ShowSnapBar/pt-br.md): mostra a barra de ferramentas [Rascunho de pressão](Draft_Snap/pt-br.md).

## Características adicionais {#características_adicionais}

-   [Restrições](Draft_Constrain/pt-br.md): limitar o ponteiro a movimentos horizontais ou verticais em relação a um ponto anterior.
-   [Captura](Draft_Snap/pt-br.md): colocar novos pontos em lugares especiais sobre objetos existentes ou sobre a grade.
-   [Modo de cópia](Draft_Copying/pt-br.md): Todas as ferramentas de modificação podem modificar os objetos selecionados ou criar uma cópia modificada dos mesmos. Pressionar e segurar **Alt** enquanto o objeto está sendo modificado, por exemplo, movido ou girado, cria uma cópia quando a chave é liberada.
-   [Modo de construção](Draft_ToggleConstructionMode/pt-br.md): Permite criar geometrias separadas das demais, simplesmente ligando e desligando-as.
-   [Plano de trabalho](Draft_SelectPlane/pt-br.md): permite selecionar uma superfície sobre a qual você pode construir suas formas.

## Tree view context menu {#tree_view_context_menu}

The following additional options are available in the [Tree view](Tree_view.md) context menu:

### Selection options {#selection_options}

If there is a selection the context menu contains one additional sub-menu:

-    {{MenuCommand|Utilities}}: a subset of the tools available in the main Draft Utilities menu.

### Wire options {#wire_options}

For a [Draft Wire](Draft_Wire.md), [Draft BSpline](Draft_BSpline.md), [Draft CubicBezCurve](Draft_CubicBezCurve.md) and [Draft BezCurve](Draft_BezCurve.md) this additional option is available:

-   <img alt="" src=images/Draft_Edit.svg  style="width:32px;"> Flatten this wire: flattens the wire based on its internal geometry. This option currently does not work properly.

### Layer container options {#layer_container_options}

For a [Draft LayerContainer](Draft_Layer.md) these additional options are available:

-   <img alt="" src=images/Draft_Layer.svg  style="width:32px;"> Merge layer duplicates: this option currently does not work.

-   <img alt="" src=images/Draft_NewLayer.svg  style="width:32px;"> [Add new layer](Draft_Layer.md): adds a new layer to the current document.

### Layer options {#layer_options}

For a [Draft Layer](Draft_Layer.md) these additional options are available:

-   <img alt="" src=images/button_right.svg  style="width:32px;"> [Activate this layer](Draft_AutoGroup.md): makes the selected layer the active layer.

-   <img alt="" src=images/Draft_SelectGroup.svg  style="width:32px;"> [Select layer contents](Draft_SelectGroup.md): selects the objects inside the selected layer.

### Working plane proxy options {#working_plane_proxy_options}

For a [Draft WorkingPlaneProxy](Draft_WorkingPlaneProxy.md) these additional options are available:

-   <img alt="" src=images/Draft_SelectPlane.svg  style="width:32px;"> [Write camera position](Draft_WorkingPlaneProxy#Tree_view_context_menu.md): updates the camera settings stored in the working plane proxy.

-   <img alt="" src=images/Draft_SelectPlane.svg  style="width:32px;"> [Write objects state](Draft_WorkingPlaneProxy#Tree_view_context_menu.md): updates the visibility state of objects stored in the working plane proxy.

## 3D view context menu {#d_view_context_menu}

The following additional options are available in the [3D view](3D_view.md) context menu:

### No-selection options {#no_selection_options}

If there is no selection the context menu contains one additional sub-menu:

-    {{MenuCommand|Utilities}}: a subset of the tools available in the main Draft Utilities menu.

### Selection options {#selection_options_1}

If there is a selection the context menu contains two additional sub-menus:

-    {{MenuCommand|Draft}}: tools for [drawing objects](#Drawing_objects.md) and [modifying objects](#Modifying_objects.md).

-    {{MenuCommand|Utilities}}: a subset of the tools available in the main Draft Utilities menu.

## Ferramentas obsoletas {#ferramentas_obsoletas}

Estes comandos são obsoletos, mas ainda estão disponíveis.

-   <img alt="" src=images/Draft_Array.svg  style="width:32px;"> [Matriz](Draft_Array/pt-br.md): cria uma matriz polar ou retangular a partir de objetos selecionados. {{Obsolete|0.19}}
-   <img alt="" src=images/Draft_Drawing.svg  style="width:32px;"> [Desenhando](Draft_Drawing/pt-br.md): escreve objetos selecionados em uma página [Drawing Workbench](Drawing_Workbench/pt-br.md). {{Obsolete|0.17}}
-   <img alt="" src=images/Draft_CloseLine.svg  style="width:32px;"> [Linha fechada](Draft_CloseLine/pt-br.md): termina o desenho do atual [Draft Wire](Draft_Wire/pt-br.md) ou [Draft BSpline](Draft_BSpline/pt-br.md), e o fecha. {{Obsolete|0.19}}
-   <img alt="" src=images/Draft_FinishLine.svg  style="width:32px;"> [Linha de acabamento](Draft_FinishLine/pt-br.md): termina o desenho do atual [Draft Wire](Draft_Wire.md) ou [Draft BSpline](Draft_BSpline/pt-br.md), sem fechá-lo. {{Obsolete|0.19}}
-   <img alt="" src=images/Draft_UndoLine.svg  style="width:32px;"> [Desfazer linha](Draft_UndoLine/pt-br.md):Desfaz o último segmento de um [Draft Wire](Draft_Wire/pt-br.md). {{Obsolete|0.19}}

-   <img alt="" src=images/Draft_Drawing.svg  style="width:32px;"> [Drawing](Draft_Drawing.md): writes selected objects to a [Drawing Workbench](Drawing_Workbench.md) page. {{Obsolete|0.17}}

These [3D view](3D_view.md) context menu options are still available when the [Draft Wire](Draft_Wire.md), [Draft BSpline](Draft_BSpline.md), [Draft CubicBezCurve](Draft_CubicBezCurve.md) or [Draft BezCurve](Draft_BezCurve.md) command is active but will be removed in the near future:

-   <img alt="" src=images/Draft_UndoLine.svg  style="width:32px;"> [Undo last segment](Draft_Wire#Options.md): use the {{button|<img src="images/Draft_UndoLine.svg" width=16px> Undo}} button in the task panel of the command instead. {{Obsolete|0.20}}

-   <img alt="" src=images/Draft_FinishLine.svg  style="width:32px;"> [Finish line](Draft_Wire#Options.md): use the **<img src="images/Draft_FinishLine.svg" width=16px> Finish** button in the task panel of the command instead. {{Obsolete|0.20}}

-   <img alt="" src=images/Draft_CloseLine.svg  style="width:32px;"> [Close line](Draft_Wire#Options.md): use the **<img src="images/Draft_CloseLine.svg" width=16px> Close** button in the task panel of the command instead. {{Obsolete|0.20}}

## Preferências

-   <img alt="" src=images/Preferences-draft.svg  style="width:32px;"> [Preferências](Draft_Preferences/pt-br.md): preferências gerais para o plano de trabalho e para as ferramentas de desenho.
-   <img alt="" src=images/Preferences-import-export.svg  style="width:32px;"> [Preferências de exportação de importação](Import_Export_Preferences/pt-br.md): preferências disponíveis para importação e exportação de e para diferentes formatos de arquivo.

## Formatos de arquivo {#formatos_de_arquivo}

These are functions for opening, importing or exporting other file formats. Opening will open a new document with the contents of the file, while importing will append the contents of the file to the current document. Export will save the selected objects to a file. If nothing is selected, all objects will be exported. Be aware that the purpose of the Draft Workbench is to work with 2D objects, so those import routines focus only on 2D objects, and although DXF and OCA formats also support object definitions in 3D space (objects are not necessarily flat), they will not import volumetric objects such as meshes, 3D surfaces, etc., but rather lines, circles, texts or flat shapes. Currently supported file formats are: The Draft Workbench provides FreeCAD with importers and exporters for the following file formats:

-   [Autodesk .DXF](Draft_DXF/pt-br.md): importação e exportação [Drawing Exchange Format](http://en.wikipedia.org/wiki/AutoCAD_DXF) arquivos criados com aplicações CAD 2D. Veja também [FreeCAD e DXF Import](FreeCAD_and_DXF_Import/pt-br.md).
-   Autodesk .DWG: importa e exporta arquivos DWG através do importador DXF, quando o utilitário [ODA Converter](Extra_python_modules#ODA_Converter_(anteriormente_Teigha_Converter).md) é instalado. Veja também [FreeCAD e DWG Import](FreeCAD_and_DWG_Import/pt-br.md).
-   [SVG](Draft_SVG/pt-br.md): importação e exportação [Scalable Vector Graphics](http://en.wikipedia.org/wiki/Scalable_Vector_Graphics) arquivos criados com aplicações de desenho vetorial.
-   [Open Cad format .OCA](Draft_OCA/pt-br.md): importa e exporta arquivos OCA/GCAD, um formato de arquivo CAD potencialmente novo [abrir arquivo CAD](http://groups.google.com/group/open_cad_format).
-   [Airfoil Data Format .DAT](Draft_DAT/pt-br.md): importa arquivos DAT descrevendo [Airfoil profiles](http://www.ae.illinois.edu/m-selig/ads/coord_database.html).

### Instalar importadores {#instalar_importadores}

-   [Importação FreeCAD e DWG](FreeCAD_and_DWG_Import/pt-br.md): Importação e exportação de arquivos DWG
-   [Importação FreeCAD e DXF](FreeCAD_and_DXF_Import/pt-br.md): Importação e exportação de arquivos DXF

## Testes unitários {#testes_unitários}


**Veja também:**

[Bancada de trabalho Testing framework](Testing/pt-br.md).

Para executar os testes unitários da bancada de trabalho, executar o seguinte a partir do terminal do sistema operacional. 
```python
freecad -t TestDraft
```

## Scripting

As ferramentas Draft podem ser usadas em [macros](macros/pt-br.md) e do console [Python](Python/pt-br.md) usando o [Draft API](Draft_API/pt-br.md).

A bancada de trabalho inclui um módulo para criar amostras de todos os objetos em um novo documento. <small>(v0.19)</small> 

Use isto para testar se todos os objetos são produzidos corretamente. 
```python
import drafttests.draft_test_objects as dto
doc = dto.create_test_file()
```

A inspeção do código deste módulo é útil para entender como utilizar a interface de programação. 
```python
$INSTALLDIR/Mod/Draft/drafttests/draft_test_objects.py
```

Where `$INSTALLDIR` is the toplevel directory where the software was installed; for example, in Linux it may be `/usr/share/freecad`.

<img alt="" src=images/Draft_test_objects.png  style="width:500px;"> 
*Objetos de teste para a [Bancada de trabalho Draft](Draft_Workbench/pt-br.md).*

## Tutorials

-   [Draft tutorial](Draft_tutorial.md)
-   [Draft ShapeString tutorial](Draft_ShapeString_tutorial.md)





 

[Category:Workbenches{{\#translation:}}](Category:Workbenches.md)
