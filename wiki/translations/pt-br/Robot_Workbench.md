# Robot Workbench/pt-br
**O Robot Workbench não está em manutenção. Se você tem experiência com o tópico e está interessado em mantê-lo, por favor, declare sua intenção na seção de desenvolvedores no  [https://forum.freecadweb.org/index.php forum FreeCAD].

A razão pela qual esta bancada de trabalho ainda está no código-fonte mestre é porque esta bancada de trabalho está programada em C++. Se esta bancada de trabalho pudesse ser programada em Python, então ela poderia ser feita em uma  [bancada de trabalho externa](external_workbenches/pt-br.md) e poderia ser movida para um repositório separado.
**

## Introdução

<img alt="Ícone da bancada de trabalho Robot" src=images/Workbench_Robot.svg  style="width:128px;">

A bancada de trabalho <img alt="" src=images/Workbench_Robot.svg  style="width:24px;"> [Robot](Robot_Workbench.md) é uma ferramenta para simular um [robô industrial de 6 eixos](Robot_6-Axis/pt-br.md) como o [Kuka](http://kuka.com/).

Você pode fazer as seguintes tarefas:

-   Configure um ambiente de simulação com um robô e peças de trabalho;
-   Crie e preencha trajetórias de movimentos;
-   Decomponha os recursos de uma peça CAD em uma trajetória.
-   Simule o movimento de robô e alcance a distância;
-   Exporte a trajetória para um arquivo de programa de robô;

Para começar, experimente o [tutorial Robot](Robot_tutorial/pt-br.md) e veja a interface de programação no arquivo de exemplo [RobotExample.py](https://github.com/FreeCAD/FreeCAD_sf_master/blob/master/src/Mod/Robot/RobotExample.py).


{{TOCright}}

<img alt="" src=images/Robot_Workbench_example.jpg  style="width:500px;">

## Ferramentas

Aqui estão os principais comandos que você pode usar para criar uma configuração de robô.

### Robôs

As ferramentas para criar e gerenciar os robôs de 6 eixos.

-   <img alt="" src=images/Robot_CreateRobot.svg  style="width:30px;"> [Criar um robô](Robot_CreateRobot/pt-br.md): Inserir um novo robô na cena.
-   <img alt="" src=images/Robot_Simulate.svg  style="width:30px;"> [Simular uma trajetória](Robot_Simulate/pt-br.md): Abre o diálogo de simulação e te permite simular.
-   <img alt="" src=images/Robot_Export.svg  style="width:30px;"> [Exportar uma trajetória](Robot_Export/pt-br.md): Exporta um arquivo de programa de robô.
-   <img alt="" src=images/Robot_SetHomePos.svg  style="width:30px;"> [Definir a posição inicial](Robot_SetHomePos/pt-br.md): Define a posição inicial de um robô.
-   <img alt="" src=images/Robot_RestoreHomePos.svg  style="width:30px;"> [Restaurar a posição inicial](Robot_RestoreHomePos/pt-br.md): Move o robô para a sua posição inicial.

### Trajetórias

Ferramentas para criar e manipular trajetórias. Existem dois tipos de trajetórias: as paramétricas e as não paramétricas.

#### Trajetórias Não Paramétricas 

-   <img alt="" src=images/Robot_CreateTrajectory.svg  style="width:30px;"> [Criar trajetória](Robot_CreateTrajectory/pt-br.md): Insere um novo objeto vazio de trajetória na cena.
-   <img alt="" src=images/Robot_SetDefaultOrientation.svg  style="width:30px;"> [Definir a configuração padrão](Robot_SetDefaultOrientation/pt-br.md): Define os pontos de caminho de orientação criados por padrão.
-   <img alt="" src=images/Robot_SetDefaultValues.svg  style="width:30px;"> [Definir o parâmetro padrão de velocidade](Robot_SetDefaultValues/pt-br.md): Define os valores padrões para a criação de pontos de caminho.
-   <img alt="" src=images/Robot_InsertWaypoint.svg  style="width:30px;"> [Inserir um ponto de caminho](Robot_InsertWaypoint/pt-br.md): Insere um ponto de caminho a partir da posição atual do robô em uma trajetória.
-   <img alt="" src=images/Robot_InsertWaypointPre.svg  style="width:30px;"> [Inserir um ponto de caminho pré-selecionado](Robot_InsertWaypointPre/pt-br.md): Insere um ponto de caminho a partir da posição atual do mouse em uma trajetória.

#### Trajetórias Paramétricas 

-   <img alt="" src=images/Robot_Edge2Trac.svg  style="width:30px;"> [Criar uma trajetória fora das arestas](Robot_Edge2Trac/pt-br.md): Insere um novo objeto que decompõe as arestas em uma trajetória.
-   <img alt="" src=images/Robot_TrajectoryDressUp.svg  style="width:30px;"> [Vestir uma trajetória](Robot_TrajectoryDressUp/pt-br.md): Permite que você substitua uma ou mais propriedades de uma trajetória.
-   <img alt="" src=images/Robot_TrajectoryCompound.svg  style="width:30px;"> [Composto de trajetória](Robot_TrajectoryCompound/pt-br.md): Crie um composto a partir de algumas trajetórias únicas.

## Scripting

Veja o exemplo [Robot API](Robot_API_example/pt-br.md) para obter uma descrição das funções utilizadas para modelar os deslocamentos de robô.

## Tutoriais

-   [Robot 6-Axis](Robot_6-Axis/pt-br.md)
-   [Preparação de VRML para simulação de robô](VRML_Preparation_for_Robot_Simulation/pt-br.md)





{{Robot Tools navi

}} 

[<img src="images/Property.png" style="width:16px"> Workbenches](Category_Workbenches.md)

---
[documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > Robot Workbench/pt-br
