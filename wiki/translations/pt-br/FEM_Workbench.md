# <img alt="Ícone da bancada de trabalho FEM" src=images/Workbench_FEM.svg  style="width:64px;"> FEM Workbench/pt-br


{{TOCright}}

## Introdução


<div class="mw-translate-fuzzy">

A [ bancada FEM](FEM_Workbench/pt-br.md) fornece um fluxo de trabalho moderno de [análise de elementos finitos](https://en.wikipedia.org/wiki/Finite_element_analysis) (FEA) para o FreeCAD. Isso significa que todas as ferramentas para fazer uma análise são combinadas em uma interface gráfica de usuário (GUI).


</div>

<img alt="" src=images/FemWorkbench.jpg  style="width:300px;">

## Fluxo de Trabalho 


<div class="mw-translate-fuzzy">

Os passos para realizar uma análise de elementos finitos são:

1.  Pré-processamento: configurar o problema de análise.
    1.  Modelando a geometria: criar a geometria com o FreeCAD ou importando-a de um aplicativo diferente.
    2.  Criando uma análise.
        1.  Adicionando restrições de simulação, como cargas e suportes fixos ao modelo geométrico.
        2.  Adicionando materiais às partes do modelo geométrico.
        3.  Criando uma malha de elementos finitos para o modelo geométrico ou importando-os de um aplicativo diferente.
2.  Resolvendo: executando um solucionador externo de dentro do FreeCAD.# Pós-processamento: visualizar os resultados da análise a partir do FreeCAD ou exportar os resultados para que possam ser pós-processados com outra aplicação.


</div>

A bancada FEM pode ser usada no Linux, Windows e Mac OSX. Como o ambiente de trabalho usa solucionadores externos, a quantidade de configuração manual dependerá do sistema operacional que você está usando. Veja [ Instalação da FEM](FEM_Install/pt-br.md) para instruções sobre como configurar as ferramentas externas.

<img alt="" src=images/FEM_Workbench_workflow.svg  style="width:600px;">


{{Caption | Fluxo de trabalho da bancada FEM; a bancada chama dois programas externos para realizar o meshing de um objeto sólido e executa a solução real do problema do elemento finito}}

## Menu: Modelo 

-   <img alt="" src=images/FEM_Analysis.svg  style="width:32px;"> [Contêiner de análise](FEM_Analysis/pt-br.md): Cria um novo contêiner de análise mecânica. Se um sólido é selecionado na árvore de visualização antes de clicar nele, a janela de malha vai ser aberta em seguida.

### Materiais

-   <img alt="" src=images/FEM_MaterialSolid.svg  style="width:32px;"> [Materiais sólidos](FEM_MaterialSolid/pt-br.md): Permite você selecionar um material a partir do banco de dados.

-   <img alt="" src=images/FEM_MaterialFluid.svg  style="width:32px;"> [Materiais fluidos](FEM_MaterialFluid/pt-br.md): Permite você selecionar um material a partir do banco de dados.

-   <img alt="" src=images/FEM_MaterialMechanicalNonlinear.svg  style="width:32px;"> [Material mecânico não linear](FEM_MaterialMechanicalNonlinear/pt-br.md): Permite você selecionar um material a partir do banco de dados.

-   <img alt="" src=images/FEM_MaterialReinforced.svg  style="width:32px;"> [Material reforçado](FEM_MaterialReinforced/pt-br.md): Permite selecionar materiais reforçados constituídos por uma matriz e um reforço da base de dados.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/FEM_MaterialEditor.svg  style="width:32px;"> [Editor de materiais](FEM_MaterialEditor/pt-br.md):: Permite que você abra o editor de materiais para editar materiais.


</div>

### Geometria do Elemento 

-   <img alt="" src=images/FEM_ElementGeometry1D.svg  style="width:32px;"> [Seção transversal da viga](FEM_ElementGeometry1D/pt-br.md)

-   <img alt="" src=images/FEM_ElementRotation1D.svg  style="width:32px;"> [Rotação de viga](FEM_ElementRotation1D/pt-br.md)

-   <img alt="" src=images/FEM_ElementGeometry2D.svg  style="width:32px;"> [Espessura da casca de placa](FEM_ElementGeometry2D/pt-br.md)


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/FEM_ElementFluid1D.svg  style="width:32px;"> [Seção do fluido para fluxo 1D](FEM_ElementFluid1D/pt-br.md)


</div>

### Restrições Eletrostáticas 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/FEM_ConstraintElectrostaticPotential.svg  style="width:32px;"> [Restrição de potencial eletrostático](FEM_ConstraintElectrostaticPotential/pt-br.md)


</div>

### Restrições do Fluido 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/FEM_ConstraintInitialFlowVelocity.svg  style="width:32px;"> [Restrição de velocidade inicial do fluxo](FEM_ConstraintInitialFlowVelocity/pt-br.md):


</div>

-   <img alt="" src=images/FEM_ConstraintInitialPressure.svg  style="width:32px;"> [Constraint initial pressure](FEM_ConstraintInitialPressure.md): Used to define an initial pressure for the body. <small>(v1.0)</small> 

-   <img alt="" src=images/FEM_ConstraintFlowVelocity.svg  style="width:32px;"> [Restrição da velocidade de fluxo](FEM_ConstraintFlowVelocity/pt-br.md)

### Restrições Geométrica 

-   <img alt="" src=images/FEM_ConstraintPlaneRotation.svg  style="width:32px;"> [Restrição rotação plana](FEM_ConstraintPlaneRotation/pt-br.md): Usada para definir uma restrição de rotação plana em uma face plana.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/FEM_ConstraintSectionPrint.svg  style="width:32px;"> [Impressão da seção de restrição](FEM_ConstraintSectionPrint/pt-br.md): <small>(v0.19)</small> 


</div>

-   <img alt="" src=images/Fem-constraint-transform.svg  style="width:32px;"> [Restrição de transformar](FEM_ConstraintTransform/pt-br.md): Usado para definir uma restrição de transformação em um rosto.

### Restrições Mecânicas 

-   <img alt="" src=images/FEM_ConstraintFixed.svg  style="width:32px;"> [Restrição fixa](FEM_ConstraintFixed/pt-br.md): Usada para definir uma restrição fixa em um ponto, aresta ou face.

-   <img alt="" src=images/FEM_ConstraintDisplacement.svg  style="width:32px;"> [Restrição de deslocamento](FEM_ConstraintDisplacement/pt-br.md): Usada para definir uma restrição de deslocamento em ponto, aresta ou face.

-   <img alt="" src=images/FEM_ConstraintContact.svg  style="width:32px;"> [Restrição de contato](FEM_ConstraintContact/pt-br.md): Usada para definir uma restrição de contato entre duas faces.

-   <img alt="" src=images/FEM_ConstraintTie.svg  style="width:32px;"> [Restrições de amarração](FEM_ConstraintTie/pt-br.md): <small>(v0.19)</small> 

-   <img alt="" src=images/FEM_ConstraintSpring.svg  style="width:32px;"> [Constraint spring](FEM_ConstraintSpring.md): Used to define a spring. <small>(v0.20)</small> 

-   <img alt="" src=images/FEM_ConstraintForce.svg  style="width:32px;"> [Restrição de força](FEM_ConstraintForce/pt-br.md): Usada para definir uma força em Newtons \[N\] aplicada uniformemente a uma face selecionável em uma direção definida.

-   <img alt="" src=images/FEM_ConstraintPressure.svg  style="width:32px;"> [Restrição de pressão](FEM_ConstraintPressure/pt-br.md): Usada para definir uma restrição de pressão.

-   <img alt="" src=images/FEM_ConstraintCentrif.svg  style="width:32px;"> [Constraint centrif](FEM_ConstraintCentrif.md): Used to define a centrifugal body load constraint. <small>(v0.20)</small> 

-   <img alt="" src=images/FEM_ConstraintSelfWeight.svg  style="width:32px;"> [Restrição de peso próprio](FEM_ConstraintSelfWeight/pt-br.md): Usada para definir uma aceleração da gravidade agindo sobre um modelo.

### Restrições Térmicas 

-   <img alt="" src=images/FEM_ConstraintInitialTemperature.svg  style="width:32px;"> [Restrição de temperatura inicial](FEM_ConstraintInitialTemperature/pt-br.md): Usada para definir a temperatura inicial de um corpo.

-   <img alt="" src=images/FEM_ConstraintHeatflux.svg  style="width:32px;"> [Restrição de fluxo de calor](FEM_ConstraintHeatflux/pt-br.md): Usada para definir uma restrição de fluxo de calor em uma face.

-   <img alt="" src=images/FEM_ConstraintTemperature.svg  style="width:32px;"> [Restrição de temperatura](FEM_ConstraintTemperature/pt-br.md): Usada para definir uma restrição de temperatura em um ponto, aresta ou face.

-   <img alt="" src=images/FEM_ConstraintBodyHeatSource.svg  style="width:32px;"> [Restrição de fonte de corpo quente](FEM_ConstraintBodyHeatSource.md)

### Restrições sem solução 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Fem-constraint-fluid-boundary.svg  style="width:32px;"> [Restrição de fronteira de fluido](FEM_ConstraintFluidBoundary/pt-br.md)


</div>

-   <img alt="" src=images/FEM_ConstraintBearing.svg  style="width:32px;"> [Restrição de rolamento](FEM_ConstraintBearing/pt-br.md): Usada para definir uma restrição de rolamento.

-   <img alt="" src=images/FEM_ConstraintGear.svg  style="width:32px;"> [Restrição de engrenagem](FEM_ConstraintGear/pt-br.md): Usada para definir uma restrição de engrenagem.

-   <img alt="" src=images/FEM_ConstraintPulley.svg  style="width:32px;"> [Restrição de polia](FEM_ConstraintPulley/pt-br.md): Usada para definir uma restrição de polia.

### Sobreescrever Restrições 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/FEM_ConstantVacuumPermittivity.svg  style="width:32px;"> [Permissividade de vácuo constante](FEM_ConstantVacuumPermittivity/pt-br.md): <small>(v0.19)</small> 


</div>

## Menu: Malhas 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/FEM_MeshNetgenFromShape.svg  style="width:32px;"> [Malha FEM da forma pelo Netgen](FEM_MeshNetgenFromShape/pt-br.md)


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/FEM_MeshGmshFromShape.svg  style="width:32px;"> [Malha FEM da forma pelo GMSH](FEM_MeshGmshFromShape/pt-br.md)


</div>

-   <img alt="" src=images/FEM_MeshBoundaryLayer.svg  style="width:32px;"> [Camada limite de malha FEM](FEM_MeshBoundaryLayer/pt-br.md): Cria malhas anisotrópicas para cálculos precisos perto dos limites.

-   <img alt="" src=images/FEM_MeshRegion.svg  style="width:32px;"> [Região de malha FEM](FEM_MeshRegion/pt-br.md): Cria uma(s) área(s) localizada(s) para malha(s) que otimiza(m) altamente o tempo de análise.

-   <img alt="" src=images/FEM_MeshGroup.svg  style="width:32px;"> [Grupo de malha FEM](FEM_MeshGroup/pt-br.md): Agrupa e etiqueta elementos de uma malha (vértice, borda, superfície) juntos, úteis para exportar a malha para solvers externos.

-   <img alt="" src=images/FEM_CreateNodesSet.svg  style="width:32px;"> [Conjunto de nós](FEM_CreateNodesSet/pt-br.md): Cria/define um conjunto de nós a partir da malha FEM.

-   <img alt="" src=images/FEM_FemMesh2Mesh.svg  style="width:32px;"> [Malha FEM para Mesh](FEM_FemMesh2Mesh/pt-br.md): Converte a superfície de uma malha FEM para uma malha de Mesh.

## Menu: Solucionador 

-   <img alt="" src=images/FEM_SolverCalculixCxxtools.svg  style="width:32px;"> [Solucionador Calculix CCX](FEM_SolverCalculixCxxtools/pt-br.md): Cria um novo solucionador para esta análise. Na maioria dos casos, o solucionador é criado junto com a análise.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/FEM_SolverCalculiX.svg  style="width:32px;"> [Solucionador CalculiX(experimental)](FEM_SolverCalculiX/pt-br.md)


</div>

-   <img alt="" src=images/FEM_SolverElmer.svg  style="width:32px;"> [Solucionador Elmer](FEM_SolverElmer/pt-br.md): Cria o controlador solver para Elmer. Ele é independente de outros objetos solucionadores.

-   <img alt="" src=images/FEM_SolverMystran.svg  style="width:32px;"> [Solver Mystran](FEM_SolverMystran.md): <small>(v0.20)</small> 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/FEM_SolverZ88.svg  style="width:32px;"> [Solucionador Z88](FEM_SolverZ88/pt-br.md)


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/FEM_EquationElasticity.svg  style="width:32px;"> [Equação de elasticidade](FEM_EquationElasticity/pt-br.md)


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/FEM_EquationElectricforce.svg  style="width:32px;"> [Equação da força elétrica](FEM_EquationElectricforce/pt-br.md): <small>(v0.19)</small> 


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/FEM_EquationElectrostatic.svg  style="width:32px;"> [Equação eletrostática](FEM_EquationElectrostatic/pt-br.md)


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/FEM_EquationFlow.svg  style="width:32px;"> [Equação de fluxo](FEM_EquationFlow/pt-br.md)


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/FEM_EquationFlux.svg  style="width:32px;"> [Equação de solucionador de fluxo](FEM_EquationFlux/pt-br.md)


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/FEM_EquationHeat.svg  style="width:32px;"> [Equação de calor](FEM_EquationHeat/pt-br.md)


</div>

-   <img alt="" src=images/FEM_SolverControl.svg  style="width:32px;"> [Solucionador do controle de trabalho](FEM_SolverControl/pt-br.md): Abre

o menu para ajustar e iniciar o solucionador selecionado.

-   <img alt="" src=images/FEM_SolverRun.svg  style="width:32px;"> [Executar solucionador de cálculo](FEM_SolverRun/pt-br.md): Executa o solucionador selecionado das análises ativas.

## Menu: Resultados 

-   <img alt="" src=images/FEM_ResultsPurge.svg  style="width:32px;"> [Limpar resultados](FEM_ResultsPurge/pt-br.md): Deleta os resultados das análises ativas.

-   <img alt="" src=images/FEM_ResultShow.svg  style="width:24px;"> [Mostrar resultado](FEM_ResultShow/pt-br.md): Usado para exibir o resultado de uma análise.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/FEM_PostApplyChanges.svg  style="width:32px;"> [Postar mudanças aplicadas](FEM_PostApplyChanges/pt-br.md)


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/FEM_PostPipelineFromResult.svg  style="width:32px;"> [Postar pipeline do resultado](FEM_PostPipelineFromResult/pt-br.md)


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/FEM_PostFilterWarp.svg  style="width:32px;"> [Filtro de dobra](FEM_PostFilterWarp/pt-br.md)


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/FEM_PostFilterClipScalar.svg  style="width:32px;"> [Scalar clip filter](FEM_PostFilterClipScalar/pt-br.md):


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/FEM_PostFilterCutFunction.svg  style="width:32px;"> [Criar filtro de corte](FEM_PostFilterCutFunction/pt-br.md):


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/FEM_PostFilterClipRegion.svg  style="width:32px;"> [Filtro de clipes de região](FEM_PostFilterClipRegion/pt-br.md)


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/FEM_PostFilterDataAlongLine.svg  style="width:32px;"> [Filtro de clipes de linha](FEM_PostCreateDataAlongLineFilter/pt-br.md)


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/FEM_PostFilterLinearizedStresses.svg  style="width:32px;"> [Gráfico de linearização de tensão](FEM_PostFilterLinearizedStresses/pt-br.md)


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/FEM_PostFilterDataAtPoint.svg  style="width:32px;"> [Dados no filtro de clipes de ponto](FEM_PostFilterDataAtPoint/pt-br.md):


</div>


<div class="mw-translate-fuzzy">

-   [Funções de filtro](FEM_PostCreateFunctions/pt-br.md):
    -   <img alt="" src=images/Fem-post-geo-plane.svg  style="width:32px;">
    -   <img alt="" src=images/Fem-post-geo-sphere.svg  style="width:32px;">


</div>

  - <img alt="" src=images/Fem-post-geo-plane.svg  style="width:32px;"> [Filter function plane](FEM_PostCreateFunctionPlane.md): Defines that the result mesh is cut with a plane.

  - <img alt="" src=images/Fem-post-geo-sphere.svg  style="width:32px;"> [Filter function sphere](FEM_PostCreateFunctionSphere.md): Defines that the result mesh is cut with a sphere.

## Menu: Utilidades 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/FEM_ClippingPlaneAdd.svg  style="width:32px;"> [Plano de grampeamento na face](FEM_ClippingPlaneAdd/pt-br.md):


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/FEM_ClippingPlaneRemoveAll.svg  style="width:32px;"> [Remover todos os aviões de corte](FEM_ClippingPlaneRemoveAll/pt-br.md):


</div>

-   <img alt="" src=images/FEM_Examples.svg  style="width:32px;"> [Exemplos de FEM abertos](FEM_Examples/pt-br.md): Abra a GUI para acessar exemplos FEM.

## Menu de Contexto 

-   <img alt="" src=images/FEM_MeshClear.svg  style="width:32px;"> [Malha FEM transparente](FEM_MeshClear/pt-br.md): Deleta o arquivo de malha do arquivo FreeCAD. Útil para fazer um arquivo FreeCAD mais leve.

-   <img alt="" src=images/FEM_MeshDisplayInfo.svg  style="width:32px;"> [Exibir informações sobre a malha FEM](FEM_MeshDisplayInfo/pt-br.md):

## Preferências

-   <img alt="" src=images/Std_DlgPreferences.svg  style="width:32px;"> [Preferências\...](FEM_Preferences/pt-br.md): Preferências disponíveis em Ferramentas FEM.

## Informações

As páginas seguintes explicam diferentes tópicos do bancada de trabalho FEM.

[Instalação FEM](FEM_Install/pt-br.md): uma descrição detalhada sobre como montar os programas externos utilizados na bancada de trabalho.

[Malha FEM](FEM_Mesh/pt-br.md): mais informações sobre como obter uma malha para análise de elementos finitos.

[Solucionador FEM](FEM_Solver/pt-br.md): mais informações sobre os diferentes solucionadores disponíveis na bancada de trabalho e aqueles que poderiam ser utilizados no futuro.

[FEM CalculiX](FEM_CalculiX/pt-br.md): mais informações sobre CalculiX, o solucionador padrão utilizado na bancada de trabalho para análise estrutural.

[FEM Concreto](FEM_Concrete/pt-br.md): informações interessantes sobre o tema da simulação de estruturas de concreto.

## Tutorials


<div class="mw-translate-fuzzy">

## Tutoriais

Tutorial 1: [FEM CalculiX Cantilever 3D](FEM_CalculiX_Cantilever_3D/pt-br.md); análise básica de feixe simplesmente suportada.(Cantilever - Viga ou estrutura com apoio, ou fixação apenas num dos lados e que tem o outro lado livre.)


</div>

Tutorial 2: [Tutorial FEM](FEM_tutorial/pt-br.md); simples análise de tensão de uma estrutura.

Tutorial 3: [FEM Tutorial Python](FEM_Tutorial_Python/pt-br.md); montar o exemplo do cantilever inteiramente através do script em Python, incluindo a malha.

Tutorial 4: [FEM Corte de um Bloco Composto](FEM_Shear_of_a_Composite_Block/pt-br.md); ver a deformação de um bloco que é composto de dois materiais.


<div class="mw-translate-fuzzy">

Tutorial 5: [Análise FEM transitória](Transient_FEM_analysis/pt-br.md)


</div>


<div class="mw-translate-fuzzy">

Tutorial 6: [Pós-processamento dos resultados FEM com Paraview](Post-Processing_of_FEM_Results_with_Paraview/pt-br.md)


</div>


<div class="mw-translate-fuzzy">

Tutorial 7: [Exemplo FEM Capacitância Duas Bolas](FEM_Example_Capacitance_Two_Ball.md); Elmer\'s GUI tutorial 6 \" Capacitância Eletrostática Duas Bolas\" usando exemplos FEM.


</div>

Acoplamento de tutoriais de análise mecânica térmica por [openSIM](https://opensimsa.github.io/training.html)

Tutoriais em vídeo 1: [Vídeo FEM para iniciantes](https://forum.freecadweb.org/viewtopic.php?f=18&t=20499#p158353) (incluindo o link do YouTube)(em inglês)

Tutoriais em vídeo: [Vídeo FEM para iniciantes](https://forum.freecadweb.org/viewtopic.php?f=18&t=20499&start=10#p162321) (incluindo o link do YouTube)(em inglês)

Muitos tutoriais em vídeo: [anisim Software de Engenharia de Código Aberto](https://www.youtube.com/channel/UCnvFCm2BbXOVI3ObfXcxXhw) (em Alemão)

## Ampliação da bancada de trabalho FEM 

O bancada de trabalho FEM está em constante desenvolvimento. Um objetivo do projeto é encontrar maneiras de interagir facilmente com vários solucionadores FEM, para que o usuário final possa agilizar o processo de criação, enredamento, simulação e otimização de um problema de projeto de engenharia, tudo dentro do FreeCAD.


<div class="mw-translate-fuzzy">

As seguintes informações são destinadas aos usuários e desenvolvedores que desejam ampliar o Workbench FEM de diferentes maneiras. A familiaridade com C++ e Python é esperada, e também é necessário algum conhecimento do sistema \"objeto de documento\" usado no FreeCAD; esta informação está disponível no [Documentação para usuários avançados](Power_users_hub/pt-br.md) e no [Documentação para desenvolvedores](Developer_hub/pt-br.md).Observe que, como o FreeCAD está em desenvolvimento ativo, alguns artigos podem ser muito antigos e, portanto, obsoletos. As informações mais atualizadas são discutidas no [FreeCAD forums](https://forum.freecadweb.org/index.php) na seção Desenvolvimento. Para discussões FEM, conselhos ou assistência na ampliação do workbench, o leitor deve consultar o [FEM subforum](https://forum.freecadweb.org/viewforum.php?f=18).


</div>


<div class="mw-translate-fuzzy">

Os artigos seguintes explicam como o workbench pode ser ampliado, por exemplo, adicionando novos tipos de condições de limite (restrições), ou equações.

-   [Ampliar o Módulo FEM](Extend_FEM_Module/pt-br.md)
-   [Adicionar Tutorial de Restrições FEM](Add_FEM_Constraint_Tutorial/pt-br.md)
-   [Adicionar Tutorial de Equação FEM](Add_FEM_Equation_Tutorial/pt-br.md)


</div>

Um guia do desenvolvedor foi escrito para ajudar os usuários a entenderem a complexa base de código do FreeCAD e as interações entre os elementos centrais e as bancadas de trabalho individuais. O livro é hospedado no github para que múltiplos usuários possam contribuir com ele e mantê-lo atualizado.

-   [Visualização antecipada do ebook: Guia do desenvolvedor do módulo para a fonte FreeCAD](https://forum.freecadweb.org/viewtopic.php?t=17581) (tópico do fórum)
-   [Guia de desenvolvimento do FreeCAD Mod](https://github.com/qingfengxia/FreeCAD_Mod_Dev_Guide) (repositório github)

## Ampliação da documentação do bancada de trabalho FEM 

-   Mais informações sobre a extensão ou falta de documentação FEM podem ser encontradas no fórum: [Documentação FEM em falta no Wiki](https://forum.freecadweb.org/viewtopic.php?f=18&t=20823)





{{FEM Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > [FEM](Category_FEM.md) > FEM Workbench/pt-br
