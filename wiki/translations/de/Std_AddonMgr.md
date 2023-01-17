---
- GuiCommand:/de
   Name:Std AddonMgr
   Name/de:Std AddonManager
   MenuLocation:Werkzeuge → Addon-Manager
   Workbenches:Alle
   Version:0.17
   SeeAlso:[Externe Arbeitsbereiche](External_workbenches/de.md), [Makros](Macros/de.md)
---

# Std AddonMgr/de



## Beschreibung

Der Befehl **Std Addon-Manager** öffnet den Addon-Manager. Mit dem Addon-Manager können [externe Arbeitsbereiche](external_workbenches/de.md), [Makros](macros/de.md), und [Voreinstellungspakete](Preference_Packs/de.md), die durch die FreeCAD-Gemeinschaft bereitgestellt werden, installiert und verwaltet werden. Standardmäßig stammen die verfügbaren Erweiterungen aus zwei Quellen, [(GitHub) FreeCAD-Addons](https://github.com/FreeCAD/FreeCAD-addons/) und von der Seite [Makrorezepte](Macros_recipes/de.md). Wenn GitPython und git auf dem eigenen System installiert sind, werden zusätzliche Makros von [(GitHub) FreeCAD-Makros](https://github.com/FreeCAD/FreeCAD-macros/) geladen. Benutzerdefinierte Quellen können in den Voreinstellungen des [Addon-Managers](Preferences_Editor/de#Addon-Manager.md) hinzugefügt werden.

Aufgrund von Änderungen an der GitHub-Plattform im Jahr 2020 funktioniert der Addon-Manager nicht mehr, wenn man die FreeCAD-Version 0.17 oder älter verwendet. Man muss auf die Version [0.18.5](https://github.com/FreeCAD/FreeCAD/releases/tag/0.18.5) oder neuer aktualisieren. Alternativ könen die Erweiterungen auch manuell installiert werden, siehe [Hinweise](#Hinweise.md) unten.



## Anwendung

1.  Den Menüeintrag **Werkzeuge → <img src="images/Std_AddonMgr.svg" width=16px> Addon-Manager** auswählen.
2.  Wird der Addon-Manager zum ersten Mal verwendet, wird ein Dialogfeld geöffnet, das darauf hinweist, dass die Erweiterungen im Addon-Manager kein offizieller Bestandteil von FreeCAD sind. Es enthält auch mehrere Optionen, die mit der Verwendung von Daten durch den Addon-Manager zusammenhängen. Hat man diese Optionen den eigenen Vorlieben entsprechend eingestellt, drückt man die Schaltfläche **OK**, um zu bestätigen und fortzufahren.
3.  Das Dialogfeld Addon-Manager öffnet sich. Für weitere Informationen siehe [Optionen](#Optionen.md).
4.  Die Schaltfläche **<img src="images/Button_valid.svg" width=16px> Alles aktualisieren** funktioniert zurzeit nicht.
5.  Die Schaltfläche **<img src="images/Process-stop.svg" width=16px> Schließen** drücken, um das Dialogfeld zu schließen.
6.  Wenn ein Arbeitsbereich installiert oder aktualisiert wurde, wird ein neues Dialogfeld geöffnet, das darauf hinweist, dass FreeCAD neu gestartet werden muss, damit die Änderungen wirksam werden.



## Optionen

<img alt="" src=images/AddonManager_Main.png  style="width:600px;">

1.  Der Addon-Manager stellt zwei Layouts zur Verfügung: \"Schmal\" and \"Erweitert\". In der \"schmalen\" Ansicht füllt eine Erweiterung eine einzelne Zeile und ihre Beschreibung wird gekürzt, um in den vorhandenen Platz zu passen. \"Erweitert\" stellt zusätzliche Einzelheiten dar, wie weiteren Beschreibungstext und auch Informationen für Bearbeiter, weitere Installationsdetails usw.
2.  Drei Arten von Erweiterungen werden unterstützt: [Arbeitsbereiche](external_workbenches/de.md), [Makros](macros/de.md), und [Voreinstellungspakete](Preference_Packs/de.md). Man kann wählen, ob nur eine Art angezeigt wird oder alle in einer einzigen Liste.
3.  Die Liste kann so eingegrenzt werden, dass sie nur installierte Pakete, nur Pakete mit erhältlichen Aktualisierungen oder nur Pakete, die noch nicht installiert wurden, enthält.
4.  Die Liste kann gefiltert werden durch die Suche nach Schlüsselwörtern in Benennung, Beschreibung und Kennzeichen (Beschreibung und Kennzeichnung müssen vom Addon-Entwickler in den Meta-Daten angegeben werden). Der Filter kann sogar ein regulärer Ausdruck sein, für eine präzise Steuerung des genauen Suchbegriffs.
5.  Die erweiterte Ansicht zeigt enthaltene Versionsinformationen, Beschreibungen, Informationen für Bearbeiter und Informationen zur Version der Installation für Pakete mit einer [Paket-Meta-Daten](Package_Metadata/de.md)-Datei (oder für Makros mit eingebetteten Meta-Daten).
6.  Die Addon-Daten werden lokal zwischengespeichert, mit einer variablen Häufigkeit der Aktualisierung des Zwischnspeichers, festgelegt in den Benutzereinstellungen.
7.  Zu jeder Zeit kann die manuelle Aktualisierung des lokalen Zwischenspeichers ausgewählt werden, um die neuesten verfügbaren Aktualisierungen für alle Erweiterungen anzuzeigen.
8.  Die Suche nach Aktualisierungen kann auf automatisch eingestellt sein oder manuell erfolgen durch einen Klick auf eine Schaltfläche (festgelegt in den Benutzereinstellungen). Wenn GitPython und git auf dem eigenen System installiert sind, werden die Aktualisierungsinformationen unter Verwendung von git abgeholt. Wenn nicht, werden Informationen zu Aktualisierungen aus allen vorhandenen Meta-Daten-Datein ausgelesen.

Klickt man in dieser Ansicht auf eine Erweiterung, wird eine Seite mit Einzelheiten zu dieser Erweiterung geöffnet:

<img alt="" src=images/AddonManager_Details.png  style="width:600px;">

Diese Seite mit Einzelheiten zeigt Schaltflächen, die es erlauben Erweiterungen zu installieren, zu deinstallieren, zu aktualisieren und zeitweise zu deaktivieren. Sie listet die aktuell installierten Versionen mit dem Installationsdatum und ob es sich um die neueste verfügbare Version handelt. Darunter befindet sich ein eingebettetes Webbrowser-Fenster, das die README-Seite der Erweiterung anzeigt (für Arbeitsbereiche und Voreinstellungspakete), oder die Wiki-Seite (für Makros).



## Einstellungen

Die Einstellungen für den Addon-Manager findet man im [Voreinstellungseditor](Preferences_Editor/de#Addon-Manager.md). {{Version/de|0.20}}



## Hinweise

-   Die Verwendung von Erweiterungen ist nicht auf die FreeCAD-Version beschränkt, mit der sie installiert wurden. Sie können auch in jeder anderen FreeCAD-Version verwenden, die von der Erweiterung unterstützt wird, die möglicherweise auf dem eigenen System vorhanden ist.
-   Die im Addon-Manager verfügbaren Erweiterungen sind nicht Teil des offiziellen FreeCAD-Programms und werden vom FreeCAD-Kernentwicklungsteam nicht unterstützt. Man solltet die bereitgestellten Informationen sorgfältig lesen, um sicherzustellen, daß man weiß, was man installiert.
-   Fehlerberichte und Anfragen für neue Funktionen sollten direkt an den Ersteller der Erweiterung gerichtet werden, durch Besuch der angegebene Webseite. Viele Erweiterungsentwickler sind regelmäßige Nutzer des [FreeCAD-Forums](https://forum.freecadweb.org), und können dort auch kontaktiert werden.
-   Wenn das [GitPython](https://github.com/gitpython-developers/GitPython)-Paket auf dem eigenen Computer installiert ist, wird der Addon-Manager davon Gebrauch machen, was das Herunterladen beschleunigt.
-   Die Erweiterungen können auch manuell installiert werden. Siehe [Wie man zusätzliche Arbeitsbereiche installiert](How_to_install_additional_workbenches/de.md) und [Wie man Makros installiert](How_to_install_macros/de.md).




<div class="mw-translate-fuzzy">

## Informationen für Entwickler 


</div>

Siehe [Erweiterung](Addon/de#Informationen_für_Entwickler.md).

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





{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std AddonMgr/de
