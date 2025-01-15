# <img alt="Ícone da Sketcher workbench" src=images/Workbench_Sketcher.svg  style="width:64px;"> Sketcher Workbench/pt-br






## Introdução


<div class="mw-translate-fuzzy">

A bancada de trabalho <img alt="" src=images/Workbench_Sketcher.svg  style="width:24px;"> [bancada de trabalho Sketcher](Sketcher_Workbench/pt-br.md) do FreeCAD é usada para criar Sketches 2D destinadas ao uso na <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [bancada de trabalho PartDesign](PartDesign_Workbench/pt-br.md), <img alt="" src=images/Workbench_Arch.svg  style="width:24px;"> [bancada de trabalho Arch](Arch_Workbench/pt-br.md), e outras bancadas de trabalho. Geralmente, um desenho 2D é considerado o ponto de partida para a maioria dos modelos CAD, pois um esboço 2D pode ser \"extrudado\" para criar uma forma 3D; outros esboços 2D podem ser usados para criar outros recursos como bolsos, saliências ou extrusões no topo das formas 3D previamente construídas. Junto com as operações booleanas definidas na <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [bancada de trabalho Part](Part_Workbench/pt-br.md), o Sketcher forma a base do método de [Geometria Sólida Construtiva](constructive_solid_geometry/pt-br.md)(constructive solid geometry - CSG) de construção de sólidos. Além disso, junto com as operações da <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [bancada de trabalho PartDesign](PartDesign_Workbench/pt-br.md), o Sketcher também forma a base da metodologia de [edição de recursos](feature_editing/pt-br.md) de criação de sólidos .


</div>

Together with boolean operations defined in the <img alt="" src=images/Workbench_Part.svg  style="width:16px;"> [Part Workbench](Part_Workbench.md), the Sketcher Workbench, or \"The Sketcher\" for short, forms the basis of the [constructive solid geometry](Constructive_solid_geometry.md) (CSG) method of building solids. Together with <img alt="" src=images/Workbench_PartDesign.svg  style="width:16px;"> [PartDesign Workbench](PartDesign_Workbench.md) operations, it also forms the basis of the [feature editing](Feature_editing.md) methodology of creating solids. But many other workbenches use sketches as well.


<div class="mw-translate-fuzzy">

A bancada do Sketcher apresenta restrições (\"constraints\"), permitindo que formas 2D sigam definições geométricas precisas em termos de comprimento, ângulos e relações (horizontalidade, verticalidade, perpendicularidade, etc.). Um solucionador de restrições calcula a extensão do efeito das restrições sobre a geometria 2D e permite a exploração interativa dos graus de liberdade do esboço.


</div>


<div class="mw-translate-fuzzy">

O Sketcher não se destina à produção de plantas 2D. Depois que os esboços são usados para gerar um sólido, eles são automaticamente ocultados. As restrições são visíveis apenas no modo de edição de esboço.


</div>

<img alt="" src=images/FC_ConstrainedSketch.png  style="width:450px;"> 
*''Um esboço básico totalmente restrito''*

## Constraints


<div class="mw-translate-fuzzy">

Em vez de cotas, restrições são usadas para limitar os graus de liberdade de um objeto. Por exemplo, uma linha sem restrições tem 4 graus de liberdade - (em inglês, Degrees Of Freedom - abreviado como \" DOF \"): ela pode ser movida horizontal e verticalmente, pode ser estendida/encurtada, e pode ser rotacionada.


</div>

Aplicar uma restrição horizontal ou vertical, ou uma restrição angular (em relação a outra linha ou a um dos eixos), limitará sua capacidade de rotação, deixando-a com 3 graus de liberdade. Travar um de seus pontos em relação à origem removerá outros 2 graus de liberdade, e a aplicação de uma restrição de tamanho (dimensão) removerá o último grau de liberdade. A linha é então considerada **totalmente restrita**.


<div class="mw-translate-fuzzy">

Vários objetos podem ser restringidos entre si. Duas linhas podem ser unidas por meio de um de seus pontos com a restrição de ponto coincidente. Um ângulo pode ser definido entre elas, ou elas podem ser postas como perpendiculares. Uma linha pode ser tangente a um arco ou círculo e assim por diante. Um esboço complexo com vários objetos terá uma série de soluções diferentes e torná-lo **totalmente restrito** significa que apenas uma dessas soluções possíveis foi alcançada com base nas restrições aplicadas.


</div>


<div class="mw-translate-fuzzy">

Existem dois tipos de restrições: geométricas e dimensionais. Eles são detalhados na seção [\'Ferramentas\'](#Ferramentas/pt-br.md) abaixo.


</div>

### Edit constraints 

When a [driving dimensional constraint](Sketcher_ToggleDrivingConstraint.md) is created, and if the **Ask for value after creating a dimensional constraint** [preference](Sketcher_Preferences#Display.md) is selected (default), a dialog opens to edit its value.

![](images/Sketcher_Edit_Constraint.png )

You can enter a numerical value or an [expression](Expressions.md), and it is possible to name the constraint to facilitate its use in other expressions. You can also check the **Reference** checkbox to switch the constrain to [reference mode](Sketcher_ToggleDrivingConstraint.md).

To edit the value of an existing dimensional constraint do one of the following:

-   Double-click the constraint value in the [3D view](3D_view.md).
-   Double-click the constraint in the [Sketcher Dialog](Sketcher_Dialog.md).
-   Right-click the constraint in the Sketcher Dialog and select the **Change value** option from the context menu.

### Reposition constraints 

Dimensional constraints can be repositioned in the 3D view by dragging. Hold down the left mouse button over the constraint value and move the mouse. The symbols of geometric constraints are positioned automatically and cannot be moved.

## Profile sketches 

To create a sketch that can be used as a profile for generating solids certain rules must be followed:

-   The sketch must contain only closed contours. Gaps between endpoints, however small, are not allowed.
-   Contours can be nested, to create voids, but should not self-intersect or intersect other contours.
-   Contours cannot share edges with other contours. Duplicate edges must be avoided.
-   T-connections, that is more than two edges sharing a common point, or a point touching an edge, are not allowed.

These rules do not apply to construction geometry (default color blue), which is not shown outside edit mode, or if the sketch is used for a different purpose. Depending on the workbench and the tool that will use the profile sketch, additional restrictions may apply.

## Drawing aids 

The Sketcher Workbench has several drawing aids and other features that can help when creating geometry and applying constraints.

### Continue modes 

There are two continue modes: **Geometry creation \"Continue Mode\"** and **Constraint creation \"Continue Mode\"**. If these are checked (default) in the [preferences](Sketcher_Preferences#Display.md), related tools will restart after finishing. To exit a continuous tool press **Esc** or the right mouse button. This must be repeated if a continuous geometry tool has already received input. You can also exit a continuous tool by starting another geometry or constraint creation tool. Note that pressing **Esc** if no tool is active will exit sketch edit mode. Uncheck the **Esc can leave sketch edit mode** [preference](Sketcher_Preferences#General.md) if you often inadvertently press **Esc** too many times.

### Auto constraints 

In sketches that have **Auto constraints** checked (default) several constraints are applied automatically. The icon of a proposed automatic constraint is shown next to the cursor when it is placed correctly. Left-Clicking will then apply that constraint. This is a per-sketch setting that can be changed in the [Sketcher Dialog](Sketcher_Dialog#Constraints.md) or by changing the **Autoconstraints** [property](Property_editor.md) of the sketch.

The following constraints are applied automatically:

-   <img alt="" src=images/Sketcher_ConstrainCoincident.svg  style="width:16px;"> [Coincident](Sketcher_ConstrainCoincident.md)

-   <img alt="" src=images/Sketcher_ConstrainPointOnObject.svg  style="width:16px;"> [Point on object](Sketcher_ConstrainPointOnObject.md)

-   <img alt="" src=images/Sketcher_ConstrainHorizontal.svg  style="width:16px;"> [Horizontal](Sketcher_ConstrainHorizontal.md)

-   <img alt="" src=images/Sketcher_ConstrainVertical.svg  style="width:16px;"> [Vertical](Sketcher_ConstrainVertical.md)

-   <img alt="" src=images/Sketcher_ConstrainTangent.svg  style="width:16px;"> [Tangent](Sketcher_ConstrainTangent.md)

-    <small>(v1.0)</small> : <img alt="" src=images/Sketcher_ConstrainSymmetric.svg  style="width:16px;"> [Symmetric](Sketcher_ConstrainSymmetric.md) (line midpoint)

### Snapping


<small>(v0.21)</small> 

It is possible to [snap](Sketcher_Snap.md) to grid lines and grid intersection, to edges of geometry and midpoints of lines and arcs, and to certain angles. Please note that snapping does not produce constraints in and of itself. For example, only if [Auto constraints](#Auto_constraints.md) is switched on will snapping to an edge produce a [Point on object constraint](Sketcher_ConstrainPointOnObject.md). But just picking a point on the edge would then have the same result.

### On-View-Parameters 


<small>(v1.0)</small> 

Depending on the selected option in the [preferences](Sketcher_Preferences#General.md) only the dimensional On-View-Parameters or both the dimensional and the positional On-View-Parameters can be enabled. Positional parameters allow the input of exact coordinates, for example the center of a circle, or the start point of a line. Dimensional parameters allow the input of exact dimensions, for example the radius of a circle, or the length and angle of a line. On-View-Parameters are not available for all tools.

![](images/Sketcher_On_view_parameters_positional.png ) 
*Determining the center point of a circle with the positional parameters enabled*

![](images/Sketcher_On_view_parameters_dimensional.png ) 
*Determining the radius of a circle with the dimensional parameters enabled*

If values are entered and confirmed by pressing **Enter** or **Tab**, related constraints are added automatically. If two parameters are displayed at the same time, for example the X and Y coordinate of a point, it is possible to enter one value and pick a point to define the other. Depending on the object additional constraints may be required to fully constrain it. Constraints resulting from On-View-Parameters take precedence over those that may result from [Auto constraints](Sketcher_Dialog#Constraints.md).

<img alt="" src=images/Sketcher_ArcExample3.png  style="width:300px;"> 
*Arc created by entering all On-View-Parameters with resulting automatically created constraints*

### Coordinate display 

If the **Show coordinates beside cursor while editing** [preference](Sketcher_Preferences#Display.md) is checked (default), the parameters of the current geometry tool (coordinates, radius, or length and angle) are displayed next to the cursor. This is deactivated while On-View-Parameters are shown.



## Métodos de seleção 

While a sketch is in edit mode the following selection methods can be used:



### Seleção de elemento de visualização 3D 

As elsewhere in FreeCAD, an element can be selected in the [3D view](3D_view.md) with a single left mouse click. But there is no need to hold down the **Ctrl** key when selecting multiple elements. Holding down that key is possible though and has the advantage that you can miss-click without losing the selection. Edges, points and constraints can be selected in this manner.



### Seleção da caixa de visualização 3D 

Box selection in the 3D view works without using [Std BoxSelection](Std_BoxSelection.md) or [Std BoxElementSelection](Std_BoxElementSelection.md):

1.  Make sure that no tool is active.
2.  Do one of the following:
    -   Click in an empty area and drag a rectangle from left to right to select elements that lie completely inside the rectangle.
    -   Click in an empty area and drag a rectangle from right to left to also select elements that touch or cross the rectangle.

You can box-select edges and points, constraints cannot be box-selected.

### 3D view connected geometry selection 


<small>(v1.0)</small> 

Double-clicking an edge in the 3D view will select all edges directly and indirectly connected with that edge via endpoints. There is no need for the edges to be connected with [Coincident constraints](Sketcher_ConstrainCoincident.md), endpoints need only have the same coordinates.



### Seleção da caixa de diálogo do Sketcher 

Edges and points can also be selected from the Elements section of the [Sketcher Dialog](Sketcher_Dialog.md), and constraints from the Constraints section of that dialog.

## Copy, cut and paste 


<small>(v1.0)</small> 

The standard keyboard shortcuts, **Ctrl**+**C**, **Ctrl**+**X** and **Ctrl**+**V**, can be used to copy, cut and paste selected Sketcher geometry including related constraints. But these tools are also available from the **Sketch → Sketcher tools** menu. They can be used within the same sketch but also between different sketches or separate instances of FreeCAD. Since the data is copied to the clipboard in the form of Python code, it can be used in other ways too (e.g. shared on the forum).



## Ferramentas

As ferramentas do Sketcher Workbench estão localizadas no menu Sketch e/ou em várias barras de ferramentas. {{Version/pt-br|0.21}}: Quase todas as barras de ferramentas do Sketcher são exibidas apenas enquanto um esboço está no modo de edição. A única exceção é o [Barra de ferramentas do Sketcher](#Barra_de_ferramentas_do_Sketcher.md) que só é exibida se nenhum esboço estiver no modo de edição.

Some tools are also available from the [3D view](3D_view.md) context menu while a sketch is in edit mode, or from the context menus of the [Sketcher Dialog](Sketcher_Dialog.md).


{{Version/pt-br|0.21}}

: Se um esboço estiver no modo de edição, a barra de ferramentas Estrutura ficará oculta, pois nenhuma de suas ferramentas poderá ser usada.



### Gerais



#### Barra de ferramentas do Sketcher 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_NewSketch.svg‎‎  style="width:32px;"> [Criar um novo esboço](Sketcher_NewSketch/pt-br.md): Cria um novo esboço em uma face ou plano selecionado. Se nenhuma face estiver selecionada enquanto esta ferramenta é executada, o usuário é solicitado a selecionar um plano em uma janela pop-up.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_EditSketch.svg  style="width:32px;"> [Editar o esboço selecionado](Sketcher_EditSketch/pt-br.md): Abre a edição do esboço selecionado. Isso abrirá a [caixa de diálogo do Sketcher](Sketcher_Dialog/pt-br.md).


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_MapSketch.svg  style="width:32px;"> [Mapear um esboço para uma face](Sketcher_MapSketch/pt-br.md): Mapeia um esboço para a face previamente selecionada de um sólido.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ReorientSketch.svg  style="width:32px;"> [Reorientação](Sketcher_ReorientSketch/pt-br.md): Permite anexar o esboço a um dos planos principais.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ValidateSketch.svg  style="width:32px;"> [Validar](Sketcher_ValidateSketch/pt-br.md): Verifica a tolerância de diferentes pontos e as ajusta.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_MergeSketches.svg  style="width:32px;"> [Fundir](Sketcher_MergeSketches/pt-br.md): Mescla dois ou mais esboços.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_MirrorSketch.svg  style="width:32px;"> [Espelhar](Sketcher_MirrorSketch/pt-br.md): Espelha um esboço em relação ao eixo x, ao eixo y ou à origem.


</div>



#### Barra de ferramentas do Sketcher Modo de Edição 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_LeaveSketch.svg  style="width:32px;"> [Fechar a edição do esboço](Sketcher_LeaveSketch/pt-br.md): Sai do modo de edição do esboço.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ViewSketch.svg  style="width:32px;"> [Olhar perpendicularmente ao plano do esboço](Sketcher_ViewSketch/pt-br.md): Configura a vista do modelo como perpendicular ao plano do esboço.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ViewSection.svg  style="width:32px;"> [Alternar entre a seção e a exibição completa](Sketcher_ViewSection/pt-br.md): Cria um plano de seção que oculta temporariamente qualquer coisa na frente do plano do esboço.


</div>



#### Barra de ferramentas de edição do Sketcher 

-   <img alt="" src=images/Sketcher_Grid.svg  style="width:32px;"> [Toggle grid](Sketcher_Grid.md): Toggles the grid in the sketch currently being edited. Settings can be changed in the related menu. <small>(v0.21)</small> 

-   <img alt="" src=images/Sketcher_Snap.svg  style="width:32px;"> [Toggle snap](Sketcher_Snap.md): Toggles snapping in all sketches. Settings can be changed in the related menu. <small>(v0.21)</small> 

-   <img alt="" src=images/Sketcher_RenderingOrder.svg  style="width:32px;"> [Configure rendering order](Sketcher_RenderingOrder.md): The rendering order of all sketches can be changed in the related menu. <small>(v0.21)</small> 



#### Outros


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_StopOperation.svg  style="width:32px;"> [Parar a operação](Sketcher_StopOperation/pt-br.md): Quando no modo de edição, para a operação atual, seja desenho, configuração de restrições, etc.


</div>



### Geometrias do Sketcher 

Estas são ferramentas para criar objetos.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_CreatePoint.svg  style="width:32px;"> [Criar um ponto no esboço](Sketcher_CreatePoint/pt-br.md): Desenha um ponto.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_CreatePolyline.svg  style="width:32px;"> [Polilinha (linha de múltiplos pontos)](Sketcher_CreatePolyline/pt-br.md): Desenha uma linha composta de vários segmentos de linha. Pressionar a tecla M enquanto se desenha uma polilinha alterna entre os diferentes modos de polilinha.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_CreateLine.svg  style="width:32px;"> [Criar uma linha no esboço](Sketcher_CreateLine/pt-br.md): Desenha um segmento de reta entre 2 pontos. As linhas são infinitas em relação a certas restrições.


</div>

-   <img alt="" src=images/Sketcher_CreateArc.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Create arc:


<div class="mw-translate-fuzzy">

  - <img alt="" src=images/Sketcher_CreateArc.svg  style="width:32px;"> [Pontos de centro e extremidades](Sketcher_CreateArc/pt-br.md): Desenha um segmento de arco a partir do centro, raio, ângulo inicial e ângulo final.


</div>


<div class="mw-translate-fuzzy">

  - <img alt="" src=images/Sketcher_Create3PointArc.svg  style="width:32px;"> [Pontos de extremidade e ponto de borda](Sketcher_Create3PointArc/pt-br.md): Desenha um segmento de arco a partir dos dois pontos finais e outro ponto na circunferência.


</div>


<div class="mw-translate-fuzzy">

  - <img alt="" src=images/Sketcher_CreateArcOfEllipse.svg  style="width:32px;"> [Arco de elipse](Sketcher_CreateArcOfEllipse/pt-br.md): Desenha um arco de elipse pelo ponto central, ponto do raio maior, ponto inicial e ponto final.


</div>


<div class="mw-translate-fuzzy">

  -<img alt="" src=images/Sketcher_CreateArcOfHyperbola.svg  style="width:32px;"> [Arco de hipérbole](Sketcher_CreateArcOfHyperbola/pt-br.md): Desenha um arco de hipérbole.


</div>


<div class="mw-translate-fuzzy">

  -<img alt="" src=images/Sketcher_CreateArcOfParabola.svg  style="width:32px;"> [Arco de parábola](Sketcher_CreateArcOfParabola/pt-br.md): Desenha um arco de parábola.


</div>

-   <img alt="" src=images/Sketcher_CreateCircle.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Create circle/ellipse:


<div class="mw-translate-fuzzy">

  - <img alt="" src=images/Sketcher_CreateCircle.svg  style="width:32px;"> [Ponto de centro e borda](Sketcher_CreateCircle/pt-br.md): Desenha um círculo a partir do centro e do raio.


</div>


<div class="mw-translate-fuzzy">

  - <img alt="" src=images/Sketcher_Create3PointCircle.svg  style="width:32px;"> [3 pontos de borda](Sketcher_Create3PointCircle/pt-br.md): Desenha um círculo a partir de três pontos na circunferência.


</div>


<div class="mw-translate-fuzzy">

  - <img alt="" src=images/Sketcher_CreateEllipseByCenter.svg  style="width:32px;"> [Elipse centro](Sketcher_CreateEllipseByCenter/pt-br.md): Desenha uma elipse pelo ponto central, ponto do raio maior e ponto do raio menor.


</div>


<div class="mw-translate-fuzzy">

  - <img alt="" src=images/Sketcher_CreateEllipseBy3Points.svg  style="width:32px;"> [Elipse 3 pontos](Sketcher_CreateEllipseBy3Points/pt-br.md): Desenha uma elipse pelo diâmetro maior (2 pontos) e ponto do raio menor.


</div>

-   <img alt="" src=images/Sketcher_CreateRectangle.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Create rectangle:


<div class="mw-translate-fuzzy">

  - <img alt="" src=images/Sketcher_CreateRectangle.svg  style="width:32px;"> [Rectângulo](Sketcher_CreateRectangle/pt-br.md): Desenha um retângulo a partir de dois vértices opostos.


</div>


<div class="mw-translate-fuzzy">

  - <img alt="" src=images/Sketcher_CreateRectangle_Center.svg  style="width:32px;"> [Rectângulo Centrado](Sketcher_CreateRectangle_Center/pt-br.md): Desenha um retângulo a partir de um ponto central e de um ponto de borda. <small>(v0.20)</small> 


</div>


<div class="mw-translate-fuzzy">

  - <img alt="" src=images/Sketcher_CreateOblong.svg  style="width:32px;"> [Rectângulo Arredondado](Sketcher_CreateOblong/pt-br.md): Traça um retângulo arredondado a partir de 2 pontos opostos. <small>(v0.20)</small> 


</div>

-   <img alt="" src=images/Sketcher_CreateHexagon.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Create regular polygon:


<div class="mw-translate-fuzzy">

  - <img alt="" src=images/Sketcher_CreateTriangle.svg  style="width:32px;"> [Triangulo](Sketcher_CreateTriangle/pt-br.md): Desenha um triângulo regular inscrito em um círculo de geometria de construção.


</div>


<div class="mw-translate-fuzzy">

  - <img alt="" src=images/Sketcher_CreateSquare.svg  style="width:32px;"> [Quadrado](Sketcher_CreateSquare/pt-br.md): Desenha um quadrado regular inscrito em um círculo de geometria de construção.


</div>


<div class="mw-translate-fuzzy">

  - <img alt="" src=images/Sketcher_CreatePentagon.svg  style="width:32px;"> [Pentágono](Sketcher_CreatePentagon/pt-br.md): Desenha um pentágono regular inscrito em um círculo de geometria de construção.


</div>


<div class="mw-translate-fuzzy">

  - <img alt="" src=images/Sketcher_CreateHexagon.svg  style="width:32px;"> [Hexágono](Sketcher_CreateHexagon/pt-br.md): Desenha um hexágono regular inscrito em um círculo de geometria de construção.


</div>


<div class="mw-translate-fuzzy">

  - <img alt="" src=images/Sketcher_CreateHeptagon.svg  style="width:32px;"> [Heptágono](Sketcher_CreateHeptagon/pt-br.md): Desenha um heptágono regular inscrito em um círculo de geometria de construção.


</div>


<div class="mw-translate-fuzzy">

  - <img alt="" src=images/Sketcher_CreateOctagon.svg  style="width:32px;"> [Octágono](Sketcher_CreateOctagon/pt-br.md): Desenha um octógono regular inscrito em um círculo de geometria de construção.


</div>


<div class="mw-translate-fuzzy">

  - <img alt="" src=images/Sketcher_CreateRegularPolygon.svg  style="width:32px;"> [Criar Polígono Regular](Sketcher_CreateRegularPolygon/pt-br.md) : Desenha um polígono regular selecionando o número de lados e escolhendo dois pontos: o centro e um canto.


</div>

-   <img alt="" src=images/Sketcher_CreateSlot.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Create slot:


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_CreateSlot.svg  style="width:32px;"> [Oblongo](Sketcher_CreateSlot/pt-br.md): Desenha uma forma oval selecionando o centro de um semicírculo e a extremidade do outro semicírculo.


</div>

  - <img alt="" src=images/Sketcher_CreateArcSlot.svg  style="width:32px;"> [Arc slot](Sketcher_CreateArcSlot.md): Creates an arc slot. <small>(v1.0)</small> 

-   <img alt="" src=images/Sketcher_CreateBSpline.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Create B-spline:


<div class="mw-translate-fuzzy">

\*: <img alt="" src=images/Sketcher_CreateBSpline.svg  style="width:32px;"> [Criar B-spline](Sketcher_CreateBSpline/pt-br.md): Desenha uma curva B-spline por seus pontos de controle.


</div>

\*: <img alt="" src=images/Sketcher_CreatePeriodicBSpline.svg  style="width:32px;"> [Criar B-spline periódica](Sketcher_CreatePeriodicBSpline/pt-br.md): Cria uma curva B-spline periódica (fechada) por pontos de controle.<small>(v1.0)</small> : Esta é a mesma ferramenta que [B-spline por pontos de controle](Sketcher_CreateBSpline/pt-br.md), mas com um modo inicial diferente.

  - <img alt="" src=images/Sketcher_CreateBSplineByInterpolation.svg  style="width:32px;"> [B-spline by knots](Sketcher_CreateBSplineByInterpolation.md): Creates a B-spline curve by knot points. Idem.

  - <img alt="" src=images/Sketcher_CreatePeriodicBSplineByInterpolation.svg  style="width:32px;"> [Periodic B-spline by knots](Sketcher_CreatePeriodicBSplineByInterpolation.md): Creates a periodic (closed) B-spline curve by knot points. Idem.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ToggleConstruction.svg  style="width:32px;"> [Modo de construção](Sketcher_ToggleConstruction/pt-br.md): Alterna a geometria do esboço de/para o modo de construção. A geometria de construção é mostrada em azul e é descartada fora do modo de edição do esboço.


</div>



### Restrições do Sketcher 


<div class="mw-translate-fuzzy">

As restrições são usadas para definir comprimentos, definir regras entre os elementos do esboço e para bloquear o esboço ao longo dos eixos vertical e horizontal. Algumas restrições requerem o uso de [Restrições de ajuda](Sketcher_helper_constraint/pt-br.md).


</div>

-   <img alt="" src=images/Sketcher_Dimension.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Dimensional constraints:

  - <img alt="" src=images/Sketcher_Dimension.svg  style="width:32px;"> [Dimension](Sketcher_Dimension.md): Is the context-sensitive constraint tool of the Sketcher Workbench. Based on the current selection, it offers appropriate dimensional constraints, but also geometric constraints. <small>(v1.0)</small> 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ConstrainDistanceX.svg  style="width:32px;"> [Distancia Horizontal](Sketcher_ConstrainDistanceX/pt-br.md): Fixa a distância horizontal entre dois pontos quaisquer, ou pontos extremos de uma linha. Se apenas um item for selecionado, a distância é definida para a origem.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ConstrainDistanceY.svg  style="width:32px;"> [Distancia Vertical](Sketcher_ConstrainDistanceY/pt-br.md): Fixa a distância vertical entre dois pontos quaisquer, ou pontos extremos de uma linha. Se apenas um item for selecionado, a distância é definida para a origem.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ConstrainDistance.svg  style="width:32px;"> [Distancia](Sketcher_ConstrainDistance/pt-br.md): Define o comprimento de uma linha, a distância perpendicular entre um ponto e uma linha, a distância entre dois pontos, ou, <small>(v0.21)</small> , a distância entre as arestas de dois círculos.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ConstrainRadiam.svg  style="width:32px;"> [Radiano](Sketcher_ConstrainRadiam/pt-br.md): Define o raio de um arco, o diâmetro de um círculo ou o peso de um pólo B-spline.<small>(v0.20)</small> 


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ConstrainRadius.svg  style="width:32px;"> [Raio ou peso](Sketcher_ConstrainRadius/pt-br.md): Define o raio de um arco ou círculo ou o peso de um pólo B-spline.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ConstrainDiameter.svg  style="width:32px;"> [Diâmetro](Sketcher_ConstrainDiameter/pt-br.md): Define o diâmetro de um arco ou círculo.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ConstrainAngle.svg  style="width:32px;"> [Angulo](Sketcher_ConstrainAngle/pt-br.md): Define o ângulo interno entre duas linhas selecionadas.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ConstrainLock.svg  style="width:32px;"> [Restringir](Sketcher_ConstrainLock/pt-br.md): Restringe o item selecionado definindo distâncias verticais e horizontais em relação à origem, travando assim a localização desse item. Essas distâncias podem ser editadas posteriormente.


</div>

-   <img alt="" src=images/Sketcher_ConstrainCoincidentUnified.svg  style="width:32px;"> [Coincident (unified)](Sketcher_ConstrainCoincidentUnified.md): Creates a coincident constraint between points, fixes points on edges or axes, or creates a concentric constraint. It combines the [Coincident](Sketcher_ConstrainCoincident.md) and [Point on object](Sketcher_ConstrainPointOnObject.md) tools. <small>(v1.0)</small> 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ConstrainCoincident.svg  style="width:32px;"> [Coincidente](Sketcher_ConstrainCoincident/pt-br.md): Afixa um ponto em (coincidente com) um ou mais outros pontos. Atua como uma restrição concêntrica se dois ou mais círculos, arcos, elipses ou arcos de elipses forem selecionados.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ConstrainPointOnObject.svg  style="width:32px;"> [Ponto sobre o objeto](Sketcher_ConstrainPointOnObject/pt-br.md): Afixa um ponto em outro objeto, como uma linha, arco ou eixo.


</div>

-   <img alt="" src=images/Sketcher_ConstrainHorVer.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;">Horizontal/vertical constraints:

  - <img alt="" src=images/Sketcher_ConstrainHorVer.svg  style="width:32px;"> [Horizontal/vertical](Sketcher_ConstrainHorVer.md): Constrains lines or pairs of points to be horizontal or vertical, whichever is closest to the current alignment. It combines the [Horizontal](Sketcher_ConstrainHorizontal.md) and [Vertical](Sketcher_ConstrainVertical.md) tools. <small>(v1.0)</small> 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ConstrainHorizontal.svg  style="width:32px;"> [Horizontal](Sketcher_ConstrainHorizontal/pt-br.md): Restringe as linhas selecionadas ou elementos de polilinha a uma orientação horizontal verdadeira. Mais de um objeto pode ser selecionado antes de aplicar esta restrição.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ConstrainVertical.svg  style="width:32px;"> [Vertical](Sketcher_ConstrainVertical/pt-br.md): Restringe as linhas selecionadas ou elementos de polilinha a uma orientação vertical verdadeira. Mais de um objeto pode ser selecionado antes de aplicar esta restrição.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ConstrainParallel.svg  style="width:32px;"> [Paralela](Sketcher_ConstrainParallel/pt-br.md): Restringe duas ou mais linhas, fazendo-as paralelas entre si.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ConstrainPerpendicular.svg  style="width:32px;"> [Perpendicular](Sketcher_ConstrainPerpendicular/pt-br.md): Restringe duas linhas, fazendo-as perpendiculares uma à outra, ou restringe uma linha perpendicular à extremidade de um arco.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ConstrainTangent.svg  style="width:32px;"> [Tangente](Sketcher_ConstrainTangent/pt-br.md): Cria uma restrição tangente entre duas entidades selecionadas ou uma restrição colinear entre dois segmentos de linha. Um segmento de linha não precisa estar diretamente sobre um arco ou círculo para ser restrito tangente a esse arco ou círculo.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ConstrainEqual.svg  style="width:32px;"> [Iguadade](Sketcher_ConstrainEqual/pt-br.md): Restringe duas entidades selecionadas, fazendo-as iguais uma à outra. Se usado em círculos ou arcos, seus raios resultarão iguais.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ConstrainSymmetric.svg  style="width:32px;"> [Simetria](Sketcher_ConstrainSymmetric/pt-br.md): Restringe dois pontos simetricamente em relação a uma linha, ou restringe os dois primeiros pontos selecionados simetricamente em relação a um terceiro ponto selecionado.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ConstrainBlock.svg  style="width:32px;"> [Bloquear](Sketcher_ConstrainBlock/pt-br.md): Impede que uma aresta se mova, ou seja, impede que seus vértices mudem suas posições atuais. Deve ser particularmente útil para corrigir a posição de B-Splines. Veja o tópico [Block Constraint](https://forum.freecadweb.org/viewtopic.php?f=9&t=26572) no fórum.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ConstrainSnellsLaw.svg  style="width:32px;"> [A Lei de Snell](Sketcher_ConstrainSnellsLaw/pt-br.md): Restringe duas linhas à obediência a uma lei de refração, para simular a luz que passa por uma interface.


</div>

-   <img alt="" src=images/Sketcher_ToggleDrivingConstraint.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Toggle constraints:


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ToggleDrivingConstraint.svg  style="width:32px;"> [Alternar restrição de direção/referência](Sketcher_ToggleDrivingConstraint/pt-br.md): Alterna a barra de ferramentas ou as restrições selecionadas de/para o modo de referência.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ToggleActiveConstraint.svg  style="width:32px;"> [Ativar/Desativar restrição](Sketcher_ToggleActiveConstraint/pt-br.md): Habilita ou desabilita uma restrição já colocada. <small>(v0.19)</small> 


</div>



### Ferramentas do Sketcher 

-   <img alt="" src=images/Sketcher_CreateFillet.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Create fillet/chamfer:


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_CreateFillet.svg  style="width:32px;"> [Filete](Sketcher_CreateFillet/pt-br.md): Faz um filete entre duas linhas unidas em um ponto. Selecione as duas linhas ou clique no ponto de canto e ative a ferramenta.


</div>

  - <img alt="" src=images/Sketcher_CreateChamfer.svg  style="width:32px;"> [Chamfer](Sketcher_CreateChamfer.md): creates a chamfer between two non-parallel edges. This is the same tool as [Fillet](Sketcher_CreateFillet.md) but with a different initial mode. <small>(v1.0)</small> 

-   <img alt="" src=images/Sketcher_Trimming.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Edit edge:


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_Trimming.svg  style="width:32px;"> [Ajustar](Sketcher_Trimming/pt-br.md): Corta uma linha, círculo ou arco em relação ao ponto clicado.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_Split.svg  style="width:32px;"> [Dividir](Sketcher_Split/pt-br.md): Divide uma linha ou um arco em dois, converte um círculo em um arco, mantendo a maior parte das restrições. <small>(v0.20)</small> 


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_Extend.svg  style="width:32px;"> [Ampliar](Sketcher_Extend/pt-br.md): Estende uma linha ou um arco a uma linha limite, arco, elipse, arco de elipse ou um ponto no espaço.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_External.svg  style="width:32px;"> [Geometria externa](Sketcher_External/pt-br.md): Cria uma aresta vinculada à geometria externa.


</div>

-   <img alt="" src=images/Sketcher_Projection.svg  style="width:32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> External geometry:

  - <img alt="" src=images/Sketcher_Projection.svg  style="width:32px;"> [Create external projection geometry](Sketcher_Projection.md): Creates the projection edges of external geometry. <small>(v1.1)</small> 

  - <img alt="" src=images/Sketcher_Intersection.svg  style="width:32px;"> [Create external intersection geometry](Sketcher_Intersection.md): Creates the intersection edges of external geometry with the sketch plane. <small>(v1.1)</small> 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_CarbonCopy.svg  style="width:32px;"> [Cópia em carbono](Sketcher_CarbonCopy/pt-br.md): Copia a geometria de outro esboço.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_SelectOrigin.svg  style="width:32px;"> [Selecionar Origem](Sketcher_SelectOrigin/pt-br.md): Seleciona a origem de um esboço.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_SelectHorizontalAxis.svg  style="width:32px;"> [Selecionar Eixo Horizontal](Sketcher_SelectHorizontalAxis/pt-br.md): Seleciona o eixo horizontal de um esboço.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_SelectVerticalAxis.svg  style="width:32px;"> [Selecionar Eixo Vertical](Sketcher_SelectVerticalAxis/pt-br.md): Seleciona o eixo vertical de um esboço.


</div>

-   <img alt="" src=images/Sketcher_Translate.svg  style="width:32px;"> [Array transform](Sketcher_Translate.md): Moves or optionally creates copies of selected elements. <small>(v1.0)</small> 

-   <img alt="" src=images/Sketcher_Rotate.svg  style="width:32px;"> [Polar transform](Sketcher_Rotate.md): Rotates or optionally creates rotated copies of selected elements. <small>(v1.0)</small> 

-   <img alt="" src=images/Sketcher_Scale.svg  style="width:32px;"> [Scale transform](Sketcher_Scale.md): Scales or optionally creates scaled copies of selected elements. <small>(v1.0)</small> 

-   <img alt="" src=images/Sketcher_Offset.svg  style="width:32px;"> [Offset geometry](Sketcher_Offset.md): Creates equidistant edges around selected edges. <small>(v1.0)</small> 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_Symmetry.svg  style="width:32px;"> [Simetria](Sketcher_Symmetry/pt-br.md): Copia um elemento do sketcher simétrico a uma linha escolhida.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_RemoveAxesAlignment.svg  style="width:32px;"> [Retirar o alinhamento dos eixos](Sketcher_RemoveAxesAlignment/pt-br.md): Remover o alinhamento dos eixos enquanto tenta preservar a relação de restrição da seleção <small>(v0.20)</small> 


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_DeleteAllGeometry.svg  style="width:32px;"> [Eliminar toda a geometria](Sketcher_DeleteAllGeometry/pt-br.md): Deleta todas as geometrias do esboço.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_DeleteAllConstraints.svg  style="width:32px;"> [Eliminar todas as restrições](Sketcher_DeleteAllConstraints/pt-br.md): Deleta todas as restrições do esboço.


</div>

-   <img alt="" src=images/Edit-copy.svg  style="width:32px;"> Copy in Sketcher: See [Copy, cut and paste](#Copy,_cut_and_paste.md).

-   <img alt="" src=images/Edit-cut.svg  style="width:32px;"> Cut in Sketcher: See [Copy, cut and paste](#Copy,_cut_and_paste.md).

-   <img alt="" src=images/Edit-paste.svg  style="width:32px;"> Paste in Sketcher: See [Copy, cut and paste](#Copy,_cut_and_paste.md).



### Ferramentas de B-spline do Sketcher 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_BSplineApproximate.svg  style="width:32px;"> [Converte geometria para B-spline](Sketcher_BSplineApproximate/pt-br.md)


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_BSplineIncreaseDegree.svg  style="width:32px;"> [Aumenta o grau da B-spline](Sketcher_BSplineIncreaseDegree/pt-br.md)


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_BSplineDecreaseDegree.svg  style="width:32px;"> [Diminui o grau da B-spline](Sketcher_BSplineDecreaseDegree/pt-br.md), <small>(v0.19)</small> 


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_BSplineIncreaseKnotMultiplicity.svg  style="width:32px;"> [Aumenta a multiplicidade do nó](Sketcher_BSplineIncreaseKnotMultiplicity/pt-br.md)


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_BSplineDecreaseKnotMultiplicity.svg  style="width:32px;"> [Diminui a multiplicidade do nó](Sketcher_BSplineDecreaseKnotMultiplicity/pt-br.md)


</div>

-   <img alt="" src=images/Sketcher_BSplineInsertKnot.svg  style="width:32px;"> [Insert knot](Sketcher_BSplineInsertKnot.md): Inserts a knot into a B-spline or increases the multiplicity of an existing knot.

-   <img alt="" src=images/Sketcher_JoinCurves.svg  style="width:32px;"> [Join curves](Sketcher_JoinCurves.md): Creates a B-spline by joining two existing B-splines or other edges. <small>(v0.21)</small> 

### Sketcher visual 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_SelectElementsWithDoFs.svg  style="width:32px;"> [ Exibindo os graus de liberdade](Sketcher_SelectElementsWithDoFs/pt-br.md): Destaca em verde a geometria com graus de liberdade (GDLs), isto é, não toalmente restrita.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_SelectConstraints.svg  style="width:32px;"> [Selecione Restrições](Sketcher_SelectConstraints/pt-br.md): Seleciona as restrições de um elemento do Sketcher.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_SelectElementsAssociatedWithConstraints.svg  style="width:32px;"> [Selecione Elementos Associados a Restrições](Sketcher_SelectElementsAssociatedWithConstraints/pt-br.md): Seleciona elementos do Sketcher associados com restrições.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_SelectRedundantConstraints.svg  style="width:32px;"> [Selecione Restrições Redundantes](Sketcher_SelectRedundantConstraints/pt-br.md): Seleciona restrições redundantes de um esboço.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_SelectConflictingConstraints.svg  style="width:32px;"> [Selecione Restrições Conflitantes](Sketcher_SelectConflictingConstraints/pt-br.md): Seleciona restrições conflitantes de um esboço.


</div>

-   <img alt="" src=images/Sketcher_ArcOverlay.svg  style="width:32px;"> [Show/hide circular helper for arcs](Sketcher_ArcOverlay.md): Shows or hides the circular helpers (underlying virtual circles) for arcs in all sketches. <small>(v1.0)</small> 

-   <img alt="" src=images/Sketcher_BSplinePolygon.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Show/hide B-spline information layer:


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_BSplineDegree.svg  style="width:32px;"> [Mostra/esconde o grau da B-spline](Sketcher_BSplineDegree/pt-br.md)


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_BSplinePolygon.svg  style="width:32px;"> [Mostra/esconde o polígono de controle da B-spline](Sketcher_BSplinePolygon/pt-br.md)


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_BSplineComb.svg  style="width:32px;"> [Mostra/esconde o pente de curvatura da B-spline](Sketcher_BSplineComb/pt-br.md)


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_BSplineKnotMultiplicity.svg  style="width:32px;"> [Mostra/esconde o nó de multiplicidade da B-spline](Sketcher_BSplineKnotMultiplicity/pt-br.md)


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_BSplinePoleWeight.svg  style="width:32px;"> [Mostra/esconde o peso dos pontos de controle da B-spline](Sketcher_BSplinePoleWeight/pt-br.md), <small>(v0.19)</small> 


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_RestoreInternalAlignmentGeometry.svg  style="width:32px;"> [Mostrar/ocultar geometria interna](Sketcher_RestoreInternalAlignmentGeometry/pt-br.md): Recria o que falta ou deleta geometria interna desnecessária em uma elipse, arco de elipse, hipérbole, parábola ou B-spline.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_SwitchVirtualSpace.svg  style="width:32px;"> [Trocar espaço virtual](Sketcher_SwitchVirtualSpace/pt-br.md): Permite esconder todas as restrições de um esboço e fazê-las visíveis novamente.


</div>



### Ferramentas obsoletas 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_Clone.svg  style="width:32px;"> [Clonar](Sketcher_Clone/pt-br.md): Clona um elemento do Sketcher.


</div>

-   <img alt="" src=images/Sketcher_CloseShape.svg  style="width:32px;"> [Forma fechada](Sketcher_CloseShape/pt-br.md): Cria uma forma fechada aplicando restrições coincidentes a exremidades. Não disponível em <small>(v0.21)</small> .

-   <img alt="" src=images/Sketcher_CreatePointFillet.svg  style="width:32px;"> [Corner-preserving fillet](Sketcher_CreatePointFillet.md): Creates a fillet between two non-parallel lines while preserving their corner point. Not available in <small>(v1.0)</small> .


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ConnectLines.svg  style="width:32px;"> [Conectar bordas](Sketcher_ConnectLines/pt-br.md): Conecta elementos do Sketcher aplicando restrições de coincidência nas extremidades. Não disponível em <small>(v0.21)</small> .


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_Copy.svg  style="width:32px;"> [Copiar](Sketcher_Copy/pt-br.md): Copia um elemento do Sketcher.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_Move.svg  style="width:32px;"> [Mover](Sketcher_Move/pt-br.md): Move a geometria selecionada tomando como referência o último ponto selecionado.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_RectangularArray.svg  style="width:32px;"> [Matriz Retangular](Sketcher_RectangularArray/pt-br.md): Cria uma matriz de elementos do Sketcher selecionados.


</div>



## Preferências


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Workbench_Sketcher.svg  style="width:32px;"> [Preferências](Sketcher_Preferences/pt-br.md): Preferências para a bancada de trabalho **Sketcher**.


</div>




<div class="mw-translate-fuzzy">

## Boas Práticas 


</div>


<div class="mw-translate-fuzzy">

Cada usuário CAD desenvolve sua própria maneira de trabalhar ao longo do tempo, mas existem alguns princípios gerais úteis a seguir.


</div>


<div class="mw-translate-fuzzy">

-   Uma série de esboços simples é mais fácil de gerenciar do que um único e complexo. Por exemplo, um primeiro esboço pode ser criado para o recurso 3D base (um "pad" ou um "revolve"), enquanto um segundo pode conter furos ou recortes ("pockets"). Alguns detalhes podem ser omitidos, para serem adicionados posteriormente como elementos 3D. Você pode escolher evitar filetes em seu esboço se houver muitos e adicioná-los como um elemento 3D.
-   Sempre crie um perfil fechado, ou seu esboço não produzirá um sólido, mas sim um conjunto de faces abertas. Se você não quiser que alguns dos objetos sejam incluídos na criação do sólido, transforme-os em elementos de construção com a ferramenta Construction Mode.
-   Use o recurso de restrições automáticas para limitar o número de restrições que você terá que adicionar manualmente.
-   Como regra geral, aplique primeiro as restrições geométricas, depois as restrições dimensionais e bloqueie o esboço por último. Mas lembre-se: as regras são feitas para serem quebradas. Se você estiver tendo problemas para manipular seu esboço, pode ser útil restringir alguns objetos antes de completar seu perfil.
-   Se possível, centralize seu esboço na origem (0,0) com a restrição de bloqueio (\"Lock\"). Se o seu esboço não for simétrico, localize um de seus pontos na origem ou escolha bons números redondos para as distâncias de bloqueio -- Uma restrição de bloqueio de (25,75) da origem é mais facilmente lembrada do que (23,47 , 73,02). Na v0.12, as restrições externas (restringindo o esboço à geometria 3D existente, como arestas ou outros esboços) não estão implementadas. Isso significa que, para localizar a geometria de esboços subsequentes em seu primeiro esboço, você precisará definir manualmente as distâncias relativas ao primeiro esboço.
-   Se você tiver a possibilidade de escolher entre a restrição Length e as restrições de distância Horizontal Distance ou Vertical Distance, prefira as últimas. Elas consomem menos recursos computacionais.
-   Em geral, as melhores restrições a serem usadas são: Restrições horizontais e verticais; restrições de comprimento horizontal e vertical; tangência ponto a ponto. Se possível, limite o uso destes: a restrição geral de comprimento; tangência borda a borda; restrição de fixar o ponto em uma linha; restrição de simetria.
-   Se estiver em dúvida sobre a validade de um esboço depois de concluído (os elementos ficam verdes), feche a caixa de diálogo do Sketcher, mude para a <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Bancada de trabalho Part](Part_Workbench/pt-br.md) e execute **[<img src=images/Part_CheckGeometry.svg style="width:16px"> [Verificar geometria](Part_CheckGeometry/pt-br.md)**.


</div>



## Tutoriais


<div class="mw-translate-fuzzy">

-   [Sketcher tutorial](https://forum.freecadweb.org/viewtopic.php?f=36&t=30104) por chrisb. Este é um documento PDF de 70 páginas que serve como um manual detalhado para o desenhista. Ele explica os fundamentos do uso do Sketcher e dá muitos detalhes sobre a criação de formas geométricas e cada uma das restrições.
-   [Tutorial Básico de Sketcher](Basic_Sketcher_Tutorial/pt-br.md) para iniciantes.
-   [Sketcher Micro Tutorial - Práticas de Restrição](Sketcher_Micro_Tutorial_-_Constraint_Practices/pt-br.md).
-   [Requisitos de esboço para um esboço](Sketcher_requirement_for_a_sketch/pt-br.md) Requisito Mínimo para um Esboço e Determinação Completa de um Esboço.


</div>

## Scripting

A página [Sketcher scripting](Sketcher_scripting/pt-br.md) contém exemplos de como criar restrições a partir de scripts Python.



## Exemplos

For some ideas of what can be achieved with Sketcher tools, have a look at: [Sketcher examples](Sketcher_Examples.md).

<img alt="" src=images/Sketcher_ExampleHinge-01.gif  style="width:80px;"> <img alt="" src=images/Sketcher_ExampleHinge-15.png  style="width:90px;">



---
⏵ [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > [Sketcher](Category_Sketcher.md) > Sketcher Workbench/pt-br
