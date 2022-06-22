# Addon/de
{{TOCright}}

## Einführung

In FreeCAD und dieser Dokumentation ist eine [Erweiterung](addon/de.md) eine beliebige Komponente, die nicht Teil der Basisinstallation ist, die aber dem System durch bestimmte Methoden hinzugefügt werden kann.

## Verschiedene Typen 

Es gibt drei Arten von Erweiterungen   *

-   [Makros](Macros/de.md)   * Kurzer Abschnitt von [Python](Python/de.md)-Kode, der ein neues Werkzeug oder eine neue Funktionalität in einer einzelnen Datei mit der Endung `.FCMacro` bereitstellt.
-   [Arbeitsbereiche](External_workbenches/de.md)   * Sammlungen von Python-Dateien, die zusammengehörige [GUI-Befehle](Gui_Command/de.md) (Werkzeuge) bereitstellen, die sich auf ein bestimmtes Thema beziehen, z.B. Werkzeuge für den Entwurf von Schränken, Werkzeuge für die Arbeit mit Architektur oder Werkzeuge für den Entwurf von Booten usw. Diese Arbeitsbereiche definieren normalerweise neue Werkzeugleisten, in denen [Befehle](Gui_Command/de.md) als Schaltflächen platziert werden.
-   [Voreinstellungspakete](Preference_Packs.md)   * Verteilbare Sammlung von Benutzervoreinstellungen. {{Version/de|0.20}}

## Installation

Beginnend mit FreeCAD 0.17 wird zur Installation von Erweiterungen die Verwendung des <img alt="" src=images/Std_AddonMgr.svg  style="width   *24px;"> [Addon-Managers](Std_AddonMgr/de.md) empfohlen.

Aber für Makros und Arbeitsbereiche ist auch eine manuelle Installation möglich   *

-   [Wie Makros installiert werden](How_to_install_macros/de.md)
-   [Weitere Arbeitsbereiche installieren](Installing_more_workbenches/de.md)

## Informationen für Entwickler 

If you have developed a macro or workbench, and want to see it included in the Addon manager, read how to do so on the repository pages   * ([FreeCAD-addons](https   *//github.com/FreeCAD/FreeCAD-addons/) and [FreeCAD-macros](https   *//github.com/FreeCAD/FreeCAD-macros/)). If you add your macro to the [Macros recipes](Macros_recipes.md) page, there is nothing else to do, it will automatically be picked up by the Addon manager.

### Python-Arbeitsbereiche 

For Python workbenches, you don\'t need any specific approval to have your workbench added to the Addon Manager. In addition, because your Addon is outside the FreeCAD source code, you can choose the license you want. If you request for your workbench to be added to the Addon Manager\'s default list (we will not add any new workbench without a request from its authors), either by asking so on the forum or by opening an issue on the [FreeCAD-addons](https   *//github.com/FreeCAD/FreeCAD-addons/) repository, your code will stay on your own git repository, we will just add it as a submodule to the [FreeCAD-addons](https   *//github.com/FreeCAD/FreeCAD-addons/) repository. Of course, before adding your workbench, we will take a look at it and make sure there is nothing potentially problematic with it. For more details about structuring your Addon, including information about metadata used by the Addon Manager, see [Workbench creation](Workbench_creation.md).

### C++Arbeitsbereiche

If you develop a workbench in C++, it cannot be run directly by users and must be compiled first. You then have two options, either you provide precompiled versions of your workbench yourself, for the different operating systems, or you should request to have your code merged into the FreeCAD source code. For that, you should use the LGPL license (or a fully compatible license like MIT or BSD), and you must present your new tools to the community in the [FreeCAD forum](https   *//forum.freecadweb.org) for review. Once your code has been tested and approved, you should fork the FreeCAD repository, if not done yet, create a new branch, push your code to it, and open a pull request so that your branch is merged into the main repository.




[Category   *Addons](Category_Addons.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Addons](Category_Addons.md) > Addon/de
