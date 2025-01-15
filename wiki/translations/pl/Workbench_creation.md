# Workbench creation/pl
## Wprowadzenie

Ta strona pokaże Ci, jak dodać nowe środowisko pracy do interfejsu programu FreeCAD. [Środowiska pracy](Workbenches/pl.md) są kontenerami dla poleceń FreeCAD. Mogą być zakodowane w Pythonie, w C++ lub w mieszance obu tych języków, co ma tę zaletę, że łączy szybkość C++ z elastycznością Pythona. We wszystkich przypadkach jednak Twoje środowisko pracy będzie uruchamiane przez zestaw dwóch plików Python. Mogą to być \"wewnętrzne\" środowiska, dołączone do dystrybucji programu FreeCAD, lub \"zewnętrzne\", dystrybuowane za pomocą [Menadżera dodatków](Std_AddonMgr/pl.md) lub instalowane ręcznie przez pobranie z jakiegoś repozytorium online. Wewnętrzne środowiska pracy mogą być napisane w C++, środowisku Python lub kombinacji tych dwóch środowisk, podczas gdy zewnętrzne środowiska pracy muszą być napisane wyłącznie w środowisku Python.



## Struktura środowiska pracy 

Potrzebny jest folder o dowolnej nazwie, umieszczony w katalogu Mod użytkownika, z plikiem `Init.py` i opcjonalnie plikiem `InitGui.py`. Plik `Init.py` jest wykonywany podczas uruchamiania FreeCAD, a plik `InitGui.py` jest wykonywany natychmiast po nim, ale tylko wtedy, gdy FreeCAD uruchamia się w trybie GUI. To wszystko, czego potrzebuje FreeCAD, aby znaleźć środowisko pracy podczas uruchamiania i dodać je do swojego interfejsu.

Katalog Mod użytkownika jest podkatalogiem katalogu danych aplikacji użytkownika (można go znaleźć wpisując `App.getUserAppDataDir()` w [konsoli Python](Python_console/pl.md)):

-   W systemie Linux jest to zazwyczaj **/home/<nazwa użytkownika>/.local/share/FreeCAD/Mod/** ({{VersionPlus/pl|0.20}}) lub **/home/<username>/.FreeCAD/Mod/** ({{VersionMinus/pl|0.19}}).
-   W systemie Windows jest to **%APPDATA%\FreeCAD\Mod\**, który zwykle jest **C:\Users\<username>\Appdata\Roaming\FreeCAD\Mod\**.
-   Na macOS jest to zazwyczaj **/Users/<username>/Library/Application Support/FreeCAD/Mod/**.

Katalog Mod powinien wyglądać następująco:


```python
/Mod/
 +-- MyWorkbench/
     +-- Init.py
     +-- InitGui.py
```

Wewnątrz tych plików można robić, co się chce. Zazwyczaj są one używane w ten sposób:

-   W pliku Init.py wystarczy dodać kilka rzeczy używanych nawet wtedy, gdy FreeCAD działa w trybie konsoli, na przykład importerów i eksporterów plików.

-   W pliku InitGui.py zazwyczaj definiuje się środowisko pracy, które zawiera nazwę, ikonę i serię poleceń FreeCAD *(patrz poniżej)*. Ten plik Pythona definiuje również funkcje, które są wykonywane podczas ładowania FreeCAD *(starasz się robić tam jak najmniej, aby nie spowalniać uruchamiania)*, kolejną, która jest wykonywana, gdy środowisko pracy jest aktywowane *(to tam będziesz wykonywał większość pracy)*, a trzecią, gdy środowisko pracy jest dezaktywowane *(dzięki czemu możesz usuwać rzeczy w razie potrzeby)*.

Opisana tutaj struktura i zawartość plików środowiska pracy jest klasycznym sposobem tworzenia nowego środowiska pracy. Można użyć niewielkiej odmiany w strukturze plików podczas tworzenia nowego środowiska pracy w Pythonie, ten alternatywny sposób najlepiej opisać jako \"środowisko pracy z przestrzenią nazw\", otwierając możliwość użycia narzędzia pip do zainstalowania środowiska pracy. Obie struktury działają, więc jest to bardziej kwestia preferencji podczas tworzenia nowego środowiska roboczego. Przedstawiony tutaj styl i struktura środowiska roboczego są dostępne w globalnej przestrzeni nazw FreeCAD, podczas gdy w przypadku alternatywnego stylu i struktury środowisko robocze znajduje się w dedykowanej przestrzeni nazw. Więcej informacji na ten temat można znaleźć w sekcji [Powiązane](#Powiązane.md).



## C++ struktura środowiska pracy 

Jeśli zamierzasz zakodować swoje środowisko pracy w Pythonie, nie musisz zachować szczególnej ostrożności i możesz po prostu umieścić inne pliki Python razem z plikami Init.py i InitGui.py. Podczas pracy z C++ należy jednak zachować większą ostrożność i zacząć od przestrzegania jednej podstawowej zasady FreeCAD: Rozdzielenie środowiska pracy na część aplikacji *(która może działać w trybie konsoli, bez żadnego elementu GUI)* i część Gui, która zostanie załadowana tylko wtedy, gdy FreeCAD działa z pełnym środowiskiem GUI. Tak więc podczas tworzenia środowiska pracy C++, najprawdopodobniej utworzysz dwa moduły, App i Gui. Te dwa moduły muszą być oczywiście wywoływalne z Pythona. Każdy moduł FreeCAD (App lub Gui) składa się co najmniej z pliku inicjującego moduł. Jest to typowy plik AppMyModuleGui.cpp:


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



### Plik Init.py 


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

Możesz wybrać dowolną licencję dla swojego środowiska pracy, ale pamiętaj, że jeśli chcesz, aby Twoje środowisko pracy było w pewnym momencie zintegrowane z kodem źródłowym FreeCAD i rozpowszechniane z nim, musi to być LGPL2+, jak w powyższym przykładzie. Zobacz stronę wyjaśniającą zagadnienia [Licencji](License/pl.md).

Funkcje `FreeCAD.addImportType()` i `addEXportType()` pozwalają na podanie nazwy i rozszerzenia typu pliku oraz modułu Python odpowiedzialnego za jego import. W powyższym przykładzie moduł `importOwn.py` będzie obsługiwał pliki `.own`. Więcej przykładów można znaleźć na stronie [Wycinki kodów](Code_snippets/pl.md).



### Środowiska pracy w Python 

To jest plik InitGui.py:


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

Poza tym możesz zrobić co chcesz: możesz umieścić cały kod workbencha w InitGui.py, jeśli chcesz, ale zwykle wygodniej jest umieścić różne funkcje workbencha w osobnych plikach. Dzięki temu pliki te są mniejsze i łatwiejsze do przeglądania. Następnie importujesz te pliki do pliku InitGui.py. Możesz zorganizować te pliki w dowolny sposób, dobrym przykładem jest jeden dla każdego dodawanego polecenia FreeCAD.



#### Ustawienia

Można dodać stronę preferencji dla środowiska pracy Python. Strony preferencji szukają ikony preferencji o określonej nazwie w systemie zasobów Qt. Jeśli ikony nie ma w systemie zasobów lub nie ma poprawnej nazwy, ikona nie pojawi się na stronie preferencji.

Dodawanie ikony środowiska pracy:

-   ikona preferencji musi mieć nazwę \"preferences-\" + \"modulename\" + \".svg\" *(wszystkie małe litery)*,
-   utwórz plik qrc zawierający wszystkie nazwy ikon,
-   w głównym katalogu \*.py, uruchom pyside-rcc -o myResources.py myqrc.qrc
-   w InitGui.py, dodaj import myResource(.py)
-   zaktualizuj swoje repozytorium *(git)* za pomocą myResources.py i myqrc.qrc

Będziesz musiał powtórzyć te kroki, jeśli dodasz / zmienisz ikony.

\@kbwbe stworzył fajny skrypt do kompilacji zasobów dla środowiska A2Plus. Zobacz poniżej.

Dodawanie stron preferencji:

-   Musisz skompilować wtyczkę Qt Designer, która umożliwia dodawanie ustawień preferencji za pomocą [Qt Designer](Compile_on_Linux/pl#Qt_designer_plugin.md)
-   Utwórz pusty widżet w Qt Designer *(bez przycisków ani niczego)*
-   Zaprojektuj swoją stronę preferencji, każde ustawienie, które musi zostać zapisane *(preferencje)* musi być jednym z widżetów Gui::Pref\*, które zostały dodane przez wtyczkę.
-   W każdym z nich upewnij się, że wypełniłeś PrefName *(nazwa wartości preferencji)* i PrefPath *(np. Mod/MyWorkbenchName)*, co spowoduje zapisanie wartości w BaseApp/Preferences/Mod/MyWorkbenchName.
-   Zapisz plik UI w swoim środowisku pracy, upewnij się, że jest on obsługiwany przez cmake.
-   W swoim środowisku pracy, np. wewnątrz pliku InitGui, wewnątrz metody Initialize *(ale każde inne miejsce też działa)*, dodaj: FreeCADGui.addPreferencePage(\"/path/to/myUiFile.ui\", \"MyGroup\"), przy czym \"MyGroup\" jest jedną z grup preferencji po lewej stronie. FreeCAD automatycznie wyszuka plik \"preferences-mygroup.svg\" w swoich znanych lokalizacjach *(które można rozszerzyć za pomocą FreeCADGui.addIconPath())*.
-   Upewnij się, że metoda addPreferencePage() jest wywoływana tylko raz, w przeciwnym razie strona preferencji zostanie dodana kilka razy.



#### Dystrybucja

Aby rozpowszechniać swoje środowisko pracy Python, możesz po prostu hostować pliki w jakiejś lokalizacji i poinstruować użytkowników, aby pobrali je i umieścili w swoim katalogu Mod samodzielnie, lub możesz hostować je w internetowym repozytorium git *(GitHub, GitLab, Framagit i Debian Salsa są obecnie obsługiwanymi lokalizacjami)* i skonfigurować je do zainstalowania przez [Menedżer dodatków](Std_AddonMgr/pl.md). Instrukcje dotyczące włączenia do oficjalnej listy dodatków FreeCAD można znaleźć na stronie [FreeCAD Addons GitHub repozytorium](https://github.com/FreeCAD/FreeCAD-addons/blob/master/README.md). Aby korzystać z Menedżera dodatków, należy dołączyć plik metadanych [package.xml](Package_Metadata/pl.md), który instruuje Menedżera dodatków, jak znaleźć ikonę środowiska pracy i umożliwia wyświetlanie opisu, numeru wersji itp. Może on być również użyty do określenia innych środowisk pracy lub pakietów Python, od których zależy, przez które jest blokowany lub które ma zastąpić.

Aby uzyskać krótki przewodnik na temat tworzenia podstawowego pliku package.xml i dodawania środowiska roboczego do [Menedżera dodatków](Std_AddonMgr/pl.md), zobacz stronę [Dodaj środowisko pracy do Menadżera dodatków](Add_Workbench_to_Addon_Manager/pl.md).

Opcjonalnie można dołączyć oddzielny plik metadanych opisujący zależności środowiska Python. Może to być albo plik o nazwie metadata.txt opisujący zewnętrzne zależności środowiska roboczego *(od innych dodatków, środowisk roboczych lub modułów Pythona)*, albo plik [requirements.txt](https://pip.pypa.io/en/latest/reference/requirements-file-format/) opisujący zależności Python. Należy pamiętać, że w przypadku korzystania z pliku requirements.txt tylko nazwy określonych pakietów są używane do rozwiązywania zależności: opcje polecenia programu, opcje dołączania i informacje o wersji nie są obsługiwane przez Menedżera dodatków. Użytkownicy mogą ręcznie uruchomić plik wymagań za pomocą programu, jeśli te funkcje są wymagane.

Format pliku metadata.txt to zwykły tekst z trzema opcjonalnymi wierszami:


```python
workbenches=
pylibs=
optionalpylibs=
```

Każdy wiersz powinien składać się z oddzielonej przecinkami listy elementów, od których zależy środowisko pracy. Środowiska te mogą być albo wewnętrznym środowiskiem pracy FreeCAD, np. \"MES\", albo zewnętrznym dodatkiem, na przykład \"Krzywe\". Wymagane i opcjonalne biblioteki Python powinny być określone za pomocą ich kanonicznych nazw Python, takich jak `pip install`. Na przykład:


```python
workbenches=FEM,Curves
pylibs=ezdxf
optionalpylibs=metadata,git
```

Możesz również dołączyć skrypt, który jest uruchamiany po odinstalowaniu pakietu. Jest to plik o nazwie \"uninstall.py\" znajdujący się na najwyższym poziomie dodatku. Jest on wykonywany, gdy użytkownik odinstalowuje dodatek za pomocą Menedżera dodatków. Użyj go, aby wyczyścić wszystko, co dodatek mógł zrobić w systemie użytkownika, a co nie powinno przetrwać po usunięciu dodatku *(np. usunięcie plików pamięci podręcznej itp.)*.

Aby upewnić się, że dodatek jest poprawnie odczytywany przez Menedżera dodatków, można włączyć \"tryb deweloperski\", w którym Menedżer dodatków sprawdza wszystkie dostępne dodatki i upewnia się, że ich metadane zawierają wymagane elementy. Aby włączyć ten tryb, wybierz: **Edycja → Preferencje ... → Menadżer dodatków → Opcje Menedżera dodatków → Tryb dewelopera dodatków**, zobacz stronę [Edytor ustawień](Preferences_Editor/pl#Opcje_Menadżera_dodatków.md) aby uzyskać szczegółowe informacje.



### Środowiska pracy w C++ 

Jeśli zamierzasz zakodować swoje środowisko pracy w C++, prawdopodobnie będziesz chciał również zakodować samą definicję środowiska pracy w C++ *(choć nie jest to konieczne: możesz również zakodować tylko narzędzia w C++, a definicję środowiska pracy pozostawić w Pythonie)*. W takim przypadku plik InitGui.py staje się bardzo prosty: Może zawierać tylko jedną linię:


```pythonimport MyModuleGui```

gdzie MyModule jest kompletnym środowiskiem pracy C++, w tym poleceniami i definicją środowiska pracy.

Kodowanie środowisk pracy C++ działa w dość podobny sposób. Jest to typowy plik Workbench.cpp, który należy dołączyć do części Gui modułu:


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



#### Ustawienia 

Można również dodać stronę preferencji dla środowiska pracy języka C++. Kroki są podobne do tych w Pythonie.



#### Dystrybucja 

Istnieją dwie opcje dystrybucji środowiska pracy C++, można albo samodzielnie hostować wstępnie skompilowane wersje dla różnych systemów operacyjnych, albo poprosić o scalenie kodu z kodem źródłowym FreeCAD. Jak wspomniano powyżej, wymaga to licencji LGPL2+ i należy najpierw przedstawić swoje środowisko pracy społeczności do przeglądu na [forum FreeCAD](https://forum.freecad.org).



## Polecenia FreeCAD 

Polecenia FreeCAD są podstawowym elementem składowym interfejsu FreeCAD. Mogą pojawiać się jako przycisk na paskach narzędzi i jako pozycja w menu. Ale to jest to samo polecenie. Polecenie jest prostą klasą Python, która musi zawierać kilka predefiniowanych atrybutów i funkcji, które definiują nazwę polecenia, jego ikonę i co należy zrobić, gdy polecenie jest aktywowane.



### Definicja polecenia w Python 


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



### Definicja polecenia w C++ 

Podobnie, można kodować polecenia w C++, zazwyczaj w pliku Commands.cpp w module Gui. To jest typowy plik Commands.cpp:


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



## \"Kompilacja\" pliku zasobów 

compileA2pResources.py ze środowiska roboczego A2Plus:


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



## Powiązane

-   [Tłumaczenie interfejsu zewnętrznych środowisk pracyh](Translating_an_external_workbench/pl.md)
-   [Dyskusja na forum: Namespaced Workbenches](https://forum.freecadweb.org/viewtopic.php?t=47460)
-   [freecad.workbench_starterkit](https://github.com/FreeCAD/freecad.workbench_starterkit)



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer%20Documentation.md) > [Python Code](Category_Python%20Code.md) > Workbench creation/pl
