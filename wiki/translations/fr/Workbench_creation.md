





{{TOCright}}

## Introduction

Cette page vous montrera comment ajouter un nouvel atelier à l\'interface FreeCAD. Les [ateliers](Workbenches/fr.md) sont des conteneurs pour les commandes FreeCAD. Ils peuvent être codés en Python, en C++ ou en un mélange des deux, ce qui a l'avantage d'allier la vitesse de C++ à la souplesse de Python. Dans tous les cas, cependant, votre atelier sera lancé par un ensemble de deux fichiers Python.

## La structure Atelier {#la_structure_atelier}

Vous avez besoin d\'un dossier, avec le nom de votre choix, placé dans le répertoire Mod de l\'utilisateur, avec un fichier `Init.py` et, éventuellement, un fichier `InitGui.py`. Le fichier Init est exécuté au démarrage de FreeCAD et le fichier `InitGui.py` est exécuté immédiatement après, mais uniquement lorsque FreeCAD démarre en mode GUI. C\'est tout ce dont FreeCAD a besoin pour trouver votre atelier au démarrage et l\'ajouter à son interface.

Le répertoire User Mod est un sous-répertoire du répertoire de données de l\'application utilisateur (vous pouvez trouver ce dernier en tapant `App.getUserAppDataDir()` dans la [console Python](Python_console/fr.md)):

-   Sous Linux, il s\'agit généralement de {{FileName|/home/<username>/.FreeCAD/Mod/}}.
-   Sous Windows, il s\'agit de {{FileName|%APPDATA%\FreeCAD\Macro\}}, qui est généralement {{FileName|C:\Users\<username>\Appdata\Roaming\FreeCAD\Mod\}}.
-   Sur macOS, il s\'agit généralement de {{FileName|/Users/<username>/Library/Preferences/FreeCAD/Mod/}}.

Le répertoire Mod devrait ressembler à ceci:


```python
/Mod/
 +-- MyWorkbench/
     +-- Init.py
     +-- InitGui.py
```

Dans ces fichiers, vous pouvez faire ce que vous voulez. Ils sont généralement utilisés comme ceci :

-   Dans le fichier Init.py, vous ajoutez simplement quelques éléments utilisés même lorsque FreeCAD fonctionne en mode console, par exemple les importateurs et les exportateurs de fichiers

-   Dans le fichier InitGui.py, vous définissez généralement un atelier, qui contient un nom, une icône et une série de commandes FreeCAD (voir ci-dessous). Cet fichier Python définit également les fonctions exécutées lors du chargement de FreeCAD (essayez d\'en faire le moins possible à ce niveau, afin de ne pas ralentir le démarrage). Un autre est exécuté lorsque l\'atelier est activé (c\'est là que vous ferez le plus du travail) et un troisième lorsque l\'atelier est désactivé (vous pouvez donc supprimer des éléments si nécessaire).

The structure and file content for a workbench described here is the classic way of creating a new workbench. One can use a slight variation in the structure of files when making a new Python workbench, that alternative way is best described as a \"namespaced workbench\", opening up the possibility to use pip to install the workbench. Both structures work, so it is more a question of preference when creating a new workbench. The style and structure for workbenches presented here are available in the global namespace of FreeCAD, whereas for the alternative style and structure the workbench resides in a dedicated namespace. For further readings on the topic see [Related](Workbench_creation#Related.md).

### La structure d\'atelier en C++ {#la_structure_datelier_en_c}

Si vous voulez coder votre atelier en python, vous n\'avez pas besoin de faire très attention, vous pouvez simplement placer vos autres fichiers python avec vos fichiers Init.py et InitGui.py. Toutefois, lorsque vous travaillez avec C++, vous devez faire preuve d\'une plus grande prudence et commencer par respecter une règle fondamentale de FreeCAD : la séparation de votre atelier entre une partie d\'application (pouvant s\'exécuter en mode console, sans aucun élément d\'interface graphique) et une partie d\'interface graphique qui ne sera chargé que lorsque FreeCAD s'exécutera avec son environnement graphique complet. Ainsi, lorsque vous construirez un atelier C++, vous élaborerez probablement deux modules, une application et une interface graphique. Ces deux modules doivent bien entendu être appelables depuis python. Tout module FreeCAD (App ou Gui) consiste à minima en un fichier init de module. Voici un fichier typique AppMyModuleGui.cpp : 
```python
extern "C" {
    void MyModuleGuiExport initMyModuleGui()  
    {
         if (!Gui::Application::Instance) {
            PyErr_SetString(PyExc_ImportError, "Cannot load Gui module in console application.");
            return;
        }
        try {
            // import other modules this one depends on
            Base::Interpreter().runString("import PartGui");
            // run some python code in the console
            Base::Interpreter().runString("print('welcome to my module!')");
        }
        catch(const Base::Exception& e) {
            PyErr_SetString(PyExc_ImportError, e.what());
            return;
        }
        (void) Py_InitModule("MyModuleGui", MyModuleGui_Import_methods);   /* mod name, table ptr */
        Base::Console().Log("Loading GUI of MyModule... done\n");    // initializes the FreeCAD commands (in another cpp file)
        CreateMyModuleCommands();    // initializes workbench and object definitions
        MyModuleGui::Workbench::init();
        MyModuleGui::ViewProviderSomeCustomObject::init();     // add resources and reloads the translators
        loadMyModuleResource();
    }
}
```

### Le fichier Init.py {#le_fichier_init.py}


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


<div class="mw-translate-fuzzy">

Les fonctions `FreeCAD.addImportType()` et `addEXportType()` vous permettent de fournir le nom et l\'extension d\'un type de fichier, ainsi qu\'un module Python responsable de son importation. Dans l\'exemple ci-dessus, un module `importOwn.py` gérera les fichiers `.own`. Voir [Extraits de codes](Code_snippets/fr.md) pour plus d\'exemples.


</div>

### Ateliers en Python {#ateliers_en_python}

Ceci est le fichier InitGui.py: 
```python
class MyWorkbench (Workbench):

    MenuText = "My Workbench"
    ToolTip = "A description of my workbench"
    Icon = """paste here the contents of a 16x16 xpm icon"""

    def Initialize(self):
        """This function is executed when FreeCAD starts"""
        import MyModuleA, MyModuleB # import here all the needed files that create your FreeCAD commands
        self.list = ["MyCommand1", "MyCommand2"] # A list of command names created in the line above
        self.appendToolbar("My Commands",self.list) # creates a new toolbar with your commands
        self.appendMenu("My New Menu",self.list) # creates a new menu
        self.appendMenu(["An existing Menu","My submenu"],self.list) # appends a submenu to an existing menu

    def Activated(self):
        """This function is executed when the workbench is activated"""
        return

    def Deactivated(self):
        """This function is executed when the workbench is deactivated"""
        return

    def ContextMenu(self, recipient):
        """This is executed whenever the user right-clicks on screen"""
        # "recipient" will be either "view" or "tree"
        self.appendContextMenu("My commands",self.list) # add commands to the context menu

    def GetClassName(self): 
        # This function is mandatory if this is a full Python workbench
        # This is not a template, the returned string should be exactly "Gui::PythonWorkbench"
        return "Gui::PythonWorkbench"
       
Gui.addWorkbench(MyWorkbench())
```


<div class="mw-translate-fuzzy">

En dehors de cela, vous pouvez faire ce que vous voulez : Vous pouvez insérer tout votre code d\'atelier dans le fichier InitGui.py si vous le souhaitez, mais il est généralement plus pratique de placer les différentes fonctions de votre atelier dans des fichiers séparés. Ainsi ces fichiers sont plus petits et plus faciles à lire. Ensuite, vous importerez ces fichiers dans votre fichier InitGui.py. Vous pouvez organiser ces fichiers comme bon vous semble, un bon exemple est en avoir un pour chaque commande FreeCAD que vous ajoutez.


</div>

#### Préférences


<div class="mw-translate-fuzzy">

Vous pouvez ajouter une page Préférences pour votre atelier Python. Les pages Préférences recherchent une icône de préférence avec un nom spécifique dans le système de ressources Qt. Si votre icône ne se trouve pas dans le système de ressources ou si son nom n\'est pas correct, votre icône n\'apparaîtra pas sur la page Préférences.


</div>

Ajouter votre icône d\'atelier :

-   l'icône des préférences doit être nommée \"preferences-\" + \"nom du module\" + \".svg\" (en minuscules)
-   créez un fichier qrc contenant les noms de tous les icônes
-   dans le répertoire \*.py principal, exécutez pyside-rcc -o myResources.py myqrc.qrc
-   dans InitGui.py, ajouter importer myResource(.py)
-   mettre à jour votre référentiel (git) avec myResources.py et myqrc.qrc

Vous devrez refaire les étapes si vous ajoutez/modifiez des icônes.


<div class="mw-translate-fuzzy">

\@kbwbe a créé un joli script pour compiler des ressources pour l\'atelier A2Plus. Voir ci-dessous.


</div>


<div class="mw-translate-fuzzy">

Ajouter votre/vos page(s) de préférence :

-   Vous devez compiler le plugin Qt Designer qui vous permet d'ajouter des paramètres de préférence avec [Qt Designer](Compile_on_Linux/Unix/fr#Plugin_Qt_designer.md)
-   Créer un widget vide dans Qt Designer (sans boutons ni quoi que ce soit)
-   Concevez votre page de préférences, de nombreux paramètres qui doivent être enregistrés (préférences) doivent être l'un des widgets Gui::Pref\* ajoutés par le plug-in)
-   Dans ces cas-là, veillez à renseigner PrefName (le nom de votre valeur de préférence) et PrefPath (ex: Mod/MyWorkbenchName), qui sauvegardera votre valeur sous BaseApp/Preferences/Mod/MyWorkbenchName
-   Enregistrez le fichier d\'interface utilisateur dans votre atelier, assurez-vous qu\'il est géré par cmake.
-   Dans votre atelier, par exemple dans le fichier InitGui, dans la méthode Initialize (mais tout autre endroit fonctionne également), ajoutez : FreeCADGui.addPreferencePage (\"/path/to/myUiFile.ui\", \"MyGroup\"), \"MyGroup\" étant l\'un des groupes de préférences de la gauche. FreeCAD recherchera automatiquement un fichier \"preferences-mygroup.svg\" dans ses emplacements connus (que vous pouvez étendre avec FreeCADGui.addIconPath())
-   Assurez-vous que la méthode addPreferencePage() n'est appelée qu'une fois, sinon votre page de préférence sera ajoutée plusieurs fois


</div>

### Ateliers en C++ {#ateliers_en_c}


<div class="mw-translate-fuzzy">

Si vous voulez coder votre atelier en C++, vous souhaiterez probablement coder aussi sa définition elle-même en C++ (bien que cela ne soit pas nécessaire : vous pouvez également coder uniquement les outils en C++, et laisser la définition de de l\'atelier en Python). Dans ce cas, le fichier InitGui.py devient très simple : il peut contenir une seule ligne :


</div>


```pythonimport MyModuleGui```


<div class="mw-translate-fuzzy">

où MyModule est votre atelier C++ complet, incluant les commandes et la définition de l\'atelier.


</div>


<div class="mw-translate-fuzzy">

Le codage des ateliers C++ fonctionne de manière assez similaire. Il s\'agit d\'un fichier Workbench.cpp typique à inclure dans la partie interface graphique de votre module :


</div>


```python
namespace MyModuleGui {
    class MyModuleGuiExport Workbench : public Gui::StdWorkbench
    {
        TYPESYSTEM_HEADER();

    public:
        Workbench();
        virtual ~Workbench();

        virtual void activated();
        virtual void deactivated();

    protected:
        Gui::ToolBarItem* setupToolBars() const;
        Gui::MenuItem*    setupMenuBar() const;
    };
}
```

#### Préférences {#préférences_1}


<div class="mw-translate-fuzzy">

Vous pouvez également ajouter une page de préférences pour les ateliers C++. Les étapes sont similaires à celles de Python.


</div>

## Commandes FreeCAD {#commandes_freecad}


<div class="mw-translate-fuzzy">

Les commandes FreeCAD constituent le bloc de construction de base de l\'interface FreeCAD. Ils peuvent apparaître sous la forme d\'un bouton dans les barres d\'outils et d\'une entrée de menu dans les menus. Mais c\'est la même commande. Une commande est une simple classe Python, qui doit contenir un couple attributs et fonctions prédéfinis, définissant le nom de la commande, son icône et l\'action à effectuer lorsque la commande est activée.


</div>

### Définition des commandes Python {#définition_des_commandes_python}


```python
class My_Command_Class():
    """My new command"""

    def GetResources(self):
        return {'Pixmap'  : 'My_Command_Icon', # the name of a svg file available in the resources
                'Accel' : "Shift+S", # a default shortcut (optional)
                'MenuText': "My New Command",
                'ToolTip' : "What my new command does"}

    def Activated(self):
        """Do something here"""
        return

    def IsActive(self):
        """Here you can define if the command must be active or not (greyed) if certain conditions
        are met or not. This function is optional."""
        return True

FreeCADGui.addCommand('My_Command',My_Command_Class())
```

### Définition des commandes en C++ {#définition_des_commandes_en_c}

De la même manière, vous pouvez coder vos commandes en C++. Vous avez généralement un fichier Commands.cpp dans votre module d\'interface graphique. Ceci est un fichier Commands.cpp typique : 
```pythonDEF_STD_CMD_A(CmdMyCommand);

CmdMyCommand::CmdMyCommand()
  :Command("My_Command")
{
  sAppModule    = "MyModule";
  sGroup        = QT_TR_NOOP("MyModule");
  sMenuText     = QT_TR_NOOP("Runs my command...");
  sToolTipText  = QT_TR_NOOP("Describes what my command does");
  sWhatsThis    = QT_TR_NOOP("Describes what my command does");
  sStatusTip    = QT_TR_NOOP("Describes what my command does");
  sPixmap       = "some_svg_icon_from_my_resource";
}

void CmdMyCommand::activated(int iMsg)
{
    openCommand("My Command");
    doCommand(Doc,"print('Hello, world!')");
    commitCommand();
    updateActive();
}

bool CmdMyCommand::isActive(void)
{
  if( getActiveGuiDocument() )
    return true;
  else
    return false;
}

void CreateMyModuleCommands(void)
{
    Gui::CommandManager &rcCmdMgr = Gui::Application::Instance->commandManager();
    rcCmdMgr.addCommand(new CmdMyCommand());
}
```

## \"Compiler\" votre fichier ressources {#compiler_votre_fichier_ressources}

compileA2pResources.py depuis l\'atelier A2Plus :


```python#!/usr/bin/env python
# -*- coding: utf-8 -*-
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
if os.path.exists(qrc_filename):
    os.remove(qrc_filename)

qrc = '''<RCC>
\t<qresource prefix="/">'''
for fn in glob.glob('./icons/*.svg'):
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

## En relation {#en_relation}


<div class="mw-translate-fuzzy">

-   [Traduction et ateliers externes](Translating_an_external_workbench/fr.md)


</div>





{{Powerdocnavi

}} 

[Category:Developer Documentation{{\#translation:}}](Category:Developer_Documentation.md) [Category:Python Code{{\#translation:}}](Category:Python_Code.md)
