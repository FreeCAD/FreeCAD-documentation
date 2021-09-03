


<div class="mw-translate-fuzzy">


{{TutorialInfo/pt
|Topic= Rascunho
|Level= Principiante
|Time= 20 minutos
|Author=[http://freecadweb.org/wiki/index.php?title=User:Drei Drei]
|FCVersion=0.16 or above
|Files=
}}


</div>


<div class="mw-translate-fuzzy">

### Introduction

Este tutorial destina-se a introduzir o leitor ao fluxo de trabalho básico da [ Bancada Rascunho](Draft_Workbench/pt.md), que inclui a criação de perfis, o uso de planos de trabalho, bem como a criação de dimensões, texto e anotações. Este tutorial usa a notação \'\' \'(X, Y, Z)\' \'\' para denotar as coordenadas necessários para definir os pontos de um objecto.


</div>

This tutorial was originally written by Drei, and it was rewritten and illustrated by vocx.

This tutorial is meant to introduce the reader to the basic workflow of the <img alt="" src=images/Workbench_Draft.svg  style="width:24px;"> [Draft Workbench](Draft_Workbench.md).

The reader will practice:

-   creation of lines, arcs, and polygons
-   the use of working planes
-   the creation of dimensions, text, and shapestrings
-   the creation of a technical drawing

This tutorial uses the notation {{Value|(x, y, z)}} to denote the coordinates required to define points in an object. The default unit is millimeters {{Value|mm}}.

<img alt="" src=images/00_Dr01_Draft_Tutorial_final.png  style="width:" height="400px;"> 
*Final drawing including various Draft objects.*


<div class="mw-translate-fuzzy">

### Requirements

-   FreeCAD versão 0.16 ou superior
-   O leitor sabe como usar as pestanas \'\' \'Dados\' \'\' e \'\'Vistas \'\' para alterar as propriedades de um elemento se desejar


</div>

1\. Open FreeCAD, create a new empty document with **File → <img src=images/Std_New.svg style="width:16px"> [New](Std_New.md)**.

:   1.1. Switch to the <img src=images/Workbench_Draft.svg style="width:Draft Workbench](Draft_Workbench.md) from the [workbench selector](Std_Workbench.md), or the menu **View → Workbench → [16px"> Draft**.
:   1.2. Make sure you understand how to use the [property editor](property_editor.md), particularly the **Data** and **View** tabs to change the properties. When changing properties, you may have to do a **<img src="images/Std_Refresh.svg" width=16px> [Std Refresh](Std_Refresh.md)** action to see the result in the [3D view](3D_view.md).
:   1.3. Since the Draft objects are planar shapes, they are better viewed from the top. Use **<img src=images/Std_ViewTop.svg style="width:16px"> [View top](Std_ViewTop.md)** to set the [3D view](3D_view.md).
:   1.4. Although it is not used in this tutorial, the Draft grid is helpful to position geometrical elements. Use **<img src=images/Draft_SelectPlane.svg style="width:16px"> <img src=images/Draft_ToggleGrid.svg style="width:SelectPlane](Draft_SelectPlane.md)** to set both the working plane and the grid, and then show and hide the grid with **[16px"> [Toggle grid](Draft_ToggleGrid.md)**.


<div class="mw-translate-fuzzy">

### Procedimento

É obrigatório garantir que a \'\'barra de ferramentas Rascunho\" esteja disponível para usar este tutorial.


</div>


<div class="mw-translate-fuzzy">

1.  Iniciar *FreeCAD*
2.  Se você não tiver aberto um documento novo FreeCAD (a maioria da janela do FreeCAD parece cinzenta-out), a partir do menu, clique em Arquivo \> Novo ou clique no botão Criar uma nova Documento ![ 32px](images/Document-new.svg ).
3.  Ative o \'\' \'Projecto Workbench\' \'\'
4.  Selecione o menu \'\' \'Edit\' \'\'
5.  Clique em \'\' \'Preferências\' \'\'
6.  Ir para \'\' \'Draft\' \'\' e selecione o \'\' \'Grid e encaixando\' \'guia\'
7.  Verifique se o \'\' \'Show Projecto snap barra de ferramentas\' \'\' está ativa


</div>


<div class="mw-translate-fuzzy">

Note que você pode alterar a visibilidade da **Grelha** neste menu, no caso de você querer desactivá-la.


</div>


<div class="mw-translate-fuzzy">

#### Usando Planos 

Os planos são usados para restringir o comportamento das ferramentas Rascunho para um plano específico, evitando-se problemas com a localização de pontos e curvas em peças complexas. Os planos podem referenciar os eixos do sistema de coordenadas **(XY, YZ, \...)**, ou podem utilizar uma superfície plana no documento como referência.


</div>

Most Draft objects are planar shapes so they are naturally based on a **working plane**. A working plane can be one of the main XY, XZ, and YZ global coordinate planes, or it can be a plane that is parallel to them with a positive or negative offset, or it can be a plane defined by the face of a solid object.


<div class="mw-translate-fuzzy">

1.  Seleccione ![ 32px](images/Draft_SelectPlane.png ) [ Definir plano de trabalho](Draft_SelectPlane.md). Pode se localizar dentro das \'ferramentas da Bancada Rascunho\" ou dentro do \'\' Menu Rascunho \'\' na \'\' \'\' divisão \'Utilities\'.
2.  Selec o plano **XY**


</div>

Before pressing the button, you can also change the value of the offset in millimeters, as well as the grid spacing, the main lines and snapping radius.


<div class="mw-translate-fuzzy">

##### Linhas e arcos 

1.  Seleccione ![](images/Draft_Arc.png ) [Arco](Draft_Arc.md).
2.  Defina o \'\' centro\'\' em \'\' \'(0, 0, 0)\' \'\'
3.  Defina o \"raio\" a 30 mm
4.  O \"Ângulo inicial\" é 60,0 °
5.  A abertura é 60,0 °


</div>


<div class="mw-translate-fuzzy">

Repetir o mesmo procedimento para um segundo arco com um raio de 25 mm, as outras propriedades permanecem inalteradas.


</div>


<div class="mw-translate-fuzzy">

1.  Seleccione ![](images/Draft_Line.png ) [ Linha](Draft_Line.md).
2.  Aproxime-se do \'\' \'Endpoint\' \'\' de qualquer arco. Um ponto branco deverá aparecer, paralelamente a este ícone ![ 32px](images/Snap_Endpoint.png ) quando o cursor se aproxima do ponto de extremidade.
3.  Selecione o ponto final do outro arco.
4.  Repetir para o outro lado dos arcos.


</div>

<img alt="" src=images/01_Dr01_Draft_Arc_profile.png  style="width:" height="400px;"> 
*Closed profile created by two arcs and two lines.*

## Fusing or compounding 


<div class="mw-translate-fuzzy">

Temos agora várias curvas que detalham um perfil, no entanto, ainda não é reconhecido como uma entidade única. É possível continuar a trabalhar com os elementos intactos, embora, neste caso, vamos fundi-las em um único objeto.


</div>


<div class="mw-translate-fuzzy">

1.  Selecione um arco e uma linha enquanto pressiona a \'\' \'CTRL\' \'\' chave
2.  Clique em ![](images/Draft_Upgrade.png ) [ Atualizar](Draft_Upgrade.md)


</div>

6b. If you wish to maintain the parametric nature of the objects you can create a compound instead.

:   6b.1. Switch to the <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Part Workbench](Part_Workbench.md).
:   6b.2. With these objects selected, click on **<img src=images/Part_Compound.svg style="width:16px"> [Part Compound](Part_Compound.md)**.


<div class="mw-translate-fuzzy">

##### Planes, retângulos e círculos 

1.  Clique ![](images/Draft_Rectangle.png ) [ Retângulo](Draft_Rectangle.md)
2.  Defina o primeiro ponto \'\' \'(-100, -60, 0)\' \'\'
3.  Defina o segundo ponto sobre o \'\' \'(140, 90, 0)\' \'\'


</div>

7\. We will draw a rectangular frame. (Switch back to the <img alt="" src=images/Workbench_Draft.svg  style="width:24px;"> [ Draft Workbench](Draft_Workbench.md).)

:   7.1. Press **<img src=images/Draft_Rectangle.svg style="width:16px"> [Rectangle](Draft_Rectangle.md)**.
:   7.2. Enter the values of the first point {{Value|(-100, -60, 0)}}, and press **Enter**.
:   7.3. Make sure the **Relative** option is unchecked, as we will use absolute units. You may press **R** in the keyboard to quickly toggle this option on and off.
:   7.4. Enter the values for the second point {{Value|(140, 90, 0)}}, and press **Enter**.


<div class="mw-translate-fuzzy">

O resultado é um \'\' \'Plano\' \'\'. Suas propriedades podem ser modificados para remover o \'\' \'preenchimento\' \'\', alterando a sua \'\' \'Modo de exibição\' \'\' para \'\' \'Wireframe\' \'\'.


</div>


<div class="mw-translate-fuzzy">

1.  Seleccione ![](images/Draft_Circle.png )
2.  Defina o centro para \'\' \'(0, 0, 0)\' \'\'
3.  Defina o raio para 15 mm


</div>


<div class="mw-translate-fuzzy">

##### Polígonos

1.  Seleccione ![](images/Draft_Polygon.png ) [ Polígono](Draft_Polygon.md)
2.  O ponto de centro está localizado na \'\' \'(0, 0, 0)\' \'\'
3.  Defina o raio para 50 mm
4.  Defina o número de lados para 6


</div>

Again, you may change the **Make Face** and **Display Mode** properties in the [property editor](property_editor.md) if you want.

The rectangle, the circle, the polygon, and most other objects created with the [Draft Workbench](Draft_Workbench.md) share many data and view properties because they are derived from the same base class, [Part Part2DObject](Part_Part2DObject.md).

<img alt="" src=images/02_Dr01_Draft_Rectangle_circle_polygon.png  style="width:" height="400px;"> 
*Rectangle, circle and polygon added.*


<div class="mw-translate-fuzzy">

##### Arrays

As matrizes são usadas para replicar um objecto várias vezes numa direcção, um eixo de revolução ou ao longo de um caminho.

1.  Selecione o \'fio\' \'\' \'\' que foi criado anteriormente
2.  Clique ![ 32px](images/Draft_Array.png ) [ matriz](Draft_Array.md)
3.  Na aba \'\' \'\' dados \'\' do objeto, altere o tipo de matriz de \'\' \'orto\' \'\' para \'\' \'polar\' \'\'
4.  Mudança \'\' \'Número Polar\' \'\' 1-3


</div>

Arrays are used to replicate an object several times in an orthogonal direction (X, Y, Z), around a revolution axis, or along a path.

10\. We will create a polar array.

:   10.1. Select the {{Value|Wire}} object that was previously created with the **<img src=images/Draft_Upgrade.svg style="width:16px"> <img src=images/Part_Compound.svg style="width:Upgrade](Draft_Upgrade.md)** tool, or the {{Value|Compound}} created with the **[16px"> [Part Compound](Part_Compound.md)** tool.
:   10.2. Press **<img src=images/Draft_PolarArray.svg style="width:16px"> [PolarArray](Draft_PolarArray.md)**.
:   10.3. Adjust the polar angle to {{Value|360°}}.
:   10.4. Set the number of elements to {{Value|4}}.
:   10.5. Enter the values for the center of rotation {{Value|(0, 0, 0)}}, and press **Enter**.

The array object shows copies of the object around the origin.

<img alt="" src=images/03_Dr01_Draft_PolarArray.png  style="width:" height="400px;"> 
*Polar array of the small profile centered around the origin.*


<div class="mw-translate-fuzzy">

#### Adicionando Dimensões 

Dimensões requerem um uso constante de \'\' Restrições de agarramento \'\' \'\' para selecionar adequadamente os pontos que se deseja dimensionar. A \'\' \'da barra de ferramentas de agarramento\' \'\' é utilizado para alterar os pontos possíveis que podem ser seleccionados.


</div>

Linear dimensions work best when using the appropriate [Draft Snap](Draft_Snap.md) methods to select points and edges to measure. However, they can also be created by specifying absolute coordinates.


<div class="mw-translate-fuzzy">

1.  Seleccione ![](images/Draft_Dimension.png ) [ Dimension](Draft_Dimension.md)
2.  Selecione o primeiro ponto. Este pode ser um elemento ou especificado por coordintes existente. Para este tutorial, o primeiro ponto será alwaysvbe \'\' \'(0, 0, 0)\' \'\'
3.  Selecione o segundo ponto. Aproxime-se do ponto médio da linha superior do polígono. Um ponto branco deverá aparecer ao lado deste ícone ![ 32px](images/Snap_Midpoint.png )
4.  Mova o cursor para o local desejado da dimensão e clique sobre ele.
5.  Alterar o tamanho da fonte na guia \'\' \'View\' \'\' e 6 mm


</div>


<div class="mw-translate-fuzzy">

Repetir o processo para os arcos e os círculos.


</div>

13\. Repeat the process for the circle located in the center. The first point of the measurement will still be the origin. To select the second point make sure **<img src=images/Draft_Snap_Lock.svg style="width:16px"> <img src=images/Draft_Snap_Angle.svg style="width:Toggle snap](Draft_Snap_Lock.md)** is active, and only **[16px"> [Angle](Draft_Snap_Angle.md)** as well. As you move the pointer to the top of the circle, the <img alt="" src=images/Draft_Snap_Angle.svg  style="width:24px;"> [Angle](Draft_Snap_Angle.md) icon should appear; click to select this point. Then move the cursor to the right, and click to fix the dimension.

Remember to adjust the **Font Size**, and other properties to see the dimension correctly.

<img alt="" src=images/04_Dr01_Draft_Dimension.png  style="width:" height="400px;"> 
*Dimensions that measure the vertical distance from the origin to the top of the circle, arcs, and polygon.*


<div class="mw-translate-fuzzy">

#### Anotações e Texto 

Existe uma pequena diferença entre os dois: só é possível usar o segundo como um perfil para executar operações 3D.


</div>


<div class="mw-translate-fuzzy">

##### Anotações

1.  Seleccione ![](images/Draft_Text.png ) [ texto](Draft_Text.md)
2.  Selecione o ponto de referência no \'\' \'Ver 3D\' \'\'. Neste caso, o midoint do arco superior.
3.  Digite o texto e pressione \'\' \'Enter\' \'\'. Repita o procedimento para o maior número de linhas de texto como você deseja introduzir.
4.  Pressione Enter\'\'\'


</div>


<div class="mw-translate-fuzzy">

##### Texto

1.  Seleccione ![ 32px](images/Draft_ShapeString.png ) [ ShapeString](Draft_ShapeString.md)
2.  Selecione o ponto de referência no \'\' \'Ver 3D\' \'\'. Isso pode ser um ponto existente ou a localização atual do cursor.
3.  Digite o texto e pressione \'\' \'Enter\' \'\'
4.  Defina o tamanho da fonte desejado
5.  Deixar rastreamento em 0 mm
6.  Selecione o \'\' \'caminho\' \'\' para o arquivo fonte que você deseja usar


</div>

<img alt="" src=images/05_Dr01_Draft_Text_ShapeString.png  style="width:" height="400px;"> 
*Text and ShapeString objects added.*

To extrude letters and engrave them on to solids, see the [Draft ShapeString tutorial](Draft_ShapeString_tutorial.md).


<div class="mw-translate-fuzzy">

#### Criando Blueprints 

Para criar os modelos, é necessário criar um \'\' \'Desenho\' \'\' com os elementos que você deseja usar. Por favor, leia o [Drawing tutorial](Drawing_tutorial.md) para uma descrição detalhada.


</div>

As it is now, the objects that we have created can be saved, exported to other formats like [SVG](SVG.md) or [DXF](DXF.md), or printed.

If you wish, you may create a technical drawing to display these objects together with additional information like a frame.

Before doing anything, hide the Draft grid by pressing **<img src=images/Draft_ToggleGrid.svg style="width:16px"> [Toggle  grid](Draft_ToggleGrid.md)**.

16\. Switch to the <img alt="" src=images/Workbench_TechDraw.svg  style="width:24px;"> [TechDraw Workbench](TechDraw_Workbench.md).

:   16.1. Create a standard page by pressing **<img src=images/TechDraw_PageDefault.svg style="width:16px"> [TechDraw PageDefault](TechDraw_PageDefault.md)**.
:   16.2. In the <img src=images/TechDraw_ActiveView.svg style="width:tree view](tree_view.md) select all objects created, except for the Page, and then press **[16px"> [TechDraw ActiveView](TechDraw_ActiveView.md)**. Press **OK** with the default options; it may take a few seconds to create the view in the page.
:   16.3. Selecting the Page object in the [tree view](tree_view.md) will automatically display the Page in the main window. With the Page selected, go to the [property editor](Property_editor.md), and change **Scale** to {{Value|0.75}}.
:   16.4. Expand the Page object in the [tree view](tree_view.md) to select the ActiveView object. With this view selected, go to the [property editor](Property_editor.md), and change **Scale Type** to {{Value|Page}}.
:   16.5. Recompute the model by using **<img src=images/Std_Refresh.svg style="width:16px"> [Refresh](Std_Refresh.md)** or pressing **F5**.
:   16.6. Hide the frames of the objects by pressing **<img src=images/TechDraw_ToggleFrame.svg style="width:16px"> [TechDraw ToggleFrame](TechDraw_ToggleFrame.md)**.

Learn more about the [TechDraw Workbench](TechDraw_Workbench.md) by reading the [Basic TechDraw Tutorial](Basic_TechDraw_Tutorial.md).

<img alt="" src=images/06_Dr01_Draft_TechDraw_page.png  style="width:" height="400px;"> 
*TechDraw page with a projection of the shapes created with the Draft Workbench.*

TechDraw works best with objects that have a [Part TopoShape](Part_TopoShape.md). Since some objects from Draft, like [Draft Texts](Draft_Text.md) and [Draft Dimensions](Draft_Dimension.md), don\'t have such \"[shapes](Shape.md)\", some operations of TechDraw don\'t work with these elements.

Tools like **<img src=images/TechDraw_ActiveView.svg style="width:16px"> <img src=images/TechDraw_DraftView.svg style="width:TechDraw ActiveView](TechDraw_ActiveView.md)**, **[16px"> <img src=images/TechDraw_ArchView.svg style="width:TechDraw DraftView](TechDraw_DraftView.md)**, and **[16px"> [TechDraw ArchView](TechDraw_ArchView.md)** work by receiving an internal SVG image that is generated by internal Draft functions; therefore, TechDraw doesn\'t have much control about how these views are displayed. More integration of Draft and TechDraw is a work in progress.


<div class="mw-translate-fuzzy">

Estamos agora a terminar com o fluxo de trabalho básico para o [ Projecto Módulo](Draft_Workbench.md).


</div>

The [Draft Workbench](Draft_Workbench.md) in many ways is similar to the [Sketcher Workbench](Sketcher_Workbench.md), as both are intended to produce 2D shapes. The main difference is in the way each workbench handles coordinate systems, and how the objects are positioned. In Draft, objects are freely positioned in the global coordinates system, usually snapping their points to a grid, or to other objects. In Sketcher, a \"[sketch object](Sketch.md)\" defines a local coordinate system which serves as the reference for all geometrical elements within that sketch. Moreover, the sketch relies on \"constraints\" to define the final position of its points.

-   The [Draft Workbench](Draft_Workbench.md) is intended for 2D drawings which are suitable to be drawn on a grid. The [Arch Workbench](Arch_Workbench.md) mostly builds on top of the tools defined in the [Draft Workbench](Draft_Workbench.md).

-   The [Sketcher Workbench](Sketcher_Workbench.md) is intended for 2D drawings that require precise relationships between its points. It does not rely on a grid, but on rules of positioning (constraints) to determine where the points and edges will be placed. The [Sketcher Workbench](Sketcher_Workbench.md) is mostly used together with the [PartDesign Workbench](PartDesign_Workbench.md) for the creation of solid [bodies](Body.md).

-   It is possible to transform a Draft object into a <img src=images/Draft_Draft2Sketch.svg style="width:Sketch](Sketch.md), and the other way around, using the **[16px"> [Draft Draft2Sketch](Draft_Draft2Sketch.md)** tool.


{{Tutorials navi

}}  
