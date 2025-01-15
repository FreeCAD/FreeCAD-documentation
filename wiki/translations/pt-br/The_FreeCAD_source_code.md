# The FreeCAD source code/pt-br
O [FreeCAD source code](https://github.com/FreeCAD/FreeCAD) é gerenciado com git e é público, aberto e disponível sob a licença [LGPL](https://en.wikipedia.org/wiki/GNU_Lesser_General_Public_License). Pode ser copiado, baixado, lido, analisado, redistribuído e modificado por qualquer pessoa. Se você planeja fazer modificações que deseja ver incluídas no próprio código oficial, lembre-se de que suas alterações precisarão ser aprovadas pelos desenvolvedores do FreeCAD, por isso é aconselhável discutir primeiro suas intenções em \[http: // forum.freecadweb.org forum\] para evitar o risco de ter suas alterações rejeitadas por algum motivo que você não previu.

Abaixo estão algumas dicas e informações úteis para colocar você nos trilhos, caso esteja interessado em explorar o código do FreeCAD.

-   O código do FreeCAD é principalmente programado em **C++**, mas depende significativamente do **Python**. Uma grande parte de sua funcionalidade é fornecida através de ligações Python associadas, e faz parte da filosofia central do desenvolvimento do FreeCAD sempre oferecer acesso via Python a qualquer novo recurso implementado em C++. Para alcançar isso, o CPython (as ferramentas de interface C fornecidas pelo próprio Python) e especialmente o [PyCXX](http://cxx.sourceforge.net/) são amplamente utilizados em todo o FreeCAD. Além disso, muitos modelos e ferramentas personalizadas são fornecidos no próprio código do FreeCAD para facilitar a criação de ligações Python associadas. Algumas partes mais de alto nível do código do FreeCAD são totalmente codificadas em Python.

-   O código fonte do FreeCAD é completamente **multiplataforma**, e é dedicado um grande cuidado para garantir que a aplicação possa ser utilizada em tantas plataformas e configurações quanto possível, sem causar dificuldades aos usuários existentes. Portanto, sempre que possível, são evitadas novas versões de componentes necessários até que estejam amplamente disponíveis em todas as plataformas, e a compatibilidade com versões anteriores (a capacidade de abrir um arquivo criado com uma versão antiga do FreeCAD em uma versão mais recente) é uma prioridade importante.

-   Quase todas as funcionalidades do FreeCAD são divididas em duas partes distintas, denominadas **App** e **Gui**. Essa divisão é refletida em toda a estrutura de arquivos do código-fonte. O módulo App contém todas as funcionalidades que precisam ser executadas no modo de console puro (sem GUI). Como o FreeCAD pode ser compilado e executado sem sua Interface Gráfica do Usuário, o código no módulo App é independente de qualquer biblioteca relacionada à GUI. Já o módulo Gui contém todo o código necessário para ser executado no modo GUI e é construído em torno da funcionalidade do módulo App.

-   A maioria das funcionalidades do FreeCAD é implementada em **Módulos**. O FreeCAD sem seus módulos é apenas uma janela contêiner simples que pode abrir e salvar arquivos. Todas as ferramentas de geometria e bancadas de trabalho são implementadas nos Módulos. Esses módulos podem ser escritos em C++, em Python ou combinando o melhor dos dois mundos. Eles podem ser módulos híbridos C++/Python, nos quais a funcionalidade central sólida é programada em C++ e as ferramentas para o usuário final são escritas em Python, tornando-as mais fáceis de estender e adaptar pelos usuários do FreeCAD. Cada módulo geralmente define e cria uma **Bancada de Trabalho** na interface do FreeCAD, quando usado no modo GUI, geralmente com o mesmo nome, mas não é obrigatório que os módulos contenham uma bancada de trabalho.

-   Os módulos do FreeCAD frequentemente **dependem de outros módulos**. A maioria dos módulos que utilizam geometria sólida dependem do módulo **Part**, que é o mais fundamental do FreeCAD e implementa a maior parte da interface com o OpenCascade. Embora outros módulos possam usar diretamente a funcionalidade do OpenCascade, geralmente eles contam com funções de nível mais alto fornecidas pelo Part.

-   Os módulos são sempre **inicializados** a partir do Python. Mesmo que sejam escritos inteiramente em C++, eles sempre incluem uma estrutura mínima do Python/CPython.

-   O FreeCAD é um ávido usuário de **outras bibliotecas de código aberto**. Além do Python e do Qt, usados pelo núcleo e por quase todos os módulos, as duas bibliotecas principais utilizadas em grande parte dos módulos são [OpenCascade Technology](https://en.wikipedia.org/wiki/Open_Cascade_Technology) (OCCT) e [Coin3D](http://www.coin3d.org/). O OpenCascade é utilizado para criar e gerenciar toda a geometria sólida do FreeCAD, enquanto o Coin3D é usado para gerenciar a visualização 3D. O OpenCascade é predominantemente utilizado no mundo do App, enquanto o Coin3D é exclusivamente usado no mundo do Gui. Uma compreensão básica do OpenCascade é fundamental para realizar qualquer trabalho relacionado à geometria com o FreeCAD. Módulos mais específicos fazem uso de bibliotecas mais específicas, e como geralmente não há restrições neste ponto além de garantir que estas bibliotecas estejam facilmente disponíveis em todas as plataformas, a lista de dependências de uma instalação completa do FreeCAD com todos os seus módulos pode ser bastante extensa.

-   Os **objetos de documento** do FreeCAD, que são todos os objetos contidos em um documento do FreeCAD, são aqueles que aparecem na Visualização de Árvore na GUI e em FreeCAD.ActiveDocument.Objects() em Python. Eles podem ou não ter dados geométricos e podem ou não mostrar algo na visualização 3D. Eles estão sempre divididos em partes App e Gui. A parte Gui não é carregada durante a execução no modo console. Objetos geométricos padrão, como os encontrados em Part ou PartDesign, têm sua geometria baseada no OpenCascade definida em sua contraparte App, enquanto a contraparte Gui (também geralmente chamada de \"Provedor de Visualização\") é responsável por criar uma representação em Coin3D dessa geometria, que será inserida no gráfico de cena principal em 3D da visualização.

-   A estrutura básica de diretórios do código-fonte é organizada da seguinte forma:
    -   **App**: contém a aplicação do FreeCAD no modo console, define estruturas básicas e classes base para objetos de documento, que são usados pelos módulos para construir os seus próprios.
    -   **Base**: contém funcionalidades essenciais comumente utilizadas em todo o FreeCAD: vetores 3D, unidades, matrizes, posicionamentos, etc.
    -   **Gui**: contém a aplicação do FreeCAD no modo GUI, define a visualização 3D, inclui muitas ferramentas e funções para serem utilizadas pelas bancadas de trabalho para interagir com a interface e com a visualização 3D, e define classes base para provedores de visualização.
    -   **Doc**: contém principalmente um arquivo de ajuda Qt completo gerado a partir deste wiki.
    -   **Mod**: contém todos os módulos, que são separados em App e Gui (exceto os módulos Python, que nem sempre seguem essa regra tão claramente).

### Relacionado

-   [Gerenciamento de código-fonte](Source_code_management.md)
-   O [Hub de usuários avançados](Hub_de_usuários_avançados.md) contém muita documentação sobre módulos, OpenCascade e Coin3D, principalmente para o programador Python. No entanto, como a funcionalidade é semelhante, estas páginas também serão de interesse para o programador C++.
-   [FCStd](File_Format_FCStd.md) - o formato de arquivo FreeCAD



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer%20Documentation.md) > The FreeCAD source code/pt-br
