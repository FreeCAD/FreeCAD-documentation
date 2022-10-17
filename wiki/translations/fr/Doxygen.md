# Doxygen/fr
## A propos 


{{TOCright}}

Doxygen est un outil populaire pour générer de la documentation à partir de sources C ++ annotées. Il prend également en charge d\'autres langages de programmation populaires tels que C#, PHP, Java et Python. Visitez le [site Web Doxygen](http   *//www.doxygen.nl/) pour en savoir plus sur le système et consultez le [Manuel Doxygen](http   *//www.doxygen.nl/manual/index.html) pour plus d\'informations.

## Doxygen et FreeCAD 

Ce document fournit une brève introduction à Doxygen, en particulier comment il est utilisé dans FreeCAD pour documenter ses sources. Consultez la page [Documentation du code source](source_documentation/fr.md) pour obtenir des instructions sur la construction de la documentation FreeCAD, également hébergée en ligne sur le site Web [FreeCAD API](https   *//www.freecadweb.org/api/).

<img alt="" src=images/FreeCAD_doxygen_workflow.svg  style="width   *800px;">



*Flux général de travail pour produire une documentation du code source avec Doxygen.*

## Doxygen avec du code C++ 

La section [Mise en route (étape 3)](http   *//www.doxygen.nl/manual/starting.html) du manuel Doxygen mentionne les méthodes de base pour documenter les sources.

Pour les membres, les classes et les espaces de noms, deux options sont disponibles   *

1.  Placez un \"bloc de documentation\" spécial (un paragraphe commenté) avant la déclaration ou la définition de la fonction, du membre, de la classe ou de l\'espace de noms. Pour les fichiers, classes et membres espaces de nom (variables), il est également autorisé de placer la documentation directement après le membre. Voir la section [Blocs de commentaires spéciaux](http   *//www.doxygen.nl/manual/docblocks.html#specialblock) dans le manuel pour en savoir plus sur ces blocs.
2.  Placez un bloc de documentation spécial ailleurs (un autre fichier ou un autre emplacement dans le même fichier) et insérez une \"commande structurelle\" dans le bloc de documentation. Une commande structurelle lie un bloc de documentation à une certaine entité pouvant être documentée (une fonction, un membre, une variable, une classe, un espace de noms ou un fichier). Voir la section [Documentation à d\'autres endroits](http   *//www.doxygen.nl/manual/docblocks.html#structuralcommands) dans le manuel pour en savoir plus sur les commandes structurelles.

Remarque   *

-   L\'avantage de la première option est qu\'il n\'est pas nécessaire de répéter le nom de l\'entité (fonction, membre, variable, classe ou espace de nom) car Doxygen analysera le code et extraira les informations pertinentes.
-   Les fichiers ne peuvent être documentés qu\'en utilisant la deuxième option car il n\'y a aucun moyen de mettre un bloc de documentation avant un fichier. Bien sûr, les membres de fichiers (fonctions, variables, typedefs, définit) n\'ont pas besoin d\'une commande structurelle explicite. il suffit de mettre un bloc de documentation avant ou après eux fonctionnera très bien.

### Premier style   * bloc de documentation avant le code 

Généralement, vous souhaiterez documenter le code dans le fichier d\'en-tête, juste avant la déclaration de classe ou le prototype de fonction. Ceci permet de garder la déclaration et la documentation proches les unes des autres, il est donc facile de mettre à jour la dernière si le premier change.

Le bloc spécial de documentation commence comme un commentaire de type C `/*` mais comporte un astérisque supplémentaire soit `/**`. Le bloc se termine par un `*/` correspondant. Une alternative consiste à utiliser des commentaires de style C ++ `//` avec une barre oblique supplémentaire soit `///`. 
```python
/**
 * Returns the name of the workbench object.
 */
std   *   *string name() const;

/**
 * Set the name to the workbench object.
 */
void setName(const std   *   *string&);

/// remove the added TaskWatcher
void removeTaskWatcher(void);
```

### Deuxième style   * bloc de documentation ailleurs 

Sinon, la documentation peut être placée dans un autre fichier (ou dans le même fichier en haut ou en bas, ou ailleurs) à l\'écart de la déclaration de classe ou du prototype de fonction. Dans ce cas, vous aurez des informations dupliquées, une fois dans le fichier source réel et une fois dans le fichier de documentation.

Premier fichier, `source.h`   * 
```python
std   *   *string name() const;
void setName(const std   *   *string&);
```

Deuxième fichier, `source.h.dox`   * 
```python
/** \file source.h
 *  \brief The documentation of source.h
 *   
 *   The details of this file go here.
 */

/** \fn std   *   *string name() const;
 *  \brief Returns the name of the workbench object.
 */
/** \fn void setName(const std   *   *string&);
 *  \brief Set the name to the workbench object.
 */
```

Dans ce cas, la commande structurelle `\file` est utilisée pour indiquer le fichier source documenté. Une commande structurelle `\fn` indique que le code suivant est une fonction et que la commande `\brief` est utilisée pour décrire brièvement cette fonction.

Cette façon de documenter un fichier source est utile si vous souhaitez simplement ajouter de la documentation à votre projet sans ajouter de code réel. Lorsque vous placez un bloc de commentaires dans un fichier portant l'une des extensions suivantes `.dox`, `.txt`, ou `.doc` alors Doxygen analysera les commentaires et construira la documentation appropriée mais masquera ce fichier auxiliaire de la liste des fichiers.

Le projet FreeCAD ajoute plusieurs fichiers se terminant par `.dox` dans de nombreux répertoires afin de fournir une description ou des exemples du code correspondant. Il est important que ces fichiers soient correctement classés dans un groupe ou un espace de noms pour lequel Doxygen fournit des commandes auxiliaires telles que `\defgroup`, `\ingroup` et `\namespace`.


<div class="mw-collapsible mw-collapsed toccolours">

Exemple `src/Base/core-base.dox`. Ce fichier dans l\'arborescence des sources de FreeCAD donne une brève explication de l\'espace de noms `Base`.


<div class="mw-collapsible-content">


```python
/** \defgroup BASE Base
 *  \ingroup CORE
    \brief Basic structures used by other FreeCAD componentsThe Base module includes most of the basic functions of FreeCAD, such as   *
    - Console services   * printing different kinds of messages to the FreeCAD report view or the terminal
    - Python interpreter   * handles the execution of Python code in FreeCAD
    - Parameter handling   * Management, saving and restoring of user preferences settings
    - Units   * Management and conversion of different units

*/

/*! \namespace Base
    \ingroup BASE
    \brief Basic structures used by other FreeCAD components

    The Base module includes most of the basic functions of FreeCAD, such as   *
    - Console services   * printing different kinds of messages to the FreeCAD report view or the terminal
    - Python interpreter   * handles the execution of Python code in FreeCAD
    - Parameter handling   * Management, saving and restoring of user preferences settings
    - Units   * Management and conversion of different units
*/
```


</div>


</div>

Un autre exemple est le fichier `src/Gui/Command.cpp`. Avant les détails d\'implémentation des méthodes `Gui   *   *Command`, il existe un bloc de documentation qui explique certains détails de la structure de commande de FreeCAD. Il comporte diverses commandes `\section` pour structurer la documentation. Il comprend même un exemple de code inclus dans une paire de mots-clés `\code` et `\endcode`. Lorsque le fichier est traité par Doxygen, cet exemple de code sera spécialement formaté pour se démarquer. Le mot clé `\ref` est utilisé à plusieurs endroits pour créer des liens vers des sections, sous-sections, pages ou ancres nommées dans la documentation. De même, les commandes `\see` ou `\sa` affichent le libellé \"See also\" et fournissent un lien vers d\'autres classes, fonctions, méthodes, variables, fichiers ou URL.


<div class="mw-collapsible mw-collapsed toccolours">

Exemple `src/Gui/Command.cpp`


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
 * \a Gui   *   *CommandBase and \a Gui   *   *Action that represent the link between Qt's QAction world and the FreeCAD's command world. 
 *
 * The Action class holds a pointer to QAction and CommandBase and acts as a mediator and -- to save memory -- that gets created 
 * (@ref Gui   *   *CommandBase   *   *createAction()) not before it is added (@ref Gui   *   *Command   *   *addTo()) to a menu or toolbar.
 *
 * Now, the implementation of the slots of MainWindow can be done in the method \a activated() of subclasses of Command instead.
 *
 * For example, the implementation of the "Open file" command can be done as follows.
 * \code
 * class OpenCommand    * public Command
 * {
 * public   *
 *   OpenCommand()    * Command("Std_Open")
 *   {
 *     // set up menu text, status tip, ...
 *     sMenuText     = "&Open";
 *     sToolTipText  = "Open a file";
 *     sWhatsThis    = "Open a file";
 *     sStatusTip    = "Open a file";
 *     sPixmap       = "Open"; // name of a registered pixmap
 *     sAccel        = "Shift+P"; // or "P" or "P, L" or "Ctrl+X, Ctrl+C" for a sequence
 *   }
 * protected   *
 *   void activated(int)
 *   {
 *     QString filter ... // make a filter of all supported file formats
 *     QStringList FileList = QFileDialog   *   *getOpenFileNames( filter,QString   *   *null, getMainWindow() );
 *     for ( QStringList   *   *Iterator it = FileList.begin(); it != FileList.end(); ++it ) {
 *       getGuiApplication()->open((*it).latin1());
 *     }
 *   }
 * };
 * \endcode
 * An instance of \a OpenCommand must be created and added to the \ref Gui   *   *CommandManager to make the class known to FreeCAD.
 * To see how menus and toolbars can be built go to the @ref workbench.
 *
 * @see Gui   *   *Command, Gui   *   *CommandManager
 */
```


</div>


</div>

### Exemple du projet VTK 

Ceci est un exemple tiré de [VTK](https   *//vtk.org/), une bibliothèque de visualisation 3D utilisée pour présenter des données scientifiques, telles que des résultats d\'éléments finis et des informations de nuage de points.

Une classe pour stocker une collection de coordonnées est définie dans un fichier d\'en-tête C++. La partie supérieure du fichier est commentée et quelques mots-clés sont utilisés, tels que `@class`, `@brief` et `@sa` pour indiquer les parties importantes. Dans la classe, avant les prototypes de méthode de classe, un bloc de texte commenté explique le rôle de la fonction et ses arguments.

-   Code source de [vtkArrayCoordinates.h](https   *//github.com/Kitware/VTK/blob/master/Common/Core/vtkArrayCoordinates.h).
-   Doxygen a produit de la documentation pour la classe [vtkArrayCoordinates](http   *//www.vtk.org/doc/nightly/html/classvtkArrayCoordinates.html).

## Compiler la documentation 

<img alt="" src=images/FreeCAD_doxygen_workflow.svg  style="width   *800px;">



*Flux général de travail pour produire une documentation du code source avec Doxygen.*

Pour générer la documentation du code source, il existe deux étapes de base   *

1.  Créez un fichier de configuration pour contrôler la façon dont Doxygen traitera les fichiers source.
2.  Exécutez `doxygen` sur cette configuration.


<div class="mw-collapsible mw-collapsed toccolours">

Le processus est décrit ci-dessous.


<div class="mw-collapsible-content">

-   Assurez-vous que les programmes `doxygen` et `doxywizard` sont installés sur votre système. Il est également recommandé de disposer du programme `dot` de [Graphviz](https   *//www.graphviz.org/) afin de générer des diagrammes avec les relations entre les classes et les espaces de noms. Sur les systèmes Linux, ces programmes peuvent être installés à partir de votre gestionnaire de paquets.


```python
sudo apt install doxygen doxygen-gui graphviz
```

Assurez-vous d\'être dans le même dossier que vos fichiers sources ou dans le répertoire toplevel de votre arborescence des sources si vous avez plusieurs fichiers sources dans différents sous-répertoires. 
```python
cd toplevel-source
```

-   Exécutez `doxygen -g DoxyDoc.cfg` pour créer un fichier de configuration nommé `DoxyDoc.cfg`. Si vous omettez ce nom, la valeur par défaut sera `Doxyfile` sans extension.
-   Il s'agit d'un gros fichier texte contenant de nombreuses variables avec leurs valeurs. Dans le manuel Doxygen, ces variables sont appelées \"tags\". Le fichier de configuration et toutes les balises sont décrits en détail dans la section [Configuration](http   *//www.doxygen.nl/manual/config.html) du manuel. Vous pouvez ouvrir le fichier avec n'importe quel éditeur de texte et éditer la valeur de chaque balise selon vos besoins. Dans le même fichier, vous pouvez lire des commentaires expliquant chacune des balises et leurs valeurs par défaut.


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

-   Au lieu d\'utiliser un éditeur de texte, vous pouvez lancer `doxywizard` pour modifier plusieurs tags en même temps. Avec cette interface, vous pouvez définir de nombreuses propriétés telles que les informations de projet, le type de sortie (HTML et LaTeX), l'utilisation de Graphviz pour créer des diagrammes, les messages d'avertissement à afficher, les modèles de fichiers (extensions) à documenter ou à exclure, les filtres de saisie, les en-têtes facultatifs. et des bas de page pour les pages générées HTML, des options pour les sorties LaTeX, RTF, XML ou Docbook, et de nombreuses autres options.


```python
doxywizard DoxyDoc.cfg
```

-   Une autre option consiste à créer le fichier de configuration à partir de rien et à ajouter uniquement les balises souhaitées avec un éditeur de texte.
-   Une fois la configuration enregistrée, vous pouvez exécuter Doxygen sur ce fichier de configuration.


```python
doxygen DoxyDoc.cfg
```

-   La documentation générée sera créée dans un dossier nommé `toplevel-source/html`. Il se composera de nombreuses pages HTML, d'images PNG pour les graphiques, de feuilles de style en cascade (`.css`), de fichiers Javascript (`.js`) et éventuellement de nombreux sous-répertoires contenant plus de fichiers, selon la taille de votre code. Le point d'entrée dans la documentation est `index.html` que vous pouvez ouvrir avec un navigateur Web.


```python
xdg-open toplevel-source/html/index.html
```


</div>


</div>

Si vous écrivez de nouvelles classes, fonctions ou un tout nouveau atelier, il est recommandé d\'exécuter périodiquement `doxygen` pour vérifier que la documentation bloque, [Markdown](#Support_de_Markdown.md) et [commandes spéciales](#Balisage_Doxygen.md) sont lus correctement et toutes les fonctions publiques sont entièrement documentées. Veuillez également lire les [conseils de documentation](https   *//github.com/FreeCAD/FreeCAD/blob/master/src/Doc/doctips.dox) situés dans le code source.

Lorsque vous générez la documentation complète de FreeCAD, vous n'exécutez pas directement `doxygen`. Au lieu de cela, le projet utilise `cmake` pour configurer l\'environnement de construction, puis `make` déclenche la compilation des sources FreeCAD et de la documentation Doxygen; ceci est expliqué dans la page [Documentation du code source](source_documentation/fr.md).

## Balisage Doxygen 

Toutes les commandes Doxygen [documentation des commandes](http   *//www.doxygen.nl/manual/commands.html) commencent par une barre oblique inversée `\` ou un symbole at `@`, selon vos préférences. Normalement, la barre oblique inversée `\` est utilisée mais il arrive que `@` soit utilisée pour améliorer la lisibilité.

Les commandes peuvent avoir un ou plusieurs arguments. Dans le manuel Doxygen, les arguments sont décrits comme suit.

-   Si des accolades `<sharp>` sont utilisées, l\'argument est un mot unique.
-   Si vous utilisez des accolades `(round)`, l\'argument s\'étend jusqu\'à la fin de la ligne sur laquelle la commande a été trouvée.
-   Si des accolades {curly} sont utilisées, l\'argument s\'étend jusqu\'au paragraphe suivant. Les paragraphes sont délimités par une ligne vide ou par un indicateur de section.
-   Si des crochets `[square]` sont utilisés, l\'argument est facultatif.


<div class="mw-collapsible mw-collapsed toccolours">

Certains des mots-clés les plus couramment utilisés dans la documentation FreeCAD sont présentés ici.


<div class="mw-collapsible-content">

-    (group title), voir [\\defgroup](http   *//www.doxygen.nl/manual/commands.html#cmddefgroup), et [Grouping](http   *//www.doxygen.nl/manual/grouping.html).
-   ]), voir [\\ingroup](http   *//www.doxygen.nl/manual/commands.html#cmdingroup), et [Grouping](http   *//www.doxygen.nl/manual/grouping.html).
-    [(title)], voir [\\addtogroup](http   *//www.doxygen.nl/manual/commands.html#cmdaddtogroup), et [Grouping](http   *//www.doxygen.nl/manual/grouping.html).
-   \author { list of authors }, voir [\\author](http   *//www.doxygen.nl/manual/commands.html#cmdauthor); indique l\'auteur de ce morceau de code.
-   \brief { brief description }, voir [\\brief](http   *//www.doxygen.nl/manual/commands.html#cmdbrief); décrit brièvement la fonction.
-   ], voir [\\file](http   *//www.doxygen.nl/manual/commands.html#cmdfile); documente un fichier source ou en-tête.
-    (title), voir [\\page](http   *//www.doxygen.nl/manual/commands.html#cmdpage); place les informations dans une page distincte, sans lien direct avec une classe, un fichier ou un membre spécifique.
-   , voir [\\package](http   *//www.doxygen.nl/manual/commands.html#cmdpackage); indique la documentation d\'un package Java (mais également utilisée avec Python).
-   \fn (function declaration), voir [\\fn](http   *//www.doxygen.nl/manual/commands.html#cmdfn); documente une fonction.
-   \var (variable declaration), voir [\\var](http   *//www.doxygen.nl/manual/commands.html#cmdvar); documente une variable; il est équivalent à `\fn`, `\propriété` et `\typedef`.
-    (section title), see [\\section](http   *//www.doxygen.nl/manual/commands.html#cmdsection); commence une section.
-    (subsection title), voir [\\subsection](http   *//www.doxygen.nl/manual/commands.html#cmdsubsection); commence une sous-section.
-   , voir [\\namespace](http   *//www.doxygen.nl/manual/commands.html#cmdnamespace); indique des informations pour un espace de noms.
-   \cond [(section-label)], and \endcond, voir [\\cond](http   *//www.doxygen.nl/manual/commands.html#cmdcond); définit un bloc à documenter ou à omettre conditionnellement.
-   , voir [\\a](http   *//www.doxygen.nl/manual/commands.html#cmda); affiche l\'argument en italique pour mettre l\'accent.
-    { parameter description }, voir [\\param](http   *//www.doxygen.nl/manual/commands.html#cmdparam); indique le paramètre d\'une fonction.
-   \return { description of the return value }, voir [\\return](http   *//www.doxygen.nl/manual/commands.html#cmdreturn); spécifie la valeur de retour.
-   \sa { references }, voir [\\sa](http   *//www.doxygen.nl/manual/commands.html#cmdsa); écrit \"See also\".
-   \note { text }, voir [\\note](http   *//www.doxygen.nl/manual/commands.html#cmdnote); ajoute un paragraphe à utiliser comme note.


</div>


</div>

## Support de Markdown 

Depuis Doxygen 1.8, la syntaxe de Markdown est reconnue dans les blocs de documentation. Markdown est un langage de formatage minimaliste inspiré du courrier électronique en texte brut qui, semblable à la syntaxe wiki, se veut simple et lisible sans nécessiter un code compliqué comme celui que l\'on trouve dans les commandes HTML, LaTeX ou Doxygen. Markdown a gagné en popularité avec les logiciels libres, en particulier sur les plates-formes en ligne telles que Github, car il permet de créer de la documentation sans utiliser de code compliqué. Consultez la section [Markdown support](http   *//www.doxygen.nl/manual/markdown.html) du manuel Doxygen pour en savoir plus. Visitez le [site Web de Markdown](https   *//daringfireball.net/projects/markdown/) pour en savoir plus sur l\'origine et la philosophie de Markdown.

Doxygen prend en charge un ensemble standard d\'instructions de Markdown, ainsi que certaines extensions telles que [Github Markdown](https   *//github.github.com/github-flavored-markdown/).


<div class="mw-collapsible mw-collapsed toccolours">

Quelques exemples de formatage Markdown sont présentés ci-après.


<div class="mw-collapsible-content">

Ce qui suit est standard Markdown. 
```python
Voici le texte pour un paragraphe.

Nous continuons avec plus de texte dans un autre paragraphe.

Ceci est un en-tête de niveau 1
========================

Ceci est un en-tête de niveau 2


# Ceci est un en-tête de niveau 1

### Ceci est un en-tête de niveau 3 #######

> Il s'agit d'une citation en bloc
> s'étendant sur plusieurs lignes

- Item 1

  Plus de texte pour cet item.

- Item 2
   * élément de liste imbriqué.
   * un autre élément imbriqué.
- Item 3

1. Premier item.
2. Deuxième item.

*astérisques simples   * accentuation*

 _underscores simples_

 **double astérisque   * forte accentuation**

 __underscores doubles__

Ceci est un paragraphe normal

    Ceci est un bloc de code

Nous continuons avec un paragraphe normal à nouveau.

Utilisation de la fonction printf(). En ligne code.

[Le lien texte](http   *//example.net/)

![Texte de légende](images//path/to/img.jpg)

<http   *//www.example.com>
```

Ce qui suit sont des extensions de Markdown.

    [TOC]

    Premier en-tête | Deuxième en-tête
     | 
    Cellule de contenu | Cellule de contenu
    Cellule de contenu | Cellule de contenu 

    <nowiki>~~~~~~~~~~~~~</nowiki>{.py}
    # A class
    class Dummy   *
        pass
    <nowiki>~~~~~~~~~~~~~</nowiki>

    <nowiki>~~~~~~~~~~~~~</nowiki>{.c}
    int func(int a, int b) { return a*b; }
    <nowiki>~~~~~~~~~~~~~</nowiki>
int func(int a, int b) { return a*b; }
    


</div>


</div>

## Analyse des blocs de documentation 

Le texte contenu dans un bloc de documentation spécial est analysé avant d'être écrit dans les fichiers de sortie HTML et LaTeX. Pendant l\'analyse, les étapes suivantes ont lieu   *

-   Le formatage de Markdown est remplacé par l\'HTML correspondant ou des commandes spéciales.
-   Les commandes spéciales à l\'intérieur de la documentation sont exécutées. Voir la section [Special Commands](http   *//www.doxygen.nl/manual/commands.html) dans le manuel pour une explication de chaque commande.
-   Si une ligne commence par un espace suivi d\'un ou de plusieurs astérisques (`*`) puis éventuellement plus d\'espaces, tous les espaces et astérisques sont supprimés.
-   Toutes les lignes vierges résultantes sont traitées comme des séparateurs de paragraphe.
-   Des liens sont automatiquement créés pour les mots correspondant aux classes ou fonctions documentées. Si le mot est précédé d\'un symbole de pourcentage `%`, ce symbole est supprimé et aucun lien n\'est créé pour le mot.
-   Les liens sont créés lorsque certains motifs se trouvent dans le texte. Voir la section [Automatic link generation](http   *//www.doxygen.nl/manual/autolink.html) dans le manuel pour plus d\'informations.
-   Les balises HTML figurant dans la documentation sont interprétées et converties en équivalents LaTeX pour la sortie LaTeX. Voir la section [HTML Commands](http   *//www.doxygen.nl/manual/htmlcmds.html) du manuel pour une explication de chaque balise HTML prise en charge.

## Doxygen avec du code Python 

Doxygen fonctionne mieux pour les langages de type statique tel que le C++. Cependant, il peut également créer une [documentation for Python files](http   *//www.doxygen.nl/manual/docblocks.html#pythonblocks).

Il existe deux manières d\'écrire des blocs de documentation pour Python   *

1.  A la Python, en utilisant \"docstrings\", c'est-à-dire un bloc de texte entouré de '''triple quotes''' immédiatement après la définition de la classe ou de la fonction.
2.  La manière Doxygen, en mettant les commentaires avant la définition de la classe ou de la fonction; dans ce cas, les caractères de double hachage `##` sont utilisés pour démarrer le bloc de documentation, puis un seul caractère de hachage peut être utilisé dans les lignes suivantes.

Remarque   *

-   La première option est préférable pour se conformer à [PEP8](https   *//www.python.org/dev/peps/pep-0008/#documentation-strings), [PEP257](https   *//www.python.org/dev/peps/pep-0257/) et la plupart des directives de style pour l\'écriture de Python (voir [1](https   *//realpython.com/python-pep8/), [2](https   *//realpython.com/documenting-python-code/)). Il est recommandé d\'utiliser ce style si vous souhaitez produire des sources documentées à l\'aide de [Sphinx](https   *//www.sphinx-doc.org/en/master/) qui est un outil très courant pour documenter le code Python. Si vous utilisez ce style, Doxygen pourra extraire les commentaires textuellement mais les commandes spéciales Doxygen commençant par `\` ou `@` ne fonctionneront pas.
-   La deuxième option n\'est pas dans le style Python traditionnel mais vous permet d\'utiliser les commandes spéciales de Doxygen telles que `\param` et `\var`.

### Premier style   * documentation de Python 

Dans l\'exemple suivant, une docstring est au début pour expliquer le contenu général de ce module (fichier). Ensuite, les docstrings apparaissent dans les définitions de méthode, de classe et de méthode. De cette façon, Doxygen extraira les commentaires et les présentera tels quels, sans modification.


```python
'''@package pyexample_a
Documentation for this module.
More details.
'''


def func()   *
    '''Documentation for a function.
    More details.
    '''
    pass


class PyClass   *
    '''Documentation for a class.
    More details.
    '''

    def __init__(self)   *
        '''The constructor.'''
        self._memVar = 0

    def PyMethod(self)   *
        '''Documentation for a method.'''
        pass
```

### Deuxième style   * bloc de documentation avant le code 

Dans l\'exemple suivant, les blocs de documentation commencent par un double signe de hachage `##`. On apparaît au début pour expliquer le contenu général de ce module (fichier). Ensuite, il y a des blocs avant les définitions de méthode, de classe et de méthode de classe, et un bloc après une variable de classe. De cette manière, Doxygen extraira la documentation, reconnaîtra les commandes spéciales `@package`, `@param` et `@var` et formatera le texte en conséquence. 
```python
## @package pyexample_b
#  Documentation for this module.
#
#  More details.


## Documentation for a function.
#
#  More details.
def func()   *
    pass


## Documentation for a class.
#
#  More details.
class PyClass   *

    ## The constructor.
    def __init__(self)   *
        self._memVar = 0

    ## Documentation for a method.
    #  @param self The object pointer.
    def PyMethod(self)   *
        pass

    ## A class variable.
    classVar = 0
    ## @var _memVar
    #  a member variable
```

## Compiler la documentation 

La compilation de la documentation se déroule de la même manière que [pour des sources C++](#Compiler_la_documentation.md). Si les deux fichiers Python, `pyexample_a.py` et `pyexample_b.py`, avec un style de commentaire distinct se trouvent dans le même répertoire, ils seront tous deux traités. 
```python
cd toplevel-source/
doxygen -g
doxygen Doxyfile
xdg-open ./html/index.html
```

La documentation doit afficher des informations similaires à celles qui suivent et créer des liens appropriés vers les modules et les classes individuels. 
```python
Class List
Here are the classes, structs, unions and interfaces with brief descriptions   *

N  pyexample_a
   C  PyClass

N  pyexample_b  Documentation for this module
   C  PyClass   Documentation for a class
```

### Convertir du style à la Python en style à la Doxygen 

Dans l\'exemple précédent, le fichier Python commenté dans un [style à la Doxygen](#Deuxième_style__bloc_de_documentation_avant_le_code.md) affiche des informations plus détaillées et un formatage pour ses classes, fonctions et variables. La raison en est que ce style permet à Doxygen d\'extraire les commandes spéciales commençant par `\` ou `@`, contrairement au [style à la Python](#Premier_style__documentation_de_Python.md). Par conséquent, il serait souhaitable de convertir le style Pythonic en style Doxygen avant de compiler la documentation. Ceci est possible avec un programme auxiliaire Python appelé [doxypypy](https   *//github.com/Feneric/doxypypy). Ce programme est inspiré d'un programme plus ancien appelé [doxypy](https   *//github.com/Feneric/doxypy), qui prendrait le '''docstrings''' de Pythonic et les convertir en blocs de commentaires Doxygen commençant par un double hachage `##`. Doxypypy va plus loin que cela en analysant les docstrings et en extrayant des éléments d'intérêt tels que des variables et des arguments, voire des doctests (exemple de code dans les docstrings).

Doxypypy peut être installé en utilisant `pip`, le programme d\'installation du paquet Python. 
```python
pip3 install --user doxypypy
```

Si la commande `pip` est utilisée sans l\'option `--user`, des privilèges de super-utilisateur (root) seront nécessaires pour installer le package, mais ce n\'est pas nécessaire dans la plupart des cas. Utilisez les autorisations root uniquement si vous êtes certain que le package ne se trouvera pas en conflit avec les packages fournis par votre distribution.

Si le package a été installé en tant qu\'utilisateur, il peut résider dans votre répertoire personnel, par exemple dans `$HOME/.local/bin`. Si ce répertoire ne se trouve pas dans `PATH` de votre système, le programme ne sera pas trouvé. Par conséquent, ajoutez le répertoire à la variable `PATH`, soit dans votre fichier `$HOME/.bashrc`, soit dans votre fichier `$HOME/.profile`. 
```python
export PATH="$HOME/.local/bin   *$PATH"
```

Vous pouvez également créer un lien symbolique vers le programme `doxypypy` en le plaçant dans un répertoire déjà inclus dans `PATH`. 
```python
mkdir -p $HOME/bin
ln -s $HOME/.local/bin/doxypypy $HOME/bin/doxypypy
```

Une fois que le programme `doxypypy` est installé et accessible depuis le terminal, un fichier Python contenant des docstrings Pythonic peut être reformaté en style Doxygen avec les instructions suivantes. Le programme sort le code reformaté sur la sortie standard, redirige donc cette sortie vers un nouveau fichier. 
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


def myfunction(arg1, arg2, kwarg='whatever.')   *
    '''
    Does nothing more than demonstrate syntax.

    This is an example of how a Pythonic human-readable docstring can
    get parsed by doxypypy and marked up with Doxygen commands as a
    regular input filter to Doxygen.

    Args   *
        arg1   *   A positional argument.
        arg2   *   Another positional argument.

    Kwargs   *
        kwarg   *  A keyword argument.

    Returns   *
        A string holding the result.

    Raises   *
        ZeroDivisionError, AssertionError, & ValueError.

    Examples   *
        >>> myfunction(2, 3)
        '5 - 0, whatever.'
        >>> myfunction(5, 0, 'oops.')
        Traceback (most recent call last)   *
            ...
        ZeroDivisionError   * integer division or modulo by zero
        >>> myfunction(4, 1, 'got it.')
        '5 - 4, got it.'
        >>> myfunction(23.5, 23, 'oh well.')
        Traceback (most recent call last)   *
            ...
        AssertionError
        >>> myfunction(5, 50, 'too big.')
        Traceback (most recent call last)   *
            ...
        ValueError
    '''
    assert isinstance(arg1, int)
    if arg2 > 23   *
        raise ValueError
    return '{0} - {1}, {2}'.format(arg1 + arg2, arg1 / arg2, kwarg)
```


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">


`pyexample_pythonic.py`


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
#        Traceback (most recent call last)   *
#            ...
#        ZeroDivisionError   * integer division or modulo by zero
#        >>> myfunction(4, 1, 'got it.')
#        '5 - 4, got it.'
#        >>> myfunction(23.5, 23, 'oh well.')
#        Traceback (most recent call last)   *
#            ...
#        AssertionError
#        >>> myfunction(5, 50, 'too big.')
#        Traceback (most recent call last)   *
#            ...
#        ValueError
# @endcode
#

def myfunction(arg1, arg2, kwarg='whatever.')   *
    assert isinstance(arg1, int)
    if arg2 > 23   *
        raise ValueError
    return '{0} - {1}, {2}'.format(arg1 + arg2, arg1 / arg2, kwarg)
```


</div>


</div>

Le fichier d\'origine contient un commentaire en haut '''@package pyexample_pythonic qui indique le module ou l\'espace de noms décrit par le fichier. Ce mot clé `@package` n\'est pas interprété lors de l\'utilisation de guillemets triples dans le bloc de commentaires.

Dans le nouveau fichier, le style de commentaire est modifié pour que la ligne devienne `##@package pyexample_pythonic` qui sera à présent interprétée par Doxygen. Cependant, pour être interprété correctement, l\'argument doit être modifié manuellement pour correspondre au nouveau nom du module (fichier). Après cela, la ligne doit être `##@package pyexample_doxygen`.


<div class="mw-collapsible mw-collapsed toccolours">


`pyexample_doxygen.py`

(le haut est édité manuellement, le reste reste le même)


<div class="mw-collapsible-content">


```python
##@package pyexample_doxygen
#Documentation for this module.
#More details go here.
#
```


</div>


</div>

Pour compiler, créez la configuration et exécutez `doxygen` dans le répertoire de niveau supérieur contenant les fichiers. 
```python
cd toplevel-source/
doxygen -g
doxygen Doxyfile
xdg-open ./html/index.html
```

La documentation doit afficher des informations similaires à celles qui suivent et créer des liens appropriés vers les modules et les classes individuels. 
```python
Namespace List
Here is a list of all documented namespaces with brief descriptions   *

 N  pyexample_doxygen   Documentation for this module
 N  pyexample_pythonic  
```

### Convertir le style commentaire à la volée 

Dans l\'exemple précédent, la conversion des blocs de documentation a été effectuée manuellement avec un seul fichier source. Idéalement, nous souhaitons que cette conversion se fasse automatiquement, à la volée, avec un nombre quelconque de fichiers Python. Pour ce faire, la configuration Doxygen doit être modifiée en conséquence.

Pour commencer, n'utilisez pas directement le programme `doxypypy`. Créez à la place le fichier de configuration avec `doxygen -g` puis éditez le `Doxyfile` créé et modifiez la balise suivante. 
```python
FILTER_PATTERNS        = *.py=doxypypy_filter
```

Cela signifie que les fichiers correspondant au modèle, tous les fichiers dont l\'extension se termine par `.py`, passent par le programme `doxypypy_filter`. Chaque fois que Doxygen rencontre un tel fichier dans l\'arborescence source, le nom du fichier est transmis en tant que premier argument à ce programme. 
```python
doxypypy_filter example.py
```

Le programme `doxypypy_filter` n\'existe pas par défaut. Il doit être créé en tant que script shell pour exécuter `doxypypy` avec les options appropriées et pour prendre un fichier comme premier argument. 
```python
#!/bin/sh
doxypypy -a -c "$1"
```

Après avoir enregistré ce script shell, assurez-vous qu\'il dispose des autorisations nécessaires et qu\'il se trouve dans un répertoire contenu dans votre `PATH` de votre système. 
```python
chmod a+x doxypypy_filter
mv doxypypy_filter $HOME/bin
```

Sur les systèmes Windows, un fichier batch peut être utilisé de la même manière. 
```python
doxypypy -a -c %1
```

Une fois cette configuration effectuée, vous pouvez exécuter la commande `doxygen Doxyfile` pour générer la documentation normalement. Tous les fichiers Python utilisant '''triple quotes''' Les styles de commentaire suivants ne permettent pas l\'analyse des docstrings par `doxypypy`. Ils doivent donc être évités.


<div class="mw-collapsible-content">


```python
'''@package Bad
'''

def first_f(one, two)   *

    "Bad comment 1"

    result = one + two
    result_m = one * two
    return result, result_m

def second_f(one, two)   *
    "Bad comment 2"
    result = one + two
    result_m = one * two
    return result, result_m

def third_f(one, two)   *
    'Bad comment 3'
    result = one + two
    result_m = one * two
    return result, result_m

def fourth_f(one, two)   *
    #Bad comment 4
    result = one + two
    result_m = one * two
    return result, result_m
```


</div>


</div>

Utilisez toujours des guillemets triples pour les docstrings et assurez-vous qu\'ils suivent immédiatement la déclaration de la classe ou de la fonction.

C\'est également une bonne idée de vérifier la qualité de votre code Python avec un outil tel que [flake8](http   *//flake8.pycqa.org/en/latest/) ([Gitlab](https   *//gitlab.com/pycqa/flake8)). Flake8 combine principalement trois outils, [Pyflakes](https   *//github.com/PyCQA/pyflakes), [Pycodestyle](https   *//github.com/PyCQA/pycodestyle) (anciennement pep8) et le [McCabe complexity checker (Vérificateur de complexité McCabe)](https   *//github.com/PyCQA/mccabe) afin d\'appliquer le style Pythonic approprié.


```python
pip install --user flake8
flake8 example.py
```

Pour vérifier tous les fichiers dans une arborescence source, utilisez `find`. 
```python
find toplevel-source/ -name '*.py' -exec flake8 {} '+'
```

Si le projet l\'exige, certaines vérifications de code jugées trop strictes peuvent être ignorées. Les codes d\'erreur peuvent être consultés dans la [documentation Pycodestyle](https   *//pycodestyle.readthedocs.io/en/latest/intro.html#error-codes). 
```python
find toplevel-source/ -name '*.py' -exec flake8 --ignore=E266,E402,E722,W503 --max-line-length=100 {} '+'
```

De la même façon, un programme qui vérifie principalement que les commentaires sont conformes à [PEP257](https   *//www.python.org/dev/peps/pep-0257/) est [Pydocstyle](https   *//github.com/PyCQA/pydocstyle). Les codes d\'erreur peuvent être consultés dans la [documentation Pydocstyle](http   *//www.pydocstyle.org/fr/4.0.0/error_codes.html). 
```python
pip install --user pydocstyle
pydocstyle example.py
```

Utilisez-le également avec `find` pour effectuer des vérifications de docstring sur tous les fichiers source. 
```python
find toplevel-source/ -name '*.py' -exec pydocstyle {} '+'
```

## Documentation source avec Sphinx 

[Sphinx](https   *//www.sphinx-doc.org/en/master/) est le système le plus populaire pour documenter le code source Python. Cependant, étant donné que les fonctions principales et les ateliers de FreeCAD sont écrits en C++, il a été jugé que Doxygen est un meilleur outil de documentation pour ce projet.

Bien que Sphinx puisse analyser nativement les docstrings Python, cela demande un peu plus de travail d\'analyser les sources C++. Le projet [Breathe](https   *//breathe.readthedocs.io/en/latest/) ([Github](https   *//github.com/michaeljones/breathe)) est une tentative de combler le fossé entre Sphinx et Doxygen, afin de Intégrez la documentation de code source Python et C++ dans le même système. Premièrement, Doxygen doit être configuré pour générer un fichier XML. la sortie XML est alors lue par Breathe et convertie en entrée appropriée pour Sphinx.

Consultez le [Guide de démarrage rapide](https   *//breathe.readthedocs.io/en/latest/quickstart.html) dans la documentation de Breathe pour en savoir plus sur ce processus.

Voir cette réponse dans [Stackoverflow](https   *//stackoverflow.com/a/35377654) pour d\'autres alternatives permettant de documenter le code C++ et Python ensemble dans le même projet.

## En relation 

-   [Documentation du code source](Source_documentation/fr.md)
-   [FreeCAD API website](https   *//www.freecadweb.org/api/)

[Category   *Developer_Documentation](Category_Developer_Documentation.md) [Category   *Developer](Category_Developer.md) [Category   *3rd Party](Category_3rd_Party.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Developer_Documentation](Category_Developer_Documentation.md) > [Developer](Category_Developer.md) > [3rd Party](Category_3rd Party.md) > Doxygen/fr
