# Addon/de
{{TOCright}}



## Einführung

In FreeCAD und dieser Dokumentation ist ein [Addon](addon/de.md) (eine Erweiterung oder Ergänzung) eine beliebige Komponente, die nicht Teil der Basisinstallation ist, die aber dem System durch bestimmte Methoden hinzugefügt werden kann.



## Verschiedene Typen 

Es gibt drei Arten von Erweiterungen:

-   [Makros](Macros/de.md): Kurzer Abschnitt von [Python](Python/de.md)-Kode, der ein neues Werkzeug oder eine neue Funktionalität in einer einzelnen Datei mit der Endung `.FCMacro` bereitstellt.
-   [Arbeitsbereiche](External_workbenches/de.md): Sammlungen von Python-Dateien, die zusammengehörige [GUI-Befehle](Gui_Command/de.md) (Werkzeuge) bereitstellen, die sich auf ein bestimmtes Thema beziehen, z.B. Werkzeuge für den Entwurf von Schränken, Werkzeuge für die Arbeit mit Architektur oder Werkzeuge für den Entwurf von Booten usw. Diese Arbeitsbereiche definieren normalerweise neue Werkzeugleisten, in denen [Befehle](Gui_Command/de.md) als Schaltflächen platziert werden.
-   [Voreinstellungspakete](Preference_Packs.md): Verteilbare Sammlung von Benutzervoreinstellungen. {{Version/de|0.20}}

## Installation

Beginnend mit FreeCAD 0.17 wird zur Installation von Erweiterungen die Verwendung des <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Addon-Managers](Std_AddonMgr/de.md) empfohlen.

Aber für Makros und Arbeitsbereiche ist auch eine manuelle Installation möglich:

-   [Wie Makros installiert werden](How_to_install_macros/de.md)
-   [Weitere Arbeitsbereiche installieren](Installing_more_workbenches/de.md)



## Informationen für Entwickler 

Hat man ein Makro oder einen Arbeitsbereich entwickelt und möchte es/ihn im Addon-Manager aufgelistet sehen, kann man auf den Seiten [FreeCAD-addons](https://github.com/FreeCAD/FreeCAD-addons/) und [FreeCAD-macros](https://github.com/FreeCAD/FreeCAD-macros/) (beide engl.) lesen, wie es funktioniert. Wird ein Makro zur Seite [Makrorezepte](Macros_recipes/de.md) hinzugefügt, muss nichts weiter getan werden, es wird automatisch vom Addon-Manager gefunden.

Siehe auch:

-   [Programmpaket eines Python-Arbeitsbereiches herausgeben](Workbench_creation/de#Programmpaket_(distribution).md)
-   [Programmpaket eines C++ -Arbeitsbereiches herausgeben](Workbench_creation/de#Distribution.md)



---
![](images/Button_right.svg) [documentation index](../README.md) > [Addons](Category_Addons.md) > Addon/de
