# Workbench creation/de
{{TOCright}}

## Einführung


<div class="mw-translate-fuzzy">

Diese Seite zeigt dir, wie du einen neuen Arbeitsbereich zur FreeCAD Oberfläche hinzufügst. [Arbeitbereiche](Workbenches/de.md) sind Behälter für FreeCAD Befehle. Sie können in Python, in C++ oder in einer Mischung aus beidem programmiert werden, was den Vorteil hat, die Geschwindigkeit von C++ mit der Flexibilität von Python zu verbinden. In allen Fällen wird dein Arbeitsbereich jedoch durch einen Satz von zwei Python Dateien gestartet.


</div>

## Die Arbeitsbereichsstruktur 

Du benötigst einen Ordner mit irgendeinem Namen den du magst, platziert im Benutzer Mod Verzeichnis, mit einer `Init.py` Datei und wahlweise, einer `InitGui.py` Datei. Die Init Datei wird immer ausgeführt wenn FreeCAD startet, und die `InitGui.py` Datei wird unmittelbar danach ausgeführt wird, aber nur, wenn FreeCAD im GUI Modus startet. Das ist alles, was FreeCAD braucht, um deinen Arbeitsbereich beim Start zu finden und ihn in seine Oberfläche aufzunehmen.

Das Benutzer Mod Verzeichnis ist ein Unterverzeichnis des Benutzer Anwendungsdaten Verzeichnisses (du kannst letzteres finden durch eintippen von `App.getUserAppDataDir()` in der [Python Konsole](Python_console/de.md)):

-   Unter Linux ist es üblicherweise {{FileName|/home/<username>/.FreeCAD/Mod/}}.
-   Unter Windows ist es {{FileName|%APPDATA%\FreeCAD\Macro\}}, üblicherweise {{FileName|C:\Users\<username>\Appdata\Roaming\FreeCAD\Mod\}}.
-   Unter macOS ist es üblicherweise {{FileName|/Users/<username>/Library/Preferences/FreeCAD/Mod/}}.

Das Mod Verzeichnis sollte so aussehen:


```python
/Mod/
 +-- MyWorkbench/
     +-- Init.py
     +-- InitGui.py
```

Innerhalb dieser Dateien kannst du tun, was immer du willst. Normalerweise werden sie so verwendet:

-   In der Datei Init.py fügst du einfach ein paar Dinge hinzu, die auch dann verwendet werden, wenn FreeCAD im Konsolenmodus arbeitet, z.B. die Datei Importeure und Exporteure

-   In der Datei InitGui.py definierst du normalerweise einen Arbeitsbereich, der einen Namen, ein Symbol und eine Reihe von FreeCAD Befehlen enthält (siehe unten). Diese Python Datei definiert auch Funktionen, die ausgeführt werden, wenn FreeCAD geladen wird (du versuchst, dort so wenig wie möglich zu tun, um den Start nicht zu verlangsamen), eine weitere, die ausgeführt wird, wenn der Arbeitsbereich aktiviert ist (dort wirst Du die meiste Arbeit erledigen), und eine dritte, wenn der Arbeitsbereich deaktiviert ist (damit Du Dinge, wenn nötig, entfernen kannst).

Die hier beschriebene Struktur und der Dateiinhalt eines Arbeitsbereich sind der klassische Weg beim Anlegen eines Arbeitsbereichs. Man kann eine leichte Abwandlung in der Dateistruktur benutzen, wenn ein neuer Python-Arbeitsbereich erstellt werden soll; dieser alternative Weg kann am besten als \"namespaced workbench\" (Arbeitsbereich mit eigenem Namensraum) bezeichnet werden, wodurch die Möglichkeit eröffnet wird, pip zur Installation des neuen Arbeitsbereichs zu verwenden. Das Aussehen und die Struktur von hier gezeigten Arbeitsbereichen sind im globalen Namensraum von FreeCAD enthalten, während sich das alternative Aussehen und die Struktur des Arbeitsbereichs in einem dedizierten Namensraum befindet.
Weitere Informationen zu dem Thema findest du unter [Verwandtes](Workbench_creation/de#Related.md).

### C++ Arbeitsbereichsstruktur 

Wenn du deinen Arbeitsbereich in Python programmieren willst, brauchst du keine besondere Vorsicht walten zu lassen und kannst einfach deine anderen Python Dateien zusammen mit deinen Init.py und InitGui.py Dateien unterbringen. Wenn du jedoch mit C++ arbeitest, solltest du größere Sorgfalt walten lassen und damit beginnen, eine grundlegende Regel von FreeCAD zu beachten: Die Trennung deines Arbeitsbereichs zwischen einem Anwendungsteil (der im Konsolenmodus laufen kann, ohne jedes GUI Element) und einem Gui Teil, der nur geladen wird, wenn FreeCAD mit seiner vollständigen GUI Umgebung läuft. Wenn du also einen C++ Arbeitsbereich verwendest, wirst du höchstwahrscheinlich zwei Module verwenden, eine Anwendung und eine Gui. Diese beiden Module müssen natürlich von Python aus aufrufbar sein. Jedes FreeCAD Modul (Anwendung oder Gui) besteht mindestens aus einer Modul Init Datei. Dies ist eine typische AppMyModuleGui.cpp Datei:


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

### Die Init.py Datei 


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

Du kannst jede beliebige Lizenz für deinen Arbeitsbereich wählen, aber sei dir bewusst, dass, wenn du deinen Arbeitsbereich irgendwann in den FreeCAD Quellcode integrierst und mit diesem verteilt sehen möchtest, diese wie im obigen Beispiel unter LGPL2+ stehen muss. Siehe [Lizenz](Licence/de.md).

Die `FreeCAD.addImportType()` und `addEXportType()` Funktionen ermöglichen es dir, den Namen und die Erweiterung eines Dateityps sowie ein für seinen Import verantwortliches Python-Modul anzugeben. Im obigen Beispiel wird ein `importOwn.py` Modul `.own` Dateien handhaben. Siehe [Codeschnipsel](Code_snippets/de.md) für weitere Beispiele.

### Python workbenches 


<div class="mw-translate-fuzzy">

### Python Arbeitsbereiche 

Dies ist die InitGui.py Datei:


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

Ansonsten kannst du alles tun, was du willst: Du kannst deinen gesamten Arbeitsbereichscode in die InitGui.py setzen, wenn du möchtest, aber es ist normalerweise bequemer, die verschiedenen Funktionen deines Arbeitsbereichs in separaten Dateien zu platzieren. Deshalb sind diese Dateien kleiner und einfacher zu lesen. Dann importierst du diese Dateien in deine InitGui.py Datei. Du kannst diese Dateien anordnen wie du willst, ein gutes Beispiel ist eine für jeden FreeCAD-Befehl, den du hinzufügst.

#### Einstellungen

Du kannst eine Einstellungsseite für deinen Python Arbeitsbereich hinzufügen. Die Einstellungsseiten suchen nach einem Einstellungssymbol mit einem bestimmten Namen im Qt Ressourcensystem. Wenn sich dein Symbol nicht im Ressourcensystem befindet oder nicht den korrekten Namen hat, wird dein Symbol nicht auf der Einstellungsseite erscheinen.

Hinzufügen deines Arbeitsbereichssymbols:

-   das Einstellungssymbol muss \"preferences-\" genannt werden + \"modulename\" + \".svg\" (alles Kleinbuchstaben)
-   erstelle eine qrc Datei, die alle Symbolnamen enthält
-   Führe im Haupt \*.py Verzeichnis pyside-rcc -o myResources.py myqrc.qrc aus
-   In InitGui.py, füge import myResource(.py) hinzu
-   aktualisiere dein Repositorium (git) mit myResources.py und myqrc.qrc

Du musst du die Schritte erneut ausführen wenn du Symbole hinzufügst/änderst,

\@kbwbe hat ein nettes Skript zum Kompilieren von Ressourcen für den A2Plus Arbeitsbereich erstellt. Siehe unten.

Hinzufügen deiner Einstellungsseite(n):

-   Du musst das Qt Designer Zusatzmodul kompilieren, das dir das Hinzufügen von Präferenzeinstellungen mit [Qt Designer](Compile_on_Linux/de#Qt_designer_plugin.md) ermöglicht
-   Erstelle ein leeres Widget im Qt Designer (keine Schaltflächen oder ähnliches)
-   Gestalte deine Präferenzseite, jede Einstellung, die gespeichert werden muss (Präferenzen), muss eines der Gui::Pref\* Widgets sein, die durch das Zusatzmodul hinzugefügt wurden)
-   Stelle sicher, dass du in einem dieser Felder den PrefName (den Namen deines Präferenzwertes) und PrefPath (z.B.: Mod/MyWorkbenchName), der deine Werte unter BaseApp/Preferences/Mod/MyWorkbenchName speichern wird
-   Speichere die ui Datei in deinem Arbeitsbereich, stelle sicher, dass sie von cmake verarbeitet wird
-   In deinem Arbeitsbereich, z.B. innerhalb der InitGui Datei, innerhalb der Initialisierungsmethode (aber jeder andere Ort funktioniert auch), füge: FreeCADGui.addPreferencePage(\"/path/to/myUiFile.ui\",\"MyGroup\"), \"MyGroup\" als eine der Präferenzgruppen auf der linken Seite. FreeCAD sucht automatisch nach einer \"preferences-mygroup.svg\" Datei an den bekannten Speicherorten (die du mit FreeCADGui.addIconPath() erweitern kannst)
-   Stelle sicher, dass die Methode addPreferencePage() nur einmal aufgerufen wird, andernfalls wird deine Vorzugsseite mehrmals hinzugefügt

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

### C++ Arbeitsbereiche 

Wenn du deinen Arbeitsbereich in C++ programmierst, wirst du wahrscheinlich die Arbeitsbereichsdefinition selbst auch in C++ programmieren (obwohl es nicht notwendig ist: du könntest auch nur die Werkzeuge in C++ programmieren und die Arbeitsbereichsdefinition in Python belassen). In diesem Fall, wird die Datei InitGui.py sehr einfach: Sie könnte nur eine Zeile enthalten:


```pythonimport MyModuleGui```

wobei MyModule dein vollständiger C++ Arbeitsbereich ist, der die Befehle und Arbeitsbereichsdefinition einschließt.

Die Programmierung von C++ Arbeitsbereichen funktioniert auf ziemlich ähnliche Weise. Dies ist eine typische Workbench.cpp Datei, die du in den Gui-Teil deines Moduls aufnehmen kannst:


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

#### Einstellungen 

Du kannst auch eine Voreinstellungsseite für C++ Arbeitsbereiche hinzufügen. Die Schritte sind ähnlich wie die für Python.

## FreeCAD Befehle 

FreeCAD Befehle sind die Grundbausteine der FreeCAD Oberfläche. Sie können als Knöpfe in Werkzeugleisten und als Einträge in Menüs erscheinen. Es handelt sich dabei immer um den selben Befehl. Ein Befehl ist einfach eine Python Klasse, die eine Reihe von vordefinierten Attributen und Funktionen enthält, wie der Befehlsname, das Symbol und der Code, der ausgeführt wird, wenn der Befehl aktiviert wird.

### Python Befehlsdefinition 


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

### C++ Befehlsdefinition 

In ähnlicher Weise kannst du deine Befehle in C++ programmieren, normalerweise hast du eine Commands.cpp Datei in deinem Gui Modul. Dies ist eine typische Commands.cpp Datei:


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

## \"Kompilieren\" deiner Ressourcendatei 

compileA2pResources.py aus dem A2Plus Arbeitsbereich:


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

## Verwandtes

-   [Übersetzen eines externen Arbeitsbereichs](Translating_an_external_workbench/de.md)
-   [Namespaced Workbenches - discussion](https://forum.freecadweb.org/viewtopic.php?t=47460)
-   [freecad.workbench\_starterkit](https://github.com/FreeCAD/freecad.workbench_starterkit)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Python Code](Category_Python Code.md) > Workbench creation/de
