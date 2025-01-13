# <img alt="" src=images/Power_user_hub.png  style="width:64px;"> Power users hub/pt-br



Este é o local ideal para você, se for um usuário experiente e deseja aprender mais sobre como personalizar e expandir o FreeCAD.

O FreeCAD é extensível por meio de código [Python](Python/pt-br.md) que é executado diretamente no [console Python](Python_console/pt-br.md), ou carregado a partir de módulos na inicialização. Isso significa que você pode modificar o FreeCAD sem precisar recompilar o programa. Por exemplo, você pode:

-   **Criar e modificar geometria**: você pode criar um novo tipo de objeto, seja do zero ou adaptando um tipo existente.
-   **Criar ferramentas e comandos personalizados**: adicione seu próprio conjunto de ferramentas que executam seu código.
-   **Modificar a interface**: crie barras de ferramentas para adicionar suas ferramentas, crie janelas especiais, painéis ou interfaces para interagir com suas ferramentas.
-   **Modificar a representação do scenegraph**: O FreeCAD possui processos separados para construir a geometria e exibi-la na tela. Você tem acesso total à maneira como o conteúdo da cena é exibido, portanto, pode modificar essa representação, interagir com ela ou adicionar comportamentos personalizados. Também é possível adicionar widgets de tela personalizados, como informações, manipuladores, âncoras ou entidades temporárias.

Se você gostaria de contribuir com conteúdo para essas páginas, solicite uma conta na wiki com permissões de editor \[aqui no fórum\](https://forum.freecadweb.org/viewtopic.php?f=21&t=6830) e leia as [Páginas da Wiki](WikiPages/pt-br.md) para as diretrizes gerais que você deve seguir. Para outras formas de contribuir com o projeto, veja a página [Ajuda FreeCAD](Help_FreeCAD/pt-br.md).



## Customizando o FreeCAD 

-   [Personalização da Interface](Interface_Customization/pt-br.md): Começando pelo básico: Barras de ferramentas e atalhos
-   [Trabalhando com Macros](Macros/pt-br.md): Grave facilmente tarefas repetidas ou código Python
-   [Receitas de Macros](Macros_recipes/pt-br.md)
-   [Personalizar Barras de Ferramentas](Customize_Toolbars/pt-br.md)
-   [Instalando mais Workbenches](Installing_more_workbenches/pt-br.md)



## Programação em FreeCAD 



### Gerais

-   [Programação e Macros](Scripting_and_macros/pt-br.md) - Uma lista de páginas relevantes do wiki
-   [Introdução ao Python](Introduction_to_Python/pt-br.md) - Veja também outros tutoriais de Python no final desta página
-   [Tutorial de Programação em FreeCAD](Python_scripting_tutorial/pt-br.md) - Uma visão geral sobre a programação em Python no FreeCAD
-   [Noções Básicas de Programação no FreeCAD](FreeCAD_Scripting_Basics/pt-br.md): Bem, as noções básicas
-   [Manual do FreeCAD - Seção Programação em Python](Manual:A_gentle_introduction/pt-br.md): Introdução de vários capítulos sobre a Programação em Python no FreeCAD
-   [Comando de Interface Gráfica](Gui_Command/pt-br.md): Adicionando comandos personalizados à interface gráfica
-   Usando unidades mistas [Unidades](Units/pt-br.md) no FreeCAD
-   [Análise de Desempenho](Profiling/pt-br.md) do código Python
-   [Depuração](Debugging#Python_Debugging/pt-br.md) do código Python
-   [Ambiente de Desenvolvimento Python](Python_Development_Environment/pt-br.md) - Um ambiente de desenvolvimento simples para Python dentro do FreeCAD



### Modulos

The functionality of FreeCAD is separated in Modules which deal with special data types and applications. FreeCAD has built-in modules and Extension Modules (plug-ins). Once plugin modules are installed, they become availible to you as easily as the built-in modules. The modules described below are the default modules, includeed in every FreeCAD installation.

-   The [Builtin modules](Builtin_modules.md) are the principal FreeCAD modules. They contain tools for manipulating general FreeCAD configurations, documents and their contents.
-   [Workbench creation](Workbench_creation.md) shows you how to create your own workbench

#### Working with Meshes 

-   [Mesh Scripting](Mesh_Scripting.md): How to interact with the [Mesh Workbench](Mesh_Workbench.md)

#### Working with Parts 

-   [The Part Workbench](Part_Workbench.md): How [Open CASCADE Technology](http://en.wikipedia.org/wiki/Open_CASCADE) tools and structure is used in FreeCAD
-   [Topological data scripting](Topological_data_scripting.md): How to interact with the Part Module
-   [PythonOCC](PythonOCC.md): How to unleash the whole Open CASCADE power
-   [Mesh to Part](Mesh_to_Part.md): Converting between object types

#### Accessing the Coin scenegraph 

-   [The Coin/Inventor scenegraph](Scenegraph.md): How the FreeCAD scene representation works
-   [Pivy](Pivy.md): How to access and modify the scenegraph

### Controlling the Qt interface 

-   [PySide](PySide.md): How to access the interface, and modify its contents
-   [Using the FreeCAD GUI](Embedding_FreeCADGui.md) in another Qt application with PyQt

### Working with parametric objects 

-   [Scripted objects](Scripted_objects.md): how to make 100% Python-scripted objects.
    -   [Scripted objects with attachment](Scripted_objects_with_attachment.md): how to make scripted objects attachable to other objects.
    -   [Scripted objects saving attributes](Scripted_objects_saving_attributes.md): how to save and restore attributes of the proxy class with `dumps` and `loads`.
    -   [Scripted objects migration](Scripted_objects_migration.md): how to migrate old scripted objects to a new class.

### Examples

-   [Code snippets](Code_snippets.md) : A collection of pieces of FreeCAD Python code, to serve as ingredients in your scripts\...
-   [Line drawing function](Line_drawing_function.md): How to build a simple tool to draw lines
-   [Dialog creation](Dialog_creation.md): How to construct dialogs with Qt designer, and use them in FreeCAD
-   [Embedding FreeCAD](Embedding_FreeCAD.md): How to import FreeCAD as a Python module in other applications
-   The [Draft Workbench](Draft_Workbench.md) adds basic 2d drawing functions to freecad. It is written entirely in Python, so it can be a good example if you want to write your own modules.
-   [FreeCAD vector math library](FreeCAD_vector_math_library.md) : A couple of handy functions to manipulate FreeCAD vectors. This library is also included in the Draft module.

## API Functions 

The complete API documentation of FreeCAD is located at <http://www.freecadweb.org/api/> . It contains both C++ and Python APIs, and is not totally well formatted yet, which can be confusing when looking for python-only code. An easier to browse version can be found [here](:Category_API.md). Note that it can be incomplete, since it is updated manually. For more accurate information, browse the modules directly from FreeCAD\'s Python console.

Related: [Exposing C++ to Python](Exposing_C%2B%2B_to_Python.md)

## Advanced modification 

-   [Start up and Configuration](Start_up_and_Configuration.md): Startup and command line options
-   [Installing on Windows](Installing_on_Windows.md): Using the windows installer
-   [Compiling FreeCAD on Windows](Compile_on_Windows.md) and [Compiling FreeCAD on Linux](Compile_on_Linux.md)
-   [Branding](Branding.md): Simple modifications you can do to the source code to change some aspects of FreeCAD
-   [Extra python modules](Extra_python_modules.md) : Extend the FreeCAD python interpreter with these powerful modules!

## Python tutorials 

These are good generic tutorials, not specific to FreeCAD, that might interest you if you are totally new to python.

**Python**

-   [Official python tutorial](https://docs.python.org/3/tutorial/index.html) - A very complete tutorial for discovering python
-   [Non-programmer tutorial for python](https://en.wikibooks.org/wiki/Non-Programmer%27s_Tutorial_for_Python_3) - an excellent wikibook
-   [Python for newbies](http://npt.cc.rsu.ru/user/wanderer/ODP/Python_for_Newbies.htm) - one big tutorial covering all the basics

**PySide** - How to create and manage FreeCAD\'s Qt UI interface from python

-   [PySide tutorial](http://zetcode.com/gui/pysidetutorial/) : A platform-agnostic tutorial showing the usage of PySide with examples
-   [PySide/PyQt tutorial](http://www.pythoncentral.io/series/python-pyside-pyqt-tutorial/) : A easy to read tutorial that covers PySide and PyQt with examples
-   [PySide documentation](http://qt-project.org/wiki/PySideDocumentation) : from the Qt Project (the people who wrote it all)
-   [Using QtCreator in PySide](http://qt-project.org/wiki/QtCreator_and_PySide) : also from the Qt Project
-   [PySide reference](http://srinikom.github.io/pyside-docs/index.html) : endless detail on the minutiae of PySide and Qt, a reliable reference source
-   [PySide code snippets](http://nullege.com/codes/search?cq=PySide) : a searchable database of PySide code snippets

The following two references are PyQt specific (not PySide) but may offer some information of use:

-   [Basic PyQt tutorial](http://www.cs.usfca.edu/~afedosov/qttut/) : A simple and short linux-based tutorial that will explain how to work with PyQt and Qt Designer
-   [Programming Qt applications in python](http://vizzzion.org/?id=pyqt) : A more in-depth tutorial covering all the process of working with qt and python

**Pivy** - How to interact with FreeCAD\'s 3D scenes

-   [Pivy - Embedding a Dynamic Scripting Language into a Scene Graph Library](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.108.947&rep=rep1&type=pdf) : Thesis that explains Pivy in detail
-   [High Level 3D Graphics Programming in Python](http://ftp.ntua.gr/mirror/python/pycon/dc2004/papers/47/) : Pivy example from Pycon 2004
-   [Introducing Pivy into studierstube](https://www.semanticscholar.org/paper/Integrating-Pivy-into-Studierstube-4.2-Gruber/08c9a89c8326c87f81c2d83428029fbfb6c2ae64) [(Mirror)](https://www.researchgate.net/publication/228737136_Integrating_Pivy_into_Studierstube_42) : A paper that is not really a tutorial, but that illustrates well how Pivy works (requires an academic account)

## Community projects 

On the [Community portal](FreeCAD_Community_Portal.md), you can find other FreeCAD-based projects run by the FreeCAD users community. If you are starting a new FreeCAD project, be sure to list it there! We also have a page with things you can do if you would like to [Help FreeCAD](Help_FreeCAD.md).



---
⏵ [documentation index](../README.md) > [Hubs](Category_Hubs.md) > Power users hub/pt-br
