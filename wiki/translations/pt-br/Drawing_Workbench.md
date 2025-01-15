# Drawing Workbench/pt-br
<div class="mw-translate-fuzzy">





</div>


**The '''Drawing Workbench''' is no longer included after version 0.20.<br>
The [TechDraw Workbench](TechDraw_Workbench.md) is its more advanced replacement.**

<img alt="Ícone da bancada de trabalho Drawing " src=images/Workbench_Drawing.svg  style="width:128px;">



## Introdução

O módulo Drawing permite que você coloque seu trabalho em 3D no papel. Ou seja, colocar vistas de seus modelos em uma janela 2D e inserir essa janela em um desenho, por exemplo, uma folha com uma borda, um título e seu logotipo e finalmente imprimir essa folha.




<img alt="" src=images/Drawing_extraction.png  style="width:600px;">



## Ferramentas

Estas são ferramentas para criar, configurar e exportar folhas de desenho 2D

-   <img alt="" src=images/Drawing_New.png  style="width:32px;"> [Abrir um gráfico vetorial escalável](Drawing_Open_SVG/pt-br.md): Abre uma folha de desenho previamente salva como um arquivo SVG

-   <img alt="" src=images/Drawing_Landscape_A3.png  style="width:32px;"> [Nova folha de desenho A3 orientação paisagem](Drawing_Landscape_A3/pt-br.md): Cria uma folha de desenho a partir do modelo padrão A3 do FreeCAD.

-   <img alt="" src=images/Drawing_View.png  style="width:32px;"> [Inserir uma vista](Drawing_View/pt-br.md): Insere uma visão do objeto selecionado na folha de desenho ativo

-   <img alt="" src=images/Drawing_Annotation.png  style="width:32px;"> [Anotação](Drawing_Annotation.md): Acrescenta uma anotação à folha de desenho atual

-   <img alt="" src=images/Drawing_Clip.png  style="width:32px;"> [Corte](Drawing_Clip/pt-br.md): Acrescenta um grupo de recortes à folha de desenho atual

-   <img alt="" src=images/Drawing_Openbrowser.png  style="width:32px;"> [Open Browser](Drawing_Openbrowser.md): Opens a preview of the current sheet in the browser

-   <img alt="" src=images/Drawing_Orthoviews.png  style="width:32px;"> [Ortho Views](Drawing_Orthoviews.md): Automatically creates orthographic views of an object on the current drawing sheet

-   <img alt="" src=images/Drawing_Symbol.png  style="width:32px;"> [Symbol](Drawing_Symbol.md): Adds the contents of a SVG file as a symbol on the current drawing sheet

-   <img alt="" src=images/Drawing_DraftView.png  style="width:32px;"> [Draft View](Draft_Drawing.md): Inserts a special Draft view of the selected object in the current drawing sheet

-   <img alt="" src=images/Drawing_SpreadsheetView.png  style="width:32px;"> [Spreadsheet View](Drawing_SpreadsheetView.md): Inserts a view of a selected spreadsheet in the current drawing sheet

-   <img alt="" src=images/Drawing_Save.png  style="width:32px;"> [Save sheet](Drawing_Save.md): Saves the current sheet as a SVG file

-   [Project Shape](Drawing_ProjectShape.md): Creates a projection of the selected object (Source) in the 3D view.

-    **Note:**the [Draft Drawing](Draft_Drawing.md) tool is used with [Draft objects](Draft_Workbench.md). It has some additional capabilities over the Drawing tools, and supports specific objects like [Draft dimensions](Draft_Dimension.md).

## Workflow

The document contains a 3D shape object (leg) from which we want to produce a drawing. Therefore a \"Page\" is created. A page it\'s instantiated from a template, for example, the \"A3_Landscape\" template. The template is an [SVG](SVG.md) document which can hold a page frame, a logo, and other elements.

Nesta página, podemos inserir uma ou mais vistas. Cada vista tem uma posição na página, um fator de escala e propriedades adicionais. Cada vez que a página ou a vista ou o objeto referenciado muda, a página é regenerada e a exibição da página é atualizada.

## Scripting

No momento, o fluxo de trabalho da interface gráfica do usuário é muito limitado, por isso a API de scripting é mais interessante.

See the [Drawing API example](Drawing_API_example.md) page for a description of the functions used to create drawing pages and views.

## Extending the Drawing Module 

Some notes on the programming side of the drawing module will be added to the [Drawing Documentation](Drawing_Documentation.md) page. This is to help quickly understand how the drawing module works, enabling programmers to rapidly start programming for it.

## External links 

-   [Intro to mechanical drawing on Youtube - by Normal Universe](https://www.youtube.com/watch?v=1Hm5Zyjmjac)


<div class="mw-translate-fuzzy">





</div>


{{Drawing Tools navi

}}



---
⏵ [documentation index](../README.md) > [Obsolete Workbenches](Category_Obsolete%20Workbenches.md) > [Drawing](Category_Drawing.md) > Drawing Workbench/pt-br
