# <img alt="" src=images/Crystal_Clear_app_tutorials.png  style="width:64px;"> Developer hub/pt-br



Este é o lugar para vir se você quiser contribuir para o desenvolvimento do programa FreeCAD.

Estas páginas estão em estágio inicial de desenvolvimento. Se você não conseguir encontrar as informações que procura ou se encontrou informações úteis em algum lugar para o qual não fornecemos links, por favor, deixe um comentário no [fórum](http://forum.freecadweb.org/index.php?sid=5f84150e79db8842e277b042077097ff) e alguém irá investigar (ou, se estiver se sentindo corajoso, por que não editar esta página diretamente!).



## Documentação do desenvolvedor 

A documentação do desenvolvedor compreende as seguintes seções:



### Compilação do FreeCAD 

-   [repositório Github](https://github.com/FreeCAD/FreeCAD). Se você é novo no git, leia [Gerenciamento de código-fonte](Source_code_management/pt-br.md)
-   [Compilar com Docker](Compile_on_Docker/pt-br.md)
-   [Compilando no Windows](Compile_on_Windows/pt-br.md)
-   [Compilando no Linux](Compile_on_Linux/pt-br.md)
-   [Compilando no MacOS](Compile_on_MacOS/pt-br.md)
-   [Detalhes da licença](License/pt-br.md) sobre as licenças do FreeCAD
-   [Bibliotecas de Terceiros](Third_Party_Libraries/pt-br.md)
-   [Ferramentas de terceiros](Third_Party_Tools/pt-br.md)
-   [Inicialização e Configuração](Start_up_and_Configuration/pt-br.md)
-   [Documentação fonte](Source_documentation/pt-br.md)
-   Use o [bug tracker](Tracker/pt-br.md) quando você tiver um problema ou achar que pode ter encontrado um bug



### Empacotamento

[Empacotamento](Packaging/pt-br.md) consiste em pegar os binários compilados e os arquivos fonte Python do FreeCAD, e distribuí-los para uso em um sistema específico.

-   [Empacotamento Linux](Linux_packaging/pt-br.md)
    -   [Desenvolvimento Debian](Debian_development/pt-br.md)
    -   [Debian instável](Debian_Unstable/pt-br.md)
    -   [Pacote de compilação Git](Git_buildpackage/pt-br.md)
-   [Empacotamento do Windows](Windows_packaging/pt-br.md)
-   [Empacotamento MacOS](MacOS_packaging.md)



### Construir ferramentas de suporte 

-   A [Ferramenta de Construção FreeCAD](FreeCAD_Build_Tool/pt-br.md)
    -   [Adicionando um módulo de aplicativo](Workbench_creation/pt-br.md) ao FreeCAD
-   [Depuração](Debugging/pt-br.md) FreeCAD
-   [Teste](Testing/pt-br.md) FreeCAD
-   [Compilando (Acelerando)](Compiling_(Speeding_up)/pt-br.md) FreeCAD
-   [Integração Contínua](Continuous_Integration/pt-br.md)



### Modificando o FreeCAD 

-   Compreendendo [O código-fonte do FreeCAD](The_FreeCAD_source_code/pt-br.md)
-   [Enviando patches](Tracker/pt-br#Submitting_patches.md)
-   Adicione [Comandos de interface gráfica](Gui_Command/pt-br.md) ao FreeCAD ou a uma bancada de trabalho
-   [Branding](Branding/pt-br.md) ou *como dar ao FreeCAD uma aparência única*
-   [Artwork](Artwork/pt-br.md) que fizemos para o FreeCAD, que você pode reutilizar livremente
-   [Diretrizes de arte](Artwork_Guidelines/pt-br.md) padrões para ícones
-   [Tradução do FreeCAD](Localisation/pt-br.md)
-   [Módulos python extras](Extra_python_modules/pt-br.md), ou *como estender a funcionalidade python dentro do FreeCAD*
-   [Google Summer of Code](Google_Summer_of_Code_2024.md) participe por meio do programa de suporte estudantil do Google
-   [Ajuste fino](Fine-tuning/pt-br.md) mostra diferentes opções e opções de parâmetros que podem superar problemas
-   [Envolvendo uma classe C++ em Python](Wrapping_a_Cplusplus_class_in_Python/pt-br.md) mostra como criar o wrapper Python para uma classe C++
-   [Lista de verificação para adicionar um recurso a um ambiente de trabalho C++](NewFeatureCheckList_C++.md) fornece uma ajuda para contribuidores.

-   [Traduzindo um ambiente de trabalho externo](Translating_an_external_workbench/pt-br.md)



### Guia do desenvolvedor do módulo 

[FreeCAD Mod Dev Guide](https://github.com/qingfengxia/FreeCAD_Mod_Dev_Guide): Este é um e-book escrito no github, bifurque e envie uma solicitação pull para contribuir.

Capítulos:

-   Visão geral e arquitetura de software
-   Estrutura do código-fonte
-   Módulo Base e App
-   Módulo Gui
-   Envolvimento do Python
-   Projeto modular
-   Análise da fonte do módulo Fem (mistura de C++ e Python)
-   Desenvolvimento do módulo CFD (Python puro)
-   Teste e depuração do módulo
-   Contribuição de código com o git

A amostra mais recente do PDF pode ser baixada na [pasta de PDF](https://github.com/qingfengxia/FreeCAD_Mod_Dev_Guide/tree/master/pdf) deste repositório git.



### Internos



#### Documentação do OpenCascade 

OpenCascade é uma plataforma de desenvolvimento de software para modelagem 3D de superfícies e sólidos, troca de dados CAD e visualização, principalmente na forma de bibliotecas em C++.

-   [Tutoriais de Roman Lygin](http://opencascade.wikidot.com/romansarticles)
-   [Documentação on-line completa](https://dev.opencascade.org/cdoc/overview/html/index.html)
-   [Manual de referência](https://dev.opencascade.org/doc/refman/html/index.html)
-   [O wiki openCascade](http://opencascade.wikidot.com) (atualmente contendo ?? spam chinês)



#### Formato de arquivo 

[Formato de arquivo FCStd](File_Format_FCStd/pt-br.md). Os arquivos criados com FreeCAD são arquivos `.zip` que incluem a geometria [BREP](https://en.wikipedia.org/wiki/Boundary_representation), bem como dados XML que descrevem o documento.



#### Solucionador de esboços 

-   [Sketcher Solver Architecture Booklet](https://forum.freecadweb.org/viewtopic.php?f=10&t=36355) (tópico do fórum), [source](https://github.com/abdullahtahiriyo/FreeCADBooks/tree/master/FreeCAD_Solver_Architecture) no GitHub.
-   [PlaneGCS solver](https://github.com/FreeCAD/FreeCAD/blob/master/src/Mod/Sketcher/App/planegcs/) no código-fonte do FreeCAD; arquivos importantes são [GCS.cpp](https://github.com/FreeCAD/FreeCAD/blob/master/src/Mod/Sketcher/App/planegcs/GCS.cpp) e [/blob/master/src/Mod/Sketcher/App/planegcs/SubSystem.cpp SubSystem.cpp](https://github.com/FreeCAD/FreeCAD).
-   [Várias melhorias recentes no Sketcher](https://forum.freecadweb.org/viewtopic.php?f=9&t=29192).

O solucionador de sketcher não é perfeito, pois há alguns problemas com precisão numérica ao usar valores grandes, consulte [Aventura de consertar o solucionador de sketcher para esboços grandes](https://forum.freecadweb.org/viewtopic.php?f=10&t=40502).

O desenvolvimento de uma nova arquitetura de solucionador poderia melhorar a forma como o solucionador é utilizado tanto no [Sketcher Workbench](Sketcher_Workbench.md), quanto para montagem de corpos 3D. Consulte [Reimplementando o solucionador de restrições](https://forum.freecadweb.org/viewtopic.php?f=20&t=40525).



## Roteiro

Embora o FreeCAD seja utilizável em certas áreas, ainda está no início de um longo caminho rumo à adoção generalizada no mercado de CAD. Ainda há muito a ser feito para alcançar um estado no qual possamos competir com o software comercial.

[Ciclo de desenvolvimento do FreeCAD 1.0](FreeCAD_1.0_Development_Cycle.md)



## Comunidade

[IRC channel](ircs://irc.libera.chat:6697/freecad) ,sincronizado com [gitter channel](https://gitter.im/FreeCAD/FreeCAD)

-   [Fórum de desenvolvimento](https://forum.freecad.org/viewforum.php?f=6)

-   [Roteiro de desenvolvimento](Development_roadmap/pt-br.md)

## Créditos

[Colaboradores](Contributors.md)



---
⏵ [documentation index](../README.md) > [Hubs](Category_Hubs.md) > [Developer Documentation](Category_Developer Documentation.md) > Developer hub/pt-br
