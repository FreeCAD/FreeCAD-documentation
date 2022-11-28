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

See also   *

-   [Distribution of a Python workbench](Workbench_creation#Distribution.md)
-   [Distribution of a C++ workbench](Workbench_creation#Distribution_2.md)




[Category   *Addons](Category_Addons.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Addons](Category_Addons.md) > Addon/de
