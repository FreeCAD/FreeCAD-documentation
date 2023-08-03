---
 GuiCommand:
   Name/ru: Менеджер дополнений
   MenuLocation: Инструменты , Менеджер дополнений
   Workbenches: All
   Version: 0.17
   SeeAlso: External_workbenches/ru, Macros/ru
---

# Std AddonMgr/ru



## Описание


<div class="mw-translate-fuzzy">

Команда **Std AddonMgr** открывает Менеджер дополнений. С его помощью Вы можете устанавливать и управлять [сторонними верстаками](external_workbenches/ru.md) и [макросами](macros/ru.md), предоставляемыми сообществом FreeCAD. Доступные верстаки и макросы берутся из двух репозиториев, [FreeCAD-addons](https://github.com/FreeCAD/FreeCAD-addons/) и [FreeCAD-macros](https://github.com/FreeCAD/FreeCAD-macros/), а так же страницы [рецепты макросов](Macros_recipes/ru.md).


</div>

Из-за изменений в платформе GitHub в 2020 году Менеджер дополнений больше не работает в FreeCAD 0.17 и в более ранних версиях. Вам нужно перейти на версию [0.18.5](https://github.com/freecad/freecad/releases/tag/0.18.5) или более позднюю. В качестве альтернативы вы можете устанавливать дополнения вручную, см. [Примечания](#Примечания.md) ниже.



## Применение

1.  Select the **Tools → <img src="images/Std_AddonMgr.svg" width=16px> Addon manager** option from the menu.
2.  If you are using the Addon manager for the first time, a dialog box will open warning you that the addons in the Addon manager are not officially part of FreeCAD. It also presents several options related to the Addon manager\'s data usage. Adjust those options to your liking and press the **OK** button to confirm and continue.
3.  The Addon manager dialog box opens. For more information see [Options](#Options.md).
4.  If you have installed or updated a workbench a new dialog box will open informing you that you have to restart FreeCAD for the changes to take effect.



## Опции

<img alt="" src=images/AddonManager_Main.png  style="width:600px;">

1.  The Addon manager provides two view layouts: \"Condensed\" and \"Expanded\". In \"Condensed\" view, each addon takes a single line, and its description is truncated to fit the available space. \"Expanded\" shows additional details, including more of the description text as well as maintainer information, more installation details, etc.
2.  Three different types of addons are supported: [workbenches](external_workbenches.md), [macros](macros.md), and [preference packs](Preference_Packs.md). You can choose to show just one type, or all of them in a single list.
3.  The list can be limited to show just installed packages, just packages with available updates, or just packages that are not yet installed.
4.  The list can be filtered, searching for a keyword in the title, description, and tags (description and tags must be specified by the addon developer in their addon\'s metadata). The filter can even be a regular expression, for fine-grained control of the exact search term.
5.  The expanded view shows available version information, description, maintainer information, and installation version information, for packages that provide a [package metadata](Package_Metadata.md) file (or for macros with embedded metadata).
6.  Addon data is cached locally, with a variable cache update frequency set in the user preferences.
7.  At any time you can choose to manually update your local cache to see the latest updates available for each addon.
8.  Update checks may be set up to be automatic, or done manually via a button click (configured in user preferences). If GitPython and git are installed on your system then update information is fetched using git. If not, then update information is obtained from any present metadata file.

При нажатии на блок с кратким описанием дополнения в представленном окне, открывается страница с более детальными сведениями о дополнении:

<img alt="" src=images/AddonManager_Details.png  style="width:600px;">

На странице детального описания дополнения отображаются кнопки, позволяющие устанавливать, удалять, обновлять и временно отключать дополнение. Для уже установленных дополнений в нем указана текущая установленная версия и дата установки, а также является ли это самой последней доступной версией. Ниже показано встроенное окно веб-браузера, показывающее страницу README дополнения (для верстаков и пакетов настроек) или страницу Wiki (для макросов).



## Настройки

The preferences for the Addon manager can be found in the [Preferences Editor](Preferences_Editor#Addon_Manager.md). <small>(v0.20)</small> 



## Примечания

-   The use of addons is not restricted to the FreeCAD version they were installed from. You will also be able to use them in any other FreeCAD version, supported by the addon, that you may have on your system.
-   The addons available in the Addon manager are not part of the official FreeCAD program and are not supported by the core FreeCAD development team. You should read the provided information carefully to make sure you know what you are installing.
-   Bug reports and feature requests should be made directly to the creator of the addon by visiting the indicated website. Many addon developers are regular users of the [FreeCAD forum](https://forum.freecadweb.org), and can also be contacted there.
-   If the [GitPython](https://github.com/gitpython-developers/GitPython) package is installed on your computer the Addon manager will use it, making downloads faster.
-   You can also install addons manually. See [How to install additional workbenches](How_to_install_additional_workbenches.md) and [How to install macros](How_to_install_macros.md).



## Информация для разработчиков дополнений 

См. [Дополнения](Addon/ru#Информация_для_разработчиков.md).



## Программирование


<div class="mw-translate-fuzzy">


{{Version/ru|1.0}}


</div>

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

Для удаления (деинсталляции), используйте:


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





{{Std Base navi

}}



---
⏵ [documentation index](../README.md) > Std AddonMgr/ru
