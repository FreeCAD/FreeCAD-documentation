# Addon/de



## Einführung

In FreeCAD und dieser Dokumentation ist eine [Erweiterung](addon/de.md) eine beliebige Komponente, die nicht Teil der Basisinstallation ist, die aber dem System durch bestimmte Methoden hinzugefügt werden kann.

## Verschiedene Typen 

Es gibt zwei Arten von Erweiterungen:

-   [Makros](Macros/de.md): kurze Schnipsel von [Python](Python/de.md) Code, der ein neues Werkzeug oder eine neue Funktionalität in einer einzigen Datei mit der Endung `.FCMacro` bereitstellt.
-   Modul: eine einzelne Python Quelldatei oder eine Sammlung von Python Dateien, die die Software in irgendeiner Weise erweitert. Module definieren nicht notwendigerweise einen grafischen \"Arbeitsbereich\", können aber eine unterstützende Funktion bieten, z.B. eine Bibliothek, die die Konvertierung von Formaten durchführt, oder Code, der die grafische [Oberfläche](interface/de.md) modifiziert.
-   [Arbeitsbereiche](External_workbenches/de.md): Sammlungen von Python Dateien, die verwandte [Gui Befehle](Gui_Command/de.md) (Werkzeuge), die sich auf ein bestimmtes Thema konzentrieren, z.B. Werkzeuge für den Entwurf von Schränken oder Werkzeuge für die Arbeit mit Architektur oder Werkzeuge für den Entwurf von Booten usw. Diese Arbeitsbereiche definieren normalerweise neue Werkzeugleisten, in denen [Befehle](Gui_Command/de.md) als Schaltflächen platziert werden.

Makros wie unter dem `Macro/` Benutzerverzeichnis installiert, während Module und Arbeitsbereiche unter dem `Mod/` Verzeichnis liegen. {{Code|lang=bash|code=
$HOME/.FreeCAD/Macro/
$HOME/.FreeCAD/Mod/
}}

Makros beginnen in der Regel als eine Möglichkeit, die Aufgabe, ein bestimmtes Objekt zu zeichnen oder zu bearbeiten, zu vereinfachen oder zu automatisieren. Wenn viele dieser Makros in einem Verzeichnis gesammelt werden und eine Struktur zur Verfügung gestellt wird, um diese Werkzeuge zu sammeln, dann kann das gesamte Verzeichnis als ein Arbeitsbereich verteilt werden.

Mit anderen Worten: Makros, Module und Arbeitsbereiche sind im Wesentlichen dasselbe, Stücke von Python Code, die die Basisinstallation erweitern. Makros sind in der Regel kurz und auf eine einzige Aufgabe konzentriert, Module stellen in der Regel neue Funktionen oder Schnittstellen zur Verfügung, und Arbeitsbereiche sind Sammlungen von Werkzeugen (Schaltflächen, Menüs) und grafischen Oberflächen zur Ausführung verwandter Aufgaben.

Wenn ein Arbeitsbereich ausreichend entwickelt und gut dokumentiert ist, wird er ggf. als einer der Basis [Arbeitsbereiche](workbenches/de.md) in FreeCAD eingefügt.

## Installation

Beginnend mit FreeCAD 0.17 ist der empfohlene Weg zur Installation von Erweiterungen mit dem <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Erweiterungsverwalter](Std_AddonMgr/de.md).

Trotzdem ist manuelle Installation weiterhin möglich.

-   [Wie Makros installiert werden](How_to_install_macros/de.md)
-   [Weitere Arbeitsbereiche installieren](Installing_more_workbenches/de.md)




[Category:Addons](Category:Addons.md)
