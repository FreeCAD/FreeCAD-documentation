# Workbench creation/fr
{{TOCright}}

## Introduction

Cette page vous montrera comment ajouter un nouvel atelier à l\'interface de FreeCAD. Les [ateliers](Workbenches/fr.md) sont des conteneurs pour les commandes de FreeCAD. Ils peuvent être codés en Python, en C++, ou dans un mélange des deux, ce qui a l\'avantage d\'allier la vitesse du C++ à la flexibilité du Python. Dans tous les cas, cependant, votre atelier sera lancé par un ensemble de deux fichiers Python. Il peut s\'agir d\'ateliers \"internes\", inclus dans la distribution de FreeCAD, ou d\'ateliers \"externes\", distribués via le [Gestionnaire d\'Addon](Std_AddonMgr/fr.md) ou installés manuellement par téléchargement depuis un dépôt en ligne. Les ateliers internes peuvent être codés en C++, Python, ou une combinaison des deux, alors que les ateliers externes doivent être en Python uniquement.

## La structure Atelier 

Vous avez besoin d\'un dossier, avec le nom de votre choix, placé dans le répertoire Mod de l\'utilisateur, avec un fichier `Init.py` et, éventuellement, un fichier `InitGui.py`. Le fichier Init est exécuté au démarrage de FreeCAD et le fichier `InitGui.py` est exécuté immédiatement après, mais uniquement lorsque FreeCAD démarre en mode GUI. C\'est tout ce dont FreeCAD a besoin pour trouver votre atelier au démarrage et l\'ajouter à son interface.

Le répertoire User Mod est un sous-répertoire du répertoire de données de l\'application utilisateur (vous pouvez trouver ce dernier en tapant `App.getUserAppDataDir()` dans la [console Python](Python_console/fr.md))   *

-   Sous Linux, il s\'agit généralement de **/home/<username>/.FreeCAD/Mod/**.
-   Sous Windows, il s\'agit de **%APPDATA%\FreeCAD\Macro\**, qui est généralement **C   *Users\<username>\Appdata\Roaming\FreeCAD\Mod\**.
-   Sur macOS, il s\'agit généralement de **/Users/<username>/Library/Application Support/FreeCAD/Mod/**.

Le répertoire Mod devrait ressembler à ceci   *


```python
/Mod/
 +-- MyWorkbench/
     +-- Init.py
     +-- InitGui.py
```

Dans ces fichiers, vous pouvez faire ce que vous voulez. Ils sont généralement utilisés comme ceci    *

-   Dans le fichier Init.py, vous ajoutez simplement quelques éléments utilisés même lorsque FreeCAD fonctionne en mode console, par exemple les importateurs et les exportateurs de fichiers

-   Dans le fichier InitGui.py, vous définissez généralement un atelier, qui contient un nom, une icône et une série de commandes FreeCAD (voir ci-dessous). Cet fichier Python définit également les fonctions exécutées lors du chargement de FreeCAD (essayez d\'en faire le moins possible à ce niveau, afin de ne pas ralentir le démarrage). Un autre est exécuté lorsque l\'atelier est activé (c\'est là que vous ferez le plus du travail) et un troisième lorsque l\'atelier est désactivé (vous pouvez donc supprimer des éléments si nécessaire).

La structure et le contenu des fichiers d\'un atelier décrits ici constituent la manière classique de créer un nouvel atelier. Il est possible d\'utiliser une légère variation dans la structure des fichiers lors de la création d\'un nouvel atelier Python. Cette méthode alternative est mieux décrite comme un \"atelier à espacement de noms\", ouvrant la possibilité d\'utiliser pip pour installer l\'atelier. Les deux structures fonctionnent, il s\'agit donc plutôt d\'une question de préférence lors de la création d\'un nouvel atelier. Le style et la structure pour les ateliers présentés ici sont disponibles dans l\'espace de noms global de FreeCAD, alors que pour le style et la structure alternatifs, l\'atelier réside dans un espace de noms dédié. Pour plus d\'informations sur le sujet, voir [En relation](Workbench_creation/fr#En_relation.md).

### La structure d\'atelier en C++ 

Si vous allez coder votre atelier en Python, vous n\'avez pas besoin de prendre de précautions particulières, et pouvez simplement placer vos autres fichiers Python avec vos fichiers Init.py et InitGui.py. Lorsque vous travaillez en C++, cependant, vous devez faire plus attention, et commencer par respecter une règle fondamentale de FreeCAD    * La séparation de votre environnement de travail entre une partie App (qui peut fonctionner en mode console, sans aucun élément GUI), et une partie Gui, qui ne sera chargée que lorsque FreeCAD fonctionnera avec son environnement GUI complet. Ainsi, lors du développement d\'un atelier en C++, vous allez très probablement créer deux modules, un App et un Gui. Ces deux modules doivent bien sûr être appelables depuis Python. Tout module FreeCAD (App ou Gui) consiste, au minimum, en un fichier init de module. Voici un fichier typique AppMyModuleGui.cpp    *


```python
extern "C" {
    void MyModuleGuiExport initMyModuleGui()  
    {
         if (!Gui   *   *Application   *   *Instance) {
            PyErr_SetString(PyExc_ImportError, "Cannot load Gui module in console application.");
            return;
        }
        try {
            // import other modules this one depends on
            Base   *   *Interpreter().runString("import PartGui");
            // run some python code in the console
            Base   *   *Interpreter().runString("print('welcome to my module!')");
        }
        catch(const Base   *   *Exception& e) {
            PyErr_SetString(PyExc_ImportError, e.what());
            return;
        }
        (void) Py_InitModule("MyModuleGui", MyModuleGui_Import_methods);   /* mod name, table ptr */
        Base   *   *Console().Log("Loading GUI of MyModule... done\n");    // initializes the FreeCAD commands (in another cpp file)
        CreateMyModuleCommands();    // initializes workbench and object definitions
        MyModuleGui   *   *Workbench   *   *init();
        MyModuleGui   *   *ViewProviderSomeCustomObject   *   *init();     // add resources and reloads the translators
        loadMyModuleResource();
    }
}
```

### Le fichier Init.py 


{{code|code=
"""FreeCAD init script of XXX module"""

# ***************************************************************************
# *   Copyright (c) 2015 John Doe john@doe.com                              *   
# *                                                                         *
# *   This file is part of the FreeCAD CAx development system.              *
# *                                                                         *
# *   This program is free software; you can redistribute it and/or modify  *
# *   it under the terms of the GNU Lesser General Public License (LGPL)    *
# *   as published by the Free Software Foundation; either version 2 of     *
# *   the License, or (at your option) any later version.                   *
# *   for detail see the LICENCE text file.                                 *
# *                                                                         *
# *   FreeCAD is distributed in the hope that it will be useful,            *
# *   but WITHOUT ANY WARRANTY; without even the implied warranty of        *
# *   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         *
# *   GNU Lesser General Public License for more details.                   *
# *                                                                         *
# *   You should have received a copy of the GNU Library General Public     *
# *   License along with FreeCAD; if not, write to the Free Software        *
# *   Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  *
# *   USA                                                                   *
# *                                                                         *
# ***************************************************************************/

FreeCAD.addImportType("My own format (*.own)", "importOwn")
FreeCAD.addExportType("My own format (*.own)", "importOwn")
print("I am executing some stuff here when FreeCAD starts!")
}}

Vous pouvez choisir la licence de votre choix pour votre atelier, mais sachez que si vous souhaitez que votre atelier soit intégré et distribué avec le code source de FreeCAD à un moment donné, il doit être LGPL2+, comme dans l\'exemple ci-dessus. Voir [Licence](Licence/fr.md).

Les fonctions `FreeCAD.addImportType()` et `addEXportType()` vous permettent de fournir le nom et l\'extension d\'un type de fichier, ainsi qu\'un module Python responsable de son importation. Dans l\'exemple ci-dessus, un module `importOwn.py` gérera les fichiers `.own`. Voir [Extraits de codes](Code_snippets/fr.md) pour plus d\'exemples.

### Ateliers Python 

Ceci est le fichier InitGui.py   *


```python
class MyWorkbench (Workbench)   *

    MenuText = "My Workbench"
    ToolTip = "A description of my workbench"
    Icon = """paste here the contents of a 16x16 xpm icon"""

    def Initialize(self)   *
        """This function is executed when the workbench is first activated.
        It is executed once in a FreeCAD session followed by the Activated function.
        """
        import MyModuleA, MyModuleB # import here all the needed files that create your FreeCAD commands
        self.list = ["MyCommand1", "MyCommand2"] # A list of command names created in the line above
        self.appendToolbar("My Commands",self.list) # creates a new toolbar with your commands
        self.appendMenu("My New Menu",self.list) # creates a new menu
        self.appendMenu(["An existing Menu","My submenu"],self.list) # appends a submenu to an existing menu

    def Activated(self)   *
        """This function is executed whenever the workbench is activated"""
        return

    def Deactivated(self)   *
        """This function is executed whenever the workbench is deactivated"""
        return

    def ContextMenu(self, recipient)   *
        """This function is executed whenever the user right-clicks on screen"""
        # "recipient" will be either "view" or "tree"
        self.appendContextMenu("My commands",self.list) # add commands to the context menu

    def GetClassName(self)   * 
        # This function is mandatory if this is a full Python workbench
        # This is not a template, the returned string should be exactly "Gui   *   *PythonWorkbench"
        return "Gui   *   *PythonWorkbench"
       
Gui.addWorkbench(MyWorkbench())
```

En dehors de cela, vous pouvez faire ce que vous voulez    * vous pouvez insérer tout votre code d\'atelier dans le fichier InitGui.py si vous le souhaitez, mais il est généralement plus pratique de placer les différentes fonctions de votre atelier dans des fichiers séparés. Ainsi ces fichiers sont plus petits et plus faciles à lire. Ensuite, vous importerez ces fichiers dans votre fichier InitGui.py. Vous pouvez organiser ces fichiers comme bon vous semble, un bon exemple est en avoir un pour chaque commande FreeCAD que vous ajoutez.

#### Préférences

Vous pouvez ajouter une page Préférences pour votre atelier Python. Les pages Préférences recherchent une icône de préférence avec un nom spécifique dans le système de ressources Qt. Si votre icône ne se trouve pas dans le système de ressources ou si son nom n\'est pas correct, votre icône n\'apparaîtra pas sur la page Préférences.

Ajouter votre icône d\'atelier    *

-   l'icône des préférences doit être nommée \"preferences-\" + \"nom du module\" + \".svg\" (en minuscules)
-   créez un fichier qrc contenant les noms de tous les icônes
-   dans le répertoire \*.py principal, exécutez pyside-rcc -o myResources.py myqrc.qrc
-   dans InitGui.py, ajouter importer myResource(.py)
-   mettre à jour votre référentiel (git) avec myResources.py et myqrc.qrc

Vous devrez refaire les étapes si vous ajoutez/modifiez des icônes.

\@kbwbe a créé un joli script pour compiler des ressources pour l\'atelier A2Plus. Voir ci-dessous.

Ajouter votre/vos page(s) de préférence    *

-   Vous devez compiler le plugin Qt Designer qui vous permet d'ajouter des paramètres de préférence avec [Qt Designer](Compile_on_Linux/fr#Plugin_Qt_designer.md)
-   Créer un widget vide dans Qt Designer (sans boutons ni quoi que ce soit)
-   Concevez votre page de préférences, de nombreux paramètres qui doivent être enregistrés (préférences) doivent être l'un des widgets Gui   *   *Pref\* ajoutés par le plug-in)
-   Dans ces cas-là, veillez à renseigner PrefName (le nom de votre valeur de préférence) et PrefPath (ex   * Mod/MyWorkbenchName), qui sauvegardera votre valeur sous BaseApp/Preferences/Mod/MyWorkbenchName
-   Enregistrez le fichier d\'interface utilisateur dans votre atelier, assurez-vous qu\'il est géré par cmake.
-   Dans votre atelier, par exemple dans le fichier InitGui, dans la méthode Initialize (mais tout autre endroit fonctionne également), ajoutez    * FreeCADGui.addPreferencePage (\"/path/to/myUiFile.ui\", \"MyGroup\"), \"MyGroup\" étant l\'un des groupes de préférences de la gauche. FreeCAD recherchera automatiquement un fichier \"preferences-mygroup.svg\" dans ses emplacements connus (que vous pouvez étendre avec FreeCADGui.addIconPath())
-   Assurez-vous que la méthode addPreferencePage() n'est appelée qu'une fois, sinon votre page de préférence sera ajoutée plusieurs fois

#### Distribution

Pour distribuer votre atelier Python, vous pouvez soit simplement héberger les fichiers dans un endroit quelconque et demander à vos utilisateurs de les télécharger et de les placer manuellement dans leur répertoire Mod, ou vous pouvez les héberger dans un dépôt git en ligne (GitHub, GitLab, Framagit et Debian Salsa sont actuellement des emplacements supportés) et les configurer pour que le [Gestionnaire d\'Addon](Std_AddonMgr/fr.md) les installe. Les instructions pour l\'inclusion dans la liste officielle des modules complémentaires de FreeCAD peuvent être trouvées sur le [Dépôt GitHub des Addons de FreeCAD](https   *//github.com/FreeCAD/FreeCAD-addons/blob/master/README.md). Pour utiliser le gestionnaire d\'addons, un [fichier de métadonnées package.xml](Package_Metadata/fr.md) doit être inclus, qui indique au gestionnaire d\'addons comment trouver l\'icône de votre atelier, et permet d\'afficher une description, un numéro de version, etc. Il peut également être utilisé pour spécifier d\'autres ateliers ou paquets Python dont votre atelier dépend, qui le bloquent ou qu\'il est destiné à remplacer.

En outre, vous pouvez inclure un fichier de métadonnées distinct décrivant vos dépendances Python. Il peut s\'agir soit d\'un fichier appelé metadata.txt décrivant les dépendances externes de votre atelier (soit d\'autres addons, ateliers ou modules Python), soit d\'un fichier [requirements.txt](https   *//pip.pypa.io/en/latest/reference/requirements-file-format/) décrivant vos dépendances Python. Notez que si vous utilisez un fichier requirements.txt, seuls les noms des paquets spécifiés sont utilisés pour la résolution des dépendances    * les options de la commande pip, les options include et les informations de version ne sont pas prises en charge par le gestionnaire d\'addons. Les utilisateurs peuvent exécuter manuellement le fichier d\'exigences en utilisant pip si ces fonctionnalités sont requises.

Le format du fichier metadata.txt est du texte brut, avec trois lignes optionnelles    *


```python
workbenches=
pylibs=
optionalpylibs=
```

Chaque ligne doit consister en une liste d\'éléments, séparés par des virgules, dont dépend votre atelier. Les ateliers peuvent être soit un atelier FreeCAD interne, par exemple \"FEM\", soit un addon externe, par exemple \"Curves\". Les bibliothèques Python requises et optionnelles doivent être spécifiées avec leur nom Python canonique, tel que vous l\'utiliseriez avec `pip install`. Par exemple    *


```python
workbenches=FEM,Curves
pylibs=ezdxf
optionalpylibs=metadata,git
```

Vous pouvez également inclure un script qui est exécuté lorsque votre paquet est désinstallé. Il s\'agit d\'un fichier appelé \"uninstall.py\" situé au niveau supérieur de votre module complémentaire. Il est exécuté lorsqu\'un utilisateur désinstalle votre module complémentaire à l\'aide du gestionnaire de modules complémentaires. Utilisez-le pour nettoyer tout ce que votre addon a pu faire sur le système de l\'utilisateur et qui ne devrait pas persister après la disparition de l\'addon (par exemple, suppression des fichiers de cache, etc.).

To ensure that your addon is being read correctly by the Addon Manager, you can enable a \"developer mode\" in which the Addon Manager examines all available addons and ensures their metadata contains the required elements. To enable this mode use the [Parameter Editor](Parameter_Editor.md) to create a boolean variable called \"developerMode\" in the \"Addons\" parameter group, and set this variable to True   * **Tools → Edit parameters... → BaseApp → Preferences → Addons → developerMode**.

### Ateliers en C++ 

Si vous voulez coder votre atelier en C++, vous souhaiterez probablement coder aussi sa définition elle-même en C++ (bien que cela ne soit pas nécessaire    * vous pouvez également coder uniquement les outils en C++, et laisser la définition de de l\'atelier en Python). Dans ce cas, le fichier InitGui.py devient très simple    * il peut contenir une seule ligne    *


```pythonimport MyModuleGui```

où MyModule est votre atelier C++ complet, incluant les commandes et la définition de l\'atelier.

Le codage des ateliers C++ fonctionne de manière assez similaire. Il s\'agit d\'un fichier Workbench.cpp typique à inclure dans la partie interface graphique de votre module    *


```python
namespace MyModuleGui {
    class MyModuleGuiExport Workbench    * public Gui   *   *StdWorkbench
    {
        TYPESYSTEM_HEADER();

    public   *
        Workbench();
        virtual ~Workbench();

        virtual void activated();
        virtual void deactivated();

    protected   *
        Gui   *   *ToolBarItem* setupToolBars() const;
        Gui   *   *MenuItem*    setupMenuBar() const;
    };
}
```

#### Préférences 

Vous pouvez également ajouter une page de préférences pour les ateliers C++. Les étapes sont similaires à celles de Python.

## Commandes FreeCAD 

Les commandes FreeCAD constituent le bloc de construction de base de l\'interface FreeCAD. Ils peuvent apparaître sous la forme d\'un bouton dans les barres d\'outils et d\'une entrée de menu dans les menus. Mais c\'est la même commande. Une commande est une simple classe Python, qui doit contenir un couple attributs et fonctions prédéfinis, définissant le nom de la commande, son icône et l\'action à effectuer lorsque la commande est activée.

### Définition des commandes Python 


```python
class My_Command_Class()   *
    """My new command"""

    def GetResources(self)   *
        return {"Pixmap"     * "My_Command_Icon", # the name of a svg file available in the resources
                "Accel"      * "Shift+S", # a default shortcut (optional)
                "MenuText"   * "My New Command",
                "ToolTip"    * "What my new command does"}

    def Activated(self)   *
        """Do something here"""
        return

    def IsActive(self)   *
        """Here you can define if the command must be active or not (greyed) if certain conditions
        are met or not. This function is optional."""
        return True

FreeCADGui.addCommand("My_Command", My_Command_Class())
```

### Définition des commandes en C++ 

De la même manière, vous pouvez coder vos commandes en C++. Vous avez généralement un fichier Commands.cpp dans votre module d\'interface graphique. Ceci est un fichier Commands.cpp typique    *


```pythonDEF_STD_CMD_A(CmdMyCommand);

CmdMyCommand   *   *CmdMyCommand()
     *Command("My_Command")
{
  sAppModule    = "MyModule";
  sGroup        = QT_TR_NOOP("MyModule");
  sMenuText     = QT_TR_NOOP("Runs my command...");
  sToolTipText  = QT_TR_NOOP("Describes what my command does");
  sWhatsThis    = QT_TR_NOOP("Describes what my command does");
  sStatusTip    = QT_TR_NOOP("Describes what my command does");
  sPixmap       = "some_svg_icon_from_my_resource";
}

void CmdMyCommand   *   *activated(int iMsg)
{
    openCommand("My Command");
    doCommand(Doc,"print('Hello, world!')");
    commitCommand();
    updateActive();
}

bool CmdMyCommand   *   *isActive(void)
{
  if( getActiveGuiDocument() )
    return true;
  else
    return false;
}

void CreateMyModuleCommands(void)
{
    Gui   *   *CommandManager &rcCmdMgr = Gui   *   *Application   *   *Instance->commandManager();
    rcCmdMgr.addCommand(new CmdMyCommand());
}
```

## \"Compiler\" votre fichier ressources 

compileA2pResources.py depuis l\'atelier A2Plus    *


```python#!/usr/bin/env python
# -*- coding   * utf-8 -*-
#***************************************************************************
#*                                                                         *
#*   Copyright (c) 2019 kbwbe                                              *
#*                                                                         *
#*   Portions of code based on hamish's assembly 2                         *
#*                                                                         *
#*   This program is free software; you can redistribute it and/or modify  *
#*   it under the terms of the GNU Lesser General Public License (LGPL)    *
#*   as published by the Free Software Foundation; either version 2 of     *
#*   the License, or (at your option) any later version.                   *
#*   for detail see the LICENCE text file.                                 *
#*                                                                         *
#*   This program is distributed in the hope that it will be useful,       *
#*   but WITHOUT ANY WARRANTY; without even the implied warranty of        *
#*   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         *
#*   GNU Library General Public License for more details.                  *
#*                                                                         *
#*   You should have received a copy of the GNU Library General Public     *
#*   License along with this program; if not, write to the Free Software   *
#*   Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  *
#*   USA                                                                   *
#*                                                                         *
#***************************************************************************

# This script compiles the A2plus icons for py2 and py3
# For Linux only
# Start this file in A2plus main directory
# Make sure pyside-rcc is installed

import os, glob

qrc_filename = 'temp.qrc'
if os.path.exists(qrc_filename)   *
    os.remove(qrc_filename)

qrc = '''<RCC>
\t<qresource prefix="/">'''
for fn in glob.glob('./icons/*.svg')   *
    qrc = qrc + '\n\t\t<file>%s</file>' % fn
qrc = qrc + '''\n\t</qresource>
</RCC>'''

print(qrc)

f = open(qrc_filename,'w')
f.write(qrc)
f.close()

os.system(
    'pyside-rcc -o a2p_Resources2.py {}'.format(qrc_filename))
os.system(
    'pyside-rcc -py3 -o a2p_Resources3.py {}'.format(qrc_filename))

os.remove(qrc_filename)
```

## En relation 

-   [Traduction et ateliers externes](Translating_an_external_workbench/fr.md)
-   [Discussion sur le forum - Namespaced Workbenches](https   *//forum.freecadweb.org/viewtopic.php?t=47460)
-   [freecad.workbench\_starterkit](https   *//github.com/FreeCAD/freecad.workbench_starterkit)







[Category   *Developer Documentation](Category_Developer_Documentation.md) [Category   *Python Code](Category_Python_Code.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Python Code](Category_Python Code.md) > Workbench creation/fr
