# Feature list/pt-br
Esta é lista recursos uma extensa, porém incompleta, que o FreeCAD disponibiliza.






## Notas da Versão 

-   [Versão 0.20](Release_notes_0.20.md) - Junho de 2022
-   [Versão 0.19](Release_notes_0.19.md) - Março de 2021
-   [Versão 0.18](Release_notes_0.18.md) - Março de 2019
-   [Versão 0.17](Release_notes_0.17.md) - Abril de 2018
-   [Versão 0.16](Release_notes_0.16.md) - Abril de 2016
-   [Versão 0.15](Release_notes_0.15.md) - Março de 2015
-   [Versão 0.14](Release_notes_0.14.md) - Março de 2014
-   [Versão 0.13](Release_notes_0.13.md) - Janeiro de 2013
-   [Versão 0.12](Release_notes_0.12.md) - Dezembro de 2011
-   [Versão 0.11](Release_notes_0.11.md) - Março de 2011



## Recursos Principais 


<div class="mw-translate-fuzzy">

-   ![](images/Feature1.jpg ) Um **kernel de geometria** completo com base na [tecnologia Open CASCADE](http://en.wikipedia.org/wiki/Open_CASCADE) que permite operações complexas formas 3D, com suporte nativo para sólidos B-rep [representação de limite](https://en.wikipedia.org/wiki/Boundary_representation), curvas e superfícies NURBS ([curvas B-spline não-uniformes e de base racional](https://en.wikipedia.org/wiki/Non-uniform_rational_B-spline)), uma ampla gama de possibilidades de geração de sólidos por operações booleanas e uso de [filetes (en)](https://en.wikipedia.org/wiki/Fillet_(mechanics)), e suporte integrado aos formatos [STEP](https://en.wikipedia.org/wiki/ISO_10303) e [IGES](https://en.wikipedia.org/wiki/IGES) 

-   ![](images/Feature3.jpg ) Um **modelo paramétrico** completo. Todos os objetos do FreeCAD são nativamente paramétricos, o que significa que sua forma pode ser baseada em [propriedades](Property/pt-br.md) ou mesmo depender de outros objetos. Todas as alterações são recalculadas sob demanda e registradas por uma pilha de desfazer e refazer. Novos tipos de objetos podem ser adicionados facilmente e podem até ser [totalmente programados em Python](Scripted_objects.md).

-   ![](images/Feature4.jpg ) Uma **arquitetura modular** que permite utilizar extensões (plug-ins) para adicionar funcionalidade ao núcleo principal do aplicativo. Uma extensão pode ser tão complexa quanto um novo aplicativo programado em C ++ ou tão simples quanto um [script Python](Power_users_hub/pt-br.md), ou [macro](macros/pt-br.md) gravado automaticamente. Você tem acesso completo a quase qualquer parte do FreeCAD a partir do interpretador Python embutido, pode criar macros ou scripts externos, seja para realizar a [criação e transformação de geometrias](Topological_data_scripting/pt-br.md), a representação 2D ou 3D destas geometrias ([Grafo de cena](scenegraph/pt-br.md)) ou mesmo alterar a [interface do FreeCAD](PySide/pt-br.md).

-   ![](images/Feature5.jpg ) Importação e exportação de **formatos padrão** como [STEP](http://en.wikipedia.org/wiki/ISO_10303), [IGES](http://en.wikipedia.org/wiki/IGES), [OBJ](http://en.wikipedia.org/wiki/Obj), [STL](http://en.wikipedia.org/wiki/STL_%28file_format%29), [DXF](http://en.wikipedia.org/wiki/Dxf), [SVG](http://en.wikipedia.org/wiki/Svg), [STL](http://en.wikipedia.org/wiki/STL_(file_format)), [DAE](http://en.wikipedia.org/wiki/COLLADA), [IFC](http://en.wikipedia.org/wiki/Industry_Foundation_Classes) ou [OFF](http://people.sc.fsu.edu/~jburkardt/data/off/off.html), [NASTRAN](http://en.wikipedia.org/wiki/NASTRAN), [VRML](http://en.wikipedia.org/wiki/VRML) além do formato de arquivo **[FCStd](File_Format_FCStd.md)** nativo do FreeCAD. O nível de compatibilidade entre o FreeCAD e um determinado formato de arquivo pode variar, pois depende do módulo que o implementa.

-   ![](images/Feature7.jpg ) [Sketcher](Sketcher_Workbench/pt-br.md), um módulo de desenho com gestão integrada de restrições geométricas, para que você crie formas 2D que podem obedecer a tais restrições. As formas 2D restritas construídas com o Sketcher podem ser usadas como base para construir outros objetos em todo o FreeCAD.

-   ![](images/Feature9.jpg ) [Simulação de robôs](Robot_Workbench/pt-br.md), módulo que permite estudar os movimentos dos robôs em um ambiente gráfico.

-   ![](images/Feature8.jpg ) [Techdraw](TechDraw_Workbench/pt-br.md), módulo para geração de pranchas com documentação técnica, com ferramentas para a exibição de vistas detalhadas e vistas de corte, recursos para o dimensionamento dos objetos, entre outros, permitindo gerar vistas 2D a partir de modelos 3D. Com o Techdraw é possível exportar as pranchas em arquivos SVG ou PDF. O módulo [Drawing](Drawing_Workbench/pt-br.md), mais antigo, com poucos comandos em interface gráfica, mas com poderosas funções Python, também está disponível.

-   ![](images/Feature-raytracing.jpg ) [Raytracing](Raytracing_Workbench/pt-br.md), módulo que serve para exportar objetos 3D para serem utilizados em renderizadores externos. Atualmente o Raytracing tem suporte ao [povray](http://en.wikipedia.org/wiki/POV-Ray) e o [LuxRender](http://en.wikipedia.org/wiki/LuxRender) e espera-se que seja estendido a outros renderizadores no futuro. 

-   ![](images/Feature-arch.jpg ) [Arch](Arch_Workbench/pt-br.md), módulo que permite um fluxo de trabalho semelhante ao da bancada [BIM](http://en.wikipedia.org/wiki/Building_Information_Modeling), e que tem compatibilidade com o padrão[IFC](http://en.wikipedia.org/wiki/Industry_Foundation_Classes). 

-   ![](images/Feature-CAM.jpg ) [Path](Path_Workbench/pt-br.md), módulo dedicado à usinagem mecânica para [CAM fabricação assistida por computador](https://en.wikipedia.org/wiki/Computer-aided_manufacturing). Usando o módulo Path você pode emitir, exibir e ajustar o [G-code](http://en.wikipedia.org/wiki/G-code) usado para controlar a máquina a ser utilizada.

-   ![](images/Feature_spreadsheet.png ) [Spreadsheet](Spreadsheet_Workbench/pt-br.md) e [Expressions](Expressions/pt-br.md), módulos que podem ser usados para desenvolver modelos baseados em fórmulas e organizar os dados dos modelos em um local central.


</div>



## Recursos gerais: 

-   **multiplataforma**. O FreeCAD roda e se comporta exatamente da mesma forma em Windows, Linux, macOS e outras plataformas.

-   **interface gráfica de usuário (GUI) completa**. O FreeCAD tem uma interface gráfica de usuário completa, baseada no framework [Qt](https://www.qt.io/), com um visualizador 3D baseado em [Open Inventor](http://en.wikipedia.org/wiki/Open_Inventor), o que permite uma rápida renderização de cenas 3D e uma representação gráfica de alta qualidade.

-   **pode ser utilizado como um aplicativo baseado em linhas de comando**. No modo de linhas de comando, o FreeCAD roda sem sua interface gráfica para o usupario (GUI), mas com todas as suas ferramentas de geometria. Este modo de trabalho faz uso de menos memória RAM que o modo GUI e pode ser usado, por exemplo, como um servidor para produzir conteúdo para outras aplicações.

-   **pode ser importado como um [módulo Python](Embedding_FreeCAD.md)**. O FreeCAD pode ser importado para qualquer aplicação que possa executar scripts em Python. Assim como ocorre no modo de linhas de comando, a interface gráfica do usuário (GUI) do FreeCAD não fica disponível, mas todas as ferramentas de geometria continuam acessíveis.


<div class="mw-translate-fuzzy">

-   **conceito de bancada de trabalho**. Na interface gráfica de usuário (GUI) do FreeCAD, as ferramentas são agrupadas por [ bancada de trabalho](workbenches/pt-br.md). Cada bancada pode conter apenas as ferramentas utilizadas para realizar uma determinada tarefa, contribuindo para manter o espaço de trabalho livre e responsivo e permitindo que a aplicação seja carregada rapidamente.


</div>

-   **posibilidade de realizar o carregamento posterior de funções e dados, por meio das estruturas Plugin e Módulo**. O FreeCAD é constituído por uma aplicação-base e por vários módulos, que são carregados quando necessário. A maior parte das ferramentas e tipos de geometria são armazenadas em módulos. Os módulos se comportam como plug-ins, pois podem ser carregados automaticamente sob demanda, e módulos externos ao desenvolvimento base do FreeCAD podem ser adicionados ou removidos.

-   **objetos parametrizáveis e associativos**. Em um documento do FreeCAD, todos os objetos podem ser definidos por parâmetros, que podem ser modificados e recalculados a qualquer momento. As relações entre objetos são vitais para que a modificação de um parâmetro possa ser utilizada para modificar parâmetros de todos os objetos que dele dependem.

-   **criação paramétrica d eprimitivas geométricas**. Primitivas geométricas, como paralelepípedo, esfera, cilindro, etc. podem ser criadas a partir da especificação de suas restrições.

-   **operações de modificação gráfica**. O FreeCAD pode executar translação, rotação, dimensionamento, espelhamento, deslocamento (triviais ou conforme descrito em [Jung/Shin/Choi](https://www.researchgate.net/publication/240754626_Self-intersection_Removal_in_Triangular_Mesh_Offsetting)) ou conversão de formas, em qualquer plano do espaço 3D.

-   **[Geometria Construtiva de Sólidos](Constructive_solid_geometry/pt-br.md) por operações booleanas**. O FreeCAD pode fazer operações CSG para criar e editar sólidos por união, diferença e intersecção.

-   **criação gráfica de geometria plana**. Linhas, fios, retângulos, B-splines e arcos circulares ou elípticos, podem ser criados graficamente em qualquer plano do espaço 3D.

-   **modelagem de extrusões, seções ou filetes a partir do uso de perfis**, **que seguem uma direção reta** ou **que giram ao redor de um eixo**.

-   **componentes topológicos** como **vértices\'\',**arestas\'\', **fios** e **planos**.

-   **testes e reparos**. FreeCAD tem ferramentas para testar a integridade de malhas (teste de sólidos, teste de superfícies (non-two-dimensional manifold), teste de auto-intersecção) e para reparar malhas (preenchimento de furos, orientação uniforme).

-   **anotações**. O FreeCAD pode inserir anotações para texto ou dimensões.

-   **Desfazer/Refazer estrutura**. Tudo no FreeCAD é desfeito/refeito, com acesso do usuário à pilha de ações. Várias etapas podem ser desfeitas de uma vez.

-   **orientado à transação**. A pilha desfazer/refazer armazena transações realizados nos documentos (e não ações isoladas), permitindo que cada ferramenta defina exatamente o que deve ser desfeito ou refeito.

-   **estrutura [scripting](Power_users_hub/pt-br.md) integrada**. O FreeCAD possui um interpretador [Python](http://www.python.org/) embutido, com uma API que cobre praticamente qualquer parte da aplicação, da interface, da geometria e da representação desta geometria no visualizador 3D. O interpretador pode executar comandos simples e scripts complexos; módulos inteiros podem ser programados completamente em Python.


<div class="mw-translate-fuzzy">

-   **console Python embutido**. O interpretador Python inclui um console com os recursos de destaque de sintaxe, autocompletar e um navegador de classe. Os comandos em Python podem ser emitidos diretamente no FreeCAD e retornar resultados imediatamente, permitindo que os programadores realizaem testes em tempo real, explorem o conteúdo dos módulos do FreeCAD e aprendam mais facilmente como funcionam os comandos que estruturam o FreeCAD internamente.


</div>


<div class="mw-translate-fuzzy">

-   **espelha a interação do usuário**. Tudo o que o usuário faz na interface FreeCAD é executado por em código Python, que são impressos no console e podem ser gravados como macros.


</div>

-   **gravação e edição completa de [macros](Macros/pt-br.md)**. Os comandos Python, emitidos quando o usuário manipula a interface, podem ser gravados, editados e, se necessário, salvos para serem reproduzidos posteriormente.


<div class="mw-translate-fuzzy">

-   **formato de salvamento de documento composto (baseado em ZIP)**. Os documentos FreeCAD são salvos com a extensão {{{Nome_do_Arquivo|.[FCStd](File_Format_FCStd/pt-br.md)}}}. O documento pode conter muitos tipos de informações, como a geometria dos objetos, scripts ou ícones em miniatura. O arquivo {{{FileName/pt-br|.FCStd}}} é um contêiner zip, ou seja, os dados de um documento FreeCAD, ao serem salvos, já são comprimidos em ZIP.


</div>

-   **interface gráfica do usuário totalmente personalizável/scriptável**. A interface [Qt](https://www.qt.io) do FreeCAD é inteiramente acessível através do interpretador Python. Além das simples funções que o próprio FreeCAD oferece às bancadas de trabalho, toda a estrutura Qt é acessível. O usuário pode realizar qualquer operação na GUI, como criar, adicionar, acoplar, modificar ou remover 'widgets' e barras de ferramentas.

-   **thumbnailer**. (atualmente apenas sistemas Linux) Os ícones do documento FreeCAD mostram o conteúdo do arquivo na maioria das aplicações de gerenciamento de arquivos, como o Nautilus do Gnome.

-   **Instalador MSI modular**. O instalador do FreeCAD permite instalações flexíveis em sistemas Windows. Pacotes para sistemas Ubuntu(baseados em Debian) também são mantidos.



## Bancadas de Trabalho Externas 

Diversas [bancadas de trabalho alternativas](External_workbenches/pt-br.md) foram criadas por usuários avançados e podem sem facilmente instaladas no seu FreeCAD. Uma lista delas está disponível na página [Bancadas de Trabalho Externas](External_workbenches/pt-br.md)



---
⏵ [documentation index](../README.md) > [User Documentation](Category_User Documentation.md) > Feature list/pt-br
