# Workbench creation/zh-tw
{{TOCright}}

## Introduction


<div class="mw-translate-fuzzy">

本頁將告訴你如何增加一個新的workbench到FreeCAD介面。[Workbenches是一個FreeCAD指令的容器](Workbenches/zh-tw.md)。我們可以用Python、C++或者是混合使用前兩種語言來撰寫。而混合使用的好處是可以擁有C++的速度和Python的 flexibility 。然而在所有的workbench都會藉由兩個檔案來開啟他們


</div>

## workbench 架構 


<div class="mw-translate-fuzzy">

基本上這很簡單：需要再Mod資料夾裏面建立一個新的資料夾，並給資料夾一個任意的名字，並在資料夾中放入 **Init.py** 檔, 以及, 依照需求選擇放或不放一個 **InitGui.py** 檔. Init 會在FreeCAD開始的時候被執行然後通常會緊接著執行InitGui.py 檔，不過InitGui.py 檔只有在FreeCAD是在圖形化介面(GUI)模式下才會被執行 ，在 console 模式下不會被執行. 這些就是讓FreeCAD在啟動時找到你的workbench並且將他加到介面上所需要做的事情。


</div>

The user Mod directory is a sub-directory of the user application data directory (you can find the latter by typing `App.getUserAppDataDir()` in the [Python console](Python_console.md)):

-   On Linux it is usually **/home/<username>/.local/share/FreeCAD/Mod/** (<small>(v0.20)</small> ) or **/home/<username>/.FreeCAD/Mod/** ({{VersionMinus|0.19}}).
-   On Windows it is **%APPDATA%\FreeCAD\Mod\**, which is usually **C:\Users\<username>\Appdata\Roaming\FreeCAD\Mod\**.
-   On macOS it is usually **/Users/<username>/Library/Application Support/FreeCAD/Mod/**.

The Mod directory should look like this:


```python
/Mod/
 +-- MyWorkbench/
     +-- Init.py
     +-- InitGui.py
```

在這些檔案裏面，你可以做任何你想做的事。通常使用的方式如下

-   In the Init.py file you just add a couple of things used even when FreeCAD works in console mode, for example the file importers and exporters

-   In the InitGui.py file you usually define a workbench, which contains a name, an icon, and a series of FreeCAD commands (see below). That python file also defines functions that are executed when FreeCAD loads (you try to do as little as possible there, so you don\'t slow down the startup), another that gets executed when the workbench is activated (that\'s where you\'ll do most of the work), and a third one when the workbench is deactivated (so you can remove things if needed).

The structure and file content for a workbench described here is the classic way of creating a new workbench. One can use a slight variation in the structure of files when making a new Python workbench, that alternative way is best described as a \"namespaced workbench\", opening up the possibility to use pip to install the workbench. Both structures work, so it is more a question of preference when creating a new workbench. The style and structure for workbenches presented here are available in the global namespace of FreeCAD, whereas for the alternative style and structure the workbench resides in a dedicated namespace. For further readings on the topic see [Related](Workbench_creation#Related.md).

### C++ workbench 架構 


<div class="mw-translate-fuzzy">

如果你打算要用Python來寫你的workbench程式碼，你只需要將其他Python檔案跟Init.py 和InitGui.py放在一起就好了，而不用再去煩惱其他事情。不過當你是使用C++來撰寫workbench的時候，你必須特別留意並且遵守FreeCAD的一個基本規則：你必須將你的workbench分成App(可以在命令列介面下執行而不需要任何圖形使用者介面)和Gui(只有在FreeCAD在圖形使用者介面下執行時才會被載入)兩個部份。 所以用C++撰寫workbench你幾乎就像是在開發兩個modules，也就是App和Gui這兩個。這兩個模組當然必須能被Python呼叫。任何 FreeCAD module(App或Gui)至少都包含一個module的init 檔。這是典型AppMyModuleGui.cpp檔 ：


</div>


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

### Init.py 檔 


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

你可以為你的workbench選擇任何你喜歡的license，不過要注意的是，如果你希望見到你的workbench被FreeCAD原始碼整合並且發佈，他必須是LGPL2+就如同上面的範例。 FreeCAD.addImportType() 和addEXportType() 函式 allow you to give the name and extension of a file type, and a python module responsible for its import. 在上面的例子中，一個\"importOwn.py\" module 將會處理.own檔。請看 [Code snippets](Code_snippets.md) 來獲得更多的例子


</div>

The `FreeCAD.addImportType()` and `addEXportType()` functions allow you to give the name and extension of a file type, and a Python module responsible for its import. In the example above, an `importOwn.py` module will handle `.own` files. See [Code snippets](Code_snippets.md) for more examples.

### Python workbenches 

This is the InitGui.py file:


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

Other than that, you can do anything you want: you could put your whole workbench code inside the InitGui.py if you want, but it is usually more convenient to place the different functions of your workbench in separate files. So those files are smaller and easier to read. Then you import those files into your InitGui.py file. You can organize those files the way you want, a good example is one for each FreeCAD command you add.

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

To distribute your Python workbench, you may either simply host the files in some location and instruct your users to download them and place them in their Mod directory manually, or you may host them in an online git repository (GitHub, GitLab, Framagit, and Debian Salsa are currently supported locations) and configure them for the [Addon Manager](Std_AddonMgr.md) to install. Instructions for inclusion on FreeCAD\'s official Addons list can be found on the [FreeCAD Addons GitHub repository](https://github.com/FreeCAD/FreeCAD-addons/blob/master/README.md). To use the Addon Manager, a [package.xml metadata file](Package_Metadata.md) should be included, which instructs the Addon Manager how to find your workbench\'s icon, and allows display of a description, version number, etc. It can also be used to specify other workbenches or Python packages that your Workbench either depends on, is blocked by, or is intended to replace.

For a quick guide on how to create a basic package.xml file and add a workbench to the [Addon Manager](Std_AddonMgr.md) see: [Add Workbench to Addon Manager](Add_Workbench_to_Addon_Manager.md).

Optionally, you can include a separate metadata file describing your Python dependencies. This may be either a file called metadata.txt describing your workbench\'s external dependencies (on either other Addons, Workbenches, or Python modules), or a [requirements.txt](https://pip.pypa.io/en/latest/reference/requirements-file-format/) describing your Python dependencies. Note that if using a requirements.txt file, only the names of the specified packages are used for dependency resolution: pip command options, include options and version information are not supported by the Addon Manager. Users may manually run the requirements file using pip if those features are required.

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

To ensure that your addon is being read correctly by the Addon Manager, you can enable a \"developer mode\" in which the Addon Manager examines all available addons and ensures their metadata contains the required elements. To enable this mode select: **Edit → Preferences... → Addon Manager → Addon manager options → Addon developer mode**, see [Preferences Editor](Preferences_Editor#Addon_manager_options.md).

### C++ workbenches 


<div class="mw-translate-fuzzy">

如果你要用C++來撰寫你的workbench，你可能也會想要用C++來撰寫workbench本身的定義(雖然不一定要這樣做：你也可以只用C++來寫你的工具，然後用Python來寫workbench的定義) 在這種狀況下，InitGui.py檔會變得十分簡單：他可能只有一行：


</div>


```pythonimport MyModuleGui```


<div class="mw-translate-fuzzy">

而MyModule是你整個C++ workbench，包含commands和workbench定義


</div>


<div class="mw-translate-fuzzy">

用C++撰寫 workbenches的方法和用Python來撰寫的方式是十分類似的。這是一個典型的Workbench.cpp to include in the Gui part of your module:


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

#### Distribution 

There are two options to distribute a C++ workbench, you can either host precompiled versions for the different operating systems yourself, or you can request for your code to be merged into the FreeCAD source code. As mentioned above this requires a LGPL2+ license, and you must first present your workbench to the community in the [FreeCAD forum](https://forum.freecad.org) for review.

## FreeCAD commands 


<div class="mw-translate-fuzzy">

FreeCAD commands 是FreeCAD interface的基本元素。他可以是一個工具列上的一個按鈕，或是一個選單上的條目。不過他們都是一樣的。一個command是一個簡單的python類別，他必須包含幾個的預先定義的屬性和函式來定義這個command的名字，他的圖像以及當他被觸發時會做什麼。


</div>

### Python command definition 


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

### C++ command definition 


<div class="mw-translate-fuzzy">

同樣地，你可以用C++編寫你的commands，通常會有一個Commands.cpp檔在你的Gui module。這是一個典型的Commands.cpp檔


</div>


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
-   [Forum discussion: Namespaced Workbenches](https://forum.freecadweb.org/viewtopic.php?t=47460)
-   [freecad.workbench_starterkit](https://github.com/FreeCAD/freecad.workbench_starterkit)



---
![](images/Button_right.svg) [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Python Code](Category_Python Code.md) > Workbench creation/zh-tw
