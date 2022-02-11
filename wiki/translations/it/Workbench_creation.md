# Workbench creation/it
{{TOCright}}

## Introduction


<div class="mw-translate-fuzzy">

Questa pagina spiega come aggiungere un nuovo ambiente di lavoro (Workbench) all\'interfaccia di FreeCAD. Gli [Workbenches](Workbenches/it.md) sono dei contenitori per i comandi di FreeCAD. Essi possono essere codificati in python, in C++, o in una combinazione di entrambi, con il vantaggio di unire la velocità di C++ alla flessibilità di python. In tutti i casi, il vostro ambiente di lavoro sarà comunque lanciato da un insieme di due file python.


</div>

## La struttura del workbench 


<div class="mw-translate-fuzzy">

Fondamentalmente è semplice: serve una cartella, con un nome a piacere, inserita nella directory Mod, contenente un file *Init.py* e, facoltativamente, un file *InitGui.py*. Il file Init viene sempre eseguito all\'avvio FreeCAD, e il file InitGui.py viene eseguito immediatamente dopo, ma solo quando FreeCAD si avvia in modalità GUI, non in modalità console. Questo è tutto ciò che serve a FreeCAD per trovare il vostro ambiente di lavoro in fase di avvio e aggiungerlo alla sua interfaccia.


</div>

The user Mod directory is a sub-directory of the user application data directory (you can find the latter by typing `App.getUserAppDataDir()` in the [Python console](Python_console.md)):

-   On Linux it is usually {{FileName|/home/<username>/.FreeCAD/Mod/}}.
-   On Windows it is {{FileName|%APPDATA%\FreeCAD\Macro\}}, which is usually {{FileName|C:\Users\<username>\Appdata\Roaming\FreeCAD\Mod\}}.
-   On macOS it is usually {{FileName|/Users/<username>/Library/Preferences/FreeCAD/Mod/}}.

The Mod directory should look like this:


```python
/Mod/
 +-- MyWorkbench/
     +-- Init.py
     +-- InitGui.py
```

All\'interno questi file si può fare quello che si vuole. Di solito vengono utilizzati in questo modo:

-   Nel file Init.py si inseriscono solo alcune cose, usate anche quando FreeCAD funziona in modalità console, per esempio, gli importatori e gli esportatori di file


<div class="mw-translate-fuzzy">

-   Nel file InitGui.py si definisce un ambiente di lavoro che contiene un nome, un\'icona e una serie di comandi di FreeCAD (vedi sotto). Nell\'ambiente si definiscono inoltre le funzioni che vengono eseguite quando si carica FreeCAD (in questa parte si cerca di fare meno lavoro possibile, in modo da non rallentare l\'avvio), quelle che vengono eseguite quando si attiva l\'ambiente (la parte dove si esegue la maggior parte del lavoro), e come terze quelle che servono quando l\'ambiente viene disattivato (in modo da poter rimuovere le cose, se è necessario).


</div>

The structure and file content for a workbench described here is the classic way of creating a new workbench. One can use a slight variation in the structure of files when making a new Python workbench, that alternative way is best described as a \"namespaced workbench\", opening up the possibility to use pip to install the workbench. Both structures work, so it is more a question of preference when creating a new workbench. The style and structure for workbenches presented here are available in the global namespace of FreeCAD, whereas for the alternative style and structure the workbench resides in a dedicated namespace. For further readings on the topic see [Related](Workbench_creation#Related.md).

### Struttura del workbench in C++ 

Per codificare l\'ambiente in python, non è necessario usare particolari attenzioni, è possibile inserire semplicemente gli altri file python insieme ai file Init.py e InitGui.py. Invece, quando si lavora in C++ si deve avere maggiori attenzioni, e iniziare rispettando una regola fondamentale di FreeCAD: separare la parte App dell\'ambiente, quella che può essere eseguita in modalità console, senza alcun elemento GUI, dalla parte Gui, che è quella che viene caricata solo quando FreeCAD funziona completo del suo ambiente GUI. Quindi, quando si crea un ambiente in C++, in realtà si creano probabilmente due moduli, un App e un Gui. Questi due moduli devono naturalmente essere richiamabili in python. Ogni modulo di FreeCAD (App o Gui) consiste, per lo meno, di un modulo con un file init. Questo è un tipico file AppMyModuleGui.cpp:


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

### Il file Init.py 


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


<div class="mw-translate-fuzzy">

Per il proprio ambiente è possibile scegliere liberamente qualsiasi licenza, ma se a un certo punto si desidera vederlo integrato e distribuito con il codice sorgente di FreeCAD si deve essere consapevoli che la licenza deve essere LGPL2+, come nell\'esempio precedente. Le funzioni FreeCAD.addImportType() e addEXportType() permettono di assegnare il nome e l\'estensione di un tipo di file, e un modulo python responsabile della sua importazione. Nell\'esempio precedente, un modulo \"importOwn.py\" gestisce i file .own. Per ulteriori esempi, vedere la pagina degli [esempi di codice](Code_snippets/it.md).


</div>

The `FreeCAD.addImportType()` and `addEXportType()` functions allow you to give the name and extension of a file type, and a Python module responsible for its import. In the example above, an `importOwn.py` module will handle `.own` files. See [Code snippets](Code_snippets.md) for more examples.

### Python workbenches 


<div class="mw-translate-fuzzy">

### Ambienti di lavoro in Python 


</div>


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

Oltre a questo, si può fare tutto quello che si vuole: si potrebbe mettere tutto il codice del workbench all\'interno di InitGui.py se si vuole, ma di solito è più conveniente posizionare le diverse funzioni dell\'ambiente in file separati. Così i file sono più piccoli e più facili da leggere. Poi si importano i file nel file InitGui.py. È possibile organizzare i file nel modo desiderato, un buon esempio di organizzazione è un file per ogni comando di FreeCAD che si aggiunge.


</div>

#### Preferences

You can add a Preferences page for your Python workbench. The Preferences pages look for a preference icon with a specific name in the Qt Resource system. If your icon isn\'t in the resource system or doesn\'t have the correct name, your icon won\'t appear on the Preferences page.

Adding your workbench icon:

-   the preferences icon needs to be named \"preferences-\" + \"modulename\" + \".svg\" (all lowercase)
-   make a qrc file containing all icon names
-   in the main \*.py directory, run pyside-rcc -o myResources.py myqrc.qrc
-   in InitGui.py, add import myResource(.py)
-   update your repository(git) with myResources.py and myqrc.qrc

You\'ll need to redo the steps if you add/change icons.

\@kbwbe has created a nice script to compile resources for the A2Plus workbench. See below.

Adding your preference page(s):

-   You need to compile the Qt designer plugin that allows you to add preference settings with [Qt Designer](Compile_on_Linux#Qt_designer_plugin.md)
-   Create a blank widget in Qt Designer (no buttons or anything)
-   Design your preference page, any setting that must be saved (preferences) must be one of the Gui::Pref\* widgets that were added by the plugin)
-   In any of those, make sure you fill the PrefName (the name of your preference value) and PrefPath (ex: Mod/MyWorkbenchName), which will save your value under BaseApp/Preferences/Mod/MyWorkbenchName
-   Save the ui file in your workbench, make sure it\'s handled by cmake
-   In your workbench, for ex. inside the InitGui file, inside the Initialize method (but any other place works too), add: FreeCADGui.addPreferencePage(\"/path/to/myUiFile.ui\",\"MyGroup\"), \"MyGroup\" being one of the preferences groups on the left. FreeCAD will automatically look for a \"preferences-mygroup.svg\" file in its known locations (which you can extend with FreeCADGui.addIconPath())
-   Make sure the addPreferencePage() method is called only once, otherwise your pref page will be added several times

#### Distribution

To distribute your Python workbench, you may either simply host the files in some location and instruct your users to download them and place them in their Mod directory manually, or you may host them in an online git repository (GitHub, GitLab, Framagit, and Debian Salsa are currently supported locations) and configure them for the [Addon Manager](Std_AddonMgr.md) to install. Instructions for inclusion on FreeCAD\'s official Addons list can be found on the [FreeCAD Addons GitHub repository](https://github.com/FreeCAD/FreeCAD-addons/blob/master/README.md). To use the Addon Manager, a [package.xml metadata file](Package_Metadata.md) should be included, which instructs the Addon Manager how to find your workbench\'s icon, and allows display of a description, version number, etc. It can also be used to specify other external Addons that your Workbench either depends on, is blocked by, or is intended to replace.

Optionally, you can include a metadata file describing your Python dependencies. This may be either a file called metadata.txt describing your workbench\'s external dependencies (on either other Addons, Workbenches, or Python modules), or a [requirements.txt](https://pip.pypa.io/en/latest/reference/requirements-file-format/) describing your Python dependencies. Note that if using a requirements.txt file, only the names of the specified packages are used for dependency resolution: pip command options, include options and version information are not supported by the Addon Manager. Users may manually run the requirements file using pip if those features are required.

The format of the metadata.txt file is plain text, with three optional lines:


```python
workbenches=
pylibs=
optionalpylibs=
```

Each line should consist of a comma-separated list of items your Workbench depends on. Workbenches may be either an internal FreeCAD Workbench, e.g. \"FEM\", or an external Addon, for example \"Curves\". The required and optional Python libraries should be specified with their canonical Python names, such as you would use with `pip install`. For example:


```python
workbenches=FEM,Curves
pylibs=ezdxf
optionalpylibs=metadata,git
```

You may also include a script that is run when your package is uninstalled. This is a file called \"uninstall.py\" located at the top level of your Addon. It is executed when a user uninstalls your Addon using the Addon Manager. Use it to clean up anything your Addon may have done to the users system that should not persist when the Addon is gone (e.g. removing cache files, etc.).

### Workbench in C++ 


<div class="mw-translate-fuzzy">

Quando si vuole codificare l\'ambiente in C ++, probabilmente si vuole anche codificare la definizione dell\'ambiente stesso in C ++ (anche se non è necessario: si potrebbe anche codificare solo gli strumenti in C++, e lasciare la definizione dell\'ambiente in python). In tal caso, il file InitGui.py diventa molto semplice: Può contenere una sola riga:


</div>


```pythonimport MyModuleGui```


<div class="mw-translate-fuzzy">

dove MyModule è l\'ambiente completo in C++, inclusi i comandi e la definizione dell\'ambiente.


</div>


<div class="mw-translate-fuzzy">

La codificazione dei workbenches in C++ funziona in modo molto simile. Questo è un tipico file Workbench.cpp da includere nella parte Gui del modulo:


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

#### Preferences 

You can add a Preferences page for C++ workbenches too. The steps are similar to those for Python.

## I comandi di FreeCAD 


<div class="mw-translate-fuzzy">

I comandi FreeCAD sono gli elementi di base dell\'interfaccia di FreeCAD. Possono apparire come un pulsanti sulla barra degli strumenti, e come voce di menu. Ma sono lo stesso comando. Un comando è una semplice classe Python, che deve contenere un paio di attributi predefiniti e le funzioni che definiscono il nome del comando, la sua icona, e cosa fare quando viene attivato il comando.


</div>

### Definizione dei comandi Python 


```python
class My_Command_Class():
    """My new command"""

    def GetResources(self):
        return {"Pixmap"  : "My_Command_Icon", # the name of a svg file available in the resources
                "Accel"   : "Shift+S", # a default shortcut (optional)
                "MenuText": "My New Command",
                "ToolTip" : "What my new command does"}

    def Activated(self):
        """Do something here"""
        return

    def IsActive(self):
        """Here you can define if the command must be active or not (greyed) if certain conditions
        are met or not. This function is optional."""
        return True

FreeCADGui.addCommand("My_Command", My_Command_Class())
```

### Definizione dei comandi C++ 

Allo stesso modo, è possibile codificare i comandi in C++, in genere hanno un file Commands.cpp nel modulo Gui. Questo è un tipico file Commands.cpp:


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

## \"Compiling\" your resource file 

compileA2pResources.py from the A2Plus workbench:


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

## Related

-   [Translating an external workbench](Translating_an_external_workbench.md)
-   [Namespaced Workbenches - discussion](https://forum.freecadweb.org/viewtopic.php?t=47460)
-   [freecad.workbench\_starterkit](https://github.com/FreeCAD/freecad.workbench_starterkit)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Python Code](Category_Python Code.md) > Workbench creation/it
