# History/pt-br
\_\_FORCETOC\_\_

## História

<img alt="FreeCAD antigo, versão desconhecida." src=images/Screenshot_mesh.jpg  style="width:300px;"> <img alt="FreeCAD versão 0.7 de 2009." src=images/Part_BooleanOperations.png  style="width:300px;">

### Como tudo começou 

O FreeCAD começou em janeiro de 2001, quando [Jürgen Riegel](Usuário_Jriegel.md) começou a trabalhar no projeto Cas.CADE, este era uma estrutura de desenvolvimento de software comercial que incluía um [kernel de modelagem geométrica](Glossary/pt-br#Geometric_modeling_kernel.md) (ou kernel CAD): que foi lançado sob uma licença de código aberto em 2000 e renomeado como [OpenCASCADE](OpenCASCADE/pt-br.md). Isso tornou possível a realização de um programa CAD 3D de código aberto, pois ter que programar um kernel CAD do zero exigiria uma quantidade enorme de trabalho.

Nas palavras do próprio Jürgen:


{{Quote|text=''O projeto FreeCAD foi iniciado por mim em janeiro de 2001, como um GOM (Graphical Object Modeler), com a ideia de usar Qt, Python e Cas.CADE, um CAD-Kernel comercial da época Eu usei nos projetos da Daimler. O Cas.CADE tornou-se um código aberto pouco tempo antes, então parecia o momento certo para tentar uma mudança para a falta de CAD de código aberto que avia naquela época. Tive uma experiência de dois anos com o OpenCascade em um projeto chamado QSpect no qual, ao final, fui o principal designer de software. Aprendi muito sobre programação 3D e CAD. Também fui influenciado pelo Catia V5 e sua interface de usuário e programação muito especial… Em 17 de março de 2002, dentro do Projeto OpenCascade, registrei o software como FreeCAD. Não consegui pensar em um nome melhor, sou péssimo com nomes... Em abril de 2003, Werner Meyer, um colega de faculdade do projeto QSpect, mudou para uma empresa chamada Imetric. O contato com a Imetric resultou muito promissor, pois buscavam uma nova plataforma de software 3D para seus sensores 3D. Em 2005, a Imetric doou a maior parte de seu Módulo de malha ao FreeCAD e à comunidade Open Source e, desde então, eles usaram o FreeCAD como base para seu software de sistema de sensores. Desde então, Werner Meyer é um desenvolvedor muito ativo do FreeCAD. Em 2005, após um ano de luta, decidi retirar o framework de documentos OpenCascade e substituí-lo por uma implementação própria. Então, no final, usamos apenas o kernel CAD do OpenCascade e não o restante de seu Framework. 2007 foi outro marco interessante. Mudamos para QT4 e, portanto, para LGPL. Nessa época a gente fazia muito trabalho, principalmente Werner''.
|sign=[Jürgen Riegel](User_Jriegel.md)|source=''[http://forum.freecadweb.org/viewtopic.php?f=8&t=295 Quem está por trás do FreeCad?]''}}

O projeto foi anunciado ao público em geral no [Forum OpenCascade](https://dev.opencascade.org/forums) em 2003:


{{Quote|text=''Olá a todos, meu nome é Juergen Riegel e hoje quero anunciar um projeto OpenCasCade, o FreeCAD. Ele é um CAx RAD de código aberto baseado no OpenCasCade, QT e Python. Ele apresenta alguns conceitos importantes, como gravação de macros, workbenches, capacidade de ser executado como servidor e como extensão de aplicativos carregáveis dinamicamente, e foi projetado para ser independente de plataforma... Embora esteja em um estágio inicial e não possa ser usado por usuários nem desenvolvedores - a primeira versão para usuários está planejada para o final de 2003 -, eu gostaria de receber algum feedback sobre a direção e o design do FreeCAD. A GUI está quase concluída e agora nós, meu co-desenvolvedor Werner Mayer e eu, começamos a adicionar as primeiras funções de CAD. O FreeCAD pode ser visto como um sistema CAD mecânico de uso geral, mas seu primeiro público, creio eu, serão os desenvolvedores de CAx que precisam de base para seu próprio desenvolvimento''.
|sign=[Jürgen Riegel](User_Jriegel.md)|source=''[https://dev.opencascade.org/content/announcing-freecad-project Announcing FreeCAD Project on Sun, 08/17/2003 - 19:23]''}}

### Werner Mayer 

Werner Mayer juntou-se ao projeto assim que ele foi anunciado como um projeto de código aberto (antes do anúncio, o projeto era um projeto particular de Jürgen). Veja esta postagem de Werner no fórum em alemão: <https://forum.freecadweb.org/viewtopic.php?f=13&t=40235&start=10#p342330>

Com o tempo, o projeto ganhou força e viu a adição de novos colaboradores importantes na comunidade.

-   **iniciando no Linux**


{{Quote|text=''Um fato engraçado é que ele queria ter um software CAD de código aberto principalmente para Linux porque naquela época não existia nada para esta plataforma. No entanto, desde o início, desenvolvemos exclusivamente no Windows nos primeiros um anos e meio. Então um cara tcheco fez uma contribuição fazendo o código da compilação principal no Linux: https://github.com/berndhahnebach/All_FreeCAD/commit/9fd2e27c95ba3dc84778d92e2564cd094793ce2f#diff-480477e89f9b6ddafb30c4383dcdd705''}}


{{Quote|text=''Meio ano depois, continuei a compilação do Linux: https://github.com/berndhahnebach/All_FreeCAD/commit/35b962d7d751dd80f7c7781df60f93bc9a3da992''}}

**P:** Você poderia compartilhar como foi esse primeiro ano e meio? Vocês se encontraram pessoalmente ou online?


{{Quote|text=''Bem, naquela época éramos colegas (até 2005), então podíamos discutir as coisas pessoalmente. Depois disso, ainda tínhamos algumas reuniões pessoais, mas discutíamos a maioria das coisas por e-mail ou telefone.}}


{{Quote|text=''Como terceiro desenvolvedor principal, Yorik entrou por volta do final de 2007, mas levou mais 3 ou 4 anos até que a comunidade e o número de colaboradores começassem a crescer significativamente''}}

.

**P:** Vocês dividiram as tarefas ou trabalharam em implementações concorrentes?


{{Quote|text=''Sim,Jürgen estava projetando e implementando a maior parte da lógica do aplicativo e do documento, e eu estava fazendo o básico da GUI.''}}


{{Quote|text=''No entanto, este não foi um processo gradual, mas experimentamos muitas coisas no início. Por exemplo, na versão inicial, usamos a estrutura de documentos OCC OCAF e seu visualizador, mas depois de um ou dois anos chegamos a um beco sem saída porque a documentação sobre OCC era muito pobre e não conseguimos fazê-la funcionar para estender o OCAF com o nosso próprio tipos de recursos. Portanto, decidimos usar apenas as capacidades de modelagem do OCC, mas desenvolver nossa própria estrutura de aplicativo/documento.''}}

**P:** Naquela época, você achava que o FreeCAD estaria onde está hoje?


{{Quote|text=''Não sabíamos, mas esperávamos. É claro que não poderíamos prever exatamente como o FreeCAD se parecerá hoje.<br>As decisões de design mais importantes foram disponibilizá-lo em todas as principais plataformas e tornar todo o SW o mais acessível possível, ou seja, impor todas as funções importantes ao Python para que que os usuários (poderosos) possam estender o FreeCAD com funções próprias. Dessa forma, esperávamos obter um público amplo.''}}

(Veja esta postagem do Werner no fórum [Re: FreeCAD History](https://forum.freecadweb.org/viewtopic.php?f=8&t=47703#p411612))

### Yorik se junta ao projeto 

[Yorik van Havre](User_Yorik.md) juntou-se ao projeto em 2008 e começou a trabalhar no [módulo Draft](Draft_Workbench/pt-br.md). Antes disso, não havia como criar geometria 2D através da [GUI](Glossary/pt-br#GUI.md). Este módulo foi totalmente programado em Python e não em C++ (a linguagem de programação central usada no FreeCAD). A nova bancada de trabalfo Draft provou que a integração do Python foi um sucesso e pode ser usado para estender ou customizar os recursos do FreeCAD. Além de seu trabalho no módulo Draft, Yorik trabalhou na expansão da documentação do FreeCAD e tornou-se o \"diretor de arte\" de fato do FreeCAD, criando muitos ícones para a GUI do FreeCAD e [definindo seu estilo](Artwork/pt-br.md).

A versão 0.7 do FreeCAD lançada em abril de 2009 foi a primeira a incluir o módulo Draft. O módulo Part forneceu um fluxo de trabalho [CSG](Glossary/pt-br#Constructive_Solid_Geometry.md) simples com a criação de formas primitivas e operações booleanas acessíveis através do menu Part. A extrusão de perfis 2D e filetes também foi possível.

A versão 0.8 lançada em julho de 2009 teve mais algum trabalho no módulo Draft, incluindo uma nova ferramenta Dimension. O módulo Part se beneficiou de uma nova barra de ferramentas junto com novas ferramentas, Revolver e Seção.

No final de 2009, o FreeCAD foi aceito como um pacote Debian nos repositórios Debian. O FreeCAD foi adicionado aos repositórios do Ubuntu 10.04 em 2010.

### O projeto continua 

A versão 0.10 foi lançada em julho de 2010 e introduziu a [bancada de trabalho Sketcher](Sketcher_Workbench.md), baseado no Sketchsolve, um solucionador baseado em restrições para criar geometria 2D. A primeira versão limitava-se à criação de retângulos e linhas.

No início de 2011, aproveitando a oportunidade oferecida pela plataforma on-line [Launchpad](https://launchpad.net), foi criada a equipe [FreeCAD Maintainers](https://launchpad.net/~freecad-maintainers) para fornecer novas versões estáveis e pacotes de compilação diária do FreeCAD aos usuários do sistema operacional Ubuntu.

A versão 0.11 foi lançada em maio de 2011 e introduziu a nova bancada de trabalho PartDesign, que incluía ferramentas como Protrusão, Cavidade, Filete e Chanfro. A bancada de trabalho Draft recebeu aprimoramentos e novas ferramentas, como o BSpline. A bancada de trabalho Robot apresentou mais ferramentas de GUI.

A versão 0.12 foi lançada em janeiro de 2012 e apresentava um bancada de trabalho Sketcher mais completo. Ela incluía um solucionador totalmente reescrito, o FreeGCS. Foi o resultado de meses de trabalho dos principais desenvolvedores do FreeCAD, juntamente com os novatos logari81 (que programou o solver) e mrlukeparry. Mais ferramentas foram adicionadas ao workbench do PartDesign.

### Ampliação da equipe principal de desenvolvedores 

Em abril de 2019, a equipe de desenvolvedores principais foi expandida: Jürgen, Werner e Yorik se juntaram a Abdullah, Bernd, sliptonic e WandererFan

## Postagens interessantes no fórum 

-   sobre PartDesignNext e outras decisões de design: <https://forum.freecadweb.org/viewtopic.php?f=8&t=34923&start=130#p297074>
-   sobre a história do Fórum: <https://forum.freecadweb.org/viewtopic.php?f=8&t=7448&start=200#p287106>
-   sobre o histórico do projeto: <https://forum.freecadweb.org/viewtopic.php?f=8&t=47703>
-   sobre o histórico do código: <https://forum.freecadweb.org/viewtopic.php?f=10&t=46733&start=10#p405068> BTW: o check-in inicial do código foi em 18 de março de 2002 (pode ser o aniversário?)
-   sobre o projeto para ser OpenSource: <https://forum.freecadweb.org/viewtopic.php?f=13&t=40235&start=10#p342330>
-   sobre o histórico de confirmação de lançamento: <https://forum.freecadweb.org/viewtopic.php?f=8&t=23695#p184940>
-   sobre Quem está por trás do FreeCAD: <http://forum.freecadweb.org/viewtopic.php?f=8&t=295>
-   sobre a história do FEM: <https://forum.freecadweb.org/viewtopic.php?f=18&t=48646#p416389>
-   sobre a história do mesher FEM: <https://forum.freecadweb.org/viewtopic.php?f=18&t=48733#p417627>



## Histórico de lançamento 

#### Visão geral 

  Versão   Nome da versão   Data de lançamento   Notas de lançamento                                         Release commit                                                                            Release branch
       
  0.21     \-               em desenvolvimento   [Notas da versão 0.21](Release_notes_0.21.md)       [head master](https://github.com/FreeCAD/FreeCAD/commits/master)                          
  0.20     \-               2022-06-14           [Notas da versão 0.20](Release_notes_0.20.md)       [release commit 0.20](https://github.com/FreeCAD/FreeCAD/commits/releases/FreeCAD-0-20)   [branch bugfixes 0.20](https://github.com/FreeCAD/FreeCAD/tree/releases/FreeCAD-0-20)
  0.19     \-               2021-03-20           [Notas de lançamento 0.19](Release_notes_0.19.md)   [release commit 0.19](https://github.com/FreeCAD/FreeCAD/commits/releases/FreeCAD-0-19)   [branch bugfixes 0.19](https://github.com/FreeCAD/FreeCAD/tree/releases/FreeCAD-0-19)
  0.18     \-               2019-03-12           [Notas de lançamento 0.18](Release_notes_0.18.md)   [release commit 0.18](https://github.com/FreeCAD/FreeCAD/commits/releases/FreeCAD-0-18)   [branch bugfixes 0.18](https://github.com/FreeCAD/FreeCAD/tree/releases/FreeCAD-0-18)
  0.17     Roland           2018-04-06           [Notas de lançamento 0.17](Release_notes_0.17.md)   [release commit 0.17](https://github.com/FreeCAD/FreeCAD/commits/releases/FreeCAD-0-17)   [branch bugfixes 0.17](https://github.com/FreeCAD/FreeCAD/tree/releases/FreeCAD-0-17)
  0.16     \-               2016-04-18           [Notas de lançamento 0.16](Release_notes_0.16.md)   [release commit 0.16](https://github.com/FreeCAD/FreeCAD/commits/releases/FreeCAD-0-16)   [branch bugfixes 0.16](https://github.com/FreeCAD/FreeCAD/tree/releases/FreeCAD-0-16)
  0.15     \-               2015-04-08           [Notas de lançamento 0.15](Release_notes_0.15.md)   [release commit 0.15](https://github.com/FreeCAD/FreeCAD/commits/releases/FreeCAD-0-15)   [branch bugfixes 0.15](https://github.com/FreeCAD/FreeCAD/tree/releases/FreeCAD-0-15)
  0.14     \-               2014-07-01           [Notas de lançamento 0.14](Release_notes_0.14.md)   [release commit 0.14](https://github.com/FreeCAD/FreeCAD/commits/releases/FreeCAD-0-14)   [branch bugfixes 0.14](https://github.com/FreeCAD/FreeCAD/tree/releases/FreeCAD-0-14)
  0.13     \-               2013-01-29           [Notas de lançamento 0.13](Release_notes_0.13.md)   [release commit 0.13](https://github.com/FreeCAD/FreeCAD/commits/releases/FreeCAD-0-13)   [branch bugfixes 0.13](https://github.com/FreeCAD/FreeCAD/tree/releases/FreeCAD-0-13)
  0.12     \-               2011-12-20           [Notas de lançamento 0.12](Release_notes_0.12.md)                                                                                             
  0.11     \-               2011-05-03           [Notas de lançamento 0.11](Release_notes_0.11.md)                                                                                             
  0.10     \-               2010-07-24                                                                                                                                                                 
  0.9      \-               2010-01-16                                                                                                                                                                 
  0.8      \-               2009-07-10                                                                                                                                                                 
  0.7      \-               2009-04-24                                                                                                                                                                 
  0.6      \-               2007-02-27                                                                                                                                                                 
  0.5      \-               2006-10-05                                                                                                                                                                 
  0.4      \-               2006-01-15                                                                                                                                                                 
  0.3      \-               2005-10-31                                                                                                                                                                 
  0.2      \-               2005-08-09                                                                                                                                                                 
  0.1      \-               2003-01-27                                                                                                                                                                 
  0.0.1    \-               2002-10-29           Inicio de vercionamento                                                                                                                               



#### Legenda

  Cor   Tipo de versão
   
        Lançamento futuro
        Versão prévia mais recente
        **Versão mais recente**
        Versão antiga, mas ainda compatível
        Versão mais antiga
        

== Links externos

-   [seção Arquivos do SourceForge](http://sourceforge.net/projects/free-cad/files/)

-   [seção Arquivos antigos do SourceForge](http://sourceforge.net/projects/free-cad/files/OldFiles/).

-   [Anunciando o Projeto FreeCAD](http://www.opencascade.org/org/forum/thread_6572/?forum=11) no fórum OpenCascade



---
⏵ [documentation index](../README.md) > [News](Category_News.md) > History/pt-br
