---
- GuiCommand:/it
   Name:Std_AddonMgr
   Name/it:Addon manager
   MenuLocation:Strumenti → Addon manager
   Workbenches:Tutti
   Version:0.17
   SeeAlso:[Macro](Macros/it.md), [Ambienti complementari](External_workbenches/it.md)
---

# Std AddonMgr/it



## Descrizione


<div class="mw-translate-fuzzy">

Il comando **Std AddonMgr** apre Addon manager. Con il gestore degli addon è possibile installare e gestire gli [ambienti esterni](external_workbenches/it.md) e le [macro](macros/it.md) forniti dalla comunità di FreeCAD. Gli ambienti e le macro disponibili sono presi da due repository, [FreeCAD-addons](https://github.com/FreeCAD/FreeCAD-addons/) e [FreeCAD-macros](https://github.com/FreeCAD/FreeCAD-macros/), e dalla pagina [Raccolta di macro](Macros_recipes/it.md).


</div>

Due to changes to the GitHub platform in the year 2020 the Addon manager no longer works if you use FreeCAD version 0.17 or earlier. You need to upgrade to version [0.18.5](https://github.com/FreeCAD/FreeCAD/releases/tag/0.18.5) or later. Alternatively you can install addons manually, see [Notes](#Notes.md) below.



## Utilizzo


<div class="mw-translate-fuzzy">

1.  Selezionare l\'opzione **Strumenti → <img src="images/Std_AddonMgr.svg" width=16px> Addon manager** dal menu principale.
2.  La prima volta che si usa il gestore Addon si apre una finestra di dialogo che avverte che i componenti aggiuntivi nel gestore Addon non fanno ufficialmente parte di FreeCAD. Premere il pulsante **OK** per confermare e continuare.
3.  Viene visualizzata la finestra di dialogo Addon manager. Per ulteriori informazioni, vedere le [Opzioni](Std_AddonMgr/it#Opzioni.md).
4.  Il pulsante **<img src="images/Button_valid.svg" width=16px> Aggiorna tutto** non funziona al momento.
5.  Premere il pulsante **<img src="images/Process-stop.svg" width=16px> Chiudi** per chiudere la finestra di dialogo.
6.  Se è stato installato o aggiornato un ambiente di lavoro, si aprirà una nuova finestra di dialogo per informare che si deve riavviare FreeCAD affinché le modifiche abbiano effetto.


</div>



## Opzioni

<img alt="" src=images/AddonManager_Main.png  style="width:600px;">

1.  The Addon manager provides two view layouts: \"Condensed\" and \"Expanded\". In \"Condensed\" view, each addon takes a single line, and its description is truncated to fit the available space. \"Expanded\" shows additional details, including more of the description text as well as maintainer information, more installation details, etc.
2.  Three different types of addons are supported: [workbenches](external_workbenches.md), [macros](macros.md), and [preference packs](Preference_Packs.md). You can choose to show just one type, or all of them in a single list.
3.  The list can be limited to show just installed packages, just packages with available updates, or just packages that are not yet installed.
4.  The list can be filtered, searching for a keyword in the title, description, and tags (description and tags must be specified by the addon developer in their addon\'s metadata). The filter can even be a regular expression, for fine-grained control of the exact search term.
5.  The expanded view shows available version information, description, maintainer information, and installation version information, for packages that provide a [package metadata](Package_Metadata.md) file (or for macros with embedded metadata).
6.  Addon data is cached locally, with a variable cache update frequency set in the user preferences.
7.  At any time you can choose to manually update your local cache to see the latest updates available for each addon.
8.  Update checks may be set up to be automatic, or done manually via a button click (configured in user preferences). If GitPython and git are installed on your system then update information is fetched using git. If not, then update information is obtained from any present metadata file.

Clicking on an addon in this view brings up the addon\'s Details page:

<img alt="" src=images/AddonManager_Details.png  style="width:600px;">

The details page shows buttons allowing installing, uninstalling, updating, and temporarily disabling an addon. For installed addons it lists the currently installed version and the installation date, and whether that is the most recent version available. Below is an embedded web browser window showing the addon\'s README page (for workbenches and preference packs), or Wiki page (for macros).

## Preferences

The preferences for the Addon manager can be found in the [Preferences Editor](Preferences_Editor#Addon_Manager.md). <small>(v0.20)</small> 



## Note


<div class="mw-translate-fuzzy">

-   I componenti aggiuntivi disponibili in Addon manager non fanno parte del programma ufficiale FreeCAD e non sono supportati dal team di sviluppo principale di FreeCAD. Bisogna leggere attentamente le informazioni fornite per assicurarsi di sapere cosa si sta installando.
-   Segnalazioni di bug e richieste di funzionalità devono essere inviate direttamente al creatore del componente aggiuntivo visitando il sito Web indicato. Molti sviluppatori di componenti aggiuntivi sono utenti regolari del [FreeCAD forum](https://forum.freecadweb.org), e possono anche essere contattato lì.
-   Se sul computer è installato il pacchetto [GitPython](https://github.com/gitpython-developers/GitPython), il gestore Addon lo utilizza, rendendo i download più veloci.
-   È inoltre possibile installare i componenti aggiuntivi manualmente. Vedere [Come installare gli ambienti aggiuntivi](How_to_install_additional_workbenches/it.md) and [Come installare le macro](How_to_install_macros/it.md).


</div>




<div class="mw-translate-fuzzy">

## Informazioni per gli sviluppatori 


</div>

See [Addon](Addon#Information_for_developers.md).

## Scripting


<small>(v1.0)</small> 

Some features of the Addon manager are designed for access via FreeCAD\'s Python API. In particular an addon can be installed, updated, and removed via the Python interface. Most uses of this API require you to create an object with at least three attributes: {{Incode|name}}, {{Incode|branch}} and {{Incode|url}}. For example:


```python
class MyAddonClass:
    def __init__(self):
        self.name = "TestAddon"
        self.url = "https://github.com/Me/MyTestAddon"
        self.branch = "main"
my_addon = MyAddonClass()
```

Your object {{Incode|my_addon}} is now ready for use with the Addon manager API.

### Commandline (non-GUI) use 

If your code needs to install or update an addon synchronously (e.g. without a GUI) the code can be very simple:


```python
from addonmanager_installer import AddonInstaller
installer = AddonInstaller(my_addon)
installer.run()
```

Note that this code blocks until complete, so you shouldn\'t run it on the main GUI thread. To the Addon manager, \"install\" and \"update\" are the same call: if this addon is already installed, and git is available, it will be updated via \"git pull\". If it is not installed, or was installed via a non-git installation method, it is downloaded from scratch (using git if available).

To uninstall, use:


```python
from addonmanager_uninstaller import AddonUninstaller
uninstaller = AddonUninstaller(my_addon)
uninstaller.run()
```

### GUI use 

If you plan on your code running in a GUI, or supporting running in the full version of FreeCAD, it\'s best to run your installation in a separate non-GUI thread, so the GUI remains responsive. To do this, first check to see if the GUI is running, and if it is, spawn a {{Incode|QThread}} (don\'t try to spawn a {{Incode|QThread}} if the GUI is not up: they require an active event loop to function).


```python
from PySide import QtCore
from addonmanager_installer import AddonInstaller

worker_thread = QtCore.QThread()
installer = AddonInstaller(my_addon)
installer.moveToThread(worker_thread)
installer.success.connect(installation_succeeded)
installer.failure.connect(installation_failed)
installer.finished.connect(worker_thread.quit)
worker_thread.started.connect(installer.run)
worker_thread.start() # Returns immediately
```

Then define the functions {{Incode|installation_succeeded}} and {{Incode|installation_failed}} to be run in each case. For uninstallation you can use the same technique, though it is usually much faster and will not block the GUI for very long, so in general it\'s safe to use the uninstaller directly, as shown above.


<div class="mw-translate-fuzzy">





</div>


{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std AddonMgr/it
