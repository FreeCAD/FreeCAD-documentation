# Workbench creation/ru
## Вступление

В данном материале изложена информация о том, как создать новый верстак для FreeCAD и добавить его в интерфейс. [Верстаки](Workbenches/ru.md) являются контейнерами для команд FreeCAD. Они могут быть написаны на Python или на C++ или в сочетании того и другого, что имеет преимущество в сочетании скорости C++ и гибкости Python. Однако во всех случаях ваш верстак будет запущен через два специальных Python файла. Это касается, как \"внутренних\" верстаков, входящих в дистрибутив FreeCAD, так и \"внешних\", распространяемых через [менеджер дополнений](Std_AddonMgr/ru.md) или устанавливаемыми вручную путем загрузки из какого-либо онлайн-репозитория. Внутренние верстаки могут быть написаны либо на C++, либо на Python, либо на их комбинации, в то время как внешние верстаки могут быть написаны, только на Python.



## Структура Верстака 

You need a folder, with any name you like, placed in the user Mod directory, with an `Init.py` file, and, optionally an `InitGui.py` file. The `Init.py` file is executed when FreeCAD starts, and the `InitGui.py` file is executed immediately after, but only when FreeCAD starts in GUI mode. That\'s all it needs for FreeCAD to find your workbench at startup and add it to its interface.

The user Mod directory is a sub-directory of the user application data directory (you can find the latter by typing `App.getUserAppDataDir()` in the [Python console](Python_console.md)):

-   On Linux it is usually **/home/<username>/.local/share/FreeCAD/Mod/** (<small>(v0.20)</small> ) or **/home/<username>/.FreeCAD/Mod/** ({{VersionMinus|0.19}}).
-   On Windows it is **%APPDATA%\FreeCAD\Mod\**, which is usually **C:\Users\<username>\Appdata\Roaming\FreeCAD\Mod\**.
-   On macOS it is usually **/Users/<username>/Library/Application Support/FreeCAD/Mod/**.

Mod папка должна выглядеть так:


```python
/Mod/
 +-- MyWorkbench/
     +-- Init.py
     +-- InitGui.py
```

Внутри этих файлов вы можете делать все, что захотите. Обычно они используются таким образом:

-   В файл Init.py вы прописываете некоторые вещи, который используются даже тогда, когда FreeCAD работает в консольном режиме, например такие как: импортеры и экспортеры файлов.

-   В файле InitGui.py вы инициализируете Верстак, который содержит имя, значок и ряд команд FreeCAD (см. Ниже). Этот python файл также должен иметь определенные функции: первая выполняется при загрузке FreeCAD (стараетесь сделать ее как можно меньше, чтобы не замедлять запуск FreeCAD), еще одну, которая выполняется при активации верстака (именно там выполняется большая часть работы), и третью, когда верстак деактивирован (чтобы при необходимости можно было освободить ненужные ресурсы).

The structure and file content for a workbench described here is the classic way of creating a new workbench. One can use a slight variation in the structure of files when making a new Python workbench, that alternative way is best described as a \"namespaced workbench\", opening up the possibility to use pip to install the workbench. Both structures work, so it is more a question of preference when creating a new workbench. The style and structure for workbenches presented here are available in the global namespace of FreeCAD, whereas for the alternative style and structure the workbench resides in a dedicated namespace. For further readings on the topic see [Related](#Related.md).



### Структура верстака на языке C++ 

Если вы собираетесь создать Верстак на python, вам не нужно проявлять особую осторожность, и вы можете просто разместить другие файлы python в папке с Init.py и InitGui.py. Однако при работе с C++ вам следует проявлять большую осторожность и начинать соблюдать одно фундаментальное правило FreeCAD: Разделение вашего рабочего стола между частью приложения (которая может работать в режиме консоли, без какого-либо элемента графического интерфейса) и частью графического интерфейса, которая будет загружена только при запуске FreeCAD с полной графической средой. Поэтому при создании верстака на C++ вы, скорее всего, будете использовать два модуля: модуль самого приложения и модуль графического интерфейса. Эти два модуля, конечно, должны быть вызываемы из python. Любой модуль FreeCAD (приложение или графический интерфейс) состоит, по крайней мере, из файла инициализации модуля. Это типичный AppMyModuleGui.cpp файл:


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



### Файл Init.py 


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
# *   for detail see the LICENSE text file.                                 *
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
FreeCAD.addExportType("My own format (*.own)", "exportOwn")
print("I am executing some stuff here when FreeCAD starts!")
}}


<div class="mw-translate-fuzzy">

Вы можете выбрать любую понравившуюся лицензию для вашего верстака, но имейте в виду, что если вы хотите, чтобы ваш верстак в какой-то момент был интегрирован в исходный код FreeCAD и распространялся вместе с ним, он должен быть LGPL2 +, как в примере выше. Смотрите [лицензирование](License/ru.md).


</div>

The `FreeCAD.addImportType()` and `addEXportType()` functions allow you to give the name and extension of a file type, and a Python module responsible for its import. In the example above, an `importOwn.py` module will handle `.own` files. See [Code snippets](Code_snippets.md) for more examples.



### Python верстаки 

InitGui.py файл:


```python
class MyWorkbench (Workbench):

    MenuText = "My Workbench"
    ToolTip = "A description of my workbench"
    Icon = """paste here the contents of a 16x16 xpm icon"""

    def Initialize(self):
        """This function is executed when the workbench is first activated.
        It is executed once in a FreeCAD session followed by the Activated function.
        """
        import MyModuleA, MyModuleB # import here all the needed files that create your FreeCAD commands
        self.list = ["MyCommand1", "MyCommand2"] # a list of command names created in the line above
        self.appendToolbar("My Commands", self.list) # creates a new toolbar with your commands
        self.appendMenu("My New Menu", self.list) # creates a new menu
        self.appendMenu(["An existing Menu", "My submenu"], self.list) # appends a submenu to an existing menu

    def Activated(self):
        """This function is executed whenever the workbench is activated"""
        return

    def Deactivated(self):
        """This function is executed whenever the workbench is deactivated"""
        return

    def ContextMenu(self, recipient):
        """This function is executed whenever the user right-clicks on screen"""
        # "recipient" will be either "view" or "tree"
        self.appendContextMenu("My commands", self.list) # add commands to the context menu

    def GetClassName(self): 
        # This function is mandatory if this is a full Python workbench
        # This is not a template, the returned string should be exactly "Gui::PythonWorkbench"
        return "Gui::PythonWorkbench"
       
Gui.addWorkbench(MyWorkbench())
```

Кроме этого, вы можете делать все, что захотите: если хотите, вы могли бы поместить весь код своего верстака внутрь InitGui.py, но обычно удобнее размещать различные функции вашего верстака в отдельных файлах. Таким образом, эти файлы меньше по размеру и их легче читать. После чего вы можете импортировать эти файлы в InitGui.py файл. Также, вы можете упорядочить файлы, как пожелаете, хорошим примером является создавать по одному отдельному файлу для каждой добавляемой вами команды FreeCAD.



#### Раздел настроек верстака 

Вы можете добавить страницу настроек для вашего Python верстака. Страницы настроек ищут значок с определенным именем в системе ресурсов Qt. Если вашего значка нет в системе ресурсов или у него неправильное имя, ваш значок не будет отображаться в окне настроек.

Добавление значка для вашего верстака:

-   значок настроек должен иметь название \"preferences-\" + \"modulename\" + \".svg\" (все в нижнем регистре)
-   создайте файл qrc, содержащий все названия значков
-   в главном каталоге \*.py запустите pyside-rcc -o myResources.py myqrc.qrc
-   в InitGui.py, добавьте импорт MyResource(.py)
-   обновите свой репозиторий (git) с помощью myResources.py и myqrc.qrc

При добавлении или изменении значков, следует повторить вышеперечисленные шаги.

\@kbwbe has created a nice script to compile resources for the A2Plus workbench. See below.

Adding your preference page(s):

-   You need to compile the Qt designer plugin that allows you to add preference settings with [Qt Designer](Compile_on_Linux#Qt_designer_plugin.md)
-   Create a blank widget in Qt Designer (no buttons or anything)
-   Design your preference page, any setting that must be saved (preferences) must be one of the Gui::Pref\* widgets that were added by the plugin)
-   In any of those, make sure you fill the PrefName (the name of your preference value) and PrefPath (ex: Mod/MyWorkbenchName), which will save your value under BaseApp/Preferences/Mod/MyWorkbenchName
-   Save the ui file in your workbench, make sure it\'s handled by cmake
-   In your workbench, for ex. inside the InitGui file, inside the Initialize method (but any other place works too), add: FreeCADGui.addPreferencePage(\"/path/to/myUiFile.ui\",\"MyGroup\"), \"MyGroup\" being one of the preferences groups on the left. FreeCAD will automatically look for a \"preferences-mygroup.svg\" file in its known locations (which you can extend with FreeCADGui.addIconPath())
-   Make sure the addPreferencePage() method is called only once, otherwise your pref page will be added several times



#### Публикация и распространение 

To distribute your Python workbench, you may either simply host the files in some location and instruct your users to download them and place them in their Mod directory manually, or you may host them in an online git repository (GitHub, GitLab, Framagit, and Debian Salsa are currently supported locations) and configure them for the [Addon Manager](Std_AddonMgr.md) to install. Instructions for inclusion on FreeCAD\'s official Addons list can be found on the [FreeCAD Addons GitHub repository](https://github.com/FreeCAD/FreeCAD-addons/blob/master/README.md). To use the Addon Manager, a [package.xml metadata file](Package_Metadata.md) should be included, which instructs the Addon Manager how to find your workbench\'s icon, and allows display of a description, version number, etc. It can also be used to specify other workbenches or Python packages that your Workbench either depends on, is blocked by, or is intended to replace.

For a quick guide on how to create a basic package.xml file and add a workbench to the [Addon Manager](Std_AddonMgr.md) see: [Add Workbench to Addon Manager](Add_Workbench_to_Addon_Manager.md).

Optionally, you can include a separate metadata file describing your Python dependencies. This may be either a file called metadata.txt describing your workbench\'s external dependencies (on either other Addons, Workbenches, or Python modules), or a [requirements.txt](https://pip.pypa.io/en/latest/reference/requirements-file-format/) describing your Python dependencies. Note that if using a requirements.txt file, only the names of the specified packages are used for dependency resolution: pip command options, include options and version information are not supported by the Addon Manager. Users may manually run the requirements file using pip if those features are required.

Формат metadata.txt файла представляет собой обычный текст с тремя опциональными строками:


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

To ensure that your addon is being read correctly by the Addon Manager, you can enable a \"developer mode\" in which the Addon Manager examines all available addons and ensures their metadata contains the required elements. To enable this mode select: **Edit → Preferences... → Addon Manager → Addon manager options → Addon developer mode**, see [Preferences Editor](Preferences_Editor#Addon_manager_options.md).



### C++ верстаки 

If you are going to code your workbench in C++, you will probably want to code the workbench definition itself in C++ too (although it is not necessary: you could also code only the tools in C++, and leave the workbench definition in Python). In that case, the InitGui.py file becomes very simple: It might contain just one line:


```pythonimport MyModuleGui```

where MyModule is your complete C++ workbench, including the commands and workbench definition.

Coding C++ workbenches works in a pretty similar way. This is a typical Workbench.cpp file to include in the Gui part of your module:


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



#### Раздел настроек верстака 

Вы также можете добавить страницу настроек для верстаков C++. Шаги аналогичны тем, что выполняются в Python.



#### Публикация и распространение 

There are two options to distribute a C++ workbench, you can either host precompiled versions for the different operating systems yourself, or you can request for your code to be merged into the FreeCAD source code. As mentioned above this requires a LGPL2+ license, and you must first present your workbench to the community in the [FreeCAD forum](https://forum.freecad.org) for review.



## команды FreeCAD 

FreeCAD commands are the basic building block of the FreeCAD interface. They can appear as a button on toolbars, and as a menu entry in menus. But it is the same command. A command is a simple Python class, that must contain a couple of predefined attributes and functions, that define the name of the command, its icon, and what to do when the command is activated.



### Определение команд в Python 


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



### Определение команд в С++ 

Similarly, you can code your commands in C++, typically in a Commands.cpp file in your Gui module. This is a typical Commands.cpp file:


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



## \"Компиляция\" файлов ресурсов 

compileA2pResources.py из верстака A2Plus:


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
#*   for detail see the LICENSE text file.                                 *
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



## Сопутствующая информация 

-   [Translating an external workbench](Translating_an_external_workbench.md)
-   [Forum discussion: Namespaced Workbenches](https://forum.freecadweb.org/viewtopic.php?t=47460)
-   [freecad.workbench_starterkit](https://github.com/FreeCAD/freecad.workbench_starterkit)



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer%20Documentation.md) > [Python Code](Category_Python%20Code.md) > Workbench creation/ru
