# Feature list/pt-br
 

Esta é uma extensa, mas incompleta, lista de recursos que o FreeCAD disponibiliza. Se você quer ter uma noção a futuro, consulte o [Development roadmap](Development_roadmap.md) para uma rápida visão geral do que vem por aí. Além disso, recomenda-se consultar [Capturas de tela](Screenshots/pt-br.md).


{{TOCright}}

## Notas de lançamento 


<div class="mw-translate-fuzzy">

-   [Versão 0.11](Release_notes_0.11.md) - Março de 2011
-   [Versão 0.12](Release_notes_0.12.md) - Dezembro de 2011
-   [Versão 0.13](Release_notes_0.13.md) - Janeiro de 2013
-   [Versão 0.14](Release_notes_0.14.md) - Março de 2014
-   [Versão 0.15](Release_notes_0.15.md) - Março de 2015
-   [Versão 0.16](Release_notes_0.16.md) - Abril de 2016
-   [Versão 0.17](Release_notes_0.17.md) - Abril de 2018
-   [Versão 0.18](Release_notes_0.18.md) - Março de 2019
-   [Versão 0.19](Release_notes_0.19.md) - Março de 2021
-   [Versão 0.20](Release_notes_0.20.md) - TBD


</div>

## Recursos Principais 


<div class="mw-translate-fuzzy">

-   ![](images/Feature1.jpg ) Um **kernel de geometria** completo com base na [tecnologia Open CASCADE](http://en.wikipedia.org/wiki/Open_CASCADE) que permite operações 3D complexas em tipos de formas complexos, com suporte nativo para conceitos como [representação de limite](https://en.wikipedia.org/wiki/Boundary_representation)(brep), curvas e superfícies [não uniformes de spline de base racional](https://en.wikipedia.org/wiki/Non-uniform_rational_B-spline) (nurbs), uma ampla gama de entidades geométricas operações booleanas e [filetes (en)](https://en.wikipedia.org/wiki/Fillet_(mechanics)), e suporte integrado aos formatos [STEP](https://en.wikipedia.org/wiki/ISO_10303) e [IGES](https://en.wikipedia.org/wiki/IGES) 
-   ![](images/Feature3.jpg ) Um **modelo paramétrico** completo. Todos os objetos do FreeCAD são nativamente paramétricos, o que significa que sua forma pode ser baseada em [propriedades](Property/pt-br.md) ou mesmo depender de outros objetos. Todas as alterações são recalculadas sob demanda e registradas por uma pilha de desfazer / refazer. Novos tipos de objetos podem ser adicionados facilmente e podem até ser [totalmente programados em Python](Scripted_objects.md).
-   ![](images/Feature4.jpg ) Uma **arquitetura modular** que permite extensões de plug-in (módulos) para adicionar funcionalidade ao aplicativo principal. Uma extensão pode ser tão complexa quanto um novo aplicativo programado em C ++ ou tão simples quanto um [script Python](Power_users_hub/pt-br.md), ou [macro](macros/pt-br.md) gravada automaticamente. Você tem acesso completo a quase qualquer parte do FreeCAD a partir do interpretador Python embutido, macros ou scripts externos, seja [criação e transformação de geometria](Topological_data_scripting/pt-br.md), representação 2D ou 3D dessa geometria ([Grafo de cena](scenegraph/pt-br.md)) ou mesmo a ['interface' do FreeCAD](PySide/pt-br.md).
-   ![](images/Feature5.jpg ) Importação/exportação de **formatos padrão** como [STEP](http://en.wikipedia.org/wiki/ISO_10303), [IGES](http://en.wikipedia.org/wiki/IGES), [OBJ](http://en.wikipedia.org/wiki/Obj), [STL](http://en.wikipedia.org/wiki/STL_%28file_format%29), [DXF](http://en.wikipedia.org/wiki/Dxf), [SVG](http://en.wikipedia.org/wiki/Svg), [STL](http://en.wikipedia.org/wiki/STL_(file_format)), [DAE](http://en.wikipedia.org/wiki/COLLADA), [IFC](http://en.wikipedia.org/wiki/Industry_Foundation_Classes) ou [OFF](http://people.sc.fsu.edu/~jburkardt/data/off/off.html), [NASTRAN](http://en.wikipedia.org/wiki/NASTRAN), [VRML](http://en.wikipedia.org/wiki/VRML) além do formato de arquivo {{FileName|[FCStd](File_Format_FCStd.md)}} nativo do FreeCAD. O nível de compatibilidade entre o FreeCAD e um determinado formato de arquivo pode variar, pois depende do módulo que o implementa.
-   ![](images/Feature7.jpg ) Um [Sketcher](Sketcher_Workbench/pt-br.md) com solucionador de restrições integrado, permitindo que você esboce formas 2D com restrições geométricas. As formas 2D restritas construídas com Sketcher podem então ser usadas como base para construir outros objetos em todo o FreeCAD.
-   ![](images/Feature9.jpg ) Um módulo [simulação de robôs](Robot_Workbench/pt-br.md) que permite estudar os movimentos dos robôs em um ambiente gráfico. 
-   ![](images/Feature8.jpg ) Um módulo de [desenho técnico](TechDraw_Workbench/pt-br.md) com opções de vistas detalhadas, vistas transversais, dimensionamento e outras, permitindo gerar vistas 2D de modelos 3D existentes. O módulo produz então arquivos SVG ou PDF prontos para exportação. Um módulo de [desenho](Drawing_Workbench/pt-br.md) mais antigo com comandos GUI escassos, mas uma poderosa funcionalidade Python também existe. 
-   ![](images/Feature-raytracing.jpg ) Um módulo de [Renderização](Raytracing_Workbench/pt-br.md) que pode exportar objetos 3D para renderização com renderizadores externos. Atualmente ele só suporta [povray](http://en.wikipedia.org/wiki/POV-Ray) e [LuxRender](http://en.wikipedia.org/wiki/LuxRender), mas espera-se que seja estendido a outros renderizadores no futuro. 
-   ![](images/Feature-arch.jpg ) Um módulo de [Arquitetura](Arch_Workbench/pt-br.md) que permite um fluxo de trabalho semelhante ao da [Modelagem da Informação para Construção](http://en.wikipedia.org/wiki/Building_Information_Modeling) (BIM), com compatibilidade com as [Classes de Fundação da Indústria](http://en.wikipedia.org/wiki/Industry_Foundation_Classes)(IFC). 
-   ![](images/Feature-CAM.jpg ) Um módulo [Path](Path_Workbench/pt-br.md) dedicado à usinagem mecânica para [fabricação assistida por computador](https://en.wikipedia.org/wiki/Computer-aided_manufacturing) (CAM). Usando o módulo Path você pode emitir, exibir e ajustar o [código G](http://en.wikipedia.org/wiki/G-code) usado para controlar a máquina alvo.
-   ![](images/Feature_spreadsheet.png ) Uma [planilha integrada](Spreadsheet_Workbench/pt-br.md) e um [analisador de expressões](Expressions/pt-br.md) que pode ser usado para conduzir modelos baseados em fórmulas e organizar os dados dos modelos em um local central.


</div>


<div class="mw-translate-fuzzy">

## Recursos gerais: 


</div>

-   **multiplataforma**. O FreeCAD roda e se comporta exatamente da mesma forma em Windows, Linux, macOS e outras plataformas.

-   **interface gráfica de usuário(GUI) completa**. FreeCAD tem uma interface gráfica de usuário completa baseada no framework [Qt](https://www.qt.io/), com um visualizador 3D baseado em [Open Inventor](http://en.wikipedia.org/wiki/Open_Inventor); permitindo uma rápida renderização de cenas 3D e uma representação gráfica de cena muito acessível.

-   *\' é executado como uma aplicação de linha de comando*\'. No modo de linha de comando, o FreeCAD roda sem sua 'interface', mas com todas as suas ferramentas de geometria. Neste modo, tem uma área de memória relativamente baixa e pode ser usado, por exemplo, como um servidor para produzir conteúdo para outras aplicações.


<div class="mw-translate-fuzzy">

-   **pode ser importado como um [módulo Python](Embedding_FreeCAD.md)**. O FreeCAD pode ser importado para qualquer aplicação que possa executar script Python. Como no modo de linha de comando, a parte de 'interface' do FreeCAD não está disponível, mas todas as ferramentas de geometria são acessíveis.


</div>

-   **conceito de bancada de trabalho**. Na 'interface' FreeCAD, as ferramentas são agrupadas por [ bancada de trabalho](workbenches/pt-br.md). Isto permite exibir apenas as ferramentas utilizadas para realizar uma determinada tarefa, mantendo o espaço de trabalho livre e responsivo, e permitindo que a aplicação seja carregada rapidamente.

-   **estrutura Plugin/Módulo para características de carregamento e tipos de dados**. O FreeCAD consiste em uma aplicação base com vários módulos, sendo carregados somente quando necessário. A maioria das ferramentas e tipos de geometria são armazenadas em módulos. Os módulos se comportam como plugins; além do carregamento atrasado, módulos individuais podem ser adicionados ou removidos de uma instalação existente do FreeCAD.

-   **objetos parametrizáveis e associativos**. Todos os objetos de um documento do FreeCAD podem ser definidos por parâmetros. Esses parâmetros podem ser modificados e recalculados a qualquer momento. As relações entre objetos são vitais para que a modificação de um parâmetro envolva a modificação de todos os objetos que dele dependem.

-   **criação primitiva paramétrica**. Objetos primitivos tais como paralelepípedo, esfera, cilindro, etc. podem ser criados especificando suas restrições geométricas.

-   **operações de modificação gráfica**. O FreeCAD pode realizar translação, rotação, escalonamento, espelhamento, deslocamento (trivial ou conforme descrito em [Jung/Shin/Choi](https://www.researchgate.net/publication/240754626_Self-intersection_Removal_in_Triangular_Mesh_Offsetting)) ou conversão de forma, em qualquer plano do espaço 3D.

-   **[Geometria sólida construtiva](Constructive_solid_geometry/pt-br.md) (operações booleanas)**. O FreeCAD pode fazer operações de geometria sólida construtiva (união, diferença, interseção).


<div class="mw-translate-fuzzy">

-   **criação gráfica de geometrias planas simples**. Linhas, segmentos, retângulos, b-splines e arcos circulares ou elípticos podem ser criados graficamente em qualquer plano do espaço 3D.


</div>

-   **modelagem utilizando extrusões retas ou revolucionárias**, **seções** e **filetes**.

-   **componentes topológicos** como *\'vértices*, *\'bordas*, **fios** e **planos**.

-   **teste e reparo**. FreeCAD tem ferramentas para testar malhas (teste de sólido, teste de não-duas-variedade, teste de auto-intersecção) e para reparar malhas (preenchimento de furos, orientação uniforme).

-   **anotações**. O FreeCAD pode inserir anotações de texto ou dimensões.

-   **Desfazer/Refazer estrutura**. Tudo no FreeCAD é desfeito/refeito, com acesso do usuário à pilha de desfazer. Várias etapas podem ser desfeitas de uma vez.

-   **orientado à transação**. A pilha desfazer/refazer armazena transações de documentos, não ações isoladas, permitindo que cada ferramenta defina exatamente o que deve ser desfeita ou refeita.

-   **estrutura [scripting](Power_users_hub/pt-br.md) integrada**. O FreeCAD possui um interpretador [Python](http://www.python.org/) embutido, com uma API que cobre praticamente qualquer parte da aplicação, 'interface', geometria e representação desta geometria no visualizador 3D. O interpretador pode executar 'scripts' complexos assim como comandos simples; módulos inteiros podem ser programados completamente em Python.

-   **console Python embutido**. O interpretador Python inclui um console com destaque de sintaxe, autocompletar e um navegador de classe. Os comandos Python podem ser emitidos diretamente no FreeCAD e retornar resultados imediatamente, permitindo que os programadores de scripts testem a funcionalidade em tempo real, explorem o conteúdo dos módulos do FreeCAD e aprendam facilmente sobre os internos do FreeCAD.

-   **espelha a interação do usuário**. Tudo o que o usuário faz na interface FreeCAD executa código Python, que pode ser impresso no console e gravado em macros.

-   **gravação e edição completa de [macro](Macros/pt-br.md)**. Os comandos Python emitidos quando o usuário manipula a 'interface' podem ser gravados, editados, se necessário, e salvos para serem reproduzidos posteriormente.

-   **formato de salvamento de documento composto (baseado em ZIP)**. Os documentos FreeCAD são salvos com uma extensão {{{Nome_do_Arquivo|.[FCStd](File_Format_FCStd/pt-br.md)}}}. O documento pode conter muitos tipos de informações, como geometria, scripts ou ícones em miniatura. O arquivo {{{FileName/pt-br|.FCStd}}} é um contêiner zip; um arquivo FreeCAD salvo já foi comprimido.

-   **'interface' gráfica do usuário totalmente personalizável/'scriptável'**. A 'interface' [Qt](https://www.qt.io) do FreeCAD é inteiramente acessível através do interpretador Python. Além das simples funções que o próprio FreeCAD oferece às bancadas de trabalho, toda a estrutura Qt é acessível. O usuário pode realizar qualquer operação na GUI, como criar, adicionar, acoplar, modificar ou remover 'widgets' e barras de ferramentas.

-   **thumbnailer**. (atualmente apenas sistemas Linux) Os ícones do documento FreeCAD mostram o conteúdo do arquivo na maioria das aplicações de gerenciamento de arquivos, como o Nautilus do Gnome.

-   **instalador MSI modular**. O instalador do FreeCAD permite instalações flexíveis em sistemas Windows. Os pacotes para sistemas Ubuntu também são mantidos.

## Em desenvolvimento 

-   ![](images/Feature-assembly.jpg ) Um módulo [ Assembly](Assembly_project/pt-br.md) que permite trabalhar com vários projetos, várias formas, vários documentos, vários arquivos, vários relacionamentos\... Este módulo está atualmente em estado de planejamento.

## Bancadas de trabalho extra 

Usuários avançados criaram várias [bancadas de trabalho externas](external_workbenches/pt-br.md) personalizadas.







[Category:User Documentation](Category:User_Documentation.md)
