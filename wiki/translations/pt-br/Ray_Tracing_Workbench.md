 


{{VeryImportantMessage|The Raytracing workbench is essentially obsolete. New development is happening in the [https://github.com/FreeCAD/FreeCAD-render Render Workbench], which is intended as its replacement. This workbench is fully programmed in Python so it is much easier to extend.

Nevertheless, the information in this page is generally useful for the new workbench, as both modules work basically in the same way.
}}

<img alt="Raytracing workbench icon" src=images/Workbench_Raytracing.svg  style="width:128px;">

## Introdução


{{TOCright}}

The <img alt="" src=images/Workbench_Raytracing.svg  style="width:24px;"> [Raytracing Workbench](Raytracing_Workbench.md) is used to generate photorealistic images of your models by processing them with an external renderer.

A bancada Raytracing trabalha com [ templates](Raytracing_templates.md), que são arquivos de projeto que definem uma cena para seu modelo 3D. Você pode colocar luzes e geometrias, como planos de base, e também contém espaços reservados para a posição da câmera e para as informações do material dos objetos na cena. O projeto pode ser exportado para um arquivo pronto para renderização ou renderizado diretamente no FreeCAD.

Atualmente, dois renderizadores são suportados: [povray](http://en.wikipedia.org/wiki/POV-Ray) e [luxrender](http://en.wikipedia.org/wiki/LuxRender). Para poder renderizar a partir do FreeCAD, pelo menos um desses programas deve ser instalado e configurado em seu sistema. No entanto, se nenhum renderizador estiver instalado, você ainda poderá exportar um arquivo de projeto para ser renderizado em outro momento.

Uma nova bancada Render está em desenvolvimento para suportar múltiplos back-ends como o Lux Renderer e o Yafaray. Informações para usar a versão de desenvolvimento podem ser visualizadas em [ Render project](Render_project.md). Para o status de desenvolvimento do Módulo Render, procure no projeto [ Raytracing project](Raytracing_project.md).

<img alt="" src=images/Raytracing_example.jpg  style="width:1024px;">


<div class="mw-translate-fuzzy">

## Fluxo de trabalho típico {#fluxo_de_trabalho_típico}

1.  Crie ou abra um projeto do FreeCAD, adicione alguns objetos sólidos ([ Part-based](Part_Workbench.md) ou [ PartDesign-based](PartDesign_Workbench.md)); malhas atualmente não são suportadas.
2.  Crie um projeto de Raytracing (povray ou luxrender).
3.  Selecione os objetos que você deseja adicionar ao projeto Raytracing e adicione-os.
4.  Exportar o arquivo do projeto ou renderizá-lo diretamente.


</div>

<img alt="" src=images/Raytracing_Workbench_workflow.svg  style="width:600px;">


{{Caption | Fluxo de trabalho da bancada Raytracing; o ambiente de trabalho prepara um arquivo de projeto de um determinado modelo e, em seguida, chama um programa externo para produzir a renderização real da cena. O renderizador externo pode ser usado independentemente do FreeCAD.}}

## Ferramentas

### Ferramentas de Projeto {#ferramentas_de_projeto}

Essas são as principais ferramentas para exportar o seu trabalho 3D para os renderizadores externos:

-   <img alt="" src=images/Raytracing_New.png  style="width:32px;"> [Novo Projeto PovRay](Raytracing_New.md): Insere um novo projeto PovRay no documento.
-   <img alt="" src=images/Raytracing_Lux.png  style="width:32px;"> [Novo Projeto LuxRender](Raytracing_Lux.md): Insere um novo projeto LuxRender in no documento.
-   <img alt="" src=images/Raytracing_InsertPart.png  style="width:32px;"> [Inserir Peça](Raytracing_InsertPart.md): Insere uma vista de uma Peça em um projeto do Raytracing.
-   <img alt="" src=images/Raytracing_ResetCamera.png  style="width:32px;"> [Redefinir camera](Raytracing_ResetCamera.md): Corresponde a posição da câmera de um projeto Raytracing à visão atual.
-   <img alt="" src=images/Raytracing_ExportProject.png  style="width:32px;"> [Exportar projeto](Raytracing_ExportProject.md): Exporta um projeto raytracing para o arquivo de cena para renderizar em um renderizador externo.
-   <img alt="" src=images/Raytracing_Render.png  style="width:32px;"> [Renderizador](Raytracing_Render.md): Renderiza um projeto raytracing com um renderizador externo.

### Utilidades

Estas são ferramentas auxiliares para realizar tarefas específicas manualmente.

-   <img alt="" src=images/Raytracing_Export.png  style="width:32px;"> [Exportar vista para povray](Raytracing_Export.md): Escreve uma vista 3D ativa com câmera e todo seu conteúdo para um arquivo povray.
-   <img alt="" src=images/Raytracing_Camera.png  style="width:32px;"> [Exportar câmera para o povray](Raytracing_Camera.md): Exporta a posição da câmera de uma vista 3D ativa no formato POV-Ray para um arquivo.
-   <img alt="" src=images/Raytracing_Part.png  style="width:32px;"> [Exportar peça para o povray](Raytracing_Part.md): Escreve a Peça selecionada (objeto) como um arquivo povray.

## Preferências

-   <img alt="" src=images/Preferences-raytracing.svg  style="width:32px;"> [Preferências](Raytracing_Preferences.md): Preferências disponíveis nas ferramentas do Raytracing.

## Tutoriais

-   [Basic Raytracing tutorial](Raytracing_tutorial.md)
-   [Intermediate Raytracing tutorial](Tutorial_FreeCAD_POV_ray.md)

## Criando um arquivo povray manualmente {#criando_um_arquivo_povray_manualmente}

As ferramentas de utilitário descritas acima permitem que você exporte a visualização 3D atual e todo o seu conteúdo para um arquivo [1](http://www.povray.org/Povray). Primeiro, você deve carregar ou criar seus dados CAD e posicionar a orientação da vista 3D como desejar. Em seguida, escolha \"Utilitários → Exportar vista \...\" no menu raytracing

![](images/FreeCAD_Raytracing.jpg )

Você será perguntado por um local para salvar o arquivo \* .pov resultante. Depois disso, você pode abri-lo em [2](http://www.povray.org/Povray) e renderizar: ![](images/Povray.jpg )

Como de costume em um renderizador você pode fazer fotos grandes e agradáveis: <img alt="" src=images/Scharniergreifer_render.jpg  style="width:800px;">

## Scripting

Consulte o [Raytracing API example](Raytracing_API_example.md) para obter informações sobre como escrever cenas programaticamente.

## Links

### POVRay

-   <http://www.spiritone.com/~english/cyclopedia/>
-   <http://www.povray.org/>
-   <http://en.wikipedia.org/wiki/POV-Ray>

### Luxrender

-   <http://www.luxrender.net/>

### Futuros possíveis renderizadores a serem implementados {#futuros_possíveis_renderizadores_a_serem_implementados}

-   <http://www.yafaray.org/>
-   <http://www.mitsuba-renderer.org/>
-   <http://www.kerkythea.net/>
-   <http://www.artofillusion.org/>

## Exportando para Kerkythea {#exportando_para_kerkythea}

Embora a exportação direta para o formato de arquivo XML Kerkythea ainda não é suportada, você pode exportar seus objetos como arquivos de malha (.obj) e, em seguida, importá-los no Kerkythea.

-   se estiver usando o Kerkythea para Linux, lembre-se de instalar o WINE-Package (necessário para o Kerkythea Linux rodar)
-   você pode converter seus modelos com a ajuda da bancada Malha para malhas e exportar essas malhas como arquivos .obj
-   Se a sua malha de exportação resultou em erros (flip de normais, buracos \...) você pode tentar a sorte com [netfabb studio basic](http://www.netfabb.com/downloadcenter.php?basic=1)

:   Gratuito para uso pessoal, disponível para Windows, Linux e Mac OSX.
:   Possui ferramentas de reparo padrão que irão reparar seu modelo na maioria dos casos.

-   Outro bom programa para análise / reparo de malhas é o [Meshlab](http://sourceforge.net/projects/meshlab/)

:   Open Source, disponível para Windows, Linux e Mac OSX.
:   Possui ferramentas de reparo padrão que reparam o modelo na maioria dos casos (preenche buracos, reorienta as normais, etc.)

-   você pode usar \"make compound\" e então \"make single copy\" ou você pode fundir sólidos para agrupá-los antes de converter em malhas
-   Lembre-se de definir em Kerkythea um fator de importação de 0.001 para o obj-modeler, já que Kerkythea espera que o arquivo obj esteja em m (mas o esquema de unidades padrão no FreeCAD é mm)

:   No Windows 7, o Kerkythea de 64 bits não parece conseguir salvar essas configurações.
:   Então lembre-se de fazer isso toda vez que você começar Kerkythea

-   Ao importar vários objetos no Kerkythea, você pode usar o comando \"Arquivo → Mesclar\" no Kerkythea

## Desenvolvimento

-   [Projeto Render](Render_project.md)

These pages refer to the new workbench, programmed in Python, meant to replace the current Raytracing Workbench.

-   [Render Workbench](https://github.com/FreeCAD/FreeCAD-render)
-   [Render Workbench](https://forum.freecadweb.org/viewtopic.php?f=9&t=25933) (announcement only, no discussion)
-   [FreeCAD Renderer Workbench improvements](https://forum.freecadweb.org/viewtopic.php?t=39168)

**Outdated**

These pages refer to a replacement workbench, programmed in C++, proposed around 2012, which was never completed.

-   [Raytracing project](Raytracing_project.md)
-   [Render project](Render_project.md)





{{Raytracing Tools navi

}} 

[Category:Workbenches{{\#translation:}}](Category:Workbenches.md)
