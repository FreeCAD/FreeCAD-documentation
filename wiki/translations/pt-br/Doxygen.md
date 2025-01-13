# Doxygen/pt-br
## Sobre




Doxygen é uma ferramenta popular para gerar documentação a partir de fontes C++ anotadas; ele também suporta outras linguagens de programação populares, como C#, PHP, Java e Python. Visite o [site da Doxygen](http://www.doxygen.nl/) para saber mais sobre o sistema e consulte o [Manual da Doxygen](http://www.doxygen.nl/manual/index.html)(inglês) para obter as informações completas.



## Doxygen e FreeCAD 

Este documento dá uma breve introdução ao Doxygen, em particular como ele é usado no FreeCAD para documentar suas fontes. Visite a página de documentação de origem para obter instruções sobre como construir a [documentação do FreeCAD](source_documentation/pt-br.md), que também está hospedada on-line no site da [do FreeCAD](https://www.freecadweb.org/api/).

<img alt="" src=images/FreeCAD_doxygen_workflow.svg  style="width:800px;">



*Fluxo de trabalho geral para produzir  documentações de código-fonte com o Doxygen.*



## Doxygen com código C++ 

A seção [Introdução (Etapa 3)](http://www.doxygen.nl/manual/starting.html) do manual do Doxygen menciona as maneiras básicas de documentar as fontes.

Para membros, classes e namespaces existem basicamente duas opções:

1.  Coloque um \"bloco de documentação\" especial (um parágrafo comentado) antes da declaração ou definição da função, membro, classe ou namespace. Para membros de arquivo, classe e namespace (variáveis) também é permitido colocar a documentação diretamente após o membro. Consulte a seção [Blocos de comentários especiais](http://www.doxygen.nl/manual/docblocks.html#specialblock) no manual para saber mais sobre esses blocos.
2.  Coloque um bloco de documentação especial em outro lugar (outro arquivo ou outro local no mesmo arquivo) e coloque um \"comando estrutural\" no bloco de documentação. Um comando estrutural vincula um bloco de documentação a uma determinada entidade que pode ser documentada (uma função, membro, variável, classe, namespace ou arquivo). Consulte a seção [Documentação em outros locais](http://www.doxygen.nl/manual/docblocks.html#structuralcommands) do manual para saber mais sobre comandos estruturais.

Nota:

-   A vantagem da primeira opção é que você não precisa repetir o nome da entidade (função, membro, variável, classe ou namespace), pois o Doxygen analisará o código e extrairá as informações relevantes.
-   Os arquivos só podem ser documentados usando a segunda opção, já que não há como colocar um bloco de documentação antes de um arquivo. É claro que os membros do arquivo (functions, variables, typedefs, defines) não precisam de um comando estrutural explícito; apenas colocar um bloco de documentação antes ou depois deles funcionará bem.



### Primeiro estilo: bloco de documentação antes do código 

Normalmente, você deseja documentar o código no arquivo de cabeçalho, logo antes da declaração de classe ou do protótipo de função. Isso mantém a declaração e a documentação próximas uma da outra, por isso é fácil atualizar a última se a primeira for alterada.

O bloco de documentação especial começa como um comentário no estilo C `/*`, mas tem um asterisco adicional `/**`; O bloco termina com uma correspondência `*/`. Uma alternativa é usar comentários no estilo C++ com uma barra adicional `//`. 
```python
/**
 * Returns the name of the workbench object.
 */
std::string name() const;

/**
 * Set the name to the workbench object.
 */
void setName(const std::string&);

/// remove the added TaskWatcher
void removeTaskWatcher(void);
```



### Segundo estilo: bloco de documentação em outro lugar 

Como alternativa, a documentação pode ser colocada em outro arquivo (ou no mesmo arquivo na parte superior ou inferior, ou onde), longe da declaração de classe ou protótipo de função. Nesse caso, você terá informações duplicadas, uma vez no arquivo de origem real e uma vez no arquivo de documentação.

Primeiro arquivo, `source.h`: 
```python
std::string name() const;
void setName(const std::string&);
```

Segundo arquivo, `source.h.dox`: 
```python
/** \file source.h
 *  \brief The documentation of source.h
 *   
 *   The details of this file go here.
 */

/** \fn std::string name() const;
 *  \brief Returns the name of the workbench object.
 */
/** \fn void setName(const std::string&);
 *  \brief Set the name to the workbench object.
 */
```

Nesse caso, o comando estrutural `\file` é usado para indicar qual arquivo de origem está sendo documentado; Um comando estrutural `\fn` indica que o código a seguir é uma função, e o comando `\brief` é usado para fornecer uma pequena descrição dessa função.

Essa maneira de documentar um arquivo de origem é útil se você quiser apenas adicionar documentação ao seu projeto sem adicionar código real. Quando você coloca um bloco de comentários em um arquivo com uma das seguintes extensões `.dox`, `.txt` ou `.doc` então o Doxygen analisará os comentários e criará a documentação apropriada, mas ocultará esse arquivo auxiliar da lista de arquivos.

O projeto FreeCAD adiciona vários arquivos terminandos em `.dox`, a fim de fornecer uma descrição, ou exemplos, do código. É importante que esses arquivos sejam categorizados corretamente em um grupo ou namespace, para o qual o Doxygen fornece alguns comandos auxiliares como `\defgroup`, `\ingroup` e `\namespace`.


<div class="mw-collapsible mw-collapsed toccolours">

Exemplo `src/Base/core-base.dox`; este arquivo na árvore de código fonte do FreeCAD dá uma breve explicação do namespace `Base`.


<div class="mw-collapsible-content">


```python
/** \defgroup BASE Base
 *  \ingroup CORE
    \brief Basic structures used by other FreeCAD componentsThe Base module includes most of the basic functions of FreeCAD, such as:
    - Console services: printing different kinds of messages to the FreeCAD report view or the terminal
    - Python interpreter: handles the execution of Python code in FreeCAD
    - Parameter handling: Management, saving and restoring of user preferences settings
    - Units: Management and conversion of different units

*/

/*! \namespace Base
    \ingroup BASE
    \brief Basic structures used by other FreeCAD components

    The Base module includes most of the basic functions of FreeCAD, such as:
    - Console services: printing different kinds of messages to the FreeCAD report view or the terminal
    - Python interpreter: handles the execution of Python code in FreeCAD
    - Parameter handling: Management, saving and restoring of user preferences settings
    - Units: Management and conversion of different units
*/
```


</div>


</div>

Outro exemplo é o arquivo `src/Gui/Command.cpp`. Antes dos detalhes de implementação `Gui::Command` dos métodos, há um bloco de documentação que explica alguns detalhes da estrutura de comando do FreeCAD. Ele tem vários comandos `\section` para estruturar a documentação. Ele ainda inclui código de exemplo incluído em um par de palavras-chave `\code` e `\endcode`; quando o arquivo é processado por Doxygen, este exemplo de código será especialmente formatado para se destacar. A palavra-chave `\ref` é usada em vários lugares para criar links para seções, subseções, páginas ou âncoras nomeadas em outros lugares da documentação. Da mesma forma, os comandos `\see` ou `\sa` imprimem \"Consulte também\" e fornecem um link para outras classes, funções, métodos, variáveis, arquivos ou URLs.


<div class="mw-collapsible mw-collapsed toccolours">

Exemplo `src/Gui/Command.cpp`


<div class="mw-collapsible-content">


```python
/** \defgroup commands Command Framework
    \ingroup GUI
    \brief Structure for registering commands to the FreeCAD system
 * \section Overview
 * In GUI applications many commands can be invoked via a menu item, a toolbar button or an accelerator key. The answer of Qt to master this
 * challenge is the class \a QAction. A QAction object can be added to a popup menu or a toolbar and keep the state of the menu item and
 * the toolbar button synchronized.
 *
 * For example, if the user clicks the menu item of a toggle action then the toolbar button gets also pressed
 * and vice versa. For more details refer to your Qt documentation.
 *
 * \section Drawbacks
 * Since QAction inherits QObject and emits the \a triggered() signal or \a toggled() signal for toggle actions it is very convenient to connect
 * these signals e.g. with slots of your MainWindow class. But this means that for every action an appropriate slot of MainWindow is necessary
 * and leads to an inflated MainWindow class. Furthermore, it's simply impossible to provide plugins that may also need special slots -- without
 * changing the MainWindow class.
 *
 * \section wayout Way out
 * To solve these problems we have introduced the command framework to decouple QAction and MainWindow. The base classes of the framework are
 * \a Gui::CommandBase and \a Gui::Action that represent the link between Qt's QAction world and the FreeCAD's command world. 
 *
 * The Action class holds a pointer to QAction and CommandBase and acts as a mediator and -- to save memory -- that gets created 
 * (@ref Gui::CommandBase::createAction()) not before it is added (@ref Gui::Command::addTo()) to a menu or toolbar.
 *
 * Now, the implementation of the slots of MainWindow can be done in the method \a activated() of subclasses of Command instead.
 *
 * For example, the implementation of the "Open file" command can be done as follows.
 * \code
 * class OpenCommand : public Command
 * {
 * public:
 *   OpenCommand() : Command("Std_Open")
 *   {
 *     // set up menu text, status tip, ...
 *     sMenuText     = "&Open";
 *     sToolTipText  = "Open a file";
 *     sWhatsThis    = "Open a file";
 *     sStatusTip    = "Open a file";
 *     sPixmap       = "Open"; // name of a registered pixmap
 *     sAccel        = "Shift+P"; // or "P" or "P, L" or "Ctrl+X, Ctrl+C" for a sequence
 *   }
 * protected:
 *   void activated(int)
 *   {
 *     QString filter ... // make a filter of all supported file formats
 *     QStringList FileList = QFileDialog::getOpenFileNames( filter,QString::null, getMainWindow() );
 *     for ( QStringList::Iterator it = FileList.begin(); it != FileList.end(); ++it ) {
 *       getGuiApplication()->open((*it).latin1());
 *     }
 *   }
 * };
 * \endcode
 * An instance of \a OpenCommand must be created and added to the \ref Gui::CommandManager to make the class known to FreeCAD.
 * To see how menus and toolbars can be built go to the @ref workbench.
 *
 * @see Gui::Command, Gui::CommandManager
 */
```


</div>


</div>



### Exemplo do projeto VTK 

Este é um exemplo do [VTK](https://vtk.org/), uma biblioteca de visualização 3D usada para apresentar dados científicos, como resultados de elementos finitos e informações de nuvem de pontos.

Uma classe para armazenar uma coleção de coordenadas é definida em um arquivo de cabeçalho C++. A parte superior do arquivo é comentada, e algumas palavras-chave são usadas, como `@class`, `@brief` e `@sa` para indicar partes importantes. Dentro da classe, antes dos protótipos do método de classe, um bloco de texto comentado explica o que a função faz e seus argumentos.

-   Código fonte de [vtkArrayCoordinates.h](https://github.com/Kitware/VTK/blob/master/Common/Core/vtkArrayCoordinates.h).
-   Doxygen produziu documentação para a [classe vtkArrayCoordinates](http://www.vtk.org/doc/nightly/html/classvtkArrayCoordinates.html).



## Compilando a documentação 

<img alt="" src=images/FreeCAD_doxygen_workflow.svg  style="width:800px;">



*Fluxo de trabalho geral para produzir documentação de código-fonte com o Doxygen.*

Para gerar a documentação do código-fonte, há duas etapas básicas:

1.  Crie um arquivo de configuração para controlar como o Doxygen processará os arquivos de origem.
2.  Execute `doxygen` nessa configuração.


<div class="mw-collapsible mw-collapsed toccolours">

O processo é descrito a seguir.


<div class="mw-collapsible-content">

-   Certifique-se de ter os programas


`doxygen`

e `doxywizard` em seu sistema. Também é recomendado ter o

`dot` programa do [Graphviz](https://www.graphviz.org/), a fim de gerar diagramas com as relações entre classes e namespaces. Em sistemas Linux, esses programas podem ser instalados a partir do seu gerenciador de pacotes.


```python
sudo apt install doxygen doxygen-gui graphviz
```

-   Verifique se você está na mesma pasta que os arquivos de origem ou no diretório de nível superior da árvore de código-fonte, se você tiver muitos arquivos de código-fonte em subdiretórios diferentes.


```python
cd toplevel-source
```

-   Execute `doxygen -g DoxyDoc.cfg` para criar um arquivo de configuração chamado `DoxyDoc.cfg`. Se você omitir esse nome, o arquivo `Doxyfile` ficara sem uma extensão.
-   Este é um arquivo de texto grande e simples que inclui muitas variáveis com seus valores. No manual do Doxygen essas variáveis são chamadas de \"tags\". O arquivo de configuração e todas as tags são descritos extensivamente na seção [Configuração](http://www.doxygen.nl/manual/config.html) do manual. Você pode abrir o arquivo com qualquer editor de texto e editar o valor de cada tag conforme necessário. No mesmo arquivo, você pode ler comentários explicando cada uma das marcas e seus valores padrão.


```python
DOXYFILE_ENCODING      = UTF-8
PROJECT_NAME           = "My Project"
PROJECT_NUMBER         =
PROJECT_BRIEF          =
PROJECT_LOGO           =
OUTPUT_DIRECTORY       =
CREATE_SUBDIRS         = NO
ALLOW_UNICODE_NAMES    = NO
BRIEF_MEMBER_DESC      = YES
REPEAT_BRIEF           = YES
...
```

-   Em vez de usar um editor de texto, você pode iniciar `doxywizard` para editar muitas tags ao mesmo tempo. Com esta interface você pode definir muitas propriedades, como informações do projeto, tipo de saída (HTML e LaTeX), uso do Graphviz para criar diagramas, mensagens de aviso para exibir, padrões de arquivo (extensões) para documentar ou excluir, filtros de entrada, cabeçalhos e rodapés opcionais para as páginas geradas em HTML, opções para saídas LaTeX, RTF, XML ou Docbook e muitas outras opções.


```python
doxywizard DoxyDoc.cfg
```

-   Outra opção é criar o arquivo de configuração do zero e adicionar apenas as tags desejadas com um editor de texto.
-   Depois que a configuração for salva, você poderá executar o Doxygen neste arquivo de configuração.


```python
doxygen DoxyDoc.cfg
```

-   A documentação gerada será criada dentro de uma pasta chamada `toplevel-source/html`. Ele consistirá em muitas páginas HTML, imagens PNG para gráficos, folhas de estilo em cascata (`.css`), arquivos Javascript (`.js`) e potencialmente muitos subdiretórios com mais arquivos, dependendo do tamanho do seu código. O ponto de entrada na documentação é `index.html`, que você pode abrir com um navegador da Web.


```python
xdg-open toplevel-source/html/index.html
```


</div>


</div>

Se você estiver escrevendo novas classes, funções ou um novo workbench inteiro, é recomendável executar `doxygen` periodicamente para ver se os blocos de documentação, [Markdown](#Markdown_support.md) e [comandos especiais](#Doxygen_markup.md) estão sendo lidos corretamente e se todas as funções públicas estão totalmente documentadas. Leia também as [dicas de documentação](https://github.com/FreeCAD/FreeCAD/blob/master/src/Doc/doctips.dox) localizadas no código-fonte.

Ao gerar a documentação completa do FreeCAD, você não executa `doxygen` diretamente. Em vez disso, o projeto usa `cmake` para configurar o ambiente de compilação e, em seguida `make`, dispara a compilação dos códigos-fonte do FreeCAD e da documentação do Doxygen; isso é explicado na página de [documentação de origem](source_documentation.md).



## Marcações de Doxygen 

Todos os [comandos da documentação](http://www.doxygen.nl/manual/commands.html) do Doxygen começam com uma barra invertida `\` ou um arroba `@`, de sua preferência. Normalmente, a barra invertida `\` é usada, mas ocasionalmente `@` é usada para melhorar a legibilidade.

Os comandos podem ter um ou mais argumentos. No manual do Doxygen, os argumentos são descritos a seguir.

-   Se `<sharp>` forem usadas chaves, o argumento será uma única palavra.
-   Se `(round)` forem usadas chaves, o argumento se estenderá até o final da linha na qual o comando foi encontrado.
-   Se {curly} forem usadas chaves, o argumento se estende até o próximo parágrafo. Os parágrafos são delimitados por uma linha em branco ou por um indicador de seção.
-   Se `[square]` forem usados colchetes, o argumento será opcional.


<div class="mw-collapsible mw-collapsed toccolours">

Algumas das palavras-chave mais comuns usadas na documentação do FreeCAD são apresentadas aqui.


<div class="mw-collapsible-content">

-    (group title), consulte [\\defgroup](http://www.doxygen.nl/manual/commands.html#cmddefgroup), e [Grouping](http://www.doxygen.nl/manual/grouping.html).
-   ]), consulte [\\ingroup](http://www.doxygen.nl/manual/commands.html#cmdingroup), e [Grouping](http://www.doxygen.nl/manual/grouping.html).
-    [(title)], consulte [\\addtogroup](http://www.doxygen.nl/manual/commands.html#cmdaddtogroup), e [Grouping](http://www.doxygen.nl/manual/grouping.html).
-   \author { list of authors }, veja [\\author](http://www.doxygen.nl/manual/commands.html#cmdauthor); indica o autor deste pedaço de código.
-   \brief { brief description }, veja [\\brief](http://www.doxygen.nl/manual/commands.html#cmdbrief); descreve brevemente a função.
-   ], consulte [\\file](http://www.doxygen.nl/manual/commands.html#cmdfile); documenta um arquivo de origem ou de cabeçalho.
-    (title), consulte [\\page](http://www.doxygen.nl/manual/commands.html#cmdpage); coloca as informações em uma página separada, não diretamente relacionada a uma classe, arquivo ou membro específico.
-   , consulte [\\package](http://www.doxygen.nl/manual/commands.html#cmdpackage); indica documentação para um pacote Java (mas também usado com Python).
-   \fn (function declaration), veja [\\fn](http://www.doxygen.nl/manual/commands.html#cmdfn); documenta uma função.
-   \var (variable declaration), veja [\\var](http://www.doxygen.nl/manual/commands.html#cmdvar); documenta uma variável; é equivalente a `\fn`, `\property` e `\typedef`.
-    (section title), consulte [\\section](http://www.doxygen.nl/manual/commands.html#cmdsection); inicia uma seção.
-    (subsection title), consulte [\\subsection](http://www.doxygen.nl/manual/commands.html#cmdsubsection); inicia uma subseção.
-   , consulte [\\namespace](http://www.doxygen.nl/manual/commands.html#cmdnamespace); indica informações para um namespace.
-   \cond [(section-label)], e \endcond, veja [\\cond](http://www.doxygen.nl/manual/commands.html#cmdcond); Define um bloco para documentar condicionalmente ou omitir.
-   , veja [\\a](http://www.doxygen.nl/manual/commands.html#cmda); exibe o argumento em itálico para ênfase.
-    { parameter description }, veja [\\param](http://www.doxygen.nl/manual/commands.html#cmdparam); Indica o parâmetro de uma função.
-   \return { description of the return value }, consulte [\\return](http://www.doxygen.nl/manual/commands.html#cmdreturn); Especifica o valor de retorno.
-   \sa { references }, consulte [\\sa](http://www.doxygen.nl/manual/commands.html#cmdsa); imprime \"See also\".
-   \note { text }, veja [\\note](http://www.doxygen.nl/manual/commands.html#cmdnote); adiciona um parágrafo para ser usado como uma nota.


</div>


</div>



## Suporte a Markdown 

Desde o Doxygen 1.8, a sintaxe Markdown é reconhecida em blocos de documentação. Markdown é uma linguagem de formatação minimalista inspirada em e-mail de texto simples que, semelhante à sintaxe wiki, pretende ser simples e legível sem exigir código complicado como o encontrado em HTML, LaTeX ou comandos do próprio Doxygen. Markdown ganhou popularidade com o software livre, especialmente em plataformas online como o Github, pois permite criar documentação sem usar código complicado. Consulte a seção [Suporte a Markdown](http://www.doxygen.nl/manual/markdown.html) no manual do Doxygen para saber mais. Visite o [site da Markdown](https://daringfireball.net/projects/markdown/) para saber mais sobre a origem e a filosofia da Markdown.

O Doxygen suporta um conjunto padrão de instruções de Markdown, bem como algumas extensões, como o [Github Markdown](https://github.github.com/github-flavored-markdown/).


<div class="mw-collapsible mw-collapsed toccolours">

Alguns exemplos de formatação Markdown são apresentados a seguir.


<div class="mw-collapsible-content">

A seguir está o Markdown padrão. 
```python
Here is text for one paragraph.

We continue with more text in another paragraph.

This is a level 1 header
========================

This is a level 2 header


# This is a level 1 header

### This is level 3 header #######

> This is a block quote
> spanning multiple lines

- Item 1

  More text for this item.

- Item 2
  * nested list item.
  * another nested item.
- Item 3

1. First item.
2. Second item.

*single asterisks: emphasis*

 _single underscores_

 **double asterisks: strong emphasis**

 __double underscores__

This a normal paragraph

    This is a code block

We continue with a normal paragraph again.

Use the printf() function. Inline code.

[The link text](http://example.net/)

![Caption text](images//path/to/img.jpg)

<http://www.example.com>
```

A seguir estão as extensões Markdown.

    [TOC]

    First Header  | Second Header
     | 
    Content Cell  | Content Cell 
    Content Cell  | Content Cell 

    <nowiki>~~~~~~~~~~~~~</nowiki>{.py}
    # A class
    class Dummy:
        pass
    <nowiki>~~~~~~~~~~~~~</nowiki>

    <nowiki>~~~~~~~~~~~~~</nowiki>{.c}
    int func(int a, int b) { return a*b; }
    <nowiki>~~~~~~~~~~~~~</nowiki>
int func(int a, int b) { return a*b; }
    


</div>


</div>



## Análise de blocos de documentação 

O texto dentro de um bloco de documentação especial é analisado antes de ser gravado nos arquivos de saída HTML e LaTeX. Durante a análise, as seguintes etapas ocorrem:

-   A formatação Markdown é substituída por comandos HTML ou especiais correspondentes.
-   Os comandos especiais dentro da documentação são executados. Consulte a seção [Comandos especiais](http://www.doxygen.nl/manual/commands.html) no manual para obter uma explicação de cada comando.
-   Se uma linha começar com algum espaço em branco seguido por um ou mais asteriscos (`*`) e, opcionalmente, mais espaço em branco, todos os espaços em branco e asteriscos serão removidos.\*
-   Todas as linhas em branco resultantes são tratadas como separadores de parágrafo.
-   Os links são criados automaticamente para palavras correspondentes a classes ou funções documentadas. Se a palavra for precedida por um símbolo de porcentagem `%`, esse símbolo será removido e nenhum link será criado para a palavra.
-   Os links são criados quando determinados padrões são encontrados no texto. Consulte a seção [Geração automática de links](http://www.doxygen.nl/manual/autolink.html) no manual para obter mais informações.
-   As tags HTML que estão na documentação são interpretadas e convertidas em equivalentes LaTeX para a saída LaTeX. Consulte a seção [Comandos HTML](http://www.doxygen.nl/manual/htmlcmds.html) no manual para obter uma explicação de cada tag HTML suportada.



## Doxygen com código Python 

Doxygen funciona melhor para linguagens tipadas estaticamente como C++. No entanto, ele também pode criar [documentação para arquivos Python](http://www.doxygen.nl/manual/docblocks.html#pythonblocks).

Há duas maneiras de escrever blocos de documentação para Python:

1.  O modo pythonico, usando \"docstrings\", ou seja, um bloco de texto cercado por '''aspas triplas''' imediatamente após a definição da classe ou função.
2.  O modo Doxygen, colocando os comentários antes da definição da classe ou função; Nesse caso, caracteres de cerquilha dupla `##` são usados para iniciar o bloco de documentação e, em seguida, um único caractere de hash pode ser usado nas linhas subsequentes.

Nota:

-   A primeira opção é preferível para cumprir com [PEP8](https://www.python.org/dev/peps/pep-0008/#documentation-strings), [PEP257](https://www.python.org/dev/peps/pep-0257/) e a maioria das diretrizes de estilo para escrever Python (veja [1](https://realpython.com/python-pep8/), [2](https://realpython.com/documenting-python-code/)). Recomenda-se usar esse estilo se você pretende produzir fontes documentadas usando o [Sphinx](https://www.sphinx-doc.org/en/master/), que é uma ferramenta muito comum para documentar código Python. Se você usar esse estilo, o Doxygen poderá extrair os comentários textualmente, mas os comandos especiais do Doxygen começando com `\` ou `@` não funcionarão.
-   A segunda opção não é o estilo Python tradicional, mas permite que você use os comandos especiais do Doxygen, como `\param` e `\var` .



### Primeiro estilo: documentação pythonica 

No exemplo a seguir, um docstring está no início para explicar o conteúdo geral deste módulo (arquivo). Em seguida, docstrings aparecem dentro das definições de método de função, classe e classe. Desta forma, Doxygen irá extrair os comentários e apresentá-los como estão, sem modificação.


```python
'''@package pyexample_a
Documentation for this module.
More details.
'''


def func():
    '''Documentation for a function.
    More details.
    '''
    pass


class PyClass:
    '''Documentation for a class.
    More details.
    '''

    def __init__(self):
        '''The constructor.'''
        self._memVar = 0

    def PyMethod(self):
        '''Documentation for a method.'''
        pass
```



### Segundo estilo: bloco de documentação antes do código 

No exemplo a seguir, os blocos de documentação começam com sinal de cerquilha dupla `##`. Um aparece no início para explicar o conteúdo geral deste módulo (arquivo). Em seguida, há blocos antes das definições de função, classe e método de classe, e há um bloco após uma variável de classe. Dessa forma, o Doxygen extrairá a documentação, reconhecerá os comandos especiais `@package`, `@param` e `@var`, e formatará o texto de acordo. 
```python
## @package pyexample_b
#  Documentation for this module.
#
#  More details.


## Documentation for a function.
#
#  More details.
def func():
    pass


## Documentation for a class.
#
#  More details.
class PyClass:

    ## The constructor.
    def __init__(self):
        self._memVar = 0

    ## Documentation for a method.
    #  @param self The object pointer.
    def PyMethod(self):
        pass

    ## A class variable.
    classVar = 0
    ## @var _memVar
    #  a member variable
```



### Compilando a documentação 

A compilação da documentação procede da mesma forma que [para fontes C++](#Compiling_the_documentation.md). Se ambos os arquivos Python `pyexample_a.py` e `pyexample_b.py`, com estilo de comentário distinto estiverem no mesmo diretório, ambos serão processados. 
```python
cd toplevel-source/
doxygen -g
doxygen Doxyfile
xdg-open ./html/index.html
```

A documentação deve mostrar informações semelhantes às seguintes e criar links apropriados para os módulos e classes individuais. 
```python
Class List
Here are the classes, structs, unions and interfaces with brief descriptions:

N  pyexample_a
   C  PyClass

N  pyexample_b  Documentation for this module
   C  PyClass   Documentation for a class
```



### Convertendo o estilo Pythonic para o estilo Doxygen 

No exemplo anterior, o arquivo Python que é comentado em um [estilo Doxygenestilo](#Second_style__documentation_block_before_the_code.md) Doxygen mostra informações mais detalhadas e formatação para suas classes, funções e variáveis. A razão é que esse estilo permite que Doxygen extraia os comandos especiais que começam com `\` ou `@`, enquanto o [estilo Pythonic](#First_style__Pythonic_documentation.md) não. Portanto, seria desejável converter o estilo Pythonic para o estilo Doxygen antes de compilar a documentação. Isso é possível com um programa Python auxiliar chamado [doxypypy](https://github.com/Feneric/doxypypy). Este programa é inspirado em um programa mais antigo chamado [doxypy](https://github.com/Feneric/doxypy), que pegaria o Pythonic '''docstrings''' e os converteria para os blocos de comentários Doxygen que começam com cerquilha dupla `##`. O Doxypypy vai além disso, pois analisa os docstrings e extrai itens de interesse, como variáveis e argumentos, e até mesmo doctests (código de exemplo nos docstrings).

O Doxypypy pode ser instalado usando o `pip`, o instalador do pacote Python. 
```python
pip3 install --user doxypypy
```

Se o comando `pip` for usado sem a opção `--user`, ele exigirá privilégios de superusuário (root) para instalar o pacote, mas isso não é necessário na maioria dos casos; Use permissões de root somente se tiver certeza de que o pacote não colidirá com os pacotes fornecidos pela distribuição.

Se o pacote foi instalado como um usuário, ele pode residir em seu diretório pessoal, por exemplo, em `$HOME/.local/bin`. Se este diretório não estiver no `PATH` do seu sistema, o programa não será encontrado. Portanto, adicione o diretório `$HOME/.bashrc` à variável `PATH`, no arquivo ou no arquivo `$HOME/.profile`. 
```python
export PATH="$HOME/.local/bin:$PATH"
```

Como alternativa, você pode criar um link simbólico para o programa `doxypypy`, colocando o link em um diretório que já está incluído no `PATH`. 
```python
mkdir -p $HOME/bin
ln -s $HOME/.local/bin/doxypypy $HOME/bin/doxypypy
```

Uma vez que o programa `doxypypy` é instalado, e acessível a partir do terminal, um arquivo Python com docstrings Pythonic pode ser reformatado para o estilo Doxygen com as seguintes instruções. O programa gera a saída do código reformatado para a saída padrão, portanto, redirecione essa saída para um novo arquivo. 
```python
doxypypy -a -c pyexample_pythonic.py > pyexample_doxygen.py
```


<div class="mw-collapsible mw-collapsed toccolours">


`pyexample_pythonic.py`


<div class="mw-collapsible-content">


```python
'''@package pyexample_pythonic
Documentation for this module.
More details go here.
'''


def myfunction(arg1, arg2, kwarg='whatever.'):
    '''
    Does nothing more than demonstrate syntax.

    This is an example of how a Pythonic human-readable docstring can
    get parsed by doxypypy and marked up with Doxygen commands as a
    regular input filter to Doxygen.

    Args:
        arg1:   A positional argument.
        arg2:   Another positional argument.

    Kwargs:
        kwarg:  A keyword argument.

    Returns:
        A string holding the result.

    Raises:
        ZeroDivisionError, AssertionError, & ValueError.

    Examples:
        >>> myfunction(2, 3)
        '5 - 0, whatever.'
        >>> myfunction(5, 0, 'oops.')
        Traceback (most recent call last):
            ...
        ZeroDivisionError: integer division or modulo by zero
        >>> myfunction(4, 1, 'got it.')
        '5 - 4, got it.'
        >>> myfunction(23.5, 23, 'oh well.')
        Traceback (most recent call last):
            ...
        AssertionError
        >>> myfunction(5, 50, 'too big.')
        Traceback (most recent call last):
            ...
        ValueError
    '''
    assert isinstance(arg1, int)
    if arg2 > 23:
        raise ValueError
    return '{0} - {1}, {2}'.format(arg1 + arg2, arg1 / arg2, kwarg)
```


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">


`pyexample_doxygen.py`


<div class="mw-collapsible-content">


```python
##@package pyexample_pythonic
#Documentation for this module.
#More details go here.
#


## @brief     Does nothing more than demonstrate syntax.
#
#    This is an example of how a Pythonic human-readable docstring can
#    get parsed by doxypypy and marked up with Doxygen commands as a
#    regular input filter to Doxygen.
#
#
# @param        arg1    A positional argument.
# @param        arg2    Another positional argument.
#
#
# @param        kwarg   A keyword argument.
#
# @return
#        A string holding the result.
#
#
# @exception        ZeroDivisionError
# @exception        AssertionError
# @exception        ValueError.
#
# @b Examples
# @code
#        >>> myfunction(2, 3)
#        '5 - 0, whatever.'
#        >>> myfunction(5, 0, 'oops.')
#        Traceback (most recent call last):
#            ...
#        ZeroDivisionError: integer division or modulo by zero
#        >>> myfunction(4, 1, 'got it.')
#        '5 - 4, got it.'
#        >>> myfunction(23.5, 23, 'oh well.')
#        Traceback (most recent call last):
#            ...
#        AssertionError
#        >>> myfunction(5, 50, 'too big.')
#        Traceback (most recent call last):
#            ...
#        ValueError
# @endcode
#

def myfunction(arg1, arg2, kwarg='whatever.'):
    assert isinstance(arg1, int)
    if arg2 > 23:
        raise ValueError
    return '{0} - {1}, {2}'.format(arg1 + arg2, arg1 / arg2, kwarg)
```


</div>


</div>

O arquivo original tem um comentário na parte superior '''@package pyexample_pythonic que indica o módulo ou namespace que está sendo descrito pelo arquivo. Essa palavra-chave `@package` não é interpretada ao usar aspas triplas no bloco de comentários.

No novo arquivo, o estilo de comentário é alterado para que a linha se torne `##@package pyexample_pythonic`, que agora será interpretada por Doxygen. No entanto, para ser interpretado corretamente, o argumento precisa ser editado manualmente para corresponder ao novo nome do módulo (arquivo); depois de fazer isso a linha deve ser `##@package pyexample_doxygen`.


<div class="mw-collapsible mw-collapsed toccolours">


`pyexample_doxygen.py`

(o topo é editado manualmente, o resto permanece o mesmo)


<div class="mw-collapsible-content">


```python
##@package pyexample_doxygen
#Documentation for this module.
#More details go here.
#
```


</div>


</div>

Para compilar, crie a configuração e execute `doxygen` no diretório de nível superior que contém os arquivos. 
```python
cd toplevel-source/
doxygen -g
doxygen Doxyfile
xdg-open ./html/index.html
```

A documentação deve mostrar informações semelhantes às seguintes e criar links apropriados para os módulos individuais. 
```python
Namespace List
Here is a list of all documented namespaces with brief descriptions:

 N  pyexample_doxygen   Documentation for this module
 N  pyexample_pythonic  
```



### Convertendo o estilo de comentário em tempo real 

No exemplo anterior, a conversão dos blocos de documentação era feita manualmente com apenas um arquivo de origem. Idealmente, queremos que essa conversão ocorra automaticamente, em tempo real, com qualquer número de arquivos Python. Para fazer isso, a configuração Doxygen deve ser editada de acordo.

Para começar, não use o programa `doxypypy` diretamente; Em vez disso, crie o arquivo de configuração com `doxygen -g`, edite o `Doxyfile`, criado e modifique a marca a seguir. 
```python
FILTER_PATTERNS        = *.py=doxypypy_filter
```

O que isso faz é que os arquivos que correspondem ao padrão, todos os arquivos com uma extensão terminando em `.py`, passarão pelo programa `doxypypy_filter`. Toda vez que Doxygen encontrar esse arquivo na árvore de origem, o nome do arquivo será passado como o primeiro argumento para este programa. 
```python
doxypypy_filter example.py
```

O programa `doxypypy_filter` não existe por padrão; ele deve ser criado como um shell script para `doxypypy` ser executado com as opções apropriadas e tomar um arquivo como seu primeiro argumento. 
```python
#!/bin/sh
doxypypy -a -c "$1"
```

Depois de salvar esse shell script, verifique se ele tem permissões de execução e se está localizado em um diretório contido no `PATH`. 
```python
chmod a+x doxypypy_filter
mv doxypypy_filter $HOME/bin
```

Em sistemas Windows, um arquivo em lotes pode ser usado de maneira semelhante. 
```python
doxypypy -a -c %1
```

Com essa configuração feita, o comando `doxygen Doxyfile` pode ser executado para gerar a documentação como de costume. Cada arquivo Python usando Pythonic '''triple quotes''' será reformatado em tempo real para usar comentários de estilo `##Doxygen` e, em seguida, será processado pelo Doxygen, que agora será capaz de interpretar os [scomandos especiais](#Doxygen_markup.md) e a [sintaxe Mardown](#Markdown_support.md). O código-fonte original não será modificado, e nenhum arquivo temporário com um nome diferente precisa ser criado como na [seção anterior](#Converting_the_Pythonic_style_to_Doxygen_style.md); Portanto, se uma instrução `@package example` for encontrada, ela não precisará ser alterada manualmente.

Observe que os arquivos Python existentes que já usam o estilo `##double hash` para seus blocos de comentários `doxypypy` não serão afetados pelo filtro e serão processados pelo Doxygen normalmente.

<img alt="" src=images/FreeCAD_doxygen_doxypypy_workflow.svg  style="width:800px;">



*Fluxo de trabalho geral para produzir documentação de código-fonte com Doxygen, quando os arquivos Python são filtrados para transformar os blocos de comentários.*



### Verificação de qualidade do código Python 

Para usar a conversão automática de blocos de documentação é importante que os fontes originais do Python estejam corretamente escritos, seguindo as diretrizes pythonicas no [PEP8](https://www.python.org/dev/peps/pep-0008/#documentation-strings)e [PEP257](https://www.python.org/dev/peps/pep-0257/). O código escrito de forma desleixada fará com que `doxypypy` falhe ao processar o arquivo e, portanto, o Doxygen não conseguirá formatar a documentação corretamente.


<div class="mw-collapsible mw-collapsed toccolours">

Os estilos de comentários a seguir não permitirão a análise das cadeias de caracteres doc pelo `doxypypy`, portanto, eles devem ser evitados.


<div class="mw-collapsible-content">


```python
'''@package Bad
'''

def first_f(one, two):

    "Bad comment 1"

    result = one + two
    result_m = one * two
    return result, result_m

def second_f(one, two):
    "Bad comment 2"
    result = one + two
    result_m = one * two
    return result, result_m

def third_f(one, two):
    'Bad comment 3'
    result = one + two
    result_m = one * two
    return result, result_m

def fourth_f(one, two):
    #Bad comment 4
    result = one + two
    result_m = one * two
    return result, result_m
```


</div>


</div>

Sempre use aspas triplas para as cadeias de caracteres doc e certifique-se de que elas sigam imediatamente a declaração de classe ou função.

Também é uma boa ideia verificar a qualidade do seu código Python com uma ferramenta como o [flake8](http://flake8.pycqa.org/en/latest/)([Gitlab](https://gitlab.com/pycqa/flake8)). Flake8 combina principalmente três ferramentas, [Pyflakes](https://github.com/PyCQA/pyflakes), [Pycodestyle](https://github.com/PyCQA/pycodestyle)(anteriormente pep8) e o [verificador de complexidade McCabe](https://github.com/PyCQA/mccabe), a fim de impor o estilo Python adequado.


```python
pip install --user flake8
flake8 example.py
```

Para verificar todos os arquivos dentro de uma árvore de código fonte use `find`. 
```python
find toplevel-source/ -name '*.py' -exec flake8 {} '+'
```

Se o projeto exigir, algumas verificações de código consideradas muito rígidas podem ser ignoradas. Os códigos de erro podem ser consultados na [documentação do Pycodestyle](https://pycodestyle.readthedocs.io/en/latest/intro.html#error-codes). 
```python
find toplevel-source/ -name '*.py' -exec flake8 --ignore=E266,E402,E722,W503 --max-line-length=100 {} '+'
```

Da mesma forma, um programa que verifica principalmente se os comentários estão em conformidade com o [PEP257](https://www.python.org/dev/peps/pep-0257/) é o [Pydocstyle](https://github.com/PyCQA/pydocstyle). Os códigos de erro podem ser consultados na [documentação do Pydocstyle](http://www.pydocstyle.org/en/4.0.0/error_codes.html). 
```python
pip install --user pydocstyle
pydocstyle example.py
```

Use-o também `find` para executar verificações docstring em todos os arquivos de origem. 
```python
find toplevel-source/ -name '*.py' -exec pydocstyle {} '+'
```



## Documentação de origem com Sphinx 

[Sphinx](https://www.sphinx-doc.org/en/master/)é o sistema mais popular para documentar o código-fonte do Python. No entanto, como as principais funções e bancadas de trabalho do FreeCAD são escritas em C++, considerou-se que o Doxygen é uma melhor ferramenta de documentação para este projeto.

Embora o Sphinx possa analisar nativamente docstrings do Python, ele requer um pouco mais de trabalho para analisar fontes C++. O projeto [Breathe](https://breathe.readthedocs.io/en/latest/) ([Github](https://github.com/michaeljones/breathe)) é uma tentativa de preencher a lacuna entre Sphinx e Doxygen, a fim de integrar a documentação de código fonte Python e C++ no mesmo sistema. Primeiro, o Doxygen precisa ser configurado para gerar um arquivo XML; a saída XML é então lida pelo Breathe e convertida em entrada adequada para o Sphinx.

Consulte o [Guia de início rápido](https://breathe.readthedocs.io/en/latest/quickstart.html) na documentação do Breathe para saber mais sobre esse processo.

Consulte esta resposta em [Stackoverflow](https://stackoverflow.com/a/35377654) para obter outras alternativas para documentar código C++ e Python juntos no mesmo projeto.



## Relacionado

-   [Documentação de origem](Source_documentation.md)
-   [Site da API FreeCAD](https://www.freecadweb.org/api/)



---
⏵ [documentation index](../README.md) > [Developer_Documentation](Category_Developer_Documentation.md) > [Developer](Category_Developer.md) > [3rd Party](Category_3rd Party.md) > Doxygen/pt-br
