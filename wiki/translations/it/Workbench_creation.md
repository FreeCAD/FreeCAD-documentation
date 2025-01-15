# Workbench creation/it
## Introduzione

Questa pagina da indicazioni su come aggiungere un nuovo ambiente di lavoro all\'interfaccia di FreeCAD. Gli [Ambienti di Lavoro](Workbenches/it.md) sono contenitori per i comandi di FreeCAD. Possono essere codificati in Python, in C++ o in un mix di entrambi, il che ha il vantaggio di unire la velocità del C++ alla flessibilità di Python. In tutti i casi, tuttavia, l\'ambiente verrà avviato da un set di due file Python. Possono essere ambienti di lavoro \"interni\", inclusi nella distribuzione di FreeCAD, o ambienti di lavoro \"esterni\", distribuiti tramite l\'[Addon Manager](Std_AddonMgr/it.md) o installati manualmente scaricandoli da qualche repository online. Gli Ambienti di lavoro interni possono essere codificati in C++, Python o una combinazione dei due, mentre i workbench esterni devono essere solo in Python.



## La struttura dell\'Ambiente di lavoro 

È necessaria una cartella, con qualsiasi nome si voglia, collocata nella directory Mod dell\'utente, con un file `Init.py` e, facoltativamente, un file `InitGui.py`. Il file `Init.py` viene eseguito all\'avvio di FreeCAD e il file `InitGui.py` viene eseguito immediatamente dopo, ma solo quando FreeCAD si avvia in modalità GUI. Questo è tutto ciò che serve a FreeCAD per trovare l\'ambiente di lavoro all\'avvio e aggiungerlo alla propria interfaccia.

La cartella utente Mod è una sottocartella della cartella dei dati dell\'applicazione utente (si può trovare quest\'ultima digitando `App.getUserAppDataDir()` nella [console Python](Python_console/it.md)):

-   Per Linux è solitamente **/home/<username>/.local/share/FreeCAD/Mod/** ({{VersionPlus/it|0.20}}) o **/home/<username>/.FreeCAD/Mod/** ({{VersionMinus/it|0.19}}).
-   Per Windows è **%APPDATA%\FreeCAD\Mod\**, che di solito è **C:\Users\<username>\Appdata\Roaming\FreeCAD\Mod\**.
-   Per macOS è solitamente **/Users/<username>/Library/Application Support/FreeCAD/Mod/**.

La directory Mod dovrebbe essere simile a questa:


```python
/Mod/
 +-- MyWorkbench/
     +-- Init.py
     +-- InitGui.py
```

All\'interno questi file si può fare quello che si vuole. Di solito vengono utilizzati in questo modo:

-   Nel file Init.py si inseriscono solo alcune cose, usate anche quando FreeCAD funziona in modalità console, per esempio, gli importatori e gli esportatori di file

-   Nel file InitGui.py si definisce un ambiente di lavoro che contiene un nome, un\'icona e una serie di comandi di FreeCAD (vedi sotto). Nel file python si definiscono inoltre le funzioni che vengono eseguite quando si carica FreeCAD (in questa parte si cerca di fare meno lavoro possibile, in modo da non rallentare l\'avvio), quelle che vengono eseguite quando si attiva l\'ambiente (la parte dove si esegue la maggior parte del lavoro), e come terze quelle che servono quando l\'ambiente viene disattivato (in modo da poter rimuovere le cose, se è necessario).

La struttura e il contenuto del file per un ambiente di lavoro descritto qui è il modo classico di creare un nuovo ambiente. Si può usare una leggera variazione nella struttura dei file quando si crea un nuovo ambiente in Python, questo modo alternativo è descritto più precisamente come un \"ambiente di lavoro con spazio dei nomi\", aprendo la possibilità di usare pip per installare l\'ambiente. Entrambe le strutture funzionano, quindi è più una questione di preferenza quando si crea un nuovo ambiente di lavoro. Lo stile e la struttura per gli ambienti qui presentati sono disponibili nello spazio dei nomi globale di FreeCAD, mentre per lo stile e la struttura alternativi l\'ambiente risiede in uno spazio dei nomi dedicato. Per ulteriori letture sull\'argomento vedere [Riferimenti](#Riferimenti.md)



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

Si può scegliere qualsiasi licenza che si desidera per il proprio workbench, ma si tenga presente che se ad un certo punto si vuole vedere il proprio workbench integrato e distribuito con il codice sorgente di FreeCAD, deve essere LGPL2+ come nell\'esempio sopra. Vedere la [Licenza](License/it.md).

Le funzioni `FreeCAD.addImportType()` e `addEXportType()` consentono di fornire il nome e l\'estensione di un tipo di file e un modulo Python responsabile della sua importazione. Nell\'esempio sopra, un modulo `importOwn.py` gestirà i file `.own`. Vedere [Frammenti di codice](Code_snippets/it.md) per altri esempi.



### Ambienti di lavoro in Python 

Questo è il file InitGui.py:


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

A parte questo, si può fare tutto ciò che si vuole: si potrebbe mettere tutto il codice del workbench all\'interno di InitGui.py se si vuole, ma di solito è più conveniente posizionare le diverse funzioni dell\'ambiente in file separati. Così i file sono più piccoli e più facili da leggere. Poi si importano i file in InitGui.py. È possibile organizzare i file nel modo desiderato, un buon esempio di organizzazione è un file per ogni comando di FreeCAD che si aggiunge.



#### Preferenze

Si può aggiungere una pagina Preferenze per il proprio ambiente di lavoro Python. Le pagine delle preferenze cercano un\'icona di preferenza con un nome specifico nel sistema Qt Resource. Se l\'icona non è nel sistema di risorse o non ha il nome corretto, l\'icona non verrà visualizzata nella pagina Preferenze.

Aggiunta dell\'icona del proprio workbench:

-   l\'icona delle preferenze deve essere chiamata \"preferences-\" + \"modulename\" + \".svg\" (tutto in minuscolo)
-   creare un file qrc contenente tutti i nomi delle icone
-   nella directory principale \*.py, eseguire pyside-rcc -o myResources.py myqrc.qrc
-   in InitGui.py, aggiungere import myResource(.py)
-   aggiornare il tuo repository (git) con myResources.py e myqrc.qrc

Si dovranno ripetere i passaggi se si aggiungono o modificano le icone.

\@kbwbe ha creato un buon script per compilare risorse per il workbench A2Plus. Vedere sotto.

Aggiunta delle tue pagine delle preferenze:

-   Si deve compilare il plug-in Qt designer che consente di aggiungere le impostazioni delle preferenze con [Qt Designer](Compile_on_Linux/it#Plug-in_Qt_designer.md)
-   Creare un widget vuoto in Qt Designer (nessun pulsante o altro)
-   Progettare tua pagina delle preferenze, qualsiasi impostazione che deve essere salvata (preferenza) deve essere uno dei widget Gui::Pref\* che sono stati aggiunti dal plugin)
-   In ognuno di questi, assicurarsi d\'inserire PrefName (il nome del tuo valore di preferenza) e PrefPath (es: Mod/MyWorkbenchName), che salverà il tuo valore in BaseApp/Preferences/Mod/MyWorkbenchName
-   Salvare il file ui nel proprio ambiente, assicurarsi che sia gestito da cmake
-   Nel proprio banco di lavoro, ad es. all\'interno del file InitGui, all\'interno del metodo Initialize (ma funziona anche in qualsiasi altro posto), aggiungere: FreeCADGui.addPreferencePage(\"/path/to/myUiFile.ui\",\"MyGroup\"), \"MyGroup\" essendo uno dei gruppi di preferenze su la sinistra. FreeCAD cercherà automaticamente un file \"preferences-mygroup.svg\" nelle sue posizioni note (che si può estendere con FreeCADGui.addIconPath())
-   Assicurarsi che il metodo addPreferencePage() sia chiamato solo una volta, altrimenti la pagina pref verrà aggiunta più volte



#### Distribuzione

Per distribuire il proprio workbench Python, si può semplicemente ospitare i file in una posizione e istruire gli utenti a scaricarli e inserirli manualmente nella loro directory Mod, oppure si possono ospitare in un repository git online (GitHub, GitLab, Framagit e Debian Salsa sono posizioni attualmente supportate) e configurarle per l\'installazione con l\'[Addon Manager](Std_AddonMgr/it.md). Le istruzioni per l\'inclusione nell\'elenco dei componenti aggiuntivi ufficiali di FreeCAD sono disponibili nel [repository GitHub dei componenti aggiuntivi di FreeCAD](https://github.com/FreeCAD/FreeCAD-addons/blob/master/README.md). Per utilizzare Addon Manager, è necessario includere un [package.xml metadata file](Package_Metadata/it.md), che istruisce Addon Manager su come trovare l\'icona del proprio ambiente e consente la visualizzazione di una descrizione, numero di versione, ecc. Può anche essere utilizzato per specificare altri workbench o pacchetti Python da cui dipende l\'ambiente in cui è bloccato o che è destinato a sostituire.

Per una guida rapida su come creare un file package.xml di base e aggiungere un workbench all\'[Addon Manager](Std_AddonMgr/it.md) vedere: [Aggiungere Workbench in Addon Manager](Add_Workbench_to_Addon_Manager/it.md).

Facoltativamente, si può includere a parte un file di metadati che descriva le dipendenze Python. Questo può essere un file chiamato metadata.txt che descrive le dipendenze esterne dell\'ambiente (su altri componenti aggiuntivi, workbench o moduli Python) o un [-format/ requirements.txt](https://pip.pypa.io/en/latest/reference/requirements-file) descrivendo le dipendenze Python. Si noti che se si utilizza un file requirements.txt, solo i nomi dei pacchetti specificati vengono utilizzati per la risoluzione delle dipendenze: le opzioni del comando pip, le opzioni di inclusione e le informazioni sulla versione non sono supportate da Addon Manager. Gli utenti possono eseguire manualmente il file dei requisiti utilizzando pip se tali funzionalità sono richieste.

Il formato del file metadata.txt è testo semplice, con tre righe facoltative:


```python
workbenches=
pylibs=
optionalpylibs=
```

Ogni riga dovrebbe consistere in un elenco separato da virgole di elementi da cui dipende l\'Ambiente. Gli ambienti di lavoro possono essere un ambiente di lavoro interno di FreeCAD, ad es. \"FEM\", o un Addon esterno, ad esempio \"Curve\". Le librerie Python obbligatorie e facoltative dovrebbero essere specificate con i loro nomi Python canonici, come si userebbe con `pip install`. Per esempio:


```python
workbenches=FEM,Curves
pylibs=ezdxf
optionalpylibs=metadata,git
```

Si può anche includere uno script che viene eseguito quando il pacchetto viene disinstallato. Questo è un file chiamato \"uninstall.py\" che si trova al livello superiore del componente aggiuntivo. Viene eseguito quando un utente disinstalla il componente aggiuntivo utilizzando Addon Manager. Si usa per ripulire tutto ciò che il componente aggiuntivo potrebbe aver fatto al sistema degli utenti e che non dovrebbe persistere quando il componente aggiuntivo viene rimosso (ad esempio, rimuovere i file della cache, ecc.).

Per assicurarti che il proprio componente aggiuntivo venga letto correttamente da Addon Manager, si può abilitare una \"modalità sviluppatore\" in cui Addon Manager esamina tutti i componenti aggiuntivi disponibili e garantisce che i loro metadati contengano gli elementi richiesti. Per abilitare questa modalità selezionare: **Modifica → Preferenze... → Gestore componenti aggiuntivi → Opzioni gestore componenti aggiuntivi → Modalità sviluppatore componenti aggiuntivi**, vedere l\'[Editor delle preferenze](Preferences_Editor/it#Opzioni_di_Addon_manager.md).



### Workbench in C++ 

Quando si vuole codificare l\'ambiente in C ++, probabilmente si vuole anche codificare la definizione dell\'ambiente stesso in C ++ (anche se non è necessario: si potrebbe anche codificare solo gli strumenti in C++, e lasciare la definizione dell\'ambiente in python). In tal caso, il file InitGui.py diventa molto semplice: Può contenere una sola riga:


```pythonimport MyModuleGui```

dove MyModule è l\'ambiente completo in C++, inclusi i comandi e la definizione dell\'ambiente.

La codificazione dei workbenches in C++ funziona in modo molto simile. Questo è un tipico file Workbench.cpp da includere nella parte Gui del modulo:


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



#### Preferenze 

Si può anche aggiungere una pagina delle preferenze per i workbench C++. I passaggi sono simili a quelli per Python.



#### Distribuzione 

Ci sono due opzioni per distribuire un workbench C++, si può ospitare da se le versioni precompilate per i diversi sistemi operativi oppure si può richiedere che il codice venga unito al codice sorgente di FreeCAD. Come accennato in precedenza, ciò richiede una licenza LGPL2+ e si deve prima presentare il proprio workbench alla comunità nel [forum di FreeCAD](https://forum.freecad.org) per la revisione.



## I comandi di FreeCAD 

I comandi FreeCAD sono gli elementi di base dell\'interfaccia di FreeCAD. Possono apparire come un pulsanti sulla barra degli strumenti, e come voce di menu. Ma sono lo stesso comando. Un comando è una semplice classe Python, che deve contenere un paio di attributi predefiniti e le funzioni che definiscono il nome del comando, la sua icona, e cosa fare quando viene attivato il comando.



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

Allo stesso modo, è possibile codificare i comandi in C++, in genere in un file Commands.cpp nel modulo Gui. Questo è un tipico file Commands.cpp:


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



## \"Compilazione\" del file di risorse 

compileA2pResources.py dall\'ambiente A2Plus:


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



## Riferimenti

-   [Traduzione di un ambiente di lavoro esterno](Translating_an_external_workbench/it.md)
-   [Forum discussion: Namespaced Workbenches](https://forum.freecadweb.org/viewtopic.php?t=47460)
-   [freecad.workbench_starterkit](https://github.com/FreeCAD/freecad.workbench_starterkit)



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer%20Documentation.md) > [Python Code](Category_Python%20Code.md) > Workbench creation/it
