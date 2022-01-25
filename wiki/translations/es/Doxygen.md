# Doxygen/es
## About


{{TOCright}}

Doxygen is a popular tool for generating documentation from annotated C++ sources; it also supports other popular programming languages such as C\#, PHP, Java, and Python. Visit the [Doxygen website](http://www.doxygen.nl/) to learn more about the system, and consult the [Doxygen Manual](http://www.doxygen.nl/manual/index.html) for the full information.

## Doxygen y FreeCAD 

This document gives a brief introduction to Doxygen, in particular how it is used in FreeCAD to document its sources. Visit the [source documentation](source_documentation.md) page for instructions on building the FreeCAD documentation, which is also hosted online on the [FreeCAD API website](https://www.freecadweb.org/api/).

<img alt="" src=images/FreeCAD_doxygen_workflow.svg  style="width:800px;">



*General workflow to produce source code documentation with Doxygen.*

## Doxygen con código C++ 

The [Getting started (Step 3)](http://www.doxygen.nl/manual/starting.html) section of the Doxygen manual mentions the basic ways of documenting the sources.

For members, classes and namespaces there are basically two options:

1.  Place a special \"documentation block\" (a commented paragraph) before the declaration or definition of the function, member, class or namespace. For file, class and namespace members (variables) it is also allowed to place the documentation directly after the member. See section [Special comment blocks](http://www.doxygen.nl/manual/docblocks.html#specialblock) in the manual to learn more about these blocks.
2.  Place a special documentation block somewhere else (another file or another location in the same file) and put a \"structural command\" in the documentation block. A structural command links a documentation block to a certain entity that can be documented (a function, member, variable, class, namespace or file). See section [Documentation at other places](http://www.doxygen.nl/manual/docblocks.html#structuralcommands) in the manual to learn more about structural commands.

Note:

-   The advantage of the first option is that you do not have to repeat the name of the entity (function, member, variable, class, or namespace), as Doxygen will analyze the code and extract the relevant information.
-   Files can only be documented using the second option, since there is no way to put a documentation block before a file. Of course, file members (functions, variables, typedefs, defines) do not need an explicit structural command; just putting a documentation block before or after them will work fine.

### First style: documentation block before the code 

Usually you\'d want to document the code in the header file, just before the class declaration or function prototype. This keeps the declaration and documentation close to each other, so it\'s easy to update the latter one if the first one changes.

The special documentation block starts like a C-style comment `/*` but has an additional asterisk, so `/**`; the block ends with a matching `*/`. An alternative is using C++-style comments `//` with an additional slash, so `///`. 
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

### Second style: documentation block elsewhere 

Alternatively, the documentation can be placed in another file (or in the same file at the top or bottom, or wherever), away from the class declaration or function prototype. In this case, you will have duplicated information, once in the actual source file, and once in the documentation file.

First file, `source.h`: 
```python
std::string name() const;
void setName(const std::string&);
```

Second file, `source.h.dox`: 
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

In this case the structural command `\file` is used to indicate which source file is being documented; a structural command `\fn` indicates that the following code is a function, and the command `\brief` is used to give a small description of this function.

This way of documenting a source file is useful if you just want to add documentation to your project without adding real code. When you place a comment block in a file with one of the following extensions `.dox`, `.txt`, or `.doc` then Doxygen will parse the comments and build the appropriate documentation, but it will hide this auxiliary file from the file list.

The FreeCAD project adds several files ending in `.dox` in many directories in order to provide a description, or examples, of the code there. It is important that such files are correctly categorized in a group or namespace, for which Doxygen provides some auxiliary commands like `\defgroup`, `\ingroup`, and `\namespace`.


<div class="mw-collapsible mw-collapsed toccolours">

Example `src/Base/core-base.dox`; this file in FreeCAD\'s source tree gives a short explanation of the `Base` namespace.


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

Another example is the file `src/Gui/Command.cpp`. Before the implementation details of the `Gui::Command` methods, there is a documentation block that explains some details of the command framework of FreeCAD. It has various `\section` commands to structure the documentation. It even includes example code enclosed in a pair of `\code` and `\endcode` keywords; when the file is processed by Doxygen this code example will be specially formatted to stand out. The `\ref` keyword is used in several places to create links to named sections, subsections, pages or anchors elsewhere in the documentation. Similarly, the `\see` or `\sa` commands print \"See also\" and provide a link to other classes, functions, methods, variables, files or URLs.


<div class="mw-collapsible mw-collapsed toccolours">

Example `src/Gui/Command.cpp`


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

### Example from the VTK project 

This is an example from [VTK](https://vtk.org/), a 3D visualization library used to present scientific data, like finite element results, and point cloud information.

A class to store a collection of coordinates is defined in a C++ header file. The top part of the file is commented, and a few keywords are used, like `@class`, `@brief`, and `@sa` to indicate important parts. Inside the class, before the class method prototypes, a block of commented text explains what the function does, and its arguments.

-   Source code of [vtkArrayCoordinates.h](https://github.com/Kitware/VTK/blob/master/Common/Core/vtkArrayCoordinates.h).
-   Doxygen produced documentation for the [vtkArrayCoordinates class](http://www.vtk.org/doc/nightly/html/classvtkArrayCoordinates.html).

## Compiling the documentation 

<img alt="" src=images/FreeCAD_doxygen_workflow.svg  style="width:800px;">



*General workflow to produce source code documentation with Doxygen.*

To generate the source code documentation there are two basic steps:

1.  Create a configuration file to control how Doxygen will process the source files.
2.  Run `doxygen` on that configuration.


<div class="mw-collapsible mw-collapsed toccolours">

The process is described in the following.


<div class="mw-collapsible-content">

-   Make sure you have the programs `doxygen` and `doxywizard` in your system. It is also recommended to have the `dot` program from [Graphviz](https://www.graphviz.org/), in order to generate diagrams with the relationships between classes and namespaces. On Linux systems these programs can be installed from your package manager.


```python
sudo apt install doxygen doxygen-gui graphviz
```

-   Make sure you are in the same folder as your source files, or in the toplevel directory of your source tree, if you have many source files in different sub-directories.


```python
cd toplevel-source
```

-   Run `doxygen -g DoxyDoc.cfg` to create a configuration file named `DoxyDoc.cfg`. If you omit this name, it will default to `Doxyfile` without an extension.
-   This is a big, plain text file that includes many variables with their values. In the Doxygen manual these variables are called \"tags\". The configuration file and all tags are described extensively in the [Configuration](http://www.doxygen.nl/manual/config.html) section of the manual. You can open the file with any text editor, and edit the value of each tag as necessary. In the same file you can read comments explaining each of the tags, and their default values.


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

-   Instead of using a text editor, you may launch `doxywizard` to edit many tags at the same time. With this interface you may define many properties such as project information, type of output (HTML and LaTeX), use of Graphviz to create diagrams, warning messages to display, file patterns (extensions) to document or to exclude, input filters, optional headers and footers for the HTML generated pages, options for LaTeX, RTF, XML, or Docbook outputs, and many other options.


```python
doxywizard DoxyDoc.cfg
```

-   Another option is to create the configuration file from scratch, and add only the tags that you want with a text editor.
-   After the configuration is saved, you can run Doxygen on this configuration file.


```python
doxygen DoxyDoc.cfg
```

-   The generated documentation will be created inside a folder named `toplevel-source/html`. It will consist of many HTML pages, PNG images for graphics, cascading style sheets (`.css`), Javascript files (`.js`), and potentially many sub-directories with more files depending on the size of your code. The point of entry into the documentation is `index.html`, which you can open with a web browser.


```python
xdg-open toplevel-source/html/index.html
```


</div>


</div>

If you are writing new classes, functions or an entire new workbench, it is recommended that you run `doxygen` periodically to see that the documentation blocks, [Markdown](#Markdown_support.md), and [special commands](#Doxygen_markup.md) are being read correctly, and that all public functions are fully documented. Please also read the [documentation tips](https://github.com/FreeCAD/FreeCAD/blob/master/src/Doc/doctips.dox) located in the source code.

When generating the complete FreeCAD documentation, you don\'t run `doxygen` directly. Instead, the project uses `cmake` to configure the build environment, and then `make` triggers compilation of the FreeCAD sources and of the Doxygen documentation; this is explained in the [source documentation](source_documentation.md) page.

## Doxygen markup 

All Doxygen [documentation commands](http://www.doxygen.nl/manual/commands.html) start with a backslash `\` or an at-symbol `@`, at your preference. Normally the backslash `\` is used, but occasionally the `@` is used to improve readability.

The commands can have one or more arguments. In the Doxygen manual the arguments are described as follows.

-   If `<sharp>` braces are used the argument is a single word.
-   If `(round)` braces are used the argument extends until the end of the line on which the command was found.
-   If {curly} braces are used the argument extends until the next paragraph. Paragraphs are delimited by a blank line or by a section indicator.
-   If `[square]` brackets are used the argument is optional.


<div class="mw-collapsible mw-collapsed toccolours">

Some of the most common keywords used in the FreeCAD documentation are presented here.


<div class="mw-collapsible-content">

-    (group title), see [\\defgroup](http://www.doxygen.nl/manual/commands.html#cmddefgroup), and [Grouping](http://www.doxygen.nl/manual/grouping.html).
-   ]), see [\\ingroup](http://www.doxygen.nl/manual/commands.html#cmdingroup), and [Grouping](http://www.doxygen.nl/manual/grouping.html).
-    [(title)], see [\\addtogroup](http://www.doxygen.nl/manual/commands.html#cmdaddtogroup), and [Grouping](http://www.doxygen.nl/manual/grouping.html).
-   \author { list of authors }, see [\\author](http://www.doxygen.nl/manual/commands.html#cmdauthor); indicates the author of this piece of code.
-   \brief { brief description }, see [\\brief](http://www.doxygen.nl/manual/commands.html#cmdbrief); briefly describes the function.
-   ], see [\\file](http://www.doxygen.nl/manual/commands.html#cmdfile); documents a source or header file.
-    (title), see [\\page](http://www.doxygen.nl/manual/commands.html#cmdpage); puts the information in a separate page, not directly related to one specific class, file or member.
-   , see [\\package](http://www.doxygen.nl/manual/commands.html#cmdpackage); indicates documentation for a Java package (but also used with Python).
-   \fn (function declaration), see [\\fn](http://www.doxygen.nl/manual/commands.html#cmdfn); documents a function.
-   \var (variable declaration), see [\\var](http://www.doxygen.nl/manual/commands.html#cmdvar); documents a variable; it is equivalent to `\fn`, `\property`, and `\typedef`.
-    (section title), see [\\section](http://www.doxygen.nl/manual/commands.html#cmdsection); starts a section.
-    (subsection title), see [\\subsection](http://www.doxygen.nl/manual/commands.html#cmdsubsection); starts a subsection.
-   , see [\\namespace](http://www.doxygen.nl/manual/commands.html#cmdnamespace); indicates information for a namespace.
-   \cond [(section-label)], and \endcond, see [\\cond](http://www.doxygen.nl/manual/commands.html#cmdcond); defines a block to conditionally document or omit.
-   , see [\\a](http://www.doxygen.nl/manual/commands.html#cmda); displays the argument in italics for emphasis.
-    { parameter description }, see [\\param](http://www.doxygen.nl/manual/commands.html#cmdparam); indicates the parameter of a function.
-   \return { description of the return value }, see [\\return](http://www.doxygen.nl/manual/commands.html#cmdreturn); specifies the return value.
-   \sa { references }, see [\\sa](http://www.doxygen.nl/manual/commands.html#cmdsa); prints \"See also\".
-   \note { text }, see [\\note](http://www.doxygen.nl/manual/commands.html#cmdnote); adds a paragraph to be used as a note.


</div>


</div>

## Markdown support 

Since Doxygen 1.8, Markdown syntax is recognized in documentation blocks. Markdown is a minimalistic formatting language inspired by plain text email which, similar to wiki syntax, intends to be simple and readable without requiring complicated code like that found in HTML, LaTeX or Doxygen\'s own commands. Markdown has gained popularity with free software, especially in online platforms like Github, as it allows creating documentation without using complicated code. See the [Markdown support](http://www.doxygen.nl/manual/markdown.html) section in the Doxygen manual to learn more. Visit the [Markdown website](https://daringfireball.net/projects/markdown/) to learn more about the origin and philosophy of Markdown.

Doxygen supports a standard set of Markdown instructions, as well as some extensions such as [Github Markdown](https://github.github.com/github-flavored-markdown/).


<div class="mw-collapsible mw-collapsed toccolours">

Some examples of Markdown formatting are presented next.


<div class="mw-collapsible-content">

The following is standard Markdown. 
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

The following are Markdown extensions.

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

## Parsing of documentation blocks 

The text inside a special documentation block is parsed before it is written to the HTML and LaTeX output files. During parsing the following steps take place:

-   Markdown formatting is replaced by corresponding HTML or special commands.
-   The special commands inside the documentation are executed. See the section [Special Commands](http://www.doxygen.nl/manual/commands.html) in the manual for an explanation of each command.
-   If a line starts with some whitespace followed by one or more asterisks (`*`) and then optionally more whitespace, then all whitespace and asterisks are removed.
-   All resulting blank lines are treated as paragraph separators.
-   Links are automatically created for words corresponding to documented classes or functions. If the word is preceded by a percentage symbol `%`, then this symbol is removed, and no link is created for the word.
-   Links are created when certain patterns are found in the text. See the section [Automatic link generation](http://www.doxygen.nl/manual/autolink.html) in the manual for more information.
-   HTML tags that are in the documentation are interpreted and converted to LaTeX equivalents for the LaTeX output. See the section [HTML Commands](http://www.doxygen.nl/manual/htmlcmds.html) in the manual for an explanation of each supported HTML tag.

## Doxygen with Python code 

Doxygen works best for statically typed languages like C++. However, it can also create [documentation for Python files](http://www.doxygen.nl/manual/docblocks.html#pythonblocks).

There are two ways to write documentation blocks for Python:

1.  The Pythonic way, using \"docstrings\", that is, a block of text surrounded by '''triple quotes''' immediately after the class or function definition.
2.  The Doxygen way, putting comments before the class or function definition; in this case double hash characters `##` are used to start the documentation block, and then a single hash character can be used in subsequent lines.

Note:

-   The first option is preferred to comply with [PEP8](https://www.python.org/dev/peps/pep-0008/#documentation-strings), [PEP257](https://www.python.org/dev/peps/pep-0257/) and most style guidelines for writing Python (see [1](https://realpython.com/python-pep8/), [2](https://realpython.com/documenting-python-code/)). It is recommended to use this style if you intend to produce documented sources using [Sphinx](https://www.sphinx-doc.org/en/master/), which is a very common tool to document Python code. If you use this style, Doxygen will be able to extract the comments verbatim, but Doxygen special commands starting with `\` or `@` won\'t work.
-   The second option isn\'t the traditional Python style, but it allows you to use Doxygen\'s special commands like `\param` and `\var`.

### First style: Pythonic documentation 

In the following example one docstring is at the beginning to explain the general contents of this module (file). Then docstrings appear inside the function, class, and class method definitions. In this way, Doxygen will extract the comments and present them as is, without modification.


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

### Second style: documentation block before the code 

In the following example the documentation blocks start with double hash signs `##`. One appears at the beginning to explain the general content of this module (file). Then there are blocks before the function, class, and class method definitions, and there is one block after a class variable. In this way, Doxygen will extract the documentation, recognize the special commands `@package`, `@param`, and `@var`, and format the text accordingly. 
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

### Compiling the documentation 

Compilation of documentation proceeds the same as [for C++ sources](#Compiling_the_documentation.md). If both Python files, `pyexample_a.py` and `pyexample_b.py`, with distinct commenting style are in the same directory, both will be processed. 
```python
cd toplevel-source/
doxygen -g
doxygen Doxyfile
xdg-open ./html/index.html
```

The documentation should show similar information to the following, and create appropriate links to the individual modules and classes. 
```python
Class List
Here are the classes, structs, unions and interfaces with brief descriptions:

N  pyexample_a
   C  PyClass

N  pyexample_b  Documentation for this module
   C  PyClass   Documentation for a class
```

### Converting the Pythonic style to Doxygen style 

In the previous example, the Python file that is commented in a [Doxygen style](#Second_style__documentation_block_before_the_code.md) shows more detailed information and formatting for its classes, functions, and variables. The reason is that this style allows Doxygen to extract the special commands that start with `\` or `@`, while the [Pythonic style](#First_style__Pythonic_documentation.md) does not. Therefore, it would be desirable to convert the Pythonic style to Doxygen style before compiling the documentation. This is possible with an auxiliary Python program called [doxypypy](https://github.com/Feneric/doxypypy). This program is inspired by an older program called [doxypy](https://github.com/Feneric/doxypy), which would take the Pythonic '''docstrings''' and convert them to the Doxygen comment blocks that start with a double hash `##`. Doxypypy goes further than this, as it analyzes the docstrings and extracts items of interest like variables and arguments, and even doctests (example code in the docstrings).

Doxypypy can be installed using `pip`, the Python package installer. 
```python
pip3 install --user doxypypy
```

If the `pip` command is used without the `--user` option, it will require superuser (root) privileges to install the package, but this is not needed in most cases; use root permissions only if you are certain the package won\'t collide with your distribution provided packages.

If the package was installed as a user, it may reside in your home directory, for example, in `$HOME/.local/bin`. If this directory is not in your system\'s `PATH`, the program will not be found. Therefore, add the directory to the `PATH` variable, either in your `$HOME/.bashrc` file, or in your `$HOME/.profile` file. 
```python
export PATH="$HOME/.local/bin:$PATH"
```

Alternatively, you can create a symbolic link to the `doxypypy` program, placing the link in a directory that is already included in the `PATH`. 
```python
mkdir -p $HOME/bin
ln -s $HOME/.local/bin/doxypypy $HOME/bin/doxypypy
```

Once the `doxypypy` program is installed, and accessible from the terminal, a Python file with Pythonic docstrings can be reformatted to Doxygen style with the following instructions. The program outputs the reformatted code to standard output, so redirect this output to a new file. 
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

The original file has a comment at the top '''@package pyexample_pythonic that indicates the module or namespace that is being described by the file. This `@package` keyword is not interpreted when using triple quotes in the comment block.

In the new file the commenting style is changed so the line becomes `##@package pyexample_pythonic`, which now will be interpreted by Doxygen. However, to be interpreted correctly, the argument has to be edited manually to match the new module (file) name; after doing this the line should be `##@package pyexample_doxygen`.


<div class="mw-collapsible mw-collapsed toccolours">


`pyexample_doxygen.py`

(the top is manually edited, the rest stays the same)


<div class="mw-collapsible-content">


```python
##@package pyexample_doxygen
#Documentation for this module.
#More details go here.
#
```


</div>


</div>

To compile, create the configuration, and run `doxygen` in the toplevel directory that contains the files. 
```python
cd toplevel-source/
doxygen -g
doxygen Doxyfile
xdg-open ./html/index.html
```

The documentation should show similar information to the following, and create appropriate links to the individual modules. 
```python
Namespace List
Here is a list of all documented namespaces with brief descriptions:

 N  pyexample_doxygen   Documentation for this module
 N  pyexample_pythonic  
```

### Converting the comment style on the fly 

In the previous example, the conversion of the documentation blocks was done manually with only one source file. Ideally we want this conversion to occur automatically, on the fly, with any number of Python files. To do this, the Doxygen configuration must be edited accordingly.

To start, don\'t use the `doxypypy` program directly; instead, create the configuration file with `doxygen -g`, then edit the created `Doxyfile`, and modify the following tag. 
```python
FILTER_PATTERNS        = *.py=doxypypy_filter
```

What this does is that files that match the pattern, all files with a extension ending in `.py`, will go through the `doxypypy_filter` program. Every time Doxygen encounters such file in the source tree, the file name will be passed as the first argument to this program. 
```python
doxypypy_filter example.py
```

The `doxypypy_filter` program does not exist by default; it should be created as a shell script to run `doxypypy` with the appropriate options, and to take a file as its first argument. 
```python
#!/bin/sh
doxypypy -a -c "$1"
```

After saving this shell script, make sure it has execute permissions, and that it is located in a directory contained in your system\'s `PATH`. 
```python
chmod a+x doxypypy_filter
mv doxypypy_filter $HOME/bin
```

On Windows systems, a batch file can be used in a similar way. 
```python
doxypypy -a -c %1
```

With this configuration done, the `doxygen Doxyfile` command can be run to generate the documentation as usual. Every Python file using Pythonic '''triple quotes''' will be reformatted on the fly to use `##Doxygen` style comments, and then will be processed by Doxygen, which now will be able to interpret the [special commands](#Doxygen_markup.md) and [Mardown syntax](#Markdown_support.md). The original source code won\'t be modified, and no temporary file with a different name needs to be created as in [the previous section](#Converting_the_Pythonic_style_to_Doxygen_style.md); therefore, if a `@package example` instruction is found, it doesn\'t need to be changed manually.

Note that existing Python files which already use the `##double hash` style for their comment blocks won\'t be affected by the `doxypypy` filter, and will be processed by Doxygen normally.

<img alt="" src=images/FreeCAD_doxygen_doxypypy_workflow.svg  style="width:800px;">



*General workflow to produce source code documentation with Doxygen, when the Python files are filtered to transform the comment blocks.*

### Python code quality check 

To use the automatic conversion of documentation blocks it is important that the original Python sources are correctly written, following the Pythonic guidelines in [PEP8](https://www.python.org/dev/peps/pep-0008/#documentation-strings) and [PEP257](https://www.python.org/dev/peps/pep-0257/). Sloppily written code will cause `doxypypy` to fail when processing the file, and thus Doxygen will be unable to format the documentation correctly.


<div class="mw-collapsible mw-collapsed toccolours">

The following commenting styles will not allow parsing of the docstrings by `doxypypy`, so they should be avoided.


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

Always use triple quotes for the docstrings, and make sure they immediately follow the class or function declaration.

It is also a good idea to verify the quality of your Python code with a tool such as [flake8](http://flake8.pycqa.org/en/latest/) ([Gitlab](https://gitlab.com/pycqa/flake8)). Flake8 primarily combines three tools, [Pyflakes](https://github.com/PyCQA/pyflakes), [Pycodestyle](https://github.com/PyCQA/pycodestyle) (formerly pep8), and the [McCabe complexity checker](https://github.com/PyCQA/mccabe), in order to enforce proper Pythonic style.


```python
pip install --user flake8
flake8 example.py
```

To check all files inside a source tree use `find`. 
```python
find toplevel-source/ -name '*.py' -exec flake8 {} '+'
```

If the project demands it, some code checks deemed too strict can be ignored. The error codes can be consulted in the [Pycodestyle documentation](https://pycodestyle.readthedocs.io/en/latest/intro.html#error-codes). 
```python
find toplevel-source/ -name '*.py' -exec flake8 --ignore=E266,E402,E722,W503 --max-line-length=100 {} '+'
```

In similar way, a program that primarily checks that comments comply with [PEP257](https://www.python.org/dev/peps/pep-0257/) is [Pydocstyle](https://github.com/PyCQA/pydocstyle). The error codes can be consulted in the [Pydocstyle documentation](http://www.pydocstyle.org/en/4.0.0/error_codes.html). 
```python
pip install --user pydocstyle
pydocstyle example.py
```

Also use it with `find` to perform docstring checks on all source files. 
```python
find toplevel-source/ -name '*.py' -exec pydocstyle {} '+'
```

## Source documentation with Sphinx 

[Sphinx](https://www.sphinx-doc.org/en/master/) is the most popular system to document Python source code. However, since FreeCAD\'s core functions and workbenches are written in C++ it was deemed that Doxygen is a better documentation tool for this project.

While Sphinx can natively parse Python docstrings, it requires a bit more work to parse C++ sources. The [Breathe](https://breathe.readthedocs.io/en/latest/) ([Github](https://github.com/michaeljones/breathe)) project is an attempt at bridging the gap between Sphinx and Doxygen, in order to integrate both Python and C++ source code documentation in the same system. First, Doxygen needs to be configured to output an XML file; the XML output is then read by Breathe, and converted to suitable input for Sphinx.

See the [Quick start guide](https://breathe.readthedocs.io/en/latest/quickstart.html) in the Breathe documentation to know more about this process.

See this answer in [Stackoverflow](https://stackoverflow.com/a/35377654) for other alternatives to documenting C++ and Python code together in the same project.

## Related

-   [Source documentation](Source_documentation.md)
-   [FreeCAD API website](https://www.freecadweb.org/api/)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Developer_Documentation](Category_Developer_Documentation.md) > [Developer](Category_Developer.md) > [3rd Party](Category_3rd Party.md) > Doxygen/es
