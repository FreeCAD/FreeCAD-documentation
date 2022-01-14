# Feature list/pt
<div class="mw-translate-fuzzy">

Esta é uma lista extensiva, ainda que incompleta dos recursos que o FreeCAD disponibiliza. Se quiser ter uma ideia de como será o FreeCAD no futuro consulte [Development roadmap](Development_roadmap/pt.md) para uma rápida visão geral do que vem aí. Além disso, a consulta de [Screenshots](Screenshots/pt.md) pode ser interessante.


</div>


{{TOCright}}

## Notas da Versão 


<div class="mw-translate-fuzzy">

-   [Versão 0.11](Release_notes_0.11.md) - março 2011
-   [Versão 0.12](Release_notes_0.12.md) - dezembro 2011
-   [Versão 0.13](Release_notes_0.13.md) - janeiro 2013
-   [Versão 0.14](Release_notes_0.14.md) - março 2014
-   [Versão 0.15](Release_notes_0.15/pt.md) - março 2015
-   [Versão 0.16](Release_notes_0.16/pt.md) - abril 2016
-   [Versão 0.17](Release_notes_0.17/pt.md) - abril 2018


</div>

## Recursos Principais 


<div class="mw-translate-fuzzy">

-   ![](images/Feature1.jpg ) Um completo **geometry kernel** baseado [na tecnologia Open CASCADE](http://en.wikipedia.org/wiki/Open_CASCADE) permite operações 3D complexas em vários tipos de formas complexas, com suporte nativo para conceitos como brep, nurbs curves e superficies, um vasto leque de entidades geométricas, operações boleanas e \"fillets\", e suporte interno dos formatos STEP e IGES 
-   ![](images/Feature3.jpg ) Um **Modelo totalmente paramétrico**. Todos os objetos FreeCAD são paramétricos de modo nativo, o que significa que as suas formas podem ser baseadas em [propriedades](Property/pt.md) ou mesmo dependentes de outros objetos, todas as alterações são recalculadas em tempo real, e gravadas na lista de \"undo/redo\". Novos tipos de objetos podem ser adicionados facilmente, e até mesmo [totalmente programados em Python](Scripted_objects/pt.md)
-   ![](images/Feature4.jpg ) **Arquitetura modular** que permite a utilização de \"plugins\" (módulos) para acrescentar funcionalidade à aplicação principal. Estas extensões podem ser tão complexas como novas aplicações completas programadas em C++ ou tão simples como [Python scripts](Power_users_hub/pt.md) ou [macros](macros/pt.md) gravados automaticamente. O utilizador tem acesso completo a partir do interprete de **Python** interno, \"macros\" ou \"scripts\" externos, a praticamente qualquer parte do FreeCAD, seja [criação e transformação de geometria](Topological_data_scripting/pt.md), ou a representação 2D ou 3D dessa geometria ([scenegraph](scenegraph/pt.md)) ou até a [interface do FreeCAD](PySide/pt.md) 
-   ![](images/Feature5.jpg ) Importar/exportar para **formatos standard** como sejam [STEP](http://en.wikipedia.org/wiki/ISO_10303), [IGES](http://en.wikipedia.org/wiki/IGES), [OBJ](http://en.wikipedia.org/wiki/Obj), [STL](http://en.wikipedia.org/wiki/STL_%28file_format%29), [DXF](http://en.wikipedia.org/wiki/Dxf), [SVG](http://en.wikipedia.org/wiki/Svg), [STL](http://en.wikipedia.org/wiki/STL_(file_format)), [DAE](http://en.wikipedia.org/wiki/COLLADA), [IFC](http://en.wikipedia.org/wiki/Industry_Foundation_Classes) ou [OFF](http://people.sc.fsu.edu/~jburkardt/data/off/off.html), [NASTRAN](http://en.wikipedia.org/wiki/NASTRAN), [VRML](http://en.wikipedia.org/wiki/VRML) além do [ Formato de ficheiro Fcstd](Fcstd_file_format/pt.md) nativo do FreeCAD\'s. O nivel de compatibilidade entre o FreeCAD e um determinado formato de ficheiro pode variar, uma vez que isso depende do modulo que o implementa.
-   ![](images/Feature7.jpg ) Uma [ Bancada de trabalho Esboço (Sketcher)](Sketcher_Workbench/pt.md) com resolvedor de restrições, permite esboçar formas 2D com geometria-restringida. O \"sketcher\" correntemente permite construir vários tipos de geometria restringida, e usá-la como base para construir outros objetos em FreeCAD.
-   ![](images/Feature9.jpg ) Um módulo [Robot simulation](Robot_Workbench/pt.md) que permite estudar os movimentos robotizados. O módulo robot já possui uma interface gráfica extensa que permite um fluxo de trabalho inteiramente gráfico.
-   ![](images/Feature8.jpg ) Um módulo [Folhas de desenho](Drawing_Workbench/pt.md) que permite inserir vistas 2D dos modelos 3D numa folha de desenho. Este módulo produz folhas em SVG ou PDF prontas a exportar. Este módulo encontra-se ainda pouco desenvolvido mas já possui recursos que permitem poderosas funcionalidades Python.
-   ![](images/Feature-raytracing.jpg ) Um módulo [Renderização](Raytracing_Workbench/pt.md) capaz de exportar objetos 3D para renderizar com renderizadores externos. De momento apenas suporta [povray](http://en.wikipedia.org/wiki/POV-Ray) e [LuxRender](http://en.wikipedia.org/wiki/LuxRender), mas espera-se que venha a ser extendido com outros renderizadores no futuro.
-   ![](images/Feature-arch.jpg ) Um Módulo [Arquitetura](Arch_Workbench/pt.md) que permite um fluxo de trabalho tipo-[BIM](http://en.wikipedia.org/wiki/Building_Information_Modeling), com compatibilidade [IFC](http://en.wikipedia.org/wiki/Industry_Foundation_Classes). A criação do módulo de Arquitetura é amplamente discutido pela comunidade [aqui](http://forum.freecadweb.org/viewtopic.php?f=10&t=821).


</div>


<div class="mw-translate-fuzzy">

## Recursos Gerais 


</div>


<div class="mw-translate-fuzzy">

-   **FreeCAD é multiplataforma**. Executa-se e comporta-se exactamente da mesma maneira em Windows, Linux e MacOS.


</div>


<div class="mw-translate-fuzzy">

-   **FreeCAD é uma aplicação totalmente GUI**. O FreeCAD conta com uma completa interface gráfica de utilizador baseada no famoso framework [Qt](http://www.qtsoftware.com/), com um visualizador 3D baseado em [Open Inventor](http://en.wikipedia.org/wiki/open_inventor), que permite uma rápida renderização das cenas 3D e uma representação gráfica muito acessível.


</div>


<div class="mw-translate-fuzzy">

-   **FreeCAD também se executa como uma aplicação de linha de comandos**, com menos requisitos de memória. No modo de linha de comandos, o FreeCAD corre sem a sua interface gráfica, mas com todas as ferramentas de geometria. Pode ser, por exemplo, utilizado como servidor para produzir conteúdos para outras aplicações.


</div>


<div class="mw-translate-fuzzy">

-   **FreeCAD pode ser importado como um [módulo de Python](Embedding_FreeCAD/pt.md)**, dentro de outras aplicações que possam executar scripts Python, ou numa consola Python. Tal como no modo consola, a parte do interface do FreeCAD não está disponível, mas todas as ferramentas de geometria ficam acessíveis.


</div>


<div class="mw-translate-fuzzy">

-   **Conceito de bancada de trabalho**: No interface do FreeCAD, as ferramentas estão agrupadas em [ Bancadas de trabalho](workbenches/pt.md). Isto permite mostrar apenas as ferramentas necessárias para realizar uma determinada tarefa, mantendo o espaço de trabalho arrumado e disponível, e um arranque rápido da aplicação.


</div>


<div class="mw-translate-fuzzy">

-   **\"Framework\" de Plugin/Módulos para carregamento retardado de recursos/tipos-de-dados**. O FreeCAD está dividido em aplicações principais e módulos, que são carregados apenas quando são necessários. Quase todas as ferramentas e tipos de geometria são armazenados em módulos. Os módulos comportam-se como plugins, e podem ser adicionados ou removidos à instalação existente do FreeCAD.


</div>


<div class="mw-translate-fuzzy">

-   **Objetos de documento com associação paramétrica**: Todos os objetos num documento FreeCAD podem ser definidos por parâmetros. Esses parâmetros podem ser modificados dinamicamente, e recalculados a qualquer momento. A relação entre entre objetos também é guardada, pelo que ao modificar um objeto também se modificam os objetos de pendentes.


</div>


<div class="mw-translate-fuzzy">

-   **Criação de primitivas paramétricas** (caixas, esferas, cilindros, etc)


</div>


<div class="mw-translate-fuzzy">

-   **Operações de modificação** gráficas como translações, rotações, escala, simetria, deslocamento paralelo (offset) (normais ou de acordo com \[<http://www.ann.jussieu.fr/~frey/papers/meshing/Jung%20W>.,%20Self-intersection%20removal%20in%20triangular%20mesh%20offsetting.pdf Jung/Shin/Choi\]) ou conversão de formas, em qualquer plano do espaço 3D


</div>


<div class="mw-translate-fuzzy">

-   **[Operações boleanas](http://en.wikipedia.org/wiki/Constructive_solid_geometry)** (união, diferença, interseção)


</div>


<div class="mw-translate-fuzzy">

-   Criação gráfica de **elementos simples de geometria plana** tais como linhas, polilinhas, retângulos, arcos ou círculos em qualquer plano do espaço 3D


</div>


<div class="mw-translate-fuzzy">

-   Modelação com **extrusão ou revolução, secções** e **boleados** (fillets).


</div>


<div class="mw-translate-fuzzy">

-   Componentes topológicos como **vértices, arestas, polilinhas** e **planos** (por programação em Python).


</div>


<div class="mw-translate-fuzzy">

-   **Testar e reparar** ferramentas para malhas: Testar sólidos, Testar malhas não solidas (non-two-manifolds), teste de auto-interseção, preenchimento de buracos e orientação uniforme.


</div>


<div class="mw-translate-fuzzy">

-   **Anotações** como textos ou cotas dimensionais


</div>


<div class="mw-translate-fuzzy">

-   \"Framework\" **desfazer/Refazer**: Todas as acções admitem os processos desfazer/refazer, com acesso ao historial de ações, de maneira que num único passo podem-se desfazer múltiplas acções.


</div>


<div class="mw-translate-fuzzy">

-   **Gestão de transacções**: A lista do historial desfazer/refazer armazena transacções de documentos e não só acções individuais. O que permite definir exactamente o que há que se desfazer ou se refazer com a cada ferramenta.


</div>


<div class="mw-translate-fuzzy">

-   **Framework de [programação](Scripting/pt.md) incorporada**: O FreeCAD conta com um interprete [Python](http://www.python.org/) incorporado, e uma API que cobre quase qualquer parte da aplicação, o interface, a geometria e a representação dessa geometria no visualizador 3D. O interprete pode correr desde simples comandos até scripts complexos, de facto mesmo módulos inteiros podem ser programados completamente em Python.


</div>


<div class="mw-translate-fuzzy">

-   **Consola Python incorporada** com destaques de sintaxe, auto-completar e navegador de classe: Os comandos Python podem ser introduzidos diretamente no FreeCAD e os resultados surgem de imediato, permitindo escrita de scripts para testar funcionalidades em tempo real, explore o conteúdo dos módulos e aprenda facilmente sobre o interior do FreeCAD.


</div>


<div class="mw-translate-fuzzy">

-   **Interação do utilizador espelhada na consola**: Tudo o que o utilizador faz no interface do FreeCAD executa código python, que pode ser mostrado na consola e gravado em macros.


</div>


<div class="mw-translate-fuzzy">

-   **Gravação e edição completa de macros**: Os comandos python gerados quando o utilizador manipula a interface podem ser então gravados, editados se necessário, e salvos para serem reproduzidos mais tarde.


</div>


<div class="mw-translate-fuzzy">

-   **Gravação de documento em formato composto (basedo em ZIP)**: Os documentos do FreeCAD salvos com a extensão .[fcstd](fcstd_file_format.md) podem conter diferentes tipos de informação, como geometria, scripts ou ícones de miniatura. O ficheiro .fcstd é ele próprio um contentor zip, pelo que os ficheiros gravados pelo FreeCAD já estão comprimidos.


</div>


<div class="mw-translate-fuzzy">

-   **Interface Gráfica do Utilizador totalmente personalizável/programável**. A interface do FreeCAD baseada em [Qt](http://www.qtsoftware.com) é inteiramente acessível pelo interprete python. Além das funções simples que o FreeCAD ele próprio disponibiliza para as bancadas de trabalho, toda a framework Qt está também acessível, permitindo qualquer operação no GUI, como criar, adicionar, ancorar, modificar ou remover \"widgets\" e barras de ferramentas.


</div>


<div class="mw-translate-fuzzy">

-   **Miniaturas** (apenas em sistemas Linux neste momento): Os ícones dos documentos do FreeCAD mostram o conteúdo dos ficheiros na maioria dos gestores de ficheiros como por exemplo no nautilus em gnome.


</div>


<div class="mw-translate-fuzzy">

-   **Instalador MSI modular** permite uma instalação flexível em sistemas baseados em Windows. Também são disponibilizados pacotes para sistemas Ubuntu.


</div>

## Em desenvolvimento 


<div class="mw-translate-fuzzy">

-   ![](images/Feature-assembly.jpg ) Um modulo de [Assemblagem (montagem)](Assembly_project.md) que permite trabalhar com múltiplos projetos, múltiplas formas, múltiplos documentos, múltiplos ficheiros, múltiplas relações\...


</div>


<div class="mw-translate-fuzzy">

## Bancadas de trabalho Extra 

Utilizadores avançados criaram várias [Bancadas de trabalho externas](external_workbenches/pt.md) personalizadas.


</div>


<div class="mw-translate-fuzzy">


{{docnav/pt|[Visão Geral](About_FreeCAD/pt.md)|[Instalação em Windows](Install_on_Windows/pt.md)}}


</div>




[<img src="images/Property.png" style="width:16px"> User Documentation](Category_User_Documentation.md)

---
[documentation index](../README.md) > [User Documentation](Category_User Documentation.md) > Feature list/pt
